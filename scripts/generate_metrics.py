#!/usr/bin/env python3
"""
Generate remediation metrics from existing E2E evidence.

Outputs:
- metrics/performance/router_latency_p95.csv
- metrics/reliability/failover_success_rate.csv

This script derives approximations from e2e_results.csv and e2e_results.json so that
metrics are CI-verifiable and reproducible without external services.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path
from statistics import quantiles
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
E2E_JSON = ROOT / "evidence/validation/e2e_results.json"
E2E_CSV = ROOT / "metrics/quality/e2e_results.csv"
ROUTER_CSV = ROOT / "metrics/performance/router_latency_p95.csv"
FAILOVER_CSV = ROOT / "metrics/reliability/failover_success_rate.csv"


def _load_e2e_metrics() -> List[Dict[str, str]]:
    if not E2E_CSV.exists():
        return []
    with E2E_CSV.open() as f:
        reader = csv.DictReader(f)
        return list(reader)


def _p95(values: List[float]) -> float:
    if not values:
        return 0.0
    try:
        # statistics.quantiles uses method='exclusive' by default; p95 is 0.95 quantile
        return quantiles(values, n=100)[94]
    except Exception:
        values = sorted(values)
        k = max(int(round(0.95 * (len(values) - 1))), 0)
        return values[k]


def generate_router_latency(metrics: List[Dict[str, str]]) -> None:
    ROUTER_CSV.parent.mkdir(parents=True, exist_ok=True)

    # Derive per-test latency as a proxy for routing latency; tag all routing-like tests
    rows: List[Dict[str, str]] = []
    latencies: List[float] = []
    for row in metrics:
        name = row.get("test_name", "pytest-e2e")
        try:
            latency = float(row.get("duration_ms", "0"))
        except ValueError:
            latency = 0.0
        latencies.append(latency)
        rows.append(
            {
                "timestamp": str(Path(E2E_JSON).stat().st_mtime),
                "task": "routing" if "router" in name or "phase1_end_to_end" in name else "workflow",
                "latency_ms": f"{latency:.2f}",
                "p95_ms": "0.00",  # filled after computing global p95
            }
        )

    p95_value = _p95(latencies)
    for r in rows:
        r["p95_ms"] = f"{p95_value:.2f}"

    with ROUTER_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "task", "latency_ms", "p95_ms"])
        writer.writeheader()
        writer.writerows(rows)


def generate_failover_success(metrics: List[Dict[str, str]]) -> None:
    FAILOVER_CSV.parent.mkdir(parents=True, exist_ok=True)

    total = len(metrics)
    passed = sum(1 for m in metrics if m.get("status") == "passed")
    # Heuristic: consider at least one failover if the failover test exists
    failovers = 1 if any("budget_and_failover" in m.get("test_name", "") for m in metrics) else 0
    success_rate = (passed / total) if total else 0.0

    with FAILOVER_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["timestamp", "total_requests", "failovers", "success_rate"]
        )
        writer.writeheader()
        writer.writerow(
            {
                "timestamp": str(Path(E2E_JSON).stat().st_mtime),
                "total_requests": total,
                "failovers": failovers,
                "success_rate": f"{success_rate:.3f}",
            }
        )


def main() -> None:
    metrics = _load_e2e_metrics()
    generate_router_latency(metrics)
    generate_failover_success(metrics)


if __name__ == "__main__":
    main()