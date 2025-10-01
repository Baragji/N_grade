# Human Verification Checklist for AI-Generated Code
## Non-Technical Stakeholder Guide (No Coding Experience Required)

> **Purpose:** This checklist enables non-technical stakeholders to verify that AI coding agents followed Test-Driven Development (TDD) and quality standards—**without needing to understand code**. You're checking for evidence patterns, not code correctness.

---

## 🎯 Quick Start: What You're Looking For

When an AI agent delivers work, you should receive output with these sections:
- **PLAN** (the approach)
- **PATCH** (the code changes)
- **LOGS** (proof of testing)
- **PR_NOTE** (explanation)
- **ARTIFACTS** (quality reports)

**Your job:** Verify the **LOGS** section shows the TDD cycle happened correctly.

---

## ✅ The 5-Minute Verification (Essential Checks)

### **1. Check: Did Tests Fail First? (RED Phase)**

**What to look for in LOGS:**
```
✅ GOOD - You should see test FAILURES first:
$ pytest -q tests/test_feature.py::test_new_behavior
F                                                    [100%]
FAILED tests/test_feature.py::test_new_behavior
```

**Red flags:**
```
❌ BAD - Only passing tests, no failures shown:
$ pytest -q
..................................................  [100%]
52 passed in 2.34s
(Missing the initial failure!)
```

**Why this matters:** If tests never failed, the agent might have written code BEFORE tests (violating TDD).

---

### **2. Check: Did Tests Pass After Implementation? (GREEN Phase)**

**What to look for in LOGS:**
```
✅ GOOD - Same test now PASSES:
$ pytest -q tests/test_feature.py::test_new_behavior
.                                                    [100%]
1 passed in 0.05s
```

**Why this matters:** This proves the agent wrote code that actually makes the test pass.

---

### **3. Check: Did Full Test Suite Stay Green?**

**What to look for in LOGS:**
```
✅ GOOD - All existing tests still pass:
$ pytest -q
....................................................  [100%]
52 passed in 2.34s
```

**Red flags:**
```
❌ BAD - Any failures in full suite:
$ pytest -q
.................................F..................  [100%]
51 passed, 1 failed in 2.45s
```

**Why this matters:** New code shouldn't break existing functionality (regressions).

---

### **4. Check: Quality Gates Passed**

**What to look for in LOGS:**
```
✅ GOOD - All these should show success:
$ make lint
All checks passed!

$ make mutation
Mutation score: 94.2% (target: 90%)

$ python scripts/owasp_llm_gate.py
No critical findings.
```

**Red flags:**
```
❌ BAD - Any gate failures:
$ make lint
ERROR: Line too long (120 > 88)
ERROR: Unused import
```

**Why this matters:** Code must meet quality standards (style, security, test coverage).

---

### **5. Check: PR_NOTE Explains TDD Approach**

**What to look for in PR_NOTE:**
```
✅ GOOD - Mentions TDD cycle explicitly:
**How (TDD):** 
1. Wrote failing test defining expected behavior (RED)
2. Implemented minimal passing code (GREEN)
3. Verified no regressions across full suite
```

**Red flags:**
```
❌ BAD - Vague or missing TDD explanation:
"Added new feature and tests pass."
(No mention of RED→GREEN cycle)
```

---

## 📋 Complete Verification Checklist

Print this and check each item:

### **Section 1: TDD Evidence (Most Important)**
- [ ] **RED Phase:** LOGS show test(s) **FAILED** initially (look for "F", "FAILED", or "AssertionError")
- [ ] **GREEN Phase:** LOGS show same test(s) **PASSED** after code changes (look for ".", "passed", or "1 passed")
- [ ] **Sequence:** Failure shown BEFORE success (chronological order matters)
- [ ] **Test name visible:** Can identify which specific test was being developed (e.g., `test_email_validation_rejects_invalid_format`)

### **Section 2: Regression Protection**
- [ ] Full test suite runs shown in LOGS (`pytest -q` without specific file)
- [ ] Full suite shows "X passed" with no failures
- [ ] Number of passing tests makes sense (should be 50+, not just 1-2)
- [ ] No error messages, tracebacks, or warnings in full suite run

### **Section 3: Quality Gates**
- [ ] **Lint:** `make lint` shows "All checks passed" or similar success message
- [ ] **Mutation:** `make mutation` shows score above 90% (e.g., "94.2%")
- [ ] **Security:** OWASP check shows "No critical findings"
- [ ] **Accessibility:** (if UI changes) `pnpm run axe-ci` shows no violations

### **Section 4: Artifacts Produced**
- [ ] ARTIFACTS section lists file paths (not just "artifacts created")
- [ ] Expected files mentioned:
  - `reports/mutation/summary.json`
  - `reports/owasp-report.json`
  - `reports/owasp-report.html`
- [ ] (Optional) Coverage report mentioned if requested

### **Section 5: PR_NOTE Quality**
- [ ] **What:** Clearly states what code was added/changed
- [ ] **Why:** Explains the problem being solved or feature being added
- [ ] **How (TDD):** Explicitly mentions RED→GREEN cycle
- [ ] **Risks:** Identifies potential issues or states "None"
- [ ] **Commit:** Uses Conventional Commits format (e.g., `feat(auth): add email validation`)
- [ ] Length: ≤120 words (concise, not verbose)

### **Section 6: PLAN Accuracy**
- [ ] PLAN section exists and was approved before implementation
- [ ] PLAN mentions "write failing test first" or similar TDD language
- [ ] PLAN lists ≤5 bullets (not a novel)
- [ ] Actual PATCH matches PLAN scope (no surprise files)

### **Section 7: PATCH Hygiene**
- [ ] PATCH section contains only code (diff format: `---/+++` and `@@`)
- [ ] No English prose or explanations inside PATCH section
- [ ] Test file changes appear BEFORE implementation file changes (when possible)
- [ ] Only files listed in PLAN are modified (no "drive-by" changes)

---

## 🚨 Red Flags That Require Push-Back

If you see ANY of these, **reject the deliverable** and ask the agent to redo it:

### **Critical Failures:**
1. **No failing test shown** - Agent skipped RED phase (not TDD)
2. **Test failures in full suite** - Code broke existing functionality
3. **Quality gate failures** - Lint/mutation/OWASP showing errors
4. **Missing LOGS section** - No evidence provided (agent could be lying)
5. **Secrets/credentials in PATCH** - Security violation (passwords, API keys visible)

### **Quality Issues:**
6. **LOGS missing TDD cycle** - Only shows final passing tests, not RED→GREEN
7. **PR_NOTE doesn't mention TDD** - No explanation of test-first approach
8. **PLAN not approved** - Agent skipped plan-then-patch workflow
9. **Stray files modified** - Files changed that weren't in PLAN
10. **Vague test names** - Tests called `test_1`, `test_it_works` (not descriptive)

---

## 🎓 Learning to Spot Patterns (No Code Knowledge Needed)

### **What "FAILED" Looks Like:**
```
F                                    [100%]
======================== FAILURES ========================
___________________ test_something ___________________
E   AssertionError: expected X but got Y
E   AttributeError: 'Class' has no attribute 'method'
E   ValueError: invalid input
```
**Key words:** `F`, `FAILED`, `AssertionError`, `Error`, `Traceback`

### **What "PASSED" Looks Like:**
```
.                                    [100%]
1 passed in 0.05s

..................................................  [100%]
52 passed in 2.34s
```
**Key words:** `.`, `passed`, no error messages

### **What "Full Suite" Looks Like:**
```
$ pytest -q
(Notice: NO file path after pytest -q, means "all tests")
```

### **What "Targeted Test" Looks Like:**
```
$ pytest -q tests/test_feature.py::test_new_behavior
(Notice: Specific file and test name)
```

---

## 📊 Example: Complete GOOD Verification

Here's what a **passing** submission looks like:

```
=== TDD CYCLE EVIDENCE ===

# Step 1: RED (test fails first)
$ pytest -q tests/test_user.py::test_email_validation
F                                                        [100%]
FAILED tests/test_user.py::test_email_validation
E   AttributeError: 'User' object has no attribute 'validate_email'
1 failed in 0.08s

# Step 2: GREEN (test now passes)
$ pytest -q tests/test_user.py::test_email_validation
.                                                        [100%]
1 passed in 0.05s

# Step 3: Full suite (no regressions)
$ pytest -q
....................................................     [100%]
52 passed in 2.34s

# Quality gates
$ make lint
All checks passed!

$ make mutation
Mutation score: 94.2% (target: 90%)
```

**Your checklist results:**
- ✅ RED phase visible (F, FAILED, AttributeError)
- ✅ GREEN phase visible (., 1 passed)
- ✅ Full suite green (52 passed)
- ✅ All gates passed
- ✅ **APPROVE THIS DELIVERABLE**

---

## 📊 Example: Complete BAD Verification

Here's what a **failing** submission looks like:

```
=== LOGS ===

$ pytest -q
....................................................     [100%]
52 passed in 2.34s

$ make lint
All checks passed!
```

**Your checklist results:**
- ❌ No RED phase visible (no failing tests shown)
- ❌ No targeted test run shown (only full suite)
- ❌ Cannot verify TDD was followed
- ❌ **REJECT THIS DELIVERABLE** with message:
  > "LOGS section missing TDD cycle evidence. Please show:
  > 1. Initial test failure (RED)
  > 2. Same test passing after implementation (GREEN)
  > See Human_Verification_Checklist.md Section 1 for examples."

---

## 💡 Quick Rejection Templates

Use these copy-paste responses when rejecting deliverables:

### **Missing RED Phase:**
```
❌ REJECTED: No TDD evidence

LOGS must show test FAILING first (RED phase) before implementation.
Currently only shows passing tests.

Required format:
1. Run test → FAILED (RED)
2. Add code
3. Run same test → PASSED (GREEN)
4. Run full suite → all PASSED

Please redo with complete RED→GREEN cycle visible.
```

### **Quality Gate Failures:**
```
❌ REJECTED: Quality gates failed

LOGS show failures:
- [specify which gate: lint/mutation/OWASP]

Fix issues and re-run gates until all GREEN.
Do not proceed with failed gates.
```

### **Missing LOGS Section:**
```
❌ REJECTED: No evidence provided

LOGS section missing or incomplete.
Cannot verify TDD cycle without evidence.

Required: Show pytest output for RED→GREEN cycle.
See Human_Verification_Checklist.md for examples.
```

---

## 🎯 Summary: The 30-Second Check

**If you're time-constrained, just check these 3 things:**

1. **LOGS has "FAILED" followed by "passed"** ✅
2. **Full test suite shows "X passed, 0 failed"** ✅
3. **All quality gates say success/passed/no findings** ✅

**All 3 green? → Approve**  
**Any red? → Reject with specific reason**

---

## 📞 When to Escalate

Ask a technical team member to review if you see:
- Confusing error messages in LOGS
- Unfamiliar quality gate failures
- Security warnings (OWASP findings)
- Mutation score below 90%
- More than 2 rejections for same task (agent may be stuck)

---

## 📝 Notes Section (for your records)

**Task ID:** _______________________  
**Reviewer:** _______________________  
**Date:** _______________________  

**Verification Results:**
- [ ] TDD Evidence: ✅ PASS / ❌ FAIL
- [ ] Quality Gates: ✅ PASS / ❌ FAIL
- [ ] PR_NOTE Quality: ✅ PASS / ❌ FAIL
- [ ] Overall: ✅ APPROVED / ❌ REJECTED

**Notes:**
_____________________________________________
_____________________________________________
_____________________________________________

---

**Version:** 1.0 (Oct 2025)  
**Optimized for:** GPT-5, Claude Sonnet 4.5, GPT-5-Codex agents  
**Last Updated:** 2025-10-29