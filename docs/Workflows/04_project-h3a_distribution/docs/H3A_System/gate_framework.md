# H3A Gate Framework
**Version:** 1.0.0  
**Last Updated:** 2025-01-XX

---

## Purpose

The H3A Gate Framework enforces **evidence-based progression** through the software development lifecycle. Each gate represents a quality checkpoint that **cannot be skipped** and **requires artifact proof** to pass.

**Core Principle:** No artifact = No progress

---

## Philosophy

### Why Gates?

Traditional agile workflows rely on human judgment ("looks good to me"). In AI-assisted development with autonomous agents, we need **objective, verifiable criteria** to prevent:

- ❌ Skipping tests ("I'll add them later")
- ❌ Deploying untested code
- ❌ Missing security scans
- ❌ Incomplete documentation
- ❌ Technical debt accumulation

**Gates enforce discipline** by making quality checks **mandatory and auditable**.

---

## Gate Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        H3A GATE FRAMEWORK                       │
│                                                                 │
│  G0: Planning → G1: Implementation → G2: Validation → G3: Prod │
│     Planner         Executor            Validator       System │
└─────────────────────────────────────────────────────────────────┘
```

| Gate | Owner | Purpose | Duration | Risk Level |
|------|-------|---------|----------|------------|
| **G0: Planning** | Planner | Strategic decomposition, TDD planning | 15-30 min | Low |
| **G1: Implementation** | Executor | TDD execution (RED→GREEN→REFACTOR) | 30-90 min | Medium |
| **G2: Validation** | Validator | Comprehensive quality verification | 15-30 min | High |
| **G3: Production-Ready** | System | Final checks, deployment readiness | 5-10 min | Critical |

---

## Gate Definitions

### G0: Planning Gate

**Owner:** Planner  
**Purpose:** Ensure task is well-defined, decomposed, and has a TDD strategy  
**Risk if skipped:** Poorly scoped work, wasted implementation effort

#### Entry Criteria

| Criterion | Verification Method | Artifact |
|-----------|---------------------|----------|
| ✅ Task brief exists | Check `state/ROADMAP.md` contains task description | `ROADMAP.md` |
| ✅ Run initialized | `h3a_init.py` completed successfully | `state.json` |
| ✅ Previous task complete (if any) | Check `CURRENT_TASK.json` shows prior task status: `complete` | `CURRENT_TASK.json` |

#### Exit Criteria

| Criterion | Verification Method | Artifact |
|-----------|---------------------|----------|
| ✅ Strategic plan documented | `ROADMAP.md` contains "Overall Strategy" section with approach and risks | `ROADMAP.md` |
| ✅ Task decomposed | `ROADMAP.md` has numbered task list (T001, T002, ...) with descriptions | `ROADMAP.md` |
| ✅ Current task defined | `CURRENT_TASK.json` populated with task_id, goal, files_affected, DoD | `CURRENT_TASK.json` |
| ✅ TDD plan created | `CURRENT_TASK.json` has tdd_plan.red, tdd_plan.green, tdd_plan.refactor filled | `CURRENT_TASK.json` |
| ✅ Definition of Done specified | `CURRENT_TASK.json` has ≥3 measurable DoD criteria | `CURRENT_TASK.json` |
| ✅ Planner report generated | `planner_report.json` exists with research findings and strategy | `planner_report.json` |
| ✅ Gate logged | `GATES_LEDGER.md` shows G0 PASSED event with timestamp | `GATES_LEDGER.md` |

#### Artifacts Required

- ✅ `state/ROADMAP.md` (updated or created)
- ✅ `state/CURRENT_TASK.json` (first task filled)
- ✅ `planner_report.json` (planning summary)
- ✅ `artifacts/planner/` (optional: diagrams, research notes)

#### Verification Commands

```bash
# Check ROADMAP exists and has task queue
grep -q "## Task Decomposition" runs/<run-id>/state/ROADMAP.md

# Check CURRENT_TASK has TDD plan
jq -e '.tdd_plan.red != null and .tdd_plan.green != null' runs/<run-id>/state/CURRENT_TASK.json

# Check gate logged
grep -q "G0_planning - PASSED" runs/<run-id>/state/GATES_LEDGER.md
```

#### Common Failures

| Failure | Symptom | Remediation |
|---------|---------|-------------|
| Vague task description | CURRENT_TASK.goal is too broad ("Make it better") | Planner refines goal with measurable outcomes |
| Missing TDD plan | tdd_plan fields are null or generic | Planner defines RED/GREEN/REFACTOR steps explicitly |
| Unrealistic scope | Task affects >10 files or >500 LOC | Planner splits into smaller tasks |
| No Definition of Done | DoD list empty or has <3 criteria | Planner adds measurable success criteria |

---

### G1: Implementation Gate

**Owner:** Executor  
**Purpose:** Ensure TDD discipline followed, all tests passing, coverage increased  
**Risk if skipped:** Untested code, broken builds, regression bugs

#### Entry Criteria

| Criterion | Verification Method | Artifact |
|-----------|---------------------|----------|
| ✅ G0 passed | `GATES_LEDGER.md` shows G0_planning PASSED | `GATES_LEDGER.md` |
| ✅ Task assigned to Executor | `SESSION_HANDOFF.json` shows handoff_to: "executor" | `SESSION_HANDOFF.json` |
| ✅ TDD plan exists | `CURRENT_TASK.json` has tdd_plan filled | `CURRENT_TASK.json` |
| ✅ Baseline tests passing | Run `pytest` or equivalent, exit code 0 | Command output |

#### Exit Criteria

| Criterion | Verification Method | Artifact |
|-----------|---------------------|----------|
| ✅ **RED phase documented** | RED test output saved showing initial test failure | `artifacts/executor/test_output_red.txt` |
| ✅ **GREEN phase documented** | GREEN test output saved showing all tests passing | `artifacts/executor/test_output_green.txt` |
| ✅ REFACTOR phase completed | Code cleaned up, tests still passing | `artifacts/executor/test_output_refactor.txt` (optional) |
| ✅ All tests passing | `pytest` or equivalent exits with code 0 | Command output in `executor_report.json` |
| ✅ Coverage increased | Coverage delta ≥ +0.1% OR absolute ≥ 90% | `artifacts/executor/coverage_delta.json` |
| ✅ No lint errors | `make lint` or equivalent exits with code 0 | Command output in `executor_report.json` |
| ✅ Type checks passing | `mypy` or equivalent exits with code 0 | Command output in `executor_report.json` |
| ✅ DoD checklist addressed | All DoD items from CURRENT_TASK checked | `executor_report.json` |
| ✅ Executor report generated | `executor_report.json` has TDD evidence and DoD status | `executor_report.json` |
| ✅ Gate logged | `GATES_LEDGER.md` shows G1 PASSED event | `GATES_LEDGER.md` |

#### Artifacts Required

- ✅ `artifacts/executor/test_output_red.txt` (RED phase proof)
- ✅ `artifacts/executor/test_output_green.txt` (GREEN phase proof)
- ✅ `artifacts/executor/coverage_delta.json` (coverage increase proof)
- ✅ `executor_report.json` (TDD cycle summary, DoD checklist)

#### Verification Commands

```bash
# Check RED phase evidence exists
test -f runs/<run-id>/artifacts/executor/test_output_red.txt

# Check GREEN phase evidence exists
test -f runs/<run-id>/artifacts/executor/test_output_green.txt

# Check all tests passing
jq -e '.tdd_cycles[-1].tdd_phases.green.test_output' runs/<run-id>/executor_report.json

# Check coverage delta positive
jq -e '.tdd_cycles[-1].coverage_delta' runs/<run-id>/executor_report.json | grep -q "+"

# Check gate logged
grep -q "G1_implementation - PASSED" runs/<run-id>/state/GATES_LEDGER.md
```

#### Common Failures

| Failure | Symptom | Remediation |
|---------|---------|-------------|
| Missing RED phase | No test_output_red.txt artifact | Executor writes failing test first, saves output |
| Tests not passing | GREEN phase has failures | Executor fixes implementation until all tests pass |
| Coverage decreased | coverage_delta shows negative value | Executor adds tests for uncovered code paths |
| Lint failures | make lint exits with non-zero code | Executor fixes style issues |
| Incomplete DoD | executor_report shows unmet DoD criteria | Executor addresses missing criteria or escalates |

#### TDD Non-Negotiables

1. **RED phase MUST exist** - No "I'll add tests later"
2. **GREEN phase MUST follow RED** - Chronological order matters
3. **Coverage MUST NOT decrease** - Absolute minimum requirement
4. **Tests MUST be meaningful** - No `assert True` placeholders

---

### G2: Validation Gate

**Owner:** Validator  
**Purpose:** Comprehensive quality verification (TDD, security, coverage, mutation, DoD)  
**Risk if skipped:** Vulnerabilities, low-quality tests, production incidents

#### Entry Criteria

| Criterion | Verification Method | Artifact |
|-----------|---------------------|----------|
| ✅ G1 passed | `GATES_LEDGER.md` shows G1_implementation PASSED | `GATES_LEDGER.md` |
| ✅ Task assigned to Validator | `SESSION_HANDOFF.json` shows handoff_to: "validator" | `SESSION_HANDOFF.json` |
| ✅ Executor report exists | `executor_report.json` is present and valid JSON | `executor_report.json` |

#### Exit Criteria

| Criterion | Verification Method | Artifact |
|-----------|---------------------|----------|
| ✅ **TDD compliance verified** | RED→GREEN evidence files exist and show progression | Validator checks artifacts |
| ✅ **Tests quality verified** | All tests passing, no skipped tests without justification | Test output analysis |
| ✅ **Coverage verified** | Coverage ≥ threshold (default 90%) OR delta ≥ +0.1% | `coverage_delta.json` |
| ✅ **Mutation score verified** | Mutation score ≥ threshold (default 85%) | `artifacts/validator/mutation_report.txt` |
| ✅ **Security scan passed** | OWASP scan clean OR vulnerabilities documented/accepted | `artifacts/validator/security_scan.json` |
| ✅ **Lint passed** | No lint errors OR documented exceptions | Lint output check |
| ✅ **Type check passed** | No mypy/pyright errors OR documented exceptions | Type check output |
| ✅ **Accessibility verified** | A11y scan passed (if UI changes) OR N/A documented | `artifacts/validator/a11y_report.json` |
| ✅ **DoD verified** | All DoD criteria met OR exceptions justified | DoD checklist analysis |
| ✅ **Intent alignment verified** | Code matches task goal (human-readable check) | Validator notes |
| ✅ Validator report generated | `validator_report.json` has comprehensive verification results | `validator_report.json` |
| ✅ Gate logged | `GATES_LEDGER.md` shows G2 verdict (PASSED/FAILED) | `GATES_LEDGER.md` |

#### Artifacts Required

- ✅ `validator_report.json` (comprehensive verification)
- ✅ `artifacts/validator/security_scan.json` (OWASP or equivalent)
- ✅ `artifacts/validator/mutation_report.txt` (mutation testing results)
- ✅ `artifacts/validator/a11y_report.json` (if UI changes)
- ✅ `artifacts/validator/verification_evidence/` (re-run command outputs)

#### Verification Commands

```bash
# Check validator report exists
test -f runs/<run-id>/validator_report.json

# Check validation status
jq -e '.verdicts[-1].status == "pass"' runs/<run-id>/validator_report.json

# Check security scan performed
test -f runs/<run-id>/artifacts/validator/security_scan.json

# Check mutation score
jq -e '.verdicts[-1].verification_results.mutation.score' runs/<run-id>/validator_report.json

# Check gate verdict
grep -E "G2_validation - (PASSED|FAILED)" runs/<run-id>/state/GATES_LEDGER.md
```

#### Validation Checklist (10-Point)

| # | Check | Pass Criteria | Artifact |
|---|-------|---------------|----------|
| 1 | **TDD Compliance** | RED→GREEN evidence exists and shows test failure → success | `test_output_red.txt`, `test_output_green.txt` |
| 2 | **Test Quality** | All tests passing, no skipped tests (or justified), assertions present | Test output analysis |
| 3 | **Coverage** | ≥90% absolute OR delta ≥+0.1% | `coverage_delta.json` |
| 4 | **Mutation Score** | ≥85% mutation score | `mutation_report.txt` |
| 5 | **Security** | OWASP scan clean (0 high/critical vulnerabilities) | `security_scan.json` |
| 6 | **Code Quality** | Lint passing, type checks passing | Command outputs |
| 7 | **Accessibility** | A11y scan passing (if UI) or N/A | `a11y_report.json` or N/A note |
| 8 | **DoD Completeness** | All DoD criteria met or justified exceptions | DoD analysis |
| 9 | **Intent Alignment** | Code matches task goal, no scope creep | Human judgment |
| 10 | **Command Verification** | Re-run key commands (tests, lint), verify outputs | Fresh command outputs |

**Pass Requirement:** 10/10 OR 9/10 with documented exception

#### Common Failures

| Failure | Symptom | Remediation |
|---------|---------|-------------|
| Missing RED evidence | test_output_red.txt not found | FAIL gate, Executor must provide RED phase proof |
| Low mutation score | <85% mutants killed | PARTIAL PASS, note in validator_report, recommend improvement |
| Security vulnerability | OWASP scan shows high/critical CVE | FAIL gate, Executor must patch or document acceptance |
| Coverage drop | Coverage decreased from baseline | FAIL gate, Executor must add tests |
| Incomplete DoD | Key DoD criteria unmet | FAIL gate, Executor must address or escalate |
| Intent mismatch | Code doesn't match task goal | FAIL gate, Planner/Executor collaboration needed |

#### Validation Status Types

- **PASS:** All checks passed, approve for production
- **PASS_WITH_NOTES:** Minor issues noted but not blocking (e.g., mutation score 83% vs target 85%)
- **FAIL:** Blocking issues found, remediation required
- **ESCALATION:** 2 iterations exhausted, human review needed

---

### G3: Production-Ready Gate

**Owner:** System (automated checks)  
**Purpose:** Final pre-deployment verification  
**Risk if skipped:** Deploy broken code to production

#### Entry Criteria

| Criterion | Verification Method | Artifact |
|-----------|---------------------|----------|
| ✅ G2 passed | `GATES_LEDGER.md` shows G2_validation PASSED | `GATES_LEDGER.md` |
| ✅ All artifacts logged | `EVIDENCE_LOG.md` has entries for all required artifacts | `EVIDENCE_LOG.md` |
| ✅ Hash verification | All artifact hashes in EVIDENCE_LOG match actual files | Hash check script |

#### Exit Criteria

| Criterion | Verification Method | Artifact |
|-----------|---------------------|----------|
| ✅ Git clean | No uncommitted changes (or documented) | `git status` |
| ✅ CI passing | CI pipeline green (if available) | CI status check |
| ✅ Dependencies audited | No high/critical vulnerabilities in dependencies | `pip-audit` or equivalent |
| ✅ Documentation updated | README, CHANGELOG updated (if applicable) | File modification check |
| ✅ Deployment checklist | Deployment prerequisites met (env vars, secrets, etc.) | Manual checklist |
| ✅ Rollback plan | Rollback procedure documented | Deployment doc |
| ✅ Gate logged | `GATES_LEDGER.md` shows G3 PASSED | `GATES_LEDGER.md` |

#### Artifacts Required

- ✅ All previous gate artifacts
- ✅ `artifacts/system/pre_deploy_checklist.md`
- ✅ `artifacts/system/rollback_plan.md`

#### Verification Commands

```bash
# Check all gates passed
grep -q "G0_planning - PASSED" runs/<run-id>/state/GATES_LEDGER.md
grep -q "G1_implementation - PASSED" runs/<run-id>/state/GATES_LEDGER.md
grep -q "G2_validation - PASSED" runs/<run-id>/state/GATES_LEDGER.md

# Check git clean
git diff --exit-code

# Check CI passing (if CI_URL set)
# curl -s $CI_URL/status | jq -e '.status == "success"'

# Verify all artifact hashes
python scripts/verify_evidence_hashes.py runs/<run-id>/state/EVIDENCE_LOG.md
```

#### Common Failures

| Failure | Symptom | Remediation |
|---------|---------|-------------|
| Uncommitted changes | `git status` shows modified files | Commit changes or add to `.gitignore` |
| CI failing | CI pipeline red | Fix failing CI checks |
| Dependency vulnerabilities | `pip-audit` finds CVEs | Update dependencies or document acceptance |
| Missing documentation | README not updated | Update docs with new features/changes |

---

## Gate Lifecycle & State Machine

### Gate Progression
```
G0_pending ──→ G0_in_progress ──→ G0_passed ──→ G1_pending ──→ ...
                     │                               
                     └──→ G0_failed ──→ remediation (iteration_count++)
                                 │
                        [iteration_count < 2?]
                                 │
                        YES ──→ back to G0_in_progress
                                 │
                        NO ──→ escalation_required
```

### Iteration Limits

**Rule:** Max 2 iterations per gate before escalation

**Rationale:**
- 1st attempt: Initial implementation
- 2nd attempt: Fix issues found in validation
- 3rd+ attempts: Likely architectural issue, needs human review

**Escalation Triggers:**
- Gate failed twice
- Architectural blocker (e.g., dependency conflict)
- Ambiguous requirements
- Resource limitations (time, compute, expertise)

---

## Evidence Protocol

### Artifact Requirements by Gate

| Gate | Required Artifacts | Optional Artifacts |
|------|--------------------|--------------------|
| **G0** | ROADMAP.md, CURRENT_TASK.json, planner_report.json | Architecture diagrams, research notes |
| **G1** | test_output_red.txt, test_output_green.txt, coverage_delta.json, executor_report.json | Refactor logs, performance benchmarks |
| **G2** | validator_report.json, security_scan.json, mutation_report.txt | A11y report, manual test results |
| **G3** | pre_deploy_checklist.md, rollback_plan.md | Deployment logs, monitoring setup |

### Hash Verification

All artifacts in `EVIDENCE_LOG.md` must include SHA-256 hash (first 16 chars):

```markdown
- `artifacts/executor/test_output_green.txt` - [hash:e4f6c1d92a8b3f57] - 2025-09-29T14:30:00Z - GREEN phase evidence
```

**Verification:**
```bash
sha256sum artifacts/executor/test_output_green.txt | cut -c1-16
# Output: e4f6c1d92a8b3f57 (must match EVIDENCE_LOG.md)
```

---

## Human Oversight Points

### Manual Reviews (Optional but Recommended)

| Gate | Review Point | Reviewer Role |
|------|--------------|---------------|
| G0 | Task decomposition reasonable? | Tech Lead / Product Owner |
| G1 | Tests meaningful, not just passing? | Senior Engineer |
| G2 | Security/quality acceptable? | Security Engineer / QA |
| G3 | Ready for production? | Release Manager |

### Escalation Protocol

**When to escalate:**
1. Gate failed 2 times (iteration_count = 2)
2. Architectural blocker discovered
3. Requirements ambiguous or conflicting
4. Resource constraints (time, compute)

**Escalation Process:**
1. Validator sets `status: "escalation_required"` in `validator_report.json`
2. Update `GATES_LEDGER.md` with ESCALATION event
3. Create `artifacts/escalation/issue_<task-id>.md` with:
   - Problem description
   - Failed attempts summary
   - Recommended solution (if any)
4. Human reviews and provides guidance
5. Update `CURRENT_TASK.json` with clarifications
6. Reset `iteration_count = 0` and retry

---

## Gate Metrics & KPIs

### Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **G0 Pass Rate** | ≥95% first attempt | (G0 passed 1st try) / (total G0 attempts) |
| **G1 Pass Rate** | ≥80% first attempt | (G1 passed 1st try) / (total G1 attempts) |
| **G2 Pass Rate** | ≥70% first attempt | (G2 passed 1st try) / (total G2 attempts) |
| **Escalation Rate** | ≤5% of tasks | (escalations) / (total tasks) |
| **Avg Gate Time** | G0: 20min, G1: 60min, G2: 25min | Sum(gate duration) / count |

### Quality Metrics

| Metric | Target | Gate |
|--------|--------|------|
| **Coverage** | ≥90% | G1, G2 |
| **Mutation Score** | ≥85% | G2 |
| **Security Scan** | 0 high/critical CVEs | G2 |
| **Lint Passing** | 100% | G1, G2 |
| **Type Check** | 0 errors | G1, G2 |

---

## Best Practices

### For Planner (G0)

1. ✅ **Decompose small:** 1 task = 1-3 files, <200 LOC changed
2. ✅ **Define TDD plan:** Explicit RED/GREEN/REFACTOR steps
3. ✅ **Set measurable DoD:** "Coverage ≥95%" not "Good coverage"
4. ✅ **Document risks:** Note potential blockers upfront
5. ✅ **Link dependencies:** Reference prior task IDs if dependent

### For Executor (G1)

1. ✅ **RED phase first:** Write failing test, save output to artifact
2. ✅ **Minimal GREEN:** Simplest implementation to pass test
3. ✅ **Refactor safely:** Tests still passing after cleanup
4. ✅ **Save evidence:** test_output_red.txt, test_output_green.txt
5. ✅ **Check DoD:** Address all DoD criteria from CURRENT_TASK.json

### For Validator (G2)

1. ✅ **Verify, don't trust:** Re-run commands to confirm outputs
2. ✅ **Check RED→GREEN:** Ensure test actually failed initially
3. ✅ **Run security scan:** `bandit`, `safety`, or OWASP ZAP
4. ✅ **Run mutation testing:** `mutmut`, `cosmic-ray`, or equivalent
5. ✅ **Check intent:** Does code match task goal?
6. ✅ **Document findings:** Clear pass/fail reasons in validator_report.json

### For System (G3)

1. ✅ **Automate checks:** CI integration, pre-commit hooks
2. ✅ **Verify hashes:** Artifact integrity before deploy
3. ✅ **Test rollback:** Ensure rollback plan actually works
4. ✅ **Monitor post-deploy:** Set up alerts for new code

---

## Compliance Mapping

| Framework | Gate | Requirement | Artifact |
|-----------|------|-------------|----------|
| **OWASP ASVS** | G2 | Security testing (V10) | `security_scan.json` |
| **ISO 42001** | All | AI system traceability | `GATES_LEDGER.md`, `EVIDENCE_LOG.md` |
| **SOC 2** | All | Audit logs | `state.json`, gate logs |
| **NIST CSF** | G2 | Vulnerability management | `security_scan.json` |
| **EU AI Act** | All | Risk management, transparency | Gate evidence, escalation logs |

---

## Troubleshooting

### Gate Stuck in "in_progress"

**Symptom:** Gate shows "in_progress" for >2 hours

**Solutions:**
1. Check if agent is still running (process alive?)
2. Review agent logs for errors
3. Check if waiting for external dependency (network, API)
4. Manually update `GATES_LEDGER.md` to FAILED if agent crashed

### Gate Passed But Artifacts Missing

**Symptom:** `GATES_LEDGER.md` shows PASSED but `EVIDENCE_LOG.md` missing entries

**Solutions:**
1. Verify artifacts actually exist in filesystem
2. Add missing entries to `EVIDENCE_LOG.md` with hashes
3. If artifacts truly missing, revert gate to FAILED and re-run

### Hash Mismatch

**Symptom:** Artifact hash in `EVIDENCE_LOG.md` doesn't match file

**Solutions:**
1. Recompute hash: `sha256sum <file> | cut -c1-16`
2. If file modified: Update hash in EVIDENCE_LOG and note reason
3. If tampering suspected: Investigate, possibly revert and re-run

---

## Related Documentation

- [State Specification](state_specification.md) - State file schemas
- [Handoff Contracts](handoff_contracts.md) - Agent-to-agent transitions
- [Human Bridge Protocol](Human_Bridge_Protocol.md) - How to invoke agents
- [Validator Prompt](prompts/validator_prompt.md) - G2 validation details

---

## Changelog

- **1.0.0** (2025-01-XX): Initial H3A gate framework
  - 4-gate system (G0-G3)
  - Evidence-based progression
  - Iteration limits and escalation protocol
  - TDD enforcement at G1/G2
  - Comprehensive validation checklist (10-point)