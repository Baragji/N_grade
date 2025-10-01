# Documentation Contracts Directory

## Overview

This directory contains **contract-based enforcement systems** for AI deliverables.

## Current Systems

### 🔥 N-Grade Contract System

**Location:** `N-Grade_contract/`

**Purpose:** Nuclear-grade enforcement of complete, production-ready documentation deliverables with ZERO TOLERANCE for shortcuts.

**Key Features:**
- Machine-parseable contracts (JSON)
- Automated validation with exit codes (0=ACCEPT, 1=REJECT)
- Quality gates: line counts, code blocks, metrics, forbidden patterns
- Self-validation workflow for AI agents

**Quick Start:**
```bash
# Read the system documentation
cat docs_ui_2_contracts/N-Grade_contract/README.md

# Review contract for Roadmap v2
cat docs_ui_2_contracts/N-Grade_contract/roadmap_v2_complete_expansion.contract.json

# Validate a delivery (run from repo root)
python scripts/validate_contract.py \
  docs_ui_2_contracts/N-Grade_contract/roadmap_v2_complete_expansion.contract.json
```

**Documentation:**
- `N-Grade_contract/README.md` - Quick start guide
- `N-Grade_contract/CONTRACT_ENFORCEMENT_GUIDE.md` - Complete guide
- `N-Grade_contract/CODEX_INSTRUCTION_PROMPT.md` - Ready-to-copy instructions for AI agents
- `N-Grade_contract/PATH_CONVENTIONS.md` - Path structure and best practices

## Directory Structure

```
docs_ui_2_contracts/
├── README.md                                    # This file
├── N-Grade_contract/                            # Nuclear-grade contract system
│   ├── documentation_delivery.contract.schema.json
│   ├── roadmap_v2_complete_expansion.contract.json
│   ├── README.md
│   ├── CONTRACT_ENFORCEMENT_GUIDE.md
│   ├── CODEX_INSTRUCTION_PROMPT.md
│   └── PATH_CONVENTIONS.md
└── [future contract systems]/
```

## Path Conventions

**All paths are relative to repository root.**

When running commands:
```bash
# Always from repo root
cd /path/to/docs_ui_2
python scripts/validate_contract.py docs_ui_2_contracts/N-Grade_contract/...
```

See `N-Grade_contract/PATH_CONVENTIONS.md` for details.

## Creating New Contract Systems

To create a new contract system:

1. **Create directory:**
   ```bash
   mkdir docs_ui_2_contracts/YourSystem_contract
   ```

2. **Copy N-Grade system as template:**
   ```bash
   cp docs_ui_2_contracts/N-Grade_contract/*.json \
      docs_ui_2_contracts/YourSystem_contract/
   ```

3. **Customize for your use case:**
   - Edit schema and contract files
   - Update quality gates
   - Adjust forbidden/required patterns
   - Document your system

4. **Maintain path conventions:**
   - Use relative paths from repo root
   - Keep schema in same directory as contracts
   - Document all path references

## Philosophy

**Contract-based enforcement provides:**
- ✅ **Clear requirements** - No ambiguity about "done"
- ✅ **Automated validation** - No human review fatigue
- ✅ **Zero tolerance** - Machine doesn't negotiate
- ✅ **Self-validation** - AI agents check their own work
- ✅ **Reproducible** - Same contract = same requirements

**This prevents:**
- ❌ Half-assed deliverables
- ❌ Template placeholders
- ❌ Copy-paste errors
- ❌ Missing details
- ❌ Back-and-forth review cycles

## Support

- **N-Grade System Issues:** See `N-Grade_contract/README.md`
- **Path Questions:** See `N-Grade_contract/PATH_CONVENTIONS.md`
- **Creating Contracts:** See `N-Grade_contract/CONTRACT_ENFORCEMENT_GUIDE.md`

---

**NO MORE HALF-ASSED DELIVERIES. CONTRACTS OR GTFO.**