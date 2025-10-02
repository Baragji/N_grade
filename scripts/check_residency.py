#!/usr/bin/env python3
"""Validate vendor residency configuration aligns with EU policies."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

import yaml


@dataclass
class ResidencyResult:
    """Represents residency validation outcome for a provider."""

    provider: str
    region: str
    compliant: bool
    reason: str


def load_yaml(path: Path) -> Dict:
    """Load YAML configuration from disk."""

    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def check_region(region: str) -> bool:
    """Return True if region is within approved EU boundaries."""

    approved_prefixes = ("eu-", "europe")
    return any(region.startswith(prefix) for prefix in approved_prefixes)


def check_entry(provider: str, config: Dict) -> ResidencyResult:
    """Validate a single provider entry."""

    region = config.get("region", "unknown")
    compliant = check_region(region)
    reason = "region approved" if compliant else f"region {region} violates residency"
    return ResidencyResult(provider=provider, region=region, compliant=compliant, reason=reason)


def check(config_path: Path) -> List[ResidencyResult]:
    """Check residency configuration and return results."""

    config = load_yaml(config_path)
    providers = config.get("providers", {}) or config.get("vendors", {})
    results = []
    for provider, details in providers.items():
        results.append(check_entry(provider, details))
    return results


def write_csv(results: List[ResidencyResult], output_path: Path) -> None:
    """Write results to CSV for compliance evidence."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["provider", "region", "compliant", "reason"])
        for result in results:
            writer.writerow([result.provider, result.region, result.compliant, result.reason])


def write_json(results: List[ResidencyResult], output_path: Path) -> None:
    """Write results to JSON for programmatic consumption."""

    payload = [result.__dict__ for result in results]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    """Build CLI argument parser."""

    parser = argparse.ArgumentParser(description="Validate vendor residency configuration")
    parser.add_argument("config", type=Path, help="Path to vendor residency YAML")
    parser.add_argument("--csv", type=Path, default=Path("evidence/validation/residency_report.csv"))
    parser.add_argument("--json", type=Path, default=Path("evidence/validation/residency_report.json"))
    return parser


def run_cli(argv: List[str] | None = None) -> int:
    """Entry point for CLI execution."""

    parser = build_parser()
    args = parser.parse_args(argv)

    results = check(args.config)
    write_csv(results, args.csv)
    write_json(results, args.json)

    non_compliant = [r for r in results if not r.compliant]
    if non_compliant:
        print("❌ residency check failed", file=sys.stderr)
        for record in non_compliant:
            print(f" - {record.provider}: {record.reason}", file=sys.stderr)
        sys.exit(1)

    print("✅ residency check passed (EU compliant)")
    sys.exit(0)


if __name__ == "__main__":
    run_cli()
