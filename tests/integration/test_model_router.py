"""Integration tests for the ModelRouter budget guardian."""
from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock

import pytest

from src.models.router import BudgetExceededError, ModelRouter, ProviderConfig


@pytest.fixture
def providers():
    return {
        "openai": ProviderConfig(
            name="openai",
            endpoint="https://api.openai.com/v1",
            latency_weight=0.4,
            cost_weight=0.3,
            accuracy_weight=0.3,
            max_tokens=60000,
            budget={"unit_cost": 0.02, "latency": 120},
            failover=["anthropic", "local"],
        ),
        "anthropic": ProviderConfig(
            name="anthropic",
            endpoint="https://api.anthropic.com",
            latency_weight=0.5,
            cost_weight=0.2,
            accuracy_weight=0.3,
            max_tokens=70000,
            budget={"unit_cost": 0.018, "latency": 130},
            failover=["openai", "local"],
        ),
        "local": ProviderConfig(
            name="local",
            endpoint="http://localhost:8080",
            latency_weight=0.2,
            cost_weight=0.5,
            accuracy_weight=0.3,
            max_tokens=50000,
            budget={"unit_cost": 0.005, "latency": 250},
            failover=["openai"],
        ),
    }


@pytest.fixture
def router(providers):
    return ModelRouter(providers, daily_budget=450, monthly_budget=12000)


@pytest.mark.asyncio
async def test_route_successful_path(monkeypatch, router, providers):
    async def fake_call(provider, payload):
        return {"provider": provider.name, "payload": payload}

    monkeypatch.setattr(router, "_call_provider", lambda provider, payload: fake_call(provider, payload))

    result = await router.route({"type": "coding"}, {"tokens": 1000})

    assert result["decision"].provider in {"openai", "anthropic", "local"}
    assert "timestamp" in result
    assert router.budget_status()["daily"] > 0
    assert router.audit_trail()


@pytest.mark.asyncio
async def test_route_respects_budget_caps(monkeypatch, router, providers):
    router.record_spend(449)

    async def fake_call(provider, payload):
        return {"provider": provider.name, "payload": payload}

    monkeypatch.setattr(router, "_call_provider", lambda provider, payload: fake_call(provider, payload))

    result = await router.route({"type": "planning"}, {"tokens": 500})

    assert result["decision"].estimated_cost < 1
    assert router.remaining_budget()["daily"] < 1
    assert router.budget_status()["daily"] >= 449
    assert router.audit_trail()[-1].provider in {"openai", "anthropic", "local"}


@pytest.mark.asyncio
async def test_route_triggers_failover(monkeypatch, router, providers):
    async def failing_call(provider, payload):
        raise RuntimeError("failure")

    async def fallback_call(payload):
        return {"provider": "local", "payload": payload}

    monkeypatch.setattr(router, "_call_provider", lambda provider, payload: failing_call(provider, payload))
    monkeypatch.setattr(router, "_invoke_local", lambda payload: fallback_call(payload))

    result = await router.route({"type": "coding"}, {"tokens": 100})

    assert result["decision"].provider == "local"
    assert result["decision"].reason == "failover"
    assert "error" in result
    assert router.budget_status()["daily"] == router.budget_status()["daily"]


@pytest.mark.asyncio
async def test_route_raises_on_budget_exceeded(monkeypatch, router, providers):
    router.record_spend(450)

    with pytest.raises(BudgetExceededError):
        await router.route({"type": "coding"}, {"tokens": 5000})

    assert router.budget_status()["daily"] >= 450
    assert router.budget_status()["monthly"] >= 450


@pytest.mark.asyncio
async def test_attach_guardrails_invokes_callback(monkeypatch, router, providers):
    captured = []

    async def fake_call(provider, payload):
        return {"provider": provider.name, "payload": payload}

    router.attach_guardrails(lambda decision: captured.append(decision.provider))
    monkeypatch.setattr(router, "_call_provider", lambda provider, payload: fake_call(provider, payload))

    await router.route({"type": "coding"}, {"tokens": 1200})

    assert captured
    assert captured[0] in {"openai", "anthropic", "local"}
    assert router.audit_trail()[-1].estimated_cost >= 0
    assert router.remaining_budget()["monthly"] <= 12000


@pytest.mark.asyncio
async def test_reset_budget_allows_future_calls(monkeypatch, router, providers):
    router.record_spend(1000)
    router.reset_budget()

    async def fake_call(provider, payload):
        return {"provider": provider.name, "payload": payload}

    monkeypatch.setattr(router, "_call_provider", lambda provider, payload: fake_call(provider, payload))

    result = await router.route({"type": "review"}, {"tokens": 2000})

    assert result["decision"].provider in {"openai", "anthropic", "local"}
    assert router.budget_status()["daily"] > 0
    assert router.remaining_budget()["daily"] <= 450
    assert router.audit_trail()


@pytest.mark.asyncio
async def test_local_fallback_records_history(monkeypatch, router, providers):
    async def failing_call(provider, payload):
        raise RuntimeError("provider failure")

    async def local_call(payload):
        return {"provider": "local", "payload": payload}

    monkeypatch.setattr(router, "_call_provider", lambda provider, payload: failing_call(provider, payload))
    monkeypatch.setattr(router, "_invoke_local", lambda payload: local_call(payload))

    result = await router.route({"type": "coding"}, {"tokens": 150})

    assert result["decision"].provider == "local"
    assert result["decision"].reason == "failover"
    assert "decision" in result
    assert result["decision"].budget_snapshot["monthly"] <= 12000


@pytest.mark.asyncio
async def test_remaining_budget_updates_after_calls(monkeypatch, router, providers):
    async def fake_call(provider, payload):
        return {"provider": provider.name, "payload": payload}

    monkeypatch.setattr(router, "_call_provider", lambda provider, payload: fake_call(provider, payload))

    before = router.remaining_budget()["daily"]
    await router.route({"type": "planning"}, {"tokens": 500})
    after = router.remaining_budget()["daily"]

    assert after <= before
    assert router.budget_status()["daily"] >= 0
    assert router.remaining_budget()["monthly"] <= 12000
    assert router.audit_trail()[-1].provider in {"openai", "anthropic", "local"}


@pytest.mark.asyncio
async def test_cost_estimate_calculation(router, providers):
    cost = router.estimate_cost(providers["openai"], tokens=1000)

    assert cost == pytest.approx(0.02)
    assert router.remaining_budget()["daily"] == 450
    assert router.remaining_budget()["monthly"] == 12000


@pytest.mark.asyncio
async def test_failover_chain_preserves_error(monkeypatch, router, providers):
    async def failing_call(provider, payload):
        raise RuntimeError("ceiling breach")

    async def local_call(payload):
        return {"provider": "local", "payload": payload}

    monkeypatch.setattr(router, "_call_provider", lambda provider, payload: failing_call(provider, payload))
    monkeypatch.setattr(router, "_invoke_local", lambda payload: local_call(payload))

    result = await router.route({"type": "coding"}, {"tokens": 300})

    assert "error" in result
    assert "ceiling" in result["error"]
    assert result["decision"].provider == "local"
    assert result["decision"].reason == "failover"
