"""End-to-end validation covering repository, router, and ledger replay."""

import asyncio
from datetime import datetime, timedelta
from typing import Dict

import fakeredis
import pytest
from redis import Redis
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

from src.models.router import ModelRouter, ProviderConfig
from src.state.ledger_replay import SessionLedger, replay
from src.state.repository import DistributedStateRepository


@pytest.fixture()
def redis_client() -> Redis:
    """Provide an isolated fake Redis instance for each test."""

    client = fakeredis.FakeRedis()
    client.flushall()
    return client


@pytest.fixture()
def engine():
    """Create an in-memory SQLite engine configured for SQLAlchemy sessions."""

    return create_engine(
        "sqlite+pysqlite:///:memory:",
        future=True,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )


@pytest.fixture()
def repository(redis_client: Redis, engine) -> DistributedStateRepository:
    """Instantiate the hardened distributed state repository."""

    return DistributedStateRepository(redis_client=redis_client, engine=engine, cache_ttl_seconds=120)


@pytest.fixture()
def ledger(engine) -> SessionLedger:
    """Return a session ledger bound to the in-memory database."""

    return SessionLedger(engine=engine)


def _provider_configurations() -> Dict[str, ProviderConfig]:
    """Assemble provider configuration for OpenAI, Anthropic, and local fallback."""

    return {
        "openai": ProviderConfig(
            name="openai",
            endpoint="https://api.openai.test",
            latency_weight=1.0,
            cost_weight=1.0,
            accuracy_weight=1.0,
            max_tokens=2000,
            budget={"unit_cost": 0.002, "latency": 120.0},
            failover=["anthropic", "local"],
            timeout_seconds=0.5,
        ),
        "anthropic": ProviderConfig(
            name="anthropic",
            endpoint="https://api.anthropic.test",
            latency_weight=1.2,
            cost_weight=1.1,
            accuracy_weight=1.1,
            max_tokens=1500,
            budget={"unit_cost": 0.003, "latency": 150.0},
            failover=["openai", "local"],
            timeout_seconds=0.5,
        ),
        "local": ProviderConfig(
            name="local",
            endpoint="local",
            latency_weight=0.5,
            cost_weight=0.1,
            accuracy_weight=0.2,
            max_tokens=1200,
            budget={"unit_cost": 0.0, "latency": 400.0},
            failover=["openai"],
            timeout_seconds=1.0,
        ),
    }


@pytest.mark.asyncio
async def test_phase_one_end_to_end(repository: DistributedStateRepository, ledger: SessionLedger):
    """Exercise repository save/get, routing, and ledger replay across workflow."""

    session_id = "session-123"
    initial_payload = {"step": 1, "content": "boot"}
    stored = repository.save(session_id, initial_payload)
    assert stored.payload_hash == repository._hash_payload(initial_payload)
    assert repository.validate_integrity(session_id)

    replay_payload = {"step": 2, "content": "checkpoint"}
    ledger.append(session_id, replay_payload)
    ledger.append(session_id, {"step": 3, "content": "final"})

    routed_task = {"type": "openai", "latency_target": 100}
    router = ModelRouter(
        providers=_provider_configurations(),
        daily_budget=10.0,
        monthly_budget=100.0,
    )
    result = await router.route(routed_task, {"tokens": 1000, "prompt": "Hello"})
    assert "decision" in result
    assert result["decision"].provider in {"openai", "anthropic", "local"}
    assert router.budget_status()["daily"] <= 10.0
    assert router.audit_trail()[-1].audit_trail["reason"] in {"best_score", "failover"}

    replayed_entries = replay(ledger, repository, session_id)
    assert len(replayed_entries) == 2
    assert all(entry.replayed is False for entry in replayed_entries)
    assert repository.validate_integrity(session_id)

    # Confirm cache TTL extension behaves as expected
    repository.touch(session_id, ttl_extension=60)
    repository.purge_stale(datetime.utcnow() + timedelta(days=365))

    cached = repository.get(session_id)
    assert cached is not None
    assert cached.version >= 1

    summary = router.audit_log()[-1]
    assert "budget" in summary

    await asyncio.sleep(0)  # Allow pending tasks to settle for coverage
