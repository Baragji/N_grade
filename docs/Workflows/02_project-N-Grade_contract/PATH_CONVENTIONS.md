# Path Conventions for N-Grade Contract System

## Best Practice: Relative Paths from Repository Root

All paths in this system are **relative to the repository root** (`/Users/Yousef_1/Documents/GitHub/docs_ui_2/`).

### Why Relative Paths?

✅ **Portability**: Works regardless of where repo is cloned  
✅ **Consistency**: Same paths work across all files  
✅ **Simplicity**: No hardcoded absolute paths to maintain  
✅ **CI/CD Friendly**: Works in any build environment  

## Path Structure

```
docs_ui_2/                                          # Repository root
├── scripts/
│   └── validate_contract.py                        # Validator script
├── docs_ui_2_contracts/
│   └── N-Grade_contract/                           # Contract system directory
│       ├── documentation_delivery.contract.schema.json
│       ├── roadmap_v2_complete_expansion.contract.json
│       ├── CODEX_INSTRUCTION_PROMPT.md
│       ├── CONTRACT_ENFORCEMENT_GUIDE.md
│       ├── README.md
│       └── PATH_CONVENTIONS.md                     # This file
├── _reports/
│   └── roadmap_v2_validation.json                  # Generated report
└── autonomous_ai_roadmap_v2.md                     # Target deliverable
```

## How to Reference Paths

### In Contract Files (`.json`)

Use relative paths from repo root:

```json
{
  "deliverables": [
    {
      "file_path": "autonomous_ai_roadmap_v2.md",
      "quality_gates": {
        "json_schema_validation": {
          "schema_file": "docs_ui_2_contracts/N-Grade_contract/documentation_delivery.contract.schema.json"
        }
      }
    }
  ]
}
```

### In Commands (bash)

Always run commands **from repository root**:

```bash
# ✅ CORRECT - Run from repo root
cd /path/to/docs_ui_2
python scripts/validate_contract.py \
  docs_ui_2_contracts/N-Grade_contract/roadmap_v2_complete_expansion.contract.json

# ❌ WRONG - Don't use absolute paths
python /Users/Yousef_1/.../validate_contract.py /Users/Yousef_1/.../contract.json
```

### In Documentation (`.md`)

Reference paths relative to repo root:

```markdown
Read the contract at:
- `docs_ui_2_contracts/N-Grade_contract/roadmap_v2_complete_expansion.contract.json`

Run validator from repo root:
- `python scripts/validate_contract.py docs_ui_2_contracts/N-Grade_contract/...`
```

### In Python Code

Use `Path(__file__)` to find repo root dynamically:

```python
from pathlib import Path

# Find repo root (assuming script is in scripts/)
repo_root = Path(__file__).parent.parent

# Construct paths relative to root
contract_path = repo_root / "docs_ui_2_contracts" / "N-Grade_contract" / "contract.json"
```

## Schema Reference in Contracts

The `$schema` field uses a **relative path from the contract file**:

```json
{
  "$schema": "./documentation_delivery.contract.schema.json",
  "contract_id": "YOUR_CONTRACT"
}
```

This means: "Schema is in the same directory as this contract."

## Running from Different Directories

### ✅ Recommended: Always Run from Repo Root

```bash
cd /path/to/docs_ui_2
python scripts/validate_contract.py docs_ui_2_contracts/N-Grade_contract/contract.json
```

### ⚠️ If You Must Run from Elsewhere

Pass absolute path to contract, validator will auto-detect repo root:

```bash
cd ~/anywhere
python /path/to/docs_ui_2/scripts/validate_contract.py \
  /path/to/docs_ui_2/docs_ui_2_contracts/N-Grade_contract/contract.json
```

The validator script automatically finds the repository root based on the contract file location.

## Quick Reference

| Context | Path Style | Example |
|---------|------------|---------|
| **Contract JSON** | Relative to repo root | `autonomous_ai_roadmap_v2.md` |
| **Bash commands** | Relative to repo root (run from root) | `python scripts/validate_contract.py docs_ui_2_contracts/...` |
| **Documentation** | Relative to repo root | `` `docs_ui_2_contracts/N-Grade_contract/...` `` |
| **$schema field** | Relative to contract file | `./documentation_delivery.contract.schema.json` |
| **Python code** | Use `Path(__file__)` | `Path(__file__).parent.parent / "contracts"` |

## Creating New Contracts

When creating a new contract in this directory:

1. **Copy template:**
   ```bash
   cp docs_ui_2_contracts/N-Grade_contract/roadmap_v2_complete_expansion.contract.json \
      docs_ui_2_contracts/N-Grade_contract/my_new_contract.json
   ```

2. **Schema reference stays the same** (same directory):
   ```json
   {
     "$schema": "./documentation_delivery.contract.schema.json"
   }
   ```

3. **Update file paths** in deliverables (relative to repo root):
   ```json
   {
     "deliverables": [
       {
         "file_path": "path/to/your/file.md"
       }
     ]
   }
   ```

## Summary

🎯 **Golden Rule**: All paths are relative to repository root, except `$schema` which is relative to the contract file.

🚀 **Always run from**: Repository root directory

📝 **Path format**: `docs_ui_2_contracts/N-Grade_contract/file.json` (no leading `/`)

---

This keeps the system portable, maintainable, and CI/CD friendly.