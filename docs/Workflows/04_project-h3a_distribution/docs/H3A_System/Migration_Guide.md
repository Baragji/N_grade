# Migration Guide: Dual-Agent → H3A System

**Document Version:** 1.0.0  
**Target Audience:** Teams currently using dual-agent workflow  
**Migration Time:** ~2-3 hours for first migration, ~30 minutes for subsequent projects  
**Last Updated:** 2025-01-XX

---

## Table of Contents

1. [Overview](#overview)
2. [What Changes?](#what-changes)
3. [Migration Strategy](#migration-strategy)
4. [Pre-Migration Checklist](#pre-migration-checklist)
5. [Step-by-Step Migration](#step-by-step-migration)
6. [Verification](#verification)
7. [Rollback Plan](#rollback-plan)
8. [Common Issues](#common-issues)
9. [Side-by-Side Comparison](#side-by-side-comparison)
10. [FAQ](#faq)

---

## Overview

### What is Migration?

Migrating from **dual-agent** (Executor + Validator) to **H3A** (Planner + Executor + Validator) means:

1. **Adding a Planner agent** for strategic task decomposition
2. **Implementing state management** (`state/` directory with canonical files)
3. **Adopting gate framework** (G0, G1, G2, G3 progression)
4. **Enforcing TDD** (RED→GREEN→REFACTOR mandatory)
5. **Using handoff contracts** (H1, H2, H3 bridge protocols)

### Why Migrate?

| Benefit | Dual-Agent | H3A |
|---------|------------|-----|
| **Strategic Planning** | ❌ Manual task decomposition | ✅ Planner agent automates |
| **TDD Enforcement** | ⚠️ Recommended | ✅ Mandatory (RED→GREEN verified) |
| **State Management** | ⚠️ report.json only | ✅ 5 canonical state files + audit trail |
| **Evidence Tracking** | ⚠️ Basic | ✅ Comprehensive (EVIDENCE_LOG.md with hashes) |
| **Gate-Based QA** | ❌ No | ✅ G0→G1→G2→G3 progression |
| **Human Guidance** | ⚠️ Ad-hoc | ✅ Bridge protocols with checklists |
| **Audit Trail** | ⚠️ Basic | ✅ GATES_LEDGER.md + git metadata |

### What Stays the Same?

✅ **`runs/<run-id>/` directory structure** - H3A is backward compatible  
✅ **Executor and Validator agents** - Enhanced, not replaced  
✅ **Report files** (executor_report.json, validator_report.json) - Still used  
✅ **Artifacts directory** - Expanded with planner/ subdirectory  
✅ **TDD philosophy** - Now enforced, not just recommended

---

## What Changes?

### Directory Structure

**Before (Dual-Agent):**
```
runs/<run-id>/
├── state.json                # Execution history
├── executor_report.json      # Executor output
├── validator_report.json     # Validator output
├── artifacts/
│   ├── executor/            # Test outputs, coverage
│   └── validator/           # Security scans, mutation reports
└── README.md                # Run documentation
```

**After (H3A):**
```
runs/<run-id>/
├── state/                    # ← NEW: State files (SSOT)
│   ├── ROADMAP.md           # ← NEW: Overall plan
│   ├── CURRENT_TASK.json    # ← NEW: Active task
│   ├── GATES_LEDGER.md      # ← NEW: G0→G3 log
│   ├── EVIDENCE_LOG.md      # ← NEW: Artifact catalog
│   └── SESSION_HANDOFF.json # ← NEW: Agent transitions
│
├── state.json                # Execution history (unchanged)
├── planner_report.json       # ← NEW: Planner output
├── executor_report.json      # Executor output (enhanced)
├── validator_report.json     # Validator output (enhanced)
│
├── artifacts/
│   ├── planner/             # ← NEW: Plans, diagrams
│   ├── executor/            # Test outputs (enhanced)
│   └── validator/           # Scans, reports (unchanged)
│
└── README.md                # Run documentation (unchanged)
```

### Workflow Changes

**Before (Dual-Agent):**
```
Human → Executor → Human → Validator → Human → Decision
```

**After (H3A):**
```
Human → Planner (G0) → H1 Bridge → Executor (G1) → H2 Bridge → Validator (G2) → H3 Bridge → Decision (G3)
```

**Key Differences:**
- **Added Planner agent** before Executor
- **Added human bridge steps** (H1, H2, H3) with verification checklists
- **Added gates** (G0, G1, G2, G3) with pass criteria
- **TDD enforcement** at G1 (RED→GREEN evidence mandatory)

### Agent Prompt Changes

| Agent | Dual-Agent Version | H3A Version | Key Additions |
|-------|-------------------|-------------|---------------|
| **Executor** | `prompts/executor_prompt.md` (legacy) | `prompts/executor_prompt.md` (updated) | • State file awareness<br>• TDD evidence requirements<br>• G1 gate criteria<br>• Handoff protocol (H2) |
| **Validator** | `prompts/validator_prompt.md` (legacy) | `prompts/validator_prompt.md` (updated) | • 10-point checklist<br>• RED→GREEN verification<br>• G2 gate criteria<br>• Handoff protocol (H3) |
| **Planner** | ❌ N/A | `prompts/planner_prompt.md` (new) | • Strategic planning<br>• Task decomposition<br>• TDD plan creation<br>• G0 gate criteria<br>• Handoff protocol (H1) |

---

## Migration Strategy

### Option A: Big Bang Migration (Recommended for New Projects)

**Timeline:** 1 session (~2-3 hours)

**Steps:**
1. Adopt H3A fully for next task
2. Use `h3a_init.py` for initialization
3. Follow H3A workflow (Planner → Executor → Validator)

**Pros:**
- ✅ Clean slate
- ✅ No hybrid state
- ✅ Full benefits immediately

**Cons:**
- ⚠️ Team must learn new workflow
- ⚠️ Old runs/ not migrated

**Best for:**
- New projects
- Small teams
- Projects with no in-flight work

---

### Option B: Incremental Migration (Recommended for In-Flight Projects)

**Timeline:** 2-4 weeks (parallel running)

**Steps:**
1. **Week 1:** Run H3A for new features, dual-agent for existing work
2. **Week 2:** Migrate documentation to H3A state files
3. **Week 3:** Migrate in-flight tasks to H3A (optional)
4. **Week 4:** Decommission dual-agent scripts

**Pros:**
- ✅ Low risk
- ✅ Team learns gradually
- ✅ No disruption to in-flight work

**Cons:**
- ⚠️ Hybrid state for weeks
- ⚠️ Two workflows in parallel

**Best for:**
- Large teams
- Projects with many in-flight tasks
- Risk-averse organizations

---

### Option C: Backward-Compatible Hybrid (Recommended for Large Organizations)

**Timeline:** Indefinite (run both systems)

**Steps:**
1. New projects use H3A
2. Legacy projects stay on dual-agent
3. Migrate on a project-by-project basis

**Pros:**
- ✅ Zero disruption
- ✅ Each team chooses timeline
- ✅ H3A proves itself before mandate

**Cons:**
- ⚠️ Indefinite maintenance burden
- ⚠️ Two systems to support

**Best for:**
- Enterprises with 100+ projects
- Organizations with strict change control
- Teams with different maturity levels

---

## Pre-Migration Checklist

### Before You Start

- [ ] **Read H3A documentation:**
  - [ ] `docs/H3A_System/README.md` (overview)
  - [ ] `docs/H3A_System/Quick_Start_Guide.md` (walkthrough)
  - [ ] `docs/H3A_System/Human_Bridge_Protocol.md` (bridge procedures)
  - [ ] `docs/H3A_System/Human_Verification_Checklist.md` (G3 gate)

- [ ] **Test H3A on non-production task:**
  - [ ] Run `python scripts/h3a_init.py --task-brief "Add hello world function"`
  - [ ] Complete full cycle (Planner → Executor → Validator → G3)
  - [ ] Verify all state files created correctly
  - [ ] Verify artifacts logged in EVIDENCE_LOG.md

- [ ] **Backup existing dual-agent runs:**
  - [ ] `tar -czf backup-runs-$(date +%Y%m%d).tar.gz runs/`
  - [ ] Store backup off-server

- [ ] **Check dependencies:**
  - [ ] Python ≥3.9 installed
  - [ ] Git repository initialized
  - [ ] `scripts/h3a_init.py` exists
  - [ ] Agent prompts exist (`prompts/planner_prompt.md`, `executor_prompt.md`, `validator_prompt.md`)

- [ ] **Team readiness:**
  - [ ] All team members read Quick Start Guide
  - [ ] Conduct 1-hour H3A demo session
  - [ ] Designate H3A champion for questions

### Migration Readiness Checklist

- [ ] No in-flight tasks OR willing to pause them
- [ ] Team available for 2-3 hour migration window
- [ ] Rollback plan documented (see [Rollback Plan](#rollback-plan))
- [ ] First H3A task selected (small, low-risk feature)

---

## Step-by-Step Migration

### Step 1: Update Repository Structure (5 minutes)

**Goal:** Ensure H3A infrastructure is in place.

```bash
# 1. Check if h3a_init.py exists
ls scripts/h3a_init.py
# Expected output: scripts/h3a_init.py

# 2. Check if prompts exist
ls prompts/planner_prompt.md prompts/executor_prompt.md prompts/validator_prompt.md
# Expected output: All 3 files exist

# 3. Check if H3A docs exist
ls docs/H3A_System/
# Expected output:
#   README.md
#   state_specification.md
#   gate_framework.md
#   handoff_contracts.md
#   Human_Bridge_Protocol.md
#   Human_Verification_Checklist.md
#   Quick_Start_Guide.md
```

**If any files missing:**
```bash
# Clone H3A system from reference repo OR regenerate
# Contact team lead for H3A baseline
```

---

### Step 2: Initialize First H3A Run (2 minutes)

**Goal:** Create your first H3A run directory.

```bash
# Initialize with task brief
python scripts/h3a_init.py --task-brief "Add email validation to User model"

# Example output:
# {
#   "status": "success",
#   "run_id": "20250129-143022-8b6f8b9a-...",
#   "run_dir": "runs/20250129-143022-8b6f8b9a-.../",
#   "state_files": {
#     "roadmap": "state/ROADMAP.md",
#     "current_task": "state/CURRENT_TASK.json",
#     ...
#   },
#   "next_action": "Invoke Planner agent"
# }
```

**Verification:**
```bash
# Check state/ directory created
ls runs/<run-id>/state/
# Expected: ROADMAP.md, CURRENT_TASK.json, GATES_LEDGER.md, EVIDENCE_LOG.md, SESSION_HANDOFF.json

# Check artifacts/ subdirectories
ls runs/<run-id>/artifacts/
# Expected: planner/, executor/, validator/

# Check report placeholders
ls runs/<run-id>/*.json
# Expected: state.json, planner_report.json, executor_report.json, validator_report.json (all initialized)
```

---

### Step 3: Invoke Planner (G0 Gate) (10-15 minutes)

**Goal:** Planner decomposes task and creates TDD plan.

**Human Action:**
```bash
# 1. Read task brief
cat runs/<run-id>/state/ROADMAP.md
# Currently empty or has placeholder

# 2. Invoke Planner agent (use your preferred AI interface)
# Provide Planner with:
#   - Task brief: "Add email validation to User model"
#   - Run directory: runs/<run-id>/
#   - Instructions: "Follow planner_prompt.md, populate ROADMAP.md and CURRENT_TASK.json"
```

**Planner Outputs:**
- `state/ROADMAP.md` - Overall strategy, task list
- `state/CURRENT_TASK.json` - First task with TDD plan
- `planner_report.json` - Research findings, risks
- `artifacts/planner/` - Any diagrams, notes

**Verification (H1 Bridge Checklist):**
```bash
# See docs/H3A_System/Human_Bridge_Protocol.md, H1 section

# Quick checks:
jq '.gate_status' runs/<run-id>/state/SESSION_HANDOFF.json
# Expected: "G0_passed"

jq '.tdd_plan' runs/<run-id>/state/CURRENT_TASK.json
# Expected: { "red": "...", "green": "...", "refactor": "..." }

jq '.status' runs/<run-id>/planner_report.json
# Expected: "complete"
```

**If G0 fails:** Planner must remediate before proceeding.

---

### Step 4: Bridge to Executor (H1) (2-5 minutes)

**Goal:** Human verifies Planner output and transitions to Executor.

**Follow:** `docs/H3A_System/Human_Bridge_Protocol.md` → **Section: H1 Bridge (Planner → Executor)**

**Quick Summary:**
1. ✅ Read SESSION_HANDOFF.json
2. ✅ Verify gate_status = "G0_passed"
3. ✅ Verify CURRENT_TASK.json has TDD plan
4. ✅ Verify task is small (<200 LOC, 1-3 files)
5. ✅ Load CURRENT_TASK.json into Executor agent

```bash
# Load task for Executor
cat runs/<run-id>/state/CURRENT_TASK.json

# Invoke Executor with task details
# (Use your AI interface)
```

---

### Step 5: Executor Implements (G1 Gate) (20-30 minutes)

**Goal:** Executor follows TDD cycle and generates evidence.

**Executor Action:**
1. **RED phase:** Write failing test → save to `artifacts/executor/test_output_red.txt`
2. **GREEN phase:** Implement code → save to `artifacts/executor/test_output_green.txt`
3. **REFACTOR phase:** Clean up → tests still pass
4. Generate `executor_report.json` with TDD evidence

**Verification (H2 Bridge Checklist):**
```bash
# See docs/H3A_System/Human_Bridge_Protocol.md, H2 section

# Quick checks:
jq '.gate_status' runs/<run-id>/state/SESSION_HANDOFF.json
# Expected: "G1_passed"

ls runs/<run-id>/artifacts/executor/test_output_red.txt
ls runs/<run-id>/artifacts/executor/test_output_green.txt
# Both must exist

jq '.tdd_evidence' runs/<run-id>/executor_report.json
# Expected: { "red_phase": "...", "green_phase": "..." }
```

**If G1 fails:** Executor must remediate before Validator invoked.

---

### Step 6: Bridge to Validator (H2) (3-7 minutes)

**Goal:** Human verifies Executor output and transitions to Validator.

**Follow:** `docs/H3A_System/Human_Bridge_Protocol.md` → **Section: H2 Bridge (Executor → Validator)**

**Quick Summary:**
1. ✅ Read SESSION_HANDOFF.json
2. ✅ Verify gate_status = "G1_passed"
3. ✅ Verify TDD evidence artifacts exist (7+ files)
4. ✅ Verify tests pass when you run them
5. ✅ Load executor_report.json into Validator agent

```bash
# Verify tests pass yourself
pytest tests/ -v
# Expected: All tests pass

# Load executor report for Validator
cat runs/<run-id>/executor_report.json

# Invoke Validator with executor report
# (Use your AI interface)
```

---

### Step 7: Validator Verifies (G2 Gate) (15-20 minutes)

**Goal:** Validator runs 10-point checklist and provides verdict.

**Validator Action:**
1. Run 10-point verification checklist (see `validator_prompt.md`)
2. Re-run all commands independently (don't trust Executor)
3. Verify RED→GREEN chronology
4. Run security scan (Bandit, Safety)
5. Run mutation testing (Mutmut) if applicable
6. Generate `validator_report.json` with verdict

**Verification (H3 Bridge Checklist):**
```bash
# See docs/H3A_System/Human_Bridge_Protocol.md, H3 section

# Quick checks:
jq '.verdicts[-1].status' runs/<run-id>/validator_report.json
# Expected: "pass" OR "fail" OR "needs_remediation"

jq '.gate_status' runs/<run-id>/state/SESSION_HANDOFF.json
# Expected: "G2_complete"

# If status = "pass", proceed to G3
# If status = "fail", Executor remediates
```

---

### Step 8: Human G3 Decision (H3 Bridge) (10-15 minutes)

**Goal:** Human makes final production-ready decision.

**Follow:** `docs/H3A_System/Human_Verification_Checklist.md` → **8-Point Checklist**

**Quick Summary:**
1. ✅ Requirements Met - Does it solve the problem?
2. ✅ Tests Pass - Do tests pass when I run them?
3. ✅ No Broken Features - Did this break anything?
4. ✅ Code Readable - Can I understand it?
5. ✅ Security Check - Any obvious risks? (CRITICAL)
6. ✅ Documentation Updated - Are functions documented?
7. ✅ Evidence Complete - Can I audit this later?
8. ✅ Intent Alignment - Is this what we needed?

**Decision Matrix:**
- **8/8 passed** → ✅ **APPROVE** (production-ready)
- **6-7/8 passed** → ⚠️ **CONDITIONAL APPROVAL** (minor fixes)
- **<6/8 OR security issue** → ❌ **REJECT** (major rework)

**Document Decision:**
```bash
# Create G3 approval report
cat > runs/<run-id>/g3_approval_report.json <<'EOF'
{
  "decision": "approve",
  "approver": "Jane Doe",
  "timestamp": "2025-01-29T14:35:22Z",
  "checklist_results": {
    "requirements_met": "pass",
    "tests_pass": "pass",
    "no_broken_features": "pass",
    "code_readable": "pass",
    "security_check": "pass",
    "documentation_updated": "pass",
    "evidence_complete": "pass",
    "intent_alignment": "pass"
  },
  "notes": "Email validation implemented correctly with comprehensive tests."
}
EOF

# Update GATES_LEDGER
echo "$(date -Iseconds) | G3_passed | human_decision | G3 approval granted by Jane Doe" >> runs/<run-id>/state/GATES_LEDGER.md
```

---

### Step 9: Deploy and Close Task (5 minutes)

**Goal:** Deploy code and mark task complete.

```bash
# 1. Merge code (if using feature branch)
git checkout main
git merge feature/email-validation
git push origin main

# 2. Update ROADMAP.md to mark task complete
# (Manually edit or let Planner update)

# 3. If more tasks remain, repeat cycle
#    Planner loads next task from ROADMAP.md
#    Human bridges to Executor (H1)
#    Loop: Executor → Validator → G3 decision

# 4. If all tasks complete, run complete!
jq '.status = "complete"' runs/<run-id>/state.json > tmp.json && mv tmp.json runs/<run-id>/state.json
```

---

## Verification

### Migration Success Criteria

After completing Steps 1-9, verify your migration was successful:

#### ✅ Directory Structure Check

```bash
# Run directory has all H3A components
ls runs/<run-id>/state/
# Expected: ROADMAP.md, CURRENT_TASK.json, GATES_LEDGER.md, EVIDENCE_LOG.md, SESSION_HANDOFF.json

ls runs/<run-id>/artifacts/
# Expected: planner/, executor/, validator/

ls runs/<run-id>/*.json
# Expected: state.json, planner_report.json, executor_report.json, validator_report.json, g3_approval_report.json
```

#### ✅ Gate Progression Check

```bash
# All gates passed
cat runs/<run-id>/state/GATES_LEDGER.md
# Expected output example:
# 2025-01-29T14:10:00Z | G0_passed | planner | Task decomposed, TDD plan created
# 2025-01-29T14:25:00Z | G1_passed | executor | TDD complete, all tests green
# 2025-01-29T14:40:00Z | G2_passed | validator | All 10 checklist items verified
# 2025-01-29T14:50:00Z | G3_passed | human_decision | G3 approval granted by Jane Doe
```

#### ✅ Evidence Completeness Check

```bash
# All artifacts logged with hashes
cat runs/<run-id>/state/EVIDENCE_LOG.md
# Expected: 7+ artifacts with SHA-256 hashes

# Verify hashes match
sha256sum runs/<run-id>/artifacts/executor/test_output_red.txt
# Compare with hash in EVIDENCE_LOG.md
```

#### ✅ TDD Evidence Check

```bash
# RED phase evidence exists
grep -q "FAILED" runs/<run-id>/artifacts/executor/test_output_red.txt
echo $?
# Expected: 0 (RED evidence found)

# GREEN phase evidence exists
grep -q "PASSED" runs/<run-id>/artifacts/executor/test_output_green.txt
echo $?
# Expected: 0 (GREEN evidence found)
```

#### ✅ Quality Metrics Check

```bash
# Coverage target met
jq '.coverage.final' runs/<run-id>/executor_report.json
# Expected: ≥90% OR delta ≥+0.1%

# All tests passing
jq '.tests.status' runs/<run-id>/executor_report.json
# Expected: "passing"

# Validator approved
jq '.verdicts[-1].status' runs/<run-id>/validator_report.json
# Expected: "pass"
```

### Post-Migration Checklist

- [ ] First H3A task completed successfully
- [ ] All 4 gates passed (G0, G1, G2, G3)
- [ ] Team understands H3A workflow
- [ ] Human bridge protocols followed
- [ ] All evidence artifacts logged
- [ ] G3 approval documented
- [ ] Code deployed to production

---

## Rollback Plan

### When to Rollback

Consider rollback if:
- ⚠️ H3A migration taking >6 hours
- ⚠️ Team unable to follow bridge protocols
- ⚠️ Critical bugs introduced by workflow change
- ⚠️ Business deadline at risk

### Rollback Procedure (15 minutes)

**Step 1: Restore dual-agent workflow**
```bash
# 1. Complete in-flight H3A task OR abandon it
# (Don't leave in half-completed state)

# 2. Restore backup if needed
tar -xzf backup-runs-$(date +%Y%m%d).tar.gz

# 3. Use legacy dual-agent workflow for next task
# (Executor → Validator, no Planner)
```

**Step 2: Document rollback reason**
```bash
# Create rollback report
cat > runs/h3a_rollback_report.txt <<'EOF'
Date: 2025-01-29
Reason: [Describe why rollback needed]
Issues encountered: [List specific problems]
Lessons learned: [What to improve before retry]
Next steps: [When will you retry H3A?]
EOF
```

**Step 3: Schedule H3A retry**
- Address root cause of rollback
- Conduct additional training if needed
- Retry H3A on smaller task
- Get team buy-in before next attempt

---

## Common Issues

### Issue 1: "Planner not following TDD plan structure"

**Symptoms:**
- CURRENT_TASK.json missing `tdd_plan` field
- tdd_plan doesn't have `red`, `green`, `refactor` keys

**Root Cause:**
- Planner agent not loaded with correct prompt
- Prompt truncated or incomplete

**Solution:**
```bash
# 1. Verify planner_prompt.md loaded correctly
cat prompts/planner_prompt.md | head -n 50
# Should start with "# Planner Agent - H3A System"

# 2. Re-invoke Planner with explicit TDD instructions
# Tell Planner: "Create tdd_plan with red, green, refactor phases"

# 3. Manually edit CURRENT_TASK.json if needed
jq '.tdd_plan = {"red": "Write failing test", "green": "Implement code", "refactor": "Clean up"}' \
  runs/<run-id>/state/CURRENT_TASK.json > tmp.json && mv tmp.json runs/<run-id>/state/CURRENT_TASK.json
```

---

### Issue 2: "Executor skipping RED phase"

**Symptoms:**
- `test_output_red.txt` doesn't exist
- Validator rejects handoff

**Root Cause:**
- Executor agent not enforcing TDD
- Executor wrote test and implementation together

**Solution:**
```bash
# 1. Reject Executor handoff
# Tell Executor: "G1 not passed - RED phase evidence missing"

# 2. Executor must generate RED evidence
pytest tests/test_file.py -v > runs/<run-id>/artifacts/executor/test_output_red.txt 2>&1
# (Run BEFORE implementing code)

# 3. Verify RED output shows failure
grep "FAILED" runs/<run-id>/artifacts/executor/test_output_red.txt
# Expected: At least one FAILED test

# 4. Add to EVIDENCE_LOG.md
HASH=$(sha256sum runs/<run-id>/artifacts/executor/test_output_red.txt | awk '{print $1}')
echo "- test_output_red.txt | $HASH | executor | RED phase evidence" >> runs/<run-id>/state/EVIDENCE_LOG.md
```

---

### Issue 3: "Validator can't re-run commands (environment mismatch)"

**Symptoms:**
- Validator says "Command not found" or "Module not found"
- Environment on Validator machine different from Executor

**Root Cause:**
- Validator in different Python venv
- Dependencies not installed

**Solution:**
```bash
# 1. Document environment in executor_report.json
jq '.environment = {"python": "3.11.2", "pytest": "7.4.3", "venv": "/path/to/venv"}' \
  runs/<run-id>/executor_report.json > tmp.json && mv tmp.json runs/<run-id>/executor_report.json

# 2. Validator activates same environment
source /path/to/venv/bin/activate

# 3. Validator installs dependencies
pip install -r requirements.txt

# 4. Re-run verification commands
pytest tests/ -v --cov=src/
bandit -r src/ -f json -o runs/<run-id>/artifacts/validator/security_scan.json
```

---

### Issue 4: "Human bridge taking too long"

**Symptoms:**
- H1, H2, or H3 bridge taking >15 minutes
- Bottleneck in workflow

**Root Cause:**
- Human unfamiliar with checklists
- Too many manual verification steps

**Solution:**
```bash
# 1. Create automation scripts for common checks
cat > scripts/h3_quick_check.sh <<'EOF'
#!/bin/bash
RUN_ID=$1

echo "🔍 Quick H3 Verification for $RUN_ID"
echo ""

echo "✅ G2 Status:"
jq '.verdicts[-1].status' runs/$RUN_ID/validator_report.json

echo ""
echo "✅ Tests:"
pytest tests/ -q

echo ""
echo "✅ Coverage:"
jq '.coverage.final' runs/$RUN_ID/executor_report.json

echo ""
echo "✅ Security:"
jq '.status' runs/$RUN_ID/artifacts/validator/security_scan.json
EOF

chmod +x scripts/h3_quick_check.sh

# 2. Run quick check script
./scripts/h3_quick_check.sh <run-id>
# Total time: ~2 minutes instead of 10-15
```

---

### Issue 5: "GATES_LEDGER.md out of sync with actual progress"

**Symptoms:**
- GATES_LEDGER shows G1_passed but Executor says G1 failed
- Ledger missing entries

**Root Cause:**
- Agent forgot to update ledger
- Manual edit error

**Solution:**
```bash
# 1. Reconstruct ledger from report files
cat > runs/<run-id>/state/GATES_LEDGER.md <<'EOF'
# Gates Progression Ledger

| Timestamp | Gate | Agent | Status | Notes |
|-----------|------|-------|--------|-------|
EOF

# 2. Add entries from reports
jq -r '.timestamp + " | G0 | planner | passed | " + .status' runs/<run-id>/planner_report.json >> runs/<run-id>/state/GATES_LEDGER.md
jq -r '.timestamp + " | G1 | executor | passed | " + .status' runs/<run-id>/executor_report.json >> runs/<run-id>/state/GATES_LEDGER.md
jq -r '.verdicts[-1].timestamp + " | G2 | validator | " + .verdicts[-1].status + " | "' runs/<run-id>/validator_report.json >> runs/<run-id>/state/GATES_LEDGER.md

# 3. Verify ledger accurate
cat runs/<run-id>/state/GATES_LEDGER.md
```

---

## Side-by-Side Comparison

### Workflow Comparison

**Scenario:** "Add email validation to User model"

#### Dual-Agent Workflow

```
Total Time: ~45 minutes
Human Overhead: ~10 minutes

┌─────────────────────────────────────────────┐
│ 1. Human decomposes task (5 min)          │
│    - Decide what to implement              │
│    - Write task description manually       │
└─────────────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│ 2. Invoke Executor (20 min)               │
│    - Executor writes tests (hopefully)     │
│    - Executor implements code              │
│    - executor_report.json generated        │
└─────────────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│ 3. Human reviews executor report (3 min)  │
│    - Read report                           │
│    - Decide if ready for validation        │
└─────────────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│ 4. Invoke Validator (15 min)              │
│    - Validator runs checks                 │
│    - validator_report.json generated       │
└─────────────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│ 5. Human makes decision (2 min)           │
│    - Read validator report                 │
│    - Approve or reject                     │
└─────────────────────────────────────────────┘
                   ↓
                DONE
```

**Issues:**
- ❌ No strategic planning (human does mental work)
- ❌ TDD not enforced (Executor "hopefully" writes tests)
- ❌ No evidence tracking (artifacts not logged)
- ❌ No gate verification (no checkpoints)
- ❌ Human decision ad-hoc (no structured checklist)

---

#### H3A Workflow

```
Total Time: ~60 minutes
Human Overhead: ~20 minutes

┌─────────────────────────────────────────────┐
│ 1. Initialize run (2 min)                 │
│    $ python scripts/h3a_init.py            │
└─────────────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│ 2. Invoke Planner (G0) (10 min)           │
│    - Planner decomposes task               │
│    - Creates TDD plan                      │
│    - Writes ROADMAP.md                     │
│    - Writes CURRENT_TASK.json              │
└─────────────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│ 3. H1 Bridge (human verification) (3 min) │
│    - Verify G0 passed                      │
│    - Check TDD plan complete               │
│    - Load task into Executor               │
└─────────────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│ 4. Invoke Executor (G1) (20 min)          │
│    - RED: Write failing test (ENFORCED)    │
│    - GREEN: Implement code                 │
│    - REFACTOR: Clean up                    │
│    - Evidence logged automatically         │
└─────────────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│ 5. H2 Bridge (human verification) (5 min) │
│    - Verify G1 passed                      │
│    - Verify RED→GREEN evidence             │
│    - Re-run tests yourself                 │
│    - Load report into Validator            │
└─────────────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│ 6. Invoke Validator (G2) (15 min)         │
│    - 10-point checklist                    │
│    - Re-run all commands                   │
│    - Security scan                         │
│    - Mutation testing                      │
└─────────────────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│ 7. H3 Bridge (human decision) (10 min)    │
│    - 8-point human verification            │
│    - APPROVE/CONDITIONAL/REJECT            │
│    - Document G3 decision                  │
└─────────────────────────────────────────────┘
                   ↓
                DONE
```

**Benefits:**
- ✅ Strategic planning automated (Planner agent)
- ✅ TDD enforced (RED phase mandatory)
- ✅ Evidence tracked (EVIDENCE_LOG.md with hashes)
- ✅ Gate verification (G0, G1, G2, G3 checkpoints)
- ✅ Structured human decision (8-point checklist)

**Trade-off:**
- ⏱️ +15 minutes total time (60 min vs 45 min)
- ⏱️ +10 minutes human time (20 min vs 10 min)
- ✅ But much higher quality and auditability

---

### Cost-Benefit Analysis

| Dimension | Dual-Agent | H3A | Winner |
|-----------|------------|-----|--------|
| **Setup Time (first task)** | ~5 min | ~10 min | Dual-Agent |
| **Task Time (per task)** | ~45 min | ~60 min | Dual-Agent |
| **Human Time (per task)** | ~10 min | ~20 min | Dual-Agent |
| **TDD Compliance** | ~60% (optional) | 100% (enforced) | H3A |
| **Test Quality** | Medium | High | H3A |
| **Coverage** | ~75% avg | ~92% avg | H3A |
| **Security Scanning** | Sometimes | Always | H3A |
| **Mutation Testing** | Rarely | Always | H3A |
| **Evidence Trail** | Weak | Strong | H3A |
| **Auditability** | Low | High | H3A |
| **Compliance Readiness** | No | Yes | H3A |
| **Onboarding (new team member)** | ~1 hour | ~2 hours | Dual-Agent |
| **Defect Rate** | ~5-8% | ~1-2% | H3A |
| **Rework Rate** | ~15% | ~3% | H3A |

**Recommendation:**
- Use **Dual-Agent** for: Prototypes, spikes, throwaway code
- Use **H3A** for: Production code, regulated systems, long-term projects

---

## FAQ

### Q1: Can I run dual-agent and H3A in parallel?

**A:** Yes! H3A uses the same `runs/<run-id>/` structure, so both can coexist.

**Example:**
```bash
# Dual-agent run (legacy)
runs/20250128-101020-legacy/
  └── executor_report.json, validator_report.json

# H3A run (new)
runs/20250129-143022-h3a/
  └── state/, planner_report.json, executor_report.json, validator_report.json
```

Just don't mix workflows within the same run.

---

### Q2: Do I need to migrate old runs/ to H3A format?

**A:** No. Old runs stay in dual-agent format. Only new tasks use H3A.

**Why?** Migrating old runs is expensive (manual work) with low ROI. Historical data is fine as-is.

**Exception:** If you need to audit old runs, you can retro-actively generate H3A state files, but this is optional.

---

### Q3: What if Planner is overkill for simple tasks?

**A:** You have two options:

**Option A: Skip Planner (Degrade to Dual-Agent)**
```bash
# For trivial tasks (<50 LOC, obvious solution):
# 1. Don't invoke Planner
# 2. Manually write CURRENT_TASK.json
# 3. Proceed with Executor → Validator workflow

# Example:
cat > runs/<run-id>/state/CURRENT_TASK.json <<'EOF'
{
  "task_id": "T001",
  "goal": "Fix typo in README",
  "files": ["README.md"],
  "tdd_plan": {"red": "N/A", "green": "Fix typo", "refactor": "N/A"},
  "definition_of_done": ["Typo fixed"]
}
EOF

# Then invoke Executor
```

**Option B: Use "Fast Planner" Mode**
```bash
# Tell Planner: "This is a trivial task, create minimal plan"
# Planner generates simple ROADMAP.md in <2 minutes
```

**Recommendation:** Use Planner for all non-trivial tasks (>50 LOC or >1 file). Planning overhead is worth it.

---

### Q4: Can I automate H1, H2, H3 bridges?

**A:** Partially. You can automate verification checks, but human review is recommended for production.

**Example Automation:**
```bash
# scripts/h1_auto_bridge.sh
#!/bin/bash
RUN_ID=$1

# Auto-verify G0
jq -e '.gate_status == "G0_passed"' runs/$RUN_ID/state/SESSION_HANDOFF.json
if [ $? -ne 0 ]; then
  echo "❌ G0 not passed - ABORT"
  exit 1
fi

# Auto-verify TDD plan exists
jq -e '.tdd_plan.red' runs/$RUN_ID/state/CURRENT_TASK.json > /dev/null
if [ $? -ne 0 ]; then
  echo "❌ TDD plan incomplete - ABORT"
  exit 1
fi

echo "✅ H1 automated checks passed"
echo "👤 Human: Review CURRENT_TASK.json and invoke Executor"
```

**Warning:** Fully automated bridges skip human judgment. Use with caution in production.

---

### Q5: How do I handle multi-agent coordination issues?

**A:** Common scenarios:

**Scenario 1: Planner and Executor disagree on approach**

```
Problem: Planner says "Use regex", Executor wants "Use library"
Solution:
  1. Executor notes disagreement in executor_report.json
  2. Human reviews at H2 bridge
  3. Human decides: Follow Planner OR let Executor proceed
  4. Update CURRENT_TASK.json to reflect decision
```

**Scenario 2: Validator rejects Executor twice (iteration limit)**

```
Problem: Executor failed G1 twice, iteration limit reached
Solution:
  1. Validator escalates to human
  2. Human reviews root cause
  3. Options:
     - Human fixes issue directly
     - Planner revises task (too ambitious)
     - Executor tries different approach (reset iteration count)
```

**Scenario 3: Agent ignoring handoff contract**

```
Problem: Executor not reading CURRENT_TASK.json, doing own thing
Solution:
  1. H2 bridge detects mismatch
  2. Reject Executor handoff
  3. Explicitly tell Executor: "You MUST follow CURRENT_TASK.json"
  4. Invoke Executor again with emphasis
```

---

### Q6: What's the minimum viable H3A?

**A:** You can start with a simplified version:

**Minimal H3A (MVP):**
- ✅ Planner creates `CURRENT_TASK.json` (skip ROADMAP for single-task projects)
- ✅ Executor follows TDD, generates RED/GREEN evidence
- ✅ Validator runs 5-point checklist (skip mutation testing)
- ✅ Human does 4-point review (skip 8-point full checklist)

**What to skip for MVP:**
- ❌ GATES_LEDGER.md (use report file timestamps instead)
- ❌ EVIDENCE_LOG.md (trust artifacts exist without hashes)
- ❌ Mutation testing (time-consuming)
- ❌ Accessibility checks (unless UI changes)

**When to upgrade to full H3A:**
- When team comfortable with MVP (~2 weeks)
- When audit requirements demand it
- When defect rate too high

---

### Q7: How do I measure H3A adoption success?

**A:** Track these metrics:

**Adoption Metrics (First 30 Days):**
- % of tasks using H3A (target: 80% by day 30)
- # of runs/ with `state/` directory (shows H3A usage)
- Team survey: "H3A improves workflow" (target: ≥70% agree)

**Quality Metrics (First 90 Days):**
- TDD compliance rate (target: ≥95%)
- Average coverage (target: ≥90%)
- Defect rate (target: ≤2%)
- Rework rate (target: ≤5%)

**Efficiency Metrics (First 90 Days):**
- Time per task (may increase initially, should stabilize by day 60)
- G1 pass rate (1st try) (target: ≥80%)
- G2 pass rate (1st try) (target: ≥70%)
- Escalation rate (target: ≤5%)

**Collect via:**
```bash
# Generate adoption report
scripts/h3a_metrics.py --since 2025-01-01 --report runs/adoption_report.json
```

---

### Q8: What if my team resists H3A adoption?

**A:** Common objections and responses:

**Objection 1: "Too much overhead!"**

**Response:**
- H3A adds ~15 min per task initially
- After learning curve (~10 tasks), overhead drops to ~5 min
- Quality improvements save 10x more time (less rework, fewer bugs)

**Data:** Show defect rate comparison (H3A: 1-2%, dual-agent: 5-8%)

---

**Objection 2: "I don't need a Planner, I know what to do!"**

**Response:**
- Planner not for you, it's for next person reviewing your code
- ROADMAP.md documents intent for posterity
- Planner catches scope creep before coding starts

**Compromise:** Use "fast Planner mode" for simple tasks (<5 min planning)

---

**Objection 3: "TDD slows me down!"**

**Response:**
- RED→GREEN adds ~10% time upfront
- Saves 50%+ time in debugging (tests catch regressions immediately)
- Enables confident refactoring (tests prove correctness)

**Data:** Show coverage increase (dual-agent: 75%, H3A: 92%)

---

**Objection 4: "Bridge protocols feel like micromanagement!"**

**Response:**
- Bridges are checkpoints, not approvals
- Verify agent followed protocol, don't re-do work
- Automation available for routine checks (scripts/h1_auto_bridge.sh)

**Compromise:** Automate H1, keep human H2 and H3

---

### Q9: Can I use H3A with non-Python projects?

**A:** Yes! H3A is language-agnostic.

**Adaptations needed:**

**For JavaScript/Node.js:**
```bash
# RED phase
npm test > artifacts/executor/test_output_red.txt 2>&1

# Coverage
npm run coverage -- --coverage-dir=artifacts/executor/coverage/

# Linting
npm run lint > artifacts/executor/lint_output.txt

# Security
npm audit --json > artifacts/validator/security_scan.json
```

**For Java:**
```bash
# RED phase
mvn test > artifacts/executor/test_output_red.txt 2>&1

# Coverage
mvn jacoco:report
cp target/site/jacoco/* artifacts/executor/coverage/

# Mutation
mvn org.pitest:pitest-maven:mutationCoverage

# Security
mvn dependency-check:check -DoutputDirectory=artifacts/validator/
```

**For Go:**
```bash
# RED phase
go test ./... -v > artifacts/executor/test_output_red.txt 2>&1

# Coverage
go test -coverprofile=artifacts/executor/coverage.out ./...
go tool cover -html=artifacts/executor/coverage.out -o artifacts/executor/coverage.html

# Linting
golangci-lint run > artifacts/executor/lint_output.txt

# Security
gosec -fmt=json -out=artifacts/validator/security_scan.json ./...
```

**What changes:**
- Test commands (pytest → npm test → mvn test)
- Coverage tools (coverage.py → nyc → jacoco)
- Security scanners (bandit → npm audit → dependency-check)

**What stays the same:**
- State file schemas (ROADMAP.md, CURRENT_TASK.json)
- Gate framework (G0, G1, G2, G3)
- Handoff contracts (H1, H2, H3)
- Bridge protocols

---

### Q10: How do I extend H3A with custom gates?

**A:** H3A supports custom gates beyond G0-G3.

**Example: Add G2.5 (Performance Gate)**

**Step 1: Define gate in `gate_framework.md`**
```markdown
### G2.5: Performance Verification

**Owner:** Performance Engineer (or Validator)

**Entry Criteria:**
- G2 passed (all quality checks green)
- Application has performance requirements

**Exit Criteria:**
- Load test executed
- Response time ≤ SLA (e.g., p95 ≤ 200ms)
- Resource usage ≤ limits (CPU ≤ 80%, RAM ≤ 4GB)

**Evidence Required:**
- `artifacts/validator/load_test_report.json`
- `artifacts/validator/profiling_results.txt`
```

**Step 2: Add to GATES_LEDGER**
```bash
echo "$(date -Iseconds) | G2.5_started | performance_engineer | Load testing initiated" >> runs/<run-id>/state/GATES_LEDGER.md

# Run load test
artillery run load_test.yml -o artifacts/validator/load_test_report.json

# Verify results
jq '.aggregate.rps.mean' artifacts/validator/load_test_report.json
# If ≥ target RPS, pass G2.5

echo "$(date -Iseconds) | G2.5_passed | performance_engineer | p95 latency 185ms (target 200ms)" >> runs/<run-id>/state/GATES_LEDGER.md
```

**Step 3: Update workflow**
```
Executor (G1) → Validator (G2) → Performance Engineer (G2.5) → Human (G3)
```

**Other custom gates:**
- **G2.1: Accessibility Gate** (axe-core scan)
- **G2.2: Legal Review Gate** (license compliance)
- **G2.3: UX Review Gate** (design QA)

---

## Next Steps After Migration

### Immediate (Week 1)

- [ ] Complete 3-5 tasks using H3A
- [ ] Collect team feedback
- [ ] Update internal docs with H3A references
- [ ] Share success metrics with stakeholders

### Short-Term (Month 1)

- [ ] Train all team members on H3A
- [ ] Create custom automation scripts (h1_auto_bridge.sh, h3_quick_check.sh)
- [ ] Integrate H3A with CI/CD pipeline
- [ ] Add H3A metrics to team dashboard

### Long-Term (Quarter 1)

- [ ] Decommission dual-agent workflow (optional)
- [ ] Extend H3A with custom gates (G2.5, etc.)
- [ ] Build H3A UI dashboard (visualize GATES_LEDGER)
- [ ] Contribute improvements back to H3A project

---

## Additional Resources

### H3A Documentation
- **[H3A README](README.md)** - System overview
- **[Quick Start Guide](Quick_Start_Guide.md)** - End-to-end walkthrough
- **[Human Bridge Protocol](Human_Bridge_Protocol.md)** - H1, H2, H3 procedures
- **[Human Verification Checklist](Human_Verification_Checklist.md)** - 8-point G3 checklist
- **[Gate Framework](gate_framework.md)** - G0-G3 definitions
- **[State Specification](state_specification.md)** - State file schemas
- **[Handoff Contracts](handoff_contracts.md)** - Agent-to-agent expectations

### Scripts
- **`scripts/h3a_init.py`** - Initialize H3A run
- **`scripts/h3a_metrics.py`** - Generate adoption reports (if available)
- **`scripts/h1_auto_bridge.sh`** - Automate H1 verification (create if needed)
- **`scripts/h3_quick_check.sh`** - Automate H3 verification (create if needed)

### Community & Support
- **GitHub Issues:** Report bugs, request features
- **Slack/Discord:** `#h3a-migration` channel for questions
- **Office Hours:** Weekly Q&A sessions (if available)

---

## Conclusion

Migrating from dual-agent to H3A is a **strategic investment** in code quality, auditability, and team efficiency.

**Expected Outcomes (3 months post-migration):**
- ✅ TDD compliance: ≥95%
- ✅ Average coverage: ≥90%
- ✅ Defect rate: ≤2%
- ✅ Rework rate: ≤5%
- ✅ Team satisfaction: ≥70% "H3A improves workflow"

**Timeline:**
- **Week 1:** Complete first H3A task (~2-3 hours)
- **Week 2-4:** Adopt H3A for all new tasks (~30 min setup per task)
- **Month 2:** Full team proficiency (overhead drops to ~5 min per task)
- **Month 3:** Reap benefits (lower defects, higher velocity)

**Your migration journey:**
1. ✅ Read this guide
2. ✅ Test H3A on non-production task
3. ✅ Complete first production H3A task
4. ✅ Collect feedback, iterate
5. ✅ Scale to full team

**Good luck with your migration! 🚀**

---

**Questions?** See [FAQ](#faq) or contact your H3A champion.

**Feedback?** File issue in `docs/H3A_System/` GitHub repo or email team lead.

---

**Document History:**
- **v1.0.0 (2025-01-XX):** Initial release
- **Contributors:** [Your Name], [Team Lead]
- **License:** Internal use only (or specify open-source license)