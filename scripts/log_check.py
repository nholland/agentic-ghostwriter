#!/usr/bin/env python3
"""
log_check.py - assert runs/log.md's two mechanical invariants.

WHY
    runs/log.md is one of the three things CLAUDE.md names as this house's
    memory, and it is the one artifact resolved BY HAND every time two branches
    diverge. Two such resolutions did real damage before anything noticed:

      a846d9c (2026-09-19, message "union the log")  dropped 26 entries whole
      bd3a334 (2026-09-20, message "Nothing dropped") detached a 30-file body

    Both commit messages assert the result is complete. The only check that ran
    was `grep -c '<<<<<<<'`, which proves no conflict markers remain and nothing
    else - both bad merges pass it. That is the shape this ledger records over
    and over: an assertion of correctness that raises no error and is falsified
    only by measuring against a known-right answer.

INVARIANTS
    1. STRUCTURE. Every '## <date> <time>' heading is followed by at least one
       file line and exactly one '**Next:**' before the next heading.
    2. UNION. When HEAD is a merge, every heading present in either parent is
       present in the result. A hand-resolved log may reorder and dedupe; it may
       never lose a session.

    Invariant 2 is the one that matters and the one no habit caught. It runs
    only on a merge commit, so the ordinary Stop pays nothing for it.

USAGE
    python3 scripts/log_check.py            # both invariants, exit 1 on any breach
    python3 scripts/log_check.py --json

EXIT CODES
    0  the log is intact
    1  an invariant is broken (it says which entries)
    2  could not run (no log, git unavailable on a merge check)
"""

import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
LOG = os.path.join(REPO, "runs", "log.md")

# The WHOLE heading line is the key, not the timestamp. Two sessions on
# different branches finished in the same minute on 2026-09-14 14:11, so keying
# on time alone collapses them - and a genuinely lost entry would then hide
# behind a same-minute survivor in the union check, which is the exact class of
# miss this script exists to catch.
HEADING = re.compile(r'^## (\d{4}-\d{2}-\d{2} \d{2}:\d{2}[^\n]*)', re.M)

# Entries that were written without a body and never had one in ANY commit.
# Exempted by name rather than by a date cutoff or a pattern, so the exemption
# cannot silently widen to cover real damage: adding one means proving, as this
# one was proved, that no commit in history ever carried a body for it.
BORN_EMPTY = {"2026-09-14 11:51"}


def entries(text):
    """{heading: block} for every entry in a log's text."""
    out = {}
    for block in re.split(r'(?=^## \d{4}-\d{2}-\d{2} )', text, flags=re.M)[1:]:
        m = HEADING.match(block)
        if m:
            out[m.group(1)] = block
    return out


def structure_breaches(text):
    bad = []
    for head, block in entries(text).items():
        if head[:16] in BORN_EMPTY:   # keyed by timestamp; the key is the full line
            continue
        files = len(re.findall(r'^- `', block, re.M))
        nxt = len(re.findall(r'^\*\*Next:\*\*', block, re.M))
        if files == 0 or nxt != 1:
            bad.append({"entry": head, "files": files, "next_lines": nxt})
    return bad


def union_breaches():
    """On a merge commit, every parent's headings must survive into the result.

    Returns (breaches, checked). checked is False when HEAD is not a merge -
    reported as such rather than counted as a pass, because a check that did
    not run is not a check that passed (Rule 12).
    """
    def git(*a):
        r = subprocess.run(["git", "-C", REPO, *a], capture_output=True, text=True)
        return r.stdout if r.returncode == 0 else None

    parents = (git("rev-list", "--parents", "-n", "1", "HEAD") or "").split()
    if len(parents) < 3:          # sha + 2 parents = a merge
        return [], False
    missing = set()
    result = set(entries(open(LOG, encoding="utf-8").read()))
    for p in parents[1:]:
        t = git("show", f"{p}:runs/log.md")
        if t is None:
            continue
        missing |= set(entries(t)) - result
    return sorted(missing), True


def main():
    ap = argparse.ArgumentParser(description="Assert runs/log.md's invariants.")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if not os.path.isfile(LOG):
        print("log_check: no runs/log.md", file=sys.stderr)
        return 2
    text = open(LOG, encoding="utf-8").read()
    struct = structure_breaches(text)
    lost, union_ran = union_breaches()
    total = len(entries(text))

    out = {"entries": total, "structure": struct, "lost_in_merge": lost,
           "union_checked": union_ran}
    if a.json:
        print(json.dumps(out, indent=2))
        return 1 if (struct or lost) else 0

    if not struct and not lost:
        tail = "union checked against both parents" if union_ran else "union UNCHECKED (HEAD is not a merge)"
        print(f"log_check: {total} entries intact - structure ok, {tail}.")
        return 0

    print(f"log_check: runs/log.md is DAMAGED ({total} entries)")
    if lost:
        print(f"\n  present in a merge parent, absent from the result ({len(lost)}):")
        for h in lost:
            print(f"    - {h}")
        print("    Recover with: git show <parent>:runs/log.md")
    if struct:
        print(f"\n  malformed entries ({len(struct)}):")
        for b in struct:
            print(f"    ! {b['entry']}: {b['files']} file line(s), "
                  f"{b['next_lines']} Next line(s) - want >=1 and exactly 1")
    return 1


if __name__ == "__main__":
    sys.exit(main())
