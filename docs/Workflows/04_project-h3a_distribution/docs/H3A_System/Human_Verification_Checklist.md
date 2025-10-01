# Human Verification Checklist (H3A System)

**Version:** 1.0.0  
**Last Updated:** 2025-01-01  
**Status:** Production-Ready ✅

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [When to Use This Checklist](#when-to-use-this-checklist)
3. [Prerequisites](#prerequisites)
4. [The 8-Point Verification Checklist](#the-8-point-verification-checklist)
5. [Quick Reference Card](#quick-reference-card)
6. [Decision Matrix](#decision-matrix)
7. [Common Issues & Solutions](#common-issues--solutions)
8. [Appendix: Verification Commands](#appendix-verification-commands)

---

## Overview

### Purpose

This checklist is your **final quality gate (G3)** before code reaches production. While the Validator agent has already performed technical verification (10-point checklist at G2), **you provide the human judgment** that AI cannot:

- ✅ **Intent alignment** - Does this solve the actual business problem?
- ✅ **User impact** - Will this improve or harm user experience?
- ✅ **Risk assessment** - What could go wrong in production?
- ✅ **Gut check** - Does this "feel right"?

**You are the last line of defense.** Trust your instincts.

---

### What You're NOT Doing

This is not a deep code review. You're doing a **spot check** to verify:

- ❌ **Not:** Reading every line of code
- ❌ **Not:** Re-running all quality gates (Validator did that)
- ❌ **Not:** Writing tests yourself
- ❌ **Not:** Fixing bugs

**You're verifying the Validator's work** and making a production deployment decision.

---

### Time Investment

**Target:** 10-15 minutes per task

| Activity | Time |
|----------|------|
| Read Validator report | 2 min |
| Run spot checks | 5 min |
| Review changed code | 3-5 min |
| Make decision + document | 2-3 min |

**If taking >20 minutes:** Task is too complex, send back to Planner for decomposition.

---

## When to Use This Checklist

**Trigger:** Validator completes G2 gate with "PASS" decision and writes `SESSION_HANDOFF.json` with `"handoff_to": "human"`.

**You verify:**
```bash
cat state/GATES_LEDGER.md | grep "G2:"
```

**Expected:**
```markdown
## Gate: G2 (Validation)
- **Status:** ✅ PASSED
- **Checklist:** 10/10 checks passed
- **Decision:** Approved for G3 gate
```

**If G2 ≠ PASSED:** Stop! Don't proceed to G3 until G2 issues resolved.

---

## Prerequisites

Before starting checklist, gather these resources:

### 1. **Context Files**

```bash
# Navigate to run directory
cd runs/<run-id>/

# Key files to review
cat validator_report.json     # Validator's findings
cat state/CURRENT_TASK.json   # Original requirements
cat executor_report.json      # Implementation details
```

### 2. **Changed Files**

```bash
# See what code was modified
git diff main...HEAD

# Or view specific files
git diff main...HEAD src/models/user.py
```

### 3. **Test Environment**

```bash
# Ensure you're in correct environment
python --version  # Should match project requirements
pip list | grep pytest

# Fresh shell (no cached modules)
```

### 4. **Validator Evidence**

```bash
# Check Validator's verification artifacts
ls -lh artifacts/validator/

# Key artifacts:
# - check_01_tdd_compliance.txt
# - check_02_test_quality.txt
# - check_03_coverage.txt
# - ... (10 total)
```

---

## The 8-Point Verification Checklist

### ✅ Point 1: Requirements Met

**Question:** Does the implementation solve the original problem?

**How to Verify:**

1. **Read original requirement:**
   ```bash
   cat state/CURRENT_TASK.json | jq '.goal'
   ```
   
   Example: `"Add email validation to User model"`

2. **Check implementation:**
   ```bash
   # Find the relevant code
   grep -n "email" src/models/user.py
   
   # Or view entire file
   cat src/models/user.py
   ```

3. **Spot check:**
   - Is there a `validate_email()` function or similar?
   - Does it check for basic email format (`@`, domain)?
   - Does it return clear success/failure indication?

**Pass Criteria:**
- ✅ Core functionality present
- ✅ Matches what was requested in `CURRENT_TASK.json`
- ✅ No obvious omissions

**Fail Criteria:**
- ❌ Feature not implemented
- ❌ Completely wrong approach (e.g., asked for validation, got formatting)
- ❌ Partial implementation (validates format but not domain)

**Time:** 2 minutes

---

### ✅ Point 2: Tests Pass

**Question:** Do all tests pass when I run them myself?

**How to Verify:**

```bash
# Run full test suite
pytest tests/ -v

# Expected output:
# ===== X passed in Y.YYs =====
# (No failures, no errors)
```

**Pass Criteria:**
- ✅ All tests pass (0 failures)
- ✅ No errors or crashes
- ✅ No warnings about deprecated APIs

**Fail Criteria:**
- ❌ Any test fails
- ❌ Tests crash with exception
- ❌ Tests hang (timeout after 60s)

**Troubleshooting:**

| Issue | Likely Cause | Fix |
|-------|--------------|-----|
| `ModuleNotFoundError` | Missing dependency | `pip install -r requirements.txt` |
| Tests fail but Validator said pass | Environment difference | Check Python version, dependencies |
| Tests hang | Infinite loop or network call | Kill tests, investigate hanging test |

**Time:** 2 minutes

---

### ✅ Point 3: No Broken Features

**Question:** Did this change break anything that previously worked?

**How to Verify:**

**Option A: Quick Smoke Test (Preferred)**

If your project has a smoke test:
```bash
# Run smoke test suite (fast, critical paths only)
pytest tests/smoke/ -v

# Or run specific integration test
pytest tests/test_integration.py -v
```

**Option B: Manual Spot Check**

If no smoke tests, manually test key workflows:

Example (for web app):
```bash
# Start app
python -m src.app

# Test in browser/curl:
# - Homepage loads
# - Login works
# - Critical feature works
```

**Pass Criteria:**
- ✅ Core functionality still works
- ✅ No obvious regressions
- ✅ App still starts/runs

**Fail Criteria:**
- ❌ Previously working feature now broken
- ❌ App won't start
- ❌ Critical path fails

**Time:** 3 minutes

---

### ✅ Point 4: Code Readable

**Question:** Can I understand what this code does without excessive effort?

**How to Verify:**

```bash
# View changed files
git diff main...HEAD src/

# Focus on new/modified functions
```

**Check for:**

1. **Clear function names**
   ```python
   # ✅ Good
   def validate_email_format(email: str) -> bool:
   
   # ❌ Bad
   def check(e):
   ```

2. **Descriptive variable names**
   ```python
   # ✅ Good
   email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
   
   # ❌ Bad
   p = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
   ```

3. **Reasonable complexity**
   ```python
   # ✅ Good (simple, linear logic)
   def validate_email(email: str) -> bool:
       if not email:
           return False
       if "@" not in email:
           return False
       return re.match(EMAIL_PATTERN, email) is not None
   
   # ❌ Bad (nested, hard to follow)
   def validate_email(email: str) -> bool:
       if email:
           if "@" in email:
               if "." in email.split("@")[1]:
                   if len(email) > 5:
                       if not email.startswith("."):
                           return True
       return False
   ```

4. **Comments where needed**
   ```python
   # ✅ Good (complex regex explained)
   # Matches: user@domain.com, first.last@company.co.uk
   # Does not match: @domain, user@, user@domain
   EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
   ```

**Pass Criteria:**
- ✅ Function names describe purpose
- ✅ Can follow logic in 30-60 seconds
- ✅ No excessive nesting (< 4 levels)
- ✅ Complex parts have comments

**Fail Criteria:**
- ❌ Cannot understand what code does
- ❌ Variables named `x`, `data`, `tmp`
- ❌ 100+ line function with no structure
- ❌ No comments on complex logic

**Time:** 3 minutes

---

### ✅ Point 5: Security Check

**Question:** Is there any obvious security risk?

**How to Verify:**

**Check 1: Validator's Security Scan**
```bash
cat artifacts/validator/check_05_security.txt

# Expected: 0 critical, 0 high issues
```

**Check 2: Manual Code Review**

Look for common security issues:

| Risk | Example | Fix |
|------|---------|-----|
| **Secrets in code** | `API_KEY = "sk-abc123"` | Use environment variables |
| **SQL injection** | `f"SELECT * FROM users WHERE email='{email}'"` | Use parameterized queries |
| **Command injection** | `os.system(f"ping {user_input}")` | Validate input, use safe APIs |
| **Path traversal** | `open(f"files/{user_file}")` | Validate path, use safe join |
| **Missing input validation** | `age = int(request.args['age'])` | Validate, handle exceptions |

**Check 3: Look at Test Coverage**

```bash
cat artifacts/validator/check_03_coverage.txt | grep -A 5 "missing"

# Are security-critical paths covered?
```

**Pass Criteria:**
- ✅ Validator security scan clean (0 critical/high)
- ✅ No secrets in code
- ✅ User input validated before use
- ✅ No dangerous patterns (SQL injection, command injection)

**Fail Criteria:**
- ❌ ANY critical or high security issue
- ❌ Secrets, API keys, passwords in code
- ❌ User input used directly in SQL, shell commands, file paths
- ❌ Missing validation on untrusted input

**If ANY security issue found:** ❌ REJECT immediately, send back to Executor

**Time:** 2 minutes

---

### ✅ Point 6: Documentation Updated

**Question:** If someone reads the docs, will they understand this feature?

**How to Verify:**

**Check 1: Docstrings**

```bash
# View new functions
git diff main...HEAD src/ | grep -A 10 "def "
```

Example:
```python
# ✅ Good
def validate_email(email: str) -> bool:
    """
    Validate email format according to RFC 5322 (simplified).
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid format, False otherwise
        
    Example:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid")
        False
    """
    ...

# ❌ Bad (no docstring)
def validate_email(email: str) -> bool:
    ...
```

**Check 2: README/User Docs**

If this is a user-facing feature:
```bash
# Check if README mentions it
grep -i "email" README.md

# Check if CHANGELOG updated
cat CHANGELOG.md | head -20
```

**Check 3: Definition of Done**

```bash
cat state/CURRENT_TASK.json | jq '.definition_of_done[] | select(.item | contains("documentation"))'
```

**Pass Criteria:**
- ✅ New functions have docstrings
- ✅ Public API documented
- ✅ README updated if user-facing
- ✅ CHANGELOG has entry (if project uses it)

**Conditional Pass:**
- ⚠️ Internal functions without docstrings (OK if names are self-documenting)
- ⚠️ No README update for internal refactoring (OK if no user impact)

**Fail Criteria:**
- ❌ Public API has no docstrings
- ❌ User-facing feature not mentioned in README
- ❌ Complex logic without any explanation

**Time:** 2 minutes

---

### ✅ Point 7: Evidence Complete

**Question:** Can I audit this task in 6 months if there's an issue?

**How to Verify:**

**Check 1: Evidence Log**

```bash
cat state/EVIDENCE_LOG.md | grep "T001"

# Expected: All artifacts listed with SHA-256 hashes
```

Example:
```markdown
## Task: T001 - Add email validation

### Executor Evidence
- `artifacts/executor/test_output_red.txt` → `sha256:a3f4b2c...`
- `artifacts/executor/test_output_green.txt` → `sha256:e8d7a1f...`
- `artifacts/executor/test_output_full_suite.txt` → `sha256:c2b5e9d...`
... (7 total)

### Validator Evidence
- `artifacts/validator/check_01_tdd_compliance.txt` → `sha256:f1e3d8a...`
- `artifacts/validator/check_02_test_quality.txt` → `sha256:b9c4e2f...`
... (10+ total)
```

**Check 2: Artifacts Exist**

```bash
# Verify files actually exist and match hashes
for file in artifacts/executor/*.txt; do
    echo "Checking $file"
    ls -lh "$file"
done
```

**Check 3: Gates Ledger Complete**

```bash
tail -50 state/GATES_LEDGER.md

# Should show:
# - G0: PASSED (Planner)
# - G1: PASSED (Executor)
# - G2: PASSED (Validator)
# - G3: PENDING (awaiting your decision)
```

**Pass Criteria:**
- ✅ All evidence files listed in EVIDENCE_LOG.md
- ✅ All files exist and have hashes
- ✅ GATES_LEDGER shows full progression (G0 → G1 → G2)
- ✅ No gaps in audit trail

**Fail Criteria:**
- ❌ Evidence files missing
- ❌ EVIDENCE_LOG.md incomplete
- ❌ Gates skipped (e.g., G0 → G2 without G1)

**Time:** 2 minutes

---

### ✅ Point 8: Intent Alignment

**Question:** Is this what we actually needed, or did scope creep occur?

**How to Verify:**

**Check 1: Compare Goal vs Implementation**

```bash
# Original goal
cat state/CURRENT_TASK.json | jq '.goal'
# "Add email validation to User model"

# What was actually done
cat executor_report.json | jq '.summary'
# Check: Did they ONLY add email validation, or also add password validation, username validation, etc.?
```

**Check 2: Files Modified**

```bash
# What files were supposed to change
cat state/CURRENT_TASK.json | jq '.scope.files_to_modify'
# ["src/models/user.py", "tests/test_user.py"]

# What files actually changed
git diff main...HEAD --name-only
# Should match exactly (or be subset)
```

**Check 3: LOC Estimate**

```bash
# Estimated lines of code
cat state/CURRENT_TASK.json | jq '.scope.estimated_loc'
# 120

# Actual lines changed
git diff main...HEAD --stat
# Should be close (within 50% margin)
```

**Scope Creep Examples:**

| Requested | What Was Delivered | Scope Creep? |
|-----------|-------------------|--------------|
| Add email validation | Email validation only | ✅ Perfect |
| Add email validation | Email validation + password validation + username validation | ❌ YES (did too much) |
| Add email validation | Email validation + fixed existing bug | ⚠️ MAYBE (ask: was bug related?) |
| Add email validation | Refactored entire User model | ❌ YES (changed too much) |

**Pass Criteria:**
- ✅ Implementation matches goal
- ✅ Files changed match scope
- ✅ LOC within reasonable range (±50% of estimate)
- ✅ No unexpected features added

**Conditional Pass:**
- ⚠️ Small related fix (e.g., fixed typo in adjacent line) - OK
- ⚠️ Slightly over LOC estimate but justified - OK

**Fail Criteria:**
- ❌ Extra features added without approval
- ❌ Files modified outside scope
- ❌ 3x+ LOC estimate (task should have been decomposed)

**Time:** 2 minutes

---

## Quick Reference Card

### Print & Pin This to Your Wall 📌

```
┌─────────────────────────────────────────────────────────────────┐
│         H3A HUMAN VERIFICATION CHECKLIST (G3 Gate)              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ✅ 1. REQUIREMENTS MET                                         │
│     Does code solve original problem?                           │
│     → Check: state/CURRENT_TASK.json vs implementation          │
│                                                                 │
│  ✅ 2. TESTS PASS                                               │
│     Do tests pass when I run them?                              │
│     → Run: pytest tests/ -v                                     │
│                                                                 │
│  ✅ 3. NO BROKEN FEATURES                                       │
│     Did this break anything?                                    │
│     → Run: pytest tests/smoke/ OR manual smoke test             │
│                                                                 │
│  ✅ 4. CODE READABLE                                            │
│     Can I understand what this does?                            │
│     → Check: git diff main...HEAD src/                          │
│                                                                 │
│  ✅ 5. SECURITY CHECK                                           │
│     Any obvious security risks?                                 │
│     → Check: artifacts/validator/check_05_security.txt          │
│     → Look for: secrets, SQL injection, missing validation      │
│                                                                 │
│  ✅ 6. DOCUMENTATION UPDATED                                    │
│     Are new functions documented?                               │
│     → Check: Docstrings, README, CHANGELOG                      │
│                                                                 │
│  ✅ 7. EVIDENCE COMPLETE                                        │
│     Can I audit this later?                                     │
│     → Check: state/EVIDENCE_LOG.md, GATES_LEDGER.md            │
│                                                                 │
│  ✅ 8. INTENT ALIGNMENT                                         │
│     Is this what we needed (no scope creep)?                    │
│     → Check: goal vs implementation, files changed, LOC         │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  DECISION:                                                      │
│  [ ] ✅ APPROVE (8/8 passed)                                    │
│  [ ] ⚠️  CONDITIONAL APPROVAL (6-7/8 passed, minor fixes)       │
│  [ ] ❌ REJECT (<6/8 passed OR any security issue)             │
│                                                                 │
│  Time: 10-15 minutes per task                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Decision Matrix

### How to Make G3 Decision

Use this flowchart:

```
START: Review validator_report.json
  ↓
Q1: Did Validator report "PASS"?
  ├─ NO → ❌ REJECT (don't proceed to G3 if G2 failed)
  └─ YES → Continue
  ↓
Q2: Did ANY of 8 human checks FAIL?
  ├─ YES → Go to Q3
  └─ NO → ✅ APPROVE (all checks passed)
  ↓
Q3: Was the failure Point 5 (Security)?
  ├─ YES → ❌ REJECT (security always blocks)
  └─ NO → Go to Q4
  ↓
Q4: How many checks failed?
  ├─ 1-2 checks → Go to Q5
  ├─ 3-4 checks → ❌ REJECT (too many issues)
  └─ 5+ checks → ❌ REJECT (fundamental problems)
  ↓
Q5: Are failures cosmetic (docs, style)?
  ├─ YES → ⚠️ CONDITIONAL APPROVAL (require minor fixes)
  └─ NO → Go to Q6
  ↓
Q6: Are failures fixable in <15 minutes?
  ├─ YES → ⚠️ CONDITIONAL APPROVAL (require fixes)
  └─ NO → ❌ REJECT (send back to Executor)
  ↓
END: Document decision in state/GATES_LEDGER.md
```

---

### Decision Outcomes

#### ✅ APPROVE

**When:**
- 8/8 checks passed
- OR: 7/8 passed with cosmetic issue (missing comment, typo)

**Action:**
```bash
# Update gates ledger
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
  "checklist_failed": 0,
  "deployment_approved": true
}
EOF
```

**Next Steps:**
- Merge PR
- Deploy to production
- If ROADMAP has more tasks → Return to Planner for next task

---

#### ⚠️ CONDITIONAL APPROVAL

**When:**
- 6-7/8 checks passed
- Failures are minor and fixable in <15 minutes
- No security issues

**Action:**
```bash
# Document required fixes
cat > state/G3_CONDITIONAL_FIXES.md << 'EOF'
## Conditional Approval - Minor Fixes Required

**Task:** T001 - Add email validation
**Approver:** [Your Name]
**Date:** 2025-01-01

### Issues Found:
1. ❌ Point 6 (Documentation): Missing docstring for `validate_email()`
2. ❌ Point 8 (Intent): Modified 3 files instead of 2 (added validation to Admin model without approval)

### Required Fixes:
1. Add docstring to `validate_email()` with description, args, returns, example
2. Remove validation from Admin model (out of scope) OR get approval to expand scope

### Deadline:
- 1 iteration (max 30 minutes)
- After fixes: I will re-verify Points 6 & 8 only

### Re-approval Process:
- Executor fixes issues
- Executor updates executor_report.json
- Human re-checks failed points
- If fixed → ✅ APPROVE
- If not fixed → ❌ REJECT
EOF

# Update gates ledger
echo "## Gate: G3 (Production-Ready)
- **Status:** ⚠️ CONDITIONAL APPROVAL
- **Timestamp:** $(date -u +"%Y-%m-%dT%H:%M:%SZ")
- **Approver:** [Your Name]
- **Checklist:** 6/8 passed
- **Fixes Required:** See state/G3_CONDITIONAL_FIXES.md
" >> state/GATES_LEDGER.md
```

**Next Steps:**
- Send G3_CONDITIONAL_FIXES.md to Executor
- Wait for fixes
- Re-verify only failed points
- Make final decision (APPROVE or REJECT)

---

#### ❌ REJECT

**When:**
- <6/8 checks passed
- OR: ANY security issue (regardless of other checks)
- OR: Fundamental problem (wrong approach, scope creep)

**Action:**
```bash
# Document rejection
cat > state/G3_REJECTION_REPORT.md << 'EOF'
## G3 Rejection Report

**Task:** T001 - Add email validation
**Approver:** [Your Name]
**Date:** 2025-01-01

### Rejection Reason:
❌ Point 5 (Security): Found SQL injection vulnerability in email lookup

### Details:
File: src/models/user.py, Line 45
```python
query = f"SELECT * FROM users WHERE email = '{email}'"
cursor.execute(query)  # ❌ SQL injection risk
```

### Impact:
CRITICAL - Attacker can inject SQL: `' OR '1'='1`

### Required Action:
Return to Executor for complete rewrite using parameterized queries.

### Next Steps:
1. Executor must use parameterized queries (SQLAlchemy ORM or psycopg2 params)
2. Validator must re-verify security (check_05)
3. Human must re-review (full 8-point checklist)
EOF

# Update gates ledger
echo "## Gate: G3 (Production-Ready)
- **Status:** ❌ REJECTED
- **Timestamp:** $(date -u +"%Y-%m-%dT%H:%M:%SZ")
- **Approver:** [Your Name]
- **Checklist:** 4/8 passed (Security FAILED)
- **Reason:** Critical security vulnerability (SQL injection)
- **Next Action:** Return to Executor for fix
" >> state/GATES_LEDGER.md
```

**Next Steps:**
- Send rejection report to Executor
- Executor fixes issue, re-submits
- Validator re-runs ALL checks (full G2 verification)
- Human re-runs ALL checks (full 8-point checklist)

**Iteration Limit:** Max 2 rejection cycles, then escalate to tech lead

---

## Common Issues & Solutions

### Issue 1: "Tests pass for Validator but fail for me"

**Symptom:**
```bash
pytest tests/
# FAILED tests/test_user.py::test_email_validation
```

But `artifacts/validator/check_02_test_quality.txt` shows all tests passing.

**Possible Causes:**

| Cause | How to Diagnose | Fix |
|-------|----------------|-----|
| **Environment difference** | `python --version` | Match Python version to Validator's |
| **Missing dependency** | `pip list` vs `requirements.txt` | `pip install -r requirements.txt` |
| **Cached modules** | Old `.pyc` files | `find . -type d -name __pycache__ -exec rm -rf {} +` |
| **Test order dependency** | Run single test: `pytest tests/test_user.py::test_email_validation` | Fix test isolation |
| **Timing issue** | Test uses `time.time()` without mocking | Mock time/random in tests |

**Resolution:**
1. Try running in fresh virtual environment
2. If still fails → Validator had environment issue, trust your result
3. If passes in fresh env → Your environment needs cleanup

---

### Issue 2: "Code works but I don't understand it"

**Symptom:** Point 4 (Code Readable) fails - code is too complex or unclear.

**Decision Framework:**

**Complexity Assessment:**

```python
# Example 1: Moderately complex but reasonable
def validate_email(email: str) -> bool:
    """Validate email format."""
    if not email or len(email) > 254:
        return False
    
    local, _, domain = email.partition("@")
    if not local or not domain:
        return False
    
    if not re.match(r"^[a-zA-Z0-9._%+-]+$", local):
        return False
    
    if not re.match(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", domain):
        return False
    
    return True

# ✅ PASS: Linear logic, each check is clear
```

```python
# Example 2: Too complex
def validate_email(email: str) -> bool:
    return bool(email and len(email) <= 254 and (lambda x: x[0] and x[1] if len(x := email.partition("@")) == 3 else False)() and all([re.match(r"^[a-zA-Z0-9._%+-]+$", email.split("@")[0]), re.match(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email.split("@")[1])]))

# ❌ FAIL: One-liner with lambdas, hard to debug
```

**Your Decision:**

- **If you can follow it in 60 seconds:** ✅ PASS (even if not elegant)
- **If you need >2 minutes to understand:** ⚠️ CONDITIONAL APPROVAL (request comments or refactor)
- **If you cannot understand it:** ❌ REJECT (request simplification)

**When in doubt:** Ask yourself "Can a junior developer maintain this?" If NO → send back.

---

### Issue 3: "Scope creep detected but changes look good"

**Symptom:** Point 8 (Intent Alignment) fails - Extra features added, but they're useful.

**Example:**
- **Requested:** Add email validation
- **Delivered:** Email validation + password validation + username validation

**Decision Framework:**

**Ask:**

1. **Were extra features necessary?**
   - If YES (e.g., email validation requires username validation) → ✅ APPROVE
   - If NO (could work without them) → Continue

2. **Do extra features add risk?**
   - If YES (touch critical code, security-sensitive) → ❌ REJECT
   - If NO (isolated, well-tested) → Continue

3. **Was scope expansion documented?**
   - If YES (executor_report.json explains why) → ⚠️ CONDITIONAL APPROVAL
   - If NO (no justification) → ❌ REJECT

4. **How much extra work was done?**
   - If <30% extra LOC → ⚠️ CONDITIONAL APPROVAL (accept but document)
   - If >50% extra LOC → ❌ REJECT (should have been separate task)

**Best Practice:**
- ⚠️ Accept scope expansion if it's small, low-risk, and documented
- ❌ Reject if it's large, risky, or unexplained
- Document in approval report: "Scope expanded to include X, accepted because Y"

---

### Issue 4: "Security scan found 'info' issues, do I care?"

**Symptom:** `check_05_security.txt` shows warnings but no critical/high issues.

**Example:**
```
INFO: Line 23: Use of assert statement
INFO: Line 45: Use of eval (but input is constant string)
```

**Decision Framework:**

| Severity | Action | Rationale |
|----------|--------|-----------|
| **Critical** | ❌ REJECT | Remote code execution, SQL injection, authentication bypass |
| **High** | ❌ REJECT | Data exposure, privilege escalation, DoS |
| **Medium** | ⚠️ CONDITIONAL | Depends on context (e.g., weak crypto in test file is OK) |
| **Low** | ✅ PASS | Create follow-up ticket but don't block deployment |
| **Info** | ✅ PASS | Ignore (informational only) |

**For INFO/LOW issues:**
- ✅ Pass G3 gate
- Create follow-up ticket for technical debt
- Document in approval report

---

### Issue 5: "I'm 50/50 on whether to approve"

**Symptom:** Some checks pass, some are borderline, overall uncertain.

**Decision Framework:**

**When uncertain, ask:**

1. **"If this breaks in production, how bad is the impact?"**
   - Catastrophic (data loss, security breach) → ❌ REJECT
   - Bad (service down, users can't work) → ❌ REJECT
   - Annoying (UI bug, wrong error message) → ⚠️ CONDITIONAL
   - Negligible (cosmetic issue) → ✅ APPROVE

2. **"Can I explain this decision to my manager?"**
   - If NO → ❌ REJECT (trust your gut)
   - If YES → Continue

3. **"Have I seen the Executor deliver quality work before?"**
   - If YES (established trust) → ⚠️ CONDITIONAL (give benefit of doubt)
   - If NO (first task or history of issues) → ❌ REJECT (hold to higher bar)

**Default Position:**
- **When uncertain:** ⚠️ CONDITIONAL APPROVAL with specific fixes
- **If still uncertain after fixes:** ❌ REJECT (better safe than sorry)
- **Never approve if you're uncomfortable with security or correctness**

**Escalation:**
If you're stuck, escalate to:
- Tech lead (for architecture decisions)
- Security team (for security questions)
- Product manager (for scope/requirements questions)

---

## Appendix: Verification Commands

### Quick Command Reference

```bash
# ─────────────────────────────────────────────────────────
# SETUP (run once)
# ─────────────────────────────────────────────────────────

# Navigate to run directory
cd runs/<run-id>/

# Activate virtual environment (if using)
source venv/bin/activate

# ─────────────────────────────────────────────────────────
# POINT 1: REQUIREMENTS MET
# ─────────────────────────────────────────────────────────

# Read original goal
cat state/CURRENT_TASK.json | jq '.goal'

# Check what was implemented
git diff main...HEAD src/ | less

# ─────────────────────────────────────────────────────────
# POINT 2: TESTS PASS
# ─────────────────────────────────────────────────────────

# Run all tests
pytest tests/ -v

# Run with coverage
pytest --cov=src --cov-report=term-missing

# Run specific test file
pytest tests/test_user.py -v

# ─────────────────────────────────────────────────────────
# POINT 3: NO BROKEN FEATURES
# ─────────────────────────────────────────────────────────

# Run smoke tests (if available)
pytest tests/smoke/ -v

# Or run integration tests
pytest tests/integration/ -v

# ─────────────────────────────────────────────────────────
# POINT 4: CODE READABLE
# ─────────────────────────────────────────────────────────

# View all changed code
git diff main...HEAD src/ | less

# View specific file
git diff main...HEAD src/models/user.py

# Check complexity (if using radon)
radon cc src/models/user.py -a

# ─────────────────────────────────────────────────────────
# POINT 5: SECURITY CHECK
# ─────────────────────────────────────────────────────────

# Read Validator's security scan
cat artifacts/validator/check_05_security.txt

# Re-run security scan yourself
bandit -r src/ -f txt

# Check for secrets
git diff main...HEAD | grep -i "api_key\|password\|secret\|token"

# ─────────────────────────────────────────────────────────
# POINT 6: DOCUMENTATION UPDATED
# ─────────────────────────────────────────────────────────

# Check docstrings in changed code
git diff main...HEAD src/ | grep -A 10 "def "

# Check README mentions feature
grep -i "email\|validation" README.md

# Check CHANGELOG
head -20 CHANGELOG.md

# ─────────────────────────────────────────────────────────
# POINT 7: EVIDENCE COMPLETE
# ─────────────────────────────────────────────────────────

# List all evidence artifacts
ls -lh artifacts/executor/
ls -lh artifacts/validator/

# Check evidence log
cat state/EVIDENCE_LOG.md | grep "T001"

# Verify gate progression
cat state/GATES_LEDGER.md

# ─────────────────────────────────────────────────────────
# POINT 8: INTENT ALIGNMENT
# ─────────────────────────────────────────────────────────

# Compare goal vs summary
cat state/CURRENT_TASK.json | jq '.goal'
cat executor_report.json | jq '.summary'

# Check files changed
cat state/CURRENT_TASK.json | jq '.scope.files_to_modify'
git diff main...HEAD --name-only

# Check LOC estimate vs actual
cat state/CURRENT_TASK.json | jq '.scope.estimated_loc'
git diff main...HEAD --stat

# ─────────────────────────────────────────────────────────
# DECISION DOCUMENTATION
# ─────────────────────────────────────────────────────────

# Approve
echo "G3: ✅ APPROVED" >> state/GATES_LEDGER.md

# Conditional approval
echo "G3: ⚠️ CONDITIONAL APPROVAL" >> state/GATES_LEDGER.md
# (create state/G3_CONDITIONAL_FIXES.md with fix list)

# Reject
echo "G3: ❌ REJECTED" >> state/GATES_LEDGER.md
# (create state/G3_REJECTION_REPORT.md with details)
```

---

## Summary

### The 8-Point Checklist (Memorize This)

1. **Requirements Met** - Does it solve the problem?
2. **Tests Pass** - Do tests pass when I run them?
3. **No Broken Features** - Did this break anything?
4. **Code Readable** - Can I understand it?
5. **Security Check** - Any obvious risks?
6. **Documentation Updated** - Are new functions documented?
7. **Evidence Complete** - Can I audit this later?
8. **Intent Alignment** - Is this what we needed (no scope creep)?

### Decision Rules (Memorize This)

- **8/8 passed** → ✅ APPROVE
- **6-7/8 passed, minor issues** → ⚠️ CONDITIONAL APPROVAL
- **<6/8 passed** → ❌ REJECT
- **ANY security issue** → ❌ REJECT (regardless of other checks)

### Time Budget

- **Target:** 10-15 minutes per task
- **Maximum:** 20 minutes
- **If taking longer:** Task too complex, send back to Planner

---

## Version History

- **v1.0.0** (2025-01-01): Initial production release

---

**You are the final guardian before production. Trust your judgment! 🛡️**

For bridge protocol, see [Human_Bridge_Protocol.md](./Human_Bridge_Protocol.md)  
For complete workflow, see [Quick_Start_Guide.md](./Quick_Start_Guide.md)