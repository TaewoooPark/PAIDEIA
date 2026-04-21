---
description: Save a clean reference derivation of a target equation or theorem to derivations/. Draws from course materials (textbook, lecture notes) rather than testing the user.
argument-hint: <equation or theorem name>
---

Load `skills/course-builder/SKILL.md` for material locations. Also read `course-index/summary.md` to resolve the target.

Target: $ARGUMENTS

Procedure:

1. **Locate the derivation** in `converted/textbook/*.md` and `converted/lectures/*.md`. If present in both, prefer the textbook (usually cleaner).
2. **If not in materials**, derive it from first principles using standard techniques for the course's domain. Cite which earlier results you're using.
3. **Format as a clean reference markdown file** with:
   - Starting definitions/assumptions clearly stated
   - Each step with a one-line explanation of why
   - Boxed final result
   - Short "물리적/수학적 해석" at the end
   - Typical pitfalls (common student errors) listed at bottom
4. **Save to** `derivations/<slug>.md`. Slug is lowercase-hyphenated from the target name.
5. **Print**: "`derivations/<slug>.md` 저장. 열어서 읽어보고, 이해 안 되는 step 있으면 질문해."

Do NOT quiz or prompt the user — this command is a pure reference-writer. The user explicitly set this up so they can read rather than type.

## Format convention (align with existing `derivations/` files if any)

```markdown
# <Target name>

**목표.** <statement of what we want to derive>

**출발점.** <definition / law / axiom / earlier result>

---

### 1단계 — <step description>

$$<step equation>$$

<why this step>

### 2단계 — ...

...

---

**결과.**
$$\boxed{\;<final>\;}$$

**해석.** <1-2 sentences on what this means physically/mathematically>

**주의할 pitfall.**
- <common error 1>
- <common error 2>

**참조.** <source section in converted/>
```

Preserve LaTeX, use `$...$` and `$$...$$`. No emojis except the final $\blacksquare$ or ∎ at the result.
