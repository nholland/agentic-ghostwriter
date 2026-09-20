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
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
LOG = os.path.join(REPO, "runs", "log.md")
START = os.path.join(REPO, ".claude", "state", "session-start-sha")


def last_entry_files():
    """The file list of the most recent '## ...' block in runs/log.md, or None
    if the log doesn't exist yet or has no entry.

    The diff this script logs is cumulative (session-start-sha..HEAD), not
    incremental, so a Stop with no new work commit since the last entry
    reproduces the same list verbatim - the retro dispatch forces exactly
    this second Stop every time it fires. 39 of 117 entries were this exact
    duplicate before this existed."""
    if not os.path.isfile(LOG):
        return None
    text = open(LOG, encoding="utf-8").read()
    blocks = text.split("\n## ")
    if len(blocks) < 2:
        return None
    last = blocks[-1]
    listed = set(re.findall(r"^- `([^`]+)`$", last, re.MULTILINE)) - {"runs/log.md"}
    m = re.search(r"^- … and (\d+) more$", last, re.MULTILINE)
    return listed, len(listed) + (int(m.group(1)) if m else 0)


def sh(*args):
    try:
        return subprocess.run(args, cwd=REPO, capture_output=True, text=True, check=False).stdout.strip()
    except Exception:
        return ""


def main():
    force = "--force" in sys.argv
    clock = sh("date", "+%Y-%m-%d %H:%M")
    branch = sh("git", "symbolic-ref", "--short", "HEAD") or "(detached)"
    start = open(START).read().strip() if os.path.isfile(START) else ""
    if start and sh("git", "cat-file", "-e", start) == "" and sh("git", "merge-base", "--is-ancestor", start, "HEAD") == "":
        changed = sh("git", "diff", "--name-only", f"{start}..HEAD")
        commits = sh("git", "rev-list", "--count", f"{start}..HEAD")
    else:
        changed = sh("git", "diff", "--name-only", "HEAD~1..HEAD")
        commits = "?"
    files = [f for f in changed.split("\n") if f]
    # An entry recording nothing but its own write is noise. Two such entries were
    # produced on 2026-09-14 before this guard existed.
    if files == ["runs/log.md"] and not force:
        print("session_log: nothing but runs/log.md changed - no entry written")
        return 0
    # Drop the log's own name once, here, so every line below sees the same
    # list. It used to be stripped in two places and left in a third - the
    # entry listed it, the current set removed it, and the stored overflow
    # count still counted it - which is why prefix comparison alone could
    # never match once the log became tracked. One filter, no asymmetry, and
    # "this session changed runs/log.md" was never information anyway.
    files = [f for f in files if f != "runs/log.md"]
    if not files and not force:
        return 0
    # The diff is cumulative from session start, so a Stop with no new work
    # commit since the last entry reproduces the same file set verbatim - most
    # often the retro dispatch's forced second Stop. Skip the restatement.
    # Compare what the entry actually STORES - its first-30 list and its
    # overflow count - not the whole diff. An entry writes files[:30], so on any
    # session touching more than 30 files the full set could never equal what
    # last_entry_files() reads back, and dedup was dead exactly when a session
    # was big enough to matter: five restatements on 2026-09-19. Third miss in
    # this lineage (#035, #039, #040), the same cause each time - the fixture
    # never reached the real sequence, here because it never crossed 30 files.
    #
    # The overflow count is half the comparison, not decoration. Comparing the
    # prefix alone silently swaps one bug for a worse one: work whose new files
    # all sort past the 30th would read as "same file set" and a real session's
    # entry would be dropped. A duplicate entry is noise; a missing one is a
    # lost record. Caught by the fixture below on its first run.
    this_sig = (set(files[:30]), len(files))
    if not force and this_sig[0] and this_sig == last_entry_files():
        print("session_log: same file set as the last entry - no entry written")
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
        # No SHA. It was the only field here that could stop resolving: 13 of 23
        # recorded SHAs were already dead by 2026-09-14, orphaned by the amends
        # this container's identity check forces, and nothing ever parsed one.
        # FLOW.md's enumeration of this format never listed it either.
        fh.write(f"\n## {clock} — `{branch}` — {commits} commit(s) this session\n")
        for f in files[:30]:
            fh.write(f"- `{f}`\n")
        if len(files) > 30:
            fh.write(f"- … and {len(files) - 30} more\n")
        fh.write(f"\n**Next:** `{next_line}` — {why}\n")
    print(f"session_log: appended to runs/log.md ({len(files)} file(s), next: {next_line})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
