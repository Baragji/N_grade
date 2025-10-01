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
