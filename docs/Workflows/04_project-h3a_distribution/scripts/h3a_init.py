#!/usr/bin/env python3
"""
H3A System Initialization Script
=================================
Hybrid 3-Agent (H3A) system run initializer combining:
- MCA's state file architecture (ROADMAP, GATES_LEDGER, EVIDENCE_LOG)
- Dual-Agent's proven runs/ directory structure
- Agentic Prompt Guide's TDD enforcement

Creates a production-grade run environment with atomic writes,
evidence tracking, and gate-based progression.

Usage:
    python scripts/h3a_init.py [--task-brief "Description"]

Output:
    JSON with run_id, paths, and initialization status
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

# ========== CONFIGURATION ==========
ROOT = Path(__file__).resolve().parents[1]
RUNS_DIR = ROOT / "runs"
H3A_VERSION = "1.0.0"

# State file templates
STATE_FILES = [
    "ROADMAP.md",
    "CURRENT_TASK.json",
    "GATES_LEDGER.md",
    "EVIDENCE_LOG.md",
    "SESSION_HANDOFF.json"
]

# Agent artifact directories
AGENTS = ["planner", "executor", "validator"]


# ========== UTILITY FUNCTIONS ==========

def now_iso() -> str:
    """Return current UTC timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def gen_run_id() -> str:
    """Generate unique run identifier: YYYYMMDD-HHMMSS-uuid4."""
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    return f"{ts}-{uuid.uuid4()}"


def git_meta() -> Dict[str, Any]:
    """Capture current git metadata for reproducibility."""
    def run(cmd: List[str]) -> str:
        try:
            return subprocess.check_output(
                cmd, 
                cwd=ROOT, 
                stderr=subprocess.DEVNULL
            ).decode().strip()
        except Exception:
            return "unknown"
    
    return {
        "repo": ROOT.name,
        "branch": run(["git", "rev-parse", "--abbrev-ref", "HEAD"]),
        "commit": run(["git", "rev-parse", "HEAD"]),
        "commit_short": run(["git", "rev-parse", "--short", "HEAD"]),
        "remote": run(["git", "config", "--get", "remote.origin.url"]),
        "ci_green": False,  # Updated by CI on successful run
        "dirty": bool(run(["git", "status", "--porcelain"]))
    }


def compute_hash(content: str) -> str:
    """Compute SHA-256 hash for content integrity verification."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()[:16]


def atomic_write_json(path: Path, data: Dict[str, Any]) -> None:
    """
    Atomic write operation using temp file + rename.
    Prevents corruption from interrupted writes.
    """
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')  # POSIX compliance
    os.replace(tmp, path)


def atomic_write_text(path: Path, content: str) -> None:
    """Atomic write for text files (markdown, etc.)."""
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        f.write(content)
    os.replace(tmp, path)


# ========== STATE FILE TEMPLATES ==========

def create_roadmap(task_brief: Optional[str] = None) -> str:
    """Initialize ROADMAP.md with task brief or placeholder."""
    brief = task_brief or "[TO BE FILLED BY PLANNER]"
    return f"""# H3A System Roadmap
**Run Initialized:** {now_iso()}
**Status:** Planning Phase (G0)

---

## Task Brief
{brief}

---

## Overall Strategy
[TO BE FILLED BY PLANNER]

**Approach:** [e.g., Incremental TDD with atomic commits]
**Risk Mitigation:** [e.g., Feature flags for new APIs]

---

## Task Decomposition
[PLANNER WILL POPULATE WITH NUMBERED TASKS]

### Task Queue
- [ ] T001: [Task description]
- [ ] T002: [Task description]
- [ ] T003: [Task description]

---

## Success Criteria
[PLANNER DEFINES OVERALL DEFINITION OF DONE]

---

## Notes
- This roadmap is the **single source of truth** for strategic planning
- Each task follows RED→GREEN→REFACTOR TDD cycle
- Max 2 iterations per task before escalation
- All tasks gate through G0 (Planning) → G1 (Implementation) → G2 (Validation)
"""


def create_current_task() -> Dict[str, Any]:
    """Initialize CURRENT_TASK.json with empty template."""
    return {
        "task_id": None,
        "status": "awaiting_planner",
        "created_at": now_iso(),
        "assigned_to": "planner",
        "goal": None,
        "tdd_plan": {
            "red": None,
            "green": None,
            "refactor": None
        },
        "files_affected": [],
        "definition_of_done": [],
        "iteration_count": 0,
        "max_iterations": 2,
        "gate_status": "G0_pending",
        "notes": ""
    }


def create_gates_ledger() -> str:
    """Initialize GATES_LEDGER.md with gate progression tracking."""
    return f"""# H3A Gates Ledger
**Run Initialized:** {now_iso()}

---

## Gate Framework

| Gate | Owner | Purpose | Status |
|------|-------|---------|--------|
| **G0: Planning** | Planner | Task decomposition, TDD strategy | 🟡 Pending |
| **G1: Implementation** | Executor | TDD execution (RED→GREEN→REFACTOR) | ⚪ Not Started |
| **G2: Validation** | Validator | Comprehensive quality verification | ⚪ Not Started |
| **G3: Production-Ready** | System | All gates passed, ready for deploy | ⚪ Not Started |

---

## Gate History

### Gate Events Log
<!-- Format: [TIMESTAMP] GATE_ID - STATUS - AGENT - NOTES -->

---

## Current Gate: G0 (Planning)
**Entry Time:** {now_iso()}
**Owner:** Planner
**Status:** In Progress

**Entry Criteria:**
- ✅ Run initialized
- ✅ Task brief provided or pending
- ✅ State files created

**Exit Criteria:**
- ⬜ ROADMAP.md populated with strategy
- ⬜ Tasks decomposed into manageable chunks
- ⬜ CURRENT_TASK.json filled with first task
- ⬜ TDD plan defined (RED→GREEN→REFACTOR)
- ⬜ planner_report.json generated

**Evidence Required:**
- `state/ROADMAP.md` (complete)
- `state/CURRENT_TASK.json` (first task)
- `planner_report.json`
- `artifacts/planner/` (diagrams, research)

---

## Notes
- Gates enforce **evidence-based progression**
- No gate can be skipped
- Failed gates trigger remediation (max 2 iterations)
- Escalation protocol activates after 2 failed iterations
"""


def create_evidence_log() -> str:
    """Initialize EVIDENCE_LOG.md with artifact tracking."""
    return f"""# H3A Evidence Log
**Run Initialized:** {now_iso()}

---

## Purpose
This log is the **authoritative index** of all artifacts generated during the H3A workflow.
Each entry includes SHA-256 hash for integrity verification.

---

## Artifact Index

### Planner Artifacts
<!-- Example:
- `planner_report.json` - [hash:a3f5c8d2] - {now_iso()} - G0 completion report
- `artifacts/planner/architecture.png` - [hash:b8e1f9a4] - {now_iso()} - System diagram
-->

### Executor Artifacts
<!-- Example:
- `executor_report.json` - [hash:c7d3e1f8] - {now_iso()} - TDD execution report
- `artifacts/executor/test_output_red.txt` - [hash:d9a2b5c3] - {now_iso()} - RED phase evidence
- `artifacts/executor/test_output_green.txt` - [hash:e4f6c1d9] - {now_iso()} - GREEN phase evidence
- `artifacts/executor/coverage_delta.json` - [hash:f1e8d2a5] - {now_iso()} - Coverage increase proof
-->

### Validator Artifacts
<!-- Example:
- `validator_report.json` - [hash:a9c3f7e1] - {now_iso()} - Validation verdict
- `artifacts/validator/security_scan.json` - [hash:b2d8f4c6] - {now_iso()} - OWASP scan results
- `artifacts/validator/mutation_report.txt` - [hash:c5e1a9f3] - {now_iso()} - Mutation testing results
-->

---

## Hash Verification
To verify artifact integrity:
```bash
# Linux/Mac
sha256sum <file> | cut -c1-16

# Or use Python
python3 -c "import hashlib; print(hashlib.sha256(open('<file>','rb').read()).hexdigest()[:16])"
```

---

## Artifact Lifecycle
1. **Created** - Agent generates artifact
2. **Logged** - Added to this index with hash
3. **Referenced** - Used as evidence in gate progression
4. **Archived** - Persisted in `runs/<run-id>/artifacts/`

---

## Compliance Mapping
- **OWASP LLM Top-10:** Validator security scan results
- **TDD Compliance:** Executor RED→GREEN evidence
- **Coverage Requirements:** Executor coverage delta reports
- **Code Quality:** Validator lint/type check results
"""


def create_session_handoff() -> Dict[str, Any]:
    """Initialize SESSION_HANDOFF.json for agent-to-agent transitions."""
    return {
        "run_id": None,  # Filled by init
        "current_agent": "planner",
        "next_agent": None,
        "handoff_time": None,
        "gate_status": "G0_pending",
        "payload": {
            "task_id": None,
            "context": "Run initialized, awaiting Planner to create roadmap",
            "files_to_review": ["state/ROADMAP.md", "state/CURRENT_TASK.json"],
            "action_required": "Planner must decompose task and fill ROADMAP.md"
        },
        "history": []
    }


def create_state_json(run_id: str) -> Dict[str, Any]:
    """Create main state.json (dual-agent compatibility layer)."""
    return {
        "run_id": run_id,
        "h3a_version": H3A_VERSION,
        "created_at": now_iso(),
        "meta": git_meta(),
        "gates": {
            "G0_planning": "pending",
            "G1_implementation": "not_started",
            "G2_validation": "not_started",
            "G3_production_ready": "not_started"
        },
        "steps": []  # Append-only execution history (dual-agent pattern)
    }


def create_planner_report(run_id: str) -> Dict[str, Any]:
    """Initialize planner_report.json."""
    return {
        "run_id": run_id,
        "agent": "planner",
        "reports": []
    }


def create_executor_report(run_id: str) -> Dict[str, Any]:
    """Initialize executor_report.json."""
    return {
        "run_id": run_id,
        "agent": "executor",
        "tdd_cycles": []
    }


def create_validator_report(run_id: str) -> Dict[str, Any]:
    """Initialize validator_report.json."""
    return {
        "run_id": run_id,
        "agent": "validator",
        "verdicts": []
    }


# ========== MAIN INITIALIZATION ==========

def main():
    """Initialize H3A run with production-grade state management."""
    parser = argparse.ArgumentParser(
        description="Initialize H3A (Hybrid 3-Agent) system run"
    )
    parser.add_argument(
        "--task-brief",
        type=str,
        help="Optional task brief to pre-populate ROADMAP.md"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print detailed initialization steps"
    )
    args = parser.parse_args()

    # Generate unique run ID
    run_id = gen_run_id()
    run_dir = RUNS_DIR / run_id

    if args.verbose:
        print(f"[H3A Init] Creating run: {run_id}", file=sys.stderr)

    # Create directory structure
    state_dir = run_dir / "state"
    state_dir.mkdir(parents=True, exist_ok=True)

    for agent in AGENTS:
        (run_dir / "artifacts" / agent).mkdir(parents=True, exist_ok=True)

    if args.verbose:
        print(f"[H3A Init] Created directory structure", file=sys.stderr)

    # Initialize state files
    atomic_write_text(
        state_dir / "ROADMAP.md",
        create_roadmap(args.task_brief)
    )
    
    current_task = create_current_task()
    atomic_write_json(state_dir / "CURRENT_TASK.json", current_task)

    atomic_write_text(
        state_dir / "GATES_LEDGER.md",
        create_gates_ledger()
    )

    atomic_write_text(
        state_dir / "EVIDENCE_LOG.md",
        create_evidence_log()
    )

    session_handoff = create_session_handoff()
    session_handoff["run_id"] = run_id
    atomic_write_json(state_dir / "SESSION_HANDOFF.json", session_handoff)

    if args.verbose:
        print(f"[H3A Init] Created MCA-style state files", file=sys.stderr)

    # Initialize main state.json (dual-agent compatibility)
    state = create_state_json(run_id)
    atomic_write_json(run_dir / "state.json", state)

    # Initialize agent report files
    atomic_write_json(run_dir / "planner_report.json", create_planner_report(run_id))
    atomic_write_json(run_dir / "executor_report.json", create_executor_report(run_id))
    atomic_write_json(run_dir / "validator_report.json", create_validator_report(run_id))

    if args.verbose:
        print(f"[H3A Init] Created agent report files", file=sys.stderr)

    # Create README in run directory
    readme_content = f"""# H3A Run: {run_id}
**Created:** {now_iso()}
**H3A Version:** {H3A_VERSION}

## Directory Structure
```
{run_id}/
├── state/                      # MCA-style state files (SSOT)
│   ├── ROADMAP.md             # Overall plan & task queue
│   ├── CURRENT_TASK.json      # Active task being worked on
│   ├── GATES_LEDGER.md        # G0→G3 progression log
│   ├── EVIDENCE_LOG.md        # Artifact index with hashes
│   └── SESSION_HANDOFF.json   # Agent-to-agent transitions
├── state.json                 # Append-only execution history
├── planner_report.json        # Planner outputs
├── executor_report.json       # Executor TDD cycles
├── validator_report.json      # Validator verdicts
└── artifacts/
    ├── planner/               # Plans, diagrams, research
    ├── executor/              # Test outputs, coverage reports
    └── validator/             # Scan results, verification evidence
```

## Workflow
1. **Planner (G0):** Reads/updates ROADMAP.md, creates CURRENT_TASK.json
2. **Executor (G1):** Implements task with TDD (RED→GREEN→REFACTOR)
3. **Validator (G2):** Verifies all quality gates (TDD, security, coverage, etc.)
4. **Repeat:** Until roadmap complete (G3)

## State Files (Single Source of Truth)
- **ROADMAP.md** - Strategic plan, task decomposition
- **CURRENT_TASK.json** - Active task details, TDD plan
- **GATES_LEDGER.md** - Gate status, entry/exit criteria
- **EVIDENCE_LOG.md** - Artifact catalog with integrity hashes
- **SESSION_HANDOFF.json** - Agent transition payload

## Agent Reports
- **planner_report.json** - Task decomposition, research findings
- **executor_report.json** - TDD evidence, coverage delta, DoD checklist
- **validator_report.json** - Verification results, pass/fail verdicts

## Best Practices
- **Atomic Writes:** All state changes use temp file + replace
- **Append-Only History:** state.json never rewrites, only appends
- **Evidence-Based:** All gate progressions require artifact proof
- **Hash Verification:** EVIDENCE_LOG.md tracks artifact integrity
- **Iteration Limits:** Max 2 attempts per task before escalation

## Next Steps
1. Invoke **Planner** agent
2. Planner reads `state/ROADMAP.md` and fills in strategy
3. Planner creates first task in `state/CURRENT_TASK.json`
4. Human bridges to **Executor** with `state/CURRENT_TASK.json`
5. Executor implements with TDD, writes `executor_report.json`
6. Human bridges to **Validator** with `executor_report.json`
7. Validator verifies, writes `validator_report.json`
8. Repeat cycle until roadmap complete
"""
    atomic_write_text(run_dir / "README.md", readme_content)

    if args.verbose:
        print(f"[H3A Init] Initialization complete!", file=sys.stderr)

    # Output initialization summary as JSON
    output = {
        "status": "success",
        "run_id": run_id,
        "h3a_version": H3A_VERSION,
        "run_dir": str(run_dir),
        "created_at": now_iso(),
        "state_files": {
            "roadmap": str(state_dir / "ROADMAP.md"),
            "current_task": str(state_dir / "CURRENT_TASK.json"),
            "gates_ledger": str(state_dir / "GATES_LEDGER.md"),
            "evidence_log": str(state_dir / "EVIDENCE_LOG.md"),
            "session_handoff": str(state_dir / "SESSION_HANDOFF.json"),
            "state_json": str(run_dir / "state.json")
        },
        "agent_reports": {
            "planner": str(run_dir / "planner_report.json"),
            "executor": str(run_dir / "executor_report.json"),
            "validator": str(run_dir / "validator_report.json")
        },
        "artifacts_dirs": {
            "planner": str(run_dir / "artifacts" / "planner"),
            "executor": str(run_dir / "artifacts" / "executor"),
            "validator": str(run_dir / "artifacts" / "validator")
        },
        "meta": git_meta(),
        "next_action": "Invoke Planner agent to populate ROADMAP.md and CURRENT_TASK.json"
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        error_output = {
            "status": "error",
            "error": str(e),
            "type": type(e).__name__
        }
        print(json.dumps(error_output, indent=2))
        sys.exit(1)