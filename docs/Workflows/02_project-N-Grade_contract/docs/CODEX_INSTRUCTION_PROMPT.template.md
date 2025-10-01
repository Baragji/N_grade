# CONTRACT-BASED DELIVERY INSTRUCTION

**COPY THIS ENTIRE PROMPT AND SEND TO YOUR AI ASSISTANT →**

---

## MANDATORY CONTRACT ENFORCEMENT

You are receiving a **CONTRACT-BASED DELIVERY REQUEST** with **ZERO TOLERANCE** for incomplete work.

### Critical Information

**Contract File:**
```
[INSERT YOUR CONTRACT PATH HERE]
Example: contracts/N-Grade/contracts/my_deliverable.contract.json
```

**Validation Command:**
```bash
python scripts/validate_contract.py [INSERT CONTRACT PATH] \
  --report-path _reports/[YOUR_DELIVERABLE]_validation.json
```

**Acceptance Criteria:**
- Validator MUST exit with code `0` (ACCEPTED)
- If exit code is `1` (REJECTED), your delivery will be sent back for fixes
- NO EXCEPTIONS

---

## WHAT YOU MUST DO

### 1. Read the Contract

Open and thoroughly read:
```
[INSERT CONTRACT PATH]
```

Pay special attention to:
- `deliverables[].quality_gates` (MANDATORY requirements)
- `forbidden_patterns` (patterns that trigger AUTOMATIC REJECTION)
- `required_patterns` (content that MUST appear with minimum occurrences)
- `definition_of_done` (ALL must be `true` for acceptance)

### 2. Understand Quality Gates

Your deliverable will be checked for:

#### ✅ Line Count
- **Minimum:** [INSERT MIN] lines
- **Maximum:** [INSERT MAX] lines
- **What this means:** [EXPLAIN YOUR EXPECTATIONS]

#### ✅ Required Sections
All required headers MUST exist:
- [LIST YOUR REQUIRED SECTIONS]
- Example: `## Overview`, `## Implementation`, `## Success Criteria`

#### ❌ Forbidden Patterns (ZERO TOLERANCE)
Any occurrence of these triggers AUTOMATIC REJECTION:
- `TODO` - NO TODOs
- `TBD` - NO TBDs
- `FIXME` - NO FIXMEs
- `...` - NO ELLIPSIS (indicates omitted content)
- `(template)` - NO TEMPLATE PLACEHOLDERS
- `[FILL IN]` - NO FILL-IN MARKERS

#### ✅ Required Patterns (Minimum Occurrences)
Your delivery MUST contain AT LEAST:

| Pattern | Minimum | Purpose |
|---------|---------|---------|
| `## ` (level 2 headers) | [N] | Major sections |
| `### ` (level 3 headers) | [N] | Subsections |
| Success criteria | [N] | Measurable outcomes |
| Code blocks (```) | [N] | Implementation examples |
| Evidence paths | [N] | Traceability |

#### ✅ Structural Requirements
- **Code blocks:** ≥[N]
- **Tables:** ≥[N]
- **Lists:** ≥[N]
- **No duplicate sections:** Headers must be unique

### 3. Content Guidelines

[INSERT SPECIFIC CONTENT REQUIREMENTS HERE]

Example:
- Each section MUST have 3-5 paragraph overview
- Include numbered implementation steps with sub-bullets
- Provide at least one code example per major section
- Define success criteria with numeric thresholds
- Reference evidence file paths

### 4. Code Example Standards

All code blocks MUST:
- Be syntactically valid
- Include inline comments
- Show realistic values (not placeholders like `YOUR_VALUE_HERE`)
- Demonstrate the specific feature being discussed

**Example (GOOD):**
```python
# [RELEVANT COMMENT]
import relevant_library

def example_function(param: str) -> bool:
    """Clear docstring."""
    result = relevant_library.process(param)
    return result is not None
```

**Example (BAD - WILL BE REJECTED):**
```python
# TODO: Add implementation here
```

### 5. Metric Standards

All numeric criteria MUST:
- Specify exact thresholds (e.g., `≥95%` not "high")
- Include units (%, ms, MB, etc.)
- State measurement method
- Reference evidence file where metric is captured

**Example (GOOD):**
```
Success criteria:
- Test coverage ≥95% (measured by pytest-cov)
- Response time <100ms (measured by benchmark)
- Zero data loss (verified by integration tests)
```

**Example (BAD - WILL BE REJECTED):**
```
Success criteria:
- High test coverage
- Fast response
- Reliable storage
```

### 6. Prohibited Shortcuts

DO NOT:
- ❌ Condense multiple features into single bullet points
- ❌ Use "etc." to indicate omitted details
- ❌ Reference external documents for core procedures
- ❌ Use generic placeholders instead of specific values
- ❌ List items without explaining what each means
- ❌ Omit error handling or edge cases from code examples
- ❌ Skip validation procedures for complex features

### 7. Self-Validation (REQUIRED)

Before submitting your work:

1. **Run the validator yourself:**
   ```bash
   python scripts/validate_contract.py [CONTRACT_PATH]
   ```

2. **Check exit code:**
   ```bash
   echo $?
   ```
   - If `0`: Proceed to submission ✅
   - If `1`: Review failures and fix ❌

3. **Review validation report:**
   ```bash
   cat _reports/[DELIVERABLE]_validation.json
   ```

4. **Fix ALL failures:**
   - Every `"status": "FAIL"` must become `"PASS"`
   - Every `"severity": "CRITICAL"` or `"ERROR"` must be resolved
   - `"final_verdict"` must be `"ACCEPTED"`

5. **Re-validate until clean:**
   Keep running the validator and fixing issues until exit code is `0`.

**DO NOT SUBMIT until validation passes.**

---

## EXECUTION PLAN

[INSERT YOUR TIMELINE HERE]

Example:

### Phase 1: Analysis (30 minutes)
1. Read contract JSON thoroughly
2. Read related reference materials
3. Identify gaps between requirements and current state
4. Create expansion/implementation plan

### Phase 2: Implementation ([X] hours)
1. [MAJOR TASK 1]
   - Subtask A
   - Subtask B
2. [MAJOR TASK 2]
   - Subtask C
   - Subtask D

### Phase 3: Quality Assurance (1 hour)
1. Add all required content elements
2. Remove all forbidden patterns
3. Verify structural requirements
4. Cross-check references

### Phase 4: Self-Validation (30 minutes)
1. Run validator script
2. Review all failures
3. Fix systematically
4. Re-validate until clean (exit code 0)

---

## DELIVERABLES

### Primary Deliverable
**File:** [INSERT FILE PATH]

**Requirements:**
- [INSERT LINE COUNT RANGE]
- [LIST ALL REQUIREMENTS]
- Zero forbidden patterns
- No duplicate sections

### Validation Report
**File:** `_reports/[DELIVERABLE]_validation.json`

**Requirements:**
- `"final_verdict": "ACCEPTED"`
- `"definition_of_done_status"` all `true`
- No `"CRITICAL"` or `"ERROR"` severity failures

---

## WHAT HAPPENS NEXT

### If Validator Returns Exit Code 0 (ACCEPTED)
✅ Your delivery will be accepted immediately
✅ Work is considered production-ready
✅ Contract fulfilled

### If Validator Returns Exit Code 1 (REJECTED)
❌ Your delivery will be sent back to you
❌ You will receive the validation report
❌ You must fix ALL failures
❌ You must re-submit until validation passes

**There is no negotiation. The validator is a machine. It does not make exceptions.**

---

## REFERENCE MATERIALS

You have access to:
- [LIST REFERENCE DOCUMENTS]
- [LIST DATA SOURCES]
- [LIST EXAMPLE FILES]

Use these to understand:
- What details should be included
- What patterns to follow
- What metrics/thresholds are standard
- What code examples are appropriate

---

## QUESTIONS BEFORE STARTING?

If ANY part of this contract is unclear:
1. **Ask now** before you begin work
2. Point to specific `quality_gates` in the contract
3. Request clarification on thresholds or patterns

If everything is clear:
1. Confirm you understand the requirements
2. Provide estimated completion time
3. Begin work

**DO NOT deliver until you have self-validated and achieved exit code 0.**

---

## SUMMARY

**What you're doing:** [ONE SENTENCE DESCRIPTION]

**How you'll be judged:** Automated validator script (zero tolerance)

**What happens if you fail:** Your work is rejected, you fix it, re-submit

**What you need to do right now:**
1. Read contract: [CONTRACT PATH]
2. Understand ALL quality gates
3. Plan your work
4. Execute implementation
5. Self-validate until clean
6. Submit ONLY when validator returns exit code 0

---

**BEGIN WORK. NO MORE HALF-ASSED DELIVERIES.**

---

*This instruction was generated by the N-Grade Contract Enforcement System.*  
*Contract ID: [INSERT CONTRACT_ID]*  
*Validator: `scripts/validate_contract.py`*  
*System Docs: `contracts/N-Grade/docs/`*