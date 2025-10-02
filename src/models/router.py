"""Multi-provider LLM routing with FinOps budget enforcement."""
from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Awaitable, Callable, Dict, List, Optional

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
    timeout_seconds: float = 2.0


@dataclass
class RoutingDecision:
    """Result of routing a task to a provider."""

    provider: str
    reason: str
    estimated_cost: float
    latency_budget: float
    budget_snapshot: Dict[str, float]
    timestamp: str
    audit_trail: Dict[str, Any]


class BudgetExceededError(RuntimeError):
    """Raised when executing a call would breach configured budget."""


class ModelRouter:
    """Routes workloads across OpenAI, Anthropic, and local fallbacks."""

    def __init__(
        self,
        providers: Dict[str, ProviderConfig],
        daily_budget: float,
        monthly_budget: float,
        provider_handlers: Optional[Dict[str, Callable[[Dict[str, Any]], Awaitable[Dict[str, Any]]]]] = None,
    ) -> None:
        self.providers = providers
        self.daily_budget = daily_budget
        self.monthly_budget = monthly_budget
        self._spend_tracker: Dict[str, float] = {"daily": 0.0, "monthly": 0.0}
        self._history: List[RoutingDecision] = []
        self._audit_log: List[Dict[str, Any]] = []
        self._guardrail_callback: Optional[Callable[[RoutingDecision], None]] = None
        self._provider_handlers = provider_handlers or {}
        self._circuit_breakers: Dict[str, int] = {}

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
            LOGGER.error("Budget breach prevented: %s > %s", amount, remaining)
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

        primary = [cfg for cfg in self.providers.values() if cfg.name == task_type]
        secondary = [cfg for cfg in self.providers.values() if task_type in cfg.failover and cfg.name != task_type]
        if not primary and not secondary:
            return sorted(self.providers.values(), key=lambda cfg: cfg.accuracy_weight, reverse=True)
        ordered = primary + sorted(secondary, key=lambda cfg: cfg.accuracy_weight, reverse=True)
        return ordered

    # Backward-compatible alias for older tests that monkeypatch `_call_provider`
    async def _call_provider(self, provider: ProviderConfig, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Compatibility wrapper delegating to `_invoke_provider`.
        Older tests patch `_call_provider`; keep this method to avoid breaking them.
        """
        return await self._invoke_provider(provider, payload)

    async def _invoke_provider(self, provider: ProviderConfig, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Call provider-specific implementation with timeout handling."""

        handler = self._provider_handlers.get(provider.name)
        if handler is None:
            if provider.name == "openai":
                handler = self._default_openai
            elif provider.name == "anthropic":
                handler = self._default_anthropic
            else:
                handler = self._default_local
        try:
            response = await asyncio.wait_for(handler(payload), timeout=provider.timeout_seconds)
        except asyncio.TimeoutError as exc:
            LOGGER.error("Timeout from provider %s", provider.name)
            raise
        except Exception as exc:  # pragma: no cover - defensive
            LOGGER.error("Provider %s raised %s", provider.name, exc)
            raise
        return response

    async def _default_openai(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate calling the OpenAI API."""

        await asyncio.sleep(0.01)
        return {"provider": "openai", "payload": payload}

    async def _default_anthropic(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate calling the Anthropic API."""

        await asyncio.sleep(0.01)
        return {"provider": "anthropic", "payload": payload}

    async def _default_local(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Fallback local execution when cloud providers fail."""

        await asyncio.sleep(0.02)
        return {"provider": "local", "payload": payload}

    # Compatibility alias expected by older tests
    async def _invoke_local(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Delegate to the default local handler to preserve test compatibility."""
        return await self._default_local(payload)

    def _record_audit(self, provider: ProviderConfig, cost: float, metadata: Dict[str, Any]) -> RoutingDecision:
        """Record routing decision and return summary object."""

        decision = RoutingDecision(
            provider=provider.name,
            reason=metadata.get("reason", "best_score"),
            estimated_cost=cost,
            latency_budget=provider.budget.get("latency", 120.0),
            budget_snapshot=self.remaining_budget(),
            timestamp=datetime.now(timezone.utc).isoformat(),
            audit_trail=metadata,
        )
        self._history.append(decision)
        audit_entry = {
            "provider": provider.name,
            "timestamp": decision.timestamp,
            "budget": decision.budget_snapshot,
            "metadata": metadata,
        }
        self._audit_log.append(audit_entry)
        self._notify_guardrails(decision)
        LOGGER.info("Routed task to %s with budget snapshot %s", decision.provider, decision.budget_snapshot)
        return decision

    def _notify_guardrails(self, decision: RoutingDecision) -> None:
        """Notify guardrail callback if present."""

        if self._guardrail_callback:
            try:
                self._guardrail_callback(decision)
            except Exception as exc:  # pragma: no cover - defensive
                LOGGER.error("Guardrail callback failed: %s", exc)

    def attach_guardrails(self, guardrail_callback: Callable[[RoutingDecision], None]) -> None:
        """Register callback invoked after each successful routing decision."""

        self._guardrail_callback = guardrail_callback

    async def _route_with_failover(self, providers: List[ProviderConfig], payload: Dict[str, Any]) -> Dict[str, Any]:
        """Attempt providers sequentially, performing failover on errors."""

        last_error: Optional[Exception] = None
        for provider in providers:
            if self._circuit_breakers.get(provider.name, 0) >= 3:
                LOGGER.warning("Skipping provider %s due to circuit breaker", provider.name)
                continue
            tokens = min(payload.get("tokens", 1000), provider.max_tokens)
            cost = self.estimate_cost(provider, tokens)
            self._ensure_budget(cost)
            try:
                # Use monkeypatch-friendly alias so tests can override provider calls
                response = await self._call_provider(provider, payload)
                self.record_spend(cost)
                metadata = {"reason": "best_score", "failover": providers[0].name != provider.name}
                decision = self._record_audit(provider, cost, metadata)
                response.update({"decision": decision, "timestamp": decision.timestamp})
                return response
            except BudgetExceededError:
                raise
            except asyncio.TimeoutError as exc:
                LOGGER.warning("Provider %s timed out; failover engaged", provider.name)
                self._circuit_breakers[provider.name] = self._circuit_breakers.get(provider.name, 0) + 1
                last_error = exc
            except Exception as exc:  # pragma: no cover - defensive
                LOGGER.warning("Provider %s failed with %s", provider.name, exc)
                self._circuit_breakers[provider.name] = self._circuit_breakers.get(provider.name, 0) + 1
                last_error = exc
                continue
        LOGGER.error("All providers failed, invoking local failover")
        failover_provider = self.providers.get("local") or ProviderConfig(
            name="local",
            endpoint="local",
            latency_weight=1.0,
            cost_weight=1.0,
            accuracy_weight=0.1,
            max_tokens=payload.get("tokens", 500),
            budget={"unit_cost": 0.0, "latency": 999.0},
        )
        # Use alias to allow tests to monkeypatch local invocation
        response = await self._invoke_local(payload)
        decision = self._record_audit(failover_provider, 0.0, {"reason": "failover", "error": str(last_error) if last_error else None})
        response.update({"decision": decision})
        if last_error:
            response["error"] = str(last_error)
        return response

    async def route(self, task: Dict[str, Any], payload: Dict[str, Any]) -> Dict[str, Any]:
        """Route a task across providers while protecting daily and monthly budget."""

        task_type = task.get("type", "openai")
        ordered = self._ordered_providers(task_type)
        return await self._route_with_failover(ordered, payload)

    def audit_trail(self) -> List[RoutingDecision]:
        """Return immutable copy of routing history."""

        return list(self._history)

    def budget_status(self) -> Dict[str, float]:
        """Return current budget utilisation."""

        return self._spend_tracker.copy()

    def reset_budget(self) -> None:
        """Reset tracked budget spend for a new reporting period."""

        self._spend_tracker = {"daily": 0.0, "monthly": 0.0}
        self._circuit_breakers.clear()

    def audit_log(self) -> List[Dict[str, Any]]:
        """Return recorded audit events for compliance reviews."""

        return list(self._audit_log)


__all__ = ["ModelRouter", "ProviderConfig", "RoutingDecision", "BudgetExceededError"]
