"""Session ledger replay ensuring deterministic state recovery."""
from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from datetime import datetime
from typing import Iterable, List, Sequence

from sqlalchemy import Column, DateTime, Integer, LargeBinary, MetaData, String, Table, select, update
from sqlalchemy.engine import Engine
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

    def as_dict(self) -> dict:
        """Convert the entry into a JSON-serialisable dictionary."""

        return {
            "id": self.id,
            "session_id": self.session_id,
            "payload": json.loads(self.payload.decode("utf-8")),
            "checksum": self.checksum,
            "created_at": self.created_at.isoformat(),
            "replayed": self.replayed,
        }


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
            Column("created_at", DateTime(timezone=True), default=datetime.utcnow, nullable=False),
        )
        self._session_factory = sessionmaker(bind=self._engine)

    @property
    def table(self) -> Table:
        """Expose the underlying table for external transactional use."""

        return self._table

    def fetch_entries(self, session_id: str) -> List[LedgerEntry]:
        """Load ledger entries for a session ordered by creation time."""

        with self._session_factory() as session:
            rows = session.execute(
                select(self._table).where(self._table.c.session_id == session_id)
            ).fetchall()
        ordered = sorted(rows, key=lambda row: row.created_at)
        return [LedgerEntry(
            id=row.id,
            session_id=row.session_id,
            payload=row.payload,
            checksum=row.checksum,
            replayed=bool(row.replayed),
            created_at=row.created_at,
        ) for row in ordered]

    def mark_replayed(self, entry_ids: Sequence[int]) -> None:
        """Mark ledger entries as replayed in a single transaction."""

        if not entry_ids:
            return
        with self._session_factory() as session:
            session.execute(
                update(self._table)
                .where(self._table.c.id.in_(entry_ids))
                .values(replayed=1)
            )
            session.commit()


def validate_entry(entry: LedgerEntry) -> None:
    """Ensure ledger entries have not been replayed and are intact."""

    if entry.replayed:
        raise ValueError(f"Ledger entry {entry.id} already replayed")
    if not entry.checksum:
        raise ValueError("Missing checksum on ledger entry")


def deserialize_payload(entry: LedgerEntry) -> dict:
    """Convert payload from bytes to dictionary."""

    return json.loads(entry.payload.decode("utf-8"))


def apply_payload(state_repo, session_id: str, payload: dict) -> None:
    """Apply payload into the state repository."""

    state_repo.save(session_id, payload)


def replay(session_ledger: SessionLedger, state_repo, session_id: str) -> List[LedgerEntry]:
    """Replay ledger entries in chronological order and persist state."""

    entries = session_ledger.fetch_entries(session_id)
    ordered_entries = sorted(entries, key=lambda entry: entry.created_at)
    applied_entries: List[LedgerEntry] = []

    for entry in ordered_entries:
        validate_entry(entry)
        payload = deserialize_payload(entry)
        apply_payload(state_repo, session_id, payload)
        applied_entries.append(entry)

    session_ledger.mark_replayed([entry.id for entry in applied_entries])
    return applied_entries


def replay_batch(session_ledger: SessionLedger, state_repo, session_ids: Iterable[str]) -> dict:
    """Replay multiple sessions and summarise results."""

    summary = {"replayed": [], "skipped": []}
    for session_id in session_ids:
        try:
            results = replay(session_ledger, state_repo, session_id)
        except ValueError as exc:
            LOGGER.warning("Skipping session %s due to error: %s", session_id, exc)
            summary["skipped"].append({"session_id": session_id, "reason": str(exc)})
            continue
        summary["replayed"].append({"session_id": session_id, "count": len(results)})
    return summary


def ensure_idempotency(entries: Sequence[LedgerEntry]) -> None:
    """Check that the entries being replayed have not been replayed previously."""

    for entry in entries:
        if entry.replayed:
            raise ValueError(f"Entry {entry.id} marked as replayed; aborting")


def commit_replay(session: Session, ledger: SessionLedger, entries: Sequence[LedgerEntry]) -> None:
    """Persist replay status using an external SQLAlchemy session."""

    if not entries:
        return
    ids = [entry.id for entry in entries]
    session.execute(
        update(ledger.table)
        .where(ledger.table.c.id.in_(ids))
        .values(replayed=1)
    )
    session.commit()


__all__ = [
    "LedgerEntry",
    "SessionLedger",
    "validate_entry",
    "deserialize_payload",
    "apply_payload",
    "replay",
    "replay_batch",
    "ensure_idempotency",
    "commit_replay",
]
