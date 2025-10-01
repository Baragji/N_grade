# Development Framework

Standards and practices for consistent, reliable delivery.

## Coding Practices
- TypeScript strict mode; no implicit `any`; consistent module boundaries.
- ESLint rules via repo config; fix warnings before PR.
- Naming: descriptive functions/modules; avoid one-letter vars.
- Error handling: return typed errors; never swallow exceptions.

## Style Guides
- Follow repo ESLint config; format consistently (editor settings).
- API: RESTful nouns, plural resources, consistent status codes.
- Frontend: Components by feature, colocate tests.

## Version Control & Branching
- Trunk-based with short-lived feature branches (`feat/<scope>`).
- Conventional commits for clarity (e.g., `feat:`, `fix:`, `docs:`).
- PRs require review, checks green, and linked specs/tests.

## Automated Testing Pipelines
- Unit: Vitest; fast feedback; run on push.
- Integration: supertest (API), Prisma test DB; run on PR.
- E2E: Playwright; smoke on PR, full on main nightly.
- Coverage thresholds enforced in CI for critical modules.

## CI Pipeline (GitHub Actions example)
- Steps: install deps → typecheck → lint → generate Prisma client → db push (test) → run unit/integration → build web.
- Cache node_modules and Prisma client to speed builds.
- Artifacts: test reports and `_executor_meta.json` for generated projects.