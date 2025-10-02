#!/usr/bin/env python3
"""CLI to execute end-to-end tests and record evidence for CI consumption."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, List


def _parse_args() -> argparse.Namespace:
    """Parse command line arguments for the E2E runner."""

    parser = argparse.ArgumentParser(description="Run pytest end-to-end suite with metrics output.")
    parser.add_argument("tests", nargs="*", default=["tests/e2e"], help="Test paths to execute")
    parser.add_argument("--output-json", default="evidence/validation/e2e_results.json", help="Path to JSON evidence file")
    parser.add_argument("--output-csv", default="metrics/quality/e2e_results.csv", help="Path to CSV metrics file")
    parser.add_argument("--pytest-args", nargs=argparse.REMAINDER, help="Additional arguments passed to pytest")
    return parser.parse_args()


def _normalise_test_line(line: str) -> str:
    """Normalise pytest output lines to extract test identifiers."""

    markers = [" PASSED", " FAILED", " SKIPPED", " XPASS", " XFAIL"]
    for marker in markers:
        if marker in line:
            return line.replace(marker, "").strip()
    return line.strip()


def _collect_test_metrics(stdout: str, duration_ms: float) -> List[Dict[str, str]]:
    """Extract best-effort metrics from pytest stdout."""

    metrics: List[Dict[str, str]] = []
    for raw_line in stdout.splitlines():
        line = raw_line.strip()
        if not line or "::" not in line:
            continue
        identifier = _normalise_test_line(line)
        status = "passed"
        if "FAILED" in raw_line:
            status = "failed"
        elif "SKIPPED" in raw_line:
            status = "skipped"
        metrics.append({"test_name": identifier, "status": status, "duration_ms": f"{duration_ms:.2f}"})
    if not metrics:
        metrics.append({"test_name": "pytest-e2e", "status": "unknown", "duration_ms": f"{duration_ms:.2f}"})
    return metrics


def _run_pytest(test_paths: List[str], extra_args: List[str] | None) -> subprocess.CompletedProcess[str]:
    """Execute pytest with provided arguments and capture output."""

    command = [sys.executable, "-m", "pytest", "-q", *test_paths]
    if extra_args:
        command.extend(extra_args)
    return subprocess.run(command, text=True, capture_output=True)


def _write_csv(path: Path, rows: List[Dict[str, str]]) -> None:
    """Write CSV metrics capturing execution status."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["test_name", "status", "duration_ms"])
        writer.writeheader()
        writer.writerows(rows)


def _write_json(path: Path, command: List[str], result: subprocess.CompletedProcess[str], duration_ms: float) -> None:
    """Persist JSON evidence from the test execution."""

    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "command": command,
        "exit_code": result.returncode,
        "duration_ms": duration_ms,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "timestamp": time.time(),
    }
    path.write_text(json.dumps(payload, indent=2))


def _print_summary(status: str, duration_ms: float, metrics: List[Dict[str, str]]) -> None:
    """Display human-readable summary to stdout."""

    headline = f"E2E status: {status} in {duration_ms:.2f} ms"
    print(headline)
    for metric in metrics:
        print(f" - {metric['test_name']}: {metric['status']} ({metric['duration_ms']} ms)")


def main() -> None:
    """Entry point for executing pytest and recording evidence."""

    args = _parse_args()
    test_paths = args.tests
    extra_args = args.pytest_args or []

    start = time.perf_counter()
    result = _run_pytest(test_paths, extra_args)
    duration_ms = (time.perf_counter() - start) * 1000
    status = "passed" if result.returncode == 0 else "failed"

    command = [sys.executable, "-m", "pytest", "-q", *test_paths, *(extra_args or [])]
    metrics = _collect_test_metrics(result.stdout, duration_ms)
    if metrics and metrics[0]["status"] == "unknown":
        metrics[0]["status"] = status
    _write_csv(Path(args.output_csv), metrics)
    _write_json(Path(args.output_json), command, result, duration_ms)

    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

    _print_summary(status, duration_ms, metrics)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
