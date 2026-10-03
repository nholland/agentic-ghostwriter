#!/usr/bin/env python3
"""
distill_status.py - which landed distillations need a second look, counted.

WHY THIS EXISTS
    A chapter's distillation is derived from its refined prose. /gw-edit
    refreshes the chapter it touched, but an edit that lands any other way, or a
    bulk pass over many chapters, leaves distillations behind the prose with
    nothing noticing. This is the mechanical half of the old `distill
    --refresh`: it says WHICH chapters to re-distill. The rewriting stays with
    the Line Editor (see "Fleet refresh" in .claude/skills/gw-edit/SKILL.md).

WHAT IT REPORTS, per chNN chapter under {bookRoot}/chapters/
    MISSING    no distillation.md next to refined.md
    MALFORMED  distillation.md lacks a required label (Mechanism, Conversation
               sentence, Lesson, Challenge, Practice) or has no numbered practice
    STALE      the PROSE of refined.md (everything above its first "Editor's
               Notes" heading, or the whole file when it has none) differs from
               the prose as it stood when distillation.md was last committed.
               A change confined to the Editor's Notes is not stale: the
               distillation is derived from the prose only. Even so, STALE is a
               prompt to re-read, not proof of error: a typo fix leaves the
               distillation right. (First version compared commit times alone
               and flagged Ch9 for a commit that only deleted a stale copy of
               the distillation from below its Editor's Notes.)
    UNCHECKED  git history unavailable for the file; it is not guessed
    ok         none of the above

    prologue/ and introduction/ are not chNN chapters and hold no distillation.md;
    they are named in the output as not read, not silently ignored.

USAGE
    python3 scripts/distill_status.py            # report; always exit 0
    python3 scripts/distill_status.py --strict   # exit 1 if any chapter is not ok
    python3 scripts/distill_status.py --book-root PATH --repo PATH   # fixtures
"""

import argparse
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import resolve_book  # noqa: E402

LABELS = ["**Mechanism:**", "**Conversation sentence:**", "**Lesson:**",
          "**Challenge:**", "**Practice:**"]
CHAPTER_DIR = re.compile(r"^ch\d+$")
PRACTICE_ITEM = re.compile(r"^\s*\d+\.\s+\S", re.M)
NOTES_HEADING = re.compile(r"^#{2,3}\s+Editor's Notes", re.M | re.I)


def prose_of(text):
    """The chapter's prose: everything above the first Editor's Notes heading."""
    m = NOTES_HEADING.search(text)
    return (text[:m.start()] if m else text).strip()


def show_at(repo, commit, path):
    r = subprocess.run(["git", "-C", repo, "show", f"{commit}:{path}"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def last_commit(repo, path):
    r = subprocess.run(["git", "-C", repo, "log", "-1", "--format=%H", "--", path],
                       capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def commit_time(repo, path):
    r = subprocess.run(["git", "-C", repo, "log", "-1", "--format=%ct", "--", path],
                       capture_output=True, text=True)
    out = r.stdout.strip()
    return int(out) if r.returncode == 0 and out else None


def classify(repo, chdir):
    refined = os.path.join(chdir, "refined.md")
    dist = os.path.join(chdir, "distillation.md")
    if not os.path.isfile(dist):
        return "MISSING", "no distillation.md beside refined.md"
    with open(dist, encoding="utf-8") as fh:
        text = fh.read()
    lacking = [l.strip("*:") for l in LABELS if l not in text]
    if lacking:
        return "MALFORMED", "lacks " + ", ".join(lacking)
    practice = text.split("**Practice:**", 1)[1]
    if not PRACTICE_ITEM.search(practice):
        return "MALFORMED", "Practice block has no numbered item"
    rt, dt = commit_time(repo, refined), commit_time(repo, dist)
    if rt is None or dt is None:
        return "UNCHECKED", "no git history for one of the two files"
    if rt > dt:
        then = show_at(repo, last_commit(repo, dist), os.path.relpath(refined, repo))
        if then is not None:
            with open(refined, encoding="utf-8") as fh:
                now = fh.read()
            if prose_of(then) == prose_of(now):
                return "ok", "refined.md changed after, but only its Editor's Notes"
        return "STALE", f"prose changed in refined.md since distillation.md was committed"
    return "ok", ""


def main():
    ap = argparse.ArgumentParser(description="Report stale or malformed distillations.")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--book-root")
    ap.add_argument("--repo", default=REPO)
    a = ap.parse_args()

    book_root = a.book_root
    if not book_root:
        rep = resolve_book.inspect(a.repo, require_okf=False)
        book_root = rep["info"].get("bookRoot")
    if not book_root:
        print("distill_status: no bookRoot; run resolve_book.py", file=sys.stderr)
        return 1
    chapters = os.path.join(book_root, "chapters")
    if not os.path.isdir(chapters):
        print(f"distill_status: {chapters} does not exist", file=sys.stderr)
        return 1

    rows, skipped = [], []
    for name in sorted(os.listdir(chapters)):
        chdir = os.path.join(chapters, name)
        if not os.path.isdir(chdir):
            continue
        if not CHAPTER_DIR.match(name):
            skipped.append(name)
            continue
        if not os.path.isfile(os.path.join(chdir, "refined.md")):
            continue
        rows.append((name, *classify(a.repo, chdir)))

    for name, status, note in rows:
        print(f"  {name:<6} {status:<10} {note}".rstrip())
    flagged = [r for r in rows if r[1] != "ok"]
    print(f"distill_status: {len(rows)} chapter(s) read, "
          f"{len(rows) - len(flagged)} ok, {len(flagged)} to look at"
          + (f"; not chNN, not read: {', '.join(skipped)}" if skipped else ""))
    if flagged:
        print("next: re-read the flagged chapters; refresh per 'Fleet refresh' in "
              ".claude/skills/gw-edit/SKILL.md")
    return 1 if (a.strict and flagged) else 0


if __name__ == "__main__":
    sys.exit(main())
