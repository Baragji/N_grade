# Contract Enforcement Guide: NO MORE HALF-ASSED DELIVERIES

## Purpose

This guide documents the **NUCLEAR-GRADE CONTRACT SYSTEM** designed to force Codex (or any AI coding agent) to deliver **COMPLETE, PRODUCTION-GRADE** work with **ZERO TOLERANCE** for shortcuts, templates, or incomplete sections.

## The Problem

Previous deliveries from Codex included:
- ❌ Template placeholders like `(template)` instead of actual content
- ❌ Duplicate sections (copy-paste errors)
- ❌ 195-line "summaries" instead of 1,500-line complete documents
- ❌ Vague "refer to original" instead of standalone content
- ❌ Missing code examples, numeric criteria, and detailed procedures

**THIS ENDS NOW.**

---

## The Solution: Machine-Parseable Contracts

### 1. Contract Schema (`documentation_delivery.contract.schema.json`)

A **JSON Schema** that defines MANDATORY requirements for documentation deliveries:

**Key Features:**
- **Quality Gates**: Line counts, required sections, forbidden patterns, structural requirements
- **Forbidden Patterns**: Rejects `(template)`, `TODO`, `TBD`, `...`, `See original`
- **Required Patterns**: Enforces code blocks, metrics, bullet points with minimum counts
- **Cross-File Validations**: Ensures consistency across multiple files
- **Definition of Done**: ALL criteria must be true (no exceptions)
- **Return Payload**: Structured JSON output (no prose excuses)

### 2. Contract Instance (`roadmap_v2_complete_expansion.contract.json`)

A **specific contract** for fixing the incomplete Roadmap v2:

**Hard Requirements:**
- ✅ **1,200-2,000 lines** (vs. 195 in failed delivery)
- ✅ **≥30 code blocks** with real examples
- ✅ **≥40 numeric metrics** (percentages, latencies, thresholds)
- ✅ **≥200 bullet points** with detailed procedures
- ✅ **≥20 success criteria** sections
- ✅ **≥50 evidence path references**
- ✅ **Zero forbidden patterns** (no templates, TODOs, TBDs)
- ✅ **No duplicate sections** (checks for copy-paste errors)
- ✅ **Canonical evidence paths** only (no legacy paths)

**Rejection Criteria:**
Any of these triggers AUTOMATIC REJECTION:
- Line count < 1,200
- Contains `(template)`, `TODO`, `TBD`, `[FILL IN]`, `...`, `See original`, `Refer to`
- Duplicate section headers (e.g., section 0.6 appearing twice)
- Fewer than 30 code examples
- Fewer than 40 numeric metrics
- Section appears twice due to copy-paste error

### 3. Validator Script (`scripts/validate_contract.py`)

A **Python script** that enforces the contract:

**Capabilities:**
- Checks file existence and line counts
- Validates required/forbidden patterns with regex
- Detects duplicate section headers
- Counts code blocks, tables, lists
- Generates machine-readable validation report (JSON)
- Prints human-readable pass/fail summary
- Exit code 0 = ACCEPTED, 1 = REJECTED

---

## How to Use This System

### Step 1: Hand Codex the Contract

When requesting work from Codex, provide:

1. **The contract file** (`roadmap_v2_complete_expansion.contract.json`)
2. **Clear instructions**:

```
MANDATORY CONTRACT-BASED DELIVERY

You MUST deliver work according to this contract:
  docs_ui_2_contracts/N-Grade_contract/roadmap_v2_complete_expansion.contract.json

Your delivery will be validated by an automated script. If ANY quality gate fails,
your delivery will be REJECTED automatically with no manual review.

CONTRACT REQUIREMENTS:
- Read the entire contract JSON
- Deliver ALL files in "deliverables" array
- Meet ALL "quality_gates" for each file
- Ensure ALL "definition_of_done" criteria are true
- Generate "return_payload" as structured JSON

ZERO TOLERANCE FOR:
- Template placeholders: (template), TODO, TBD, [FILL IN]
- Duplicate sections (copy-paste errors)
- Incomplete line counts (min: 1,200 lines for roadmap)
- Missing code examples (min: 30 blocks)
- Missing metrics (min: 40 numeric thresholds)
- References to external docs for core content

Your delivery MUST pass this validation command (run from repo root):
  python scripts/validate_contract.py docs_ui_2_contracts/N-Grade_contract/roadmap_v2_complete_expansion.contract.json

DO NOT deliver until you have validated your own work against the contract.
```

### Step 2: Codex Works (Autonomously)

According to `codex.md`, Codex can work for 4-5 hours autonomously. It should:

1. Read the contract
2. Understand all quality gates
3. Generate deliverables
4. Self-validate against contract requirements
5. Fix any failures
6. Deliver only when validation passes

### Step 3: Validate the Delivery

Run the validator to check if Codex met the requirements:

```bash
# Run from repository root
cd /path/to/docs_ui_2

# Basic validation
python scripts/validate_contract.py \
  docs_ui_2_contracts/N-Grade_contract/roadmap_v2_complete_expansion.contract.json

# With custom report path
python scripts/validate_contract.py \
  docs_ui_2_contracts/N-Grade_contract/roadmap_v2_complete_expansion.contract.json \
  --report-path _reports/roadmap_v2_validation.json

# Print full JSON report
python scripts/validate_contract.py \
  docs_ui_2_contracts/N-Grade_contract/roadmap_v2_complete_expansion.contract.json \
  --print-report
```

**Exit codes:**
- `0`: ✅ ACCEPTED (all quality gates passed)
- `1`: ❌ REJECTED (one or more failures)
- `2`: ⚠️ ERROR (invalid contract or script failure)

### Step 4: Review Validation Report

The validator generates a detailed JSON report:

```json
{
  "contract_id": "ROADMAP_V2_COMPLETE_EXPANSION_2025",
  "final_verdict": "ACCEPTED" | "REJECTED",
  "rejection_reasons": [
    "Quality gate failures",
    "Forbidden patterns detected (templates, TODOs, etc.)"
  ],
  "deliverable_status": [
    {
      "file_path": "autonomous_ai_roadmap_v2.md",
      "status": "FAIL",
      "line_count": 195,
      "quality_gate_results": {
        "min_lines": false,
        "forbidden_patterns": false
      },
      "failures": [
        {
          "check": "line_count",
          "expected": "≥1200 lines",
          "actual": "Only 195 lines",
          "severity": "CRITICAL"
        },
        {
          "check": "forbidden_pattern",
          "expected": "Zero occurrences of '(template)'",
          "actual": "12 found: ['(template)', ...]",
          "severity": "CRITICAL"
        }
      ]
    }
  ]
}
```

### Step 5: Accept or Reject

**If validator returns exit code 0:**
- ✅ **ACCEPT** the delivery
- Codex met all requirements
- Work is production-ready

**If validator returns exit code 1:**
- ❌ **REJECT** the delivery
- Send validation report back to Codex
- Demand fixes for ALL failures
- Re-run validation until exit code 0

**NO EXCEPTIONS. NO NEGOTIATION.**

---

## Contract Anatomy

### Quality Gates (Per-File)

```json
{
  "min_lines": 1200,              // HARD minimum line count
  "max_lines": 2000,               // Prevents padding/bloat
  "required_sections": [           // Regex patterns for headers
    "^## Phase 0:",
    "^### 0\\.0 "
  ],
  "forbidden_patterns": [          // Auto-reject if found
    {
      "pattern": "\\(template\\)",
      "reason": "NO TEMPLATE PLACEHOLDERS"
    }
  ],
  "required_patterns": [           // Must appear N times
    {
      "pattern": "```(python|bash)",
      "min_occurrences": 30,
      "reason": "MUST include ≥30 code examples"
    }
  ],
  "no_duplicate_sections": true,   // Reject copy-paste errors
  "structural_requirements": {
    "min_code_blocks": 30,
    "min_tables": 5,
    "min_lists": 50
  }
}
```

### Definition of Done (Global)

ALL must be `true` for acceptance:

```json
{
  "all_deliverables_present": true,           // Every file exists
  "all_quality_gates_passed": true,           // Every check passed
  "all_cross_file_validations_passed": true,  // Cross-file consistency
  "no_forbidden_patterns_found": true,        // Zero templates/TODOs
  "validation_report_generated": true         // Report created
}
```

**If ANY is `false`: AUTOMATIC REJECTION.**

---

## Creating New Contracts

### Template

```json
{
  "$schema": "./documentation_delivery.contract.schema.json",
  "contract_version": "1.0.0",
  "contract_id": "YOUR_CONTRACT_ID_HERE",
  "intent": "One-sentence description of what this enforces",
  
  "deliverables": [
    {
      "file_path": "path/to/file.md",
      "file_type": "markdown",
      "purpose": "What this file achieves",
      "quality_gates": {
        "min_lines": 500,
        "forbidden_patterns": [
          {"pattern": "TODO", "reason": "Work must be complete"}
        ],
        "required_patterns": [
          {"pattern": "```", "min_occurrences": 10, "reason": "Need code examples"}
        ]
      }
    }
  ],
  
  "execution_constraints": {
    "max_session_time_hours": 4.0,
    "fail_fast": true
  },
  
  "definition_of_done": {
    "all_deliverables_present": true,
    "all_quality_gates_passed": true,
    "all_cross_file_validations_passed": true,
    "no_forbidden_patterns_found": true,
    "validation_report_generated": true
  },
  
  "return_payload": {
    "contract_id": "YOUR_CONTRACT_ID_HERE",
    "final_verdict": "REJECTED",
    "validation_report_path": "_reports/your_validation.json"
  }
}
```

### Common Quality Gates

**Prevent incomplete work:**
```json
"forbidden_patterns": [
  {"pattern": "\\(template\\)", "reason": "NO TEMPLATES"},
  {"pattern": "TODO|TBD|FIXME", "reason": "NO INCOMPLETE SECTIONS"},
  {"pattern": "\\.\\.\\.", "reason": "NO ELLIPSIS (indicates omitted content)"},
  {"pattern": "See original|Refer to", "reason": "MUST BE STANDALONE"}
]
```

**Enforce detail:**
```json
"required_patterns": [
  {"pattern": "```[\\w]*", "min_occurrences": 20, "reason": "≥20 code blocks"},
  {"pattern": "\\d+\\.\\d+%|≥\\d+%", "min_occurrences": 30, "reason": "≥30 numeric metrics"},
  {"pattern": "Success criteria:|Exit criteria:", "min_occurrences": 10, "reason": "Clear success criteria"}
]
```

**Ensure structure:**
```json
"structural_requirements": {
  "min_code_blocks": 20,
  "min_tables": 3,
  "min_lists": 50,
  "require_toc": true
}
```

---

## Example: Roadmap v2 Contract in Action

### What Codex Delivered (REJECTED)

```
Line count: 195 (required: ≥1,200) ❌
Forbidden pattern '(template)': 12 occurrences ❌
Code blocks: 5 (required: ≥30) ❌
Numeric metrics: 8 (required: ≥40) ❌
Duplicate sections: Section 0.6 appears twice ❌

VERDICT: REJECTED
```

### What Codex MUST Deliver (ACCEPTED)

```
Line count: 1,487 (required: ≥1,200) ✅
Forbidden patterns: 0 occurrences ✅
Code blocks: 34 (required: ≥30) ✅
Numeric metrics: 52 (required: ≥40) ✅
Duplicate sections: None ✅

VERDICT: ACCEPTED
```

---

## Philosophy: Zero Tolerance

This system is designed with **ZERO TOLERANCE** for:

1. **Half-assed work**: If line count < minimum, REJECT (no excuses)
2. **Template placeholders**: Any `(template)` or `TODO` → REJECT
3. **Copy-paste errors**: Duplicate sections → REJECT
4. **Missing details**: Not enough code/metrics → REJECT
5. **External dependencies**: "See original doc" for core content → REJECT

**The validator is a MACHINE. It does not negotiate. It does not make exceptions.**

If Codex (or any agent) cannot meet the contract, it should:
1. Request clarification on requirements
2. Request more time/resources
3. Deliver incrementally with checkpoints

**What it CANNOT do:**
- Deliver incomplete work and claim it's "good enough"
- Ignore quality gates
- Make excuses in prose instead of structured output

---

## Benefits

### For You (User)
- ✅ **No more review fatigue**: Validator catches issues automatically
- ✅ **Clear pass/fail**: No subjective "this seems okay-ish"
- ✅ **Reproducible**: Same contract = same requirements every time
- ✅ **Documented expectations**: Contract IS the specification

### For Codex (Agent)
- ✅ **Clear requirements**: No ambiguity about what constitutes "done"
- ✅ **Self-validation**: Can check own work before delivery
- ✅ **Specific feedback**: Knows exactly what failed and why
- ✅ **No wasted iterations**: Gets it right the first time

---

## Files in This System

```
docs_ui_2_contracts/
├── documentation_delivery.contract.schema.json   # Contract schema (reusable)
├── roadmap_v2_complete_expansion.contract.json   # Specific contract instance
├── CONTRACT_ENFORCEMENT_GUIDE.md                 # This guide
└── (future contracts...)

scripts/
└── validate_contract.py                          # Validator script

_reports/
└── roadmap_v2_validation.json                    # Generated validation report
```

---

## Next Steps

### 1. Send This Contract to Codex

Provide Codex with:
- `roadmap_v2_complete_expansion.contract.json`
- Instruction to validate before delivery
- Command: `python scripts/validate_contract.py docs_ui_2_contracts/roadmap_v2_complete_expansion.contract.json`

### 2. Run Validation on Delivery

```bash
python scripts/validate_contract.py \
  docs_ui_2_contracts/roadmap_v2_complete_expansion.contract.json \
  --report-path _reports/roadmap_v2_validation.json
```

### 3. Review Report

Check `_reports/roadmap_v2_validation.json` for detailed results.

### 4. Accept or Reject

- Exit code 0 → ACCEPT
- Exit code 1 → REJECT (send report back to Codex)

---

## Future Enhancements

### Potential Additions

1. **JSON Schema validation** for structured files (JSON, YAML)
2. **CSV validation** with column/row checks
3. **Semantic checks** (e.g., "all functions in taxonomy appear in roadmap")
4. **Link validation** (check internal file references)
5. **Diff validation** (ensure changes match requirements)
6. **Performance gates** (e.g., "indexing must complete in <5 minutes")

### Contract Templates

Create reusable contract templates for:
- API documentation
- Architecture decision records (ADRs)
- Test reports
- Code refactoring
- Schema migrations

---

## Summary

**This is not a request. This is a CONTRACT.**

Codex (or any agent) must:
1. Read the contract
2. Understand all requirements
3. Deliver work that passes validation
4. Self-check before submission

**If validation fails: REJECTED. No excuses. No exceptions.**

---

## Contact / Issues

If the validator has bugs or the contract has ambiguous requirements:
1. File an issue with the validation report
2. Propose contract amendments as PRs
3. Document edge cases for future contracts

**But if Codex simply didn't meet the requirements: That's on Codex, not the contract.**

---

**END OF GUIDE. GO ENFORCE SOME CONTRACTS.**