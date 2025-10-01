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
