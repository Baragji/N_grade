# 📦 N-Grade Contract System - Portable Package

## What Is This?

A **zero-tolerance quality enforcement system** for AI deliverables. No more half-assed work, incomplete drafts, or "I'll finish it later" excuses.

**How it works:**
1. Write a JSON contract defining what you want
2. Hand it to your AI assistant (GPT, Claude, Codex, etc.)
3. AI delivers work
4. Machine validator checks everything
5. Exit code 0 = ACCEPTED, Exit code 1 = REJECTED (no negotiation)

---

## ✅ Proven Results

**Before N-Grade:**
- 195-line skeleton with placeholder templates
- 9 forbidden patterns ("TODO", "TBD", etc.)
- Missing 29 code blocks

**After N-Grade:**
- 1,902-line production-ready document
- Zero violations
- All quality gates passed
- Exit code: 0 (ACCEPTED)

**Verdict:** The machine doesn't negotiate. The AI delivers or gets rejected.

---

## 📦 What's In This Package?

```
N-Grade_contract/
├── PACKAGE_README.md                          ← You are here
├── SETUP.md                                   ← Installation instructions
├── QUICKSTART.md                              ← Get started in 5 minutes
│
├── scripts/
│   └── validate_contract.py                  ← The enforcer
│
├── contracts/
│   ├── documentation_delivery.contract.schema.json  ← Schema definition
│   ├── template.contract.json                ← Start here for new contracts
│   └── example_roadmap.contract.json         ← Real working example
│
├── docs/
│   ├── README.md                             ← System overview
│   ├── CONTRACT_ENFORCEMENT_GUIDE.md         ← Complete usage guide
│   ├── PATH_CONVENTIONS.md                   ← Path best practices
│   └── CODEX_INSTRUCTION_PROMPT.template.md  ← Give this to your AI
│
└── examples/
    └── roadmap_v2_complete_expansion/        ← Full working example
        ├── contract.json
        ├── instruction_prompt.md
        └── validation_report.json
```

---

## 🚀 Quick Install (3 Steps)

### 1. Copy to Your Repo

```bash
# In your new repo
mkdir -p contracts/N-Grade
cp -r N-Grade_contract/* contracts/N-Grade/

# Copy validator to scripts
mkdir -p scripts
cp contracts/N-Grade/scripts/validate_contract.py scripts/
```

### 2. Install Dependencies

```bash
pip install jsonschema  # Only dependency
```

### 3. Test It Works

```bash
python scripts/validate_contract.py \
  contracts/N-Grade/examples/roadmap_v2_complete_expansion/contract.json
```

**Expected output:** Validation runs, shows status. You're ready.

---

## 📝 Create Your First Contract (5 Minutes)

### Step 1: Copy Template

```bash
cd contracts/N-Grade/contracts/
cp template.contract.json my_deliverable.contract.json
```

### Step 2: Edit Contract

```json
{
  "contract_id": "MY_DELIVERABLE_2025",
  "deliverables": [
    {
      "file_path": "docs/my_document.md",
      "quality_gates": {
        "line_count": {"min": 500, "max": 1000},
        "forbidden_patterns": ["TODO", "TBD", "(template)"],
        "required_patterns": {
          "```python": 10,  // At least 10 Python code blocks
          "Success criteria": 5
        }
      }
    }
  ]
}
```

### Step 3: Create Instruction for AI

```bash
cp docs/CODEX_INSTRUCTION_PROMPT.template.md my_deliverable_prompt.md
# Edit file: replace [CONTRACT_FILE] with your contract path
```

### Step 4: Hand to AI

```bash
cat my_deliverable_prompt.md
# Copy output, send to your AI assistant
```

### Step 5: Validate Delivery

```bash
python scripts/validate_contract.py contracts/N-Grade/contracts/my_deliverable.contract.json

# Check exit code
echo $?
# 0 = ACCEPTED ✅
# 1 = REJECTED ❌
```

---

## 🎯 Core Concepts

### 1. Contract = Executable Requirements

Instead of vague instructions:
```
❌ "Write a comprehensive roadmap with details"
```

Use machine-checkable contracts:
```json
✅ {
  "line_count": {"min": 1200},
  "forbidden_patterns": ["TODO", "..."],
  "required_patterns": {"```python": 30}
}
```

### 2. Machine Validation = No Negotiation

```bash
python scripts/validate_contract.py my_contract.json
echo $?
```

- Exit code 0: Work is accepted, move forward
- Exit code 1: Work is rejected, fix and resubmit

**There is no argument. The machine decides.**

### 3. Quality Gates = Automatic Checks

Every deliverable can check:
- **Line count** (min/max ranges)
- **Forbidden patterns** (regex, zero tolerance)
- **Required patterns** (regex, minimum occurrences)
- **Structural requirements** (tables, code blocks, lists)
- **Cross-file consistency** (references between files)

### 4. Definition of Done = Exit Criteria

Contract includes explicit DoD:
```json
"definition_of_done": {
  "all_deliverables_present": true,
  "all_quality_gates_passed": true,
  "validation_report_generated": true
}
```

All must be `true` for acceptance.

---

## 🔧 Customization

### Add New Quality Gates

Edit schema:
```bash
contracts/N-Grade/contracts/documentation_delivery.contract.schema.json
```

Add new gate types:
```json
{
  "word_count": {"min": 5000, "max": 10000},
  "heading_depth": {"max": 4},
  "link_validation": {"required": true}
}
```

Update validator logic:
```bash
scripts/validate_contract.py
```

### Create Domain-Specific Contracts

```bash
contracts/
├── N-Grade/                    # This system
├── API_Documentation/          # New: API doc contracts
├── Test_Coverage/              # New: Test spec contracts
└── Code_Quality/               # New: Code review contracts
```

Each can have its own schemas, validators, and quality gates.

---

## 📚 Documentation

| File | Purpose |
|------|---------|
| `SETUP.md` | Detailed installation and configuration |
| `QUICKSTART.md` | Get your first contract working in 5 minutes |
| `CONTRACT_ENFORCEMENT_GUIDE.md` | Complete usage guide with examples |
| `PATH_CONVENTIONS.md` | How to structure paths correctly |
| `CODEX_INSTRUCTION_PROMPT.template.md` | Template for AI instructions |

---

## 🎓 Best Practices

### ✅ DO:
- Run all commands from repository root
- Use relative paths from repo root
- Test validator after creating new contracts
- Start with template.contract.json
- Make AI self-validate before submission
- Document your quality gates in contract

### ❌ DON'T:
- Use absolute paths in contracts
- Skip validation before accepting work
- Make quality gates too loose
- Accept work with exit code 1
- Negotiate with the machine (it won't listen)

---

## 🐛 Troubleshooting

### "Contract file not found"
```bash
# Ensure path is relative to repo root
python scripts/validate_contract.py contracts/N-Grade/contracts/my_contract.json
```

### "Deliverable file not found"
```bash
# Check file_path in contract JSON
# Must be relative to repo root
{
  "file_path": "docs/my_doc.md"  // ✅ From repo root
}
```

### "Exit code always 1"
```bash
# View validation report
cat _reports/validation.json

# Fix all "FAIL" items
# Re-run validator until exit code 0
```

---

## 🏗️ Integration Examples

### CI/CD Pipeline

```yaml
# .github/workflows/validate_deliverables.yml
name: Validate Deliverables
on: [pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install dependencies
        run: pip install jsonschema
      - name: Run N-Grade validator
        run: |
          python scripts/validate_contract.py contracts/active_deliverable.json
          # Fails if exit code != 0
```

### Pre-commit Hook

```bash
# .git/hooks/pre-commit
#!/bin/bash
python scripts/validate_contract.py contracts/current_work.contract.json
if [ $? -ne 0 ]; then
  echo "❌ Contract validation failed. Commit rejected."
  exit 1
fi
```

### IDE Integration

Add task to `.vscode/tasks.json`:
```json
{
  "label": "Validate Contract",
  "type": "shell",
  "command": "python scripts/validate_contract.py ${input:contractFile}",
  "problemMatcher": []
}
```

---

## 📊 Success Metrics

After deploying N-Grade in your workflow:

**Track:**
- % of deliverables accepted on first submission
- Average validation failures before acceptance
- Time saved on rework cycles
- Quality improvement over time

**Expected results:**
- Week 1: 20-40% first-pass acceptance (AI learning)
- Week 2: 60-80% first-pass acceptance (AI adapting)
- Week 3+: 90%+ first-pass acceptance (AI trained)

---

## 🤝 Support & Extension

### Getting Help

1. Read `CONTRACT_ENFORCEMENT_GUIDE.md`
2. Check `examples/` directory for working contracts
3. Review `PATH_CONVENTIONS.md` for path issues
4. Test with `template.contract.json` first

### Extending the System

Want to add:
- **New quality gates?** Edit schema + validator
- **Domain-specific contracts?** Create new subdirectory
- **Custom validators?** Subclass or create new script
- **Integration with other tools?** Validator returns JSON

---

## 📜 License & Credits

**Created:** 2025-01  
**Purpose:** Enforce quality in AI-generated deliverables  
**Status:** Production-ready (validated with 1,902-line deliverable)  

**Core principle:**  
> "The machine doesn't negotiate. The AI delivers or gets rejected."

---

## 🚀 Ready to Deploy?

1. **Read:** `SETUP.md`
2. **Try:** `QUICKSTART.md`
3. **Create:** Your first contract
4. **Validate:** Test with your AI
5. **Iterate:** Tighten gates as AI improves

**No more half-assed deliveries. Start now.**

---

*Package Version: 1.0.0*  
*Validator: v1.0 (Python 3.8+)*  
*Dependencies: jsonschema*