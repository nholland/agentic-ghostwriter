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
    auto-commit. Overwrites --file with its content at --at, runs the
    worktree's own tests/run.py, confirms --case prints [FAIL]. Restores
    --file to the worktree's checked-out (current) version, runs again,
    confirms --case prints [ ok ]. Removes the worktree either way.

USAGE
    python3 tests/prove.py --file scripts/session_log.py --at c17f979 \
        --case "session_log dedups when the last entry itself lists runs/log.md"

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
