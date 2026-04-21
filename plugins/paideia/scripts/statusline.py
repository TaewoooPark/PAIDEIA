#!/usr/bin/env python3
"""
PAIDEIA statusline — emits one line for Claude Code's statusline slot.

Format:  paideia · <COURSE_NAME> · D-N · <phase> · P<k> ↑
Color:   one neon color per session (hashed from session_id), truecolor ANSI.
Silent:  if CWD has no .course-meta, output nothing (Claude Code falls back).

Phases (artifact-derived, not time-derived):
  setup  — course-index/patterns.md absent
  diag   — patterns exist, no quizzes yet
  drill  — quizzes exist, no mock yet
  mock   — mock exists, no cheatsheet/final.* yet
  cram   — cheatsheet/final.{md,pdf} present
  cool   — D-0 (today == exam date) overrides all

Input (stdin, JSON, per Claude Code's statusline contract):
  { "session_id": "...", "cwd": "...", "workspace": {"current_dir": "..."} }
"""
from __future__ import annotations

import datetime
import glob
import hashlib
import json
import os
import re
import sys
from pathlib import Path

NEON = [
    (57, 255, 20),     # neon green
    (255, 20, 147),    # hot pink
    (0, 255, 255),     # electric cyan
    (204, 255, 0),     # laser yellow
    (255, 0, 255),     # magenta
    (191, 0, 255),     # electric purple
    (255, 102, 0),     # neon orange
    (176, 255, 0),     # acid green
    (255, 49, 49),     # neon red
    (125, 249, 255),   # electric blue
    (255, 111, 97),    # neon coral
    (255, 153, 0),     # tangerine
]


def pick_color(seed: str) -> str:
    h = int(hashlib.sha1(seed.encode("utf-8", "replace")).hexdigest()[:8], 16)
    r, g, b = NEON[h % len(NEON)]
    return f"\033[38;2;{r};{g};{b}m"


def parse_meta(cwd: Path) -> dict[str, str]:
    meta: dict[str, str] = {}
    p = cwd / ".course-meta"
    if not p.exists():
        return meta
    try:
        for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
            m = re.match(r"^\s*([A-Z_][A-Z0-9_]*)\s*:\s*(.+?)\s*$", line)
            if m:
                meta[m.group(1)] = m.group(2)
    except OSError:
        pass
    return meta


def days_until(exam_date: str) -> int | None:
    try:
        d = datetime.datetime.strptime(exam_date.strip(), "%Y-%m-%d").date()
    except (ValueError, AttributeError):
        return None
    return (d - datetime.date.today()).days


def detect_phase(cwd: Path, days: int | None) -> str:
    if days == 0:
        return "cool"
    cheatsheet = cwd / "cheatsheet"
    if (cheatsheet / "final.pdf").exists() or (cheatsheet / "final.md").exists():
        return "cram"
    if glob.glob(str(cwd / "mock" / "*.md")):
        return "mock"
    if not (cwd / "course-index" / "patterns.md").exists():
        return "setup"
    if glob.glob(str(cwd / "quizzes" / "*.md")):
        return "drill"
    return "diag"


def top_miss(cwd: Path) -> str | None:
    wms = sorted(glob.glob(str(cwd / "weakmap" / "weakmap_*.md")), reverse=True)
    if wms:
        try:
            text = Path(wms[0]).read_text(encoding="utf-8", errors="replace")
            m = re.search(r"\bP(\d+)\b", text)
            if m:
                return f"P{m.group(1)}"
        except OSError:
            pass
    log = cwd / "errors" / "log.md"
    if log.exists():
        try:
            text = log.read_text(encoding="utf-8", errors="replace")
            counts: dict[str, int] = {}
            for m in re.finditer(r"pattern:\s*(P\d+)", text):
                counts[m.group(1)] = counts.get(m.group(1), 0) + 1
            if counts:
                return max(counts, key=counts.get)
        except OSError:
            pass
    return None


def fmt_days(days: int | None) -> str | None:
    if days is None:
        return None
    if days == 0:
        return "D-0"
    if days > 0:
        return f"D-{days}"
    return f"D+{-days}"


def truncate(name: str, limit: int = 28) -> str:
    name = name.strip()
    if len(name) <= limit:
        return name
    return name[: limit - 1].rstrip() + "…"


def resolve_cwd(payload: dict) -> Path:
    for key in ("cwd",):
        v = payload.get(key)
        if v:
            return Path(v).expanduser()
    ws = payload.get("workspace") or {}
    v = ws.get("current_dir") or ws.get("cwd")
    if v:
        return Path(v).expanduser()
    return Path(os.getcwd())


def resolve_session(payload: dict) -> str:
    for key in ("session_id",):
        v = payload.get(key)
        if v:
            return str(v)
    sess = payload.get("session") or {}
    v = sess.get("id")
    if v:
        return str(v)
    return os.environ.get("USER", "paideia")


def main() -> int:
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        payload = {}

    cwd = resolve_cwd(payload)
    meta = parse_meta(cwd)
    if not meta:
        return 0  # silent — not a paideia course folder

    name = truncate(meta.get("COURSE_NAME", "course"))
    days = days_until(meta.get("EXAM_DATE", ""))
    phase = detect_phase(cwd, days)
    miss = top_miss(cwd)

    parts = ["paideia", name]
    d = fmt_days(days)
    if d:
        parts.append(d)
    parts.append(phase)
    if miss:
        parts.append(f"{miss} ↑")

    color = pick_color(resolve_session(payload))
    reset = "\033[0m"
    sys.stdout.write(f"{color}{' · '.join(parts)}{reset}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
