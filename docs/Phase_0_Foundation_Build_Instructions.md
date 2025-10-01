# Phase 0: Foundation Setup Build Instructions
**Autonomous AI Coding System — Incremental Build Strategy**

---

## 📋 Document Information

**Owner:** Yousef Baragji  
**Version:** 1.0  
**Date:** 2025-01-XX  
**Target Audience:** AI Assistant executing build tasks  
**Estimated Duration:** 1-2 weeks  
**Gate Target:** G0 Foundation Ready

---

## 🎯 Mission

Bootstrap the autonomous AI coding system repository from current state to **G0 Foundation Ready** gate compliance. This phase establishes the infrastructure scaffolding, development environment, CI/CD foundation, and governance baseline that all subsequent phases will build upon.

**G0 Definition:** Repository bootstrapped, CI online, Docker services healthy, branch protection enforced, strategic charter approved.

---

## 📚 Context & Prerequisites

### Required Reading
You must review these documents before beginning work:

1. **`/docs/00_Plans_&_Data/autonomous_ai_roadmap_v2.md`**  
   - Read Phase 0 section (lines 71-249)
   - Understand G0 gate criteria
   - Review canonical evidence paths

2. **`/docs/00_Plans_&_Data/autonomous_ai_coding_system_taxonomy_ssot_v1.2.md`**  
   - Focus on Priority=Required functions
   - Note evidence artifact paths for G0/G1 gates

3. **`/docs/Workflows/WORKFLOW_ANALYSIS_REPORT.md`**  
   - Review Merge Strategy (lines 379-403)
   - Understand adoption roadmap Phase 0

4. **`/docs/Workflows/01_project-Agentic_prompt_guide/Gap_Analysis_Missing_Best_Practices.md`**  
   - Understand TDD requirements (CRITICAL)
   - Note iteration limits (2-failure rule)
   - Review evidence requirements

### Current Repository State
- Root: `/Users/Yousef_1/Coding/N_grade/`
- Existing structure: `executor-mvp/`, `docs/`, `scripts/`, partial planning documentation
- **No formal repository structure yet** — you will create it
- Git repository initialized but no branch protection

---

## 🏆 Best Practices to Incorporate

### From Gap Analysis (ALL MANDATORY)
1. **✅ TDD Mandatory:** All code must follow RED→GREEN→REFACTOR cycle
2. **✅ Evidence Required:** Every task must produce verifiable artifacts
3. **✅ Iteration Limits:** Max 2 attempts before human escalation
4. **✅ Coverage Delta:** Report if ±5% change detected
5. **✅ DoD Checklist Tables:** Use ✅/❌ format in all reports
6. **✅ Context Discipline:** Target specific files, avoid repo dumps
7. **✅ Patch Regeneration:** Use ±3 context lines on apply failures

### From Roadmap v2
- **Canonical Evidence Paths:** All artifacts must use standard paths
- **Gate Framework:** G0 must be passed before G1 work begins
- **Validation Process:** Every subsection has explicit validation steps
- **Reproducible Scripts:** Manual steps must be scripted

### From Merge Strategy
- **Layer UMCA governance** (charter, RACI, compliance)
- **Prepare for H3A state suite** (directory structure)
- **Enable N-Grade contracts** (validation scripts)
- **Support EXE MVP ergonomics** (session rituals)

---

## 📝 Detailed Task Breakdown

## Task 0.0: Strategic Kick-off and Charter Approval

### Objective
Create strategic charter documenting problem statement, success criteria, budget limits (€250k/6mo), compliance obligations (EU AI Act GPAI), and stakeholder RACI.

### Inputs
- Review existing: `/docs/00_Plans_&_Data/spec.md`
- Review existing: `/docs/00_Plans_&_Data/autonomous_ai_roadmap_v2.md`
- Review existing: `/docs/governing/*.md`

### Outputs Required

1. **`docs/strategy/charter.md`** (Markdown format)
   - Problem statement (≤200 words)
   - Success criteria (5-8 measurable outcomes)
   - Budget ceiling (€250,000)
   - Regulatory obligations (EU AI Act GPAI compliance, ISO 42001)
   - Primary risks (3-5 with mitigations)
   - Timeline (26 weeks, phases 0-8)

2. **`docs/strategy/charter.yaml`** (Machine-readable format)
   ```yaml
   initiative: autonomous_ai_coding_system
   mission: >-
     Deliver a production-grade autonomous coding platform with verifiable safety,
     security, and compliance controls within 26 weeks.
   budget_eur: 250000
   stakeholders:
     - role: Architecture Lead
       contact: [TBD]
     - role: Security Officer
       contact: [TBD]
     - role: Compliance Lead
       contact: [TBD]
     - role: Finance Controller
       contact: [TBD]
   steering_cadence_days: 7
   success_metrics:
     - name: charter_signoff
       target: true
       evidence: evidence/approvals/phase0_charter.json
     - name: g0_gate_passed
       target: true
       evidence: evidence/gates/g0_foundation.json
   ```

3. **`docs/strategy/raci_phase0.csv`** (Stakeholder accountability)
   - Minimum 10 roles with unique owners
   - Columns: Role, Responsible, Accountable, Consulted, Informed
   - Cover: Architecture, DevOps, Security, Compliance, Finance, Product, QA, Legal, Data Privacy, Executive Sponsor

4. **`evidence/approvals/phase0_charter.json`** (Approval record)
   ```json
   {
     "charter_version": "1.0",
     "approval_date": "2025-01-XX",
     "approvers": [
       {"role": "Architecture Lead", "approved": true, "timestamp": "2025-01-XX"},
       {"role": "Compliance Lead", "approved": true, "timestamp": "2025-01-XX"},
       {"role": "Finance Controller", "approved": true, "timestamp": "2025-01-XX"},
       {"role": "Executive Sponsor", "approved": true, "timestamp": "2025-01-XX"}
     ],
     "signed_artifact": "docs/strategy/charter.md",
     "verification_hash": "sha256:..."
   }
   ```

### Success Criteria (DoD)
| Criterion | Target |
|-----------|--------|
| Charter signed by 4+ stakeholders | ✅ Required |
| RACI lists ≥10 unique roles | ✅ Required |
| Budget documented (€250k) | ✅ Required |
| Compliance obligations specified | ✅ Required |
| Evidence file created | ✅ Required |

### Validation Steps
1. ✅ Review charter.md for completeness (all sections present)
2. ✅ Verify charter.yaml parses correctly and matches .md content
3. ✅ Confirm RACI has no duplicate owners
4. ✅ Check approval JSON has 4+ approvers with timestamps
5. ✅ Calculate SHA-256 hash of charter.md and record in approval JSON

### Notes
- **Iteration Limit:** Max 2 attempts; if charter not approved, escalate
- **Evidence Trail:** Store draft versions as `charter_draft_v1.md`, etc.
- **TBD Placeholders:** Acceptable for Phase 0; will be filled in Phase 1

---

## Task 0.1: Repository and Branch Protection Baseline

### Objective
Create deterministic repository structure with canonical directories and enforce branch protection on `main` branch.

### Inputs
- Roadmap v2 canonical evidence paths (lines 20-29)
- Taxonomy v1.2 evidence artifact locations
- Current repo structure audit

### Outputs Required

1. **`scripts/bootstrap_repo.sh`** (Bash script)
   ```bash
   #!/usr/bin/env bash
   # Bootstrap repository structure for autonomous AI coding system
   set -euo pipefail
   
   echo "🚀 Bootstrapping repository structure..."
   
   # Create canonical directories
   mkdir -p src/{agents,orchestration,models,tools,api}
   mkdir -p tests/{unit,integration,e2e}
   mkdir -p docs/{architecture,api,guides,ops,compliance,strategy}
   mkdir -p evidence/{gates,static_checks,secrets_scan,release,approvals,quality,security,env}
   mkdir -p metrics/{kpi,cost,quality,errors,usage,performance,compliance}
   mkdir -p sbom
   mkdir -p recovery
   mkdir -p logs/ai_actions
   mkdir -p siem/parsers
   mkdir -p governance/{technical_file,dpia,control_mappings}
   mkdir -p policies/runtime
   mkdir -p benchmarks/{harness,results}
   mkdir -p golden_tasks
   mkdir -p state/{context,mdc,tkg,run}
   mkdir -p orchestration
   mkdir -p sessions
   mkdir -p prompts
   mkdir -p handoffs/{RA,AA,IA,SA,QA,DA,DBA,DOCS}
   mkdir -p research
   mkdir -p go_nogo
   mkdir -p notifications
   mkdir -p provenance
   mkdir -p coverage
   mkdir -p mutation
   mkdir -p .github/{workflows,actions}
   mkdir -p .devcontainer
   mkdir -p deploy
   mkdir -p env
   
   # Create .keep files for empty directories
   find src tests docs evidence metrics sbom recovery logs siem governance policies benchmarks golden_tasks state orchestration sessions prompts handoffs research go_nogo notifications provenance coverage mutation -type d -empty -exec touch {}/.keep \;
   
   echo "✅ Repository structure created"
   echo "📊 Directory count: $(find . -type d | wc -l)"
   ```

2. **`scripts/validate_structure.py`** (Python validation script)
   ```python
   #!/usr/bin/env python3
   """Validate repository structure against canonical requirements."""
   import json
   import sys
   from pathlib import Path
   
   REQUIRED_DIRS = [
       "src/agents", "src/orchestration", "src/models", "src/tools", "src/api",
       "tests/unit", "tests/integration", "tests/e2e",
       "docs/architecture", "docs/api", "docs/guides", "docs/ops", "docs/compliance", "docs/strategy",
       "evidence/gates", "evidence/static_checks", "evidence/secrets_scan", "evidence/release", "evidence/approvals",
       "metrics/kpi", "metrics/cost", "metrics/quality", "metrics/performance",
       "sbom", "recovery", "logs/ai_actions", "siem/parsers",
       "governance/technical_file", "policies/runtime", "benchmarks/harness",
       "state/context", "state/mdc", "orchestration", "sessions", "prompts"
   ]
   
   def main():
       root = Path.cwd()
       missing = []
       
       for dir_path in REQUIRED_DIRS:
           full_path = root / dir_path
           if not full_path.exists():
               missing.append(dir_path)
       
       result = {
           "validation_date": "2025-01-XX",
           "root_directory": str(root),
           "required_directories": len(REQUIRED_DIRS),
           "found_directories": len(REQUIRED_DIRS) - len(missing),
           "missing_directories": missing,
           "status": "PASS" if not missing else "FAIL"
       }
       
       output_path = root / "evidence/gates/g0_foundation.json"
       output_path.parent.mkdir(parents=True, exist_ok=True)
       
       with open(output_path, 'w') as f:
           json.dump(result, f, indent=2)
       
       print(f"✅ Validation complete: {result['status']}")
       print(f"📄 Report: {output_path}")
       
       sys.exit(0 if result['status'] == 'PASS' else 1)
   
   if __name__ == "__main__":
       main()
   ```

3. **`evidence/release/branch_protection.md`** (Branch policy documentation)
   ```markdown
   # Branch Protection Configuration
   
   ## Main Branch Protection Rules
   - **Branch:** `main`
   - **Status Checks Required:** `ci`, `security`, `sbom`, `lint`
   - **Require Signed Commits:** ✅ Yes
   - **Require Linear History:** ✅ Yes
   - **Minimum Reviews:** 2
   - **Dismiss Stale Reviews:** ✅ Yes
   - **Require Code Owner Review:** ✅ Yes
   - **Restrict Push Access:** Admins only
   - **Allow Force Pushes:** ❌ No
   - **Allow Deletions:** ❌ No
   
   ## Verification
   - Policy configured via GitHub API on: 2025-01-XX
   - Policy snapshot captured in: evidence/release/branch_protection_snapshot.json
   - Verified by: [Your Name]
   
   ## Testing
   - Attempted unsigned commit: ❌ Blocked (expected)
   - Attempted direct push: ❌ Blocked (expected)
   - Pull request without CI: ❌ Blocked (expected)
   ```

4. **Git Tag:** `v0.0-foundation`
   - Tag initial bootstrap commit
   - Record commit hash in `evidence/gates/g0_foundation.json`

### Success Criteria (DoD)
| Criterion | Status |
|-----------|--------|
| All canonical directories created | ✅ Required |
| Validation script passes | ✅ Required |
| Branch protection configured | ✅ Required |
| Git tag created | ✅ Required |
| Evidence file generated | ✅ Required |

### Validation Steps
1. ✅ Run `./scripts/bootstrap_repo.sh` and verify exit code 0
2. ✅ Run `python3 scripts/validate_structure.py --strict` → expect PASS
3. ✅ Check `evidence/gates/g0_foundation.json` exists with status=PASS
4. ✅ Verify git tag exists: `git tag -l v0.0-foundation`
5. ✅ Confirm branch protection via GitHub API (manual verification acceptable for Phase 0)

### Notes
- **TDD N/A:** No application code in this task (infrastructure only)
- **Idempotency:** Scripts must be safe to re-run
- **Windows Compatibility:** Not required (macOS/Linux only per spec)

---

## Task 0.2: Development Environment Provisioning

### Objective
Create reproducible development environment with Docker Compose services, developer tooling scripts, and environment variable management.

### Inputs
- Roadmap v2 section 0.2 (lines 157-212)
- Current `executor-mvp/.env.example` file
- Technology stack: Python (uv), Node.js (pnpm), Docker, PostgreSQL, Redis

### Outputs Required

1. **`docker-compose.yml`** (Root directory)
   ```yaml
   version: "3.9"
   services:
     app:
       build:
         context: .
         dockerfile: docker/Dockerfile
       command: uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
       environment:
         ENVIRONMENT: development
         DATABASE_URL: postgresql+psycopg2://app_user:dev_password_change_in_prod@postgres:5432/autonomous_ai
         REDIS_URL: redis://redis:6379/0
         PYTHONPATH: /app
       ports:
         - "8000:8000"
       volumes:
         - ./src:/app/src
         - ./tests:/app/tests
       depends_on:
         postgres:
           condition: service_healthy
         redis:
           condition: service_healthy
     
     postgres:
       image: postgres:17-alpine
       environment:
         POSTGRES_DB: autonomous_ai
         POSTGRES_USER: app_user
         POSTGRES_PASSWORD: dev_password_change_in_prod
       ports:
         - "5432:5432"
       volumes:
         - .infra_data/postgres:/var/lib/postgresql/data
       healthcheck:
         test: ["CMD-SHELL", "pg_isready -U app_user -d autonomous_ai"]
         interval: 5s
         timeout: 3s
         retries: 10
     
     redis:
       image: redis:7-alpine
       ports:
         - "6379:6379"
       volumes:
         - .infra_data/redis:/data
       healthcheck:
         test: ["CMD", "redis-cli", "ping"]
         interval: 5s
         timeout: 3s
         retries: 10
     
     meilisearch:
       image: getmeili/meilisearch:v1.5
       environment:
         MEILI_ENV: development
         MEILI_MASTER_KEY: dev_master_key_change_in_prod
       ports:
         - "7700:7700"
       volumes:
         - .infra_data/meilisearch:/meili_data
   ```

2. **`docker/Dockerfile`** (Application container)
   ```dockerfile
   FROM python:3.12-slim
   
   WORKDIR /app
   
   # Install system dependencies
   RUN apt-get update && apt-get install -y \
       git \
       curl \
       && rm -rf /var/lib/apt/lists/*
   
   # Install uv
   RUN curl -LsSf https://astral.sh/uv/install.sh | sh
   ENV PATH="/root/.cargo/bin:$PATH"
   
   # Copy dependency files
   COPY pyproject.toml uv.lock* ./
   
   # Install dependencies
   RUN uv pip install --system -r pyproject.toml
   
   # Copy application code
   COPY . .
   
   EXPOSE 8000
   
   CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

3. **`scripts/install_dev_tools.sh`** (Developer tooling)
   ```bash
   #!/usr/bin/env bash
   # Install development tools for autonomous AI system
   set -euo pipefail
   
   echo "🔧 Installing development tools..."
   
   # Detect OS
   OS="$(uname -s)"
   
   # Install uv (Python package manager)
   if ! command -v uv &> /dev/null; then
       echo "📦 Installing uv..."
       curl -LsSf https://astral.sh/uv/install.sh | sh
   fi
   
   # Install pre-commit
   if ! command -v pre-commit &> /dev/null; then
       echo "🎣 Installing pre-commit..."
       pip install pre-commit
   fi
   
   # Install Node.js tools (if Node installed)
   if command -v npm &> /dev/null; then
       echo "📦 Installing pnpm..."
       npm install -g pnpm
   fi
   
   # Install Git hooks
   if [ -f ".git/config" ]; then
       echo "🎣 Installing Git hooks..."
       pre-commit install
   fi
   
   # Verify installations
   echo ""
   echo "✅ Verification:"
   uv --version && echo "  ✅ uv installed"
   pre-commit --version && echo "  ✅ pre-commit installed"
   docker --version && echo "  ✅ Docker installed" || echo "  ⚠️  Docker not found"
   
   echo ""
   echo "🎉 Development tools installation complete!"
   ```

4. **`docs/ops/environment_reference.md`** (Environment documentation)
   ```markdown
   # Environment Reference
   
   ## Environment Variables
   
   ### Application
   - `ENVIRONMENT`: `development` | `staging` | `production`
   - `DATABASE_URL`: PostgreSQL connection string
   - `REDIS_URL`: Redis connection string
   - `PYTHONPATH`: Python module path (set to `/app` in container)
   
   ### API Keys (Secrets)
   - `OPENAI_API_KEY`: OpenAI API key for GPT-5
   - `ANTHROPIC_API_KEY`: Anthropic API key for Claude
   - `GITHUB_TOKEN`: GitHub PAT for API access
   
   ### Service Endpoints
   - `MEILISEARCH_URL`: http://meilisearch:7700
   - `MEILISEARCH_KEY`: Master key for Meilisearch
   
   ## Local Development Setup
   
   1. Copy `.env.example` to `.env`:
      ```bash
      cp .env.example .env
      ```
   
   2. Fill in required secrets:
      ```bash
      # .env
      OPENAI_API_KEY=sk-...
      ANTHROPIC_API_KEY=sk-ant-...
      GITHUB_TOKEN=ghp_...
      ```
   
   3. Generate hash for audit trail:
      ```bash
      shasum -a 256 .env | awk '{print $1}' > evidence/security/env_hashes.json
      ```
   
   ## Security Notes
   - **Never commit `.env` files** (already in `.gitignore`)
   - Rotate secrets quarterly (see `docs/ops/secret_rotation.md`)
   - Use OIDC for cloud providers (avoid long-lived credentials)
   ```

5. **`.env.example`** (Template for secrets)
   ```bash
   # Environment
   ENVIRONMENT=development
   
   # Database
   DATABASE_URL=postgresql+psycopg2://app_user:dev_password@localhost:5432/autonomous_ai
   REDIS_URL=redis://localhost:6379/0
   
   # API Keys (REPLACE WITH YOUR KEYS)
   OPENAI_API_KEY=sk-your-key-here
   ANTHROPIC_API_KEY=sk-ant-your-key-here
   GITHUB_TOKEN=ghp_your-token-here
   
   # Meilisearch
   MEILISEARCH_URL=http://localhost:7700
   MEILISEARCH_KEY=dev_master_key
   ```

6. **`evidence/security/env_hashes.json`** (Audit trail)
   ```json
   {
     "env_file_hash": "sha256:...",
     "hashed_at": "2025-01-XX",
     "verification_note": "Hash computed without exposing secret values"
   }
   ```

### Success Criteria (DoD)
| Criterion | Status |
|-----------|--------|
| `docker compose up` completes <60s | ✅ Required |
| All services report `healthy` | ✅ Required |
| Dev tools script exits 0 | ✅ Required |
| Environment docs complete | ✅ Required |
| `.env` hash recorded | ✅ Required |

### Validation Steps
1. ✅ Run `docker compose up -d` and time completion
2. ✅ Run `docker compose ps` → verify all services `healthy`
3. ✅ Run `./scripts/install_dev_tools.sh --verify`
4. ✅ Verify `.env.example` exists and is documented
5. ✅ Check `evidence/security/env_hashes.json` exists

### Notes
- **Secrets Management:** Use placeholders in `.env.example`, actual keys in ignored `.env`
- **Performance:** If services take >60s, document in issues
- **TDD N/A:** Infrastructure task (no application logic)

---

## Task 0.3: CI/CD Pipeline Foundation

### Objective
Create GitHub Actions CI/CD pipeline with lint, test, security scan, and SBOM generation jobs.

### Inputs
- Roadmap v2 section 0.3 (lines 213-249)
- Gap Analysis TDD requirements
- Current `executor-mvp/.github/workflows/*` (if exists)

### Outputs Required

1. **`.github/workflows/ci.yml`** (Main CI pipeline)
   ```yaml
   name: Autonomous AI CI
   
   on:
     push:
       branches: [main, develop, release/*]
     pull_request:
       paths-ignore:
         - 'docs/**'
         - '*.md'
   
   env:
     PYTHON_VERSION: "3.12"
     NODE_VERSION: "20"
   
   jobs:
     lint:
       name: Lint & Format
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         
         - name: Set up Python
           uses: actions/setup-python@v5
           with:
             python-version: ${{ env.PYTHON_VERSION }}
         
         - name: Install uv
           run: curl -LsSf https://astral.sh/uv/install.sh | sh
         
         - name: Install dependencies
           run: |
             uv pip install --system ruff mypy bandit
         
         - name: Run ruff
           run: |
             ruff check . --output-format=text > evidence/static_checks/ruff.txt || true
             ruff check .
         
         - name: Run mypy
           run: |
             mypy src --strict > evidence/static_checks/mypy.txt || true
             mypy src --strict
         
         - name: Upload lint results
           uses: actions/upload-artifact@v4
           if: always()
           with:
             name: lint-results
             path: evidence/static_checks/
     
     security:
       name: Security Scans
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
           with:
             fetch-depth: 0  # Full history for gitleaks
         
         - name: Run Gitleaks
           uses: gitleaks/gitleaks-action@v2
           env:
             GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
         
         - name: Run Bandit
           run: |
             pip install bandit
             bandit -r src -f txt -o evidence/secrets_scan/bandit.txt || true
         
         - name: Upload security results
           uses: actions/upload-artifact@v4
           if: always()
           with:
             name: security-results
             path: evidence/secrets_scan/
     
     test:
       name: Test & Coverage
       runs-on: ubuntu-latest
       services:
         postgres:
           image: postgres:17-alpine
           env:
             POSTGRES_DB: test_db
             POSTGRES_USER: test_user
             POSTGRES_PASSWORD: test_pass
           options: >-
             --health-cmd pg_isready
             --health-interval 5s
             --health-timeout 3s
             --health-retries 10
           ports:
             - 5432:5432
         
         redis:
           image: redis:7-alpine
           options: >-
             --health-cmd "redis-cli ping"
             --health-interval 5s
             --health-timeout 3s
             --health-retries 10
           ports:
             - 6379:6379
       
       steps:
         - uses: actions/checkout@v4
         
         - name: Set up Python
           uses: actions/setup-python@v5
           with:
             python-version: ${{ env.PYTHON_VERSION }}
         
         - name: Install dependencies
           run: |
             curl -LsSf https://astral.sh/uv/install.sh | sh
             uv pip install --system -r pyproject.toml
             uv pip install --system pytest pytest-cov pytest-xdist
         
         - name: Run unit tests
           run: |
             pytest tests/unit \
               --maxfail=1 \
               --disable-warnings \
               --cov=src \
               --cov-report=xml:coverage/coverage.xml \
               --cov-report=term \
               -v
         
         - name: Run integration tests
           env:
             DATABASE_URL: postgresql://test_user:test_pass@localhost:5432/test_db
             REDIS_URL: redis://localhost:6379/0
           run: |
             pytest tests/integration \
               --maxfail=1 \
               --disable-warnings \
               -v
         
         - name: Upload coverage
           uses: actions/upload-artifact@v4
           with:
             name: coverage-report
             path: coverage/
         
         - name: Coverage comment
           uses: py-cov-action/python-coverage-comment-action@v3
           with:
             GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
             MINIMUM_GREEN: 85
             MINIMUM_ORANGE: 70
     
     sbom:
       name: Generate SBOM
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         
         - name: Install CycloneDX
           run: pip install cyclonedx-bom
         
         - name: Generate SBOM
           run: |
             cyclonedx-py -o sbom/SBOM.json --format json
         
         - name: Upload SBOM
           uses: actions/upload-artifact@v4
           with:
             name: sbom
             path: sbom/SBOM.json
   ```

2. **`.github/actions/setup-python-and-node/action.yml`** (Shared setup action)
   ```yaml
   name: 'Setup Python and Node'
   description: 'Composite action to set up Python, Node, and dependencies'
   
   runs:
     using: "composite"
     steps:
       - name: Set up Python
         uses: actions/setup-python@v5
         with:
           python-version: "3.12"
           cache: 'pip'
       
       - name: Set up Node
         uses: actions/setup-node@v4
         with:
           node-version: "20"
           cache: 'pnpm'
       
       - name: Install uv
         shell: bash
         run: curl -LsSf https://astral.sh/uv/install.sh | sh
       
       - name: Cache uv packages
         uses: actions/cache@v4
         with:
           path: ~/.cache/uv
           key: ${{ runner.os }}-uv-${{ hashFiles('pyproject.toml') }}
   ```

3. **`.github/workflows/gate-validation.yml`** (Gate enforcement)
   ```yaml
   name: Gate Validation
   
   on:
     pull_request:
       types: [opened, synchronize, reopened]
   
   jobs:
     validate-gates:
       name: Validate G0-G8 Gates
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         
         - name: Check G0 Foundation
           run: |
             if [ -f "evidence/gates/g0_foundation.json" ]; then
               echo "✅ G0 evidence found"
               cat evidence/gates/g0_foundation.json
             else
               echo "❌ G0 evidence missing"
               exit 1
             fi
         
         - name: Validate evidence structure
           run: |
             python3 scripts/validate_structure.py
   ```

### Success Criteria (DoD)
| Criterion | Status |
|-----------|--------|
| CI pipeline completes <12min | ✅ Required |
| All jobs pass (lint, test, security, sbom) | ✅ Required |
| Coverage report generated | ✅ Required |
| SBOM artifact uploaded | ✅ Required |
| Gate validation workflow created | ✅ Required |

### Validation Steps
1. ✅ Create test PR to trigger pipeline
2. ✅ Verify all jobs complete successfully
3. ✅ Check artifacts uploaded (coverage, sbom, lint results)
4. ✅ Confirm pipeline runtime <12 minutes
5. ✅ Verify branch protection enforces CI checks

### Notes
- **TDD:** This task creates infrastructure for TDD validation
- **Iteration Limit:** If CI configuration fails 2x, escalate with logs
- **Cache Optimization:** Use actions/cache for dependencies

---

## 📊 Evidence Checklist

After completing all tasks, verify these artifacts exist:

### Strategic Documents
- [ ] `docs/strategy/charter.md`
- [ ] `docs/strategy/charter.yaml`
- [ ] `docs/strategy/raci_phase0.csv`
- [ ] `evidence/approvals/phase0_charter.json`

### Repository Structure
- [ ] `scripts/bootstrap_repo.sh`
- [ ] `scripts/validate_structure.py`
- [ ] `evidence/gates/g0_foundation.json`
- [ ] `evidence/release/branch_protection.md`
- [ ] Git tag: `v0.0-foundation`

### Development Environment
- [ ] `docker-compose.yml`
- [ ] `docker/Dockerfile`
- [ ] `scripts/install_dev_tools.sh`
- [ ] `docs/ops/environment_reference.md`
- [ ] `.env.example`
- [ ] `evidence/security/env_hashes.json`

### CI/CD Pipeline
- [ ] `.github/workflows/ci.yml`
- [ ] `.github/workflows/gate-validation.yml`
- [ ] `.github/actions/setup-python-and-node/action.yml`
- [ ] CI pipeline passing (verified via PR)

---

## ✅ G0 Gate Validation

### G0 Success Criteria (All Required)
1. ✅ Repository contains all canonical directories (validated by `validate_structure.py`)
2. ✅ Branch protection configured with 4+ status checks
3. ✅ Docker services start <60s and report healthy
4. ✅ CI pipeline completes <12min with all jobs passing
5. ✅ Strategic charter approved by 4+ stakeholders
6. ✅ RACI matrix has ≥10 unique roles
7. ✅ Initial commit tagged `v0.0-foundation`
8. ✅ Evidence file `evidence/gates/g0_foundation.json` validates PASS

### Gate Validation Command
```bash
# Run this command to validate G0 completion
python3 scripts/validate_structure.py && \
docker compose up -d && \
docker compose ps | grep healthy && \
test -f evidence/approvals/phase0_charter.json && \
test -f evidence/gates/g0_foundation.json && \
git tag -l v0.0-foundation && \
echo "✅ G0 GATE PASSED"
```

---

## 📤 Deliverable Report Format

When you complete Phase 0, return this report to the user:

```markdown
# Phase 0 Completion Report

## Executive Summary
- **Status:** ✅ COMPLETE / ⚠️ PARTIAL / ❌ FAILED
- **G0 Gate:** ✅ PASSED / ❌ FAILED
- **Duration:** X days
- **Iterations:** X (max 2 per task)
- **Blockers:** None / [List blockers]

## Task Completion Status

### Task 0.0: Strategic Charter
| Criterion | Status | Evidence |
|-----------|--------|----------|
| Charter signed | ✅/❌ | `evidence/approvals/phase0_charter.json` |
| RACI matrix | ✅/❌ | `docs/strategy/raci_phase0.csv` |
| Budget documented | ✅/❌ | `docs/strategy/charter.yaml` |

### Task 0.1: Repository Structure
| Criterion | Status | Evidence |
|-----------|--------|----------|
| Directories created | ✅/❌ | `scripts/bootstrap_repo.sh` executed |
| Validation passed | ✅/❌ | `evidence/gates/g0_foundation.json` |
| Branch protection | ✅/❌ | `evidence/release/branch_protection.md` |

### Task 0.2: Development Environment
| Criterion | Status | Evidence |
|-----------|--------|----------|
| Docker services healthy | ✅/❌ | `docker compose ps` output |
| Dev tools installed | ✅/❌ | `scripts/install_dev_tools.sh` exit code |
| Environment docs | ✅/❌ | `docs/ops/environment_reference.md` |

### Task 0.3: CI/CD Pipeline
| Criterion | Status | Evidence |
|-----------|--------|----------|
| CI pipeline passing | ✅/❌ | GitHub Actions run #XXXX |
| Runtime <12min | ✅/❌ | XX:XX actual |
| All jobs pass | ✅/❌ | lint, test, security, sbom |

## Evidence Artifacts (All Generated)
- [x] `evidence/gates/g0_foundation.json`
- [x] `evidence/approvals/phase0_charter.json`
- [x] `evidence/release/branch_protection.md`
- [x] `evidence/security/env_hashes.json`
- [x] CI artifacts (coverage, sbom, lint results)

## G0 Gate Validation Result
✅ **PASSED** - All criteria met, system ready for Phase 1

## Issues Encountered
1. **Issue:** [Description]
   - **Resolution:** [How it was fixed]
   - **Iteration:** 1/2

## Next Steps
- User should review evidence artifacts in `evidence/` directory
- User should verify Docker services: `docker compose ps`
- User should verify CI pipeline: Check GitHub Actions tab
- **Ready for Phase 1 instructions** (Core Architecture)

## Artifacts Location
- Repository: `/Users/Yousef_1/Coding/N_grade/`
- Evidence: `/Users/Yousef_1/Coding/N_grade/evidence/`
- Git tag: `v0.0-foundation` (commit: XXXXXXX)

---

**Completed by:** [AI Assistant Name]  
**Date:** 2025-01-XX  
**Verification:** User should review and approve before Phase 1
```

---

## 🚨 Escalation Protocol

### When to Escalate to Human
1. ✅ **After 2 failed iterations** on any task
2. ✅ Dependency not available (e.g., GitHub API access)
3. ✅ Ambiguous requirement interpretation
4. ✅ CI pipeline fails >2x despite fixes
5. ✅ Stakeholder approvals blocked (charter sign-off)

### Escalation Format
```markdown
## ESCALATION REQUIRED

**Task:** [Task number and name]  
**Iteration:** 2/2 (limit reached)  
**Issue:** [Brief description]

**Attempted Solutions:**
1. [First attempt] → [Result]
2. [Second attempt] → [Result]

**Recommendation:**
[What human should do to unblock]

**Evidence:**
- Logs: [path to logs]
- Error output: [paste or link]
```

---

## 📚 Additional Notes

### TDD Reminder
- Phase 0 is primarily infrastructure (bash scripts, YAML, documentation)
- TDD becomes critical in Phase 1 (Python application code)
- Test infrastructure is being **built** in Phase 0 (CI pipeline, test directories)

### Context Discipline
- Focus on Phase 0 tasks only
- Do not implement Phase 1 features
- Keep scripts simple and focused

### Iteration Tracking
- Track attempts per task (max 2)
- Document issues in report
- Escalate if blocked

### Quality Bar
- All scripts must be idempotent (safe to re-run)
- All evidence must be machine-verifiable
- All documentation must be complete (no TBD in critical sections)

---

**END OF PHASE 0 INSTRUCTIONS**

**Questions?** Escalate to user with specific question and context.

**Ready to Begin?** Start with Task 0.0 (Strategic Charter).

**Remember:** "Start with the simplest thing that proves the system works." — Build G0 perfectly, then move to G1.