"""Multi-provider LLM routing with FinOps budget enforcement."""
from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional

LOGGER = logging.getLogger(__name__)


@dataclass
class ProviderConfig:
    """Configuration for an individual LLM provider."""

    name: str
    endpoint: str
    latency_weight: float
    cost_weight: float
    accuracy_weight: float
    max_tokens: int
    budget: Dict[str, float]
    failover: List[str] = field(default_factory=list)


@dataclass
class RoutingDecision:
    """Result of routing a task to a provider."""

    provider: str
    reason: str
    estimated_cost: float
    latency_budget: float
    budget_snapshot: Dict[str, float]


class BudgetExceededError(RuntimeError):
    """Raised when executing a call would breach configured budget."""


class ModelRouter:
    """Routes workloads across OpenAI, Anthropic, and local fallbacks."""

    def __init__(self, providers: Dict[str, ProviderConfig], daily_budget: float, monthly_budget: float) -> None:
        self.providers = providers
        self.daily_budget = daily_budget
        self.monthly_budget = monthly_budget
        self._spend_tracker: Dict[str, float] = {"daily": 0.0, "monthly": 0.0}
        self._history: List[RoutingDecision] = []
        self._guardrail_callback: Optional[Callable[[RoutingDecision], None]] = None

    def estimate_cost(self, provider: ProviderConfig, tokens: int) -> float:
        """Estimate euro cost for a request based on token usage."""

        unit_cost = provider.budget.get("unit_cost", 0.0)
        return (tokens / 1000) * unit_cost

    def record_spend(self, amount: float) -> None:
        """Record spend against tracked budgets."""

        self._spend_tracker["daily"] += amount
        self._spend_tracker["monthly"] += amount

    def remaining_budget(self) -> Dict[str, float]:
        """Return the remaining budget for daily and monthly caps."""

        return {
            "daily": max(self.daily_budget - self._spend_tracker["daily"], 0.0),
            "monthly": max(self.monthly_budget - self._spend_tracker["monthly"], 0.0),
        }

    def _ensure_budget(self, amount: float) -> None:
        """Ensure the requested call keeps budgets within caps."""

        remaining = self.remaining_budget()
        if amount > remaining["daily"] or amount > remaining["monthly"]:
            raise BudgetExceededError("Requested call would exceed budget cap")

    def _score_provider(self, provider: ProviderConfig, request: Dict[str, Any]) -> float:
        """Score a provider using weighted cost, latency, and accuracy metrics."""

        latency = request.get("latency_target", provider.latency_weight)
        accuracy = request.get("accuracy_target", provider.accuracy_weight)
        cost = request.get("cost_target", provider.cost_weight)
        return (
            provider.accuracy_weight * accuracy
            + provider.latency_weight / max(latency, 1e-3)
            + provider.cost_weight / max(cost, 1e-3)
        )

    def _ordered_providers(self, task_type: str) -> List[ProviderConfig]:
        """Return providers sorted by suitability for the task type."""

        candidates = []
        for cfg in self.providers.values():
            if task_type in cfg.failover or cfg.name == task_type:
                candidates.append(cfg)
        if not candidates:
            candidates = list(self.providers.values())
        return sorted(candidates, key=lambda cfg: cfg.accuracy_weight, reverse=True)

    async def _invoke_openai(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate calling the OpenAI API."""

        await asyncio.sleep(0.01)
        return {"provider": "openai", "payload": payload}

    async def _invoke_anthropic(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate calling the Anthropic API."""

        await asyncio.sleep(0.01)
        return {"provider": "anthropic", "payload": payload}

    async def _invoke_local(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Fallback local execution when cloud providers fail."""

        await asyncio.sleep(0.02)
        return {"provider": "local", "payload": payload}

    async def _call_provider(self, provider: ProviderConfig, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Call provider-specific implementation."""

        if provider.name == "openai":
            return await self._invoke_openai(payload)
        if provider.name == "anthropic":
            return await self._invoke_anthropic(payload)
        return await self._invoke_local(payload)

    def _create_decision(self, provider: ProviderConfig, cost: float) -> RoutingDecision:
        """Record routing decision and return summary object."""

        decision = RoutingDecision(
            provider=provider.name,
            reason="best_score",
            estimated_cost=cost,
            latency_budget=provider.budget.get("latency", 120.0),
            budget_snapshot=self.remaining_budget(),
        )
        self._history.append(decision)
        self._notify_guardrails(decision)
        return decision

    async def route(self, task: Dict[str, Any], payload: Dict[str, Any]) -> Dict[str, Any]:
        """Route a task across providers while protecting daily and monthly budget."""

        task_type = task.get("type", "coding")
        ordered = self._ordered_providers(task_type)
        last_error: Optional[Exception] = None

        for provider in ordered:
            tokens = min(payload.get("tokens", 1000), provider.max_tokens)
            cost = self.estimate_cost(provider, tokens)
            self._ensure_budget(cost)
            try:
                response = await self._call_provider(provider, payload)
                self.record_spend(cost)
                decision = self._create_decision(provider, cost)
                LOGGER.info("Routed task to %s with budget snapshot %s", decision.provider, decision.budget_snapshot)
                response.update({
                    "decision": decision,
                    "timestamp": datetime.utcnow().isoformat(),
                })
                return response
            except Exception as exc:  # pragma: no cover - defensive logging
                LOGGER.warning("Provider %s failed, attempting failover: %s", provider.name, exc)
                last_error = exc
                continue

        LOGGER.error("All providers failed, invoking failover chain")
        failover_payload = await self._invoke_local(payload)
        failover_payload["decision"] = RoutingDecision(
            provider="local",
            reason="failover",
            estimated_cost=0.0,
            latency_budget=999,
            budget_snapshot=self.remaining_budget(),
        )
        if last_error:
            failover_payload["error"] = str(last_error)
        return failover_payload

    def audit_trail(self) -> List[RoutingDecision]:
        """Return immutable copy of routing history."""

        return list(self._history)

    def reset_budget(self) -> None:
        """Reset tracked budget spend for a new reporting period."""

        self._spend_tracker = {"daily": 0.0, "monthly": 0.0}

    def budget_status(self) -> Dict[str, float]:
        """Return current budget utilisation."""

        return self._spend_tracker.copy()

    def attach_guardrails(self, guardrail_callback: Callable[[RoutingDecision], None]) -> None:
        """Register callback invoked after each successful routing decision."""

        self._guardrail_callback = guardrail_callback

    def _notify_guardrails(self, decision: RoutingDecision) -> None:
        """Notify guardrail callback if present."""

        if self._guardrail_callback:
            self._guardrail_callback(decision)


__all__ = ["ModelRouter", "ProviderConfig", "RoutingDecision", "BudgetExceededError"]
