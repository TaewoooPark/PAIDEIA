---
description: Strategy-level blind drill on a known HW or example problem. User describes approach in prose (no math typing); Claude verifies against solution then saves clean reference to derivations/.
argument-hint: <problem-id, e.g. "hw4-p3" or "example-5.2">
---

Load `skills/exam-drill/SKILL.md`. Read `course-index/patterns.md`.

Target: $ARGUMENTS

Procedure:

1. **Load problem statement ONLY** from `converted/homework/<n>.md` or `converted/textbook/<ch>.md` (for textbook examples). Do NOT open the solution yet.

2. **Present the problem verbatim** to the user.

3. **Request strategy** (3–5 lines Korean, no math typing):
   ```
   전략만 말해줘 — 수식은 쓸 필요 없음.
   1) 어느 pattern 쓸 건지 (course-index/patterns.md의 Pk 번호)
   2) 어떤 변수 고정, 어떤 변수로 전개할지
   3) 최종 답이 어떤 형태일 거라 예상하는지
   ```

4. **Wait for response.** Do NOT proceed until the user answers.

5. **Load solution** from `converted/solutions/<n>.md` (or `converted/textbook/...` for example). Compare 3 axes:

   a. **Pattern identification** — correct Pk(s)?
   b. **Variable choice** — correct hold-fixed set?
   c. **End-form prediction** — matches actual answer structure?

6. **Feedback protocol:**
   - ✅ all three → confirm, then copy the relevant part of the solution into `derivations/blind-<id>.md` for permanent reference
   - ❌ on any axis → point out specifically which axis failed, WITHOUT revealing correct answer. Ask for revision.
   - After 2 failed attempts on same axis → give a one-line hint referencing the relevant pattern name.

7. **Log errors** if user needed revision. Append to `errors/log.md`:
   ```yaml
   - problem_id: <id>
     pattern_missed_initial: <Pk>
     strategy_error_type: pattern | variable-choice | end-form
     summary: "<1 line>"
     date: <ISO>
   ```

8. **Close:**
   "같은 유형 retention 확인하려면 `/twin <id>`로 변형 하나 풀어봐."

## Why strategy-based, not full-derivation

Exam pattern recognition is the bottleneck — if the user can articulate the correct strategy in 30 seconds, they'll execute it in 10 minutes on the exam. The strategy check IS the drill. Execution is practiced via paper + `/grade`.
