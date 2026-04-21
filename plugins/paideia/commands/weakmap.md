---
description: Priority-ranked weakness report. No arg → fresh report from latest errors per pattern. With concept arg → patch latest report by adding the user-declared weakness, save as new timestamped file.
argument-hint: [개념 텍스트 (선택)]
---

Arguments: $ARGUMENTS

목적: 사용자가 공부하다가 "나 이 포인트 약한 것 같아"라고 느낄 때 바로 `/weakmap <개념>`으로 적어두면 보고서에 누적된다. 인자 없이 부르면 최근 오답 기록 기준으로 스냅샷을 새로 찍는다.

## 저장 규약

- 보고서 디렉토리: `weakmap/`
- 파일명: `weakmap/weakmap_<YYYY-MM-DD_HHmm>.md`
- 상단 제목: `# Weakmap — <YYYY-MM-DD HH:mm>`
- **절대 덮어쓰지 말 것.** 항상 새 타임스탬프로 신규 파일 저장 (history 유지).
- "최신 보고서" = `weakmap/` 내 파일 중 mtime이 가장 최근인 것.

## 분기

### Case A — 인자 없음 (fresh snapshot)

1. `errors/log.md`를 읽는다. YAML 엔트리를 `pattern` 기준으로 그룹화.
2. **각 pattern에서 `date`가 가장 최근인 엔트리 1개씩만** 추린다. (이전 에러는 이미 교정됐을 수 있으므로 "현재 약점 스냅샷"은 최신만.)
3. `course-index/coverage.md`의 blind spot 교차 참조.
4. (있으면) 최신 weakmap의 "User-declared weaknesses" 섹션은 **이어서 재수록**하지 않는다. 인자 없이 부른 건 에러 로그 기반 재스냅샷이 목적이므로, 이 모드에서는 user-declared 섹션은 비운다.
5. 아래 포맷으로 `weakmap/weakmap_<ts>.md`에 저장하고, 요약을 chat에 출력.

### Case B — 인자 있음 (concept patch)

"최신 보고서를 읽고 → user-declared 항목에 새 개념을 **누적(A,B에 C 추가)** → 전체 보고서를 A,B,C 기반으로 다시 써서 새 타임스탬프로 저장" 흐름.

1. 최신 weakmap 파일을 읽는다. 없으면 Case A를 먼저 실행한 것으로 간주하고 빈 보고서부터 시작.
2. 기존 파일의 "User-declared weaknesses" 섹션에서 항목 리스트를 추출 → `[A, B, ...]`.
3. `$ARGUMENTS` 전체를 새 개념 `C`로 취급. 중복이면 중복 제거. 최종 리스트 `[A, B, C]`.
4. 각 개념을 `course-index/patterns.md`, `course-index/summary.md`에 매핑 → 관련 §, Pk, 추천 드릴 식별.
5. `errors/log.md` 기반 최신 스냅샷(Case A의 1–3단계)도 함께 수행해 최신 에러 데이터와 user-declared 데이터를 **둘 다 반영**한 보고서를 새로 작성.
6. 새 타임스탬프로 `weakmap/weakmap_<ts>.md` 저장.

## 보고서 포맷

```markdown
# Weakmap — <YYYY-MM-DD HH:mm>

## Error histogram (최신 per pattern)

| Pattern/topic | Latest error type | Date | § |
|---|---|---|---|
...pattern별 최신 1건, 최근순 정렬.

## Top 5 weaknesses (priority ranked)

1. **<pattern 또는 topic>** — <한 줄 요약>
   → 추천: `/<command> <target>`

(error_type에 따른 추천 규칙:)
- `pattern-missed` / `wrong-variable` → `/blind <problem>` 또는 `/derive <concept>`
- `algebraic` / `sign` → `/quiz <topic> 3`
- `definition` → `converted/lectures/`의 해당 § 5분 재독
- `wrong-end-form` → `/pattern <Pk>` 인식 드릴

## User-declared weaknesses

(Case B에서만 채워짐. Case A는 비움.)

- **<개념 A>** — 관련 §<x>, P<k>. 추천: `/<command>`
- **<개념 B>** — ...
- **<개념 C (이번에 추가)>** — ...

## Exam-hot zones not yet drilled

`coverage.md`에서 🔥🔥/🔥 (Exam-primary, Exam-likely)로 표시됐지만 `errors/log.md`에 entry가 없는 §:
- §X, §Y

→ HW 밀도가 높은 구간인데 아직 에러 로그에 안 찍혔다는 건 (a) 이미 잘하거나 (b) 아직 안 풀어본 것. `/blind <hw-id>`로 빠르게 확인.

(⚪ Low-risk 구간은 이 섹션에 포함하지 않는다. HW에 없으면 시험 확률도 낮으니 weakmap의 우선순위에서도 제외.)

## One-line verdict

<지금 가장 먼저 드릴할 한 가지>
```

## Chat 출력

- 저장한 파일 경로 1줄
- 보고서 전문은 붙여넣지 말고, **Top 5 + one-line verdict만** 요약해서 출력 (30줄 이내)
- 끝에 안내: "추가 약점이 생기면 `/weakmap <개념>`으로 패치, `/quiz weakmap`으로 이 보고서 기반 문제 생성."
