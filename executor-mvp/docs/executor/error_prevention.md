# Error Prevention Mechanisms

## Pre-Commit Checklist (Common Pitfalls)
- Ports aligned across web and API; `VITE_API_URL` set and dev server restarted.
- Database schema initialized (`prisma db push`); Prisma client generated.
- Requests include `Content-Type: application/json`; bodies JSON-stringified.
- Validation schemas cover required/optional fields; clear error messages.
- Env files present (`.env.example`); secrets loaded via env; no plaintext secrets.
- CORS origin configured for local dev.

## Validation Tools
- Lint and typecheck: `npm run lint`, `npm run typecheck` before PR.
- Schema validation: Ajv/Zod gates on API inputs.
- Contract tests: Golden file tests for generated outputs.

## Monitoring & Runtime Errors
- Server logs: morgan + structured error logging; alert on 5xx spikes.
- Frontend: error boundaries and network error handling.
- Post-deploy health checks: automated `GET /healthz` and critical path probes.