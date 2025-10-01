# Next Up (≤3 items)
1) **Should:** [COMPLETED] Add `.github/workflows/ci.yml` and `.github/PULL_REQUEST_TEMPLATE.md` from `docs/executor/session_handoff.md`.  
   **DoD:** CI runs on PR/main; typecheck/lint/build steps execute; PR template shows QA/error-prevention checklists.
2) **Could:** Create `docs/state_management/handoff_template.md` and wire `scripts/check-state.sh` into dev ritual.  
   **DoD:** cold start uses files to resume; validator passes.
3) **Could:** Expand CI tests (Vitest/E2E) and artifact handling.  
   **DoD:** tests run; artifacts upload when present.
