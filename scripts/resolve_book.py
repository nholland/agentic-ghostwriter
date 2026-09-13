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
    python3 scripts/resolve_book.py --list-books # every book in the registry
    python3 scripts/resolve_book.py --book <slug> # inspect a book other than
                                                 # the manifest's active one

WHICH BOOK
    The manifest's `bookRoot` is the active book. To work another registered
    book WITHOUT writing to the book repo's manifest (the engine never does),
    pass --book <slug> or set $GW_BOOK_SLUG; every engine script reads the
    same override through inspect(), so one switch covers all of them. This is
    the engine's /book-switch: a view, not a write.

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
        p = hint if os.path.isabs(hint) else os.path.join(REPO, hint)
        out.append((f"config hint {hint!r}", os.path.abspath(p)))
    # Discovery: siblings of this repo, then siblings of its parent. The test
    # harness sets GW_NO_DISCOVERY=1 so a deliberately broken fixture cannot be
    # rescued by a real book repo that happens to sit next door.
    seen = set()
    if os.environ.get("GW_NO_DISCOVERY"):
        return out
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
        if why == "$GW_BOOK_REPO":
            # An explicit override that does not resolve must stop here. Falling
            # through to a config hint would silently point every desk at a
            # DIFFERENT book than the one the author named - the wrong-answer-
            # that-looks-fine failure this script exists to prevent.
            return None, None, tried
    return None, None, tried


def inspect(repo_root, require_okf, book_override=None):
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
    override = book_override or os.environ.get("GW_BOOK_SLUG")
    info["registry"] = sorted(manifest.get("books", {}).keys())
    if override:
        hits = [k for k in manifest.get("books", {}) if k == override or k.endswith("/" + override)]
        if len(hits) != 1:
            problems.append(f"--book {override!r} matches {len(hits)} registry entries "
                            f"(have: {', '.join(info['registry']) or 'none'})")
            return {"problems": problems, "info": info}
        rel = hits[0]
        info["bookOverride"] = override
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
    ap.add_argument("--book", help="registry slug to inspect instead of the active bookRoot (a view, not a write)")
    ap.add_argument("--list-books", action="store_true", help="list every book in the book repo's registry")
    a = ap.parse_args()

    cfg = load_config()
    repo_root, why, tried = resolve(cfg)

    if not repo_root:
        out = {"found": False, "tried": tried}
        if a.json:
            print(json.dumps(out, indent=2))
        else:
            print("resolve_book: NO BOOK REPO FOUND.\n")
            if tried and tried[0]["source"] == "$GW_BOOK_REPO":
                print(f"$GW_BOOK_REPO is set to {tried[0]['path']!r} and it is not a book repo. "
                      "An explicit override is never silently replaced by a guess - fix or unset it.\n")
            print("A directory containing book-manifest.json is required. Tried:")
            for t in tried[:14]:
                print(f"  [{'x' if not t['is_book_repo'] else 'ok'}] {t['path']}   ({t['source']})")
            if len(tried) > 14:
                print(f"  ... and {len(tried)-14} more")
            print("\nFix by either:")
            print("  export GW_BOOK_REPO=/path/to/Playground-260420")
            print("  or add the path to 'bookRepoCandidates' in config/house.json")
            print("\nNo desk may run without this. A missing voice spec does not")
            print("raise an error, it produces generic prose.")
        return 2

    if a.list_books:
        manifest = json.load(open(os.path.join(repo_root, "book-manifest.json"), encoding="utf-8"))
        active = manifest.get("bookRoot")
        rows = []
        for key, b in sorted(manifest.get("books", {}).items()):
            chapters = (b.get("stages") or {}).get("chapters") or {}
            refined = sum(1 for k, v in chapters.items() if k.isdigit() and v.get("refined") == "complete")
            rows.append({"key": key, "slug": b.get("slug"), "title": b.get("title"), "active": key == active,
                         "chapter_count": b.get("chapter_count"), "refined": refined,
                         "lastModified": b.get("lastModified")})
        if a.json:
            print(json.dumps(rows, indent=2))
        else:
            print(f"resolve_book: {len(rows)} book(s) registered in {repo_root}/book-manifest.json")
            for r in rows:
                mark = "*" if r["active"] else " "
                print(f"  {mark} {r['slug'] or r['key']:<28} {r['refined']}/{r['chapter_count'] or '?'} refined  "
                      f"{r['title'] or ''}")
            print("  (* = active bookRoot; use --book <slug> or $GW_BOOK_SLUG to view another without switching it)")
        return 0

    rep = inspect(repo_root, a.require_okf, a.book)
    out = {"found": True, "bookRepo": repo_root, "resolvedVia": why, **rep}

    if a.json:
        print(json.dumps(out, indent=2))
    else:
        i = rep["info"]
        print(f"resolve_book: book repo at {repo_root}")
        print(f"  resolved via: {why}")
        if i.get("bookOverride"):
            print(f"  viewing     : {i['bookOverride']} (override; the manifest's active book is unchanged)")
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
