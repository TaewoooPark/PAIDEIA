---
description: Show HW/example coverage of course sections from course-index/coverage.md. HW density = exam probability; surface the exam-hot zones.
argument-hint: [§ number, or "hot" to list exam-primary zones, or "all"]
---

Read `course-index/coverage.md`. If missing, tell the user to run `/analyze` first.

Query: $ARGUMENTS

**Core premise.** HW coverage is an exam-probability signal. Sections the professor drilled into HW are where the exam points live. "No HW coverage" is not a red flag — it's a low-risk zone the professor chose to omit.

Procedure:

**If query is a § number or section name:**
Show which problems cover that section, and adjacent sections (§±1) for context. List the patterns involved. State the exam tier (🔥🔥 / 🔥 / 🟡 / ⚪) and the drill recommendation that follows.

**If query is `hot` (or `primary`, `exam`, `risk`, `blind` for backwards compatibility):**
Return 🔥🔥 Exam-primary and 🔥 Exam-likely sections, ranked by HW density (highest first). For each:
- List the HW problems that target it (these are your drill anchors)
- One-line drill recommendation:
  - Many HW, pattern fluent → `/twin <hw-id>` (build surface variance)
  - Many HW, strategy shaky → `/blind <hw-id>` (strategy-check on the real HW)
  - User has solved HW but forgets the pattern → `/pattern <Pk>` then `/quiz §<n> 3`

Do **not** recommend `/derive` here as a default — derivations are for reading gaps, not for drilling exam-likely zones. Use `/derive` only if the user explicitly asks for a clean reference.

**If query is `all` or empty:**
Render an exam-tier distribution table:

| Exam tier | Count | Sections |
|---|---|---|
| 🔥🔥 Exam-primary (3+ HW) | n | list |
| 🔥 Exam-likely (2 HW) | n | list |
| 🟡 Exam-possible (1 HW) | n | list |
| ⚪ Low-risk (no HW) | n | list |

Plus the "Recommended drill priority" section from `coverage.md` (ordered by HW density, not by absence).

**Low-risk section handling.** If the user insists on drilling a ⚪ section, warn once: "HW에 한 번도 안 나온 구간은 시험 출제 확률이 낮아. 시간 없으면 🔥🔥부터." Then comply if they still want to.

**Always close with:**
"🔥🔥 중에서 지금 당장 드릴 걸 1개만 고른다면? 시간 몇 분 남았어?"

Output goal: exam-point maximization. Steer time toward HW-dense zones.
