# Session Protocol (REQUIRED)

> The assistant MUST complete this protocol *before* any change.

## STARTUP (≈60s)
- [ ] Load `docs/state_management/NOW.md` → **STATE ALOUD:** current **Status**, **Branch**, **Active Work**
- [ ] Load `docs/state_management/NEXT.md` → **STATE ALOUD:** the **Must** task you will execute + its **DoD**
- [ ] Load latest `state_management/session/*.json` → **STATE ALOUD:** last **commit**, **time_min**, **tokens.in/out**
- [ ] Verify env: `npm run typecheck && npm run lint` → **STATE RESULTS**
- [ ] If UI relevant: confirm servers 3000 / 3001 / 5173
- [ ] **Declare intent:** “I will execute **[TASK]** with **DoD:** [CRITERIA]. Proceeding.”

## WORK (15–20 min)
- Execute the single **Must** to its **DoD**.
- After each logical change: `npm run typecheck && npm run lint`.

## END (≈3 min)
- [ ] Verify: `npm run typecheck && npm run build` (+ preview if UI)
- [ ] Update `docs/state_management/NOW.md` (Status/health/Active Work)
- [ ] Append `docs/state_management/DECISIONS.md` (Changed / Why / Verified)
- [ ] Write `docs/state_management/session/YYYY-MM-DD.json` (state snapshot)
- [ ] Update `docs/state_management/NEXT.md` (completed → archive/reprioritize)
