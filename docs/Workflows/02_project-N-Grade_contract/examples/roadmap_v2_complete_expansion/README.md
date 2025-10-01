# Example: Roadmap V2 Complete Expansion

This is a **real, production-validated example** of the N-Grade Contract System in action.

---

## What This Example Shows

✅ **Real contract** that was used in production  
✅ **Real AI instructions** given to Codex  
✅ **Real validation report** showing ACCEPTED verdict  
✅ **Complete workflow** from contract to acceptance  

**Result:** 1,902-line production-ready roadmap document that passed all quality gates.

---

## The Challenge

**Before:** 195-line skeleton document with:
- 9 forbidden patterns (`(template)`)
- Only 1 code block (needed ≥30)
- Only 5 metrics (needed ≥40)
- 58 bullet points (needed ≥200)
- 0 success criteria sections (needed ≥20)

**After:** 1,902-line complete roadmap with:
- Zero forbidden patterns ✅
- 35+ code blocks ✅
- 45+ metrics ✅
- 250+ bullet points ✅
- 25+ success criteria sections ✅
- All quality gates passed ✅

**Exit code:** 0 (ACCEPTED)

---

## Files in This Example

### 1. `contract.json`

The actual contract handed to the AI assistant.

**Key quality gates:**
```json
{
  "line_count": {"min": 1200, "max": 2000},
  "forbidden_patterns": ["TODO", "TBD", "\\.\\.\\.", "(template)"],
  "required_patterns": {
    "```": 30,        // Code blocks
    "%|ms|seconds": 40,  // Metrics
    "^- ": 200,       // Bullet points
    "Success criteria": 20,
    "Evidence:": 50
  }
}
```

**Total deliverable size:** 1,902 lines

### 2. `instruction_prompt.md`

The instructions given to the AI (Codex in this case).

**Structure:**
- Contract reference and validation command
- Quality gate explanations with examples
- Code example standards
- Metric formatting requirements
- Self-validation instructions
- Execution timeline

**Key principle:** "DO NOT deliver until exit code is 0"

### 3. `validation_report.json`

The machine-generated report showing ACCEPTED verdict.

**Critical fields:**
```json
{
  "final_verdict": "ACCEPTED",
  "deliverable_status": [
    {
      "file_path": "autonomous_ai_roadmap_v2.md",
      "status": "PASS",
      "line_count": 1902,
      "quality_gate_results": {
        "min_lines": true,
        "required_sections": true,
        "forbidden_patterns": true,
        "required_patterns": true,
        "no_duplicate_sections": true,
        "structural_requirements": true
      },
      "failures": []
    }
  ]
}
```

**Exit code:** 0

---

## The Workflow

### Step 1: Contract Creation

```bash
# Contract defined quality requirements
cat contract.json
```

Specified exact requirements:
- 1,200-2,000 lines (was 195)
- Zero forbidden patterns (had 9)
- ≥30 code blocks (had 1)
- ≥40 metrics (had 5)
- No shortcuts, no templates, no TODOs

### Step 2: AI Instructions

```bash
# Instructions given to AI
cat instruction_prompt.md
```

Explained:
- Every quality gate in detail
- Examples of GOOD vs BAD code
- Examples of GOOD vs BAD metrics
- Self-validation requirement
- Zero tolerance policy

### Step 3: AI Execution

**AI (Codex) received:**
- Contract path
- Instruction document
- Reference materials
- Validation command

**AI delivered:**
- Expanded roadmap from 195 → 1,902 lines
- Added 34 code blocks (≥30 ✅)
- Added 40+ metrics (≥40 ✅)
- Added 200+ bullets (≥200 ✅)
- Removed all forbidden patterns ✅

**AI self-validated:**
```bash
python scripts/validate_contract.py \
  docs_ui_2_contracts/N-Grade_contract/roadmap_v2_complete_expansion.contract.json

echo $?
# Output: 0 (ACCEPTED)
```

### Step 4: Validation

```bash
# Validation ran automatically
python scripts/validate_contract.py contract.json \
  --report-path validation_report.json

# Result
cat validation_report.json | jq '.final_verdict'
# Output: "ACCEPTED"
```

**All quality gates passed:**
- ✅ Line count in range (1,902 / 1,200-2,000)
- ✅ All required sections present
- ✅ Zero forbidden patterns (0 / 0 allowed)
- ✅ All required patterns met (30+ code blocks, 40+ metrics, etc.)
- ✅ No duplicate sections
- ✅ Structural requirements met

### Step 5: Acceptance

**Exit code:** 0  
**Verdict:** ACCEPTED  
**Action:** Work accepted, moved to production

---

## Key Learnings

### 1. Machine Validation Works

**Zero ambiguity:**
- Exit code 0 = Accept
- Exit code 1 = Reject
- No negotiation, no exceptions

### 2. AI Responds to Clear Contracts

**When given:**
- Exact numeric thresholds
- Pattern examples (GOOD vs BAD)
- Self-validation instructions
- Zero tolerance policy

**AI delivers:**
- Work that passes first time
- Or iterates until it passes
- No shortcuts, no "good enough"

### 3. Quality Gates Enforce Quality

**Forbidden patterns prevented:**
- Template placeholders
- TODO markers
- Incomplete sections
- Ellipsis (indicating omitted content)

**Required patterns ensured:**
- Code examples
- Numeric metrics
- Detailed bullet points
- Success criteria
- Evidence references

### 4. Self-Validation Saves Time

**AI validated before submission:**
- Caught issues early
- Fixed before human review
- Delivered clean work first time

**Result:**
- Human only reviewed ACCEPTED work
- No back-and-forth cycles
- Time saved: ~2-3 hours

---

## Reproduce This Example

### 1. Copy Files to Your Repo

```bash
# Copy contract
cp contract.json /your/repo/contracts/my_roadmap.contract.json

# Copy instruction template
cp instruction_prompt.md /your/repo/instructions_roadmap.md
```

### 2. Customize Contract

```json
{
  "file_path": "docs/your_roadmap.md",  // Your deliverable
  "quality_gates": {
    "line_count": {"min": 500},  // Adjust as needed
    // ... customize gates
  }
}
```

### 3. Customize Instructions

```markdown
# Edit instructions_roadmap.md
- Replace contract path
- Adjust requirements
- Add domain-specific examples
```

### 4. Hand to AI

```bash
cat instructions_roadmap.md
# Copy output, send to your AI assistant
```

### 5. AI Delivers → Validate

```bash
python scripts/validate_contract.py contracts/my_roadmap.contract.json
echo $?
# 0 = Accept, 1 = Reject
```

---

## Metrics

### Effort

- **Contract creation:** 30 minutes
- **Instruction writing:** 45 minutes
- **AI execution:** 4 hours (autonomous)
- **Validation:** 5 seconds (automated)
- **Human review:** 15 minutes (accepted work only)

**Total human time:** ~1.5 hours (vs. 8-10 hours manual writing)

### Quality Improvements

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Lines | 195 | 1,902 | 10x |
| Code blocks | 1 | 35 | 35x |
| Metrics | 5 | 45 | 9x |
| Bullet points | 58 | 250+ | 4x |
| Success criteria | 0 | 25+ | N/A |
| Forbidden patterns | 9 | 0 | 100% |
| Exit code | 1 (REJECT) | 0 (ACCEPT) | ✅ |

### ROI

- **Time saved:** 6.5-8.5 hours
- **Quality improved:** All gates passed
- **First-pass acceptance:** Yes (after self-validation)
- **Rework cycles:** 0

**Verdict:** System works as designed.

---

## Troubleshooting

### "My AI doesn't deliver this quality"

**Likely causes:**
1. Contract gates too loose (tighten thresholds)
2. Instruction template not clear (add examples)
3. AI didn't self-validate (enforce in instructions)

**Solution:**
- Start with stricter gates
- Show GOOD vs BAD examples
- Make self-validation mandatory

### "Validation always rejects"

**Likely causes:**
1. Gates too strict for current capability
2. AI skipping self-validation
3. Contract unclear

**Solution:**
- Review validation report: `cat _reports/*.json`
- Start with looser gates, tighten iteratively
- Add more examples to instructions

### "AI argues with validator"

**Solution:**
```
"The machine doesn't negotiate. Fix the failures or don't submit."
```

Point AI to validation report JSON. No discussion.

---

## Next Steps

After reviewing this example:

1. **Copy contract structure** for your deliverables
2. **Adapt quality gates** to your domain
3. **Customize instruction template** for your AI
4. **Start with easier deliverable** (500 lines, fewer gates)
5. **Iterate and tighten** as AI improves

**The system works. Use it.** 🚀

---

*Example Status: Production-Validated*  
*Deliverable Size: 1,902 lines*  
*Validation Result: ACCEPTED (exit 0)*  
*Date: 2025-01*