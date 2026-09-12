#!/usr/bin/env python3
"""
sync_plugin_layout.py - mirror .claude/ into the plugin-root layout.

WHY BOTH LAYOUTS EXIST
    Claude Code loads desks from two different places depending on how this repo
    arrives:

      attached repo / project   ->  .claude/skills/, .claude/agents/   (+ CLAUDE.md)
      plugin (--plugin-dir)     ->  skills/, agents/ at the REPO ROOT

    The author's sessions are cloud sessions where the repo is attached, so
    `.claude/` is canonical and is the only copy anyone should edit. The root
    copies exist so `--plugin-dir` and marketplace distribution also work.

WHY A SCRIPT AND NOT A MANUAL COPY
    A second copy of a rule with nothing keeping the copies equal is exactly the
    citation-manifest.md failure: it described itself as derived, nothing derived
    it, and it drifted until its own queue read "None at this time" while seven
    concepts were waiting. Any file that calls itself derived must have a script
    deriving it, and any check that calls itself enforcement must have a caller.
    So: this script derives, and --check is run before every commit.

USAGE
    python3 scripts/sync_plugin_layout.py           # derive root/ from .claude/
    python3 scripts/sync_plugin_layout.py --check   # exit 1 if out of sync

EXIT CODES
    0  in sync (or synced successfully)
    1  --check found drift
"""

import argparse
import filecmp
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
PAIRS = [(".claude/skills", "skills"), (".claude/agents", "agents")]

BANNER = (
    "<!-- DERIVED FILE - DO NOT EDIT.\n"
    "     Canonical copy: {src}\n"
    "     Regenerate: python3 scripts/sync_plugin_layout.py -->\n"
)


def insert_banner(body, src_rel):
    """Place the banner AFTER the frontmatter block.

    Putting it first means the frontmatter is no longer at the top of the file,
    Claude Code stops reading `description`, and the skill loads without the
    metadata that makes it findable. `claude plugin validate` caught this on the
    first run of this script - which is the argument for running the validator
    rather than trusting that a mirror is a mirror.
    """
    banner = BANNER.format(src=src_rel)
    if body.startswith("---\n"):
        end = body.find("\n---\n", 3)
        if end != -1:
            cut = end + len("\n---\n")
            return body[:cut] + "\n" + banner + body[cut:].lstrip("\n")
    return banner + body


def walk(root):
    out = {}
    if not os.path.isdir(root):
        return out
    for base, _, files in os.walk(root):
        for f in files:
            if f.endswith(".pyc"):
                continue
            full = os.path.join(base, f)
            out[os.path.relpath(full, root)] = full
    return out


def check():
    drift = list(check_hooks())
    for src_rel, dst_rel in PAIRS:
        src, dst = os.path.join(REPO, src_rel), os.path.join(REPO, dst_rel)
        s, d = walk(src), walk(dst)
        for rel in sorted(set(s) | set(d)):
            if rel not in s:
                drift.append(f"{dst_rel}/{rel} exists but {src_rel}/{rel} does not (stale)")
            elif rel not in d:
                drift.append(f"{src_rel}/{rel} is not mirrored into {dst_rel}/")
            else:
                # Compare ignoring the derived banner.
                a = open(s[rel], encoding="utf-8").read()
                b = open(d[rel], encoding="utf-8").read()
                b_stripped = b.replace(BANNER.format(src=f"{src_rel}/{rel}"), "")
                if a.split() != b_stripped.split():
                    drift.append(f"{dst_rel}/{rel} differs from {src_rel}/{rel}")
    return drift


def sync_hooks():
    """hooks/hooks.json is derived from .claude/settings.json. The docs say the
    two formats are identical, so this is a straight extraction of the "hooks"
    key - one canonical copy, one derived, same as the skills and agents."""
    import json
    src = os.path.join(REPO, ".claude", "settings.json")
    dst = os.path.join(REPO, "hooks", "hooks.json")
    if not os.path.isfile(src):
        return 0
    with open(src, encoding="utf-8") as fh:
        settings = json.load(fh)
    hooks = settings.get("hooks")
    if not hooks:
        return 0
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w", encoding="utf-8") as fh:
        json.dump({"_derived_from": ".claude/settings.json - do not edit; run scripts/sync_plugin_layout.py",
                   "hooks": hooks}, fh, indent=2)
        fh.write("\n")
    return 1


def check_hooks():
    import json
    src = os.path.join(REPO, ".claude", "settings.json")
    dst = os.path.join(REPO, "hooks", "hooks.json")
    if not os.path.isfile(src):
        return []
    if not os.path.isfile(dst):
        return ["hooks/hooks.json missing - derive it from .claude/settings.json"]
    a = json.load(open(src, encoding="utf-8")).get("hooks")
    b = json.load(open(dst, encoding="utf-8")).get("hooks")
    return [] if a == b else ["hooks/hooks.json differs from .claude/settings.json hooks"]


def sync():
    n = sync_hooks()
    for src_rel, dst_rel in PAIRS:
        src, dst = os.path.join(REPO, src_rel), os.path.join(REPO, dst_rel)
        if not os.path.isdir(src):
            continue
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        for rel, full in sorted(walk(src).items()):
            out = os.path.join(dst, rel)
            os.makedirs(os.path.dirname(out), exist_ok=True)
            body = open(full, encoding="utf-8").read()
            with open(out, "w", encoding="utf-8") as fh:
                fh.write(insert_banner(body, f"{src_rel}/{rel}"))
            n += 1
    return n


def main():
    ap = argparse.ArgumentParser(description="Mirror .claude/ into the plugin layout.")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    if a.check:
        drift = check()
        if drift:
            print("sync_plugin_layout: OUT OF SYNC")
            for d in drift:
                print(f"  - {d}")
            print("\nFix: python3 scripts/sync_plugin_layout.py")
            print("Edit only the .claude/ copies; the root copies are derived.")
            return 1
        print("sync_plugin_layout: in sync")
        return 0

    n = sync()
    print(f"sync_plugin_layout: derived {n} file(s) into skills/ and agents/")
    print("  .claude/ is canonical. Never edit the root copies.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
