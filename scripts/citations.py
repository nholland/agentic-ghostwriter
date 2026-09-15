#!/usr/bin/env python3
"""
citations.py - where every citation stands, and which chapters carry open ones.

WHY THIS EXISTS
    Author's direction, 2026-09-15: "Nothing should stop the progress of the
    book. It should just keep up with its different statuses and let me know in
    the inbox." Once the gate stopped halting on unverified work, something had
    to carry the statuses instead, or the book would simply proceed with nobody
    tracking what was still open.

WHY IT DOES NOT BUILD A MANIFEST
    Because the book repo already generates one. `citation_queue.py` writes
    `{bookRoot}/citation-queue.md` from the concept frontmatter, and it replaced
    a hand-maintained `sources/citation-manifest.md` that drifted until its own
    queue read "None at this time" while seven concepts were waiting - the
    failure CLAUDE.md Rule 15 is named after. A second manifest here would be
    that failure a third time. This reports, and points at the generated file.

WHAT IT ADDS THAT THE QUEUE DOES NOT
    The queue is a whole-book list. This answers the question a chapter run
    needs: which citations does THIS chapter lean on, and what is their status?
    That is what gets flagged in the chapter and raised in the inbox.

THE THREE KINDS, MATCHING okf_gate.py
    open        not confirmed yet. Normal, expected, never a fault.
    overclaim   the status stands above the evidence - a verbatim quote called
                confirmed with nobody having opened the page, or `verified` set
                by something other than the author's own copy. The repair is to
                lower the status, and this proposes that; it never writes in the
                book repo (Rule 8).
    settled     verified against the author's own copy, or superseded.

USAGE
    python3 scripts/citations.py                  # whole-book rollup
    python3 scripts/citations.py --chapter 12     # just this chapter's
    python3 scripts/citations.py --json
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

# What each status is allowed to rest on. A status above its evidence is an
# overclaim, and the honest repair is to come down to the best status the
# evidence supports - never to halt, and never to invent better evidence.
PAGE_EVIDENCE = {"author-copy", "page-image", "page-text"}
SETTLED = {"superseded"}


def frontmatter(path):
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return {}
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}
    fm, key = {}, None
    for line in m.group(1).split("\n"):
        if re.match(r"^[A-Za-z_]+:", line):
            key, _, val = line.partition(":")
            key, fm[key.strip()] = key.strip(), val.strip()
        elif key and line.startswith(" "):
            fm[key] = (fm[key] + " " + line.strip()).strip()
    # A folded scalar ("status: >" then an indented line) leaves the fold marker
    # at the front of the value. Eight concepts write status that way, and
    # without this they report as "> verifiable" and match no status at all -
    # a wrong count that looks like a new status rather than a parse bug.
    for k, v in fm.items():
        fm[k] = re.sub(r"^[>|][-+]?\s*", "", v).strip()
    return fm


def downgrade_to(status, quote_form, evidence):
    """The best status this evidence actually supports, or None if it is fine."""
    if status in SETTLED or not status:
        return None
    if status == "verified" and evidence != "author-copy":
        # Only the author closes a citation, against his own copy.
        return "verifiable" if evidence in PAGE_EVIDENCE else "unverified"
    if quote_form == "verbatim" and status in ("verifiable", "verified") \
            and evidence not in PAGE_EVIDENCE:
        # A quotation cannot be called confirmed when nobody opened the page.
        return "unverified"
    return None


def load(book_root, book_rel):
    d = os.path.join(book_root, book_rel, "okf", "citations")
    out = []
    if not os.path.isdir(d):
        return out
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md"):
            continue
        fm = frontmatter(os.path.join(d, fn))
        status = fm.get("status", "").strip()
        quote = fm.get("quote_form", "").strip()
        evid = fm.get("evidence_source", "").strip()
        slugs = re.findall(r"[A-Za-z0-9\-]+", fm.get("chapter_slugs", ""))
        prop = downgrade_to(status, quote, evid)
        out.append({
            "slug": fn[:-3], "title": fm.get("title", fn[:-3]),
            "status": status, "quote_form": quote, "evidence_source": evid,
            "chapter_slugs": slugs,
            "kind": ("overclaim" if prop else
                     "settled" if status in SETTLED or
                     (status == "verified" and evid == "author-copy") else "open"),
            "proposed_status": prop,
        })
    return out


def slugify(title):
    t = title.strip().lower()
    t = t.replace("\u2019", "").replace("'", "")
    t = re.sub(r"[^a-z0-9]+", "-", t)
    return t.strip("-")


def chapter_slug_map(book_root, book_rel):
    """chapter number -> outline slug, read from the book's own outline."""
    path = os.path.join(book_root, book_rel, "03-outline.md")
    out = {}
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return out
    # The outline carries no slug field: headings read "## Chapter 3: The
    # Discipline of Not Reacting" and the concepts carry the slugified title.
    # Derive it the same way rather than asking the author to maintain a map.
    for m in re.finditer(r"^#+\s*Chapter\s+(\d+)\s*[:\-\u2014]\s*([^\n]+)", text, re.M):
        out[int(m.group(1))] = slugify(m.group(2))
    return out


def main():
    ap = argparse.ArgumentParser(description="Where every citation stands.")
    ap.add_argument("--chapter", type=int, help="only citations this chapter leans on")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    cfg = resolve_book.load_config()
    root, _, _ = resolve_book.resolve(cfg)
    if not root:
        print("citations: no book repo resolvable. Run scripts/resolve_book.py.",
              file=sys.stderr)
        return 2
    rep = resolve_book.inspect(root, require_okf=True)
    book_rel = rep["info"].get("bookRootRelative")
    if not book_rel:
        print("citations: the book manifest has no bookRoot.", file=sys.stderr)
        return 2

    items = load(root, book_rel)
    scope = "the whole book"
    if a.chapter is not None:
        slug = chapter_slug_map(root, book_rel).get(a.chapter)
        if not slug:
            print("citations: chapter %d has no slug in 03-outline.md, so its "
                  "citations cannot be identified." % a.chapter, file=sys.stderr)
            return 1
        items = [i for i in items if slug in i["chapter_slugs"]]
        scope = "chapter %d (%s)" % (a.chapter, slug)

    by = {k: [i for i in items if i["kind"] == k]
          for k in ("open", "overclaim", "settled")}
    queue = os.path.join(book_rel, "citation-queue.md")

    if a.json:
        print(json.dumps({"scope": scope, "counts": {k: len(v) for k, v in by.items()},
                          "items": items, "manifest": queue}, indent=2))
        return 0

    print("citations: %s - %d total" % (scope, len(items)))
    print("  %3d open        not confirmed yet. Normal; never blocks a chapter."
          % len(by["open"]))
    print("  %3d overclaim   the status stands above the evidence." % len(by["overclaim"]))
    print("  %3d settled     your own copy, or superseded." % len(by["settled"]))

    if by["overclaim"]:
        print("\n  Claiming more than the evidence supports:")
        for i in by["overclaim"]:
            print("    %s" % i["slug"])
            print("      %s / %s / evidence: %s" % (i["status"],
                  i["quote_form"] or "unset", i["evidence_source"] or "unset"))
            print("      -> should read `status: %s` until better evidence exists"
                  % i["proposed_status"])
        print("\n  These are edits in the BOOK repo, which this engine never makes.")

    if by["open"]:
        print("\n  Open, by status:")
        counts = {}
        for i in by["open"]:
            counts[i["status"] or "unset"] = counts.get(i["status"] or "unset", 0) + 1
        for k in sorted(counts):
            print("    %-12s %d" % (k, counts[k]))

    print("\n  The manifest is generated, not kept here: %s" % queue)
    print("  Regenerate it with the book repo's scripts/citation_queue.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
