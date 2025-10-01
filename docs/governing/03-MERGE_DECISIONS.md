# Workflow Merge Decisions

## Decision 001: Foundation Choice
**Date**: 2025-10-01
**Decision**: Start with Executor MVP as foundation
**Rationale**: 
- Most recent clean win
- Simplest codebase
- Already has contracts folder
- TypeScript/Node stack
- Wife-approved win

**Parked Options**:
- Repo #18 (H3A): Extract patterns in Phase 2
- Repo #21 (Bootstrap): Assess in Phase 3+

**Next**: Copy Executor MVP into N_grade repo

---

## Decision 002: Run and Generate First Project
**Date**: 2025-10-01
**Decision**: Use the imported Executor MVP to generate a "hello-world-app" from the UI.
**Rationale**:
- Validates end-to-end functionality in the new repo location
- Reinforces the "one increment = one win" rule

**Steps**:
1. Copy `.env.example` to `.env` and set `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`.
2. Start dev server: `npm --prefix /Users/Yousef_1/Coding/N_grade/executor-mvp run dev`.
3. Open `http://localhost:3000` and submit the minimal prompt.
4. Verify files under `/Users/Yousef_1/Coding/N_grade/executor-mvp/output/<slug>` and browse via `/output/<slug>/`.
5. Commit results: `git add -A && git commit -m "chore: generated hello-world-app via executor"`.
6. Stop for the day.
