# Phase 0 Development Environment Setup Guide

## Prerequisites
- macOS, Linux, or WSL2 environment with administrative privileges.
- Internet connectivity to access package repositories, container registries, and GitHub.
- Access to the Phase 0 repository with branch protection policies enforced.
- Bootstrap time: under 2 hours for an engineer familiar with Docker and Git.

## Installation
1. Clone the repository.
   ```bash
   git clone git@github.com:example/autonomous-ai-phase0.git
   ```
2. Change into the project directory.
   ```bash
   cd autonomous-ai-phase0
   ```
3. Run the bootstrap script to create canonical directories.
   ```bash
   ./scripts/bootstrap_repo.sh
   ```
4. Execute the tooling installer for Python, Docker, and Node utilities.
   ```bash
   ./scripts/install_dev_tools.sh
   ```
5. Copy the environment template and adjust values.
   ```bash
   cp .env.example .env
   ```
6. Review `.env` and update secrets securely.
   ```bash
   sed -n '1,20p' .env
   ```
7. Install additional application dependencies if required.
   ```bash
   pip install -r requirements.txt
   ```
8. Pull optional development containers.
   ```bash
   docker pull postgres:15 redis:7 getmeili/meilisearch:v1.7
   ```

## Configuration
- Update `.env` with unique credentials distinct from production.
- Confirm that APP_PORT, POSTGRES_*, REDIS_*, and MEILISEARCH_* values match docker-compose.yml references.
- Enable telemetry as required by setting `COMPLIANCE_MODE=enabled` and `SECURITY_SCAN_LEVEL=high`.

## Running the Stack
1. Start the Docker services.
   ```bash
   docker compose up --build -d
   ```
2. Check container health statuses.
   ```bash
   docker compose ps
   ```
3. Tail logs for the application service.
   ```bash
   docker compose logs --tail=100 app
   ```
4. Run database migrations inside the app container.
   ```bash
   docker compose exec app python src/manage.py migrate
   ```
5. Seed reference data.
   ```bash
   docker compose exec app python src/manage.py loaddata seeds/phase0.json
   ```

## Verification
- Execute unit tests to confirm baseline functionality.
  ```bash
  docker compose exec app pytest tests/unit
  ```
- Execute integration tests to validate service interactions.
  ```bash
  docker compose exec app pytest tests/integration
  ```
- Run contract validation before submission.
  ```bash
  python3 scripts/validate_contract.py \
    contracts/phase_0_foundation.contract.json \
    --report-path evidence/validation/phase0_contract_validation.json
  ```
- Generate structure validation evidence.
  ```bash
  python scripts/validate_structure.py
  ```
- Capture SBOM and security reports from CI outputs.
  ```bash
  ls evidence/security
  ```

## Health Check Matrix
| Service      | Command                                                    | Expected Result |
|--------------|------------------------------------------------------------|-----------------|
| Application  | `curl http://localhost:${APP_PORT}/health`                 | HTTP 200        |
| Postgres     | `docker compose exec postgres pg_isready`                  | accepts connections |
| Redis        | `docker compose exec redis redis-cli ping`                 | PONG            |
| Meilisearch  | `curl http://localhost:${MEILISEARCH_PORT}/health`         | {"status":"available"} |

## Evidence Management
- Store approval documents under `evidence/approvals/` with sha256 digests.
- Maintain gate validation outputs under `evidence/gates/` for Phase 0 readiness.
- Archive CI, security, and contract validation logs under `evidence/validation/`.

## Branch Protection Expectations
- Pull requests require two approvals and successful CI workflows (`ci`, `security`, `gate_validation`).
- Ensure each PR references evidence updates and compliance confirmations for EU AI Act, ISO 42001, and GDPR obligations.

## Troubleshooting
- If Docker services fail healthchecks, inspect logs and confirm environment variables are defined.
  ```bash
  docker compose logs postgres
  ```
- For missing dependencies, rerun the install script to reinstall packages.
  ```bash
  ./scripts/install_dev_tools.sh
  ```
- When tests fail, execute targeted suites locally to replicate CI conditions.
  ```bash
  docker compose exec app pytest tests/system
  ```
- Document incidents in `evidence/state/audit_logs/` and notify stakeholders per branch protection policy.
  ```bash
  echo "2025-10-01T10:15Z incident resolved" >> evidence/state/audit_logs/phase0.log
  ```

## Onboarding Checklist
- [ ] Repository cloned and synchronized with `main`.
- [ ] Bootstrap and install scripts executed without error.
- [ ] `.env` configured with secure credentials distinct from production secrets.
- [ ] Docker services running with healthy status.
- [ ] Tests and linters executed successfully.
- [ ] Contract validation report generated and stored under evidence/validation/.

## Security Considerations
- Never commit actual production secrets; use placeholders in `.env.example` and store secrets securely elsewhere.
- Rotate credentials regularly and update `.env` with new values.
- Review security.yml output after each CI run to confirm zero high-severity findings.

## Compliance Alignment
- Maintain documentation that references EU AI Act risk management, ISO 42001 controls, and GDPR privacy safeguards.
- Update evidence/compliance artifacts whenever controls change.
- Prepare for Phase 5 security audits by keeping vulnerability reports current.

## Support Channels
- Engineering assistance: `#phase0-engineering` Slack channel.
- Compliance queries: `#phase0-compliance` channel with weekly office hours.
- Infrastructure support: ticket via ServiceDesk referencing Phase 0 environment setup.

## Next Steps
- Once Phase 0 environment is validated, coordinate with Phase 1 teams to hand off assets.
- Continue maintaining evidence directories and updating documentation as processes evolve.
