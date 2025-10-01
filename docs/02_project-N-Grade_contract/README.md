# Documentation Delivery Contracts

## What Is This?

A **NUCLEAR-GRADE CONTRACT SYSTEM** to force AI agents (Codex, Claude, etc.) to deliver **COMPLETE, PRODUCTION-GRADE** work with **ZERO TOLERANCE** for shortcuts, templates, or half-assed deliverables.

## Why Does This Exist?

Because we're tired of getting deliverables like:
- ❌ 195-line "summaries" instead of 1,500-line complete documents
- ❌ `(template)` placeholders instead of actual content
- ❌ Duplicate sections from copy-paste errors
- ❌ "Refer to original doc" instead of standalone content

**NO MORE.**

## How It Works

### 1. Define Requirements in JSON Contract

Machine-parseable contract with hard requirements:

```json
{
  "deliverables": [
    {
      "file_path": "autonomous_ai_roadmap_v2.md",
      "quality_gates": {
        "min_lines": 1200,
        "forbidden_patterns": [
          {"pattern": "(template)", "reason": "NO TEMPLATES"}
        ],
        "required_patterns": [
          {"pattern": "```", "min_occurrences": 30, "reason": "≥30 code examples"}
        ]
      }
    }
  ],
  "definition_of_done": {
    "all_deliverables_present": true,
    "all_quality_gates_passed": true,
    "no_forbidden_patterns_found": true
  }
}
```

### 2. Hand Contract to Agent

Tell Codex (or any agent):

> **"You MUST deliver according to `roadmap_v2_complete_expansion.contract.json`. Your work will be validated by an automated script. If ANY quality gate fails, your delivery is REJECTED automatically."**

### 3. Validate with Script

```bash
python scripts/validate_contract.py \
  docs_ui_2_contracts/roadmap_v2_complete_expansion.contract.json
```

**Exit codes:**
- `0` = ✅ ACCEPTED (all gates passed)
- `1` = ❌ REJECTED (one or more failures)

### 4. Accept or Reject

If exit code is 1:
- Send validation report back to agent
- Demand fixes
- Re-validate until exit code 0

**NO EXCEPTIONS.**

## Files in This Directory

| File | Purpose |
|------|---------|
| `documentation_delivery.contract.schema.json` | **Contract schema** (JSON Schema) defining structure of all contracts |
| `roadmap_v2_complete_expansion.contract.json` | **Contract instance** for fixing incomplete Roadmap v2 |
| `CONTRACT_ENFORCEMENT_GUIDE.md` | **Complete guide** on how to use this system |
| `README.md` | **This file** (quick reference) |

## Quick Start

### For the Impatient

```bash
# 1. Give Codex the contract
echo "Deliver according to: docs_ui_2_contracts/roadmap_v2_complete_expansion.contract.json"

# 2. After delivery, validate
python scripts/validate_contract.py \
  docs_ui_2_contracts/roadmap_v2_complete_expansion.contract.json

# 3. Check exit code
echo $?
# 0 = ACCEPT, 1 = REJECT

# 4. Review report
cat _reports/roadmap_v2_validation.json
```

### For the Thorough

Read `CONTRACT_ENFORCEMENT_GUIDE.md` for full details.

## Contract Anatomy

### Quality Gates (What Gets Checked)

- ✅ **Line counts** (min/max)
- ✅ **Required sections** (regex patterns)
- ✅ **Forbidden patterns** (`(template)`, `TODO`, `TBD`)
- ✅ **Required patterns** (code blocks, metrics, bullets)
- ✅ **No duplicates** (catches copy-paste errors)
- ✅ **Structural requirements** (min code blocks, tables, lists)

### Definition of Done (Pass/Fail)

ALL must be `true`:
- All deliverables present
- All quality gates passed
- All cross-file validations passed
- No forbidden patterns found

**If ANY is `false`: AUTOMATIC REJECTION.**

## Example: Roadmap v2 Contract

**What Codex delivered (REJECTED):**

```
Line count: 195 (required: ≥1,200) ❌
Pattern '(template)': 12 occurrences ❌
Code blocks: 5 (required: ≥30) ❌
VERDICT: REJECTED
```

**What Codex MUST deliver (ACCEPTED):**

```
Line count: 1,487 (required: ≥1,200) ✅
Pattern '(template)': 0 occurrences ✅
Code blocks: 34 (required: ≥30) ✅
VERDICT: ACCEPTED
```

## Creating New Contracts

1. Copy `roadmap_v2_complete_expansion.contract.json`
2. Edit `deliverables`, `quality_gates`, `definition_of_done`
3. Validate schema: `jsonschema -i your_contract.json documentation_delivery.contract.schema.json`
4. Hand to agent with clear instructions
5. Run validator after delivery

## Philosophy

**ZERO TOLERANCE for:**
- Half-assed work (line count too low)
- Template placeholders (`(template)`, `TODO`)
- Copy-paste errors (duplicate sections)
- Missing details (not enough code/metrics)
- External dependencies ("See original doc")

**The validator is a MACHINE. It does not negotiate.**

## Benefits

### For You
- No more manual review of 1,500-line docs
- Clear pass/fail (no subjective judgment)
- Reproducible (same contract = same requirements)

### For Agent
- Clear requirements (no ambiguity)
- Self-validation (can check own work)
- Specific feedback (knows exactly what failed)

## Support

- **Validator bugs?** Check `scripts/validate_contract.py`
- **Unclear requirements?** Read `CONTRACT_ENFORCEMENT_GUIDE.md`
- **Contract too strict?** Adjust quality gates in JSON

## Next Steps

1. **Read the guide:** `docs_ui_2_contracts/N-Grade_contract/CONTRACT_ENFORCEMENT_GUIDE.md`
2. **Review the contract:** `docs_ui_2_contracts/N-Grade_contract/roadmap_v2_complete_expansion.contract.json`
3. **Test the validator:** Run on current files to see what fails
4. **Hand to Codex:** Provide contract + instructions (see `CODEX_INSTRUCTION_PROMPT.md`)
5. **Validate delivery:** Run script from repo root, check exit code
6. **Accept or reject:** No middle ground

---

**NO MORE HALF-ASSED DELIVERIES. CONTRACTS OR GTFO.**