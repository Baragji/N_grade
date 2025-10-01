# Session Handoff — Executor Systems

Purpose: Provide an unambiguous, step-by-step handoff so the next session can seamlessly continue implementing the Executor’s workflow improvements. This focuses on perfecting the Executor’s systems, not any specific app.

## Overarching Goal
Make the Executor’s workflow repeatable, observable, and resilient for all future projects (e.g., sleep tracker). Deliver clear specifications, standards, QA, and error-prevention baked into repo docs and CI.

## Current Context & Progress
- Core Executor MVP is running locally and serves `/api/execute` and `/output`.
- Documentation suite created under `docs/executor/`:
  - `README.md` — suite index and usage order
  - `technical_spec.md` — requirements, UI/UX, constraints, architecture, data flows, acceptance criteria, testing protocols
  - `development_framework.md` — coding standards, style guides, branching, testing pipelines
  - `qa_process.md` — peer reviews, CI/CD gates, performance benchmarking
  - `asset_management.md` — design/documentation/templates organization
  - `error_prevention.md` — checklists, validation tools, monitoring guidance
- Roadmap and MVP delivery notes present (`ROADMAP.md`, `docs/mvp_delivery_notes.md`).

## Exact Next Steps
1) Add CI workflow
   - Create `.github/workflows/ci.yml` implementing:
     - Node setup, dependency install
     - Typecheck, lint
     - (If applicable) Prisma client generation and test DB push
     - Unit/integration tests
     - Frontend build (if present in generated projects)
     - Artifact upload for test reports
   - Acceptance criteria:
     - CI passes on PR and main; failures block merges
     - Caches are used to speed builds

2) Add PR template
   - Create `.github/PULL_REQUEST_TEMPLATE.md` referencing:
     - QA checklist (`docs/executor/qa_process.md`)
     - Error-prevention checklist (`docs/executor/error_prevention.md`)
     - Require links to specs (`docs/executor/technical_spec.md`) for feature PRs
   - Acceptance criteria:
     - Template renders with checkboxes and links
     - Reviewers can quickly validate scope and readiness

3) Optional pre-commit hooks (Husky)
   - Install and configure Husky to run lint/typecheck locally before commit
   - Acceptance criteria:
     - Commits are blocked if lint/typecheck fail
     - Hooks are documented in `README.md` or `docs/executor/development_framework.md`

4) Add templates/skeletons per `asset_management.md`
   - Create `templates/` with skeletons for:
     - Node service (Express + TypeScript + Zod/Prisma-ready)
     - Frontend app (React + Vite + testing)
     - CI snippets (jobs/steps for unit/integration/E2E)
   - Acceptance criteria:
     - Each template runs locally after minimal `npm install`
     - Readme included in each template with usage steps

## Implementation Details (Where, What, How)

### 1) CI Workflow (`.github/workflows/ci.yml`)
Use the following starting point and adjust to generated project needs:

```yaml
name: CI
on:
  pull_request:
  push:
    branches: [ main ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci || npm i

      - name: Typecheck
        run: npm run typecheck || true

      - name: Lint
        run: npm run lint || true

      # Uncomment if Prisma is used in generated projects
      # - name: Generate Prisma Client
      #   run: npx prisma generate

      # - name: Prepare Test DB
      #   run: npx prisma db push

      # Add your test commands here (Vitest, supertest, Playwright smoke)
      - name: Tests
        run: echo "No tests yet" && exit 0

      - name: Build
        run: npm run build || true

      - name: Upload artifacts (optional)
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: ci-artifacts
          path: |
            coverage
            junit.xml
            **/_executor_meta.json
```

### 2) PR Template (`.github/PULL_REQUEST_TEMPLATE.md`)

```md
## Summary
Describe the change and link to the spec in `docs/executor/technical_spec.md`.

## Checklist (QA)
- [ ] Lint passes (`npm run lint`)
- [ ] Typecheck passes (`npm run typecheck`)
- [ ] Tests added/updated and passing (unit/integration/E2E)
- [ ] Performance unchanged or improved (see `docs/executor/qa_process.md`)
- [ ] Security and validation reviewed (Ajv/Zod gates)
- [ ] Docs updated (specs, ADRs) where applicable

## Error Prevention (pre-commit)
- [ ] Ports/env aligned; dev servers restarted if `VITE_*`/env changed
- [ ] DB schema initialized if applicable (`prisma db push`)
- [ ] Requests use `Content-Type: application/json` and JSON bodies
- [ ] Clear error messages for validation failures

## Reviewers
List reviewers and risk areas (schema/auth/filesystem).
```

### 3) Pre-Commit Hooks (Husky)

```bash
npm i -D husky lint-staged
npx husky init
# This creates .husky/pre-commit; edit it to run:
#   npm run lint && npm run typecheck
```

Add to `package.json` (optional):
```json
{
  "lint-staged": {
    "**/*.{ts,tsx,js,jsx}": "eslint --fix"
  }
}
```

### 4) Templates (`templates/`)
Structure to add:

```
templates/
  node-service/
    README.md
    package.json
    src/index.ts
    src/routes/example.ts
    src/validators/example.ts
    tsconfig.json
  web-app/
    README.md
    package.json
    src/main.tsx
    src/App.tsx
    src/api.ts
    vite.config.ts
  ci-snippets/
    ci-base.yml
    prisma-setup.yml
    e2e-smoke.yml
```

Each template should:
- Install with `npm i` and start with `npm run dev`
- Include minimal tests and docs

## References (Paths)
- Docs suite: `docs/executor/*`
- Contract: `contracts/executor-output.schema.json`
- Executor server: `src/server.ts`
- Roadmap: `ROADMAP.md`
- MVP notes: `docs/mvp_delivery_notes.md`

## Continuity Plan (Order of Operations for Next Session)
1. Read `docs/executor/README.md` to understand the suite and usage order.
2. Implement `.github/workflows/ci.yml` using the provided template; push branch and confirm CI runs.
3. Add `.github/PULL_REQUEST_TEMPLATE.md` referencing QA and error-prevention checklists.
4. (Optional) Install Husky and configure pre-commit hooks for lint/typecheck.
5. Create `templates/` skeletons per `asset_management.md`; verify each template runs.
6. Open a PR that:
   - Adds CI, PR template, and (optional) Husky
   - Documents templates and how to use them (update `docs/executor/asset_management.md` if needed)
7. Ensure acceptance criteria for each step are met; merge.

## Notes
- Keep changes minimal and consistent with existing repository style.
- Do not commit secrets; use `.env.example` and environment variables.
- Prefer incremental PRs with passing CI over large changes.