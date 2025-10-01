# H3A System (Hybrid 3-Agent)
**Version:** 1.0.0  
**Status:** Phases 1, 2, 3 & 4 Complete ✅ (Production-Ready)

---

## What is H3A?

**H3A** (Hybrid 3-Agent) is a **production-grade, evidence-based workflow system** for AI-assisted software development. It combines the best practices from three systems:

1. **MCA (Master Coordinator Assistant)** - State file architecture, gate-based progression, evidence protocol
2. **Dual-Agent System** - Proven runs/ directory structure, append-only history, atomic writes
3. **Agentic Prompt Guide** - TDD enforcement (RED→GREEN→REFACTOR), 7 best practices, iteration limits

---

## Architecture Overview

```
┌────────────────────────────────────────────────────────────────┐
│                         H3A WORKFLOW                           │
│                                                                │
│  (a) Human Invokes → (b) PLANNER → (c) Human Bridges →       │
│                           ↓                                    │
│  (d) EXECUTOR → (e) Human Bridges → (f) VALIDATOR →           │
│       ↓                                                        │
│  (g) VERDICT → (h) REPEAT UNTIL ROADMAP COMPLETE              │
│                                                                │
│  GATES: G0 (Planning) → G1 (Implementation) → G2 (Validation) │
│         → G3 (Production-Ready)                                │
└────────────────────────────────────────────────────────────────┘
```

### 3 Agents

| Agent | Role | Responsibilities | Gate |
|-------|------|------------------|------|
| **Planner** | Strategic | Roadmap creation, task decomposition, TDD planning | G0 |
| **Executor** | Tactical | TDD implementation (RED→GREEN→REFACTOR) | G1 |
| **Validator** | Quality | Comprehensive verification (10-point checklist) | G2 |

### 4 Gates

| Gate | Owner | Pass Criteria | Evidence Required |
|------|-------|---------------|-------------------|
| **G0: Planning** | Planner | Task decomposed, TDD plan ready | ROADMAP.md, CURRENT_TASK.json, planner_report.json |
| **G1: Implementation** | Executor | TDD complete, all tests green | RED→GREEN evidence, coverage delta, executor_report.json |
| **G2: Validation** | Validator | All quality checks passed | validator_report.json, security scan, mutation report |
| **G3: Production-Ready** | System | Ready for deployment | All artifacts verified, CI green |

---

## Quick Start

### 1. Initialize a Run

```bash
# Create new H3A run with optional task brief
python scripts/h3a_init.py --task-brief "Add user authentication"

# Output (JSON):
{
  "status": "success",
  "run_id": "20250929-134215-8b6f8b9a-...",
  "run_dir": "runs/20250929-134215-8b6f8b9a-.../",
  "state_files": { ... },
  "next_action": "Invoke Planner agent to populate ROADMAP.md"
}
```

### 2. Invoke Planner (G0)

```bash
# Human reads task brief, invokes Planner
# Planner fills:
#   - state/ROADMAP.md (strategy, task decomposition)
#   - state/CURRENT_TASK.json (first task with TDD plan)
#   - planner_report.json (research findings)
```

**Planner must pass G0:**
- ✅ ROADMAP.md has strategy and task list
- ✅ CURRENT_TASK.json has TDD plan (red/green/refactor)
- ✅ Definition of Done defined (≥3 measurable criteria)
- ✅ planner_report.json generated

### 3. Bridge to Executor (Human Step)

```bash
# Human reads state/SESSION_HANDOFF.json
cat runs/<run-id>/state/SESSION_HANDOFF.json

# Verify handoff valid:
#   - next_agent: "executor"
#   - gate_status: "G0_passed"
#   - payload contains task_id, tdd_plan, DoD

# Invoke Executor with task details
```

### 4. Executor Implements (G1)

```bash
# Executor follows TDD cycle:
#   RED: Write failing test → save to artifacts/executor/test_output_red.txt
#   GREEN: Implement code → save to artifacts/executor/test_output_green.txt
#   REFACTOR: Clean up, tests still pass

# Executor generates:
#   - executor_report.json (TDD evidence, coverage delta, DoD status)
#   - artifacts/executor/* (test outputs, coverage reports)
```

**Executor must pass G1:**
- ✅ RED phase evidence (test_output_red.txt)
- ✅ GREEN phase evidence (test_output_green.txt)
- ✅ Coverage increased OR ≥90% absolute
- ✅ All tests passing (exit code 0)
- ✅ Lint/type checks passing
- ✅ executor_report.json complete

### 5. Bridge to Validator (Human Step)

```bash
# Human reads state/SESSION_HANDOFF.json
cat runs/<run-id>/state/SESSION_HANDOFF.json

# Verify handoff valid:
#   - next_agent: "validator"
#   - gate_status: "G1_passed"
#   - TDD evidence artifacts present

# Invoke Validator with executor report
```

### 6. Validator Verifies (G2)

```bash
# Validator runs comprehensive 10-point checklist:
#   1. TDD Compliance (RED→GREEN verified)
#   2. Test Quality (all passing, meaningful assertions)
#   3. Coverage (≥90% OR delta ≥+0.1%)
#   4. Mutation Score (≥85%)
#   5. Security Scan (OWASP clean)
#   6. Code Quality (lint/type checks)
#   7. Accessibility (if UI changes)
#   8. DoD Completeness (all criteria addressed)
#   9. Intent Alignment (code matches goal)
#   10. Command Verification (re-run commands)

# Validator generates:
#   - validator_report.json (verdict: pass/fail/needs_remediation)
#   - artifacts/validator/security_scan.json
#   - artifacts/validator/mutation_report.txt
```

**Validator must complete G2:**
- ✅ All 10 checklist items verified
- ✅ Security scan performed
- ✅ Mutation testing run (or N/A justified)
- ✅ Verdict documented (pass/fail with reasoning)
- ✅ validator_report.json complete

### 7. Act on Verdict

```bash
# Human reads validator_report.json
jq '.verdicts[-1].status' runs/<run-id>/validator_report.json

# Outcomes:
#   - "pass" → Proceed to G3 (production-ready)
#   - "fail" → Executor remediates (iteration_count++)
#   - "escalation_required" → Human reviews (2 iterations exhausted)
```

### 8. Repeat Cycle

```bash
# If task complete and approved:
#   - Planner loads next task from ROADMAP.md
#   - Human bridges to Executor with new CURRENT_TASK.json
#   - Cycle repeats: Executor → Validator → Verdict

# Loop until ROADMAP.md all tasks complete (G3)
```

---

## Directory Structure

```
runs/<run-id>/
├── state/                          # MCA-style state files (SSOT)
│   ├── ROADMAP.md                 # Overall plan & task queue
│   ├── CURRENT_TASK.json          # Active task specification
│   ├── GATES_LEDGER.md            # G0→G3 progression log
│   ├── EVIDENCE_LOG.md            # Artifact catalog with hashes
│   └── SESSION_HANDOFF.json       # Agent-to-agent transitions
│
├── state.json                      # Append-only execution history
│
├── planner_report.json             # Planner outputs
├── executor_report.json            # Executor TDD cycles
├── validator_report.json           # Validator verdicts
│
├── artifacts/                      # Evidence storage
│   ├── planner/                   # Plans, diagrams
│   ├── executor/                  # Test outputs, coverage
│   └── validator/                 # Scans, mutation reports
│
└── README.md                       # Run documentation
```

---

## Documentation

### Phase 1: Infrastructure (✅ Complete)

| Document | Purpose | Audience |
|----------|---------|----------|
| **[README.md](README.md)** (this file) | H3A overview, quick start | All users |
| **[state_specification.md](state_specification.md)** | State file schemas, write protocols | Developers |
| **[gate_framework.md](gate_framework.md)** | G0-G3 definitions, entry/exit criteria | All agents |
| **[handoff_contracts.md](handoff_contracts.md)** | Agent-to-agent expectations | All agents |

### Phase 2: Agent Prompts (✅ Complete)

| Document | Purpose | Audience |
|----------|---------|----------|
| **[planner_prompt.md](../../prompts/planner_prompt.md)** | Planner agent instructions (~1,300 lines) | Planner |
| **[executor_prompt.md](../../prompts/executor_prompt.md)** | Executor agent instructions (~1,600 lines) | Executor |
| **[validator_prompt.md](../../prompts/validator_prompt.md)** | Validator agent instructions (~1,800 lines) | Validator |
| **[PHASE2_COMPLETION_REPORT.md](PHASE2_COMPLETION_REPORT.md)** | Phase 2 deliverables summary (~600 lines) | All users |

### Phase 3: Human Tools (✅ Complete)

| Document | Purpose | Audience |
|----------|---------|----------|
| **[Human_Bridge_Protocol.md](Human_Bridge_Protocol.md)** | How to pass handoffs (~1,100 lines) | Humans |
| **[Human_Verification_Checklist.md](Human_Verification_Checklist.md)** | Manual review steps (~900 lines) | Humans |
| **[Quick_Start_Guide.md](Quick_Start_Guide.md)** | End-to-end walkthrough (~1,300 lines) | New users |
| **[PHASE3_COMPLETION_REPORT.md](PHASE3_COMPLETION_REPORT.md)** | Phase 3 deliverables summary | All users |

### Phase 4: Migration & Integration (✅ Complete)

| Document | Purpose | Audience |
|----------|---------|----------|
| **[Migration_Guide.md](Migration_Guide.md)** | Dual-agent → H3A migration (~950 lines) | DevOps, Team Leads |
| **[PHASE4_COMPLETION_REPORT.md](PHASE4_COMPLETION_REPORT.md)** | Phase 4 deliverables summary | All users |

---

## Key Features

### ✅ Production-Grade State Management

- **Atomic writes:** Temp file + replace prevents corruption
- **Append-only history:** `state.json` never deletes, only appends
- **Hash verification:** All artifacts logged with SHA-256 hashes
- **Git metadata:** Captures branch, commit, CI status for reproducibility

### ✅ Evidence-Based Gates

- **No artifact = No progress:** Every gate requires proof
- **Re-run verification:** Validator doesn't trust Executor, re-runs commands
- **Audit trail:** GATES_LEDGER.md logs every gate event with timestamps

### ✅ TDD Enforcement

- **RED phase mandatory:** No "I'll add tests later"
- **GREEN phase follows RED:** Chronological order enforced
- **Coverage monitoring:** Delta tracked, decreases blocked
- **Mutation testing:** Weak tests caught at G2

### ✅ Iteration Limits & Escalation

- **Max 2 iterations:** Prevents infinite loops
- **Escalation protocol:** Human review after 2 failures
- **Remediation plans:** Validator provides specific fix guidance

### ✅ Comprehensive Validation (10-Point Checklist)

1. TDD Compliance
2. Test Quality
3. Coverage
4. Mutation Score
5. Security Scan
6. Code Quality (lint/type)
7. Accessibility (if UI)
8. DoD Completeness
9. Intent Alignment
10. Command Verification

---

## Best Practices

### For Planner

1. ✅ **Decompose small:** 1 task = 1-3 files, <200 LOC
2. ✅ **Define TDD plan:** Explicit RED/GREEN/REFACTOR steps
3. ✅ **Set measurable DoD:** "Coverage ≥95%" not "Good coverage"
4. ✅ **Document risks:** Note blockers upfront

### For Executor

1. ✅ **RED phase first:** Write failing test, save output
2. ✅ **Minimal GREEN:** Simplest implementation to pass
3. ✅ **Refactor safely:** Tests still passing after cleanup
4. ✅ **Save evidence:** test_output_red.txt, test_output_green.txt

### For Validator

1. ✅ **Verify, don't trust:** Re-run commands independently
2. ✅ **Check RED→GREEN:** Ensure test actually failed initially
3. ✅ **Run security scan:** Bandit, Safety, or OWASP ZAP
4. ✅ **Run mutation testing:** Mutmut, Cosmic Ray, or equivalent
5. ✅ **Check intent:** Does code match task goal?

### For Humans

1. ✅ **Read SESSION_HANDOFF.json:** Know what to pass to next agent
2. ✅ **Verify handoffs:** Check verification_checklist before invoking
3. ✅ **Don't force:** If agent rejects handoff, address root cause
4. ✅ **Review escalations promptly:** Blocked agents waste time

---

## Metrics & KPIs

### Success Metrics

| Metric | Target | Formula |
|--------|--------|---------|
| **G0 Pass Rate (1st try)** | ≥95% | Passed G0 first time / Total G0 attempts |
| **G1 Pass Rate (1st try)** | ≥80% | Passed G1 first time / Total G1 attempts |
| **G2 Pass Rate (1st try)** | ≥70% | Passed G2 first time / Total G2 attempts |
| **Escalation Rate** | ≤5% | Escalations / Total tasks |

### Quality Metrics

| Metric | Target | Gate |
|--------|--------|------|
| **Coverage** | ≥90% | G1, G2 |
| **Mutation Score** | ≥85% | G2 |
| **Security Scan** | 0 high/critical CVEs | G2 |
| **Lint Passing** | 100% | G1, G2 |

---

## Troubleshooting

### "CURRENT_TASK.json not found"

**Cause:** Run not initialized or Planner didn't complete G0

**Solution:**
```bash
# Check if run exists
ls runs/<run-id>/

# If missing, initialize:
python scripts/h3a_init.py --task-brief "Your task"

# If exists but CURRENT_TASK empty, Planner must fill it
```

### "RED phase evidence missing"

**Cause:** Executor skipped RED phase or forgot to save output

**Solution:**
```bash
# Validator rejects handoff
# Executor must:
#   1. Write failing test
#   2. Run test: pytest tests/test_file.py -v > artifacts/executor/test_output_red.txt
#   3. Save output as artifact
#   4. Add to EVIDENCE_LOG.md with hash
```

### "Handoff rejected by receiver"

**Cause:** Sending agent didn't fulfill handoff contract

**Solution:**
```bash
# Check SESSION_HANDOFF.json for rejection reason
jq '.payload.rejection_reason' runs/<run-id>/state/SESSION_HANDOFF.json

# Sender remediates issue
# Human re-invokes receiver after fix
```

### "Gate stuck in 'in_progress'"

**Cause:** Agent crashed or waiting for input

**Solution:**
```bash
# Check agent logs for errors
# If crashed, manually update GATES_LEDGER.md to FAILED
# Restart agent or escalate to human
```

---

## Compliance & Audit

### Artifact Integrity

- All artifacts logged in `EVIDENCE_LOG.md` with SHA-256 hashes
- Hash verification detects tampering or corruption
- Immutable audit trail (append-only logs)

### Regulatory Mapping

| Framework | H3A Support | Evidence |
|-----------|-------------|----------|
| **OWASP ASVS** | Security testing (V10) | `security_scan.json` |
| **ISO 42001** | AI traceability | `GATES_LEDGER.md`, `EVIDENCE_LOG.md` |
| **SOC 2** | Audit logs | `state.json`, gate logs |
| **NIST CSF** | Vulnerability mgmt | `security_scan.json` |
| **EU AI Act** | Risk mgmt, transparency | Gate evidence, escalation logs |

---

## Performance Considerations

### File Sizes (Typical)

- `ROADMAP.md`: ~5-20 KB
- `CURRENT_TASK.json`: ~2-5 KB
- `GATES_LEDGER.md`: ~10-50 KB
- `EVIDENCE_LOG.md`: ~5-30 KB
- `state.json`: ~50-500 KB (grows with steps)

**Scalability:** For runs with >100 tasks, consider pagination or archiving.

### Concurrent Access

- **Reads:** Always safe (immutable snapshots)
- **Writes:** Atomic (temp + replace)
- **Conflicts:** Agents run sequentially, no concurrency issues

---

## Backward Compatibility

### With Dual-Agent System

| Dual-Agent | H3A Equivalent | Compatibility |
|------------|----------------|---------------|
| `state.json` | `state.json` | ✅ Identical schema (H3A adds `gates` field) |
| `executor_report.json` | `executor_report.json` | ✅ Enhanced (superset of dual-agent) |
| `validator_report.json` | `validator_report.json` | ✅ Enhanced (comprehensive checklist) |
| `artifacts/executor/` | `artifacts/executor/` | ✅ Same structure |
| `artifacts/validator/` | `artifacts/validator/` | ✅ Same structure |

**Migration:** Existing dual-agent runs continue to work. New runs use `h3a_init.py`.

---

## Scripts

### `scripts/h3a_init.py`

**Purpose:** Initialize H3A run with production-grade state management

**Usage:**
```bash
python scripts/h3a_init.py [--task-brief "Description"] [--verbose]
```

**Output:** JSON with run_id, paths, initialization status

**What it creates:**
- `runs/<run-id>/` directory structure
- State files (ROADMAP, CURRENT_TASK, GATES_LEDGER, EVIDENCE_LOG, SESSION_HANDOFF)
- Agent report files (planner, executor, validator)
- Artifact directories (planner/, executor/, validator/)

---

## Contributing

### Adding New Gates

1. Update `gate_framework.md` with gate definition
2. Add entry/exit criteria and evidence requirements
3. Update `state.json` schema with new gate field
4. Update agent prompts to handle new gate

### Adding New State Files

1. Define schema in `state_specification.md`
2. Add creation logic to `h3a_init.py`
3. Update agent prompts to read/write new file
4. Document in handoff contracts if cross-agent

### Modifying Handoff Contracts

1. Update `handoff_contracts.md` with new obligations
2. Update `SESSION_HANDOFF.json` schema
3. Update sending agent to provide new data
4. Update receiving agent to verify new data

---

## Changelog

### Version 1.0.0 (2025-01-XX)

**Phase 1: Infrastructure (✅ Complete)**
- ✅ `scripts/h3a_init.py` - Run initialization with production-grade state management
- ✅ `docs/H3A_System/state_specification.md` - Comprehensive state file schemas
- ✅ `docs/H3A_System/gate_framework.md` - 4-gate system (G0-G3) with evidence protocol
- ✅ `docs/H3A_System/handoff_contracts.md` - Agent-to-agent expectations (H1-H3)
- ✅ `docs/H3A_System/README.md` - This file

**Phase 2: Agent Prompts (🚧 Next)**
- 🚧 Planner prompt (with state file integration)
- 🚧 Executor prompt (TDD + state management)
- 🚧 Validator prompt (comprehensive 10-point checklist)

**Phase 3: Human Tools (🚧 Future)**
- 🚧 Human Bridge Protocol
- 🚧 Human Verification Checklist
- 🚧 Quick Start Guide (detailed walkthrough)

**Phase 4: Migration (🚧 Future)**
- 🚧 Migration guide (dual-agent → H3A)

---

## Support & Contact

**Documentation Issues:** Open issue in repo  
**Feature Requests:** Create enhancement proposal  
**Questions:** See [Quick Start Guide](Quick_Start_Guide.md) (coming in Phase 3)

---

## License

[Same as parent repository]

---

## Acknowledgments

**H3A builds on:**
- **MCA System** - Gate-based progression, state files, evidence protocol
- **Dual-Agent System** - Proven runs/ structure, atomic writes, append-only history
- **Agentic Prompt Guide** - TDD enforcement, 7 best practices, iteration limits
- **SWE-bench Research** (Oct 2025) - Industry best practices for AI coding agents
- **OWASP, NIST, ISO Standards** - Security and compliance frameworks

---

**🚀 H3A System - Production-Grade AI-Assisted Development** 🚀