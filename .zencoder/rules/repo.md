# Repository Overview: N_grade

## Purpose
This repository delivers the N-Grade Phase 0/1 system with state management, orchestration, LLM routing, FinOps guardrails, evidence generation, and CI-friendly validation artifacts.

## Structure
- **src/**: Application code
  - **state/**: Repository and ledger replay
  - **orchestration/**: LangGraph workflow and helpers
  - **models/**: LLM router and provider logic
  - **finops/**: Budget guardrails
  - **notifications/**: Async publisher with correlation IDs
- **tests/**: Pytest suites
  - **integration/**: Integration-style tests for core modules
  - **e2e/**: End-to-end scenarios for budget, failover, ledger replay and workflow
  - `conftest.py`: Ensures `src` is importable
- **scripts/**: Utilities including the E2E runner that outputs metrics/evidence
- **configs/**, **policies/**, **contracts/**: Configuration, gates, and contracts
- **metrics/**, **evidence/**: Machine-readable outputs used for verification

## Environment
- Python 3.13+ recommended
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Running Tests
- From repository root:
  ```bash
  pytest
  ```
- Run only E2E and generate evidence/metrics:
  ```bash
  python scripts/run_e2e.py
  ```

## Evidence & Metrics
- JSON evidence: `evidence/validation/e2e_results.json`
- E2E metrics: `metrics/quality/e2e_results.csv`
- Additional contract artifacts:
  - Router perf: `metrics/performance/router_latency_p95.csv`
  - Failover reliability: `metrics/reliability/failover_success_rate.csv`
  - Remediation validation: `evidence/validation/phase1_remediation_validation.json`

## Notes
- UTC timestamps are enforced using timezone-aware `datetime` APIs
- Backward compatibility maintained for router/provider method names and state repository alias
- Orchestration uses conditional edges for refinement and approval flow