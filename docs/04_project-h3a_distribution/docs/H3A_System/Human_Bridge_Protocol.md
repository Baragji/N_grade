# Human Bridge Protocol (H3A System)

**Version:** 1.0.0  
**Last Updated:** 2025-01-01  
**Status:** Production-Ready ✅

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Your Role as Human Bridge](#your-role-as-human-bridge)
3. [General Principles](#general-principles)
4. [Bridge Protocol: Planner → Executor (H1)](#bridge-protocol-planner--executor-h1)
5. [Bridge Protocol: Executor → Validator (H2)](#bridge-protocol-executor--validator-h2)
6. [Bridge Protocol: Validator → Human/System (H3)](#bridge-protocol-validator--humansystem-h3)
7. [Emergency Procedures](#emergency-procedures)
8. [Troubleshooting](#troubleshooting)
9. [Appendix: State File Reference](#appendix-state-file-reference)

---

## Overview

### What is the Human Bridge?

In the H3A (Hybrid 3-Agent) system, **you are the bridge** that connects autonomous agents:

```
🧠 PLANNER → 👤 YOU → ⚙️ EXECUTOR → 👤 YOU → ✅ VALIDATOR → 👤 YOU → 🚀 PRODUCTION
    (G0)        (H1)        (G1)         (H2)         (G2)        (H3)      (G3)
```

**Why humans are essential:**
- ✅ **Verify gate passage** - Did agent truly complete its gate obligations?
- ✅ **Provide context** - Load correct state files for next agent
- ✅ **Break deadlocks** - Intervene when agents iterate endlessly
- ✅ **Make final call** - Approve production deployment (G3 gate)

**What you DON'T do:**
- ❌ Write code (agents do that)
- ❌ Fix bugs (that's Executor's job during remediation)
- ❌ Run tests manually (agents run all commands)

---

## Your Role as Human Bridge

### Core Responsibilities

| Responsibility | When | What You Do |
|----------------|------|-------------|
| **Verify Gate Passage** | After each agent completes | Check GATES_LEDGER.md for gate status |
| **Load Context** | Before invoking next agent | Copy relevant state files into agent prompt |
| **Monitor Progress** | During agent work | Watch for completion signals |
| **Escalate Issues** | When agent fails 2x | Review error, decide remediation or abort |
| **Make G3 Decision** | After Validator passes G2 | Approve production deployment |

### Time Investment

| Bridge | Typical Duration | What You're Doing |
|--------|------------------|-------------------|
| **H1: Planner → Executor** | 2-5 minutes | Read CURRENT_TASK.json, verify task is small/testable |
| **H2: Executor → Validator** | 3-7 minutes | Skim executor_report.json, check evidence artifacts exist |
| **H3: Validator → Human** | 5-15 minutes | Review validator_report.json, read 10-point checklist |

**Total per task:** ~10-27 minutes of human oversight

---

## General Principles

### 1. **Trust but Verify**
- Agents are powerful but can hallucinate
- Always check state files, don't rely on agent's verbal summary
- If unsure, re-run a verification command yourself

### 2. **State Files are Source of Truth**
- Agent's chat messages ≠ reality
- `GATES_LEDGER.md` tells you gate status
- `SESSION_HANDOFF.json` tells you next agent + context

### 3. **Don't Skip Gates**
- Each gate has entry/exit criteria for a reason
- Skipping = risk of untested code, scope creep, security issues
- When in doubt, escalate to team lead

### 4. **Iteration Limits are Hard Stops**
- Max 2 attempts per gate before human review
- Prevents infinite loops (agent trying same failed approach)
- After 2 failures, you must diagnose root cause

### 5. **Evidence is Mandatory**
- No artifact = gate not passed
- Example: G1 (Executor) requires `test_output_red.txt` + `test_output_green.txt`
- If files missing, Executor hasn't completed TDD cycle

---

## Bridge Protocol: Planner → Executor (H1)

### When to Use
After Planner completes G0 gate and writes `state/SESSION_HANDOFF.json` with `"handoff_to": "executor"`.

---

### Step-by-Step Bridge Procedure

#### **Step 1: Verify G0 Gate Passage** (2 minutes)

**Check 1: GATES_LEDGER.md**
```bash
cd runs/<run-id>
cat state/GATES_LEDGER.md | grep "G0:"
```

**Expected Output:**
```markdown
## Gate: G0 (Planning)
- **Status:** ✅ PASSED
- **Timestamp:** 2025-01-01T10:15:00Z
- **Agent:** Planner
- **Evidence:** ROADMAP.md, CURRENT_TASK.json, planner_report.json
```

**If Status ≠ PASSED:**
- ❌ Stop! Planner has not completed G0
- Read planner_report.json for details
- Address issues before proceeding

---

**Check 2: CURRENT_TASK.json Exists**
```bash
ls -lh state/CURRENT_TASK.json
```

**Expected:** File exists, size > 0 bytes

**If Missing:**
- ❌ Stop! Planner didn't create task spec
- Re-invoke Planner with clear brief

---

**Check 3: Task is Small/Testable**

Open `state/CURRENT_TASK.json` and verify:

```json
{
  "task_id": "T001",
  "goal": "Add email validation to User model",
  "scope": {
    "files_to_modify": ["src/models/user.py", "tests/test_user.py"],
    "estimated_loc": 120,
    "touch_only_listed": true
  },
  "tdd_plan": {
    "red": "Write test_email_validation_valid() and test_email_validation_invalid()",
    "green": "Implement validate_email() method in User model",
    "refactor": "Extract regex pattern to constant"
  },
  "definition_of_done": [ /* 10 items */ ]
}
```

**Quality Checks:**
- ✅ `files_to_modify` lists 1-3 files?
- ✅ `estimated_loc` < 200?
- ✅ `tdd_plan` has RED/GREEN/REFACTOR phases?
- ✅ `definition_of_done` has ~10 items?

**If Any Check Fails:**
- ❌ Send back to Planner: "Task too large, decompose further"

---

#### **Step 2: Prepare Executor Context** (1 minute)

**Context to Load:**

1. **Primary Input:** `state/CURRENT_TASK.json` (entire file)
2. **Supporting Context:**
   - `state/ROADMAP.md` (first 50 lines for overall context)
   - `planner_report.json` (optional, if task is complex)

**What NOT to load:**
- ❌ Previous executor/validator reports (creates confusion)
- ❌ Old artifacts (agents should only see current task)
- ❌ Full chat history (agents are stateless)

---

#### **Step 3: Invoke Executor** (30 seconds)

**In your AI agent interface (Custom GPT, Claude, IDE):**

1. **Load Executor Prompt:**
   - Copy contents of `prompts/executor_prompt.md`
   - Paste into agent system instructions

2. **Provide Context:**
   ```
   You are the Executor agent in the H3A system.
   
   Your task specification is in the file below:
   
   <CURRENT_TASK>
   [paste entire state/CURRENT_TASK.json here]
   </CURRENT_TASK>
   
   Working directory: runs/<run-id>/
   
   Begin implementation following TDD cycle: RED → GREEN → REFACTOR.
   ```

3. **Monitor Execution:**
   - Executor will write code, run tests, save evidence
   - Watch for completion signal: "✅ G1 Gate Passed"

---

#### **Step 4: Completion Check** (1 minute)

**After Executor signals completion:**

```bash
# Check G1 gate
cat state/GATES_LEDGER.md | grep "G1:"

# Check evidence artifacts
ls -lh artifacts/executor/
```

**Expected Artifacts (minimum 7 files):**
- ✅ `test_output_red.txt` - Failing tests (RED phase)
- ✅ `test_output_green.txt` - Passing tests (GREEN phase)
- ✅ `test_output_full_suite.txt` - No regressions
- ✅ `lint_output.txt`
- ✅ `mypy_output.txt`
- ✅ `mutation_output.txt`
- ✅ `coverage_output.txt`

**If Any Missing:**
- ❌ Executor hasn't completed G1 obligations
- Ask Executor: "Please save missing evidence artifacts"

---

#### **Step 5: Handoff to Validator** (30 seconds)

Once G1 passed:

```bash
cat state/SESSION_HANDOFF.json
```

**Expected:**
```json
{
  "from": "executor",
  "to": "validator",
  "handoff_contract": "H2",
  "context": {
    "task_id": "T001",
    "executor_report": "executor_report.json",
    "evidence_dir": "artifacts/executor/"
  }
}
```

✅ **H1 Bridge Complete!** → Proceed to H2 (Executor → Validator)

---

## Bridge Protocol: Executor → Validator (H2)

### When to Use
After Executor completes G1 gate and writes `state/SESSION_HANDOFF.json` with `"handoff_to": "validator"`.

---

### Step-by-Step Bridge Procedure

#### **Step 1: Verify G1 Gate Passage** (3 minutes)

**Check 1: GATES_LEDGER.md**
```bash
cat state/GATES_LEDGER.md | grep "G1:"
```

**Expected Output:**
```markdown
## Gate: G1 (Implementation)
- **Status:** ✅ PASSED
- **Timestamp:** 2025-01-01T10:45:00Z
- **Agent:** Executor
- **Evidence:** executor_report.json, 7 artifacts in artifacts/executor/
```

---

**Check 2: Executor Report**
```bash
cat executor_report.json | jq '.gate_status'
```

**Expected:**
```json
{
  "gate": "G1",
  "status": "passed",
  "tdd_evidence": {
    "red_phase": "artifacts/executor/test_output_red.txt",
    "green_phase": "artifacts/executor/test_output_green.txt"
  }
}
```

---

**Check 3: Artifact Integrity**

```bash
# Verify RED phase occurred BEFORE GREEN phase
stat -f "%m %N" artifacts/executor/test_output_red.txt
stat -f "%m %N" artifacts/executor/test_output_green.txt
```

**Expected:** RED modification time < GREEN modification time  
(Proves chronological TDD cycle)

---

**Check 4: Skim Evidence Files**

Quick sanity check (don't re-run commands, Validator will do that):

```bash
# Check RED phase shows failures
head -20 artifacts/executor/test_output_red.txt

# Check GREEN phase shows passes
head -20 artifacts/executor/test_output_green.txt
```

**Red Flags:**
- ❌ RED file shows all tests passing → TDD violation
- ❌ GREEN file shows failures → Implementation incomplete
- ❌ Evidence files are empty → Executor didn't save outputs

**If Red Flags:**
- Send back to Executor: "TDD evidence invalid, please fix"

---

#### **Step 2: Prepare Validator Context** (2 minutes)

**Context to Load:**

1. **Primary Input:** `executor_report.json` (entire file)
2. **Supporting Context:**
   - `state/CURRENT_TASK.json` (original requirements)
   - Path to evidence: `artifacts/executor/` (Validator will re-run commands)

**What NOT to load:**
- ❌ Evidence file contents (Validator must verify independently)
- ❌ Previous validator reports (creates bias)

---

#### **Step 3: Invoke Validator** (30 seconds)

**In your AI agent interface:**

1. **Load Validator Prompt:**
   - Copy contents of `prompts/validator_prompt.md`
   - Paste into agent system instructions

2. **Provide Context:**
   ```
   You are the Validator agent in the H3A system.
   
   Executor has completed implementation. Your job: verify ALL claims independently.
   
   <EXECUTOR_REPORT>
   [paste entire executor_report.json here]
   </EXECUTOR_REPORT>
   
   <ORIGINAL_TASK>
   [paste state/CURRENT_TASK.json here]
   </ORIGINAL_TASK>
   
   Working directory: runs/<run-id>/
   Evidence directory: artifacts/executor/
   
   Begin 10-point verification. DO NOT TRUST executor claims - re-run all commands.
   ```

3. **Monitor Validation:**
   - Validator will re-run tests, lint, coverage, mutation, security
   - Watch for completion signal: "✅ G2 Gate Decision: PASS" (or FAIL/ESCALATE)

---

#### **Step 4: Review Validation Results** (5 minutes)

**After Validator completes:**

```bash
cat state/GATES_LEDGER.md | grep "G2:"
```

**Expected Output:**
```markdown
## Gate: G2 (Validation)
- **Status:** ✅ PASSED | ⚠️ NEEDS_REMEDIATION | ❌ FAILED
- **Timestamp:** 2025-01-01T11:15:00Z
- **Agent:** Validator
- **Checklist:** 10/10 checks passed
```

---

**Review Validator Report:**

```bash
cat validator_report.json | jq '.validation_results'
```

**Key Sections:**

```json
{
  "gate": "G2",
  "decision": "PASS",  // or FAIL, ESCALATE
  "checks_passed": 10,
  "checks_failed": 0,
  "validation_results": {
    "check_01_tdd_compliance": {"status": "✅ PASS", "evidence": "..."},
    "check_02_test_quality": {"status": "✅ PASS", "evidence": "..."},
    "check_03_coverage": {"status": "✅ PASS", "evidence": "..."},
    // ... (10 total)
  },
  "discrepancies": [],  // Empty if no issues
  "remediation_plan": null  // Null if PASS
}
```

---

**Possible Outcomes:**

### **Outcome 1: ✅ PASS (All 10 Checks Passed)**

```json
{
  "decision": "PASS",
  "checks_passed": 10,
  "checks_failed": 0,
  "approval_for_next_task": true
}
```

**Your Action:**
- ✅ Proceed to H3 bridge (Validator → Human for G3 decision)
- No further action needed

---

### **Outcome 2: ⚠️ NEEDS_REMEDIATION (1-3 Checks Failed, Fixable)**

```json
{
  "decision": "NEEDS_REMEDIATION",
  "checks_passed": 8,
  "checks_failed": 2,
  "failed_checks": ["check_04_mutation_score", "check_06_code_quality"],
  "remediation_plan": {
    "issue": "Mutation score 85% (requires ≥90%)",
    "fix_steps": [
      "Strengthen assertions in test_email_validation_invalid()",
      "Add edge case tests for empty string, null",
      "Re-run mutation tests"
    ],
    "estimated_effort": "10-15 minutes"
  }
}
```

**Your Action:**
1. Read `remediation_plan.fix_steps`
2. Send back to Executor with remediation instructions
3. Executor fixes issues, re-submits
4. Validator re-runs checks
5. **Iteration limit:** Max 2 remediation cycles, then escalate

---

### **Outcome 3: ❌ FAILED (>3 Checks Failed or Critical Issue)**

```json
{
  "decision": "FAILED",
  "checks_passed": 6,
  "checks_failed": 4,
  "critical_issues": [
    "TDD compliance violated: No RED phase evidence",
    "Security scan found 2 high-severity issues",
    "Coverage decreased by 3.2%"
  ],
  "escalation_required": true,
  "escalation_reason": "Multiple fundamental issues, requires human review"
}
```

**Your Action:**
1. **STOP** - Do not proceed to G3
2. Review critical issues
3. Decide:
   - **Option A:** Send entire task back to Planner (task poorly scoped)
   - **Option B:** Send to Executor with specific fix instructions
   - **Option C:** Abort task (requirements unclear, need stakeholder input)

---

### **Outcome 4: 🚨 ESCALATE (Agent Uncertain or Deadlock)**

```json
{
  "decision": "ESCALATE",
  "escalation_reason": "Executor claims coverage increased but I measured decrease. Possible environment issue.",
  "human_decision_required": true
}
```

**Your Action:**
1. Investigate discrepancy:
   - Check environment (Python version, dependencies)
   - Check test isolation (tests depending on order?)
   - Re-run commands yourself manually
2. Make call:
   - If Executor correct: Override Validator (document reason)
   - If Validator correct: Send back to Executor
   - If unclear: Escalate to tech lead

---

#### **Step 5: Handoff Decision** (1 minute)

**If G2 PASSED:**
```bash
cat state/SESSION_HANDOFF.json
```

**Expected:**
```json
{
  "from": "validator",
  "to": "human",
  "handoff_contract": "H3",
  "context": {
    "task_id": "T001",
    "validator_report": "validator_report.json",
    "decision": "PASS",
    "g3_approval_required": true
  }
}
```

✅ **H2 Bridge Complete!** → Proceed to H3 (Validator → Human for G3 gate)

---

## Bridge Protocol: Validator → Human/System (H3)

### When to Use
After Validator completes G2 gate with "PASS" decision and writes `state/SESSION_HANDOFF.json` with `"handoff_to": "human"`.

---

### Step-by-Step Bridge Procedure

#### **Step 1: Verify G2 Gate Passage** (2 minutes)

**Check 1: GATES_LEDGER.md**
```bash
cat state/GATES_LEDGER.md | grep "G2:"
```

**Expected:**
```markdown
## Gate: G2 (Validation)
- **Status:** ✅ PASSED
- **Timestamp:** 2025-01-01T11:45:00Z
- **Agent:** Validator
- **Checklist:** 10/10 checks passed
- **Decision:** Approved for G3 gate
```

**If Status ≠ PASSED:**
- ❌ Stop! Task not ready for production consideration
- Address G2 failures before proceeding

---

**Check 2: Validator Report**
```bash
cat validator_report.json | jq '.decision'
```

**Expected:**
```json
{
  "decision": "PASS",
  "checks_passed": 10,
  "checks_failed": 0,
  "approval_for_next_task": true
}
```

---

#### **Step 2: Human Verification** (10-15 minutes)

**Use the Human Verification Checklist:**

See [Human_Verification_Checklist.md](./Human_Verification_Checklist.md) for complete guide.

**Quick Summary (you verify 8 points):**

1. ✅ **Requirements Met** - Does code solve the original problem?
2. ✅ **Tests Pass** - Re-run test suite yourself
3. ✅ **No Broken Features** - Quick smoke test
4. ✅ **Code Readable** - Skim changed files
5. ✅ **Security Check** - No secrets, proper validation
6. ✅ **Documentation Updated** - Docstrings, README if needed
7. ✅ **Evidence Complete** - All artifacts have hashes in EVIDENCE_LOG.md
8. ✅ **Intent Alignment** - No scope creep or unexpected changes

**Spot Check Commands:**

```bash
# Re-run test suite
pytest tests/

# Check coverage
pytest --cov=src --cov-report=term-missing

# Quick lint check
ruff check src/ tests/

# Review changed files
git diff main...HEAD
```

---

#### **Step 3: Make G3 Decision** (2 minutes)

**Three Possible Decisions:**

### **Decision 1: ✅ APPROVE (Deploy to Production)**

**When:** All 8 verification points passed, code looks good, no red flags

**Action:**
```bash
# Update GATES_LEDGER.md
echo "## Gate: G3 (Production-Ready)
- **Status:** ✅ APPROVED
- **Timestamp:** $(date -u +"%Y-%m-%dT%H:%M:%SZ")
- **Approver:** [Your Name]
- **Evidence:** All artifacts verified, human checklist 8/8 passed
- **Next Action:** Ready for deployment
" >> state/GATES_LEDGER.md

# Optional: Tag this task as complete
git tag -a "task-T001-complete" -m "Email validation feature approved for production"
```

**Next Steps:**
- Merge PR / Deploy code
- If ROADMAP has more tasks → Return to H1 (Planner loads next task)
- If ROADMAP complete → Project done! 🎉

---

### **Decision 2: ⚠️ CONDITIONAL APPROVAL (Minor Fixes Needed)**

**When:** 6-7/8 verification points passed, but minor issues (e.g., missing docstring, typo in comment)

**Action:**
```bash
# Create fix ticket
echo "## Minor Fixes Required for T001
- Missing docstring for validate_email()
- Typo in test name: 'test_email_validaton_invalid' → 'test_email_validation_invalid'

Approval pending these fixes.
" > state/G3_CONDITIONAL_FIXES.md

# Send back to Executor
```

**Iteration Limit:** 1 round of minor fixes, then must approve or reject

---

### **Decision 3: ❌ REJECT (Block Production)**

**When:** <6/8 verification points passed, OR critical issue discovered (security, data loss risk, broken feature)

**Action:**
```bash
# Update GATES_LEDGER.md
echo "## Gate: G3 (Production-Ready)
- **Status:** ❌ REJECTED
- **Timestamp:** $(date -u +"%Y-%m-%dT%H:%M:%SZ")
- **Approver:** [Your Name]
- **Reason:** [e.g., 'Security concern: email validation accepts SQL injection patterns']
- **Next Action:** Return to Executor for fix
" >> state/GATES_LEDGER.md

# Create rejection report
```

**Escalation Required:** Send entire task back to Planner if issue is fundamental (wrong approach, poor design)

---

#### **Step 4: Update Roadmap** (1 minute)

**If APPROVED:**

```bash
# Mark task as complete in ROADMAP.md
sed -i '' 's/- \[ \] T001: Add email validation/- [x] T001: Add email validation (Completed 2025-01-01)/g' state/ROADMAP.md
```

**Check for next task:**
```bash
grep "- \[ \]" state/ROADMAP.md | head -1
```

**If next task exists:**
- ✅ Return to H1 (Planner → Executor bridge)
- Planner loads next task from ROADMAP

**If no more tasks:**
- 🎉 **Project Complete!**
- Archive run: `tar -czf runs/<run-id>.tar.gz runs/<run-id>/`

---

#### **Step 5: Document Decision** (2 minutes)

**Create G3 report:**

```bash
cat > g3_approval_report.json << 'EOF'
{
  "gate": "G3",
  "task_id": "T001",
  "decision": "APPROVED",
  "timestamp": "2025-01-01T12:00:00Z",
  "approver": "[Your Name]",
  "human_verification": {
    "requirements_met": true,
    "tests_pass": true,
    "no_broken_features": true,
    "code_readable": true,
    "security_ok": true,
    "docs_updated": true,
    "evidence_complete": true,
    "intent_aligned": true
  },
  "notes": "Feature looks good, no issues found during spot checks.",
  "deployment_approved": true
}
EOF
```

**Archive evidence:**
```bash
# Optional: Copy all evidence to permanent archive
mkdir -p /project/evidence_archive/
cp -r runs/<run-id>/ /project/evidence_archive/task-T001-$(date +%Y%m%d)/
```

✅ **H3 Bridge Complete!** → Task approved for production

---

## Emergency Procedures

### 🚨 Emergency Stop

**When to use:** Agent is stuck in infinite loop, making harmful changes, or violating security policies

**Procedure:**

1. **Stop the Agent Immediately**
   - Kill IDE agent process
   - Or: Close Custom GPT / Claude session

2. **Assess Damage**
   ```bash
   # Check what files were modified
   git status
   
   # Review changes
   git diff
   
   # Check if tests still pass
   pytest tests/
   ```

3. **Rollback if Needed**
   ```bash
   # Revert uncommitted changes
   git restore .
   
   # Or: Restore from last commit
   git reset --hard HEAD
   ```

4. **Document Incident**
   ```bash
   echo "## Emergency Stop - $(date)
   - Agent: [Planner/Executor/Validator]
   - Reason: [e.g., 'Executor modifying files outside scope']
   - Action Taken: [e.g., 'Killed process, reverted changes']
   - Root Cause: [e.g., 'Task scope too vague']
   " >> state/INCIDENT_LOG.md
   ```

5. **Decide Next Action:**
   - **Option A:** Re-invoke agent with clearer instructions
   - **Option B:** Manually fix issue, skip to next gate
   - **Option C:** Abort task, return to Planner

---

### ⚠️ Agent Iteration Limit Exceeded

**When to use:** Agent has failed same gate 2 times

**Procedure:**

1. **Read Failure Reports**
   ```bash
   # Check how many attempts
   grep "Status: ❌ FAILED" state/GATES_LEDGER.md | wc -l
   
   # Read latest failure
   tail -50 [planner/executor/validator]_report.json
   ```

2. **Diagnose Root Cause**
   
   **Common Causes:**
   
   | Cause | Symptom | Fix |
   |-------|---------|-----|
   | **Vague Requirements** | Planner creates different tasks each attempt | Clarify requirements, provide examples |
   | **Environment Issue** | Tests fail with "ModuleNotFoundError" | Fix dependencies, update requirements.txt |
   | **Test Flakiness** | Tests pass sometimes, fail randomly | Fix non-deterministic tests (timing, randomness) |
   | **Agent Hallucination** | Agent claims tests pass but they fail | Provide explicit command outputs to agent |
   | **Scope Creep** | Agent keeps adding "extra features" | Make scope restrictions explicit in task |

3. **Escalate to Human**
   - Review issue with tech lead
   - Decide: Fix root cause, or manually intervene

4. **Document Resolution**
   ```bash
   echo "## Iteration Limit Resolution - $(date)
   - Agent: [name]
   - Gate: [G0/G1/G2]
   - Failures: 2
   - Root Cause: [diagnosis]
   - Resolution: [what you did]
   " >> state/ITERATION_LOG.md
   ```

---

### 🔄 Agent Handoff Mismatch

**When to use:** `SESSION_HANDOFF.json` doesn't match expected workflow

**Example Issue:**
```json
{
  "from": "executor",
  "to": "planner"  // ❌ Wrong! Should be "validator"
}
```

**Procedure:**

1. **Verify Current Gate**
   ```bash
   tail -20 state/GATES_LEDGER.md
   ```

2. **Manually Fix Handoff**
   ```bash
   # Correct the handoff
   cat > state/SESSION_HANDOFF.json << 'EOF'
   {
     "from": "executor",
     "to": "validator",
     "handoff_contract": "H2",
     "context": {
       "task_id": "T001",
       "executor_report": "executor_report.json"
     }
   }
   EOF
   ```

3. **Document Manual Override**
   ```bash
   echo "## Manual Handoff Override - $(date)
   - Original: executor → planner
   - Corrected: executor → validator
   - Reason: [e.g., 'Executor confused about workflow']
   " >> state/GATES_LEDGER.md
   ```

4. **Continue with Correct Bridge**

---

## Troubleshooting

### Issue: "State file not found"

**Symptom:**
```bash
cat: state/CURRENT_TASK.json: No such file or directory
```

**Diagnosis:**
- Agent didn't complete gate obligations
- Or: Wrong working directory

**Fix:**
```bash
# Check if you're in correct run directory
pwd  # Should show: /path/to/runs/<run-id>/

# Check what files exist
ls -la state/

# If completely missing, re-initialize
cd /path/to/project/
python scripts/h3a_init.py --task-brief "Your brief"
```

---

### Issue: "Agent keeps failing same test"

**Symptom:** Executor runs TDD cycle, but same test fails in GREEN phase multiple times

**Diagnosis:**
- Test is too strict (expecting exact string when logic is correct)
- Or: Test has bug (not implementation)
- Or: Environment issue (missing dependency)

**Fix:**

1. **Review the test:**
   ```bash
   cat tests/test_user.py | grep -A 20 "def test_email_validation"
   ```

2. **Run test yourself:**
   ```bash
   pytest tests/test_user.py::test_email_validation_valid -v
   ```

3. **Check test is correct:**
   - Does test match requirements?
   - Is assertion too strict?
   - Is test isolated (no dependencies on other tests)?

4. **If test is wrong:**
   ```bash
   # Fix the test manually
   # Then tell Executor: "Test has been corrected, re-run GREEN phase"
   ```

5. **If test is correct:**
   - Send more explicit hint to Executor
   - Or: Show Executor the expected implementation pattern

---

### Issue: "Validator reports discrepancy"

**Symptom:**
```json
{
  "discrepancies": [
    {
      "check": "coverage",
      "executor_claim": "95.2%",
      "validator_measurement": "89.7%",
      "explanation": "Executor may have run tests with different flags"
    }
  ]
}
```

**Diagnosis:**
- Environment difference (Executor vs Validator ran in different contexts)
- Or: Executor lied/hallucinated
- Or: Timing issue (tests run at different times, code changed)

**Fix:**

1. **Re-run command yourself:**
   ```bash
   pytest --cov=src --cov-report=term-missing
   ```

2. **Compare all three outputs:**
   - Your measurement
   - Executor's claim (in `artifacts/executor/coverage_output.txt`)
   - Validator's measurement (in `artifacts/validator/check_03_coverage.txt`)

3. **If all match Validator:**
   - Executor was wrong
   - Send back to Executor: "Your coverage claim was incorrect, please re-measure"

4. **If all match Executor:**
   - Validator had environment issue
   - Override Validator decision (document reason)

5. **If all different:**
   - Environment is non-deterministic (tests have randomness?)
   - Fix root cause (seed random, fix timing issues)

---

### Issue: "G3 decision is unclear"

**Symptom:** You're at G3 gate, but unsure if code should be approved (some aspects look good, others questionable)

**Decision Framework:**

Ask yourself:

1. **Is there ANY security risk?**
   - If YES → ❌ REJECT (security always blocks deployment)

2. **Will this break production?**
   - If YES → ❌ REJECT
   - If MAYBE → ⚠️ CONDITIONAL APPROVAL (require more testing)

3. **Does it solve the original requirement?**
   - If NO → ❌ REJECT (intent misalignment)
   - If PARTIALLY → ⚠️ CONDITIONAL APPROVAL

4. **Are there only cosmetic issues?** (typos, missing comments, style)
   - If YES → ✅ APPROVE (create follow-up ticket for cosmetic fixes)

5. **When in doubt:**
   - ⚠️ CONDITIONAL APPROVAL with specific fix list
   - Or: Escalate to tech lead for second opinion

**Never approve if you're uncertain about security or correctness!**

---

### Issue: "ROADMAP is empty"

**Symptom:**
```bash
cat state/ROADMAP.md
# File exists but has no tasks
```

**Diagnosis:**
- Planner never created roadmap
- Or: All tasks already complete

**Fix:**

1. **Check if initialization was correct:**
   ```bash
   # Look for task brief
   cat planner_report.json | jq '.task_brief'
   ```

2. **If brief is missing:**
   - Re-invoke Planner with clear requirements:
     ```
     Create a roadmap for: [your feature description]
     
     Break down into small, testable tasks (<200 LOC each).
     ```

3. **If brief exists but no tasks:**
   - Planner may have misunderstood
   - Provide example task decomposition
   - Ask Planner to create at least 1-3 concrete tasks

---

## Appendix: State File Reference

### Quick Reference Table

| File | Owner | Purpose | When Created | When Read |
|------|-------|---------|--------------|-----------|
| **ROADMAP.md** | Planner | Overall task sequence | G0 passage | Planner (to load next task) |
| **CURRENT_TASK.json** | Planner | Active task spec | G0 passage | Executor (H1) |
| **GATES_LEDGER.md** | All agents | Gate progression log | Initialization | All agents (audit trail) |
| **EVIDENCE_LOG.md** | All agents | Artifact hashes | Initialization | Validator, Human (integrity check) |
| **SESSION_HANDOFF.json** | All agents | Next agent + context | After each gate | Human bridges (routing) |
| **planner_report.json** | Planner | Planning summary | G0 passage | Human (H1 bridge) |
| **executor_report.json** | Executor | Implementation summary | G1 passage | Validator (H2 bridge) |
| **validator_report.json** | Validator | Validation summary | G2 passage | Human (H3 bridge) |
| **g3_approval_report.json** | Human | Production decision | G3 passage | Archive (compliance) |

---

### State File Locations

```
runs/<run-id>/
├── state/
│   ├── ROADMAP.md              # Planner creates, all read
│   ├── CURRENT_TASK.json       # Planner creates, Executor reads
│   ├── GATES_LEDGER.md         # All agents append
│   ├── EVIDENCE_LOG.md         # All agents append
│   └── SESSION_HANDOFF.json    # All agents update
├── planner_report.json         # Planner writes
├── executor_report.json        # Executor writes
├── validator_report.json       # Validator writes
├── g3_approval_report.json     # Human writes
└── artifacts/
    ├── planner/
    ├── executor/
    └── validator/
```

---

### Example: Complete H1 → H2 → H3 Flow

**Scenario:** Add email validation to User model

#### **H1: Planner → Executor**

```bash
# 1. Verify G0 passed
cat state/GATES_LEDGER.md | grep "G0:"
# ✅ PASSED

# 2. Check task
cat state/CURRENT_TASK.json
# Task looks good: 2 files, 120 LOC, TDD plan included

# 3. Invoke Executor
# (copy executor_prompt.md + CURRENT_TASK.json into agent)

# 4. Wait for completion
# Executor signals: "✅ G1 Gate Passed"
```

#### **H2: Executor → Validator**

```bash
# 1. Verify G1 passed
cat state/GATES_LEDGER.md | grep "G1:"
# ✅ PASSED

# 2. Check evidence
ls artifacts/executor/
# 7 files present ✅

# 3. Invoke Validator
# (copy validator_prompt.md + executor_report.json into agent)

# 4. Wait for validation
# Validator signals: "✅ G2 Gate Decision: PASS (10/10 checks passed)"
```

#### **H3: Validator → Human**

```bash
# 1. Verify G2 passed
cat state/GATES_LEDGER.md | grep "G2:"
# ✅ PASSED

# 2. Human verification (8 points)
pytest tests/  # ✅ All pass
git diff       # ✅ Changes look good
# ... (8 checks)

# 3. Make G3 decision
echo "G3: ✅ APPROVED" >> state/GATES_LEDGER.md

# 4. Mark task complete
sed -i '' 's/- \[ \] T001/- [x] T001/' state/ROADMAP.md

# 5. Check for next task
grep "- \[ \]" state/ROADMAP.md
# Next task: T002

# → Return to H1 (Planner loads T002)
```

---

## Summary

### Bridge Responsibilities

| Bridge | Time | Your Role |
|--------|------|-----------|
| **H1: Planner → Executor** | 2-5 min | Verify G0, check task is small, load context |
| **H2: Executor → Validator** | 3-7 min | Verify G1, check evidence exists, load reports |
| **H3: Validator → Human** | 5-15 min | Verify G2, human checklist (8 points), make G3 decision |

**Total:** ~10-27 minutes per task

---

### Key Principles

1. ✅ **Always check GATES_LEDGER.md** - Source of truth for gate status
2. ✅ **Evidence is mandatory** - No artifacts = gate not passed
3. ✅ **Iteration limits are hard stops** - Max 2 attempts, then escalate
4. ✅ **Don't skip gates** - Each gate catches specific quality issues
5. ✅ **When uncertain, escalate** - Better safe than deploy broken code

---

### Quick Commands Cheat Sheet

```bash
# Check current gate status
tail -20 state/GATES_LEDGER.md

# Check next handoff
cat state/SESSION_HANDOFF.json

# List evidence artifacts
ls -lh artifacts/executor/
ls -lh artifacts/validator/

# Verify TDD chronology
stat -f "%m %N" artifacts/executor/test_output_red.txt
stat -f "%m %N" artifacts/executor/test_output_green.txt

# Re-run tests yourself
pytest tests/

# Check coverage
pytest --cov=src --cov-report=term-missing

# Review changes
git diff

# Mark task complete
sed -i '' 's/- \[ \] T001/- [x] T001/' state/ROADMAP.md
```

---

## Version History

- **v1.0.0** (2025-01-01): Initial production release

---

**🎉 You're now ready to bridge H3A agents!**

For examples, see [Quick_Start_Guide.md](./Quick_Start_Guide.md)  
For human verification checklist, see [Human_Verification_Checklist.md](./Human_Verification_Checklist.md)