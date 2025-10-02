# Phase 0 Foundation Build Instructions
## ⚠️ CONTRACT-BASED DELIVERY - ZERO TOLERANCE ENFORCEMENT

**READ THIS ENTIRE DOCUMENT BEFORE STARTING WORK.**

---

## 🎯 CRITICAL INFORMATION

### Contract File
```
/contracts/phase_0_foundation.contract.json
```

### Validation Command
```bash
python3 scripts/validate_contract.py \
  contracts/phase_0_foundation.contract.json \
  --report-path evidence/validation/phase0_contract_validation.json
```

### Acceptance Criteria
- ✅ Validator MUST exit with code `0` (ACCEPTED)
- ❌ If exit code is `1` (REJECTED), delivery will be sent back for fixes
- 🚫 **NO EXCEPTIONS. NO NEGOTIATION.**

---

## 📋 MANDATORY CONTRACT ENFORCEMENT

You are receiving a **CONTRACT-BASED DELIVERY REQUEST** with **ZERO TOLERANCE** for incomplete work.

### What This Means

1. **Read the Contract First**
   - Open `contracts/phase_0_foundation.contract.json`
   - Understand ALL `quality_gates` (MANDATORY requirements)
   - Note `forbidden_patterns` (trigger AUTOMATIC REJECTION)
   - Check `required_patterns` (content that MUST appear)
   - Review `definition_of_done` (ALL must be `true` for acceptance)

2. **Self-Validate Before Submission**
   - Run validator yourself BEFORE submitting
   - Fix ALL failures until exit code is `0`
   - DO NOT DELIVER until validation passes

3. **Structured Output Required**
   - Generate machine-readable validation report
   - No prose excuses if validation fails
   - Status must be objective: PASS or FAIL

---

## 🎓 REQUIRED READING (Before You Start)

You MUST read these documents to understand context and standards:

1. **`/docs/00_Plans_&_Data/autonomous_ai_roadmap_v2.md`**
   - Focus: Phase 0 sections, gate criteria, evidence paths
   - Why: Defines 26-week timeline, 9 phases, canonical directory structure

2. **`/docs/00_Plans_&_Data/autonomous_ai_coding_system_taxonomy_ssot_v1.2.md`**
   - Focus: Functions #17, #21, #36, #40 (Priority=Required, Gate=G0-G2)
   - Why: Defines capability taxonomy that Phase 0 must support

3. **`/docs/Workflows/01_project-Agentic_prompt_guide/Gap_Analysis_Missing_Best_Practices.md`**
   - Focus: 7 critical best practices (TDD, iteration limits, evidence requirements, DoD tables)
   - Why: Defines quality standards for all deliverables

4. **`/docs/Workflows/WORKFLOW_MERGE_PROJECT_OVERVIEW.md`**
   - Focus: Merge strategy (UMCA governance + H3A orchestration + N-Grade validation + EXE MVP patterns)
   - Why: Explains why we're building what we're building

---

## 🚀 MISSION & CONTEXT

### Goal: G0 Foundation Ready

**Definition:**
- ✅ Repository bootstrapped with canonical structure (40+ directories)
- ✅ Strategic charter approved by 4+ stakeholders
- ✅ CI/CD pipeline online with lint, test, security workflows
- ✅ Docker environment healthy (postgres, redis, meilisearch, app)
- ✅ Branch protection enforced on main branch
- ✅ All evidence artifacts generated and validated

### What You're Building

Phase 0 is the **FOUNDATION** for a 26-week, €250k autonomous AI coding system. You're not building the system itself - you're building the infrastructure, governance, and validation framework that the system will be built ON TOP OF.

Think of it like building a construction site before building a skyscraper:
- 🏗️ **Not building:** The skyscraper (that's Phases 1-8)
- ✅ **Building:** Foundation, safety barriers, tool storage, inspection checkpoints

---

## 📦 DELIVERABLES (15 Files)

Your contract requires **15 deliverables** organized into 4 groups:

### Group 1: Governance & Strategy (4 files)
1. `docs/strategy/charter.md` (200-400 lines)
2. `docs/strategy/charter.yaml` (30-100 lines)
3. `docs/governance/raci_phase0.csv` (12+ lines, 10+ roles)
4. `evidence/approvals/phase0_charter.json` (10+ lines, 4+ approvals)

### Group 2: Repository Structure (3 files)
5. `scripts/bootstrap_repo.sh` (80-200 lines, creates 40+ dirs)
6. `scripts/validate_structure.py` (50-150 lines)
7. `docs/governance/branch_protection.md` (40-100 lines)

### Group 3: Development Environment (4 files)
8. `docker-compose.yml` (60-150 lines, 4 services)
9. `docker/Dockerfile` (30-80 lines, multi-stage)
10. `scripts/install_dev_tools.sh` (40-120 lines)
11. `docs/development/environment_setup.md` (80-200 lines)
12. `.env.example` (20-60 lines, 15+ vars)

### Group 4: CI/CD Pipeline (3 files)
13. `.github/workflows/ci.yml` (50-150 lines)
14. `.github/workflows/security.yml` (40-120 lines)
15. `.github/workflows/gate_validation.yml` (30-100 lines)

### Group 5: Evidence Artifact (1 file)
16. `evidence/gates/g0_foundation.json` (15+ lines)

**Each file has strict quality gates in the contract. Read them carefully.**

---

## 🎯 QUALITY GATES SUMMARY

### Forbidden Patterns (ZERO TOLERANCE)

If ANY deliverable contains these, AUTOMATIC REJECTION:
- ❌ `TODO`, `TBD`, `FIXME` — No incomplete sections
- ❌ `(template)`, `[FILL IN]` — No placeholder markers
- ❌ `...` — No ellipsis indicating omitted content
- ❌ `See original`, `Refer to` — Must be standalone
- ❌ Hardcoded weak passwords (`admin`, `root`, `123`)
- ❌ Dangerous commands (`rm -rf /`)

### Required Patterns (Minimum Thresholds)

Each deliverable must meet minimum occurrence counts:
- ✅ Code blocks (where applicable): varies by file
- ✅ Evidence paths: `evidence/` references
- ✅ Compliance frameworks: EU AI Act, ISO 42001, GDPR
- ✅ Budget amounts: €250,000 total, €41,700 monthly
- ✅ Phase references: Phase 0-8 (all 9 phases)
- ✅ Health checks: All Docker services must have healthcheck

### Structural Requirements

- ✅ Scripts must have shebang (`#!/bin/bash` or `#!/usr/bin/env python3`)
- ✅ Scripts must use safe settings (`set -euo pipefail` for bash)
- ✅ Scripts must return proper exit codes (0=success, 1=failure)
- ✅ Documentation must have headers, lists, code examples
- ✅ YAML/JSON must be syntactically valid
- ✅ CSV must have required columns and no empty cells

### Cross-File Validations

1. **Budget Consistency:** Charter.md EUR amount = charter.yaml `budget_eur`
2. **Evidence Paths:** All paths in charter.yaml must exist as deliverables
3. **Docker Env:** Variables in docker-compose.yml must exist in .env.example
4. **Phase Timeline:** Charter must reference all 9 phases across 26 weeks

---

## 🛠️ IMPLEMENTATION GUIDANCE

### Task 0.0: Strategic Charter & Governance (60 min)

**What to Build:**
1. `docs/strategy/charter.md` — Prose document with:
   - Problem statement (why this system?)
   - Success criteria (7+ measurable outcomes)
   - Budget ceiling (€250k total, breakdown by phase if helpful)
   - Regulatory obligations (EU AI Act GPAI, ISO 42001, GDPR)
   - Risks & mitigations (5+ risks with mitigation strategies)
   - Timeline (26 weeks, Phase 0-8 with week ranges)

2. `docs/strategy/charter.yaml` — Machine-readable spec with:
   - `initiative` name
   - `mission` statement
   - `budget_eur: 250000`
   - `stakeholders` list (10+ roles: Architecture Lead, Security Officer, Compliance Lead, Finance Controller, Product Director, QA Manager, DevOps Lead, Data Privacy Officer, Legal Counsel, Executive Sponsor)
   - `steering_cadence_days: 7` (weekly)
   - `success_metrics` with evidence paths:
     - `charter_signoff → evidence/approvals/phase0_charter.json`
     - `g0_gate_passed → evidence/gates/g0_foundation.json`
     - `env_bootstrap_time_hours: 2 → evidence/quality/env_bootstrap_time.json`
     - `compliance_mapping_complete → evidence/compliance/control_mapping.json`

3. `docs/governance/raci_phase0.csv` — RACI matrix:
   ```csv
   Activity,Architecture Lead,Security Officer,Compliance Lead,Finance Controller,Product Director,QA Manager,DevOps Lead,Data Privacy Officer,Legal Counsel,Executive Sponsor
   Charter Approval,C,C,A,R,C,I,I,I,C,R
   Repository Setup,A,I,I,I,I,R,R,I,I,C
   Docker Environment,C,R,I,I,I,R,A,I,I,I
   CI/CD Pipeline,R,A,I,I,I,R,A,I,I,C
   Branch Protection,C,A,I,I,I,R,R,I,I,C
   Budget Tracking,I,I,C,A,R,I,I,I,C,R
   Compliance Mapping,C,C,A,I,C,I,I,R,A,C
   G0 Gate Validation,R,C,C,C,A,R,C,C,C,R
   Risk Management,C,A,C,C,R,C,C,C,A,R
   Stakeholder Communication,C,C,C,C,A,C,C,C,C,R
   ```
   (Minimum 10 activities, 10 roles - adjust as needed)

4. `evidence/approvals/phase0_charter.json`:
   ```json
   {
     "charter_version": "1.0",
     "approval_date": "2025-01-15",
     "approvers": [
       {"role": "Architecture Lead", "approved": true, "timestamp": "2025-01-15T10:00:00Z"},
       {"role": "Compliance Lead", "approved": true, "timestamp": "2025-01-15T10:30:00Z"},
       {"role": "Finance Controller", "approved": true, "timestamp": "2025-01-15T11:00:00Z"},
       {"role": "Executive Sponsor", "approved": true, "timestamp": "2025-01-15T14:00:00Z"}
     ],
     "signed_artifact": "docs/strategy/charter.md",
     "verification_hash": "sha256:<generate actual SHA-256 of charter.md after creating it>"
   }
   ```

**How to Generate SHA-256:**
```bash
# After creating charter.md, run:
sha256sum docs/strategy/charter.md
# Or on macOS:
shasum -a 256 docs/strategy/charter.md
# Copy the hash into phase0_charter.json
```

**Success Criteria:**
- ✅ Charter addresses all sections from contract (Problem, Success, Budget, Compliance, Risks, Timeline)
- ✅ Charter.yaml is valid YAML with all required fields
- ✅ RACI has 10+ roles and 10+ activities
- ✅ Approval JSON has 4+ approvals, all `approved: true`, valid SHA-256

---

### Task 0.1: Repository Structure (45 min)

**What to Build:**
1. `scripts/bootstrap_repo.sh` — Bash script that creates:
   ```bash
   #!/bin/bash
   set -euo pipefail
   
   # Evidence directories (from autonomous_ai_roadmap_v2.md)
   mkdir -p evidence/gates
   mkdir -p evidence/approvals
   mkdir -p evidence/quality
   mkdir -p evidence/compliance
   mkdir -p evidence/security
   mkdir -p evidence/metrics
   mkdir -p evidence/artifacts
   mkdir -p evidence/validation
   
   # State management (from H3A Distribution)
   mkdir -p state/sessions
   mkdir -p state/checkpoints
   mkdir -p state/history
   
   # Governance (from UMCA)
   mkdir -p docs/governance
   mkdir -p docs/strategy
   mkdir -p docs/development
   mkdir -p docs/architecture
   mkdir -p docs/compliance
   
   # Agent components (future Phase 1-2)
   mkdir -p src/orchestrator
   mkdir -p src/executor
   mkdir -p src/planner
   mkdir -p src/validator
   mkdir -p src/state_manager
   mkdir -p src/llm_gateway
   
   # Tests (TDD from Agentic Prompt Guide)
   mkdir -p tests/unit
   mkdir -p tests/integration
   mkdir -p tests/fixtures
   
   # CI/CD
   mkdir -p .github/workflows
   mkdir -p .github/actions
   
   # Docker
   mkdir -p docker
   
   # Scripts
   mkdir -p scripts
   
   # Contracts (N-Grade)
   mkdir -p contracts
   
   # Create README stubs
   echo "# Evidence Directory" > evidence/README.md
   echo "# State Management" > state/README.md
   echo "# Governance Documentation" > docs/governance/README.md
   # ... (create README for all major dirs)
   
   echo "✅ Repository structure created (40+ directories)"
   ```

2. `scripts/validate_structure.py` — Python validator:
   ```python
   #!/usr/bin/env python3
   import json
   import sys
   from pathlib import Path
   
   REQUIRED_DIRS = [
       "evidence/gates",
       "evidence/approvals",
       "state/sessions",
       "docs/governance",
       "src/orchestrator",
       "tests/unit",
       # ... (list all 40+ required directories)
   ]
   
   def validate_structure():
       repo_root = Path(__file__).parent.parent
       missing = []
       
       for dir_path in REQUIRED_DIRS:
           full_path = repo_root / dir_path
           if not full_path.exists():
               missing.append(dir_path)
       
       result = {
           "validation_type": "repository_structure",
           "timestamp": "2025-01-15T12:00:00Z",
           "required_directories": len(REQUIRED_DIRS),
           "found_directories": len(REQUIRED_DIRS) - len(missing),
           "missing_directories": missing,
           "status": "PASS" if len(missing) == 0 else "FAIL"
       }
       
       output_path = repo_root / "evidence" / "validation" / "structure_validation.json"
       output_path.parent.mkdir(parents=True, exist_ok=True)
       with open(output_path, 'w') as f:
           json.dump(result, f, indent=2)
       
       print(f"✅ Structure validation: {result['status']}")
       print(f"📊 Found: {result['found_directories']}/{result['required_directories']} directories")
       if missing:
           print(f"❌ Missing: {', '.join(missing)}")
       
       return 0 if len(missing) == 0 else 1
   
   if __name__ == "__main__":
       sys.exit(validate_structure())
   ```

3. `docs/governance/branch_protection.md` — Documentation:
   - Branch protection rules for `main` and `develop`
   - Required status checks (CI, security, gate validation)
   - Review requirements (1+ approvals, dismiss stale reviews)
   - Configuration examples (GitHub API, CLI, or UI)

**Success Criteria:**
- ✅ bootstrap_repo.sh creates 40+ directories
- ✅ validate_structure.py checks all required paths
- ✅ Branch protection doc has configuration examples
- ✅ All scripts are idempotent (safe to re-run)

---

### Task 0.2: Development Environment (60 min)

**What to Build:**
1. `docker-compose.yml`:
   ```yaml
   version: '3.9'
   
   services:
     app:
       build:
         context: .
         dockerfile: docker/Dockerfile
       ports:
         - "3000:3000"
       environment:
         - POSTGRES_HOST=postgres
         - REDIS_HOST=redis
         - MEILISEARCH_HOST=meilisearch
       depends_on:
         postgres:
           condition: service_healthy
         redis:
           condition: service_healthy
         meilisearch:
           condition: service_healthy
       healthcheck:
         test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
         interval: 30s
         timeout: 10s
         retries: 3
       volumes:
         - ./src:/app/src:ro
         - ./output:/app/output
     
     postgres:
       image: postgres:16-alpine
       environment:
         POSTGRES_DB: ${POSTGRES_DB:-autonomous_ai}
         POSTGRES_USER: ${POSTGRES_USER:-dbuser}
         POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
       ports:
         - "5432:5432"
       volumes:
         - postgres_data:/var/lib/postgresql/data
       healthcheck:
         test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-dbuser}"]
         interval: 10s
         timeout: 5s
         retries: 5
     
     redis:
       image: redis:7-alpine
       ports:
         - "6379:6379"
       volumes:
         - redis_data:/data
       healthcheck:
         test: ["CMD", "redis-cli", "ping"]
         interval: 10s
         timeout: 5s
         retries: 5
     
     meilisearch:
       image: getmeili/meilisearch:v1.5
       environment:
         MEILI_MASTER_KEY: ${MEILI_MASTER_KEY}
         MEILI_ENV: development
       ports:
         - "7700:7700"
       volumes:
         - meilisearch_data:/meili_data
       healthcheck:
         test: ["CMD", "curl", "-f", "http://localhost:7700/health"]
         interval: 30s
         timeout: 10s
         retries: 3
   
   volumes:
     postgres_data:
     redis_data:
     meilisearch_data:
   
   networks:
     default:
       name: autonomous_ai_network
   ```

2. `docker/Dockerfile`:
   ```dockerfile
   # Build stage
   FROM node:20-alpine AS builder
   
   WORKDIR /build
   COPY package*.json ./
   RUN npm ci --only=production
   
   COPY src ./src
   COPY tsconfig.json ./
   RUN npm run build
   
   # Runtime stage
   FROM node:20-alpine AS runtime
   
   # Create non-root user
   RUN addgroup -g 1001 appgroup && \
       adduser -u 1001 -G appgroup -s /bin/sh -D appuser
   
   WORKDIR /app
   
   # Copy built artifacts
   COPY --from=builder --chown=appuser:appgroup /build/node_modules ./node_modules
   COPY --from=builder --chown=appuser:appgroup /build/dist ./dist
   COPY --chown=appuser:appgroup package.json ./
   
   # Switch to non-root user
   USER appuser
   
   EXPOSE 3000
   
   HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
     CMD node -e "require('http').get('http://localhost:3000/health', (r) => process.exit(r.statusCode === 200 ? 0 : 1))"
   
   CMD ["node", "dist/server.js"]
   ```

3. `scripts/install_dev_tools.sh`:
   - Check for Docker, install if missing
   - Check for Python 3.10+, install if missing
   - Check for Node.js 20+, install if missing
   - Install pre-commit hooks
   - Verify installations

4. `docs/development/environment_setup.md`:
   - Prerequisites list (OS, hardware, network)
   - Installation steps (numbered, with commands)
   - Verification commands (`docker compose ps`, `python --version`, etc.)
   - Troubleshooting common issues
   - **Bootstrap time target: <2 hours**

5. `.env.example`:
   ```bash
   # Database Configuration
   POSTGRES_HOST=postgres
   POSTGRES_PORT=5432
   POSTGRES_DB=autonomous_ai
   POSTGRES_USER=dbuser
   POSTGRES_PASSWORD=CHANGE_ME_STRONG_PASSWORD
   
   # Redis Configuration
   REDIS_HOST=redis
   REDIS_PORT=6379
   REDIS_PASSWORD=CHANGE_ME_REDIS_PASSWORD
   
   # Meilisearch Configuration
   MEILI_HOST=http://meilisearch:7700
   MEILI_MASTER_KEY=CHANGE_ME_MEILI_KEY
   
   # Application Configuration
   NODE_ENV=development
   PORT=3000
   LOG_LEVEL=info
   
   # LLM Configuration (Phase 1+)
   LLM_PROVIDER=openai
   OPENAI_API_KEY=sk-...
   ANTHROPIC_API_KEY=sk-ant-...
   
   # Evidence Storage
   EVIDENCE_PATH=./evidence
   STATE_PATH=./state
   ```

**Success Criteria:**
- ✅ docker-compose.yml has 4 services, all with health checks
- ✅ Dockerfile uses multi-stage build, non-root user
- ✅ .env.example has 15+ variables with comments
- ✅ Environment setup doc estimates <2 hour bootstrap

---

### Task 0.3: CI/CD Pipeline (45 min)

**What to Build:**
1. `.github/workflows/ci.yml`:
   - Triggers: push to main, pull_request
   - Jobs: lint, test, build
   - Runs: ESLint, Prettier, vitest, TypeScript compile
   - Uploads: test results, coverage reports
   - Target runtime: <12 minutes

2. `.github/workflows/security.yml`:
   - Triggers: push to main, schedule (weekly)
   - Jobs: SAST (Semgrep or CodeQL), dependency scan (Trivy), SBOM generation (Syft)
   - Uploads: SARIF reports, SBOM artifacts

3. `.github/workflows/gate_validation.yml`:
   - Triggers: workflow_dispatch (manual), push to main
   - Jobs: validate gate criteria, check evidence artifacts
   - Runs: `python scripts/validate_gates.py` (you'll create this in future phase)
   - Uploads: gate validation reports

**Success Criteria:**
- ✅ CI workflow includes lint, test, build jobs
- ✅ Security workflow includes SAST, dependency scan, SBOM
- ✅ Gate validation workflow checks evidence paths
- ✅ All workflows upload artifacts

---

### Task 0.4: G0 Gate Evidence (15 min)

**What to Build:**
1. `evidence/gates/g0_foundation.json`:
   ```json
   {
     "gate_id": "G0",
     "gate_name": "Foundation Ready",
     "status": "PASS",
     "validation_timestamp": "2025-01-15T16:00:00Z",
     "criteria": [
       {
         "criterion": "Repository structure complete",
         "status": "PASS",
         "evidence": "evidence/validation/structure_validation.json"
       },
       {
         "criterion": "Strategic charter approved",
         "status": "PASS",
         "evidence": "evidence/approvals/phase0_charter.json"
       },
       {
         "criterion": "Docker services healthy",
         "status": "PASS",
         "evidence": "docker compose ps shows 4/4 healthy"
       },
       {
         "criterion": "CI/CD pipelines configured",
         "status": "PASS",
         "evidence": ".github/workflows/ contains 3 workflows"
       },
       {
         "criterion": "Branch protection enforced",
         "status": "PASS",
         "evidence": "docs/governance/branch_protection.md"
       },
       {
         "criterion": "Environment bootstrap time <2 hours",
         "status": "PASS",
         "evidence": "docs/development/environment_setup.md"
       },
       {
         "criterion": "All deliverables present",
         "status": "PASS",
         "evidence": "Contract validator returned exit code 0"
       },
       {
         "criterion": "No forbidden patterns found",
         "status": "PASS",
         "evidence": "Contract validation report"
       }
     ],
     "gate_approved_by": "Automated Validator",
     "next_gate": "G1",
     "next_phase": "Phase 1 - Core Architecture"
   }
   ```

**Success Criteria:**
- ✅ G0 gate JSON has all 8 criteria marked PASS
- ✅ Status field is "PASS"
- ✅ Evidence paths reference actual deliverables

---

## ✅ SELF-VALIDATION CHECKLIST

Before submitting, YOU MUST:

### 1. Run Contract Validator
```bash
python3 scripts/validate_contract.py contracts/phase_0_foundation.contract.json
```

**Expected output:**
```
✅ ACCEPTED
All quality gates passed.
Exit code: 0
```

**If you see exit code 1:**
- Read the validation report at `evidence/validation/phase0_contract_validation.json`
- Fix ALL failures (CRITICAL and ERROR severity)
- Re-run validator until exit code is 0

### 2. Run Structure Validator
```bash
python3 scripts/validate_structure.py
```

**Expected:**
- Exit code: 0
- Output: "Found: 40+/40+ directories"

### 3. Test Docker Environment
```bash
docker compose up -d
docker compose ps
```

**Expected:**
- All 4 services show STATUS: healthy
- No services in "Exit" or "Restarting" state

### 4. Verify Evidence Artifacts
```bash
ls -la evidence/gates/g0_foundation.json
ls -la evidence/approvals/phase0_charter.json
ls -la evidence/validation/
```

**Expected:**
- All files exist
- g0_foundation.json has `"status": "PASS"`

### 5. Check for Forbidden Patterns
```bash
# Search all deliverables for forbidden patterns
grep -r "TODO\|TBD\|FIXME" docs/ scripts/ .github/ docker/ contracts/ 2>/dev/null
```

**Expected:**
- No matches (exit code 1 from grep = no matches found = GOOD)

### 6. Validate YAML/JSON Syntax
```bash
# YAML validation
yamllint docker-compose.yml .github/workflows/*.yml

# JSON validation
python3 -m json.tool evidence/gates/g0_foundation.json > /dev/null
python3 -m json.tool evidence/approvals/phase0_charter.json > /dev/null
```

**Expected:**
- No syntax errors

---

## 📊 DEFINITION OF DONE

All must be ✅ for acceptance:

| Criterion | Check Method | Status |
|-----------|-------------|--------|
| All 16 deliverables present | Contract validator | ⬜ |
| All quality gates passed | Contract validator | ⬜ |
| No forbidden patterns found | Contract validator | ⬜ |
| Cross-file validations passed | Contract validator | ⬜ |
| Repository structure validated | validate_structure.py exit 0 | ⬜ |
| Docker services healthy | docker compose ps | ⬜ |
| G0 gate status = PASS | g0_foundation.json | ⬜ |
| Charter approved by 4+ stakeholders | phase0_charter.json | ⬜ |
| Budget consistency (€250k) | Charter.md = charter.yaml | ⬜ |
| Contract validator exit code 0 | Final validation | ⬜ |

---

## 🚨 ITERATION LIMITS & ESCALATION

**From Agentic Prompt Guide: 2-Failure Rule**

If ANY deliverable fails validation 2 times:
1. **STOP WORK IMMEDIATELY**
2. **Document the issue:**
   - What deliverable failed
   - What quality gate failed
   - What you tried
   - Why it's not passing
3. **Escalate to human:**
   - "I've attempted [DELIVERABLE] twice and cannot pass [QUALITY GATE]. Validation error: [ERROR]. Request clarification or intervention."

**DO NOT attempt more than 2 iterations without human guidance.**

---

## 📤 RETURN PAYLOAD (When Complete)

When all validation passes, generate this structured report:

```json
{
  "contract_id": "PHASE_0_FOUNDATION_BUILD_2025",
  "execution_summary": {
    "start_time": "2025-01-15T08:00:00Z",
    "end_time": "2025-01-15T12:00:00Z",
    "elapsed_seconds": 14400,
    "deliverables_count": 16
  },
  "final_verdict": "ACCEPTED",
  "validation_report_path": "evidence/validation/phase0_contract_validation.json",
  "gate_status": {
    "gate_id": "G0",
    "status": "PASS",
    "evidence_path": "evidence/gates/g0_foundation.json"
  },
  "deliverable_summary": {
    "governance_files": 4,
    "repository_structure_files": 3,
    "environment_files": 5,
    "cicd_files": 3,
    "evidence_files": 1
  },
  "verification_steps_completed": [
    "Contract validator returned exit code 0",
    "Structure validator returned exit code 0",
    "Docker compose shows 4/4 services healthy",
    "G0 gate JSON status = PASS",
    "Charter approved by 4 stakeholders",
    "No forbidden patterns found in any deliverable",
    "All cross-file validations passed"
  ],
  "next_steps": [
    "User validates G0 gate with Zencoder AI",
    "Upon approval, Zencoder creates Phase 1 instructions",
    "Phase 1: Core Architecture build begins"
  ]
}
```

Save this to: `evidence/validation/phase0_completion_report.json`

---

## 🎓 BEST PRACTICES INTEGRATION

This contract integrates all 7 best practices from Gap Analysis:

1. **TDD Mandatory** ✅
   - Phase 0 is infrastructure (no code tests)
   - Test infrastructure BUILT for Phase 1+ (tests/ directories, CI test jobs)

2. **Evidence Requirements** ✅
   - Every deliverable produces evidence artifact
   - Gate validation requires evidence inventory

3. **Iteration Limits (2-failure rule)** ✅
   - Documented in escalation section
   - Enforced through execution_constraints

4. **Coverage Delta Reporting** ✅
   - CI workflow prepared for coverage reporting
   - Will be used in Phase 1+

5. **DoD Checklist Tables** ✅
   - Provided in this document (Definition of Done section)
   - Required in future phase deliverables

6. **Context Discipline** ✅
   - Required reading section limits context
   - No repo dumps, targeted document references

7. **Patch Regeneration Guidance** ✅
   - Contract validation provides specific line-level failures
   - Validator reports exact patterns that failed

---

## 🔗 WORKFLOW INTEGRATIONS

This Phase 0 build integrates patterns from all 5 workflows:

| Workflow | Integration | Evidence |
|----------|------------|----------|
| **N-Grade Contract** | Machine-enforceable quality gates, validation script | `contracts/phase_0_foundation.contract.json` |
| **Agentic Prompt Guide** | TDD, iteration limits, evidence requirements, DoD tables | See Best Practices section |
| **UMCA** | Governance layer, RACI matrix, approval flows | `docs/governance/raci_phase0.csv`, `evidence/approvals/` |
| **H3A Distribution** | State management directories, evidence paths | `state/`, `evidence/` |
| **EXE MVP** | Session protocol concepts (applied in Phase 1+) | Directory structure prepared |

---

## ❓ QUESTIONS BEFORE STARTING?

If ANY part of this contract is unclear:
1. **Ask now** before you begin work
2. Point to specific quality gates or deliverables
3. Request clarification on thresholds, patterns, or requirements

If everything is clear:
1. Confirm you understand the requirements
2. Provide estimated completion time (target: 3-4 hours)
3. Begin work

**DO NOT deliver until contract validator returns exit code 0.**

---

## 📝 SUMMARY

**What you're doing:** Building Phase 0 foundation (16 deliverables) to achieve G0 gate

**How you'll be judged:** Automated contract validator (zero tolerance)

**What happens if you fail:** Delivery rejected, fix issues, re-validate, re-submit

**What happens if you pass:** G0 gate PASS, user validates with Zencoder, Phase 1 instructions created

**Success looks like:**
```bash
$ python3 scripts/validate_contract.py contracts/phase_0_foundation.contract.json
✅ ACCEPTED
All 16 deliverables passed quality gates.
Exit code: 0

$ docker compose ps
NAME                STATUS
app                 healthy
postgres            healthy
redis               healthy
meilisearch         healthy

$ cat evidence/gates/g0_foundation.json
{
  "gate_id": "G0",
  "status": "PASS",
  ...
}
```

---

**BEGIN WORK. NO MORE HALF-ASSED DELIVERIES.**

---

*This instruction was generated by Zencoder AI Assistant using contract-based enforcement methodology.*  
*Contract ID: `PHASE_0_FOUNDATION_BUILD_2025`*  
*Validator: `scripts/validate_contract.py`*  
*Workflow Integrations: N-Grade Contract, Agentic Prompt Guide, UMCA, H3A Distribution, EXE MVP*  
*Date: October 1, 2025*