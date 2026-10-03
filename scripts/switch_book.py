#!/usr/bin/env python3
"""
switch_book.py - list the registered books, or make another one the active book.

WHY THIS EXISTS
    book-manifest.json is the registry and its top-level "bookRoot" names the
    ACTIVE book; every script reads it through resolve_book.py. Switching books
    is therefore one value in one file - but a hand edit to that value can
    point at a folder that is not registered, or one with no voice spec, and a
    desk handed a missing voice spec does not crash, it writes generic prose.
    So the switch is validated first and written once.

USAGE
    python3 scripts/switch_book.py                  # list books, mark the active one
    python3 scripts/switch_book.py <slug|path>      # make it active
    python3 scripts/switch_book.py <slug> --manifest PATH   # fixtures only

WHAT IT CHECKS BEFORE WRITING
    - the target is a key of "books" in the manifest (slug or books/<slug>)
    - its folder exists and holds every REQUIRED_BOOK_FILES entry
    - "bookRoot" occurs exactly once in the manifest text (Rule 11: count,
      abort if the count is wrong, replace in memory, verify, write once)

WHAT IT DOES NOT DO
    It does not move config/house.json's mirrored voice thresholds. Those
    mirror ONE book's voice spec. After a switch, voice_rules_check.py fails
    until the spec and the mirror agree for the new book - which is the
    intended loud failure, not a bug. The script says so after every switch.

EXIT CODES
    0  listed, switched, or already active
    1  refused (unregistered, folder missing, spec files missing, bad manifest)
"""

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import resolve_book  # noqa: E402

ROOT_KEY = re.compile(r'("bookRoot"\s*:\s*)"([^"]*)"')


def load(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    return text, json.loads(text)


def find_target(manifest, arg):
    books = manifest.get("books", {})
    arg = arg.strip().rstrip("/")
    if arg in books:
        return arg
    for key, meta in books.items():
        if arg == (meta or {}).get("slug") or arg == os.path.basename(key):
            return key
    return None


def main():
    ap = argparse.ArgumentParser(description="List or switch the active book.")
    ap.add_argument("book", nargs="?", help="slug or books/<slug> path")
    ap.add_argument("--manifest", default=os.path.join(REPO, "book-manifest.json"))
    a = ap.parse_args()

    try:
        text, manifest = load(a.manifest)
    except Exception as exc:
        print(f"switch_book: cannot read {a.manifest}: {exc}", file=sys.stderr)
        return 1
    root = os.path.dirname(os.path.abspath(a.manifest))
    active = manifest.get("bookRoot")
    books = manifest.get("books", {})

    if not a.book:
        for key, meta in books.items():
            meta = meta or {}
            mark = "*" if key == active else " "
            print(f" {mark} {meta.get('slug', os.path.basename(key)):<24} {key}  "
                  f"- {meta.get('title', '?')}")
        print(f"\nactive: {active}")
        print("say: python3 scripts/switch_book.py <slug> to change it")
        return 0

    target = find_target(manifest, a.book)
    if target is None:
        print(f"switch_book: {a.book!r} is not registered. Registered: "
              f"{', '.join(books) or '(none)'}", file=sys.stderr)
        return 1
    if target == active:
        print(f"switch_book: {target} is already the active book; nothing written.")
        return 0

    folder = os.path.join(root, target)
    if not os.path.isdir(folder):
        print(f"switch_book: {target} is registered but {folder} does not exist.",
              file=sys.stderr)
        return 1
    missing = [f for f in resolve_book.REQUIRED_BOOK_FILES
               if not os.path.isfile(os.path.join(folder, f))]
    if missing:
        print(f"switch_book: {target} lacks {', '.join(missing)}; refusing - a desk "
              f"run against a missing spec writes generic prose.", file=sys.stderr)
        return 1

    matches = ROOT_KEY.findall(text)
    if len(matches) != 1:
        print(f"switch_book: expected exactly one \"bookRoot\" in the manifest, "
              f"found {len(matches)}; aborting without writing.", file=sys.stderr)
        return 1
    new_text = ROOT_KEY.sub(lambda m: f'{m.group(1)}"{target}"', text, count=1)
    if json.loads(new_text).get("bookRoot") != target:
        print("switch_book: in-memory replacement did not verify; nothing written.",
              file=sys.stderr)
        return 1
    with open(a.manifest, "w", encoding="utf-8") as fh:
        fh.write(new_text)

    print(f"switch_book: active book {active} -> {target}")
    print("next: python3 scripts/resolve_book.py")
    print("      voice_rules_check.py will FAIL until config/house.json mirrors "
          "this book's voice spec - that is the intended loud failure, not a bug.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
