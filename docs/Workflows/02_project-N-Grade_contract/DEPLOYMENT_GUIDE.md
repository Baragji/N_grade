# 🚀 N-Grade Contract System - Deployment Guide

How to package and deploy the N-Grade system to a new repository.

---

## Quick Deploy (5 Minutes)

### For New Clean Repo

```bash
# 1. In your NEW repo (where you want N-Grade)
cd /path/to/new/repo

# 2. Copy the entire system
mkdir -p contracts
cp -r /path/to/docs_ui_2/docs_ui_2_contracts/N-Grade_contract contracts/N-Grade

# 3. Copy validator to scripts
mkdir -p scripts
cp contracts/N-Grade/scripts/validate_contract.py scripts/

# 4. Create reports directory
mkdir -p _reports

# 5. Install dependencies
pip install jsonschema

# 6. Test it works
python scripts/validate_contract.py \
  contracts/N-Grade/examples/roadmap_v2_complete_expansion/contract.json

# ✅ If you see validation output, you're ready!
```

---

## Create Portable Package

### Option 1: Archive (Recommended)

```bash
# From source repo
cd /Users/Yousef_1/Documents/GitHub/docs_ui_2/docs_ui_2_contracts

# Create full package
tar -czf n-grade-system-v1.0.0-full.tar.gz N-Grade_contract/

# Create core-only package (minimal, ~50 KB)
tar -czf n-grade-system-v1.0.0-core.tar.gz \
  N-Grade_contract/scripts/validate_contract.py \
  N-Grade_contract/contracts/documentation_delivery.contract.schema.json \
  N-Grade_contract/contracts/template.contract.json \
  N-Grade_contract/SETUP.md \
  N-Grade_contract/QUICKSTART.md \
  N-Grade_contract/PACKAGE_README.md

# You now have:
# - n-grade-system-v1.0.0-full.tar.gz (~2.5 MB with docs/examples)
# - n-grade-system-v1.0.0-core.tar.gz (~50 KB minimal)
```

### Option 2: Git Repository

```bash
# Create standalone repo for N-Grade system
cd /tmp
mkdir n-grade-contracts
cd n-grade-contracts

# Copy system
cp -r /Users/Yousef_1/Documents/GitHub/docs_ui_2/docs_ui_2_contracts/N-Grade_contract/* .

# Initialize repo
git init
git add .
git commit -m "Initial commit: N-Grade Contract System v1.0.0"

# Push to remote (adjust URL)
git remote add origin https://github.com/your-org/n-grade-contracts.git
git branch -M main
git push -u origin main
```

### Option 3: Directory Sync

```bash
# Sync to cloud storage
rsync -av --progress \
  /Users/Yousef_1/Documents/GitHub/docs_ui_2/docs_ui_2_contracts/N-Grade_contract/ \
  ~/Dropbox/n-grade-system-v1.0.0/

# Or zip for sharing
cd /Users/Yousef_1/Documents/GitHub/docs_ui_2/docs_ui_2_contracts
zip -r n-grade-system-v1.0.0.zip N-Grade_contract/
```

---

## Deploy to New Repo

### From Archive

```bash
# In new repo
cd /path/to/new/repo
mkdir -p contracts/N-Grade

# Extract
tar -xzf /path/to/n-grade-system-v1.0.0-full.tar.gz -C contracts/

# Copy validator
mkdir -p scripts
cp contracts/N-Grade_contract/scripts/validate_contract.py scripts/

# Install dependencies
pip install jsonschema

# Test
python scripts/validate_contract.py \
  contracts/N-Grade_contract/examples/roadmap_v2_complete_expansion/contract.json
```

### From Git Repo

```bash
# In new repo
cd /path/to/new/repo

# Add as submodule (tracks updates)
git submodule add https://github.com/your-org/n-grade-contracts.git contracts/N-Grade

# Or clone directly (no tracking)
git clone https://github.com/your-org/n-grade-contracts.git contracts/N-Grade

# Copy validator
mkdir -p scripts
cp contracts/N-Grade/scripts/validate_contract.py scripts/

# Install dependencies
pip install jsonschema

# Commit
git add contracts/N-Grade scripts/validate_contract.py
git commit -m "Add N-Grade contract system"
```

---

## Verify Installation

### Quick Test

```bash
# 1. Validator exists and is executable
ls -l scripts/validate_contract.py

# 2. Can import dependencies
python -c "import jsonschema; print('✅ jsonschema installed')"

# 3. Validator runs
python scripts/validate_contract.py --help

# 4. Example contract validates
python scripts/validate_contract.py \
  contracts/N-Grade/examples/roadmap_v2_complete_expansion/contract.json

# 5. Check exit code
echo $?  # Should print 0 or 1 (validator working)
```

### Full Test

```bash
# Create test contract
cat > contracts/test_install.contract.json << 'EOF'
{
  "$schema": "./N-Grade/contracts/documentation_delivery.contract.schema.json",
  "contract_id": "TEST_INSTALL",
  "deliverables": [
    {
      "file_path": "test_doc.md",
      "quality_gates": {
        "line_count": {"min": 1}
      }
    }
  ],
  "definition_of_done": {
    "all_deliverables_present": true,
    "all_quality_gates_passed": true
  }
}
EOF

# Create test deliverable
echo "# Test" > test_doc.md

# Validate
python scripts/validate_contract.py contracts/test_install.contract.json

# Should ACCEPT (exit 0)
echo $?

# Clean up
rm contracts/test_install.contract.json test_doc.md _reports/test_install_validation.json
```

---

## Post-Installation Setup

### 1. Configure .gitignore

Add to your repo's `.gitignore`:

```gitignore
# N-Grade validation reports (auto-generated)
_reports/*.json

# Python
__pycache__/
*.pyc
*.pyo
.venv/
venv/

# System files
.DS_Store
Thumbs.db
```

### 2. Add to README

Add to your repository's `README.md`:

```markdown
## Quality Enforcement

This repository uses the [N-Grade Contract System](contracts/N-Grade/) for enforcing AI deliverable quality.

**Quick start:**
1. Create contract: `cp contracts/N-Grade/contracts/template.contract.json contracts/my_deliverable.json`
2. Edit contract to define requirements
3. Hand to AI with validation command
4. Validate: `python scripts/validate_contract.py contracts/my_deliverable.json`
5. Accept only if exit code is 0

**Documentation:** `contracts/N-Grade/PACKAGE_README.md`
```

### 3. Set Up CI/CD (Optional)

**GitHub Actions:**

Create `.github/workflows/validate_contracts.yml`:

```yaml
name: Validate Deliverables
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
      
      - name: Find active contracts
        id: contracts
        run: |
          # Find all .contract.json files
          echo "contracts=$(find contracts -name '*.contract.json' -not -path '*/examples/*' | tr '\n' ' ')" >> $GITHUB_OUTPUT
      
      - name: Validate contracts
        run: |
          for contract in ${{ steps.contracts.outputs.contracts }}; do
            echo "Validating $contract"
            python scripts/validate_contract.py "$contract"
            if [ $? -ne 0 ]; then
              echo "❌ Validation failed for $contract"
              exit 1
            fi
          done
          echo "✅ All contracts passed"
```

### 4. Create Your First Contract

```bash
# Copy template
cp contracts/N-Grade/contracts/template.contract.json contracts/first_deliverable.contract.json

# Edit contract
nano contracts/first_deliverable.contract.json

# Read quick start guide
cat contracts/N-Grade/QUICKSTART.md

# Follow the 5-minute tutorial
```

---

## Directory Structure After Deployment

```
new-repo/
├── .git/
├── .gitignore                                   ← Updated
├── README.md                                    ← Updated
│
├── contracts/
│   ├── N-Grade/                                 ← Deployed system
│   │   ├── PACKAGE_README.md
│   │   ├── SETUP.md
│   │   ├── QUICKSTART.md
│   │   ├── DEPLOYMENT_GUIDE.md
│   │   ├── PACKAGE_MANIFEST.md
│   │   ├── scripts/
│   │   │   └── validate_contract.py
│   │   ├── contracts/
│   │   │   ├── documentation_delivery.contract.schema.json
│   │   │   ├── template.contract.json
│   │   │   └── example_roadmap.contract.json
│   │   ├── docs/
│   │   │   ├── README.md
│   │   │   ├── CONTRACT_ENFORCEMENT_GUIDE.md
│   │   │   ├── PATH_CONVENTIONS.md
│   │   │   ├── MIGRATION_NOTES.md
│   │   │   └── CODEX_INSTRUCTION_PROMPT.template.md
│   │   └── examples/
│   │       └── roadmap_v2_complete_expansion/
│   │           ├── contract.json
│   │           ├── instruction_prompt.md
│   │           ├── validation_report.json
│   │           └── README.md
│   │
│   └── your_contracts/                          ← Your contracts here
│       └── first_deliverable.contract.json
│
├── scripts/
│   └── validate_contract.py                     ← Copied from N-Grade
│
├── _reports/                                    ← Auto-generated
│   └── validation_*.json
│
└── docs/                                        ← Your deliverables
    └── your_documents.md
```

---

## Multiple Repo Deployment

### Scenario 1: Many Independent Repos

**Approach:** Copy full package to each

```bash
# Script to deploy to multiple repos
#!/bin/bash

REPOS=(
  "/path/to/repo1"
  "/path/to/repo2"
  "/path/to/repo3"
)

SOURCE="/Users/Yousef_1/Documents/GitHub/docs_ui_2/docs_ui_2_contracts/N-Grade_contract"

for repo in "${REPOS[@]}"; do
  echo "Deploying to $repo"
  
  mkdir -p "$repo/contracts/N-Grade"
  cp -r "$SOURCE/"* "$repo/contracts/N-Grade/"
  
  mkdir -p "$repo/scripts"
  cp "$SOURCE/scripts/validate_contract.py" "$repo/scripts/"
  
  echo "✅ Deployed to $repo"
done
```

### Scenario 2: Shared Organization

**Approach:** Git submodule

```bash
# Create central repo once
cd /tmp
git clone https://github.com/org/n-grade-contracts.git

# In each project repo
cd /path/to/project
git submodule add https://github.com/org/n-grade-contracts.git contracts/N-Grade
cp contracts/N-Grade/scripts/validate_contract.py scripts/

# Update all projects later
cd /path/to/project
git submodule update --remote contracts/N-Grade
```

### Scenario 3: Monorepo

**Approach:** Single installation, shared by all projects

```
monorepo/
├── shared/
│   └── n-grade/              ← Single installation
│       └── ...
├── projects/
│   ├── project-a/
│   │   └── contracts/        ← Reference shared system
│   ├── project-b/
│   │   └── contracts/
│   └── project-c/
│       └── contracts/
└── scripts/
    └── validate_contract.py  ← References shared system
```

---

## Update/Upgrade Process

### Check for Updates

```bash
# If using Git submodule
cd /path/to/repo/contracts/N-Grade
git fetch origin
git log HEAD..origin/main --oneline

# If updates available
cd /path/to/repo
git submodule update --remote contracts/N-Grade
```

### Manual Update

```bash
# Download new version
cd /tmp
tar -xzf n-grade-system-v1.1.0.tar.gz

# Backup current
cd /path/to/repo
mv contracts/N-Grade contracts/N-Grade.backup

# Deploy new version
cp -r /tmp/N-Grade_contract contracts/N-Grade

# Test
python scripts/validate_contract.py \
  contracts/N-Grade/examples/roadmap_v2_complete_expansion/contract.json

# If working, remove backup
rm -rf contracts/N-Grade.backup
```

---

## Troubleshooting Deployment

### Issue: "No module named 'jsonschema'"

```bash
# Install in correct environment
pip install jsonschema

# If using venv
source .venv/bin/activate
pip install jsonschema
```

### Issue: "Contract file not found"

```bash
# Check path is relative to repo root
pwd  # Should be at repo root

# Verify file exists
ls -l contracts/your_contract.json

# Run from repo root
python scripts/validate_contract.py contracts/your_contract.json
```

### Issue: "Permission denied on validator"

```bash
chmod +x scripts/validate_contract.py
```

### Issue: "Schema not found"

```bash
# Verify schema exists
ls contracts/N-Grade/contracts/documentation_delivery.contract.schema.json

# Check $schema path in contract is relative to contract file
cat contracts/your_contract.json | grep schema
# Should be: "./N-Grade/contracts/documentation_delivery.contract.schema.json"
```

---

## Rollback/Uninstall

### Remove N-Grade System

```bash
# Remove system directory
rm -rf contracts/N-Grade

# Remove validator (if not used elsewhere)
rm scripts/validate_contract.py

# Remove reports
rm -rf _reports

# Remove from git
git rm -rf contracts/N-Grade scripts/validate_contract.py
git commit -m "Remove N-Grade system"
```

### Restore Previous Version

```bash
# If you have backup
mv contracts/N-Grade.backup contracts/N-Grade

# Or from git history
git checkout HEAD~1 -- contracts/N-Grade scripts/validate_contract.py
```

---

## Next Steps After Deployment

1. ✅ **Read:** `contracts/N-Grade/QUICKSTART.md` (5 minutes)
2. ✅ **Create:** Your first contract from template
3. ✅ **Test:** Validate a simple deliverable
4. ✅ **Document:** Update project README with contract info
5. ✅ **Integrate:** Add validation to CI/CD
6. ✅ **Scale:** Create contracts for all AI deliverables

---

## Support

### Documentation
- **Package overview:** `contracts/N-Grade/PACKAGE_README.md`
- **Installation:** `contracts/N-Grade/SETUP.md`
- **Quick start:** `contracts/N-Grade/QUICKSTART.md`
- **Complete guide:** `contracts/N-Grade/docs/CONTRACT_ENFORCEMENT_GUIDE.md`

### Troubleshooting
- Check `contracts/N-Grade/SETUP.md` troubleshooting section
- Review `contracts/N-Grade/examples/` for working configurations
- Consult `contracts/N-Grade/docs/PATH_CONVENTIONS.md` for path issues

---

**Deployment complete? Start with QUICKSTART.md to create your first contract!** 🚀

---

*Deployment Guide Version: 1.0.0*  
*Last Updated: 2025-01*