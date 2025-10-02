"""FinOps guardrails ensuring routing adheres to strict budgets."""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional

LOGGER = logging.getLogger(__name__)


@dataclass
class BudgetSnapshot:
    """Represents a point-in-time view of budget utilisation."""

    daily_cap: float
    monthly_cap: float
    daily_spend: float
    monthly_spend: float
    timestamp: datetime = field(default_factory=datetime.utcnow)

    def remaining_daily(self) -> float:
        """Return remaining daily cap."""

        return max(self.daily_cap - self.daily_spend, 0.0)

    def remaining_monthly(self) -> float:
        """Return remaining monthly cap."""

        return max(self.monthly_cap - self.monthly_spend, 0.0)


class FinOpsGuardrails:
    """Implements enforcement logic for FinOps budgets and alerts."""

    def __init__(self, daily_cap_eur: float, monthly_cap_eur: float, threshold_percent: float = 80.0) -> None:
        self.daily_cap = daily_cap_eur
        self.monthly_cap = monthly_cap_eur
        self.threshold_percent = threshold_percent
        self._history: List[BudgetSnapshot] = []
        self._alerts: List[Dict[str, str]] = []

    def record_snapshot(self, daily_spend: float, monthly_spend: float) -> BudgetSnapshot:
        """Record a new snapshot and emit alerts if thresholds exceeded."""

        snapshot = BudgetSnapshot(
            daily_cap=self.daily_cap,
            monthly_cap=self.monthly_cap,
            daily_spend=daily_spend,
            monthly_spend=monthly_spend,
        )
        self._history.append(snapshot)
        self._evaluate_threshold(snapshot)
        return snapshot

    def _evaluate_threshold(self, snapshot: BudgetSnapshot) -> None:
        """Trigger alerts when utilisation passes configured threshold."""

        utilisation_daily = (snapshot.daily_spend / self.daily_cap) * 100 if self.daily_cap else 0
        utilisation_monthly = (snapshot.monthly_spend / self.monthly_cap) * 100 if self.monthly_cap else 0
        if utilisation_daily >= self.threshold_percent:
            self._alerts.append({
                "type": "daily",
                "message": f"Daily cap {self.daily_cap} nearly exhausted",
                "utilisation": f"{utilisation_daily:.1f}%",
            })
        if utilisation_monthly >= self.threshold_percent:
            self._alerts.append({
                "type": "monthly",
                "message": f"Monthly cap {self.monthly_cap} nearly exhausted",
                "utilisation": f"{utilisation_monthly:.1f}%",
            })

    def check_budget(self, estimated_cost: float) -> bool:
        """Return True if execution is allowed under current caps."""

        if estimated_cost > self.daily_cap:
            LOGGER.error("Cost %.2f exceeds daily cap %.2f", estimated_cost, self.daily_cap)
            return False
        if estimated_cost > self.monthly_cap:
            LOGGER.error("Cost %.2f exceeds monthly cap %.2f", estimated_cost, self.monthly_cap)
            return False
        return True

    def enforce(self, estimated_cost: float, current_daily_spend: float, current_monthly_spend: float) -> None:
        """Raise if budgets would be breached by executing the request."""

        projected_daily = current_daily_spend + estimated_cost
        projected_monthly = current_monthly_spend + estimated_cost
        if projected_daily > self.daily_cap:
            raise RuntimeError("Projected spend exceeds daily cap")
        if projected_monthly > self.monthly_cap:
            raise RuntimeError("Projected spend exceeds monthly cap")

    def track_alerts(self) -> List[Dict[str, str]]:
        """Return alert history for auditing."""

        return list(self._alerts)

    def history(self) -> List[BudgetSnapshot]:
        """Return budget history snapshots."""

        return list(self._history)

    def reset(self) -> None:
        """Clear history and alerts."""

        self._history.clear()
        self._alerts.clear()

    def serialize(self) -> List[Dict[str, str]]:
        """Return serializable representation of alert history."""

        return [
            {
                "type": alert["type"],
                "message": alert["message"],
                "timestamp": datetime.utcnow().isoformat(),
            }
            for alert in self._alerts
        ]

    def latest_snapshot(self) -> Optional[BudgetSnapshot]:
        """Return the latest recorded snapshot if available."""

        return self._history[-1] if self._history else None


__all__ = ["FinOpsGuardrails", "BudgetSnapshot", "Guardrails"]

class Guardrails(FinOpsGuardrails):
    """Compatibility alias used in policy enforcement rules."""

    def __init__(self, daily_cap_eur: float, monthly_cap_eur: float, threshold_percent: float = 80.0) -> None:
        super().__init__(daily_cap_eur=daily_cap_eur, monthly_cap_eur=monthly_cap_eur, threshold_percent=threshold_percent)

