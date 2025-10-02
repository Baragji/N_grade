"""Ledger replay idempotency and checksum validation tests."""

import json
from typing import List

import fakeredis
import pytest
from redis import Redis
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

from src.state.ledger_replay import (
    LedgerEntry,
    SessionLedger,
    ensure_idempotency,
    replay,
)
from src.state.repository import DistributedStateRepository


@pytest.fixture()
def redis_client() -> Redis:
    """Provide isolated Redis stub."""

    client = fakeredis.FakeRedis()
    client.flushall()
    return client


@pytest.fixture()
def engine():
    """Create SQLite engine shared across ledger operations."""

    return create_engine(
        "sqlite+pysqlite:///:memory:",
        future=True,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )


@pytest.fixture()
def repository(redis_client: Redis, engine) -> DistributedStateRepository:
    """Instantiate repository for idempotency tests."""

    return DistributedStateRepository(redis_client=redis_client, engine=engine, cache_ttl_seconds=45)


@pytest.fixture()
def ledger(engine) -> SessionLedger:
    """Return session ledger bound to SQLite."""

    return SessionLedger(engine=engine)


@pytest.mark.asyncio
async def test_ledger_replay_is_idempotent(repository: DistributedStateRepository, ledger: SessionLedger):
    """Ensure replay is ordered, checksum validated, and idempotent."""

    session_id = "ledger-session"
    payloads = [
        {"step": 1, "value": "alpha"},
        {"step": 2, "value": "beta"},
        {"step": 3, "value": "gamma"},
    ]

    for payload in payloads:
        ledger.append(session_id, payload)

    replayed = replay(ledger, repository, session_id)
    assert len(replayed) == len(payloads)
    ordered_steps = [entry.as_dict()["payload"]["step"] for entry in replayed]
    assert ordered_steps == sorted(ordered_steps)

    entries: List[LedgerEntry] = ledger.fetch_entries(session_id)
    ensure_idempotency(replayed)
    for entry in entries:
        assert entry.checksum
        decoded = json.loads(entry.payload.decode("utf-8"))
        assert decoded["step"] in {1, 2, 3}

    repository_state = repository.get(session_id)
    assert repository_state is not None
    assert repository_state.payload["step"] == 3

    # Replaying again should fail idempotency validation because records are marked replayed
    with pytest.raises(Exception):
        ensure_idempotency(entries)
