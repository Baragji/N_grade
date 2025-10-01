# 🔧 N-Grade Contract System - Setup Guide

Complete installation and configuration instructions for deploying the N-Grade Contract System in any repository.

---

## Prerequisites

### Required
- **Python 3.8+** (3.10+ recommended)
- **pip** (Python package manager)
- **Git** (for version control)

### Optional
- **Virtual environment tool** (venv, virtualenv, conda)
- **CI/CD platform** (GitHub Actions, GitLab CI, etc.)

---

## Installation Methods

### Method 1: Quick Drop-In (Recommended)

**Use this if:** You have a clean repo and want to get started fast.

```bash
# 1. Navigate to your repository root
cd /path/to/your/repo

# 2. Create directory structure
mkdir -p contracts/N-Grade
mkdir -p scripts
mkdir -p _reports

# 3. Copy N-Grade package
# (Assuming you have the package in ~/Downloads/N-Grade_contract/)
cp -r ~/Downloads/N-Grade_contract/* contracts/N-Grade/

# 4. Copy validator to scripts directory
cp contracts/N-Grade/scripts/validate_contract.py scripts/

# 5. Install dependencies
pip install jsonschema

# 6. Test installation
python scripts/validate_contract.py contracts/N-Grade/examples/roadmap_v2_complete_expansion/contract.json

# ✅ If validation runs without errors, installation successful
```

---

### Method 2: Git Submodule (For Tracking Updates)

**Use this if:** You want to track upstream changes to N-Grade system.

```bash
# 1. Add as submodule
git submodule add https://github.com/your-org/n-grade-contracts.git contracts/N-Grade

# 2. Copy validator to main repo
cp contracts/N-Grade/scripts/validate_contract.py scripts/

# 3. Install dependencies
pip install jsonschema

# 4. Commit submodule
git add .gitmodules contracts/N-Grade scripts/validate_contract.py
git commit -m "Add N-Grade contract system"

# Update later
git submodule update --remote contracts/N-Grade
```

---

### Method 3: Manual Setup (Full Control)

**Use this if:** You want to customize heavily or understand every component.

```bash
# 1. Create directory structure
mkdir -p contracts/N-Grade/{scripts,contracts,docs,examples}
mkdir -p scripts
mkdir -p _reports

# 2. Copy files individually (adjust paths as needed)
cp /path/to/source/validate_contract.py scripts/
cp /path/to/source/documentation_delivery.contract.schema.json contracts/N-Grade/contracts/
cp /path/to/source/template.contract.json contracts/N-Grade/contracts/
# ... copy other files as needed

# 3. Install dependencies
pip install jsonschema

# 4. Verify structure
tree contracts/N-Grade  # Should match expected structure
```

---

## Directory Structure (After Installation)

```
your-repo/
├── contracts/
│   └── N-Grade/
│       ├── PACKAGE_README.md
│       ├── SETUP.md                              ← You are here
│       ├── QUICKSTART.md
│       ├── scripts/
│       │   └── validate_contract.py
│       ├── contracts/
│       │   ├── documentation_delivery.contract.schema.json
│       │   ├── template.contract.json
│       │   └── example_roadmap.contract.json
│       ├── docs/
│       │   ├── README.md
│       │   ├── CONTRACT_ENFORCEMENT_GUIDE.md
│       │   ├── PATH_CONVENTIONS.md
│       │   └── CODEX_INSTRUCTION_PROMPT.template.md
│       └── examples/
│           └── roadmap_v2_complete_expansion/
│               ├── contract.json
│               ├── instruction_prompt.md
│               └── validation_report.json
│
├── scripts/
│   └── validate_contract.py                      ← Copied from N-Grade
│
├── _reports/                                     ← Auto-generated
│   └── *.json                                    ← Validation reports
│
└── docs/                                         ← Your deliverables
    └── your_document.md
```

---

## Configuration

### 1. Python Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv .venv

# Activate
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate  # Windows

# Install dependencies
pip install jsonschema

# Save dependencies
pip freeze > requirements.txt
```

### 2. Path Configuration

**Critical:** All paths in contracts must be **relative to repository root**.

```json
// ✅ CORRECT
{
  "file_path": "docs/roadmap.md",
  "schema": "./documentation_delivery.contract.schema.json"
}

// ❌ WRONG
{
  "file_path": "/Users/you/repo/docs/roadmap.md",
  "schema": "/absolute/path/to/schema.json"
}
```

See `contracts/N-Grade/docs/PATH_CONVENTIONS.md` for complete guide.

### 3. Validator Configuration

Edit `scripts/validate_contract.py` if you need to:

**Change report directory:**
```python
# Line ~20
DEFAULT_REPORT_DIR = "_reports"  # Change to your preference
```

**Add custom quality gates:**
```python
# Add new gate validation functions
def validate_custom_gate(content, gate_config):
    # Your validation logic
    pass
```

**Adjust severity levels:**
```python
SEVERITY_CRITICAL = ["line_count", "forbidden_patterns"]
SEVERITY_ERROR = ["required_patterns", "structural_requirements"]
SEVERITY_WARNING = ["your_custom_gates"]
```

---

## Validation

### Basic Test

```bash
# Run validator on example contract
python scripts/validate_contract.py \
  contracts/N-Grade/examples/roadmap_v2_complete_expansion/contract.json

# Check exit code
echo $?
# Should print 0 or 1 (validator is working)
```

### Create Test Contract

```bash
# Copy template
cp contracts/N-Grade/contracts/template.contract.json contracts/test.contract.json

# Create test deliverable
echo "# Test Document" > docs/test.md
echo "This is a test." >> docs/test.md

# Edit contract
nano contracts/test.contract.json
# Set "file_path": "docs/test.md"
# Set "line_count": {"min": 1}

# Validate
python scripts/validate_contract.py contracts/test.contract.json

# Should ACCEPT (exit 0)
```

---

## Integration

### Git Integration

**Add to `.gitignore`:**
```gitignore
# Validation reports (auto-generated)
_reports/*.json

# Python cache
__pycache__/
*.pyc
.venv/
```

**Add to version control:**
```bash
git add contracts/N-Grade
git add scripts/validate_contract.py
git commit -m "Add N-Grade contract enforcement system"
```

### CI/CD Integration

**GitHub Actions:**

Create `.github/workflows/validate_contracts.yml`:

```yaml
name: Validate Contracts
on:
  pull_request:
    paths:
      - 'docs/**'
      - 'contracts/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: pip install jsonschema
      
      - name: Validate active contracts
        run: |
          for contract in contracts/*.contract.json; do
            echo "Validating $contract"
            python scripts/validate_contract.py "$contract"
            if [ $? -ne 0 ]; then
              echo "❌ Validation failed for $contract"
              exit 1
            fi
          done
          echo "✅ All contracts validated"
```

**GitLab CI:**

Add to `.gitlab-ci.yml`:

```yaml
validate_contracts:
  stage: test
  image: python:3.10
  before_script:
    - pip install jsonschema
  script:
    - python scripts/validate_contract.py contracts/active.contract.json
  only:
    changes:
      - docs/**
      - contracts/**
  allow_failure: false
```

### Pre-commit Hook

```bash
# Create hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
# Validate contracts before commit

CONTRACTS=$(git diff --cached --name-only | grep "\.contract\.json$")

if [ -n "$CONTRACTS" ]; then
  echo "📋 Validating contracts..."
  for contract in $CONTRACTS; do
    python scripts/validate_contract.py "$contract"
    if [ $? -ne 0 ]; then
      echo "❌ Contract validation failed: $contract"
      echo "Fix issues and re-commit."
      exit 1
    fi
  done
  echo "✅ All contracts validated"
fi
EOF

# Make executable
chmod +x .git/hooks/pre-commit
```

---

## Troubleshooting

### Issue: "Module 'jsonschema' not found"

**Solution:**
```bash
pip install jsonschema
# OR in virtual environment
source .venv/bin/activate
pip install jsonschema
```

### Issue: "Contract file not found"

**Solution:**
```bash
# Check path is relative to repo root
pwd  # Should be at repository root
ls contracts/your_contract.json  # Should exist

# Run from repo root
python scripts/validate_contract.py contracts/your_contract.json
```

### Issue: "Deliverable file not found"

**Solution:**
```json
// In contract.json, check file_path
{
  "file_path": "docs/document.md"  // Must be relative to repo root
}
```

```bash
# Verify file exists
ls docs/document.md
```

### Issue: "Invalid JSON in contract file"

**Solution:**
```bash
# Validate JSON syntax
python -m json.tool contracts/your_contract.json
# Will show syntax errors

# Or use online validator
cat contracts/your_contract.json | jq
```

### Issue: "Validator always rejects (exit 1)"

**Solution:**
```bash
# Check validation report
cat _reports/your_validation.json

# Look for "status": "FAIL" entries
# Fix each failure in your deliverable
# Re-validate until "final_verdict": "ACCEPTED"
```

### Issue: "Permission denied on validator script"

**Solution:**
```bash
chmod +x scripts/validate_contract.py
```

---

## Next Steps

After successful installation:

1. ✅ **Read:** `contracts/N-Grade/QUICKSTART.md`
2. ✅ **Create:** Your first contract from template
3. ✅ **Test:** Validate a simple deliverable
4. ✅ **Document:** Add contract info to your project README
5. ✅ **Integrate:** Add to CI/CD pipeline
6. ✅ **Scale:** Create contracts for all AI deliverables

---

## Support

### Documentation
- **Complete guide:** `contracts/N-Grade/docs/CONTRACT_ENFORCEMENT_GUIDE.md`
- **Path conventions:** `contracts/N-Grade/docs/PATH_CONVENTIONS.md`
- **Examples:** `contracts/N-Grade/examples/`

### Common Resources
- Schema reference: `contracts/N-Grade/contracts/documentation_delivery.contract.schema.json`
- Template contract: `contracts/N-Grade/contracts/template.contract.json`
- AI instruction template: `contracts/N-Grade/docs/CODEX_INSTRUCTION_PROMPT.template.md`

---

## Uninstallation

```bash
# Remove N-Grade system
rm -rf contracts/N-Grade

# Remove validator (if not used elsewhere)
rm scripts/validate_contract.py

# Remove validation reports
rm -rf _reports

# Remove dependencies (if in virtual env)
deactivate
rm -rf .venv
```

---

**Installation complete? Move to QUICKSTART.md to create your first contract!**

---

*Setup Guide Version: 1.0.0*  
*Last Updated: 2025-01*