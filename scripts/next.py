#!/usr/bin/env python3
"""
next.py - the engine's state oracle. What is next, from artifacts, never from reasoning.

WHY A SCRIPT
    The book repo's Rule 10: /book-resume determines NEXT_ACTION by running
    pipeline_state.py, and the model must not determine it from file contents,
    context, or reasoning. That rule held when others did not. This is the
    engine's equivalent. /gw reads this output and shows it; it never computes
    "next" itself.

HOW "NEXT" IS DECIDED (first match wins)
    1. A chapter in runs/ with an inbox.md       -> parked; the inbox comes first
    2. A bake-off packet with an unfilled verdict -> read it (work already done)
    3. A chapter in runs/ that is in progress     -> continue at its next stage
    4. The lowest chapter not refined anywhere    -> start it
    5. Everything refined                         -> whole-book QA

USAGE
    python3 scripts/next.py              # the board, human-readable
    python3 scripts/next.py --chapter 12 # that chapter's next stage only
    python3 scripts/next.py --json
"""

import argparse
import glob
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import resolve_book  # noqa: E402

STAGES = [
    # (artifact that must exist to be PAST this stage, stage name, command)
    ("interview.md", "interview", "/gw-interview"),
    ("research.md",  "research",  "/gw-research"),
    ("draft.md",     "draft",     "/gw-draft"),
    ("refined.md",   "refine",    "/gw-refine"),
]


def chapter_dirs():
    out = {}
    for d in sorted(glob.glob(os.path.join(REPO, "runs", "ch*"))):
        m = re.fullmatch(r"ch(\d{2})", os.path.basename(d))
        if m:
            out[int(m.group(1))] = d
    return out


def chapter_state(n, d):
    """Return (stage, command, detail) for chapter n whose runs dir is d (or None)."""
    if d is None or not os.path.isdir(d):
        return "interview", "/gw-interview", "not started"
    have = set(os.listdir(d))
    # Terminal state, checked first. "verdict" had no exit: on 2026-09-18 Ch12
    # was landed into the book repo and this still answered "waiting on your
    # verdict", and would have gone on answering it with Ch13 fully refined
    # beside it. Nothing else in this house writes runs/chNN/verdict.md - only
    # bakeoff.py writes one, and into bakeoff/chNN/, a different file. The
    # verdict step of /gw-chapter writes this one, with the real clock, once
    # the author has actually given the verdict.
    if "verdict.md" in have:
        return "shipped", None, "verdict recorded; chapter is done here"
    if "inbox.md" in have:
        return "parked", "/gw-inbox", "a cold desk could not decide; the inbox holds the question"
    for artifact, stage, cmd in STAGES:
        if artifact not in have:
            return stage, cmd, f"{artifact} missing"
    plate = "plate.svg" in have
    return "verdict", "/gw-compile", ("refined; plate present" if plate else "refined; no plate yet (optional)")


def bakeoffs_waiting():
    waiting = []
    for d in sorted(glob.glob(os.path.join(REPO, "bakeoff", "ch*"))):
        v = os.path.join(d, "verdict.md")
        if os.path.isfile(v) and "variant-_" in open(v, encoding="utf-8").read():
            waiting.append(os.path.basename(d))
    return waiting


def inbox_counts():
    """(open, ruled). A RULED item is the author's decision that has not landed.

    Counted separately and shown on the board because it is invisible otherwise:
    on 2026-09-14 three rulings were recorded and never applied while every
    surface reported nothing waiting. An item the author has answered is not the
    same as an item that is finished.
    """
    o = r = 0
    for p in glob.glob(os.path.join(REPO, "inbox", "*.md")):
        txt = open(p, encoding="utf-8").read()
        if re.search(r"^status:\s*open\s*$", txt, re.M):
            o += 1
        elif re.search(r"^status:\s*ruled\s*$", txt, re.M):
            r += 1
    return o, r


def prose_gate():
    """Return the blocking reason from okf_gate.py, or None when prose may be written.

    WHY THE ORACLE ASKS. On 2026-09-14 the citation gate was red for a whole day
    while this script kept answering "/gw 12". Rule 4 already says the gate is
    blocking; it was simply invisible on the one surface the author reads every
    session, so he would have met it only after starting work. An oracle that
    names an action the gate forbids is a plausible wrong answer, which is the
    failure this repo is built against.
    """
    try:
        r = subprocess.run([sys.executable, os.path.join(HERE, "okf_gate.py")],
                           cwd=REPO, capture_output=True, text=True, timeout=120)
    except Exception:
        return None          # cannot run it: say nothing rather than invent a block
    if r.returncode == 0:
        return None
    for line in (r.stdout + r.stderr).splitlines():
        line = line.strip()
        if line.startswith("x "):
            return line[2:].strip()
    return "okf_gate.py is blocking; run it to see why"


def compute(book):
    info = book["info"]
    total = info.get("chapter_count") or 0
    shipped = set()
    # resolve_book reports directory names: "ch01", "prologue", "introduction".
    # The first version of this checked name.isdigit(), matched nothing, and
    # reported 0 shipped and "start at chapter 1" for a book with 13 refined -
    # a plausible wrong answer, caught only by running it against the real repo.
    for name in info.get("refined_chapters", []):
        m = re.fullmatch(r"ch(\d+)", name)
        if m:
            shipped.add(int(m.group(1)))
    runs = chapter_dirs()

    per_chapter = {}
    for n, d in runs.items():
        stage, cmd, detail = chapter_state(n, d)
        per_chapter[n] = {"stage": stage, "command": cmd, "detail": detail,
                          "shipped_by_book_pipeline": n in shipped}

    parked = sorted(n for n, s in per_chapter.items() if s["stage"] == "parked")
    in_progress = sorted(n for n, s in per_chapter.items()
                         if s["stage"] not in ("parked", "verdict", "shipped"))
    awaiting_verdict = sorted(n for n, s in per_chapter.items() if s["stage"] == "verdict")
    packets = bakeoffs_waiting()
    open_items, ruled_items = inbox_counts()

    candidates = [n for n in range(1, total + 1) if n not in shipped and n not in runs]
    next_new = candidates[0] if candidates else None

    if parked:
        n = parked[0]
        nxt = {"action": "inbox", "command": "/gw inbox", "chapter": n,
               "why": f"Chapter {n} is parked on a question only you can answer."}
    elif packets:
        nxt = {"action": "verdict", "command": f"/gw compare {packets[0][2:]}", "chapter": int(packets[0][2:]),
               "why": f"A blind comparison for {packets[0]} is built and waiting on your read."}
    elif in_progress:
        n = in_progress[0]
        s = per_chapter[n]
        nxt = {"action": "continue", "command": f"/gw {n}", "chapter": n,
               "why": f"Chapter {n} stopped at {s['stage']} ({s['detail']})."}
    elif awaiting_verdict:
        n = awaiting_verdict[0]
        nxt = {"action": "verdict", "command": f"/gw {n}", "chapter": n,
               "why": f"Chapter {n} is refined and waiting on your verdict."}
    elif next_new:
        nxt = {"action": "start", "command": f"/gw {next_new}", "chapter": next_new,
               "why": f"Chapter {next_new} has not started."}
    else:
        nxt = {"action": "qa", "command": "/gw qa", "chapter": None,
               "why": "Every chapter is refined. Whole-book QA is next."}

    # A gated action is not the next action. Checked last so the rest of the
    # board still computes normally, and reported rather than hidden.
    blocked = prose_gate()
    if blocked and nxt["action"] in ("start", "verdict", "shadow", "qa"):
        nxt = {"action": "unblock", "command": "fix the blocking citation, then /gw",
               "chapter": nxt.get("chapter"),
               "why": ("No desk may write prose while the citation gate is red: "
                       + blocked)}

    return {
        "book": info.get("title"), "chapters_total": total,
        "prose_gate_blocked": blocked,
        "shipped_by_book_pipeline": sorted(shipped),
        "engine_chapters": per_chapter,
        "inbox_open": open_items, "inbox_ruled": ruled_items,
        "bakeoffs_awaiting_verdict": packets,
        "next": nxt,
    }


def branch_line():
    """From local refs only - no fetch here. session-start.sh fetched already."""
    import subprocess
    def g(*a):
        try:
            return subprocess.run(["git", *a], cwd=REPO, capture_output=True, text=True).stdout.strip()
        except Exception:
            return ""
    br = g("symbolic-ref", "--short", "HEAD")
    if not br:
        return None
    # A missing origin/main must read as unknown, never as 0. The first version
    # used `or "0"` and reported "0 ahead, 0 behind" on a repo whose empty clone
    # had no remote-tracking refs at all.
    has_main = subprocess.run(["git", "rev-parse", "--verify", "--quiet", "origin/main"],
                              cwd=REPO, capture_output=True).returncode == 0
    ahead = g("rev-list", "--count", f"origin/main..{br}") if has_main else ""
    behind = g("rev-list", "--count", f"{br}..origin/main") if has_main else ""
    dirty = len([l for l in g("status", "--porcelain").split("\n") if l.strip()])
    note = ""
    if not has_main:
        note = " · vs main: UNKNOWN (origin/main not fetched)"
    elif br == "main":
        note = " · on main"
    elif ahead.isdigit() and behind.isdigit() and int(ahead) and not int(behind):
        note = f" · {ahead} commit(s) saved here, not yet on main - say \"put it on main\" when ready"
    elif behind.isdigit() and int(behind):
        note = f" · {behind} BEHIND main"
    if dirty:
        note += f" · {dirty} uncommitted"
    return f"branch: {br}{note}"


def render(state):
    L = []
    bl = branch_line()
    if bl:
        L.append(bl)
    shipped = len(state["shipped_by_book_pipeline"])
    L.append(f"{state['book']} · {state['chapters_total']} chapters · {shipped} landed in the book")
    eng = state["engine_chapters"]
    if eng:
        parts = [f"ch{n:02d} {s['stage']}" for n, s in sorted(eng.items())]
        L.append(f"this house: {', '.join(parts)}")
    else:
        L.append("this house: no chapter started yet")
    if state["inbox_open"]:
        L.append(f"inbox: {state['inbox_open']} question(s) waiting on you")
    if state.get("inbox_ruled"):
        L.append(f"inbox: {state['inbox_ruled']} ruling(s) you made that have not "
                 f"landed yet - say /gw inbox")
    if state["bakeoffs_awaiting_verdict"]:
        L.append(f"bake-off: {', '.join(state['bakeoffs_awaiting_verdict'])} built, verdict unwritten")
    n = state["next"]
    L.append("")
    L.append(f"NEXT_ACTION: {n['command']}")
    L.append(f"  {n['why']}")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="What is next, from artifacts.")
    ap.add_argument("--chapter", type=int)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    cfg = resolve_book.load_config()
    repo_root, _, _ = resolve_book.resolve(cfg)
    if not repo_root:
        print("next: no book repo resolvable - run scripts/resolve_book.py", file=sys.stderr)
        return 2
    book = resolve_book.inspect(repo_root, require_okf=False)
    if book["problems"]:
        print("next: book repo has problems - run scripts/resolve_book.py", file=sys.stderr)
        return 1

    if a.chapter:
        d = chapter_dirs().get(a.chapter)
        stage, cmd, detail = chapter_state(a.chapter, d)
        out = {"chapter": a.chapter, "stage": stage, "command": cmd, "detail": detail}
        print(json.dumps(out) if a.json else f"ch{a.chapter:02d}: next stage is {stage} ({detail}) -> {cmd} {a.chapter}")
        return 0

    state = compute(book)
    print(json.dumps(state, indent=2) if a.json else render(state))
    return 0


if __name__ == "__main__":
    sys.exit(main())
