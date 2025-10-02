"""Distributed state repository with Redis caching and PostgreSQL durability."""
from __future__ import annotations

import hashlib
import json
import logging
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any, Dict, Optional

from redis import Redis
from sqlalchemy import Column, DateTime, Integer, LargeBinary, MetaData, String, Table, select, update
from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, sessionmaker

LOGGER = logging.getLogger(__name__)


@dataclass
class StateRecord:
    """Representation of a persisted session state."""

    session_id: str
    payload: Dict[str, Any]
    payload_hash: str
    version: int
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_row(cls, row: Any) -> "StateRecord":
        """Instantiate a record from a SQLAlchemy row."""

        return cls(
            session_id=row.session_id,
            payload=json.loads(row.payload.decode("utf-8")),
            payload_hash=row.payload_hash,
            version=row.version,
            created_at=row.created_at,
            updated_at=row.updated_at,
        )


class DistributedStateRepository:
    """Repository coordinating Redis cache and PostgreSQL persistence."""

    def __init__(
        self,
        redis_client: Redis,
        engine: Engine,
        cache_ttl_seconds: int = 60,
    ) -> None:
        self._redis = redis_client
        self._engine = engine
        self._cache_ttl = cache_ttl_seconds
        self._metadata = MetaData()
        self._table = Table(
            "session_state",
            self._metadata,
            Column("session_id", String(64), primary_key=True),
            Column("payload", LargeBinary, nullable=False),
            Column("payload_hash", String(64), nullable=False),
            Column("version", Integer, nullable=False, default=1),
            Column("created_at", DateTime(timezone=True), nullable=False, default=datetime.utcnow),
            Column("updated_at", DateTime(timezone=True), nullable=False, default=datetime.utcnow),
        )
        self._session_factory = sessionmaker(bind=self._engine)

    def _hash_payload(self, payload: Dict[str, Any]) -> str:
        """Return a deterministic SHA-256 hash of the payload."""

        encoded = json.dumps(payload, sort_keys=True).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()

    def _cache_key(self, session_id: str) -> str:
        """Build the Redis cache key for the provided session."""

        return f"state:{session_id}"

    def _cache_record(self, session_id: str, record: StateRecord) -> None:
        """Write a record to the Redis cache with TTL enforcement."""

        key = self._cache_key(session_id)
        payload = json.dumps({
            "payload": record.payload,
            "hash": record.payload_hash,
            "version": record.version,
            "updated_at": record.updated_at.isoformat(),
        })
        self._redis.setex(key, timedelta(seconds=self._cache_ttl), payload)

    def _load_from_cache(self, session_id: str) -> Optional[StateRecord]:
        """Attempt to load a record from Redis if present."""

        cached = self._redis.get(self._cache_key(session_id))
        if not cached:
            return None
        decoded = json.loads(cached.decode("utf-8"))
        return StateRecord(
            session_id=session_id,
            payload=decoded["payload"],
            payload_hash=decoded["hash"],
            version=int(decoded["version"]),
            created_at=datetime.fromisoformat(decoded["updated_at"]),
            updated_at=datetime.fromisoformat(decoded["updated_at"]),
        )

    def save(self, session_id: str, payload: Dict[str, Any]) -> StateRecord:
        """Persist session payload ensuring integrity against tampering."""

        payload_hash = self._hash_payload(payload)
        encoded_payload = json.dumps(payload).encode("utf-8")

        with self._session_factory() as session:
            record = session.execute(select(self._table).where(self._table.c.session_id == session_id)).fetchone()
            timestamp = datetime.utcnow()
            if record:
                LOGGER.debug("Updating state for %s", session_id)
                current_hash = record.payload_hash
                if current_hash == payload_hash:
                    LOGGER.debug("No changes detected for %s; skipping commit", session_id)
                    cached = StateRecord.from_row(record)
                    self._cache_record(session_id, cached)
                    return cached
                session.execute(
                    update(self._table)
                    .where(self._table.c.session_id == session_id)
                    .values(
                        payload=encoded_payload,
                        payload_hash=payload_hash,
                        version=record.version + 1,
                        updated_at=timestamp,
                    )
                )
            else:
                LOGGER.debug("Creating new state row for %s", session_id)
                session.execute(
                    self._table.insert().values(
                        session_id=session_id,
                        payload=encoded_payload,
                        payload_hash=payload_hash,
                        version=1,
                        created_at=timestamp,
                        updated_at=timestamp,
                    )
                )
            try:
                session.commit()
            except IntegrityError as exc:
                session.rollback()
                LOGGER.error("Integrity violation when saving %s: %s", session_id, exc)
                raise

        record = StateRecord(
            session_id=session_id,
            payload=payload,
            payload_hash=payload_hash,
            version=1 if record is None else record.version + 1,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        self._cache_record(session_id, record)
        return record

    def get(self, session_id: str) -> Optional[StateRecord]:
        """Retrieve state, preferring Redis cache before database access."""

        cached = self._load_from_cache(session_id)
        if cached:
            return cached

        with self._session_factory() as session:
            row = session.execute(select(self._table).where(self._table.c.session_id == session_id)).fetchone()
            if not row:
                return None
            record = StateRecord.from_row(row)
            self._cache_record(session_id, record)
            return record

    def delete(self, session_id: str) -> None:
        """Remove state from both Redis and PostgreSQL."""

        self._redis.delete(self._cache_key(session_id))
        with self._session_factory() as session:
            session.execute(self._table.delete().where(self._table.c.session_id == session_id))
            session.commit()

    def validate_integrity(self, session_id: str) -> bool:
        """Validate persisted payload hash matches the cached copy."""

        record = self.get(session_id)
        if not record:
            return False
        expected_hash = self._hash_payload(record.payload)
        if expected_hash != record.payload_hash:
            LOGGER.warning("Integrity drift detected for %s", session_id)
            return False
        return True

    def hydrate(self, session_id: str) -> Dict[str, Any]:
        """Return payload while ensuring the cache is refreshed."""

        record = self.get(session_id)
        if not record:
            raise KeyError(f"Session {session_id} not found")
        self._cache_record(session_id, record)
        return record.payload

    def touch(self, session_id: str, ttl_extension: Optional[int] = None) -> None:
        """Extend cache lifetime for an active session."""

        ttl = ttl_extension or self._cache_ttl
        self._redis.expire(self._cache_key(session_id), ttl)

    def record_cache_latency(self, session_id: str, latency_ms: float) -> None:
        """Store latency metrics alongside the state payload."""

        key = f"state:latency:{session_id}"
        body = json.dumps({"latency_ms": latency_ms, "timestamp": datetime.utcnow().isoformat()})
        self._redis.setex(key, timedelta(minutes=5), body)

    def session_exists(self, session_id: str) -> bool:
        """Determine whether session state is present in cache or storage."""

        if self._redis.exists(self._cache_key(session_id)):
            return True
        with self._session_factory() as session:
            result = session.execute(select(self._table.c.session_id).where(self._table.c.session_id == session_id)).scalar()
            return result is not None

    def purge_stale(self, older_than: datetime) -> int:
        """Remove records that have not been updated since the threshold."""

        with self._session_factory() as session:
            rows = session.execute(
                self._table.delete().where(self._table.c.updated_at < older_than)
            )
            session.commit()
            return rows.rowcount or 0
