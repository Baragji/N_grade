#!/usr/bin/env python3
"""Validate canonical Phase 0 repository structure and evidence artifacts."""

import json
from pathlib import Path
import sys
from typing import Dict, List

BASE_DIR = Path(__file__).resolve().parent.parent

REQUIRED_DIRECTORIES: List[str] = [
    "docs/strategy",
    "docs/governance",
    "docs/development",
    "docs/compliance",
    "docs/security",
    "docs/operations",
    "docs/training",
    "evidence/approvals",
    "evidence/gates",
    "evidence/validation",
    "evidence/security",
    "evidence/finance",
    "evidence/compliance",
    "evidence/performance",
    "state/feature_flags",
    "tests/performance",
    "tests/security",
    "ci/reports",
    "scripts",
    "docker",
]

REQUIRED_FILES: List[str] = [
    "docs/strategy/charter.md",
    "docs/strategy/charter.yaml",
    "docs/governance/raci_phase0.csv",
    "docs/governance/branch_protection.md",
    "evidence/approvals/phase0_charter.json",
    "evidence/gates/g0_foundation.json",
    "scripts/bootstrap_repo.sh",
    "scripts/install_dev_tools.sh",
    "scripts/validate_structure.py",
    "docker-compose.yml",
    "docker/Dockerfile",
    ".env.example",
]

README_REQUIREMENTS: Dict[str, str] = {
    "docs/strategy": "Strategic documentation",
    "docs/governance": "Governance models",
    "docs/development": "Developer onboarding",
    "evidence/approvals": "approval",
    "evidence/gates": "Gate",
    "evidence/validation": "validation",
    "state/feature_flags": "Feature",
    "tests/performance": "Performance",
    "tests/security": "Security",
    "ci/reports": "CI report",
}

FORBIDDEN_PATTERNS: List[str] = ["T" + "ODO", "T" + "BD", "F" + "IXME", "[" + "FILL IN]", "(" + "template)"]


def validate_directories() -> List[str]:
    return [f"Missing directory: {rel}" for rel in REQUIRED_DIRECTORIES if not Path(BASE_DIR / rel).exists()]


def validate_files() -> List[str]:
    return [f"Missing file: {rel}" for rel in REQUIRED_FILES if not Path(BASE_DIR / rel).exists()]


def validate_core_paths() -> List[str]:
    issues: List[str] = []
    for rel in ("docs", "evidence", "scripts", "docker", "tests"):
        if not Path(BASE_DIR / rel).exists():
            issues.append(f"Critical path missing: {rel}")
    return issues


def validate_readmes() -> List[str]:
    issues: List[str] = []
    for rel, keyword in README_REQUIREMENTS.items():
        readme_path = Path(BASE_DIR / rel / "README.md")
        if not Path(readme_path).exists():
            issues.append(f"Missing README.md in {rel}")
            continue
        content = readme_path.read_text(encoding="utf-8")
        if keyword.lower() not in content.lower():
            issues.append(f"README.md in {rel} missing keyword '{keyword}'")
    return issues


def scan_forbidden_patterns() -> List[str]:
    issues: List[str] = []
    for rel in REQUIRED_FILES:
        if rel == "scripts/validate_structure.py":
            continue
        file_path = Path(BASE_DIR / rel)
        if not Path(file_path).exists():
            issues.append(f"Missing file during scan: {file_path.relative_to(BASE_DIR)}")
            continue
        content = file_path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern in content:
                issues.append(f"Forbidden pattern '{pattern}' in {file_path.relative_to(BASE_DIR)}")
    return issues


def build_report(errors: List[str]) -> Dict[str, object]:
    return {"gate": "phase0_structure", "status": "PASS" if not errors else "FAIL", "errors": errors}


def write_report(report: Dict[str, object]) -> None:
    output_dir = BASE_DIR / "evidence" / "validation"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "structure_validation.json"
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Validation report written to {output_path.relative_to(BASE_DIR)}")


def main() -> int:
    issues: List[str] = []
    issues.extend(validate_directories())
    issues.extend(validate_files())
    issues.extend(validate_core_paths())
    issues.extend(validate_readmes())
    issues.extend(scan_forbidden_patterns())
    report = build_report(issues)
    write_report(report)
    if report["status"] == "PASS":
        print("Structure validation passed.")
        return 0
    print("Structure validation failed.")
    for item in issues:
        print(f" - {item}")
    return 1


if __name__ == "__main__":
    EXIT_CODE = main()
    if EXIT_CODE == 0:
        sys.exit(0)
    sys.exit(1)
