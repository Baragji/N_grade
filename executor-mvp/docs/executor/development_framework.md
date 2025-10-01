# Development Framework

This document defines how we build, test, review, and ship software in this repository. It establishes production-grade practices for reliability, security, and maintainability.

## Core Principles
- Ship small, reversible changes frequently.
- Automate checks: typecheck, lint, tests, coverage, security.
- Prefer explicitness over magic; document decisions and rationale.
- Treat CI failures as release blockers; keep `main` green.
- Secure by default: least privilege, no plaintext secrets.

## Branching Strategy
- Default branch: `main` always green (build + tests pass).
- Use short-lived feature branches: `feature/<slug>`; bugfix: `fix/<slug>`.
- Rebase or squash merge; avoid long-lived diverging branches.
- Keep PRs focused (<400 LOC diff when possible) with clear scope.

## Commit & PR Conventions
- Commits: imperative mood, concise subject, detailed body when needed.
- Reference issues in PR description; include context and screenshots/logs.
- Link to `docs/state_management/DECISIONS.md` when changing architecture or contracts.
- Fill `.github/PULL_REQUEST_TEMPLATE.md` checklists (QA, error prevention).
## Code Quality
- TypeScript strict mode; no `any` unless justified and documented.
- ESLint enforced with `--max-warnings=0` in CI.
- Format via project conventions (Prettier or ESLint rules).
- Avoid global state; prefer DI for testability.
- Keep functions small; favor pure functions where possible.

## Testing Policy
- Unit tests for core logic (schema validation, file writing).
- Integration tests for API endpoints using Supertest (happy + sad paths).
- Coverage: minimum 80% lines/branches on `src/**`; report `text` + `lcov`.
- Exclude generated `output/**` and `dist/**` from test discovery.
- Run tests locally before pushing; CI gates block on failures.

## Security & Secrets
- Never commit secrets; use `.env` locally and GitHub Secrets in CI.
- Validate inputs; sanitize paths (`toSafeRelative`) to prevent traversal.
- Pin critical dependencies; monitor advisories.
- Limit external calls; mock LLMs/providers in tests.

## Environments & Servers
- Local dev: ports `3000` (server), `5173` (frontend) standard.
- Health endpoints: `/healthz` returns 200; used for readiness.
- Docker provided (`docker-compose.yml`) for parity; prefer local for speed.

## CI & Automation
- Workflow at `.github/workflows/ci.yml` runs: typecheck, lint, tests, coverage, build.
- Upload artifacts: `coverage/` and executor metadata for traceability.
- Use `actions/setup-node` cache to accelerate installs.
- Block merges on failing checks; treat warnings as errors where configured.

## Documentation & Decision Logging
- Keep `docs/state_management/NOW.md` and `NEXT.md` current.
- Append architectural changes to `docs/state_management/DECISIONS.md`.
- Use `docs/executor/session_handoff.md` when preparing PRs and releases.

## Error Prevention Ritual
- Run `npm run typecheck && npm run lint && npm run test:coverage && npm run build` before PR.
- Check logs for schema validation issues and sanitize file paths.
- Validate CI artifact presence (`coverage/lcov.info`).

## Release Process
- Tag releases from green `main`; generate release notes.
- Build Docker images; verify health endpoints.
- Post-release monitoring checklist (errors, performance, coverage drift).

## Governance
- Review ownership in `CODEOWNERS` (add if missing); require approvals.
- Security reviews for new providers/integrations.
- Regular dependency updates with automated PRs.
