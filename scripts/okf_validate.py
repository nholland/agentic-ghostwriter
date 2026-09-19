#!/usr/bin/env python3
"""Conformance + integrity checker for a book's OKF knowledge bundle.

Validates a `{bookRoot}/okf/` bundle against the spec in `.claude/OKF.md`
(which adapts Google's Open Knowledge Format v0.1). Intended to be run by the
author at any time, and callable from /book-status as a health check before
chapter work begins.

Checks performed:
  1. Conformance — every non-reserved okf/**/*.md has parseable YAML
     frontmatter with a non-empty `type`.
  2. Index parity — counts in okf/index.md match the files on disk per type.
  3. Link integrity — internal `/...md` links resolve (broken links are
     reported as an inventory; per spec they are tolerated, not fatal).
  4. No-fabrication — no `status: verified` citation has an empty `resource`.
  5. Citation reconciliation — every citation row in
     sources/citation-manifest.md has a matching okf/citations/*.md.
  6. Tombstone guard — nothing outside the tombstone references the retired
     sources/evidence-library.md as a live source.
  7. Future-dated timestamps — no concept's `timestamp` is later than today.
     A concept stamped with a date that hasn't happened is not a typo, it is
     an invented date: the only way to produce one is to supply a plausible
     value instead of reading the clock. Added 2026-09-01 after a Ch11
     research pass stamped sixteen concepts 1-4 days early, which no check
     could see because CLAUDE.md Rule 9's read-the-time requirement is scoped
     to progress.md and every wrong date here was in OKF frontmatter.
  8. Chapter slug integrity — every `chapter_slugs` entry resolves to a
     chapter/Introduction/Conclusion heading currently in 03-outline.md (or
     is the literal `all`). Catches drift after a chapter title is renamed —
     chapter *numbers* can't drift anymore (concepts don't reference them),
     but a stale slug from before a rename still can.

Exit code 0 if no errors (warnings allowed), 1 if any error.

Usage:
    python3 scripts/okf_validate.py books/the-stoic-husband
    python3 scripts/okf_validate.py            # defaults to bookRoot in book-manifest.json
"""

import argparse
import datetime
import json
import os
import re
import sys

import yaml


def slugify(title):
    s = title.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    return re.sub(r"-+", "-", s)


def valid_chapter_slugs(book_root):
    """Slugs currently valid per 03-outline.md, plus the fixed tokens."""
    outline_path = os.path.join(book_root, "03-outline.md")
    if not os.path.isfile(outline_path):
        return None  # can't check; caller should skip
    text = open(outline_path, encoding="utf-8").read()
    slugs = {"introduction", "conclusion", "all"}
    for m in re.finditer(r"^## Chapter \d+: (.+)$", text, re.MULTILINE):
        slugs.add(slugify(m.group(1)))
    # The Introduction and Conclusion carry titles too - "## Introduction: The
    # Man Without a Blueprint" - and a concept may name either by its title
    # slug, exactly as it would a numbered chapter. Accepting only the bare
    # tokens reported a correct slug as an orphan (2026-09-19: the river/oak/sun
    # framework's 'the-man-without-a-blueprint', which is a real chapter). A
    # checker that calls good data drift is worse than no checker: the repair it
    # invites is to damage the data until the check goes quiet.
    for m in re.finditer(r"^## (?:Introduction|Conclusion): (.+)$", text, re.MULTILINE):
        slugs.add(slugify(m.group(1)))
    return slugs

RESERVED = {"index.md", "log.md", "README.md"}
TYPE_DIRS = {
    "frameworks": "Framework",
    "stories": "Story",
    "citations": "Citation",
    "signals": "Reader Signal",
    "findings": "QA Finding",
    "notes": "Author Note",
}


def parse_frontmatter(path):
    """Return (frontmatter_dict_or_None, body_str). None dict = no/!parseable FM."""
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None, text
    return (fm if isinstance(fm, dict) else None), parts[2]


STATUS_VALUES = {"unverified", "verifiable", "verified", "superseded"}
QUOTE_FORM_VALUES = {"verbatim", "paraphrase", "none"}
EVIDENCE_VALUES = {
    "author-copy", "page-image", "page-text",
    "database-abstract", "search-synthesis", "none",
}
# Evidence that nobody actually opened the page. A verbatim quotation may not
# be called confirmed on any of these — see `.claude/OKF.md`, "The
# transcription rule".
UNTRANSCRIBED_EVIDENCE = {"search-synthesis", "database-abstract", "none"}
CONFIRMED_STATUS = {"verifiable", "verified"}


def check_citation_axes(fm, rel):
    """The three-axis citation schema and the transcription rule.

    Returns a list of problem strings. Callers decide whether these are errors
    (--strict) or warnings, so the existing ledger can be backfilled before the
    gate is wired into /book-chapter-refine and /book-compile.
    """
    problems = []
    status = str(fm.get("status", "")).strip()

    # `superseded` concepts are historical records of a gap that a better concept
    # replaced. The spec already excludes them from open-gap counts; holding them
    # to the live three-axis schema would be noise about something nobody will
    # cite. Only the status value itself is checked.
    if status == "superseded":
        return problems
    quote_form = str(fm.get("quote_form", "")).strip()
    evidence = str(fm.get("evidence_source", "")).strip()

    # Presence + enum. A missing field and a typo'd one fail the same way:
    # before this check, `status: verifed` passed clean AND silently bypassed
    # the `verified`-needs-a-resource check, because that compares the exact
    # string "verified".
    for field, value, allowed in (
        ("status", status, STATUS_VALUES),
        ("quote_form", quote_form, QUOTE_FORM_VALUES),
        ("evidence_source", evidence, EVIDENCE_VALUES),
    ):
        if not value:
            problems.append(
                f"{rel}: citation has no `{field}` "
                f"(required — one of: {', '.join(sorted(allowed))})"
            )
        elif value not in allowed:
            problems.append(
                f"{rel}: `{field}` is {value!r}, not one of: "
                f"{', '.join(sorted(allowed))}"
            )

    # The transcription rule.
    if (quote_form == "verbatim"
            and status in CONFIRMED_STATUS
            and evidence in UNTRANSCRIBED_EVIDENCE):
        problems.append(
            f"{rel}: quote_form: verbatim + status: {status} + "
            f"evidence_source: {evidence or 'unset'} violates the transcription "
            "rule — a quotation cannot be called confirmed when nobody opened "
            "the page. Either obtain page evidence (page-text / page-image / "
            "author-copy) or drop status to `unverified`. "
            "See .claude/OKF.md, 'The transcription rule'."
        )

    # Rule 11: only the author, against his own copy.
    if status == "verified" and evidence and evidence != "author-copy":
        problems.append(
            f"{rel}: status: verified requires evidence_source: author-copy "
            f"(got {evidence!r}). Only the author closes a citation, against "
            "his own copy — CLAUDE.md Rule 11."
        )

    return problems


def default_book_root():
    try:
        manifest = json.load(open("book-manifest.json", encoding="utf-8"))
        return manifest.get("bookRoot")
    except (OSError, ValueError):
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book_root", nargs="?", default=default_book_root())
    ap.add_argument(
        "--strict", action="store_true",
        help="Enforce the three-axis citation schema (status / quote_form / "
             "evidence_source) and the transcription rule. Advisory until the "
             "existing ledger is backfilled, then wired into "
             "/book-chapter-refine and /book-compile as a gate.",
    )
    args = ap.parse_args()

    if not args.book_root:
        print("ERROR: no bookRoot given and none found in book-manifest.json")
        return 1

    okf = os.path.join(args.book_root, "okf")
    if not os.path.isdir(okf):
        print(f"ERROR: no OKF bundle at {okf}")
        return 1

    errors, warnings = [], []
    axis_warnings = []
    concept_paths = []  # bundle-relative ("/frameworks/x.md") for link checking
    disk_counts = {d: 0 for d in TYPE_DIRS}
    valid_slugs = valid_chapter_slugs(args.book_root)
    stale_slugs = []

    # 1. Conformance + collect concepts
    for sub, expected_type in TYPE_DIRS.items():
        d = os.path.join(okf, sub)
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            if not name.endswith(".md") or name in RESERVED:
                continue
            path = os.path.join(d, name)
            disk_counts[sub] += 1
            concept_paths.append(f"/{sub}/{name}")
            fm, body = parse_frontmatter(path)
            rel = os.path.relpath(path, args.book_root)
            if fm is None:
                errors.append(f"{rel}: missing or unparseable YAML frontmatter")
                continue
            if not str(fm.get("type", "")).strip():
                errors.append(f"{rel}: frontmatter has no non-empty `type`")
            elif fm.get("type") != expected_type:
                warnings.append(
                    f"{rel}: type is '{fm.get('type')}', expected '{expected_type}' for {sub}/"
                )
            # 7. Future-dated timestamp = an invented date, not a typo.
            ts = str(fm.get("timestamp", "")).strip()
            if ts:
                try:
                    stamped = datetime.date.fromisoformat(ts[:10])
                except ValueError:
                    warnings.append(
                        f"{rel}: `timestamp` is not an ISO date: {ts!r}"
                    )
                else:
                    if stamped > datetime.date.today():
                        errors.append(
                            f"{rel}: `timestamp` {stamped} is in the future. "
                            "A future date cannot be a typo — it means the date "
                            "was supplied rather than read. Get it from "
                            "`date '+%Y-%m-%d'` or from the commit that "
                            "introduced the concept."
                        )

            # 4. No-fabrication: verified citation must have a resource
            if sub == "citations" and str(fm.get("status", "")).strip() == "verified":
                if not str(fm.get("resource", "")).strip():
                    errors.append(
                        f"{rel}: status: verified but `resource` is empty "
                        "(CLAUDE.md Rule 3 — do not present unverified sources as fact)"
                    )

            # 8. The three citation axes + the transcription rule.
            #    See `.claude/OKF.md` "The three citation axes".
            if sub == "citations":
                axis_problems = check_citation_axes(fm, rel)
                (errors if args.strict else axis_warnings).extend(axis_problems)

            # 7. Chapter slug integrity
            if valid_slugs is not None:
                for cs in fm.get("chapter_slugs") or []:
                    if str(cs).strip() not in valid_slugs:
                        stale_slugs.append(f"{rel}: chapter_slugs has {cs!r}, no matching chapter in 03-outline.md")

    # 2. Index parity
    index_path = os.path.join(okf, "index.md")
    if os.path.isfile(index_path):
        index_text = open(index_path, encoding="utf-8").read()
        for sub in TYPE_DIRS:
            listed = len(set(re.findall(rf"\(/{sub}/[^)]+\.md\)", index_text)))
            if disk_counts[sub] and listed != disk_counts[sub]:
                warnings.append(
                    f"index.md lists {listed} {sub} but {disk_counts[sub]} exist on disk"
                )
    else:
        warnings.append("no index.md (tolerated by spec, but rollup is missing)")

    # 3. Link integrity (inventory broken internal links; not fatal)
    existing = set(concept_paths)
    broken = []
    for relpath in concept_paths:
        path = os.path.join(okf, relpath.lstrip("/"))
        _, text = parse_frontmatter(path)
        for target in re.findall(r"\]\((/[A-Za-z0-9._/\-]+\.md)\)", text):
            if target not in existing and not os.path.isfile(os.path.join(okf, target.lstrip("/"))):
                broken.append(f"{relpath} -> {target}")

    # 5. Citation queue freshness.
    #    This used to be "reconciliation with sources/citation-manifest.md", but the
    #    check was never implemented -- it computed these two values and used them
    #    only to print a note. That dead check is why ten manifest quote rows sat
    #    with no matching concept, unnoticed, until an audit on 2026-08-14. The
    #    manifest is now a tombstone and the queue is generated, so the real
    #    invariant is that the generated file is not stale.
    citation_slugs = {
        os.path.basename(p)[:-3] for p in concept_paths if p.startswith("/citations/")
    }
    queue_path = os.path.join(args.book_root, "citation-queue.md")
    if not os.path.isfile(queue_path):
        warnings.append(
            "citation-queue.md missing — run: python3 scripts/citation_queue.py "
            f"{args.book_root}"
        )
    else:
        listed = set(re.findall(r"\(okf/citations/([A-Za-z0-9._\-]+)\.md\)", open(queue_path, encoding="utf-8").read()))
        missing = citation_slugs - listed
        if missing:
            warnings.append(
                f"citation-queue.md is stale — {len(missing)} concept(s) absent from it "
                f"(e.g. {sorted(missing)[0]}). Run: python3 scripts/citation_queue.py "
                f"{args.book_root}"
            )

    # 6. Tombstone guard: live references to evidence-library.md
    #
    # Scans the book directory AND .claude/, because the governance files are
    # where a stale pointer does the most damage: book-chapter-draft.md's Step 7
    # directed new author IP into the retired evidence-library.md until
    # 2026-08-17, and following it literally would have written the author's own
    # frameworks into a dead file. This guard existed the whole time and could
    # not see it, because it walked only args.book_root.
    scan_roots = [args.book_root]
    claude_dir = os.path.join(os.path.dirname(os.path.abspath(args.book_root)), ".claude")
    if not os.path.isdir(claude_dir):
        claude_dir = ".claude"
    if os.path.isdir(claude_dir):
        scan_roots.append(claude_dir)

    live_refs = []
    manifest_refs = []
    for scan_root in scan_roots:
      for root, _, files in os.walk(scan_root):
          for name in files:
            if not name.endswith(".md"):
                continue
            p = os.path.join(root, name)
            # LEARNINGS.md is an incident archive: it names retired files in the
            # past tense by design, the same exemption chapters/ and okf/ get below.
            if os.path.basename(p) == "LEARNINGS.md":
                continue
            # Same exemption, same reason, for the book's own append-only
            # history (2026-09-19). okf/log.md is a timestamped bundle log,
            # okf/README.md is the pilot assessment index.md itself points at
            # ("the original pilot assessment"), and its argument IS a Today-vs-OKF
            # comparison, so it names the retired file by design. Rewriting either
            # to quiet this guard would falsify a record - the house's Rule 15 says
            # a file that accumulates appends and never rewrites. A live pointer in
            # a file nothing writes to is not the risk this guard was built for;
            # governance and draft instructions are, and those are still scanned.
            if os.path.relpath(p, args.book_root) in (
                    os.path.join("okf", "log.md"), os.path.join("okf", "README.md")):
                continue
            if os.path.basename(p) in ("evidence-library.md", "citation-manifest.md"):
                continue  # a tombstone may reference itself
            text = open(p, encoding="utf-8").read()
            # Same changelog exemption the citation-manifest half uses below: a
            # mention whose own PARAGRAPH marks the file retired/superseded is a
            # record of its own history, not a live pointer. Without this, the
            # note documenting a fix gets flagged as the defect it just fixed.
            #
            # Paragraph, not line, and word STEMS, not inflections (2026-09-19).
            # The line-and-inflection version reported all six of its hits as
            # live when every one was historical: prose wraps, so the mention and
            # the word clearing it land on different lines, and the list missed
            # the forms actually used - index.md says "supersedes" where the
            # regex wanted "superseded", progress.md says "migration" not
            # "migrated". A guard that cries wolf on a tombstone teaches its
            # reader to edit good prose until it goes quiet, which is the damage
            # it exists to prevent. The teeth are unchanged: a live instruction
            # ("append new IP to evidence-library.md") carries none of these
            # stems anywhere in its paragraph and still flags - fixtured.
            CLEARED = re.compile(
                r"retir|supersed|migrat|tombstone|correct|replac|no longer|"
                r"instead of|the old|used to|has been|deprecat|"
                r"deriv|drawn from|faithfully",
                re.I)
            for para in re.split(r"\n\s*\n", text):
                if "evidence-library.md" not in para:
                    continue
                if CLEARED.search(para):
                    continue
                live_refs.append(os.path.relpath(p, args.book_root))
                break
            # citation-manifest.md retired 2026-08-14. Historical logs, shipped
            # chapters' Editor's Notes, and the migrated concepts' own provenance
            # all legitimately name it in the past tense; only governance docs
            # that could still send a reader to it as a live source are flagged.
            rel = os.path.relpath(p, args.book_root)
            historical = (
                rel.startswith(("chapters" + os.sep, "okf" + os.sep))
                or os.path.basename(p) in (
                    "progress.md", "sweep-report.md", "citation-queue.md",
                )
                # sources/verification/ holds dated verification packets: each
                # records what was logged, and where, at the time it ran. Naming
                # the manifest that was live in August is the record being
                # accurate, not a reader being misdirected (2026-09-19).
                or rel.startswith("sources" + os.sep + "verification" + os.sep)
            )
            # A mention on a line that also marks it retired/migrated is a
            # changelog entry, not a live pointer -- those are how a file records
            # its own history and must not be flagged.
            if not historical:
                for line in text.splitlines():
                    if "citation-manifest.md" not in line:
                        continue
                    if re.search(r"retired|migrated|tombstone", line, re.I):
                        continue
                    manifest_refs.append(rel)
                    break

    # ---- Report ----
    print(f"OKF bundle: {okf}")
    print(
          "Concepts: "
          + ", ".join(f"{disk_counts[s]} {s}" for s in TYPE_DIRS if disk_counts[s])
    )
    if broken:
          print(f"\nBroken internal links ({len(broken)}) — tolerated, but review:")
          for b in broken:
            print(f"  - {b}")
    if manifest_refs:
          warnings.append(
            "retired sources/citation-manifest.md referenced as live in: "
            + ", ".join(sorted(set(manifest_refs)))
            + " (point these at citation-queue.md)"
          )
    if live_refs:
          warnings.append(
            "evidence-library.md referenced as a live source in: "
            + ", ".join(sorted(set(live_refs)))
            + " (it is retired — point these at okf/index.md)"
          )
    if valid_slugs is None:
          warnings.append("no 03-outline.md found — skipped chapter slug integrity check")
    else:
          warnings.extend(stale_slugs)
    print(f"\nCitations: {len(citation_slugs)} concepts; okf/citations/ `status` is "
          "canonical. Reader-facing queue: citation-queue.md (generated).")

    # Three-axis schema problems. Advisory by default so the existing ledger
    # can be backfilled; --strict routes them into `errors` instead.
    if axis_warnings:
          print(f"\nCITATION SCHEMA ({len(axis_warnings)} advisory; "
                "re-run with --strict to fail on these):")
          for a in axis_warnings[:15]:
            print(f"  ~ {a}")
          if len(axis_warnings) > 15:
            print(f"  ... and {len(axis_warnings) - 15} more")

    if warnings:
          print(f"\nWARNINGS ({len(warnings)}):")
          for w in warnings:
            print(f"  ! {w}")
    if errors:
          print(f"\nERRORS ({len(errors)}):")
          for e in errors:
            print(f"  x {e}")
          return 1
    print("\nPASS — bundle conforms (warnings above are non-fatal).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
