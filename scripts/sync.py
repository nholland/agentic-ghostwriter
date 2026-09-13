#!/usr/bin/env python3
"""
sync.py - the git mechanics, done the same way every time, and named out loud.

WHY A SCRIPT AND NOT A DESK
    The book repo's git-sync procedure was copied into twenty skill files and
    eighteen copies were wrong. A session ran from a clone 13 commits behind main
    and bypassed the freshness guard by hand. The confusion the author actually
    reported was simpler than either: not knowing whether "pushed" meant the
    session branch or main. A model following instructions produced all three.
    This script produces none of them.

RULES IT ENFORCES
    - It always says WHICH BRANCH. "Pushed" alone is the ambiguity.
    - It never force-pushes, never rewrites history, never touches a branch it
      is not on.
    - --land is the only thing that moves main, and it is fast-forward only. If
      the session branch has diverged, it refuses and says how to merge main in.
    - It does not decide WHEN to land. The author says "land it"; the Publisher
      runs this. That is the book repo's fallback policy, kept on purpose.

USAGE
    python3 scripts/sync.py --status        # branch, ahead/behind main, uncommitted, unpushed
    python3 scripts/sync.py --push          # push the current branch (after the Stop hook committed)
    python3 scripts/sync.py --merge-main    # bring origin/main into this branch (reports conflicts)
    python3 scripts/sync.py --land          # ff-only merge this branch into main, push main

EXIT CODES
    0 ok · 1 refused (says why) · 2 not a git repo / no remote
"""

import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)


def run(*args, check=False):
    p = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True)
    if check and p.returncode != 0:
        raise RuntimeError(p.stderr.strip() or p.stdout.strip())
    return p.returncode, p.stdout.strip(), p.stderr.strip()


def ensure_tracking():
    """A repo cloned while EMPTY has no remote.origin.fetch refspec, so no fetch
    ever creates refs/remotes/origin/*, and every ahead/behind comparison against
    origin/main errors. The first version of this script turned that error into
    "0 ahead, 0 behind" - a false zero with no error, in the one script whose job
    is to remove ambiguity. Write the standard refspec if it is missing, then fetch."""
    rc, spec, _ = run("config", "--get", "remote.origin.fetch")
    if rc != 0 or not spec:
        run("config", "remote.origin.fetch", "+refs/heads/*:refs/remotes/origin/*")
    run("fetch", "origin", "--quiet")


def count(rev_range):
    """An int, or None when git could not compare. None is rendered as 'unknown',
    never as 0."""
    rc, out, _ = run("rev-list", "--count", rev_range)
    return int(out) if rc == 0 and out.isdigit() else None


def status():
    rc, branch, _ = run("symbolic-ref", "--short", "HEAD")
    if rc != 0:
        return None
    ensure_tracking()
    has_main = run("rev-parse", "--verify", "--quiet", "origin/main")[0] == 0
    has_up = run("rev-parse", "--verify", "--quiet", f"origin/{branch}")[0] == 0
    _, dirty, _ = run("status", "--porcelain")
    return {
        "branch": branch,
        "has_origin_main": has_main,
        "behind_main": count(f"{branch}..origin/main") if has_main else None,
        "ahead_of_main": count(f"origin/main..{branch}") if has_main else None,
        "unpushed": count(f"origin/{branch}..{branch}") if has_up else None,
        "branch_on_origin": has_up,
        "uncommitted": len([l for l in dirty.split("\n") if l.strip()]),
    }


def fmt(n, none="unknown"):
    return none if n is None else str(n)


def say_status(s):
    print(f"branch          : {s['branch']}")
    if s["has_origin_main"]:
        print(f"vs origin/main  : {fmt(s['ahead_of_main'])} ahead, {fmt(s['behind_main'])} behind")
    else:
        print("vs origin/main  : UNKNOWN - origin/main could not be fetched. Do not trust any 'ahead/behind' until it can.")
    if s["branch_on_origin"]:
        print(f"unpushed commits: {fmt(s['unpushed'])}")
    else:
        print(f"unpushed commits: branch '{s['branch']}' is not on origin yet (nothing of it is pushed)")
    print(f"uncommitted     : {s['uncommitted']} file(s)")
    if s["branch"] == "main":
        print("\n  You are ON main. The SessionStart hook moves a remote session onto a "
              "session/ branch; here you are not on one. Work on main is not wrong, "
              "but nothing will ask before it is pushed there.")
    elif s["behind_main"] and s["ahead_of_main"]:
        print("\n  DIVERGED. --land will refuse. Run --merge-main first.")
    elif s["ahead_of_main"] is None:
        pass
    elif s["ahead_of_main"]:
        print(f"\n  {s['ahead_of_main']} commit(s) on '{s['branch']}' are not on main. "
              f"They land only when the author says so: --land")


def push(s):
    if s["uncommitted"]:
        print(f"sync: refusing to push with {s['uncommitted']} uncommitted file(s). "
              f"The Stop hook commits work paths; rule files you commit deliberately.")
        return 1
    rc, out, err = run("push", "-u", "origin", s["branch"])
    if rc != 0:
        print(f"sync: push FAILED to '{s['branch']}':\n{err}")
        return 1
    print(f"Pushed to `{s['branch']}`" + ("" if s['branch'] == "main" else " (not main)")
          + f". {fmt(s['ahead_of_main'])} commit(s) ahead of main.")
    return 0


def merge_main(s):
    if s["uncommitted"]:
        print("sync: refusing to merge with uncommitted changes."); return 1
    rc, out, err = run("merge", "origin/main", "--no-edit")
    if rc != 0:
        _, conflicts, _ = run("diff", "--name-only", "--diff-filter=U")
        print("sync: merge of origin/main has CONFLICTS in:\n  " + conflicts.replace("\n", "\n  "))
        print("\n  Resolve them, commit, then --land. If both sides changed the same logic and "
              "picking either loses behaviour, that is the author's call, not this script's.")
        return 1
    print(f"Merged origin/main into `{s['branch']}`. Now --land when ready.")
    return 0


def land(s):
    if s["branch"] == "main":
        print("sync: already on main; nothing to land."); return 1
    if s["uncommitted"]:
        print("sync: refusing to land with uncommitted changes."); return 1
    if s["behind_main"] is None or s["ahead_of_main"] is None:
        print("sync: refusing to land - cannot compare with origin/main (fetch failed or ref missing). "
              "A land on an unknown comparison is how main gets something it should not.")
        return 1
    if s["behind_main"]:
        print(f"sync: refusing - '{s['branch']}' is {s['behind_main']} behind main. "
              f"Fast-forward is impossible. Run --merge-main first.")
        return 1
    if not s["ahead_of_main"]:
        print(f"sync: nothing to land - '{s['branch']}' has no commits main lacks."); return 0
    if s["unpushed"] is None or s["unpushed"] > 0:
        rc, _, err = run("push", "-u", "origin", s["branch"])
        if rc != 0:
            print(f"sync: could not push '{s['branch']}' first:\n{err}"); return 1
    try:
        run("checkout", "main", check=True)
        run("merge", "--ff-only", s["branch"], check=True)
        rc, _, err = run("push", "origin", "main")
        if rc != 0:
            raise RuntimeError(err)
        _, sha, _ = run("rev-parse", "--short", "HEAD")
    except RuntimeError as exc:
        run("checkout", s["branch"])
        print(f"sync: land FAILED, back on '{s['branch']}':\n{exc}"); return 1
    run("checkout", s["branch"])
    print(f"Landed on `main` @ {sha} ({s['ahead_of_main']} commit(s), fast-forward). "
          f"Back on `{s['branch']}`, which now equals main.")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Git mechanics, the same way every time.")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--status", action="store_true")
    g.add_argument("--push", action="store_true")
    g.add_argument("--merge-main", action="store_true")
    g.add_argument("--land", action="store_true")
    a = ap.parse_args()
    s = status()
    if s is None:
        print("sync: not on a branch, or not a git repo", file=sys.stderr); return 2
    if a.status:
        say_status(s); return 0
    if a.push:
        return push(s)
    if a.merge_main:
        return merge_main(s)
    if a.land:
        return land(s)


if __name__ == "__main__":
    sys.exit(main())
