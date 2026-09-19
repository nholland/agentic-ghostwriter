#!/usr/bin/env python3
"""
prove.py - mechanically prove a fixture case discriminates: red against the
named file's content at a prior commit, green against the current tree.

WHY THIS EXISTS
    inbox.py --add used to accept a typed "[FAIL]" substring in --evidence as
    proof a case was watched fail first. That is an attestation, not a
    measurement - an item whose evidence read "I did not run anything.
    [FAIL] is a string I typed." was accepted, exit 0 (found 2026-09-19,
    reviewing #041 - the guard meant to stop unproven proofs was itself
    unproven). This runs the red pass instead of trusting a claim about it.

WHAT THIS DOES
    Creates a throwaway git worktree - never the live tree, since reverting a
    tracked file in place during --add would race the Stop hook's own
    auto-commit. `git worktree add` checks out HEAD, which is blind to
    uncommitted work - the exact state a case new this session is usually in
    when someone is about to file the item proving it. So immediately after
    creating the worktree, every path `git status --porcelain` reports as
    modified or untracked in the live tree is copied in over the checkout
    (deleted paths are removed), which is what makes "the current tree" in
    this file's claims actually mean the live tree, not just HEAD (found
    2026-09-19: without this, a case that only existed uncommitted was
    REFUSED as "missing", and the only triples that could ever pass were
    older committed ones - unrelated to whatever the item being filed was
    actually about). Then overwrites --file with its content at --at, runs
    the worktree's own tests/run.py, confirms --case prints [FAIL]. Restores
    --file to the synced current version, runs again, confirms --case prints
    [ ok ]. Removes the worktree either way.

USAGE
    python3 tests/prove.py --file <path changed by the fix> --at <commit before the fix> \
        --case "<exact fixture case name the fix's own commit added or changed>"

    Not a copy-pasteable example - see WHAT THIS DOES NOT DO.

WHAT THIS DOES NOT DO
    It measures that --case genuinely goes [FAIL] at --at and [ ok ] now. It
    does NOT measure that --case has anything to do with the item being filed.
    Binding a fixture case to an English proposal is a semantic judgment, not
    a mechanical one, and this file cannot make it. inbox.py --add adds one
    guard on top (refusing a --prove-case already present in tests/run.py at
    this session's review-window start), which closes the failure that
    actually happened by accident (#042 reused a stale case unknowingly). It
    does not close, and no further layer here should try to close, these
    (all measured live, 2026-09-19, after that guard landed):

    - Renaming an older, unrelated, genuinely-discriminating case's string by
      a few words makes it "new" to the window-start check while it still
      discriminates against its own old, unrelated commit.
    - Reusing a case THIS window itself already added, verbatim - the guard
      only excludes cases older than the window start, and everything the
      window has added so far is fair game until the pointer next moves.
    - An unreadable window state (retro-window/retro-last-sha/session-start-
      sha all absent, or pointing at a commit tests/run.py can't be read
      from) used to skip the check with no output at all - inbox.py now
      prints a NOTE when this happens, which does not close the hole, only
      stops it from passing in silence.
    - A dirty path with a git-quoted name (non-ASCII, an embedded quote) is
      silently skipped by sync_dirty's plain-string unquoting instead of
      copied - latent, since this repo is all-ASCII today.

    Found and reasoned through 2026-09-19, reviewing the window-start guard
    that closed the exact "mascot" attack that broke #042: every proposed
    tightening has its own bypass, discoverable in about ten minutes, because
    the underlying problem - "is this proof about this proposal" - cannot be
    decided by a script reading strings. The house's own prior conclusion on
    a differently-shaped recurrence applies unchanged: "no amount of rule
    text will fix this... recording this plainly so a fifth occurrence is not
    met with a fifth proposed clause" (LEARNINGS.md). This is that note for
    this lineage. An eighth guard is not the answer; noticing the pattern is.

EXIT
    0  PROVED - case is [FAIL] at --at, [ ok ] on the current tree.
    2  REFUSED - case did not fail at --at, or did not pass on the current
       tree, or was not found in tests/run.py's output at all.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)


def sh(*args, cwd=None, check=True):
    return subprocess.run(args, cwd=cwd or REPO, capture_output=True, text=True, check=check)


def sync_dirty(worktree):
    """Copy every uncommitted change in the live tree into the worktree, which
    `git worktree add` checks out at HEAD and so never sees on its own."""
    status = sh("git", "status", "--porcelain", "-uall").stdout
    for line in status.splitlines():
        if not line.strip():
            continue
        code, path = line[:2], line[3:]
        if " -> " in path:  # a rename or copy: only the destination matters here
            path = path.split(" -> ", 1)[1]
        path = path.strip('"')
        src = os.path.join(REPO, path)
        dst = os.path.join(worktree, path)
        if code.strip().startswith("D") or not os.path.isfile(src):
            if os.path.isfile(dst):
                os.remove(dst)
            continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)


def run_case(worktree, case):
    r = subprocess.run([sys.executable, os.path.join(worktree, "tests", "run.py")],
                       cwd=worktree, capture_output=True, text=True)
    if re.search(rf"^\[ ok \] {re.escape(case)}$", r.stdout, re.MULTILINE):
        return "ok"
    if re.search(rf"^\[FAIL\] {re.escape(case)}$", r.stdout, re.MULTILINE):
        return "fail"
    return "missing"


def main():
    ap = argparse.ArgumentParser(description="Mechanically prove a fixture case discriminates.")
    ap.add_argument("--file", required=True, help="repo-relative path the proposal changed")
    ap.add_argument("--at", required=True, help="commit before the fix")
    ap.add_argument("--case", required=True, help="exact fixture case name, as tests/run.py prints it")
    a = ap.parse_args()

    base = tempfile.mkdtemp(prefix="gw-prove-")
    wt = os.path.join(base, "wt")
    try:
        sh("git", "worktree", "add", "--detach", "--quiet", wt, "HEAD")
        sync_dirty(wt)

        old_content = sh("git", "show", f"{a.at}:{a.file}").stdout
        target = os.path.join(wt, a.file)
        current_content = open(target, encoding="utf-8").read()

        open(target, "w", encoding="utf-8").write(old_content)
        status_red = run_case(wt, a.case)
        open(target, "w", encoding="utf-8").write(current_content)

        if status_red == "missing":
            print(f"prove: REFUSED - case '{a.case}' not found in tests/run.py's output")
            return 2
        if status_red != "fail":
            print(f"prove: REFUSED - case is [{status_red}] against {a.file}@{a.at}, not FAIL")
            return 2

        status_green = run_case(wt, a.case)
        if status_green != "ok":
            print(f"prove: REFUSED - case is [{status_green}] on the current tree, expected [ ok ]")
            return 2

        print(f"prove: PROVED - '{a.case}' red={a.file}@{a.at} then green on the current tree")
        return 0
    finally:
        sh("git", "worktree", "remove", "--force", wt, check=False)
        shutil.rmtree(base, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
