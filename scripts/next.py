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
    1. A chapter parked on an open inbox item          -> the inbox comes first
    2. A bake-off packet with an unfilled verdict      -> read it (work already done)
    3. A chapter in runs/ that is in progress          -> continue at its next stage
    4. The lowest chapter not refined anywhere         -> start it; if the book
       pipeline already holds its brief, start it COLD as a shadow run
    5. Everything refined                              -> whole-book QA

TWO PIPELINES, ONE BOARD
    While both pipelines are live a chapter can exist in the book repo (the
    one that ships) and in runs/ (this house). The board says which is which.
    When the book pipeline has researched a chapter that this house has not
    touched, the brief is the automation boundary already crossed: the house
    can draft it cold, in parallel, from the same brief. That is the Ch12
    bake-off design, and the oracle names it rather than leaving it to be
    remembered.

STAGES AND WHO RUNS THEM
    interview  author   research  cold   draft  cold   refine  cold
    plate      cold     verdict   author
    --floor lists every chapter whose next stage is cold, for parallel dispatch.

USAGE
    python3 scripts/next.py              # the board, human-readable
    python3 scripts/next.py --chapter 12 # that chapter's next stage only
    python3 scripts/next.py --floor      # every cold stage that can run now
    python3 scripts/next.py --json
"""

import argparse
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
# Where runs/, inbox/ and bakeoff/ live. Overridable so the test harness can
# point the oracle at a fixture tree instead of the real one.
STATE = os.environ.get("GW_STATE_ROOT", REPO)
sys.path.insert(0, HERE)
import resolve_book  # noqa: E402

STAGES = [
    # (artifact that must exist to be PAST this stage, stage name, command, who runs it)
    ("interview.md", "interview", "/gw-interview", "author"),
    ("research.md",  "research",  "/gw-research",  "cold"),
    ("draft.md",     "draft",     "/gw-draft",     "cold"),
    ("refined.md",   "refine",    "/gw-refine",    "cold"),
]
COLD = {"research", "draft", "refine", "plate"}


def chapter_dirs():
    out = {}
    for d in sorted(glob.glob(os.path.join(STATE, "runs", "ch*"))):
        m = re.fullmatch(r"ch(\d{2})", os.path.basename(d))
        if m:
            out[int(m.group(1))] = d
    return out


def open_inbox_by_chapter():
    """Chapter -> [item ids] for OPEN inbox items. inbox.py is the one inbox;
    the first version of the skills also wrote runs/chNN/inbox.md, a second
    mechanism /gw-inbox never read, so a desk's question could park a chapter
    invisibly. Both are read here; only the first is written anywhere now."""
    out = {}
    for p in glob.glob(os.path.join(STATE, "inbox", "*.md")):
        txt = open(p, encoding="utf-8").read()
        if not re.search(r"^status:\s*open\s*$", txt, re.M):
            continue
        m = re.search(r"^chapter:\s*(\d+)\s*$", txt, re.M)
        i = re.search(r"^id:\s*(\S+)", txt, re.M)
        if m:
            out.setdefault(int(m.group(1)), []).append(i.group(1) if i else "?")
    return out


def book_brief_exists(book_info, n):
    chapters = book_info.get("chapters") or ""
    return os.path.isfile(os.path.join(chapters, f"ch{n:02d}", "research.md"))


def chapter_state(n, d, parked_ids=None, shadow_brief=False):
    """Return (stage, command, detail, who) for chapter n whose runs dir is d (or None)."""
    have = set(os.listdir(d)) if d and os.path.isdir(d) else set()
    if parked_ids:
        return ("parked", "/gw-inbox",
                f"a cold desk could not decide; inbox item(s) {', '.join('#' + i for i in parked_ids)} hold the question",
                "author")
    if "inbox.md" in have:
        return ("parked", "/gw-inbox",
                "legacy runs/chNN/inbox.md present - move its question into inbox.py (--add --chapter N) so /gw-inbox can see it",
                "author")
    if not have:
        if shadow_brief:
            return ("draft", "/gw-chapter", "not started here; the book pipeline's brief exists - "
                    "run with --shadow to draft cold from it in parallel", "cold")
        return "interview", "/gw-interview", "not started", "author"
    for artifact, stage, cmd, who in STAGES:
        if artifact not in have:
            if stage == "research" and shadow_brief:
                return ("draft", "/gw-chapter", "interview done here and the book pipeline's brief exists - "
                        "--shadow drafts from that brief; otherwise /gw-research builds the house's own", "cold")
            detail = f"{artifact} missing"
            if stage == "draft" and "brief-gaps.md" in have:
                detail += "; brief-gaps.md outstanding (gaps a cold desk could not close were sent to the inbox)"
            return stage, cmd, detail, who
    plate = "plate.svg" in have
    return "verdict", "/gw-compile", ("refined; plate present" if plate else "refined; no plate yet (optional)"), "author"


def bakeoffs_waiting():
    waiting = []
    for d in sorted(glob.glob(os.path.join(STATE, "bakeoff", "ch*"))):
        v = os.path.join(d, "verdict.md")
        if os.path.isfile(v) and "variant-_" in open(v, encoding="utf-8").read():
            waiting.append(os.path.basename(d))
    return waiting


def inbox_open():
    n = 0
    for p in glob.glob(os.path.join(STATE, "inbox", "*.md")):
        if re.search(r"^status:\s*open\s*$", open(p, encoding="utf-8").read(), re.M):
            n += 1
    return n


def parked_open():
    n = 0
    for p in glob.glob(os.path.join(STATE, "runs", "parked", "*.md")):
        if re.search(r"^status:\s*open\s*$", open(p, encoding="utf-8").read(), re.M):
            n += 1
    return n


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
    parked_map = open_inbox_by_chapter()

    per_chapter = {}
    for n, d in runs.items():
        stage, cmd, detail, who = chapter_state(n, d, parked_map.get(n), book_brief_exists(info, n))
        per_chapter[n] = {"stage": stage, "command": cmd, "detail": detail, "runs_by": who,
                          "shipped_by_book_pipeline": n in shipped,
                          "book_brief_exists": book_brief_exists(info, n)}

    parked = sorted(n for n, s in per_chapter.items() if s["stage"] == "parked")
    in_progress = sorted(n for n, s in per_chapter.items() if s["stage"] not in ("parked", "verdict"))
    awaiting_verdict = sorted(n for n, s in per_chapter.items() if s["stage"] == "verdict")
    packets = bakeoffs_waiting()
    open_items = inbox_open()

    candidates = [n for n in range(1, total + 1) if n not in shipped and n not in runs]
    next_new = candidates[0] if candidates else None
    next_new_shadow = bool(next_new and book_brief_exists(info, next_new))

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
    elif next_new and next_new_shadow:
        nxt = {"action": "shadow", "command": f"/gw {next_new} --shadow", "chapter": next_new,
               "why": (f"The book pipeline has researched Chapter {next_new}; this house can draft it cold "
                       f"from the same brief, in parallel, with no author time.")}
    elif next_new:
        nxt = {"action": "start", "command": f"/gw {next_new}", "chapter": next_new,
               "why": f"Chapter {next_new} has not started in either pipeline."}
    else:
        nxt = {"action": "qa", "command": "/gw qa", "chapter": None,
               "why": "Every chapter is refined. Whole-book QA is next."}

    # Every cold stage that could be dispatched right now, for the floor.
    floor = []
    for n, s in sorted(per_chapter.items()):
        if s["runs_by"] == "cold":
            floor.append({"chapter": n, "stage": s["stage"], "command": s["command"], "detail": s["detail"]})
        elif s["stage"] == "verdict" and "no plate" in s["detail"]:
            floor.append({"chapter": n, "stage": "plate", "command": "gw-designer", "detail": "refined, plate not drawn"})
    if next_new and next_new_shadow:
        floor.append({"chapter": next_new, "stage": "draft", "command": f"/gw-chapter {next_new} --shadow",
                      "detail": "shadow draft from the book pipeline's brief"})

    return {
        "book": info.get("title"), "chapters_total": total,
        "shipped_by_book_pipeline": sorted(shipped),
        "engine_chapters": per_chapter,
        "inbox_open": open_items, "parked_open": parked_open(),
        "bakeoffs_awaiting_verdict": packets,
        "floor": floor,
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
    L.append(f"{state['book']} · {state['chapters_total']} chapters · {shipped} shipped on the book pipeline")
    eng = state["engine_chapters"]
    if eng:
        parts = [f"ch{n:02d} {s['stage']}" + (" (shipped there too)" if s["shipped_by_book_pipeline"] else "")
                 for n, s in sorted(eng.items())]
        L.append(f"this house: {', '.join(parts)}")
    else:
        L.append("this house: no chapter started yet")
    if state["inbox_open"]:
        L.append(f"inbox: {state['inbox_open']} question(s) waiting on you")
    if state["parked_open"]:
        L.append(f"parked: {state['parked_open']} deferred question(s) with a revisit trigger")
    if state["bakeoffs_awaiting_verdict"]:
        L.append(f"bake-off: {', '.join(state['bakeoffs_awaiting_verdict'])} built, verdict unwritten")
    if state["floor"]:
        L.append("cold stages runnable now: " + ", ".join(f"ch{f['chapter']:02d} {f['stage']}" for f in state["floor"]))
    n = state["next"]
    L.append("")
    L.append(f"NEXT_ACTION: {n['command']}")
    L.append(f"  {n['why']}")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="What is next, from artifacts.")
    ap.add_argument("--chapter", type=int)
    ap.add_argument("--floor", action="store_true", help="list every cold stage that can run now")
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
        stage, cmd, detail, who = chapter_state(a.chapter, d, open_inbox_by_chapter().get(a.chapter),
                                                book_brief_exists(book["info"], a.chapter))
        out = {"chapter": a.chapter, "stage": stage, "command": cmd, "detail": detail, "runs_by": who,
               "shipped_by_book_pipeline": f"ch{a.chapter:02d}" in (book["info"].get("refined_chapters") or []),
               "book_brief_exists": book_brief_exists(book["info"], a.chapter)}
        print(json.dumps(out) if a.json else
              f"ch{a.chapter:02d}: next stage is {stage} ({detail}) -> {cmd} {a.chapter}  [{who}]")
        return 0

    state = compute(book)
    if a.floor:
        if a.json:
            print(json.dumps(state["floor"], indent=2))
        elif not state["floor"]:
            print("floor: nothing cold can run right now. Every open stage needs the author.")
        else:
            print(f"floor: {len(state['floor'])} cold stage(s) can run now, in parallel:")
            for f in state["floor"]:
                print(f"  ch{f['chapter']:02d}  {f['stage']:<9} {f['command']:<28} {f['detail']}")
        return 0
    print(json.dumps(state, indent=2) if a.json else render(state))
    return 0


if __name__ == "__main__":
    sys.exit(main())
