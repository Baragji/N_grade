# H3A Handoff Contracts
**Version:** 1.0.0  
**Last Updated:** 2025-01-XX

---

## Purpose

Handoff contracts define **explicit expectations** between agents in the H3A workflow. Each contract specifies:

1. **What the sending agent promises to deliver**
2. **What the receiving agent can assume**
3. **How to verify the handoff is valid**
4. **What to do if expectations aren't met**

**Goal:** Eliminate ambiguity and prevent wasted work due to miscommunication.

---

## Handoff Overview

```
┌──────────┐           ┌──────────┐           ┌───────────┐
│ PLANNER  │ ────────► │ EXECUTOR │ ────────► │ VALIDATOR │
└──────────┘           └──────────┘           └───────────┘
     │                       │                       │
   [H1]                    [H2]                   [H3]
  G0→G1                   G1→G2                   G2→G3
```

| Handoff | From | To | Gate Transition | Payload |
|---------|------|----|-----------------|---------  |
| **H1** | Planner | Executor | G0 → G1 | Task specification, TDD plan |
| **H2** | Executor | Validator | G1 → G2 | TDD evidence, implementation |
| **H3** | Validator | System/Planner | G2 → G3 | Verdict, next task approval |

---

## H1: Planner → Executor

### Context

**When:** After Planner completes G0 (Planning Gate)  
**Why:** Executor needs clear task definition and TDD strategy to implement  
**Human Role:** Reads `SESSION_HANDOFF.json`, invokes Executor with payload

---

### Planner's Obligations

The Planner **MUST** provide:

| Obligation | Artifact | Verification |
|------------|----------|--------------|
| ✅ **Task specification** | `state/CURRENT_TASK.json` | File exists, `goal` field filled |
| ✅ **TDD plan** | `state/CURRENT_TASK.json` → `tdd_plan` | `red`, `green`, `refactor` fields filled |
| ✅ **Definition of Done** | `state/CURRENT_TASK.json` → `definition_of_done` | Array with ≥3 measurable criteria |
| ✅ **Files affected** | `state/CURRENT_TASK.json` → `files_affected` | Array with expected file paths |
| ✅ **Planning report** | `planner_report.json` | File exists with task_id entry |
| ✅ **Gate status** | `state/GATES_LEDGER.md` | Shows "G0_planning - PASSED" |
| ✅ **Handoff logged** | `state/SESSION_HANDOFF.json` | Updated with `next_agent: "executor"` |

---

### Executor's Assumptions

The Executor **CAN ASSUME**:

1. ✅ Task is well-scoped (1-3 files, <200 LOC changed)
2. ✅ TDD plan is executable (tests can be written as described)
3. ✅ DoD criteria are measurable and achievable
4. ✅ No blocking dependencies (or documented in `CURRENT_TASK.json`)
5. ✅ Baseline tests are passing (no broken builds)

---

### Handoff Payload (H1)

**File:** `state/SESSION_HANDOFF.json`

```json
{
  "run_id": "20250929-134215-8b6f8b9a-...",
  "handoff_id": "H1",
  "from_agent": "planner",
  "to_agent": "executor",
  "handoff_time": "2025-09-29T14:05:30Z",
  "gate_transition": "G0_passed → G1_pending",
  
  "payload": {
    "task_id": "T001",
    "goal": "Add JWT authentication with token expiration",
    "context": "Implement secure token-based auth following OWASP guidelines",
    
    "files_to_review": [
      "state/ROADMAP.md",
      "state/CURRENT_TASK.json",
      "planner_report.json"
    ],
    
    "tdd_plan": {
      "red": "Write test_jwt_generation() expecting valid token structure with exp claim",
      "green": "Implement generate_jwt() using PyJWT to pass test",
      "refactor": "Extract key management to src/config/keys.py"
    },
    
    "definition_of_done": [
      "Test coverage ≥95% for auth module",
      "Token expiration validated (tokens expire in 1 hour)",
      "Secret key rotation documented in README",
      "Security scan passes (no JWT vulnerabilities)"
    ],
    
    "action_required": "Executor must implement TDD cycle (RED→GREEN→REFACTOR) and save evidence to artifacts/executor/"
  },
  
  "verification_checklist": [
    "CURRENT_TASK.json exists and is valid JSON",
    "tdd_plan has red, green, refactor fields filled",
    "definition_of_done has ≥3 criteria",
    "files_affected is non-empty array",
    "GATES_LEDGER shows G0 PASSED"
  ]
}
```

---

### Handoff Validation

**Executor MUST verify before starting:**

```bash
# Check task file exists
test -f runs/<run-id>/state/CURRENT_TASK.json

# Check TDD plan filled
jq -e '.tdd_plan.red != null and .tdd_plan.green != null and .tdd_plan.refactor != null' \
  runs/<run-id>/state/CURRENT_TASK.json

# Check DoD has ≥3 criteria
jq -e '.definition_of_done | length >= 3' runs/<run-id>/state/CURRENT_TASK.json

# Check G0 passed
grep -q "G0_planning - PASSED" runs/<run-id>/state/GATES_LEDGER.md
```

**If validation fails:**
1. Log error in `state/GATES_LEDGER.md`: `[timestamp] G1_implementation - REJECTED - executor - Reason: <error>`
2. Update `SESSION_HANDOFF.json` with `status: "rejected"`
3. Escalate to human for Planner remediation

---

### Common Handoff Failures (H1)

| Failure | Detection | Resolution |
|---------|-----------|------------|
| **Vague TDD plan** | tdd_plan.red is generic ("Write tests") | Executor rejects handoff, Planner refines |
| **Unrealistic DoD** | DoD includes unmeasurable criteria ("Fast performance") | Executor rejects, Planner makes DoD measurable |
| **Missing dependencies** | Executor discovers blocker (missing API key) | Executor adds blocker to CURRENT_TASK.json, escalates |
| **Broken baseline** | Existing tests failing | Executor rejects, Planner fixes or documents known issue |

---

## H2: Executor → Validator

### Context

**When:** After Executor completes G1 (Implementation Gate)  
**Why:** Validator needs TDD evidence and implementation artifacts to verify quality  
**Human Role:** Reads `SESSION_HANDOFF.json`, invokes Validator with payload

---

### Executor's Obligations

The Executor **MUST** provide:

| Obligation | Artifact | Verification |
|------------|----------|--------------|
| ✅ **RED phase evidence** | `artifacts/executor/test_output_red.txt` | File exists, shows test failure |
| ✅ **GREEN phase evidence** | `artifacts/executor/test_output_green.txt` | File exists, shows all tests passing |
| ✅ **Coverage delta** | `artifacts/executor/coverage_delta.json` | Coverage increased OR ≥90% absolute |
| ✅ **Execution report** | `executor_report.json` | TDD cycle documented, DoD checked |
| ✅ **Files changed** | `executor_report.json` → `files_changed` | List of modified files |
| ✅ **Commands run** | `executor_report.json` → `commands_run` | Test/lint/type check commands with exit codes |
| ✅ **Gate status** | `state/GATES_LEDGER.md` | Shows "G1_implementation - PASSED" |
| ✅ **Handoff logged** | `state/SESSION_HANDOFF.json` | Updated with `next_agent: "validator"` |

---

### Validator's Assumptions

The Validator **CAN ASSUME**:

1. ✅ TDD cycle followed (RED→GREEN evidence exists)
2. ✅ All tests are passing (executor verified)
3. ✅ Coverage did not decrease
4. ✅ Lint and type checks passed (executor verified)
5. ✅ DoD checklist addressed (executor attempted all criteria)

**Note:** Validator still **re-runs** verification commands to independently confirm!

---

### Handoff Payload (H2)

**File:** `state/SESSION_HANDOFF.json`

```json
{
  "run_id": "20250929-134215-8b6f8b9a-...",
  "handoff_id": "H2",
  "from_agent": "executor",
  "to_agent": "validator",
  "handoff_time": "2025-09-29T14:45:00Z",
  "gate_transition": "G1_passed → G2_pending",
  
  "payload": {
    "task_id": "T001",
    "summary": "JWT authentication implemented with TDD, all tests passing, coverage +5.2%",
    
    "files_to_review": [
      "state/CURRENT_TASK.json",
      "executor_report.json",
      "artifacts/executor/test_output_red.txt",
      "artifacts/executor/test_output_green.txt",
      "artifacts/executor/coverage_delta.json"
    ],
    
    "tdd_evidence": {
      "red_phase": "artifacts/executor/test_output_red.txt",
      "green_phase": "artifacts/executor/test_output_green.txt",
      "refactor_phase": "Code refactored, tests still passing"
    },
    
    "files_changed": [
      "src/auth/jwt.py",
      "tests/test_auth.py",
      "src/config/keys.py"
    ],
    
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
      },
      {
        "cmd": "make lint",
        "exit_code": 0,
        "artifact": "artifacts/executor/lint_output.txt"
      }
    ],
    
    "coverage_delta": "+5.2%",
    "coverage_absolute": "94.2%",
    
    "definition_of_done_status": [
      {"criterion": "Coverage ≥95%", "met": false, "actual": "94.2%", "notes": "0.8% short, acceptable?"},
      {"criterion": "Token expiration validated", "met": true},
      {"criterion": "Secret key rotation documented", "met": true},
      {"criterion": "Security scan passes", "met": true, "notes": "Bandit scan clean"}
    ],
    
    "iteration_count": 1,
    
    "action_required": "Validator must verify TDD compliance, re-run security scan, check mutation score, and approve/reject based on comprehensive checklist"
  },
  
  "verification_checklist": [
    "executor_report.json exists and is valid JSON",
    "TDD evidence files exist (test_output_red.txt, test_output_green.txt)",
    "coverage_delta is positive or absolute ≥90%",
    "commands_run array shows exit_code: 0 for tests/lint/type",
    "GATES_LEDGER shows G1 PASSED"
  ]
}
```

---

### Handoff Validation

**Validator MUST verify before starting:**

```bash
# Check RED phase exists
test -f runs/<run-id>/artifacts/executor/test_output_red.txt

# Check GREEN phase exists
test -f runs/<run-id>/artifacts/executor/test_output_green.txt

# Check coverage delta
jq -e '.tdd_cycles[-1].coverage_delta' runs/<run-id>/executor_report.json

# Check executor report complete
jq -e '.tdd_cycles[-1].tdd_phases.red.test_file' runs/<run-id>/executor_report.json

# Check G1 passed
grep -q "G1_implementation - PASSED" runs/<run-id>/state/GATES_LEDGER.md
```

**If validation fails:**
1. Log error in `GATES_LEDGER.md`: `[timestamp] G2_validation - REJECTED - validator - Reason: <error>`
2. Update `SESSION_HANDOFF.json` with `status: "rejected"`
3. Escalate to human for Executor remediation

---

### Common Handoff Failures (H2)

| Failure | Detection | Resolution |
|---------|-----------|------------|
| **Missing RED evidence** | test_output_red.txt not found | Validator rejects, Executor must provide RED proof |
| **Tests not actually passing** | Validator re-runs tests, sees failures | Validator fails G2, Executor must fix |
| **Coverage delta negative** | coverage_delta shows "-1.2%" | Validator fails G2, Executor must add tests |
| **Incomplete commands** | commands_run missing lint or type check | Validator runs missing commands, notes in report |
| **DoD unmet** | Critical DoD criteria not addressed | Validator fails G2 or escalates if ambiguous |

---

## H3: Validator → System/Planner

### Context

**When:** After Validator completes G2 (Validation Gate)  
**Why:** System needs verdict to proceed to G3 (production) OR Planner needs to assign next task  
**Human Role:** Reads `validator_report.json`, decides next action based on verdict

---

### Validator's Obligations

The Validator **MUST** provide:

| Obligation | Artifact | Verification |
|------------|----------|--------------|
| ✅ **Comprehensive verdict** | `validator_report.json` | `status` field: pass/fail/needs_remediation |
| ✅ **Verification results** | `validator_report.json` → `verification_results` | 10-point checklist results |
| ✅ **Security scan** | `artifacts/validator/security_scan.json` | OWASP or equivalent scan results |
| ✅ **Mutation score** | `artifacts/validator/mutation_report.txt` | Mutation testing results |
| ✅ **Remediation plan** (if failed) | `validator_report.json` → `remediation_plan` | Specific steps to fix issues |
| ✅ **Approval decision** | `validator_report.json` → `approval_for_next_task` | Boolean: ready for next task? |
| ✅ **Gate status** | `state/GATES_LEDGER.md` | Shows "G2_validation - PASSED/FAILED" |
| ✅ **Handoff logged** | `state/SESSION_HANDOFF.json` | Updated with verdict |

---

### System/Planner's Assumptions

The System/Planner **CAN ASSUME**:

1. ✅ Validation was **comprehensive** (10-point checklist)
2. ✅ Validator **independently verified** (didn't just trust Executor)
3. ✅ Security scan was **actually run** (artifact exists)
4. ✅ Mutation testing was performed (or N/A justified)
5. ✅ Verdict is **actionable** (pass/fail with clear reasoning)

---

### Handoff Payload (H3)

**File:** `state/SESSION_HANDOFF.json`

```json
{
  "run_id": "20250929-134215-8b6f8b9a-...",
  "handoff_id": "H3",
  "from_agent": "validator",
  "to_agent": "system",
  "handoff_time": "2025-09-29T15:00:00Z",
  "gate_transition": "G2_passed → G3_pending",
  
  "payload": {
    "task_id": "T001",
    "verdict": "pass",
    "summary": "All quality gates passed. TDD compliance verified, security scan clean, mutation score 91.3%, coverage 94.2%. Minor note: coverage 0.8% below target (95%) but acceptable for this task.",
    
    "files_to_review": [
      "validator_report.json",
      "artifacts/validator/security_scan.json",
      "artifacts/validator/mutation_report.txt"
    ],
    
    "verification_summary": {
      "tdd_compliance": "✅ PASS - RED→GREEN evidence verified",
      "tests": "✅ PASS - All 47 tests passing",
      "coverage": "✅ PASS - 94.2% (target 90%, note: DoD target 95% unmet by 0.8%)",
      "mutation": "✅ PASS - 91.3% (target 85%)",
      "security": "✅ PASS - 0 vulnerabilities found (Bandit + Safety)",
      "lint": "✅ PASS - No errors",
      "type_check": "✅ PASS - No errors",
      "accessibility": "⚪ N/A - No UI changes",
      "dod_checklist": "⚠️ PARTIAL - 3/4 met (coverage 94.2% vs 95% target)",
      "intent_alignment": "✅ PASS - Code matches task goal"
    },
    
    "approval_for_next_task": true,
    "next_action": "Mark CURRENT_TASK complete, move to G3 (production-ready), Planner can assign T002",
    
    "notes": "Coverage slightly below DoD target (95%) but above system threshold (90%). Recommend accepting and addressing in future tasks if coverage becomes critical."
  },
  
  "verification_checklist": [
    "validator_report.json exists with verdict",
    "Security scan artifact exists",
    "Mutation report artifact exists (or N/A justified)",
    "Verification results cover all 10 checklist items",
    "GATES_LEDGER shows G2 verdict"
  ]
}
```

---

### Handoff Validation

**System MUST verify before proceeding to G3:**

```bash
# Check validator report exists
test -f runs/<run-id>/validator_report.json

# Check verdict
jq -e '.verdicts[-1].status' runs/<run-id>/validator_report.json

# Check security scan performed
test -f runs/<run-id>/artifacts/validator/security_scan.json

# Check G2 verdict
grep -E "G2_validation - (PASSED|FAILED)" runs/<run-id>/state/GATES_LEDGER.md
```

**Based on verdict:**
- **PASS:** Proceed to G3 (production-ready checks)
- **PASS_WITH_NOTES:** Proceed to G3, log notes for review
- **FAIL:** Return to Executor for remediation (iteration_count++)
- **ESCALATION:** Human review required

---

### Common Handoff Failures (H3)

| Failure | Detection | Resolution |
|---------|-----------|------------|
| **Incomplete verification** | validator_report missing checklist items | Human reviews, Validator re-runs |
| **Security scan not run** | security_scan.json missing | Human rejects, Validator must scan |
| **Vague remediation plan** | remediation_plan is "fix bugs" | Human clarifies, Validator refines |
| **Conflicting signals** | Verdict "pass" but critical DoD unmet | Human reviews, likely changes to "fail" |

---

## Handoff Rejection Protocol

### When to Reject a Handoff

Any receiving agent **MUST reject** if:

1. ❌ Required artifacts missing
2. ❌ Gate status incorrect (e.g., G0 not passed before H1)
3. ❌ Verification checklist fails (see payload schemas)
4. ❌ Critical assumptions violated (e.g., baseline tests broken)

### Rejection Process

1. **Log rejection** in `GATES_LEDGER.md`:
   ```
   [2025-09-29T14:10:00Z] G1_implementation - REJECTED - executor - Reason: TDD plan missing from CURRENT_TASK.json
   ```

2. **Update SESSION_HANDOFF.json**:
   ```json
   {
     "status": "rejected",
     "rejection_reason": "TDD plan incomplete (refactor step missing)",
     "rejected_by": "executor",
     "rejected_at": "2025-09-29T14:10:00Z"
   }
   ```

3. **Escalate to human**:
   - Create `artifacts/escalation/handoff_rejection_H1.md`
   - Document issue and required fix
   - Human coordinates with sending agent to remediate

4. **Retry after fix**:
   - Sending agent addresses issue
   - Updates artifacts and SESSION_HANDOFF.json
   - Receiving agent re-validates and accepts

---

## State Machine: Handoff Lifecycle

```
┌─────────────────────────────────────────────────┐
│             HANDOFF LIFECYCLE                   │
└─────────────────────────────────────────────────┘

[AGENT COMPLETES WORK]
         │
         ↓
[UPDATES SESSION_HANDOFF.json]
    - next_agent: "<receiver>"
    - payload: {...}
    - verification_checklist: [...]
         │
         ↓
[HUMAN READS SESSION_HANDOFF]
         │
         ↓
[HUMAN INVOKES RECEIVER AGENT]
         │
         ↓
[RECEIVER VALIDATES HANDOFF]
         │
    ┌────┴────┐
    │         │
   PASS     REJECT
    │         │
    ↓         ↓
[ACCEPT]  [LOG REJECTION]
    │         │
    │         ↓
    │   [ESCALATE TO HUMAN]
    │         │
    │         ↓
    │   [SENDER REMEDIATES]
    │         │
    └─────────┘
         │
         ↓
[RECEIVER STARTS WORK]
```

---

## Best Practices

### For Sending Agents

1. ✅ **Complete all obligations** before handoff (see tables above)
2. ✅ **Update SESSION_HANDOFF.json** with clear payload
3. ✅ **Log gate completion** in GATES_LEDGER.md
4. ✅ **Add artifacts to EVIDENCE_LOG** with hashes
5. ✅ **Provide verification checklist** for receiver to validate

### For Receiving Agents

1. ✅ **Validate handoff first** (run verification commands)
2. ✅ **Reject if incomplete** (don't assume sender did their job)
3. ✅ **Log acceptance/rejection** in GATES_LEDGER.md
4. ✅ **Start with clean state** (don't carry forward sender's errors)
5. ✅ **Re-run critical commands** (don't just trust sender's output)

### For Humans

1. ✅ **Read SESSION_HANDOFF.json** before invoking next agent
2. ✅ **Check verification_checklist** manually if unsure
3. ✅ **Don't force handoff** if receiver rejects (address root cause)
4. ✅ **Review escalations promptly** (blocked agents waste time)
5. ✅ **Update ROADMAP.md** as workflow evolves

---

## Handoff Metrics

### Handoff Success Rate

| Metric | Target | Formula |
|--------|--------|---------|
| **H1 Accept Rate** | ≥95% | (H1 accepted) / (H1 attempted) |
| **H2 Accept Rate** | ≥90% | (H2 accepted) / (H2 attempted) |
| **H3 Accept Rate** | ≥85% | (H3 accepted) / (H3 attempted) |

### Handoff Latency

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Human Handoff Time** | <5 minutes | Time from agent completion to human invoking next agent |
| **Validation Time** | <2 minutes | Time for receiver to validate handoff |

---

## Troubleshooting

### Handoff Rejected Repeatedly

**Symptom:** Same handoff rejected 2+ times

**Solutions:**
1. Human review: Are requirements clear?
2. Sender review: Is sender missing context?
3. Receiver review: Is receiver too strict?
4. Update specs: Clarify ambiguous criteria

### Human Forgets to Update SESSION_HANDOFF

**Symptom:** Agent starts work without checking handoff

**Solutions:**
1. Agents check SESSION_HANDOFF.json at startup
2. Agents reject if handoff status != "ready"
3. Add human checklist to Bridge Protocol

### Artifacts Missing After Handoff

**Symptom:** Receiver can't find expected artifacts

**Solutions:**
1. Check EVIDENCE_LOG.md for artifact paths
2. Verify file permissions (readable by all agents)
3. Check disk space (filesystem full?)
4. Review sender's logs for write errors

---

## Related Documentation

- [State Specification](state_specification.md) - SESSION_HANDOFF.json schema details
- [Gate Framework](gate_framework.md) - Gate entry/exit criteria
- [Human Bridge Protocol](Human_Bridge_Protocol.md) - How to invoke agents
- [Agent Prompts](prompts/) - Planner, Executor, Validator prompts

---

## Changelog

- **1.0.0** (2025-01-XX): Initial H3A handoff contracts
  - H1: Planner → Executor
  - H2: Executor → Validator
  - H3: Validator → System/Planner
  - Rejection protocol and validation commands
  - Handoff metrics and troubleshooting