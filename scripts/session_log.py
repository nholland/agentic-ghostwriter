#!/usr/bin/env python3
"""
session_log.py - mechanical session memory. Appended by the Stop hook.

WHY MECHANICAL
    The book repo's progress.md is hand-written by each command: a timestamp, what
    was done, what the author said, what is next. It is the reason cold re-entry
    works there - and it is also where the dates went wrong four times, where
    "Next command:" went stale, and where two or three entries a day produced
    ambiguous state. Every one of those failures is a human-or-model writing a
    fact that a script could have read.

    So this engine's log is derived: the real clock, the branch, what changed
    since the session started, and NEXT_ACTION from the oracle. It cannot carry a
    wrong date or a stale "next". What it cannot carry either is the author's
    own words - those live where they were said: runs/chNN/interview.md, and the
    resolution text on each inbox item.

USAGE
    python3 scripts/session_log.py            # append an entry if anything changed
    python3 scripts/session_log.py --force    # append regardless
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
LOG = os.path.join(REPO, "runs", "log.md")
START = os.path.join(REPO, ".claude", "state", "session-start-sha")


def sh(*args):
    try:
        return subprocess.run(args, cwd=REPO, capture_output=True, text=True, check=False).stdout.strip()
    except Exception:
        return ""


def main():
    force = "--force" in sys.argv
    clock = sh("date", "+%Y-%m-%d %H:%M")
    branch = sh("git", "symbolic-ref", "--short", "HEAD") or "(detached)"
    head = sh("git", "rev-parse", "--short", "HEAD")
    start = open(START).read().strip() if os.path.isfile(START) else ""
    if start and sh("git", "cat-file", "-e", start) == "" and sh("git", "merge-base", "--is-ancestor", start, "HEAD") == "":
        changed = sh("git", "diff", "--name-only", f"{start}..HEAD")
        commits = sh("git", "rev-list", "--count", f"{start}..HEAD")
    else:
        changed = sh("git", "diff", "--name-only", "HEAD~1..HEAD")
        commits = "?"
    files = [f for f in changed.split("\n") if f]
    if not files and not force:
        return 0

    nxt = sh(sys.executable, os.path.join(HERE, "next.py"))
    next_line = next((l.replace("NEXT_ACTION:", "").strip() for l in nxt.split("\n") if l.startswith("NEXT_ACTION:")), "?")
    why = ""
    lines = nxt.split("\n")
    for i, l in enumerate(lines):
        if l.startswith("NEXT_ACTION:") and i + 1 < len(lines):
            why = lines[i + 1].strip()

    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    new = not os.path.isfile(LOG)
    with open(LOG, "a", encoding="utf-8") as fh:
        if new:
            fh.write("# Session log\n\nAppended by the Stop hook. Every line is read from git or the oracle; "
                     "nothing here is typed by hand, so nothing here can carry a wrong date or a stale next.\n")
        fh.write(f"\n## {clock} — `{branch}` @ `{head}` — {commits} commit(s) this session\n")
        for f in files[:30]:
            fh.write(f"- `{f}`\n")
        if len(files) > 30:
            fh.write(f"- … and {len(files) - 30} more\n")
        fh.write(f"\n**Next:** `{next_line}` — {why}\n")
    print(f"session_log: appended to runs/log.md ({len(files)} file(s), next: {next_line})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
