# Quality Assurance Process

## Peer Code Review
- Two reviewers for critical changes; one for low-risk.
- Use a review checklist (logic, tests, security, perf, docs).
- Require explicit approval on risky areas (auth, schema, filesystem).

## Continuous Integration/Deployment
- CI gates: lint, typecheck, tests, build must pass.
- Deploy on main with version tags; rollback plan documented.
- Post-deploy verification: health checks and smoke tests.

## Performance Benchmarking
- Tooling: `autocannon` or `k6` for API; Lighthouse/Web Vitals for UI.
- Baselines: set P95 latency and throughput targets per service.
- Regression detection: fail CI if thresholds exceeded.