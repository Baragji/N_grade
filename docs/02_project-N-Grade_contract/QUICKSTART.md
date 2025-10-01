# ⚡ N-Grade Contract System - Quick Start

Get your first contract working in **5 minutes**.

---

## Prerequisites

✅ N-Grade system installed (see `SETUP.md`)  
✅ Python 3.8+ with `jsonschema` installed  
✅ Working from repository root  

---

## Step 1: Create Your Contract (2 minutes)

```bash
# Copy template
cp contracts/N-Grade/contracts/template.contract.json contracts/my_first_contract.json

# Edit with your favorite editor
nano contracts/my_first_contract.json
```

**Minimal contract example:**

```json
{
  "$schema": "./N-Grade/contracts/documentation_delivery.contract.schema.json",
  "contract_id": "MY_FIRST_CONTRACT_2025",
  "contract_version": "1.0.0",
  "deliverables": [
    {
      "file_path": "docs/my_document.md",
      "description": "My first AI-generated document",
      "quality_gates": {
        "line_count": {
          "min": 50,
          "max": 200
        },
        "forbidden_patterns": [
          "TODO",
          "TBD",
          "\\.\\.\\."
        ],
        "required_patterns": {
          "^## ": 3,
          "Success criteria": 1,
          "```": 2
        }
      }
    }
  ],
  "definition_of_done": {
    "all_deliverables_present": true,
    "all_quality_gates_passed": true,
    "validation_report_generated": true
  }
}
```

**What this contract demands:**
- 50-200 lines
- No TODO/TBD/... patterns
- At least 3 `## ` headers (level 2 headings)
- At least 1 "Success criteria" mention
- At least 2 code blocks (```)

---

## Step 2: Create AI Instructions (1 minute)

```bash
# Copy instruction template
cp contracts/N-Grade/docs/CODEX_INSTRUCTION_PROMPT.template.md instructions_my_document.md

# Edit to reference your contract
nano instructions_my_document.md
```

**Quick template:**

```markdown
# CONTRACT-BASED DELIVERY INSTRUCTION

You are receiving a CONTRACT with ZERO TOLERANCE for incomplete work.

## Contract File
contracts/my_first_contract.json

## Validation Command
python scripts/validate_contract.py contracts/my_first_contract.json

## What You Must Deliver

**File:** docs/my_document.md

**Requirements:**
- 50-200 lines
- At least 3 major sections (## headers)
- At least 2 code examples
- Include "Success criteria" section
- No TODO/TBD/... placeholders

## Self-Validation

Before submitting:
```bash
python scripts/validate_contract.py contracts/my_first_contract.json
echo $?  # Must be 0 (ACCEPTED)
```

## What You're Writing

[DESCRIBE YOUR DOCUMENT PURPOSE HERE]

Example: "A technical guide for setting up Redis caching in Python applications"

---

**BEGIN WORK. DELIVER ONLY WHEN VALIDATOR RETURNS EXIT CODE 0.**
```

---

## Step 3: Give Instructions to AI (30 seconds)

```bash
# Display instructions
cat instructions_my_document.md

# Copy output, paste to your AI assistant (GPT, Claude, Codex, etc.)
```

**What to say to AI:**

> "Here is a contract-based delivery request. Read the contract at `contracts/my_first_contract.json` and deliver the document according to all quality gates. Self-validate before submitting. Exit code must be 0."
>
> [Paste contents of instructions_my_document.md]

---

## Step 4: AI Works → Delivers → You Validate (1 minute)

When AI says "I'm done":

```bash
# Validate
python scripts/validate_contract.py contracts/my_first_contract.json

# Check exit code
echo $?
```

**Exit code 0 (ACCEPTED):**
```bash
✅ All quality gates passed
✅ Document is production-ready
✅ Move to next task
```

**Exit code 1 (REJECTED):**
```bash
❌ Quality gates failed
❌ Review report: cat _reports/my_first_contract_validation.json
❌ Send back to AI with specific failures
❌ AI fixes and resubmits
```

---

## Step 5: Review Results (30 seconds)

```bash
# View validation report
cat _reports/my_first_contract_validation.json
```

**Successful report looks like:**

```json
{
  "final_verdict": "ACCEPTED",
  "deliverable_status": [
    {
      "file_path": "docs/my_document.md",
      "status": "PASS",
      "line_count": 87,
      "quality_gate_results": {
        "min_lines": true,
        "forbidden_patterns": true,
        "required_patterns": true
      },
      "failures": []
    }
  ],
  "definition_of_done_status": {
    "all_deliverables_present": true,
    "all_quality_gates_passed": true,
    "validation_report_generated": true
  }
}
```

**Key fields:**
- `"final_verdict": "ACCEPTED"` → Work is done ✅
- `"status": "PASS"` → File passed all gates ✅
- `"failures": []` → No issues found ✅

---

## Common First-Time Issues

### Issue: AI delivers document with TODOs

**Validator output:**
```json
"failures": [
  {
    "gate": "forbidden_patterns",
    "severity": "CRITICAL",
    "message": "Found 3 occurrences of 'TODO'"
  }
]
```

**What to do:**
```bash
# Send back to AI with clear instruction
echo "❌ REJECTED: 3 TODO patterns found. Remove ALL placeholders and resubmit."
```

### Issue: Document too short

**Validator output:**
```json
"failures": [
  {
    "gate": "line_count",
    "severity": "CRITICAL",
    "message": "Only 32 lines, required: ≥50"
  }
]
```

**What to do:**
```bash
echo "❌ REJECTED: Only 32 lines, need ≥50. Expand all sections with details."
```

### Issue: Missing required content

**Validator output:**
```json
"failures": [
  {
    "gate": "required_patterns",
    "severity": "ERROR",
    "message": "Pattern '```' found 0 times, required: ≥2"
  }
]
```

**What to do:**
```bash
echo "❌ REJECTED: Need at least 2 code examples. Add code blocks."
```

---

## Quick Reference

### Command Cheat Sheet

```bash
# Validate contract
python scripts/validate_contract.py contracts/YOUR_CONTRACT.json

# Check exit code
echo $?

# View validation report
cat _reports/YOUR_CONTRACT_validation.json

# Count lines in deliverable
wc -l docs/your_document.md

# Search for forbidden patterns manually
grep -n "TODO\|TBD" docs/your_document.md
```

### Exit Codes

| Code | Meaning | Action |
|------|---------|--------|
| 0 | ACCEPTED | ✅ Work complete, move forward |
| 1 | REJECTED | ❌ Review failures, fix, resubmit |
| 2 | ERROR | 🔧 Validator issue, check syntax |

### Quality Gate Status

| Status | Meaning |
|--------|---------|
| `PASS` | ✅ Gate satisfied |
| `FAIL` | ❌ Gate violated |
| `SKIP` | ⏭️ Gate not applicable |

---

## Next Steps

### ✅ Success Path (Exit Code 0)

1. **Archive contract & validation report**
   ```bash
   git add contracts/my_first_contract.json
   git add _reports/my_first_contract_validation.json
   git add docs/my_document.md
   git commit -m "Add: My first contract-enforced deliverable"
   ```

2. **Create more contracts**
   ```bash
   cp contracts/my_first_contract.json contracts/next_deliverable.json
   # Edit for new requirements
   ```

3. **Tighten quality gates** as AI improves
   ```json
   {
     "line_count": {"min": 100},  // Increased from 50
     "required_patterns": {
       "```python": 5  // More specific
     }
   }
   ```

### ❌ Failure Path (Exit Code 1)

1. **Review validation report**
   ```bash
   cat _reports/my_first_contract_validation.json | jq '.deliverable_status[].failures'
   ```

2. **Identify all failures** (severity CRITICAL and ERROR)

3. **Send specific feedback to AI:**
   ```
   ❌ REJECTED - Fix these issues:
   1. Line count: 32 lines (need ≥50)
   2. Forbidden pattern: 3 occurrences of "TODO"
   3. Required pattern: Missing "Success criteria" section
   
   Resubmit when fixed.
   ```

4. **AI fixes → Revalidate → Repeat until exit 0**

---

## Tips for Success

### 1. Start Small
- First contract: 50 lines, basic gates
- Second contract: 100 lines, more patterns
- Third contract: Full complexity

### 2. Be Specific
```json
// ❌ Vague
{"required_patterns": {"code": 1}}

// ✅ Specific
{"required_patterns": {"```python": 3, "```bash": 2}}
```

### 3. Test Gates Before Deployment
```bash
# Create dummy deliverable that should PASS
echo "## Test" > test.md
echo "Success criteria: all good" >> test.md
# ... add content matching gates

# Validate
python scripts/validate_contract.py test_contract.json
# Should return 0
```

### 4. Make AI Self-Validate
Include in instructions:
```markdown
## MANDATORY: Self-Validation

Run this before submitting:
```bash
python scripts/validate_contract.py YOUR_CONTRACT.json
echo $?
```

DO NOT submit until exit code is 0.
```

### 5. Iterate on Failures
- Week 1: AI might fail 80% of first submissions → Normal
- Week 2: AI adapts, ~50% first-pass success
- Week 3+: AI trained, 90%+ first-pass success

---

## You're Ready! 🚀

You now know:
- ✅ How to create contracts
- ✅ How to instruct AI
- ✅ How to validate deliverables
- ✅ How to handle failures
- ✅ How to iterate toward success

**Create your first contract now:**

```bash
cp contracts/N-Grade/contracts/template.contract.json contracts/real_deliverable.contract.json
nano contracts/real_deliverable.contract.json
# Define what you need
# Hand to AI
# Validate
# Done.
```

---

## Need More?

- **Complete guide:** `contracts/N-Grade/docs/CONTRACT_ENFORCEMENT_GUIDE.md`
- **Real example:** `contracts/N-Grade/examples/roadmap_v2_complete_expansion/`
- **Path conventions:** `contracts/N-Grade/docs/PATH_CONVENTIONS.md`
- **Schema reference:** `contracts/N-Grade/contracts/documentation_delivery.contract.schema.json`

---

**No more half-assed deliveries. The machine decides. Start now.** 🔥

---

*Quick Start Version: 1.0.0*  
*Estimated completion time: 5 minutes*