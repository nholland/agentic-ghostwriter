#!/usr/bin/env python3
"""Apply external verification results back into the OKF citation ledger.

Reads the JSON array produced by an external session against a packet from
`verification_packet.py` and updates each citation concept: it records the
evidence found (edition, URL, locator, exact wording, context) in the concept's
`verification_note`, and appends an `# External Verification` section to the
body.

WHAT IT WILL NOT DO, BY DESIGN:

  * It never sets `status: verified`. CLAUDE.md Rule 11 reserves that for the
    author, against his own copy. External evidence moves a citation to
    `verifiable` and stages the wording; the author closes it. `--author-confirmed`
    exists for the case where the author is sitting there doing the confirming
    himself, and it is the only path to `verified`.
  * It never rewrites a quotation in the manuscript or in a chapter draft. A
    changed wording is REPORTED, loudly, and left for a human to apply, because
    changing a quote inside prose can break the sentence around it.

Verdict handling:
  CONFIRMED               evidence recorded; status -> verifiable
  WRONG_LOCATOR           the text is real but the book cites the wrong book,
                          section, or letter number; status -> unverified;
                          FLAGGED. Added 2026-09-03 after three of eight
                          entries in one packet came back with the right words
                          under the wrong number, which the original enum had
                          nowhere to put.
  PARTIAL                 genuine wording, but the book has spliced separated
                          passages into one continuous quotation, or otherwise
                          misrepresents how it appears; status -> unverified;
                          FLAGGED
  DIFFERENT_WORDING       evidence recorded; status -> verifiable; FLAGGED as a
                          prose-affecting change if the concept is quote_form:
                          verbatim
  NOT_FOUND               status -> unverified; note records where it was looked for
  SOURCE_DOES_NOT_SAY_THIS  status -> unverified; FLAGGED — this is a claim the
                          book may be making without support
  WRONG_ATTRIBUTION       status -> unverified; FLAGGED — highest severity

Usage:
    python3 scripts/verification_ingest.py books/the-stoic-husband results.json
    python3 scripts/verification_ingest.py books/the-stoic-husband results.json --dry-run
"""

import argparse
import datetime
import json
import os
import re
import sys

VERDICTS = {"CONFIRMED", "DIFFERENT_WORDING", "WRONG_LOCATOR", "PARTIAL",
            "NOT_FOUND", "SOURCE_DOES_NOT_SAY_THIS", "WRONG_ATTRIBUTION"}
EVIDENCE_VALUES = {"author-copy", "page-image", "page-text",
                   "database-abstract", "search-synthesis", "none"}
# Evidence where nobody opened the page — see `.claude/OKF.md`, "The
# transcription rule".
UNTRANSCRIBED_EVIDENCE = {"search-synthesis", "database-abstract", "none"}
STATUS_FOR = {
    "CONFIRMED": "verifiable",
    "DIFFERENT_WORDING": "verifiable",
    # WRONG_LOCATOR and PARTIAL: the text is real, so the source is not in
    # doubt — but the citation as printed is wrong and the prose must change.
    # They stay `unverified` because what the book currently says is not what
    # the source says, which is the condition `unverified` exists to mark.
    "WRONG_LOCATOR": "unverified",
    "PARTIAL": "unverified",
    "NOT_FOUND": "unverified",
    "SOURCE_DOES_NOT_SAY_THIS": "unverified",
    "WRONG_ATTRIBUTION": "unverified",
}
# Verdicts that mean printed prose is wrong and a human must change it.
PROSE_AFFECTING = {"DIFFERENT_WORDING", "WRONG_LOCATOR", "PARTIAL",
                   "SOURCE_DOES_NOT_SAY_THIS", "WRONG_ATTRIBUTION"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book_root")
    ap.add_argument("results_json")
    # Preview is the DEFAULT and writing requires --apply, deliberately.
    #
    # WHY THE DEFAULT IS INVERTED. CLAUDE.md Rule 7 requires generate -> check-in
    # -> save for every write to okf/, and Rule 13 extends it to ad hoc passes.
    # That gate used to live only in /book-verify's prose, which made it optional
    # for anyone invoking this script directly — and on 2026-09-07 it was bypassed
    # exactly that way, writing five concepts on an unanswered check-in. That was
    # the second walk of a borderline first recorded 2026-09-01.
    #
    # A gate in a command's prose is advisory. A gate in the write path is not.
    # With preview as the default, the careless invocation produces the artifact
    # you are supposed to show the author, and applying is a separate deliberate
    # act performed after he answers.
    ap.add_argument("--apply", action="store_true",
                    help="Actually write to the ledger. Without this the run is "
                         "a preview. Show the preview to the author and get a "
                         "response BEFORE passing --apply (CLAUDE.md Rule 7).")
    ap.add_argument("--dry-run", action="store_true",
                    help="No-op; preview is now the default. Kept so existing "
                         "docs and habits don't break.")
    ap.add_argument("--author-confirmed", action="store_true",
                    help="the author checked these against his own copies in "
                         "this sitting; allows CONFIRMED -> verified")
    args = ap.parse_args()

    with open(args.results_json, encoding="utf-8") as fh:
        try:
            results = json.load(fh)
        except json.JSONDecodeError as exc:
            print(f"could not parse {args.results_json}: {exc}", file=sys.stderr)
            print("The external session must return a JSON array and nothing "
                  "else. Strip any surrounding prose or code fences.",
                  file=sys.stderr)
            return 1
    if not isinstance(results, list):
        print("expected a JSON array", file=sys.stderr)
        return 1

    cdir = os.path.join(args.book_root, "okf", "citations")
    today = datetime.date.today().isoformat()
    applied, flagged, problems = [], [], []
    downgraded = []

    for r in results:
        slug = str(r.get("slug", "")).strip()
        verdict = str(r.get("verdict", "")).strip().upper()
        path = os.path.join(cdir, slug + ".md")
        if not slug or not os.path.exists(path):
            problems.append(f"no such citation concept: {slug!r}")
            continue
        if verdict not in VERDICTS:
            problems.append(f"{slug}: unknown verdict {verdict!r}")
            continue
        ctx = str(r.get("surrounding_context") or "").strip()
        if verdict in ("CONFIRMED", "DIFFERENT_WORDING", "WRONG_LOCATOR",
                       "PARTIAL") and not ctx:
            problems.append(
                f"{slug}: verdict {verdict} with no surrounding_context — "
                "treating as unevidenced, not applied")
            continue

        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        if not m:
            problems.append(f"{slug}: unparseable frontmatter")
            continue
        fm_raw, body = m.group(1), m.group(2)

        new_status = STATUS_FOR[verdict]
        if verdict == "CONFIRMED" and args.author_confirmed:
            new_status = "verified"

        was_verbatim = re.search(r"^quote_form:\s*verbatim\s*$", fm_raw, re.M)

        # The transcription rule (.claude/OKF.md). A quotation is confirmed only
        # by opening the page. If the evidence behind this result is a search
        # summary or a bibliographic record, the wording is NOT established, and
        # the result gets recorded at `unverified` no matter what verdict the
        # verifier returned. This is the check that would have kept six of this
        # project's nine printed defects out of the ledger.
        evidence = str(r.get("evidence_source") or "").strip()
        if evidence and evidence not in EVIDENCE_VALUES:
            problems.append(
                f"{slug}: unknown evidence_source {evidence!r} "
                f"(one of: {', '.join(sorted(EVIDENCE_VALUES))})")
            continue
        if not evidence:
            problems.append(
                f"{slug}: no `evidence_source` in the result — required, since "
                "nothing downstream can tell a page you opened from a search "
                "summary without it")
            continue
        if evidence == "author-copy" and not args.author_confirmed:
            problems.append(
                f"{slug}: evidence_source: author-copy requires "
                "--author-confirmed (Rule 11 — only the author closes a "
                "citation, against his own copy)")
            continue
        if new_status == "verified" and evidence != "author-copy":
            problems.append(
                f"{slug}: cannot set `verified` on evidence_source "
                f"{evidence!r} — Rule 11 requires the author's own copy")
            continue
        if (was_verbatim and new_status in ("verifiable", "verified")
                and evidence in UNTRANSCRIBED_EVIDENCE):
            downgraded.append((slug, evidence))
            new_status = "unverified"

        fm_new = re.sub(r"^status:.*$", f"status: {new_status}",
                        fm_raw, count=1, flags=re.M)
        if re.search(r"^evidence_source:.*$", fm_new, re.M):
            fm_new = re.sub(r"^evidence_source:.*$",
                            f"evidence_source: {evidence}",
                            fm_new, count=1, flags=re.M)
        else:
            fm_new = fm_new.rstrip("\n") + f"\nevidence_source: {evidence}"
        if verdict in PROSE_AFFECTING:
            flagged.append((slug, verdict, str(r.get("notes") or "").strip()))

        section = [
            "\n\n# External Verification",
            f"\nChecked {today} in an external session with web access, because "
            "this environment's egress proxy blocks the hosts carrying primary "
            "texts and journal pages.",
            f"\n**Verdict:** `{verdict}`",
        ]
        for label, key in (("Edition", "edition"), ("Locator", "locator"),
                           ("URL", "url"), ("Confidence", "confidence")):
            v = str(r.get(key) or "").strip()
            if v:
                section.append(f"\n**{label}:** {v}")
        exact = str(r.get("exact_text") or "").strip()
        if exact:
            section.append(f"\n**Source's own wording:**\n\n> {exact}")
        if ctx:
            section.append(f"\n**Surrounding context:** {ctx}")
        notes = str(r.get("notes") or "").strip()
        if notes:
            section.append(f"\n**Notes:** {notes}")
        if new_status != "verified":
            section.append(
                "\n**Still not `verified`.** External evidence does not close "
                "CLAUDE.md Rule 11; only the author does, against his own copy.")

        with open(path, "w", encoding="utf-8") if args.apply else open(os.devnull, "w") as fh:
            fh.write(f"---\n{fm_new}\n---\n{body.rstrip()}" + "".join(section) + "\n")
        applied.append((slug, verdict, new_status))

    verb = "applied" if args.apply else "would apply"
    print(f"{verb} {len(applied)} result(s)")
    for slug, verdict, st in applied:
        print(f"  {verdict:24} -> {st:11} {slug}")
    if flagged:
        print(f"\nNEEDS A HUMAN ({len(flagged)}) — prose may be affected, "
              "nothing was rewritten:")
        for slug, verdict, note in flagged:
            print(f"  ! {verdict}: {slug}")
            if note:
                print(f"      {note[:150]}")
    if downgraded:
        print(f"\nDOWNGRADED BY THE TRANSCRIPTION RULE ({len(downgraded)}):")
        print("  These are verbatim quotations whose evidence was not the page "
              "itself,\n  so the wording is not established. Recorded as "
              "`unverified`.")
        for slug, ev in downgraded:
            print(f"  v {slug} (evidence_source: {ev})")
    if problems:
        print(f"\nNOT APPLIED ({len(problems)}):")
        for p in problems:
            print(f"  x {p}")
    if not args.apply:
        print("\n" + "=" * 68)
        print("PREVIEW — nothing was written.")
        print("Show this to the author and get a response, then re-run with")
        print("--apply. CLAUDE.md Rule 7: generate -> check-in -> save.")
        print("=" * 68)
    if args.apply and applied:
        print("\nNext: python3 scripts/citation_queue.py " + args.book_root)
    return 0


if __name__ == "__main__":
    sys.exit(main())
