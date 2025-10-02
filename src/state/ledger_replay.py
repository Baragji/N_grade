"""Session ledger replay ensuring deterministic state recovery."""
from __future__ import annotations

import hashlib
import json
import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, Iterable, List, Sequence

from sqlalchemy import Column, DateTime, Integer, LargeBinary, MetaData, String, Table, insert, select, update
from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm import Session, sessionmaker

LOGGER = logging.getLogger(__name__)


@dataclass
class LedgerEntry:
    """Represents a single ledger entry stored in PostgreSQL."""

    id: int
    session_id: str
    payload: bytes
    checksum: str
    created_at: datetime
    replayed: bool

    def as_dict(self) -> Dict[str, object]:
        """Convert the entry into a JSON-serialisable dictionary."""

        return {
            "id": self.id,
            "session_id": self.session_id,
            "payload": json.loads(self.payload.decode("utf-8")),
            "checksum": self.checksum,
            "created_at": self.created_at.isoformat(),
            "replayed": self.replayed,
        }


class LedgerReplayError(RuntimeError):
    """Raised when the ledger replay cannot complete safely."""

class SessionLedger:
    """Ledger abstraction used by replay orchestration."""

    def __init__(self, engine: Engine) -> None:
        self._engine = engine
        self._metadata = MetaData()
        self._table = Table(
            "session_ledger",
            self._metadata,
            Column("id", Integer, primary_key=True),
            Column("session_id", String(64), index=True, nullable=False),
            Column("payload", LargeBinary, nullable=False),
            Column("checksum", String(64), nullable=False),
            Column("replayed", Integer, nullable=False, default=0),
            Column("created_at", DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False),
        )
        self._metadata.create_all(self._engine)
        self._session_factory = sessionmaker(bind=self._engine, expire_on_commit=False)

    @property
    def table(self) -> Table:
        """Expose the underlying table for external transactional use."""

        return self._table

    def append(self, session_id: str, payload: Dict[str, object]) -> LedgerEntry:
        """Append a new ledger entry, computing checksum for integrity."""

        encoded_json = json.dumps(payload, sort_keys=True).encode("utf-8")
        checksum = hashlib.sha256(encoded_json).hexdigest()
        encoded = encoded_json
        timestamp = datetime.now(timezone.utc)
        with self._session_factory() as session:
            with session.begin():
                row = session.execute(
                    insert(self._table)
                    .values(
                        session_id=session_id,
                        payload=encoded,
                        checksum=checksum,
                        created_at=timestamp,
                        replayed=0,
                    )
                    .returning(self._table)
                ).fetchone()
            session.commit()
        return LedgerEntry(
            id=row.id,
            session_id=session_id,
            payload=encoded,
            checksum=checksum,
            created_at=timestamp,
            replayed=False,
        )

    def fetch_entries(self, session_id: str) -> List[LedgerEntry]:
        """Load ledger entries for a session ordered by creation time."""

        with self._session_factory() as session:
            rows = session.execute(
                select(self._table).where(self._table.c.session_id == session_id)
            ).fetchall()
        ordered = sorted(rows, key=lambda row: row.created_at)
        return [
            LedgerEntry(
                id=row.id,
                session_id=row.session_id,
                payload=row.payload,
                checksum=row.checksum,
                replayed=bool(row.replayed),
                created_at=row.created_at,
            )
            for row in ordered
        ]

    def mark_replayed(self, entry_ids: Sequence[int]) -> None:
        """Mark ledger entries as replayed in a single transaction."""

        if not entry_ids:
            return
        with self._session_factory() as session:
            with session.begin():
                session.execute(
                    update(self._table)
                    .where(self._table.c.id.in_(entry_ids))
                    .values(replayed=1)
                )
            session.commit()


def _validate_checksum(entry: LedgerEntry) -> None:
    """Ensure the stored checksum matches the payload contents."""

    expected = hashlib.sha256(entry.payload).hexdigest()
    if expected != entry.checksum:
        raise LedgerReplayError(f"Checksum mismatch for entry {entry.id}")


def validate_entry(entry: LedgerEntry) -> None:
    """Ensure ledger entries have not been replayed and are intact."""

    if entry.replayed:
        raise LedgerReplayError(f"Ledger entry {entry.id} already replayed")
    _validate_checksum(entry)


def deserialize_payload(entry: LedgerEntry) -> Dict[str, object]:
    """Convert payload from bytes to dictionary."""

    return json.loads(entry.payload.decode("utf-8"))


def apply_payload(state_repo, session_id: str, payload: Dict[str, object]) -> None:
    """Apply payload into the state repository."""

    state_repo.save(session_id, payload)


def _replay_entries(entries: Sequence[LedgerEntry], state_repo, session_id: str) -> List[LedgerEntry]:
    """Replay ordered entries handling idempotency and integrity validation."""

    applied_entries: List[LedgerEntry] = []
    for entry in entries:
        validate_entry(entry)
        payload = deserialize_payload(entry)
        apply_payload(state_repo, session_id, payload)
        applied_entries.append(entry)
    return applied_entries


def replay(session_ledger: SessionLedger, state_repo, session_id: str) -> List[LedgerEntry]:
    """Replay ledger entries in chronological order and persist state."""

    try:
        entries = session_ledger.fetch_entries(session_id)
    except (OperationalError, IntegrityError) as exc:
        raise LedgerReplayError(f"Failed to load ledger entries for {session_id}") from exc

    ordered_entries = sorted(entries, key=lambda entry: entry.created_at)
    applied_entries = _replay_entries(ordered_entries, state_repo, session_id)
    session_ledger.mark_replayed([entry.id for entry in applied_entries])
    LOGGER.info("Replayed %s entries for %s", len(applied_entries), session_id)
    return applied_entries


def replay_batch(session_ledger: SessionLedger, state_repo, session_ids: Iterable[str]) -> Dict[str, List[Dict[str, object]]]:
    """Replay multiple sessions and summarise results."""

    summary: Dict[str, List[Dict[str, object]]] = {"replayed": [], "skipped": []}
    for session_id in session_ids:
        try:
            results = replay(session_ledger, state_repo, session_id)
        except LedgerReplayError as exc:
            LOGGER.warning("Skipping session %s due to error: %s", session_id, exc)
            summary["skipped"].append({"session_id": session_id, "reason": str(exc)})
            continue
        summary["replayed"].append({"session_id": session_id, "count": len(results)})
    return summary


def ensure_idempotency(entries: Sequence[LedgerEntry]) -> None:
    """Check that the entries being replayed have not been replayed previously."""

    for entry in entries:
        if entry.replayed:
            raise LedgerReplayError(f"Entry {entry.id} marked as replayed; aborting")


def commit_replay(session: Session, ledger: SessionLedger, entries: Sequence[LedgerEntry]) -> None:
    """Persist replay status using an external SQLAlchemy session."""

    if not entries:
        return
    ids = [entry.id for entry in entries]
    with session.begin():
        session.execute(
            update(ledger.table)
            .where(ledger.table.c.id.in_(ids))
            .values(replayed=1)
        )
    session.commit()


__all__ = [
    "LedgerEntry",
    "SessionLedger",
    "LedgerReplayError",
    "validate_entry",
    "deserialize_payload",
    "apply_payload",
    "replay",
    "replay_batch",
    "ensure_idempotency",
    "commit_replay",
]
