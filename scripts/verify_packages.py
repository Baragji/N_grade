#!/usr/bin/env python3
"""Verify Python and JavaScript dependencies against lockfiles and OSV."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional

import requests

OSV_API = "https://api.osv.dev/v1/query"


@dataclass
class PackageRecord:
    """Represents a dependency discovered in lockfiles."""

    name: str
    version: str
    ecosystem: str
    source: Path


def load_requirements(path: Path) -> List[PackageRecord]:
    """Parse a requirements.txt style file."""

    packages: List[PackageRecord] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "==" in line:
                name, version = line.split("==", 1)
            else:
                name, version = line, "latest"
            packages.append(PackageRecord(name=name, version=version, ecosystem="PyPI", source=path))
    return packages


def load_package_lock(path: Path) -> List[PackageRecord]:
    """Parse a package-lock.json file."""

    data = json.loads(path.read_text(encoding="utf-8"))
    packages: List[PackageRecord] = []
    dependencies = data.get("dependencies", {})
    for name, info in dependencies.items():
        version = info.get("version", "unknown")
        packages.append(PackageRecord(name=name, version=version, ecosystem="npm", source=path))
    return packages


def load_lockfile(path: Path) -> List[PackageRecord]:
    """Load dependencies from supported lockfiles."""

    if path.name.endswith("requirements.txt"):
        return load_requirements(path)
    if path.name == "package-lock.json":
        return load_package_lock(path)
    raise ValueError(f"Unsupported lockfile: {path}")


def query_osv(package: PackageRecord) -> List[Dict[str, str]]:
    """Query OSV database for known vulnerabilities."""

    payload = {
        "package": {"name": package.name, "ecosystem": package.ecosystem},
        "version": package.version,
    }
    response = requests.post(OSV_API, json=payload, timeout=5)
    response.raise_for_status()
    data = response.json()
    vulns = []
    for item in data.get("vulns", []):
        vulns.append({
            "id": item.get("id", "unknown"),
            "summary": item.get("summary", ""),
            "ecosystem": package.ecosystem,
            "package": package.name,
        })
    return vulns


def verify(packages: Iterable[PackageRecord], fail_on_vulnerabilities: bool = True) -> Dict[str, List[Dict[str, str]]]:
    """Verify dependencies against OSV and return results."""

    findings: Dict[str, List[Dict[str, str]]] = {"vulnerabilities": [], "validated": []}
    for pkg in packages:
        vulnerabilities = query_osv(pkg)
        if vulnerabilities:
            findings["vulnerabilities"].extend(vulnerabilities)
        else:
            findings["validated"].append({
                "package": pkg.name,
                "version": pkg.version,
                "ecosystem": pkg.ecosystem,
                "source": str(pkg.source),
            })
    if fail_on_vulnerabilities and findings["vulnerabilities"]:
        raise RuntimeError("vulnerability check failed")
    return findings


def write_report(results: Dict[str, List[Dict[str, str]]], report_path: Path) -> None:
    """Write verification results to CSV for evidence."""

    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["package", "version", "ecosystem", "status"])
        for item in results["validated"]:
            writer.writerow([item["package"], item["version"], item["ecosystem"], "validated"])
        for vuln in results["vulnerabilities"]:
            writer.writerow([vuln["package"], "-", vuln["ecosystem"], f"OSV:{vuln['id']}"])


def build_argument_parser() -> argparse.ArgumentParser:
    """Create CLI argument parser."""

    parser = argparse.ArgumentParser(description="Verify lockfile dependencies against OSV")
    parser.add_argument("paths", nargs="+", type=Path, help="Lockfile paths (requirements.txt, package-lock.json)")
    parser.add_argument("--report", type=Path, default=Path("evidence/validation/package_verification.csv"))
    parser.add_argument("--allow-vulnerabilities", action="store_true", help="Do not fail on vulnerabilities")
    return parser


def run_cli(args: Optional[List[str]] = None) -> int:
    """Entry point for command line execution."""

    parser = build_argument_parser()
    parsed = parser.parse_args(args=args)

    packages: List[PackageRecord] = []
    for path in parsed.paths:
        packages.extend(load_lockfile(path))

    try:
        results = verify(packages, fail_on_vulnerabilities=not parsed.allow_vulnerabilities)
    except RuntimeError as exc:
        print(f"❌ vulnerability detected: {exc}", file=sys.stderr)
        sys.exit(1)

    write_report(results, parsed.report)
    print(f"✅ verification complete, report saved to {parsed.report}")
    sys.exit(0)


if __name__ == "__main__":
    run_cli()
