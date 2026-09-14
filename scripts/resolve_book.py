#!/usr/bin/env python3
"""
resolve_book.py - find the book repo at runtime, or fail loudly.

WHY THIS EXISTS
    The first version of config/house.json hardcoded
    "../Playground-260420/books/the-stoic-husband". That resolved only because
    both repos happened to be cloned as siblings with those exact names in one
    particular session. On another machine, or a session that attaches them
    differently, it would have resolved to nothing - and a skill reading a
    missing voice spec does not crash, it just writes generic prose. A silent
    wrong answer, which is the failure mode this whole repo is built against.

    So the path is discovered and VALIDATED, never assumed, and this script
    exits non-zero with a readable reason rather than letting a desk run blind.

RESOLUTION ORDER (first hit wins)
    1. $GW_BOOK_REPO                      explicit override
    2. config/house.json "bookRepoCandidates"   ordered hints
    3. discovery: walk up from this repo and scan siblings for a directory
       containing book-manifest.json

USAGE
    python3 scripts/resolve_book.py              # human-readable
    python3 scripts/resolve_book.py --json       # for a skill to parse
    python3 scripts/resolve_book.py --require-okf

EXIT CODES
    0  book repo found and every required artifact present
    1  found, but something required is missing (it says what)
    2  no book repo found at all
"""

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
CONFIG = os.path.join(REPO, "config", "house.json")

REQUIRED_BOOK_FILES = ["01-voice.md", "00-premise.md", "03-outline.md"]
OPTIONAL_BOOK_FILES = ["02-audience.md", "04-archetype.md", "05-framework.md",
                       "06-sources.md", "progress.md", "parking-lot.md"]


def load_config():
    try:
        with open(CONFIG, encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return {}


def is_book_repo(path):
    return os.path.isfile(os.path.join(path, "book-manifest.json"))


def candidates(cfg):
    out = []
    env = os.environ.get("GW_BOOK_REPO")
    if env:
        out.append(("$GW_BOOK_REPO", os.path.abspath(os.path.expanduser(env))))
    for hint in cfg.get("bookRepoCandidates", []):
        # expanduser BEFORE the isabs test: '~/x' is not an absolute path, so
        # without this it silently joins to the repo root and prints as
        # '/home/user/agentic-ghostwriter/~/x' - a candidate that can never match.
        h = os.path.expanduser(hint)
        p = h if os.path.isabs(h) else os.path.join(REPO, h)
        out.append((f"config hint {hint!r}", os.path.abspath(p)))
    # Discovery: siblings of this repo, then siblings of its parent.
    seen = set()
    for base in (os.path.dirname(REPO), os.path.dirname(os.path.dirname(REPO))):
        if not os.path.isdir(base) or base in seen:
            continue
        seen.add(base)
        try:
            entries = sorted(os.listdir(base))
        except OSError:
            continue
        for name in entries:
            p = os.path.join(base, name)
            if p == REPO or not os.path.isdir(p):
                continue
            out.append((f"discovered in {base}", p))
    return out


def resolve(cfg):
    tried = []
    for why, path in candidates(cfg):
        tried.append({"source": why, "path": path, "is_book_repo": is_book_repo(path)})
        if is_book_repo(path):
            return path, why, tried
    return None, None, tried


def inspect(repo_root, require_okf):
    """Read book-manifest.json for the ACTIVE bookRoot rather than guessing a
    slug. The manifest is the registry; a hardcoded slug goes stale the moment a
    second book is sparked."""
    problems, info = [], {}
    mpath = os.path.join(repo_root, "book-manifest.json")
    try:
        with open(mpath, encoding="utf-8") as fh:
            manifest = json.load(fh)
    except Exception as exc:
        return {"problems": [f"cannot read {mpath}: {exc}"], "info": info}

    rel = manifest.get("bookRoot")
    if not rel:
        problems.append(f"{mpath} has no 'bookRoot' key")
        return {"problems": problems, "info": info}

    book_root = os.path.join(repo_root, rel)
    info["bookRootRelative"] = rel
    info["bookRoot"] = book_root
    info["title"] = (manifest.get("books", {}).get(rel, {}) or {}).get("title")
    info["chapter_count"] = (manifest.get("books", {}).get(rel, {}) or {}).get("chapter_count")

    if not os.path.isdir(book_root):
        problems.append(f"bookRoot {rel!r} does not exist under {repo_root}")
        return {"problems": problems, "info": info}

    for f in REQUIRED_BOOK_FILES:
        if not os.path.isfile(os.path.join(book_root, f)):
            problems.append(f"REQUIRED missing: {rel}/{f}")
    info["optional_present"] = [
        f for f in OPTIONAL_BOOK_FILES
        if os.path.isfile(os.path.join(book_root, f))
    ]

    okf = os.path.join(book_root, "okf")
    info["okf"] = okf
    info["okf_present"] = os.path.isdir(okf)
    if info["okf_present"]:
        n = sum(len([x for x in files if x.endswith(".md")])
                for _, _, files in os.walk(okf))
        info["okf_concepts"] = n
    elif require_okf:
        problems.append(f"REQUIRED missing: {rel}/okf/ (--require-okf)")

    # Every book-repo file this engine calls, checked by name. These are declared
    # in config/house.json rather than scattered through skill prose so the
    # coupling is auditable in one place - and so a missing one surfaces at
    # session start instead of halfway through a chapter.
    cfg = load_config()
    deps = cfg.get("book_repo_dependencies", {})
    info["dependencies"] = {"required": {}, "optional": {}}
    for kind in ("required", "optional"):
        for rel, why in (deps.get(kind) or {}).items():
            if rel.startswith("_"):
                continue
            full = os.path.join(repo_root, rel)
            present = os.path.isfile(full)
            info["dependencies"][kind][rel] = {"present": present, "why": why}
            if not present and kind == "required":
                problems.append(f"REQUIRED book-repo dependency missing: {rel} - {why}")

    validator = os.path.join(repo_root, "scripts", "okf_validate.py")
    info["okf_validate"] = validator if os.path.isfile(validator) else None

    chapters = os.path.join(book_root, "chapters")
    info["chapters"] = chapters
    if os.path.isdir(chapters):
        info["refined_chapters"] = sorted(
            d for d in os.listdir(chapters)
            if os.path.isfile(os.path.join(chapters, d, "refined.md"))
        )
    return {"problems": problems, "info": info}


def main():
    ap = argparse.ArgumentParser(description="Resolve and validate the book repo.")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--require-okf", action="store_true")
    a = ap.parse_args()

    cfg = load_config()
    repo_root, why, tried = resolve(cfg)

    if not repo_root:
        out = {"found": False, "tried": tried}
        if a.json:
            print(json.dumps(out, indent=2))
        else:
            print("resolve_book: NO BOOK REPO FOUND.\n")
            print("A directory containing book-manifest.json is required. Tried:")
            hints = [t for t in tried if not t["source"].startswith("discovered")]
            for t in hints:
                print(f"  [{'x' if not t['is_book_repo'] else 'ok'}] {t['path']}   ({t['source']})")
            scanned = len(tried) - len(hints)
            if scanned:
                bases = sorted({os.path.dirname(t["path"])
                                for t in tried if t["source"].startswith("discovered")})
                print(f"  [x] {scanned} sibling director{'y' if scanned == 1 else 'ies'} "
                      f"scanned under {', '.join(bases)} - none held book-manifest.json")
            print("\nFix by one of:")
            if os.environ.get("CLAUDE_CODE_REMOTE") == "true":
                # A fresh container clones only the repo the session was started
                # from. The book repo is then reachable but absent - the one case
                # neither remedy below covers, and the only one that can occur here.
                print("  the book repo is not cloned in this container. Attach it")
                print("  read-only and clone it beside this repo; discovery finds it:")
                print(f"    git clone --depth 1 <book-repo-url> {os.path.dirname(REPO)}/<name>")
            print("  export GW_BOOK_REPO=/path/to/Playground-260420")
            print("  or add the path to 'bookRepoCandidates' in config/house.json")
            print("\nNo desk may run without this. A missing voice spec does not")
            print("raise an error, it produces generic prose.")
        return 2

    rep = inspect(repo_root, a.require_okf)
    out = {"found": True, "bookRepo": repo_root, "resolvedVia": why, **rep}

    if a.json:
        print(json.dumps(out, indent=2))
    else:
        i = rep["info"]
        print(f"resolve_book: book repo at {repo_root}")
        print(f"  resolved via: {why}")
        if i.get("title"):
            print(f"  active book : {i['title']}")
        if i.get("bookRoot"):
            print(f"  bookRoot    : {i['bookRoot']}")
        if i.get("chapter_count"):
            print(f"  chapters    : {i['chapter_count']} planned, "
                  f"{len(i.get('refined_chapters', []))} refined")
        if i.get("okf_present"):
            print(f"  okf         : {i.get('okf_concepts')} concepts at {i['okf']}")
        else:
            print("  okf         : ABSENT")
        deps = i.get("dependencies", {})
        req, opt = deps.get("required", {}), deps.get("optional", {})
        if req or opt:
            miss_r = [k for k, v in req.items() if not v["present"]]
            miss_o = [k for k, v in opt.items() if not v["present"]]
            print(f"  book-repo deps: {len(req) - len(miss_r)}/{len(req)} required, "
                  f"{len(opt) - len(miss_o)}/{len(opt)} optional present")
            for k in miss_r:
                print(f"    MISSING (required) {k}")
            for k in miss_o:
                print(f"    missing (optional) {k} - the feature it serves is unavailable")
        if i.get("optional_present"):
            print(f"  also present: {', '.join(i['optional_present'])}")
        if rep["problems"]:
            print("\n  PROBLEMS (a desk must not run past these):")
            for p in rep["problems"]:
                print(f"    - {p}")
        else:
            print("\n  all required artifacts present")
    return 1 if rep["problems"] else 0


if __name__ == "__main__":
    sys.exit(main())
