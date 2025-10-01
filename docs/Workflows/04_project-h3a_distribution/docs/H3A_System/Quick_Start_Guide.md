# H3A Quick Start Guide

**Version:** 1.0.0  
**Last Updated:** 2025-01-01  
**Status:** Production-Ready ✅

---

## 📋 Table of Contents

1. [What is H3A?](#what-is-h3a)
2. [5-Minute Setup](#5-minute-setup)
3. [Your First Task: Complete Walkthrough](#your-first-task-complete-walkthrough)
4. [Real-World Example](#real-world-example)
5. [Common Workflows](#common-workflows)
6. [Troubleshooting Quick Fixes](#troubleshooting-quick-fixes)
7. [Next Steps](#next-steps)

---

## What is H3A?

**H3A** = **Hybrid 3-Agent System**

A production-grade workflow for building software with AI agents:

```
USER BRIEF
    ↓
🧠 PLANNER → Breaks work into small tasks, creates TDD plan
    ↓
⚙️ EXECUTOR → Implements with RED→GREEN→REFACTOR TDD cycle
    ↓
✅ VALIDATOR → Verifies quality (10-point checklist)
    ↓
👤 HUMAN → Final approval for production (G3 gate)
    ↓
🚀 PRODUCTION
```

### Why Use H3A?

✅ **TDD Enforced** - No "I'll add tests later" (evidence required)  
✅ **Quality Guaranteed** - 10-point validation checklist before deployment  
✅ **Audit Trail** - Complete evidence log with SHA-256 hashes  
✅ **No Scope Creep** - Agents only touch specified files  
✅ **Zero-Trust** - Validator independently verifies all claims  
✅ **Compliance Ready** - Maps to GDPR, SOC 2, OWASP, ISO 42001  

---

## 5-Minute Setup

### Prerequisites

```bash
# 1. Python 3.9+
python --version

# 2. Project initialized with git
git status

# 3. Tests can run
pytest tests/

# 4. AI agent access (one of):
#    - Custom GPT (ChatGPT Plus)
#    - Claude Projects (Claude Pro)
#    - IDE agent (Cursor, Copilot, Zencoder)
```

### Install H3A

```bash
# Navigate to your project
cd /path/to/your/project

# Initialize H3A infrastructure (one-time)
python scripts/h3a_init.py --task-brief "Add user email validation"

# Expected output:
# ✅ Created: runs/20250101-120000-abc123/
# ✅ State files initialized
# ✅ Gates ledger created
# ✅ Ready for Planner
```

**That's it!** You're ready to use H3A.

---

## Your First Task: Complete Walkthrough

Let's build a simple feature: **"Add email validation to User model"**

### Step 1: Initialize Run (30 seconds)

```bash
python scripts/h3a_init.py --task-brief "Add email validation to User model"
```

**Output:**
```
✅ Run initialized: runs/20250101-120000-abc123/
📁 Working directory: /path/to/project/runs/20250101-120000-abc123
🎯 Task brief: Add email validation to User model
📝 Next action: Invoke Planner agent

Copy this path: runs/20250101-120000-abc123
```

**Save that path!** You'll need it for all agents.

---

### Step 2: Invoke Planner Agent (5 minutes)

**Where:** Custom GPT, Claude Project, or IDE agent

**What to do:**

1. **Load Planner Prompt:**
   - Open: `prompts/planner_prompt.md`
   - Copy entire file
   - Paste into agent's system instructions (or custom instructions)

2. **Provide Task Brief:**
   ```
   You are the Planner agent in the H3A system.
   
   Working directory: runs/20250101-120000-abc123/
   
   Task brief: "Add email validation to User model"
   
   Please create:
   1. ROADMAP.md with task breakdown
   2. CURRENT_TASK.json for first task
   3. planner_report.json
   
   Begin planning.
   ```

3. **Wait for Planner to complete:**
   - Planner will analyze requirements
   - Break into small tasks (1-3 tasks)
   - Create TDD plan (RED→GREEN→REFACTOR)
   - Write Definition of Done checklist
   - Signal completion: "✅ G0 Gate Passed"

**Verification:**

```bash
cd runs/20250101-120000-abc123/

# Check files created
ls -lh state/
# Expected: ROADMAP.md, CURRENT_TASK.json, GATES_LEDGER.md, etc.

# Read the plan
cat state/ROADMAP.md
cat state/CURRENT_TASK.json
```

**Example CURRENT_TASK.json:**
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
    "red": "Write test_email_validation_valid() and test_email_validation_invalid() - expect failures",
    "green": "Implement validate_email() method in User class to make tests pass",
    "refactor": "Extract email regex pattern to constant EMAIL_PATTERN"
  },
  "definition_of_done": [
    {"item": "Tests pass", "command": "pytest tests/test_user.py -v"},
    {"item": "Coverage ≥90%", "command": "pytest --cov=src/models/user --cov-report=term-missing"},
    {"item": "Lint clean", "command": "ruff check src/models/user.py"},
    {"item": "Type hints", "command": "mypy src/models/user.py"},
    {"item": "Mutation score ≥90%", "command": "mutmut run"},
    {"item": "Security scan clean", "command": "bandit -r src/models/user.py"},
    {"item": "Docstrings added", "command": "grep -A 5 'def validate_email' src/models/user.py"},
    {"item": "No scope creep", "command": "git diff --name-only"},
    {"item": "Evidence saved", "command": "ls artifacts/executor/"},
    {"item": "Intent verified", "command": "cat executor_report.json"}
  ]
}
```

✅ **Step 2 Complete!** Planner has created task specification.

---

### Step 3: Human Bridge H1 (Planner → Executor) (2 minutes)

**Your job:** Verify G0 gate and prepare context for Executor.

```bash
# 1. Check G0 gate passed
cat state/GATES_LEDGER.md | grep "G0:"
# Expected: ✅ PASSED

# 2. Verify task is small
cat state/CURRENT_TASK.json | jq '.scope.files_to_modify | length'
# Expected: 1-3 files

# 3. Check LOC estimate
cat state/CURRENT_TASK.json | jq '.scope.estimated_loc'
# Expected: <200 lines
```

**If all checks pass:** ✅ Ready for Executor

**If task too large:** Send back to Planner: "Task too large, decompose further"

---

### Step 4: Invoke Executor Agent (10 minutes)

**Where:** Custom GPT, Claude Project, or IDE agent (can be same or different agent from Planner)

**What to do:**

1. **Load Executor Prompt:**
   - Open: `prompts/executor_prompt.md`
   - Copy entire file
   - Paste into agent's system instructions

2. **Provide Task Context:**
   ```
   You are the Executor agent in the H3A system.
   
   Working directory: runs/20250101-120000-abc123/
   
   Your task specification:
   
   <CURRENT_TASK>
   [paste entire state/CURRENT_TASK.json here]
   </CURRENT_TASK>
   
   Begin implementation following TDD cycle: RED → GREEN → REFACTOR.
   Save all evidence artifacts.
   ```

3. **Watch Executor work:**
   - Executor follows TDD cycle:
     - **RED:** Write failing tests, save `test_output_red.txt`
     - **GREEN:** Implement minimal code to pass, save `test_output_green.txt`
     - **REFACTOR:** Clean up code, verify tests still pass
   - Executor runs quality gates (lint, types, coverage, mutation, security)
   - Executor saves evidence (7+ artifacts in `artifacts/executor/`)
   - Executor signals completion: "✅ G1 Gate Passed"

**Verification:**

```bash
# Check G1 gate passed
cat state/GATES_LEDGER.md | grep "G1:"
# Expected: ✅ PASSED

# Check evidence artifacts exist
ls -lh artifacts/executor/
# Expected: 7+ .txt files

# Verify TDD chronology (RED before GREEN)
stat -f "%m %N" artifacts/executor/test_output_red.txt
stat -f "%m %N" artifacts/executor/test_output_green.txt
# Expected: RED timestamp < GREEN timestamp
```

✅ **Step 4 Complete!** Executor has implemented feature with TDD.

---

### Step 5: Human Bridge H2 (Executor → Validator) (3 minutes)

**Your job:** Verify G1 gate and prepare context for Validator.

```bash
# 1. Check G1 gate passed
cat state/GATES_LEDGER.md | grep "G1:"
# Expected: ✅ PASSED

# 2. Verify evidence artifacts exist
ls artifacts/executor/ | wc -l
# Expected: ≥7 files

# 3. Quick sanity check (don't re-run commands, Validator will)
head -20 artifacts/executor/test_output_red.txt
# Should show test failures

head -20 artifacts/executor/test_output_green.txt
# Should show test passes
```

**If all checks pass:** ✅ Ready for Validator

**If evidence missing:** Send back to Executor: "Please save missing evidence files"

---

### Step 6: Invoke Validator Agent (10 minutes)

**Where:** Custom GPT, Claude Project, or IDE agent

**What to do:**

1. **Load Validator Prompt:**
   - Open: `prompts/validator_prompt.md`
   - Copy entire file
   - Paste into agent's system instructions

2. **Provide Validation Context:**
   ```
   You are the Validator agent in the H3A system.
   
   Working directory: runs/20250101-120000-abc123/
   
   Executor has completed implementation. Your job: verify ALL claims independently.
   DO NOT TRUST executor's outputs - re-run all commands.
   
   <EXECUTOR_REPORT>
   [paste entire executor_report.json here]
   </EXECUTOR_REPORT>
   
   <ORIGINAL_TASK>
   [paste state/CURRENT_TASK.json here]
   </ORIGINAL_TASK>
   
   Begin 10-point verification.
   ```

3. **Watch Validator work:**
   - Validator re-runs ALL commands independently
   - Validator performs 10-point checklist:
     1. TDD Compliance
     2. Test Quality
     3. Coverage
     4. Mutation Score
     5. Security
     6. Code Quality
     7. Accessibility (if UI)
     8. DoD Completeness
     9. Intent Alignment
     10. Command Verification
   - Validator detects discrepancies (if Executor claims don't match reality)
   - Validator makes G2 decision: PASS / FAIL / ESCALATE
   - Validator signals completion: "✅ G2 Gate Decision: PASS" (or other outcome)

**Verification:**

```bash
# Check G2 gate decision
cat state/GATES_LEDGER.md | grep "G2:"
# Expected: ✅ PASSED (best case)

# Read validation results
cat validator_report.json | jq '.validation_results'

# Check if all 10 checks passed
cat validator_report.json | jq '.checks_passed'
# Expected: 10
```

**Possible Outcomes:**

- **✅ PASS:** All 10 checks passed → Proceed to Step 7 (Human G3 gate)
- **⚠️ NEEDS_REMEDIATION:** Minor issues found → Send back to Executor with fix list
- **❌ FAIL:** Major issues → Send back to Executor or Planner
- **🚨 ESCALATE:** Discrepancy detected → Human investigation required

✅ **Step 6 Complete!** Validator has verified quality.

---

### Step 7: Human Bridge H3 (G3 Gate Decision) (10 minutes)

**Your job:** Final production approval using 8-point human verification checklist.

**Use the checklist:**

See [Human_Verification_Checklist.md](./Human_Verification_Checklist.md) for complete guide.

**Quick version:**

```bash
# 1. Requirements Met
cat state/CURRENT_TASK.json | jq '.goal'
# Compare to what was implemented

# 2. Tests Pass
pytest tests/test_user.py -v
# ✅ All pass?

# 3. No Broken Features
pytest tests/ -v
# ✅ No regressions?

# 4. Code Readable
git diff main...HEAD src/models/user.py
# ✅ Can you understand it?

# 5. Security Check
cat artifacts/validator/check_05_security.txt
# ✅ 0 critical/high issues?

# 6. Documentation Updated
git diff main...HEAD src/models/user.py | grep -A 5 "def validate_email"
# ✅ Docstring present?

# 7. Evidence Complete
cat state/EVIDENCE_LOG.md | grep "T001"
# ✅ All artifacts listed with hashes?

# 8. Intent Alignment
cat state/CURRENT_TASK.json | jq '.scope.files_to_modify'
git diff --name-only
# ✅ Only specified files changed?
```

**Make Decision:**

- **8/8 passed** → ✅ APPROVE
- **6-7/8 passed** → ⚠️ CONDITIONAL APPROVAL (minor fixes)
- **<6/8 passed OR ANY security issue** → ❌ REJECT

**Document Decision:**

```bash
# If APPROVED:
echo "## Gate: G3 (Production-Ready)
- **Status:** ✅ APPROVED
- **Timestamp:** $(date -u +"%Y-%m-%dT%H:%M:%SZ")
- **Approver:** [Your Name]
- **Checklist:** 8/8 passed
- **Next Action:** Deploy to production
" >> state/GATES_LEDGER.md

# Create approval report
cat > g3_approval_report.json << EOF
{
  "gate": "G3",
  "decision": "APPROVED",
  "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "approver": "[Your Name]",
  "checklist_passed": 8,
  "deployment_approved": true
}
EOF
```

✅ **Step 7 Complete!** Task approved for production.

---

### Step 8: Deploy & Cleanup (5 minutes)

```bash
# 1. Merge code
git add .
git commit -m "feat: Add email validation to User model (Task T001)"
git push origin feature/email-validation

# Create PR, get approval, merge to main

# 2. Mark task complete in ROADMAP
sed -i '' 's/- \[ \] T001/- [x] T001 (Completed 2025-01-01)/' state/ROADMAP.md

# 3. Check if more tasks exist
grep "- \[ \]" state/ROADMAP.md

# If more tasks: Return to Step 2 (Planner loads next task)
# If no tasks: Project complete! 🎉

# 4. Archive run (optional)
tar -czf runs/20250101-120000-abc123.tar.gz runs/20250101-120000-abc123/
```

---

## 🎉 Congratulations!

**You've completed your first H3A task!**

**What you accomplished:**
- ✅ Planned with TDD approach (Planner)
- ✅ Implemented with RED→GREEN→REFACTOR (Executor)
- ✅ Verified with 10-point checklist (Validator)
- ✅ Human-approved for production (G3 gate)
- ✅ Complete audit trail with evidence

**Time Investment:**
- Setup: 5 minutes (one-time)
- Planner: 5 minutes
- Executor: 10 minutes
- Validator: 10 minutes
- Human verification: 10 minutes
- **Total:** ~40 minutes for production-grade feature

---

## Real-World Example

### Scenario: Build a REST API Endpoint

**Requirement:** "Add GET /api/users/:id endpoint that returns user profile"

---

### Full Workflow

#### **Initialize:**

```bash
python scripts/h3a_init.py --task-brief "Add GET /api/users/:id endpoint"
```

---

#### **Planner Output (G0):**

**ROADMAP.md:**
```markdown
# Roadmap: Add User Profile Endpoint

## Tasks
- [ ] T001: Add GET /api/users/:id route handler with error handling
- [ ] T002: Add integration test for /api/users/:id endpoint
- [ ] T003: Update API documentation with new endpoint

Total: 3 tasks, ~4 hours estimated
```

**CURRENT_TASK.json (T001):**
```json
{
  "task_id": "T001",
  "goal": "Add GET /api/users/:id route handler with error handling",
  "scope": {
    "files_to_modify": [
      "src/api/routes/users.py",
      "tests/test_routes_users.py"
    ],
    "estimated_loc": 180,
    "touch_only_listed": true
  },
  "tdd_plan": {
    "red": "Write test_get_user_by_id_success() expecting 200, test_get_user_by_id_not_found() expecting 404",
    "green": "Implement get_user_by_id() route handler in users.py",
    "refactor": "Extract error response formatting to helper function"
  },
  "definition_of_done": [
    {"item": "Tests pass", "command": "pytest tests/test_routes_users.py -v"},
    {"item": "Coverage ≥90%", "command": "pytest --cov=src/api/routes/users --cov-report=term"},
    {"item": "Lint clean", "command": "ruff check src/api/routes/users.py"},
    {"item": "Type hints", "command": "mypy src/api/routes/users.py"},
    {"item": "Security scan", "command": "bandit -r src/api/"},
    {"item": "Integration test", "command": "pytest tests/integration/test_api.py -v"},
    {"item": "API contract", "command": "openapi-spec-validator openapi.yaml"},
    {"item": "Performance", "command": "ab -n 100 -c 10 http://localhost:8000/api/users/1"},
    {"item": "Evidence saved", "command": "ls artifacts/executor/"},
    {"item": "Docs updated", "command": "grep -A 10 'GET /api/users/:id' docs/API.md"}
  ]
}
```

---

#### **Executor Implementation (G1):**

**RED Phase:**

```python
# tests/test_routes_users.py
def test_get_user_by_id_success():
    """Test successful user retrieval by ID."""
    response = client.get("/api/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert "email" in response.json()

def test_get_user_by_id_not_found():
    """Test user not found returns 404."""
    response = client.get("/api/users/99999")
    assert response.status_code == 404
    assert "error" in response.json()
```

**Run tests:** `pytest tests/test_routes_users.py -v`

**Output:** `test_output_red.txt` shows 2 failures ✅ (RED phase proven)

---

**GREEN Phase:**

```python
# src/api/routes/users.py
from fastapi import APIRouter, HTTPException
from src.models.user import User
from src.database import get_db

router = APIRouter()

@router.get("/api/users/{user_id}")
async def get_user_by_id(user_id: int):
    """
    Get user profile by ID.
    
    Args:
        user_id: User ID to retrieve
        
    Returns:
        User profile dict with id, email, name
        
    Raises:
        HTTPException: 404 if user not found
    """
    db = get_db()
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "created_at": user.created_at.isoformat()
    }
```

**Run tests:** `pytest tests/test_routes_users.py -v`

**Output:** `test_output_green.txt` shows 2 passes ✅ (GREEN phase proven)

---

**REFACTOR Phase:**

```python
# src/api/routes/users.py (refactored)
from fastapi import APIRouter, HTTPException
from src.models.user import User
from src.database import get_db
from src.api.responses import error_response, user_response

router = APIRouter()

@router.get("/api/users/{user_id}")
async def get_user_by_id(user_id: int):
    """Get user profile by ID."""
    db = get_db()
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        return error_response(404, "User not found")
    
    return user_response(user)

# src/api/responses.py (new helper)
def error_response(status_code: int, message: str):
    """Standard error response format."""
    raise HTTPException(status_code=status_code, detail=message)

def user_response(user):
    """Standard user profile response format."""
    return {
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "created_at": user.created_at.isoformat()
    }
```

**Run tests again:** All still pass ✅ (refactor successful)

---

**Evidence Artifacts:**

```bash
artifacts/executor/
├── test_output_red.txt          # 2 failures (RED proven)
├── test_output_green.txt        # 2 passes (GREEN proven)
├── test_output_full_suite.txt   # All 45 tests pass (no regressions)
├── lint_output.txt              # ruff: 0 issues
├── mypy_output.txt              # mypy: Success, no issues
├── coverage_output.txt          # 94.2% (+3.1% delta)
├── mutation_output.txt          # 92.5% mutation score
└── security_output.txt          # bandit: 0 high/critical issues
```

---

#### **Validator Verification (G2):**

**10-Point Checklist Results:**

```json
{
  "gate": "G2",
  "decision": "PASS",
  "checks_passed": 10,
  "checks_failed": 0,
  "validation_results": {
    "check_01_tdd_compliance": {
      "status": "✅ PASS",
      "evidence": "RED phase (13:45:12) before GREEN phase (13:52:30)"
    },
    "check_02_test_quality": {
      "status": "✅ PASS",
      "evidence": "Descriptive names, isolated, good assertions"
    },
    "check_03_coverage": {
      "status": "✅ PASS",
      "evidence": "94.2% total, 100% on changed files"
    },
    "check_04_mutation_score": {
      "status": "✅ PASS",
      "evidence": "92.5% score (≥90% threshold)"
    },
    "check_05_security": {
      "status": "✅ PASS",
      "evidence": "0 critical, 0 high issues"
    },
    "check_06_code_quality": {
      "status": "✅ PASS",
      "evidence": "Lint clean, type hints present, complexity low"
    },
    "check_07_accessibility": {
      "status": "N/A",
      "evidence": "No UI changes (API endpoint)"
    },
    "check_08_dod_completeness": {
      "status": "✅ PASS",
      "evidence": "All 10 DoD items verified"
    },
    "check_09_intent_alignment": {
      "status": "✅ PASS",
      "evidence": "Implemented exactly what was specified"
    },
    "check_10_command_verification": {
      "status": "✅ PASS",
      "evidence": "All DoD commands re-run successfully"
    }
  },
  "discrepancies": [],
  "approval_for_next_task": true
}
```

**Validator Decision:** ✅ PASS → Ready for G3 gate

---

#### **Human Verification (G3):**

**8-Point Checklist:**

1. ✅ **Requirements Met:** GET /api/users/:id endpoint works, returns user profile
2. ✅ **Tests Pass:** Re-ran `pytest`, all 47 tests pass
3. ✅ **No Broken Features:** Smoke test passed, other endpoints still work
4. ✅ **Code Readable:** Clean, well-structured, helper functions extracted
5. ✅ **Security Check:** No SQL injection (using ORM), no secrets in code
6. ✅ **Documentation Updated:** Docstrings present, API docs updated
7. ✅ **Evidence Complete:** All 7 executor + 10 validator artifacts present
8. ✅ **Intent Alignment:** Only specified files changed, scope respected

**Decision:** ✅ **APPROVED** (8/8 passed)

---

#### **Deployment:**

```bash
# Commit and push
git add .
git commit -m "feat: Add GET /api/users/:id endpoint (T001)"
git push origin feature/user-endpoint

# Create PR, get approval, merge

# Mark complete
sed -i '' 's/- \[ \] T001/- [x] T001/' state/ROADMAP.md

# Move to next task
# Return to Planner → Load T002 (integration test)
```

---

### Result

**Task T001 Complete in ~45 minutes:**
- ✅ TDD-driven implementation (RED→GREEN→REFACTOR)
- ✅ 94.2% test coverage
- ✅ 92.5% mutation score
- ✅ 0 security issues
- ✅ Complete audit trail
- ✅ Production-ready code

**Next:** Repeat workflow for T002 (integration test) and T003 (documentation).

---

## Common Workflows

### Workflow 1: Simple Feature (1 Task)

**Example:** "Fix typo in error message"

```
Initialize → Planner (1 task) → Executor → Validator → Human → Deploy
Time: ~30 minutes
```

---

### Workflow 2: Medium Feature (2-4 Tasks)

**Example:** "Add password reset functionality"

```
Initialize → Planner (3 tasks) → Loop:
  Task 1: Add reset token model
    → Executor → Validator → Human → Continue
  Task 2: Add /api/password-reset endpoint
    → Executor → Validator → Human → Continue
  Task 3: Add reset email template
    → Executor → Validator → Human → Deploy
Time: ~2-3 hours
```

---

### Workflow 3: Large Feature (5+ Tasks)

**Example:** "Add OAuth2 authentication"

```
Initialize → Planner (8 tasks) → Loop for each task:
  → Executor → Validator → Human → Continue/Deploy
Time: ~6-8 hours (spread across days)
```

**Tip:** Review ROADMAP after 3-4 tasks, adjust if priorities change.

---

### Workflow 4: Bug Fix

**Example:** "Fix race condition in user login"

```
Initialize → Planner → Executor (with repro test) → Validator → Human → Deploy
Time: ~45 minutes

Key: Executor must prove bug fixed (test fails before fix, passes after)
```

---

### Workflow 5: Refactoring

**Example:** "Extract database logic to repository pattern"

```
Initialize → Planner (4 tasks, each file group) → Loop:
  → Executor (refactor + verify tests still pass) → Validator → Human → Continue
Time: ~3-4 hours

Key: No behavior change, tests must pass throughout
```

---

## Troubleshooting Quick Fixes

### Issue: "Agent isn't following instructions"

**Symptoms:**
- Executor skips TDD cycle
- Planner creates 1 huge task instead of breaking it down
- Validator trusts Executor without re-running commands

**Fix:**

1. **Reload prompts:** Copy prompt file again, paste fresh (agents can drift)
2. **Be explicit:** Add to your message:
   ```
   CRITICAL: You MUST follow RED→GREEN→REFACTOR cycle.
   Save test_output_red.txt BEFORE test_output_green.txt.
   No exceptions.
   ```
3. **Check agent type:** Some agents (GPT-3.5, small models) struggle with complex prompts. Use GPT-4+ or Claude Sonnet+

---

### Issue: "State files not updating"

**Symptoms:**
- GATES_LEDGER.md missing entries
- EVIDENCE_LOG.md not listing artifacts

**Fix:**

```bash
# Check if agent has file write access
ls -la state/
# Permissions should allow writing

# If using IDE agent, check workspace settings
# Ensure agent can modify files in runs/ directory

# Manual fix (if needed):
echo "## Gate: G1 (Implementation)
- **Status:** ✅ PASSED
- **Agent:** Executor
" >> state/GATES_LEDGER.md
```

---

### Issue: "Tests fail for me but passed for Executor"

**Symptoms:**
- Executor claims "All tests pass"
- You run tests, they fail

**Fix:**

```bash
# 1. Check environment
python --version  # Match Executor's version
pip list          # Match dependencies

# 2. Fresh environment
python -m venv venv_fresh
source venv_fresh/bin/activate
pip install -r requirements.txt
pytest tests/

# 3. If still fails: Executor was wrong
# Send back with evidence:
"Your tests are failing when I run them:
[paste error output]
Please fix and re-submit."
```

---

### Issue: "Validator too strict / too lenient"

**Too Strict:**
```bash
# Validator fails on minor issue (e.g., coverage 89.9% vs 90% threshold)
# Solution: Override with human judgment (document reason)
echo "Human override: 89.9% coverage acceptable, threshold met in spirit" >> state/GATES_LEDGER.md
```

**Too Lenient:**
```bash
# Validator passes but you found issue
# Solution: Trust your judgment, reject at G3
echo "G3: ❌ REJECTED - Found security issue Validator missed" >> state/GATES_LEDGER.md
```

---

### Issue: "Task taking too long"

**Symptoms:**
- Executor running for >20 minutes
- Validator stuck on mutation testing

**Fix:**

```bash
# 1. Check what's running
ps aux | grep python

# 2. If stuck: Kill and restart
pkill -f pytest  # Or whatever is hung

# 3. Invoke agent again with:
"Continue from where you left off. If tests are slow, consider:
- Running subset first
- Skipping mutation tests temporarily
- Breaking into smaller scope"
```

---

## Next Steps

### You've Completed the Quick Start! 🎉

**What you learned:**
- ✅ How to initialize H3A runs
- ✅ How to invoke all 3 agents (Planner, Executor, Validator)
- ✅ How to perform human bridges (H1, H2, H3)
- ✅ How to make G3 production decisions
- ✅ Real-world workflows

---

### Deepen Your Knowledge

**Essential Reading:**

1. **[Human_Bridge_Protocol.md](./Human_Bridge_Protocol.md)** - Complete guide to bridging agents (H1, H2, H3)
2. **[Human_Verification_Checklist.md](./Human_Verification_Checklist.md)** - 8-point checklist for G3 gate decisions
3. **[Gate_Framework.md](./Gate_Framework.md)** - Deep dive into G0, G1, G2, G3 gates
4. **[State_Specification.md](./State_Specification.md)** - State file formats and protocols

**Agent Prompts:**

5. **[prompts/planner_prompt.md](../../prompts/planner_prompt.md)** - Complete Planner system prompt
6. **[prompts/executor_prompt.md](../../prompts/executor_prompt.md)** - Complete Executor system prompt
7. **[prompts/validator_prompt.md](../../prompts/validator_prompt.md)** - Complete Validator system prompt

---

### Advanced Topics

**Custom Workflows:**

- **Multi-Agent Parallelization:** Run multiple Executors in parallel for independent tasks
- **Custom Quality Gates:** Add project-specific checks (e.g., performance benchmarks, visual regression tests)
- **Integration with CI/CD:** Automate H3A workflow in GitHub Actions / GitLab CI

**Enterprise Features:**

- **Compliance Audits:** Use EVIDENCE_LOG.md for SOC 2, ISO 42001 audits
- **Multi-Team Coordination:** Share ROADMAP.md across teams for dependencies
- **Cost Tracking:** Log AI agent API costs per task in custom field

---

### Get Help

**Resources:**

- **Documentation:** `docs/H3A_System/` folder
- **Examples:** `runs/` folder (see past runs)
- **Scripts:** `scripts/h3a_init.py` (read source for insights)

**Common Questions:**

**Q: Can I use H3A with non-Python projects?**  
A: Yes! Update DoD commands for your language (e.g., `npm test`, `cargo test`). Core workflow is language-agnostic.

**Q: Do I need all 3 agents or can I skip one?**  
A: Recommended to use all 3 for production code. For experiments, you can skip Planner (manual task creation) but NEVER skip Validator (quality enforcement).

**Q: Can I use same AI agent for all roles?**  
A: Yes! Just reload the appropriate prompt (planner_prompt.md, executor_prompt.md, validator_prompt.md) when switching roles.

**Q: How do I handle tasks that require human research?**  
A: Planner can include "Human research required" in task, with note: "Human must provide [X] before Executor can proceed". Pause workflow, gather info, resume.

**Q: What if my team already has a workflow?**  
A: H3A can coexist! Use for new features, migrate gradually. State files (GATES_LEDGER, EVIDENCE_LOG) provide value even without agents.

---

## Summary

### The H3A Workflow in One Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     H3A WORKFLOW LOOP                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📝 INIT: python scripts/h3a_init.py --task-brief "..."    │
│     │                                                       │
│     ↓                                                       │
│  🧠 PLANNER (G0):                                           │
│     - Break into small tasks                               │
│     - Create TDD plan                                      │
│     - Definition of Done                                   │
│     - Output: ROADMAP.md, CURRENT_TASK.json               │
│     │                                                       │
│     ↓ H1 Bridge (Human: 2 min)                            │
│     │                                                       │
│  ⚙️  EXECUTOR (G1):                                         │
│     - RED: Write failing tests                             │
│     - GREEN: Implement to pass                             │
│     - REFACTOR: Clean up                                   │
│     - Output: Code + 7 evidence artifacts                  │
│     │                                                       │
│     ↓ H2 Bridge (Human: 3 min)                            │
│     │                                                       │
│  ✅ VALIDATOR (G2):                                         │
│     - Re-run all commands (zero-trust)                     │
│     - 10-point checklist                                   │
│     - Output: PASS / FAIL / ESCALATE                       │
│     │                                                       │
│     ↓ H3 Bridge (Human: 10 min)                           │
│     │                                                       │
│  👤 HUMAN (G3):                                             │
│     - 8-point verification                                 │
│     - Decision: APPROVE / CONDITIONAL / REJECT             │
│     - Output: g3_approval_report.json                      │
│     │                                                       │
│     ↓                                                       │
│  🚀 DEPLOY: Merge to main, deploy to production           │
│     │                                                       │
│     └─────→ More tasks? → Return to Planner (load next)   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### Key Principles (Remember These!)

1. **Small Tasks Win** - Break work into <200 LOC chunks
2. **TDD is Mandatory** - RED→GREEN→REFACTOR, no exceptions
3. **Evidence Required** - No artifact = gate not passed
4. **Zero-Trust Validation** - Validator re-runs everything
5. **Human Final Say** - You approve production (G3 gate)
6. **Iteration Limits** - Max 2 attempts per gate, then escalate
7. **State is Truth** - Agents have no memory, state files are SSOT

---

### Time Investment (Typical Task)

| Phase | Agent | Time | Human Time |
|-------|-------|------|------------|
| G0: Planning | Planner | 5 min | 2 min (H1 bridge) |
| G1: Implementation | Executor | 10 min | 3 min (H2 bridge) |
| G2: Validation | Validator | 10 min | 10 min (H3 bridge) |
| G3: Approval | Human | - | 10 min (verification) |
| **Total** | | **~25 min** | **~25 min** |

**Total per task:** ~50 minutes for production-grade, fully-tested, audited code.

---

**🚀 You're ready to use H3A! Start with a small task and experience the workflow. Good luck!**

For detailed guidance, see:
- [Human_Bridge_Protocol.md](./Human_Bridge_Protocol.md) - Step-by-step bridging
- [Human_Verification_Checklist.md](./Human_Verification_Checklist.md) - G3 gate checklist

---

## Version History

- **v1.0.0** (2025-01-01): Initial production release

---

**Happy building with H3A! 🎉**