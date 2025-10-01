# CONTRACT-BASED DELIVERY INSTRUCTION FOR CODEX

**COPY THIS ENTIRE PROMPT AND SEND TO CODEX →**

---

## MANDATORY CONTRACT ENFORCEMENT

You are receiving a **CONTRACT-BASED DELIVERY REQUEST** with **ZERO TOLERANCE** for incomplete work.

### Critical Information

**Contract File:**
```
docs_ui_2_contracts/roadmap_v2_complete_expansion.contract.json
```

**Validation Command:**
```bash
python3 scripts/validate_contract.py \
  docs_ui_2_contracts/roadmap_v2_complete_expansion.contract.json \
  --report-path _reports/roadmap_v2_validation.json
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
docs_ui_2_contracts/roadmap_v2_complete_expansion.contract.json
```

Pay special attention to:
- `deliverables[].quality_gates` (MANDATORY requirements)
- `forbidden_patterns` (patterns that trigger AUTOMATIC REJECTION)
- `required_patterns` (content that MUST appear with minimum occurrences)
- `definition_of_done` (ALL must be `true` for acceptance)

### 2. Understand Quality Gates

Your deliverable will be checked for:

#### ✅ Line Count
- **Minimum:** 1,200 lines
- **Maximum:** 2,000 lines
- **Current state:** 195 lines (REJECTED)
- **What this means:** You need to expand the roadmap by ~6x

#### ✅ Required Sections
All phase headers MUST exist:
- `## Phase 0:` through `## Phase 8:`
- `### 0.0` through `### 0.6` (Phase 0 subsections)
- `### 1.0` through `### 1.7` (Phase 1 subsections)
- And all subsections for remaining phases

#### ❌ Forbidden Patterns (ZERO TOLERANCE)
Any occurrence of these triggers AUTOMATIC REJECTION:
- `(template)` - NO TEMPLATE PLACEHOLDERS
- `TODO` - NO TODOs
- `TBD` - NO TBDs
- `[FILL IN]` - NO FILL-IN MARKERS
- `...` - NO ELLIPSIS (indicates omitted content)
- `See original` - MUST BE STANDALONE
- `Refer to` - NO EXTERNAL DEPENDENCIES

**Current state:** 9 occurrences of `(template)` (CRITICAL FAILURE)

#### ✅ Required Patterns (Minimum Occurrences)
Your delivery MUST contain AT LEAST:

| Pattern | Minimum | Current | Status |
|---------|---------|---------|--------|
| Code blocks (```python/bash/yaml/json) | 30 | 1 | ❌ FAIL |
| Numeric metrics (%, ms, seconds) | 40 | 5 | ❌ FAIL |
| Bullet points (detailed lists) | 200 | 58 | ❌ FAIL |
| Success criteria sections | 20 | 0 | ❌ FAIL |
| Evidence path references | 50 | 18 | ❌ FAIL |

#### ✅ Structural Requirements
- **Code blocks:** ≥30 (currently 2) ❌
- **Tables:** ≥5 (currently 0) ❌
- **Lists:** ≥50 complete lists
- **No duplicate sections:** Headers must be unique ✅

### 3. Expansion Guidelines (From Contract)

Each Phase 0 subsection (0.0-0.6) MUST have:
1. 3-5 paragraph overview
2. Implementation steps as numbered list with sub-bullets
3. At least one code example
4. Success criteria with numeric thresholds
5. Evidence file paths

Each Phase 1 subsection (1.0-1.7) MUST have:
1. Feature description
2. Technical requirements with metrics
3. Integration points
4. Code snippets
5. Validation procedures
6. Rollback procedures

### 4. Code Example Standards

All code blocks MUST:
- Be syntactically valid
- Include inline comments
- Show realistic values (not placeholders like `YOUR_VALUE_HERE`)
- Demonstrate the specific feature being discussed

**Example (GOOD):**
```python
# State persistence with Redis
import redis
import json

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    decode_responses=True
)

def save_state(session_id: str, state: dict) -> bool:
    """Persist agent state with TTL."""
    key = f"agent:state:{session_id}"
    redis_client.setex(
        key,
        ttl=3600,  # 1 hour TTL
        value=json.dumps(state)
    )
    return True
```

**Example (BAD - WILL BE REJECTED):**
```python
# TODO: Add state management code here
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
- Test coverage ≥95% (measured by pytest-cov, recorded in gates/g3_test_coverage.json)
- p95 latency <100ms (measured by locust, recorded in gates/g6_performance.json)
- Zero data loss across 1,000 test runs (verified by audit script, recorded in gates/g2_data_integrity.json)
```

**Example (BAD - WILL BE REJECTED):**
```
Success criteria:
- High test coverage
- Fast response times
- Reliable data storage
```

### 6. Prohibited Shortcuts

DO NOT:
- ❌ Condense multiple features into single bullet points
- ❌ Use "etc." to indicate omitted details
- ❌ Reference external documents for core procedures
- ❌ Combine phases to reduce line count
- ❌ Use generic placeholders instead of specific values
- ❌ List evidence paths without explaining what each contains
- ❌ Omit error handling or edge cases from code examples
- ❌ Skip validation procedures for complex features

### 7. Self-Validation (REQUIRED)

Before submitting your work:

1. **Run the validator yourself:**
   ```bash
   python3 scripts/validate_contract.py \
     docs_ui_2_contracts/roadmap_v2_complete_expansion.contract.json
   ```

2. **Check exit code:**
   ```bash
   echo $?
   ```
   - If `0`: Proceed to submission ✅
   - If `1`: Review failures in `_reports/roadmap_v2_validation.json` and fix ❌

3. **Review validation report:**
   ```bash
   cat _reports/roadmap_v2_validation.json
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

Based on your autonomous execution model (4-5 hours):

### Phase 1: Analysis (30 minutes)
1. Read contract JSON thoroughly
2. Read current `autonomous_ai_roadmap_v2.md` (195 lines)
3. Read original `autonomous_ai_roadmap.md` for reference
4. Identify ALL gaps between current state and contract requirements
5. Create expansion plan (which sections need what content)

### Phase 2: Expansion (3 hours)
1. **Phase 0 sections (0.0-0.6):**
   - Expand each from 2-3 lines to 50-100 lines
   - Add code examples, metrics, procedures
   - Add success criteria with numeric thresholds
   
2. **Phase 1 sections (1.0-1.7):**
   - Expand each from 2-3 lines to 80-120 lines
   - Add detailed procedures
   - Add validation and rollback steps
   
3. **Phases 2-8:**
   - Expand each major section to 100-200 lines
   - Include all subsections from original roadmap
   - Add implementation details

### Phase 3: Quality Assurance (1 hour)
1. Add all required code blocks (need 30+)
2. Add all required metrics (need 40+)
3. Ensure all bullet points are detailed (need 200+)
4. Add success criteria sections (need 20+)
5. Add evidence path references (need 50+)
6. Remove ALL forbidden patterns
7. Check for duplicate sections

### Phase 4: Self-Validation (30 minutes)
1. Run validator script
2. Review all failures
3. Fix systematically
4. Re-validate until clean (exit code 0)
5. Generate final report

---

## DELIVERABLES

### Primary Deliverable
**File:** `autonomous_ai_roadmap_v2.md`

**Requirements:**
- 1,200-2,000 lines (currently 195)
- All phase sections fully expanded
- ≥30 code blocks with real examples
- ≥40 numeric metrics with units
- ≥200 bullet points (detailed)
- ≥20 success criteria sections
- ≥50 evidence path references
- Zero forbidden patterns
- No duplicate sections

### Validation Report
**File:** `_reports/roadmap_v2_validation.json`

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

## CURRENT STATE ANALYSIS

Running the validator on current state shows:

```
❌ autonomous_ai_roadmap_v2.md (195 lines)
    └─ CRITICAL: line_count (Only 195 lines, required: ≥1200)
    └─ CRITICAL: forbidden_pattern (9 occurrences of '(template)')
    └─ ERROR: required_pattern (Only 1 code block, required: ≥30)
    └─ ERROR: required_pattern (Only 5 metrics, required: ≥40)
    └─ ERROR: required_pattern (Only 58 bullets, required: ≥200)
    └─ ERROR: required_pattern (0 success criteria, required: ≥20)
    └─ ERROR: required_pattern (18 evidence paths, required: ≥50)
    └─ ERROR: structural_requirement (Only 2 code blocks, required: ≥30)
    └─ ERROR: structural_requirement (0 tables, required: ≥5)

VERDICT: REJECTED
```

**You need to fix ALL of these issues.**

---

## REFERENCE MATERIALS

You have access to:
- ✅ `autonomous_ai_roadmap.md` (original, for content reference)
- ✅ `autonomous_ai_coding_system_taxonomy_ssot_v1.2.md` (for function mapping)
- ✅ `docs/taxonomy/traceability_matrix.csv` (for phase/gate/evidence mapping)
- ✅ `docs/gates/*.md` (for validation procedures)
- ✅ `scripts/validate_gates.py` (for evidence path examples)

Use these to understand:
- What details should be in each phase
- What evidence paths are canonical
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

**What you're doing:** Expanding `autonomous_ai_roadmap_v2.md` from 195 lines to 1,200-2,000 lines with complete details

**How you'll be judged:** Automated validator script (zero tolerance)

**What happens if you fail:** Your work is rejected, you fix it, re-submit

**What you need to do right now:**
1. Read contract: `docs_ui_2_contracts/N-Grade_contract/roadmap_v2_complete_expansion.contract.json`
2. Understand ALL quality gates
3. Plan your expansion
4. Execute expansion (4-5 hours)
5. Self-validate until clean
6. Submit ONLY when validator returns exit code 0

---

**BEGIN WORK. NO MORE HALF-ASSED DELIVERIES.**

---

*This instruction was generated by the Contract Enforcement System.*  
*Contract ID: `ROADMAP_V2_COMPLETE_EXPANSION_2025`*  
*Validator: `scripts/validate_contract.py`*  
*Full Guide: `docs_ui_2_contracts/N-Grade_contract/CONTRACT_ENFORCEMENT_GUIDE.md`*