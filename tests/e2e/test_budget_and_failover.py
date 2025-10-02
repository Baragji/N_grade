"""Budget enforcement and failover reliability end-to-end tests."""

import asyncio
from typing import Dict

import fakeredis
import pytest
from redis import Redis
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

from src.models.router import BudgetExceededError, ModelRouter, ProviderConfig
from src.state.repository import DistributedStateRepository


@pytest.fixture()
def redis_client() -> Redis:
    """Provide fake Redis for the repository interactions."""

    client = fakeredis.FakeRedis()
    client.flushall()
    return client


@pytest.fixture()
def engine():
    """Create SQLite engine for repository operations."""

    return create_engine(
        "sqlite+pysqlite:///:memory:",
        future=True,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )


@pytest.fixture()
def repository(redis_client: Redis, engine) -> DistributedStateRepository:
    """Return a repository instance with deterministic TTL."""

    return DistributedStateRepository(redis_client=redis_client, engine=engine, cache_ttl_seconds=90)


def _budgeted_providers() -> Dict[str, ProviderConfig]:
    """Configure providers with explicit budgets for testing."""

    return {
        "openai": ProviderConfig(
            name="openai",
            endpoint="https://api.openai.test",
            latency_weight=1.0,
            cost_weight=1.0,
            accuracy_weight=1.0,
            max_tokens=1000,
            budget={"unit_cost": 0.01, "latency": 120.0},
            failover=["anthropic", "local"],
            timeout_seconds=0.2,
        ),
        "anthropic": ProviderConfig(
            name="anthropic",
            endpoint="https://api.anthropic.test",
            latency_weight=1.0,
            cost_weight=0.9,
            accuracy_weight=1.1,
            max_tokens=900,
            budget={"unit_cost": 0.009, "latency": 140.0},
            failover=["openai", "local"],
            timeout_seconds=0.2,
        ),
        "local": ProviderConfig(
            name="local",
            endpoint="local",
            latency_weight=0.3,
            cost_weight=0.1,
            accuracy_weight=0.2,
            max_tokens=800,
            budget={"unit_cost": 0.0, "latency": 500.0},
            failover=["openai"],
            timeout_seconds=0.4,
        ),
    }


@pytest.mark.asyncio
async def test_failover_and_budget_enforcement(repository: DistributedStateRepository):
    """Simulate provider timeouts triggering failover while respecting budgets."""

    fail_counter = {"openai": 0}

    async def failing_openai(payload):
        fail_counter["openai"] += 1
        raise asyncio.TimeoutError("simulated timeout")

    async def successful_anthropic(payload):
        await asyncio.sleep(0.01)
        return {"provider": "anthropic", "payload": payload}

    router = ModelRouter(
        providers=_budgeted_providers(),
        daily_budget=0.005,
        monthly_budget=0.01,
        provider_handlers={"openai": failing_openai, "anthropic": successful_anthropic},
    )

    task = {"type": "openai", "latency_target": 90}
    payload = {"tokens": 500, "prompt": "Budget test"}
    result = await router.route(task, payload)
    assert result["decision"].provider == "anthropic"
    assert result["decision"].audit_trail["failover"] is True
    assert fail_counter["openai"] >= 1
    assert router.budget_status()["daily"] > 0

    # Trigger budget exceed scenario
    with pytest.raises(BudgetExceededError):
        await router.route(task, {"tokens": 2000, "prompt": "Too expensive"})

    repository.save("failover-session", {"stage": "post-failover"})
    assert repository.validate_integrity("failover-session")
