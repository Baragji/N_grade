# H3A State Specification
**Version:** 1.0.0  
**Last Updated:** 2025-01-XX

---

## Purpose

The H3A (Hybrid 3-Agent) state specification defines a **production-grade, evidence-based state management system** that enables:

1. **Tiny-context agents** to operate without conversation memory
2. **Append-only history** preventing state corruption
3. **Evidence-based gate progression** (no artifact = no progress)
4. **Atomic operations** preventing concurrent write conflicts
5. **Audit trails** for compliance and debugging

This specification combines:
- **MCA's state files** (ROADMAP, GATES_LEDGER, EVIDENCE_LOG) for organizational clarity
- **Dual-Agent's proven patterns** (runs/ directory, state.json, artifacts/)
- **TDD enforcement** (RED→GREEN evidence tracking, coverage deltas)

---

## Directory Structure

Every H3A run creates an immutable, self-contained directory:

```
runs/<run-id>/
├── state/                          # MCA-style state files (SSOT)
│   ├── ROADMAP.md                 # Overall strategic plan
│   ├── CURRENT_TASK.json          # Active task being executed
│   ├── GATES_LEDGER.md            # G0→G3 progression log
│   ├── EVIDENCE_LOG.md            # Artifact catalog with hashes
│   └── SESSION_HANDOFF.json       # Agent-to-agent payload
│
├── state.json                      # Append-only execution history
│
├── planner_report.json             # Planner outputs
├── executor_report.json            # Executor TDD cycles
├── validator_report.json           # Validator verdicts
│
├── artifacts/                      # Evidence storage
│   ├── planner/                   # Plans, diagrams, research
│   ├── executor/                  # Test outputs, coverage reports
│   └── validator/                 # Scan results, verification
│
└── README.md                       # Run documentation
```

### Run Identifier Format
```
<YYYYMMDD>-<HHMMSS>-<uuid4>
Example: 20250929-134215-8b6f8b9a-7c9f-4c5e-8c6a-2f0f0d2e9c1a
```

**Properties:**
- ✅ Sortable by creation time
- ✅ Globally unique (UUID collision probability < 10⁻³⁶)
- ✅ Human-readable timestamp prefix
- ✅ Compatible with filesystems (no special characters)

---

## State Files (Single Source of Truth)

### 1. `state/ROADMAP.md`

**Owner:** Planner  
**Purpose:** Strategic plan, task decomposition, success criteria  
**Format:** Markdown

**Schema:**
```markdown
# H3A System Roadmap
**Run Initialized:** <ISO-8601-timestamp>
**Status:** <Planning Phase | Execution Phase | Validation Phase | Complete>

---

## Task Brief
<User-provided or Planner-generated description>

---

## Overall Strategy
**Approach:** <e.g., Incremental TDD with feature flags>
**Risk Mitigation:** <e.g., Rollback plan, monitoring strategy>

---

## Task Decomposition

### Task Queue
- [ ] T001: <Task description>
- [ ] T002: <Task description>
- [x] T003: <Task description> ✅ (Completed: <timestamp>)

---

## Success Criteria
- [ ] All tests passing (100% pass rate)
- [ ] Coverage ≥ 90%
- [ ] Mutation score ≥ 85%
- [ ] Security scan clean (OWASP)
- [ ] Lint/type checks passing
- [ ] A11y compliance (if UI changes)

---

## Notes
<Rationale, architectural decisions, trade-offs>
```

**Update Protocol:**
- Planner **creates** on first run
- Planner **appends** tasks as decomposition evolves
- Executor **marks tasks complete** with timestamps
- Never delete history, only add completion markers

---

### 2. `state/CURRENT_TASK.json`

**Owner:** Planner (creates), Executor (updates status)  
**Purpose:** Active task specification with TDD plan  
**Format:** JSON

**Schema:**
```json
{
  "task_id": "T001",
  "status": "in_progress",
  "created_at": "2025-09-29T13:42:15Z",
  "assigned_to": "executor",
  "goal": "Add user authentication with JWT tokens",
  "context": "Implement secure token-based auth following OWASP guidelines",
  
  "tdd_plan": {
    "red": "Write test_jwt_generation() expecting valid token structure",
    "green": "Implement generate_jwt() to pass test",
    "refactor": "Extract key management to separate module"
  },
  
  "files_affected": [
    "src/auth/jwt.py",
    "tests/test_auth.py",
    "src/config/keys.py"
  ],
  
  "definition_of_done": [
    "Test coverage ≥ 95% for auth module",
    "Token expiration validated",
    "Secret key rotation documented",
    "Security scan passes (no JWT vulnerabilities)"
  ],
  
  "iteration_count": 0,
  "max_iterations": 2,
  "gate_status": "G0_passed",
  
  "dependencies": ["T000"],
  "blocked_by": [],
  
  "notes": "Using PyJWT library, requires HMAC SHA-256"
}
```

**State Machine:**
```
awaiting_planner → in_progress → validation → complete
                             ↓
                        failed (retry if iteration_count < 2)
```

**Update Protocol:**
- Planner writes on task creation
- Executor updates `status`, `iteration_count`, `gate_status`
- Atomic write using temp file + replace
- Never delete, archive to ROADMAP on completion

---

### 3. `state/GATES_LEDGER.md`

**Owner:** System (all agents append)  
**Purpose:** Gate progression tracking with entry/exit criteria  
**Format:** Markdown

**Schema:**
```markdown
# H3A Gates Ledger
**Run Initialized:** <timestamp>

---

## Gate Framework

| Gate | Owner | Purpose | Status |
|------|-------|---------|--------|
| **G0: Planning** | Planner | Task decomposition, TDD strategy | 🟢 Passed |
| **G1: Implementation** | Executor | TDD execution | 🟡 In Progress |
| **G2: Validation** | Validator | Quality verification | ⚪ Not Started |
| **G3: Production-Ready** | System | Ready for deploy | ⚪ Not Started |

**Status Legend:**
- 🟢 Passed
- 🟡 In Progress
- 🔴 Failed (remediation needed)
- ⚪ Not Started

---

## Gate History

### Gate Events Log
[2025-09-29T13:42:15Z] G0_planning - STARTED - planner - Task decomposition initiated
[2025-09-29T14:05:30Z] G0_planning - PASSED - planner - ROADMAP complete, CURRENT_TASK created
[2025-09-29T14:10:00Z] G1_implementation - STARTED - executor - TDD cycle T001 begins
[2025-09-29T14:45:00Z] G1_implementation - PASSED - executor - All tests green, coverage +5.2%

---

## Current Gate: <Gate ID>
**Entry Time:** <timestamp>
**Owner:** <agent>
**Status:** <In Progress | Passed | Failed>

**Entry Criteria:**
- ✅ <criterion 1>
- ⬜ <criterion 2>

**Exit Criteria:**
- ⬜ <criterion 1>
- ⬜ <criterion 2>

**Evidence Required:**
- `<artifact path>` - <description>
- `<artifact path>` - <description>

**Blockers:**
- <None | Description of blocker>

---

## Escalation Protocol
**Trigger:** Gate failure after 2 iterations  
**Action:** Human review required  
**Evidence:** See EVIDENCE_LOG.md for artifact hashes
```

**Update Protocol:**
- Agents append to "Gate Events Log" on status changes
- Use ISO 8601 timestamps with UTC timezone
- Include agent name and brief notes
- Never delete history

---

### 4. `state/EVIDENCE_LOG.md`

**Owner:** All agents  
**Purpose:** Artifact catalog with integrity verification  
**Format:** Markdown

**Schema:**
```markdown
# H3A Evidence Log
**Run Initialized:** <timestamp>

---

## Purpose
Authoritative index of all artifacts with SHA-256 hashes for integrity verification.

---

## Artifact Index

### Planner Artifacts
- `planner_report.json` - [hash:a3f5c8d21f4e9b76] - 2025-09-29T14:05:30Z - Task decomposition report
- `artifacts/planner/architecture.png` - [hash:b8e1f9a47c3d2e56] - 2025-09-29T14:03:15Z - System diagram

### Executor Artifacts
- `executor_report.json` - [hash:c7d3e1f89a2b5c14] - 2025-09-29T14:45:00Z - TDD cycle T001 complete
- `artifacts/executor/test_output_red.txt` - [hash:d9a2b5c38f1e7d46] - 2025-09-29T14:15:00Z - RED phase (1 test failing)
- `artifacts/executor/test_output_green.txt` - [hash:e4f6c1d92a8b3f57] - 2025-09-29T14:30:00Z - GREEN phase (all tests passing)
- `artifacts/executor/coverage_delta.json` - [hash:f1e8d2a54c9b7f36] - 2025-09-29T14:45:00Z - Coverage +5.2%

### Validator Artifacts
- `validator_report.json` - [hash:a9c3f7e18d5b2f64] - 2025-09-29T15:00:00Z - Validation PASSED
- `artifacts/validator/security_scan.json` - [hash:b2d8f4c69a3e1f75] - 2025-09-29T14:55:00Z - OWASP scan clean
- `artifacts/validator/mutation_report.txt` - [hash:c5e1a9f37b4d8c26] - 2025-09-29T14:58:00Z - 91.3% mutation score

---

## Hash Verification
```bash
# Verify artifact integrity
sha256sum <file> | cut -c1-16  # Linux/Mac
```

---

## Compliance Mapping
- **OWASP LLM Top-10:** `artifacts/validator/security_scan.json`
- **TDD RED→GREEN:** `artifacts/executor/test_output_*.txt`
- **Coverage Delta:** `artifacts/executor/coverage_delta.json`
- **Mutation Testing:** `artifacts/validator/mutation_report.txt`
```

**Update Protocol:**
- Agents append entries when creating artifacts
- Hash format: First 16 chars of SHA-256 hex digest
- Include timestamp and brief description
- Never delete entries (immutable audit log)

---

### 5. `state/SESSION_HANDOFF.json`

**Owner:** System (agents update on transitions)  
**Purpose:** Agent-to-agent handoff payload  
**Format:** JSON

**Schema:**
```json
{
  "run_id": "20250929-134215-8b6f8b9a-...",
  "current_agent": "executor",
  "next_agent": "validator",
  "handoff_time": "2025-09-29T14:45:00Z",
  "gate_status": "G1_passed",
  
  "payload": {
    "task_id": "T001",
    "context": "TDD cycle complete, all tests passing, coverage +5.2%",
    "files_to_review": [
      "state/CURRENT_TASK.json",
      "executor_report.json",
      "artifacts/executor/test_output_green.txt"
    ],
    "action_required": "Validator must verify TDD compliance, security, coverage, and all quality gates"
  },
  
  "history": [
    {
      "from": "planner",
      "to": "executor",
      "time": "2025-09-29T14:05:30Z",
      "gate": "G0_passed",
      "notes": "Task T001 ready for implementation"
    },
    {
      "from": "executor",
      "to": "validator",
      "time": "2025-09-29T14:45:00Z",
      "gate": "G1_passed",
      "notes": "Implementation complete, awaiting validation"
    }
  ]
}
```

**Update Protocol:**
- Agent appends to `history[]` when completing work
- Updates `current_agent`, `next_agent`, `gate_status`
- Atomic write (temp file + replace)
- Human reads this to know next agent to invoke

---

### 6. `state.json` (Dual-Agent Compatibility Layer)

**Owner:** System  
**Purpose:** Append-only execution history (audit log)  
**Format:** JSON

**Schema:**
```json
{
  "run_id": "20250929-134215-8b6f8b9a-...",
  "h3a_version": "1.0.0",
  "created_at": "2025-09-29T13:42:15Z",
  
  "meta": {
    "repo": "18_Jobs_Excellense_Coding",
    "branch": "feature/h3a-system",
    "commit": "a3f5c8d21f4e9b76...",
    "commit_short": "a3f5c8d",
    "remote": "git@github.com:user/repo.git",
    "ci_green": false,
    "dirty": true
  },
  
  "gates": {
    "G0_planning": "passed",
    "G1_implementation": "passed",
    "G2_validation": "in_progress",
    "G3_production_ready": "not_started"
  },
  
  "steps": [
    {
      "task_id": "T001",
      "agent": "planner",
      "timestamp": "2025-09-29T14:05:30Z",
      "summary": "Task decomposition complete",
      "gate": "G0_planning",
      "status": "passed",
      "artifacts": [
        "planner_report.json",
        "artifacts/planner/architecture.png"
      ]
    },
    {
      "task_id": "T001",
      "agent": "executor",
      "timestamp": "2025-09-29T14:45:00Z",
      "summary": "TDD cycle complete: RED→GREEN→REFACTOR",
      "gate": "G1_implementation",
      "status": "passed",
      "files_changed": ["src/auth/jwt.py", "tests/test_auth.py"],
      "commands_run": [
        {
          "cmd": "pytest tests/test_auth.py -v",
          "exit_code": 0,
          "artifact": "artifacts/executor/test_output_green.txt"
        },
        {
          "cmd": "coverage report --format=json",
          "exit_code": 0,
          "artifact": "artifacts/executor/coverage_delta.json"
        }
      ],
      "tdd_evidence": {
        "red": "artifacts/executor/test_output_red.txt",
        "green": "artifacts/executor/test_output_green.txt"
      },
      "coverage_delta": "+5.2%",
      "artifacts": [
        "executor_report.json",
        "artifacts/executor/"
      ],
      "notes": "All tests passing, coverage target met"
    }
  ]
}
```

**Update Protocol:**
- Agents **append** one `steps[]` entry per completed task
- Never rewrite or delete history
- Corrections add a new step with `corrects: <task_id>`
- Atomic write using temp file + replace

---

## Agent Report Files

### `planner_report.json`

**Schema:**
```json
{
  "run_id": "...",
  "agent": "planner",
  "reports": [
    {
      "task_id": "T001",
      "timestamp": "2025-09-29T14:05:30Z",
      "roadmap_status": "updated",
      "tasks_created": ["T001", "T002", "T003"],
      "research_findings": [
        "PyJWT is industry standard for JWT handling",
        "HMAC SHA-256 recommended by OWASP"
      ],
      "tdd_strategy": {
        "T001": {
          "red": "Write test_jwt_generation() expecting token structure",
          "green": "Implement generate_jwt() to pass",
          "refactor": "Extract key management"
        }
      },
      "artifacts": [
        "artifacts/planner/architecture.png"
      ],
      "gate_status": "G0_passed"
    }
  ]
}
```

---

### `executor_report.json`

**Schema:**
```json
{
  "run_id": "...",
  "agent": "executor",
  "tdd_cycles": [
    {
      "task_id": "T001",
      "timestamp": "2025-09-29T14:45:00Z",
      "tdd_phases": {
        "red": {
          "test_file": "tests/test_auth.py",
          "test_name": "test_jwt_generation",
          "failure_output": "artifacts/executor/test_output_red.txt",
          "timestamp": "2025-09-29T14:15:00Z"
        },
        "green": {
          "implementation_file": "src/auth/jwt.py",
          "test_output": "artifacts/executor/test_output_green.txt",
          "timestamp": "2025-09-29T14:30:00Z"
        },
        "refactor": {
          "changes": "Extracted key management to src/config/keys.py",
          "test_still_passing": true,
          "timestamp": "2025-09-29T14:40:00Z"
        }
      },
      "coverage_delta": "+5.2%",
      "coverage_absolute": "94.2%",
      "files_changed": [
        "src/auth/jwt.py",
        "tests/test_auth.py",
        "src/config/keys.py"
      ],
      "definition_of_done": [
        {"criterion": "Coverage ≥ 95% for auth module", "met": false, "actual": "94.2%"},
        {"criterion": "Token expiration validated", "met": true},
        {"criterion": "Secret key rotation documented", "met": true},
        {"criterion": "Security scan passes", "met": true}
      ],
      "iteration_count": 1,
      "gate_status": "G1_passed",
      "artifacts": [
        "artifacts/executor/test_output_red.txt",
        "artifacts/executor/test_output_green.txt",
        "artifacts/executor/coverage_delta.json"
      ]
    }
  ]
}
```

---

### `validator_report.json`

**Schema:**
```json
{
  "run_id": "...",
  "agent": "validator",
  "verdicts": [
    {
      "task_id": "T001",
      "timestamp": "2025-09-29T15:00:00Z",
      "status": "pass",
      "verification_results": {
        "tdd_compliance": {
          "status": "pass",
          "red_evidence": "artifacts/executor/test_output_red.txt",
          "green_evidence": "artifacts/executor/test_output_green.txt",
          "notes": "Clear RED→GREEN transition verified"
        },
        "tests": {
          "status": "pass",
          "total": 47,
          "passed": 47,
          "failed": 0,
          "skipped": 0
        },
        "coverage": {
          "status": "pass",
          "absolute": "94.2%",
          "delta": "+5.2%",
          "threshold": "90%"
        },
        "mutation": {
          "status": "pass",
          "score": "91.3%",
          "threshold": "85%",
          "report": "artifacts/validator/mutation_report.txt"
        },
        "security": {
          "status": "pass",
          "scan_type": "OWASP",
          "vulnerabilities": 0,
          "report": "artifacts/validator/security_scan.json"
        },
        "lint": {
          "status": "pass",
          "errors": 0,
          "warnings": 0
        },
        "type_check": {
          "status": "pass",
          "tool": "mypy",
          "errors": 0
        },
        "accessibility": {
          "status": "not_applicable",
          "notes": "No UI changes in this task"
        },
        "dod_checklist": {
          "status": "partial",
          "total": 4,
          "met": 3,
          "unmet": ["Coverage ≥ 95% (actual: 94.2%)"]
        }
      },
      "approval_for_next_task": true,
      "remediation_plan": null,
      "gate_status": "G2_passed",
      "artifacts": [
        "artifacts/validator/security_scan.json",
        "artifacts/validator/mutation_report.txt"
      ]
    }
  ]
}
```

---

## Write Operations (Best Practices)

### Atomic Write Protocol

**Problem:** Concurrent writes or interrupted writes cause corruption.

**Solution:** Temp file + atomic rename

```python
import json
import os
from pathlib import Path

def atomic_write_json(path: Path, data: dict):
    """Write JSON atomically to prevent corruption."""
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')  # POSIX compliance
    os.replace(tmp, path)  # Atomic on POSIX, nearly atomic on Windows
```

**Guarantees:**
- ✅ No partial writes visible to readers
- ✅ Either old or new content, never corrupted
- ✅ Safe for concurrent reads during write

---

### Append-Only Pattern

**Rule:** Never delete or rewrite history in `state.json` or `GATES_LEDGER.md`

**Corrections:**
```json
{
  "task_id": "T001-correction",
  "corrects": "T001",
  "reason": "Coverage calculation error, actual is 94.2% not 95%",
  "corrected_values": {
    "coverage_absolute": "94.2%"
  }
}
```

**Benefits:**
- ✅ Full audit trail
- ✅ Debug history preserved
- ✅ No lost information
- ✅ Compliance-friendly

---

### Hash Verification

**Purpose:** Detect artifact tampering or corruption

**Implementation:**
```python
import hashlib

def compute_hash(file_path: str) -> str:
    """Compute SHA-256 hash (first 16 chars)."""
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()[:16]
```

**Usage:**
```python
hash_val = compute_hash("artifacts/executor/test_output_green.txt")
# Add to EVIDENCE_LOG.md:
# - `artifacts/executor/test_output_green.txt` - [hash:e4f6c1d92a8b3f57] - ...
```

---

## State Machine

### Task Lifecycle
```
[PLANNER CREATES]
     │
     ├─→ awaiting_planner
     │        │
     │   [PLANNER FILLS]
     │        ↓
     ├─→ ready_for_execution (G0_passed)
     │        │
     │  [EXECUTOR STARTS]
     │        ↓
     ├─→ in_progress (G1_in_progress)
     │        │
     │  [EXECUTOR COMPLETES TDD]
     │        ↓
     ├─→ awaiting_validation (G1_passed)
     │        │
     │  [VALIDATOR STARTS]
     │        ↓
     ├─→ validation (G2_in_progress)
     │        │
     │        ├─→ [PASS] → complete (G2_passed)
     │        │
     │        └─→ [FAIL] → remediation_needed
     │                  │
     │          [iteration_count < 2?]
     │                  │
     │                  ├─→ YES → back to in_progress
     │                  └─→ NO → escalation_required
```

### Gate Progression
```
G0 (Planning) ────→ G1 (Implementation) ────→ G2 (Validation) ────→ G3 (Production-Ready)
     │                    │                         │                        │
   Planner             Executor                 Validator                 System
     │                    │                         │                        │
   ROADMAP             TDD Cycle                All Gates Pass         Deploy Ready
```

---

## Backward Compatibility

### With Dual-Agent System

The H3A system maintains compatibility with existing dual-agent tooling:

| Dual-Agent File | H3A Equivalent | Notes |
|-----------------|----------------|-------|
| `state.json` | `state.json` | Identical schema, H3A adds `gates` field |
| `executor_report.json` | `executor_report.json` | Enhanced with `tdd_phases`, `coverage_delta` |
| `validator_report.json` | `validator_report.json` | Enhanced with comprehensive verification |
| `artifacts/executor/` | `artifacts/executor/` | Same structure |
| `artifacts/validator/` | `artifacts/validator/` | Same structure |
| N/A | `state/ROADMAP.md` | **NEW** - Strategic layer |
| N/A | `state/CURRENT_TASK.json` | **NEW** - Task specification |
| N/A | `state/GATES_LEDGER.md` | **NEW** - Gate tracking |
| N/A | `state/EVIDENCE_LOG.md` | **NEW** - Artifact catalog |
| N/A | `state/SESSION_HANDOFF.json` | **NEW** - Agent transitions |

**Migration Path:**
1. Existing runs in `runs/<run-id>/` continue to work
2. New runs use `h3a_init.py` instead of `dual_agent_init.py`
3. Old reports can be read by H3A-aware agents
4. H3A reports are backward-compatible (superset of dual-agent schema)

---

## Compliance & Audit

### Artifact Integrity
- All artifacts logged in `EVIDENCE_LOG.md` with SHA-256 hashes
- Hash verification detects tampering or corruption
- Immutable audit trail (append-only logs)

### Evidence-Based Gates
- Each gate requires artifact proof (no artifact = no progress)
- `GATES_LEDGER.md` tracks entry/exit criteria and evidence
- Validator verifies artifact presence and integrity

### Regulatory Compliance
- **GDPR:** Audit logs for AI-generated code changes
- **SOC 2:** Evidence of testing, security scanning
- **ISO 42001 (AI Management):** Traceable AI agent actions
- **OWASP ASVS:** Security scan results in artifacts

### Retention
- Runs are immutable and never deleted automatically
- Human can archive old runs (e.g., `mv runs/old-run-id/ archive/`)
- Recommended retention: 90 days for active, indefinite for audits

---

## Performance Considerations

### File Sizes
- `ROADMAP.md`: ~5-20 KB (grows with task count)
- `CURRENT_TASK.json`: ~2-5 KB (single task)
- `GATES_LEDGER.md`: ~10-50 KB (one line per gate event)
- `EVIDENCE_LOG.md`: ~5-30 KB (one line per artifact)
- `state.json`: ~50-500 KB (grows with step count)

**Scalability:**
- For runs with >100 tasks, consider pagination or archiving
- `state.json` can grow large; consider chunking if >10 MB

### Concurrent Access
- **Reads:** Always safe (state files are immutable snapshots)
- **Writes:** Use atomic write protocol (temp + replace)
- **Conflicts:** Agents run sequentially (Planner → Executor → Validator), no concurrency

### Filesystem Requirements
- **Atomic rename:** Required (supported on all POSIX systems, Windows 10+)
- **UTF-8 support:** Required for markdown files
- **Case-sensitive:** Recommended (but H3A tolerates case-insensitive FS)

---

## Error Handling

### Missing State Files
```python
if not (run_dir / "state" / "CURRENT_TASK.json").exists():
    raise FileNotFoundError(
        "CURRENT_TASK.json missing. Was the run initialized with h3a_init.py?"
    )
```

### Corrupted JSON
```python
try:
    with open(path) as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    # Check for .tmp file (interrupted write)
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    if tmp_path.exists():
        # Restore from backup or fail gracefully
        raise RuntimeError(f"State file corrupted: {path}. Temp file exists: {tmp_path}")
```

### Hash Mismatch
```python
expected_hash = "e4f6c1d92a8b3f57"
actual_hash = compute_hash(artifact_path)
if actual_hash != expected_hash:
    raise IntegrityError(
        f"Artifact {artifact_path} hash mismatch! "
        f"Expected: {expected_hash}, Got: {actual_hash}"
    )
```

---

## Next Steps

1. **Read:** [Gate Framework](gate_framework.md) for G0-G3 definitions
2. **Read:** [Handoff Contracts](handoff_contracts.md) for agent-to-agent expectations
3. **Initialize:** Run `python scripts/h3a_init.py --task-brief "Your task"` to create a run
4. **Invoke:** Follow [Human Bridge Protocol](Human_Bridge_Protocol.md) to invoke agents

---

## Changelog

- **1.0.0** (2025-01-XX): Initial H3A state specification
  - Combines MCA state files + dual-agent runs/ structure
  - Adds TDD enforcement tracking
  - Production-grade atomic writes and hash verification