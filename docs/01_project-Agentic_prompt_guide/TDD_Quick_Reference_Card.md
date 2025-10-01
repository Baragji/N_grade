# TDD Quick Reference Card
## For AI Coding Agents (Planner & Executor)

> **Print this:** 1-page cheatsheet for Test-Driven Development in AI agent workflows

---

## 🎯 Core Principle: RED → GREEN → REFACTOR

```
┌─────────────────────────────────────────────────────┐
│  1. RED    Write failing test → Run → FAILS       │
│  2. GREEN  Write minimal code → Run → PASSES      │
│  3. REFACTOR Clean code → Run → STAYS GREEN       │
└─────────────────────────────────────────────────────┘
```

**Evidence Required:** LOGS must show test **FAILED** then **PASSED**

---

## 📋 Planner's TDD Checklist

### **PLAN Format (≤5 bullets):**
```
1. Write failing test in tests/test_X.py::test_new_behavior (RED)
2. Run test → capture FAILURE output
3. Implement minimal code in autonomy/X.py
4. Run test → capture SUCCESS output (GREEN)
5. Run full suite + gates; update PR note
```

### **definition_of_done Must Include:**
```json
"TDD cycle followed: at least one new test written FIRST 
and failed (RED), then code implemented, then test passes 
(GREEN); logs show RED→GREEN evidence"
```

### **Instruct Executor:**
- "Write failing test FIRST (RED phase)"
- "Implement minimal passing code (GREEN phase)"
- "Prove RED→GREEN in LOGS output"

---

## 📋 Executor's TDD Checklist

### **NEW Feature Workflow:**
```bash
# 1. Write test FIRST
edit tests/test_feature.py  # Add test_new_behavior

# 2. Prove RED
$ pytest -q tests/test_feature.py::test_new_behavior
F [FAILED] ← Capture this output!

# 3. Implement minimal code
edit autonomy/feature.py  # Add new_behavior()

# 4. Prove GREEN
$ pytest -q tests/test_feature.py::test_new_behavior
. [1 passed] ← Capture this output!

# 5. Verify no regressions
$ pytest -q
[52 passed] ← Capture this output!
```

### **BUG Fix Workflow:**
```bash
# 1. Write test that REPRODUCES bug
edit tests/test_feature.py  # Add test_bug_reproduction

# 2. Prove bug exists (RED)
$ pytest -q tests/test_feature.py::test_bug_reproduction
F [FAILED] ← Bug confirmed!

# 3. Fix bug
edit autonomy/feature.py  # Minimal fix

# 4. Prove bug fixed (GREEN)
$ pytest -q tests/test_feature.py::test_bug_reproduction
. [1 passed] ← Bug gone!
```

### **REFACTORING Workflow:**
```bash
# 1. Ensure tests cover code being refactored
$ pytest -q --cov=autonomy/feature.py
[Coverage: 95%] ← Good coverage

# 2. Refactor while keeping tests GREEN
edit autonomy/feature.py  # Refactor
$ pytest -q
[52 passed] ← Still green!

# If gaps found:
# Write tests FIRST (RED→GREEN), THEN refactor
```

---

## ❌ TDD Anti-Patterns (FORBIDDEN)

| ❌ DON'T | ✅ DO |
|---------|------|
| Write code before tests | Write failing test FIRST |
| Assume test would fail | **Run and prove** it fails (RED) |
| Write tests for existing code | Write tests, watch fail, then code |
| Skip RED phase | Always capture FAILED output |
| Over-implement | Minimal code to pass current test |
| Generic test names (`test_1`) | Descriptive names (`test_email_rejects_invalid_format`) |
| Skip refactor when messy | Refactor but keep tests green |
| Fake test results | Show **actual pytest output** |

---

## 📊 LOGS Format (Required Evidence)

```
=== TDD CYCLE EVIDENCE ===

# Step 1: RED (test fails as expected)
$ pytest -q tests/test_feature.py::test_new_behavior
F                                                        [100%]
================================= FAILURES =================================
_________________________ test_new_behavior _________________________
    def test_new_behavior(self):
        result = feature.new_behavior(input="test")
E       AttributeError: 'Feature' has no attribute 'new_behavior'
1 failed in 0.08s

# Step 2: GREEN (minimal implementation passes)
$ pytest -q tests/test_feature.py::test_new_behavior
.                                                        [100%]
1 passed in 0.05s

# Step 3: Full suite (no regressions)
$ pytest -q
....................................................     [100%]
52 passed in 2.34s

# Step 4: Quality gates
$ make lint
All checks passed!

$ make mutation
Mutation score: 94.2% (target: 90%)
```

**Key signals for humans:**
- `F` or `FAILED` = RED phase ✅
- `.` or `passed` = GREEN phase ✅
- `52 passed` = No regressions ✅

---

## 🎯 Test Naming Convention

### **Good (Descriptive):**
```python
def test_email_validation_rejects_invalid_format():
def test_user_creation_succeeds_with_valid_inputs():
def test_payment_fails_when_insufficient_balance():
def test_cache_hit_returns_cached_value():
```

### **Bad (Vague):**
```python
def test_email():
def test_user():
def test_1():
def test_it_works():
```

**Rule:** Test name should describe expected behavior, not just the method being tested.

---

## 📝 PR_NOTE TDD Section (Required)

```markdown
**How (TDD):** 
1. Wrote failing test defining expected behavior (RED)
2. Implemented minimal passing code (GREEN)
3. Verified no regressions across full suite

**Test Evidence:** 
- tests/test_feature.py::test_new_behavior (FAILED → PASSED)
- Full suite: 52 passed, 0 failed
```

---

## 🚀 Model-Specific TDD Tips

### **GPT-5 / GPT-5-Codex:**
- Use explicit tool sequence: `write_test()` → `run_test()` → `implement()` → `run_test()` → `run_gates()`
- Codex self-plans aggressively → **follow Planner's TDD sequence strictly**
- Capture each step's output separately

### **Claude Sonnet 4.5:**
- Emphasize tool-heavy: `bash` + `file_edit`
- Explicitly state "write tests first" in every task prompt
- Sonnet excels at TDD when workflow is explicit

---

## 🔄 Iteration Protocol

### **If test stays RED after implementation:**
```
1. STOP and report:
   STATUS: test_still_failing
   LOGS: <failure output>
   REMEDIATION:
   - Check test expectations vs implementation
   - Verify test setup/fixtures correct
   - Run test in isolation to debug

2. AWAIT approval before trying again
```

### **If gates fail after GREEN:**
```
1. STOP and report which gate failed:
   STATUS: mutation_gate_failed
   LOGS: <mutation score: 87% (target: 90%)>
   REMEDIATION:
   - Add missing edge case tests
   - Test error handling paths
   - Re-run mutation gate

2. AWAIT approval before proceeding
```

### **2-Iteration Rule:**
After **2 failed attempts**, pause and request human intervention.

---

## 🎓 TDD Verification for Non-Technical Reviewers

**Look for these patterns in LOGS:**

1. **Word "FAILED" or letter "F" appears first** ← RED phase
2. **Same test then shows "passed" or "."** ← GREEN phase
3. **Full suite shows "X passed, 0 failed"** ← No regressions
4. **All gates show success messages** ← Quality verified

**If any missing → REJECT deliverable**

---

## 📋 Complete Task Checklist

Before marking task DONE, verify:

- [ ] ✅ At least one new test written FIRST (before implementation)
- [ ] ✅ Test failed initially (RED phase in LOGS)
- [ ] ✅ Minimal code added to make test pass
- [ ] ✅ Test now passes (GREEN phase in LOGS)
- [ ] ✅ Full test suite passes (no regressions)
- [ ] ✅ All quality gates pass (lint, mutation ≥90%, OWASP, accessibility)
- [ ] ✅ Code refactored if needed (while keeping tests green)
- [ ] ✅ LOGS show complete RED→GREEN cycle
- [ ] ✅ PR_NOTE explains TDD approach with evidence
- [ ] ✅ PATCH shows test file changes BEFORE implementation files
- [ ] ✅ Test names are descriptive (not `test_1`, `test_it_works`)
- [ ] ✅ Artifacts list includes all quality reports

---

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| "Agent skipped RED phase" | **Reject:** Require FAILED output before PASSED |
| "Can't tell if TDD followed" | **Check LOGS:** Must show F or FAILED then passed |
| "Test names too vague" | **Reject:** Require descriptive names explaining behavior |
| "No regression tests shown" | **Require:** Full suite run (`pytest -q`) output |
| "Agent loops on same test" | **Stop after 2 iterations:** Request human debugging |

---

## 📞 When to Escalate

- Test fails after 2 implementation attempts
- Mutation score stuck below 90% after 2 tries
- OWASP findings show critical security issues
- Agent outputs secrets/credentials in PATCH
- Agent modifies files outside PLAN scope

---

## 🔗 Related Documents

- **Human_Verification_Checklist.md** - Non-technical verification guide
- **System_prompt_planner.md** - Complete Planner prompt with TDD
- **Executor_system_prompt.md** - Complete Executor prompt with TDD
- **ai-coding-prompt-guide.md** - Original research & best practices

---

**Version:** 1.0 (Oct 2025)  
**Compatible:** GPT-5, Claude Sonnet 4.5, GPT-5-Codex  
**Scope:** Copilot, Cursor, Trae, Zencoder agent workflows