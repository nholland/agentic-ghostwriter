#!/usr/bin/env python3
"""Generate external-verification request packets from the OKF citation ledger.

WHY THIS EXISTS. This environment's egress proxy blocks every host that carries
a primary text or a paywalled paper (Gutenberg, Wikisource, archive.org,
classics.mit.edu, PubMed, SAGE, Taylor & Francis, and more). Citations
therefore reach `status: verifiable` on the strength of multiple independent
secondary listings and stop there. This script packages what is outstanding so
the work can be done in a session that DOES have web or computer access, and
brings the answers back in a form `verification_ingest.py` can apply.

WHAT IT DELIBERATELY DOES NOT DO. It does not let an external model mark
anything `verified`. Per CLAUDE.md Rule 11 only the author does that. What an
external pass produces is EVIDENCE — a specific edition, a URL, surrounding
context, and a verdict — which the author then accepts or rejects. See the
"Tiering" note below for the one place that rule is worth revisiting.

TIERING. Ordered by what breaks if the citation is wrong:
  1. verbatim-in-manuscript — an exact quote already sitting in compiled prose.
     Wrong wording here is a wrong book. Mostly public-domain classical texts,
     which is also the tier an external agent can actually close.
  2. claim-in-manuscript — a research finding asserted in compiled prose.
     Wording doesn't matter; whether the source says it does.
  3. backlog — filed for chapters not yet drafted.

Usage:
    python3 scripts/verification_packet.py books/the-stoic-husband
    python3 scripts/verification_packet.py books/the-stoic-husband --per-packet 8
"""

import argparse
import json
import os
import re
import sys

import yaml

SCHEMA = """{
  "slug": "<the slug exactly as given>",
  "verdict": "CONFIRMED | DIFFERENT_WORDING | WRONG_LOCATOR | PARTIAL | NOT_FOUND | SOURCE_DOES_NOT_SAY_THIS | WRONG_ATTRIBUTION",
  "edition": "<translator/editor, publisher, year — or null>",
  "url": "<direct URL to the page you actually opened — or null>",
  "exact_text": "<what the source actually says, transcribed from what you saw — or null>",
  "surrounding_context": "<~40 words around it, so a reader can confirm you were on the right page — or null>",
  "locator": "<book/section/letter/page as the source numbers it — or null>",
  "notes": "<anything that would change the verdict; disagreements between editions; why not found>",
  "confidence": "high | medium | low"
}"""

PREAMBLE = """# Citation verification request — packet {n} of {total}
### {book_title}

You are checking quotations and claims for a nonfiction book. Accuracy matters
more than completeness. **A confident wrong answer here ends up printed.**

## The one rule that matters

**"NOT_FOUND" is a correct and welcome answer.** It is not a failure and it is
not a disappointment. Roughly a third of these may be unfindable, misattributed,
or subtly different from what is recorded below, and finding that out is the
entire point of the exercise. Do not stretch to confirm something. Do not
reason from what a source "would" say. Do not treat a quote appearing on
quote-aggregator sites, Goodreads, Pinterest, or a blog as evidence — those are
where misattributions breed, and several entries below are suspected to have
come from exactly there.

## What counts as evidence

- A scan, facsimile, or full-text edition of the actual work (archive.org,
  Project Gutenberg, Wikisource, Perseus, Standard Ebooks, a publisher's
  preview, Google Books page images).
- A journal's own page for a paper: abstract, DOI record, or full text.
- **Not** evidence: a quote site, a listicle, an AI summary, another chatbot,
  or "commonly attributed to."

If you can open the actual text, transcribe what you SEE. If your only access
is a secondary source, say so in `notes` and set `confidence` to low.

## Editions matter here

This book is standardizing on **public-domain translations**: George Long for
Marcus Aurelius and Epictetus, Richard Gummere (Loeb) for Seneca's letters.
Where an entry names a different translator, report BOTH: what the named
translator says, and what Long/Gummere say. Translations of the same passage
differ enough that a reader comparing editions will notice.

Report the **translator and year** every time. "Meditations 4.49" without an
edition is not a verified quote, because the wordings genuinely differ.

**Standing request, and it applies to every Marcus Aurelius and Epictetus entry
below regardless of what translator that entry names: give me George Long's
wording specifically.** Long is the house standard because he is public domain
and this book is self-published. Where an entry currently records Hays,
Farquharson, Haines, Carter, Matheson, or Oldfather, report that translator's
wording *and* Long's, clearly labelled. An entry confirmed only in a
copyrighted translation does not close, because the book cannot print it.

Long's Marcus Aurelius and Epictetus are both on Wikisource and archive.org in
full text.

## Output format

Return a JSON array, one object per entry, nothing else. Use exactly this shape:

```json
{schema}
```

Field notes:
- `exact_text` — transcribe it. Do not normalize punctuation, do not modernize
  spelling, do not fix what looks like an error. If the source has a dash, keep
  the dash. The book has a house rule about punctuation inside quotations and
  needs to know what the translator actually printed.
- `surrounding_context` — this is the anti-hallucination check. If you cannot
  produce it, you did not open the source, and the verdict should be NOT_FOUND.
- `WRONG_ATTRIBUTION` — the text exists but belongs to someone else, or to a
  different work by the same author. Say who or what in `notes`.
- `WRONG_LOCATOR` — **check this on every entry.** The wording is right but the
  book, section, or letter number we recorded is wrong. This is the single most
  common defect found so far: three of eight entries in one packet had the
  right words under the wrong number. Give the correct locator.
- `PARTIAL` — the wording is genuine but we have misrepresented how it appears:
  two separated passages spliced into one continuous quotation, a fragment
  presented as a whole sentence, a mid-sentence excerpt capitalized as if it
  began one. Say exactly what the source does instead.

---

## Entries

"""


def parse_frontmatter(path):
    with open(path, "r", encoding="utf-8") as fh:
        raw = fh.read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m:
        return {}, raw
    try:
        return yaml.safe_load(m.group(1)) or {}, m.group(2)
    except yaml.YAMLError:
        return {}, m.group(2)


def extract_quote(body):
    """Pull the first blockquote out of a concept body, if there is one."""
    lines, buf = body.splitlines(), []
    for ln in lines:
        if ln.startswith(">"):
            buf.append(ln.lstrip("> ").rstrip())
        elif buf:
            break
    return " ".join(buf).strip()


def tier_of(slug, fm, body, manuscript):
    surname = slug.split("-")[0].lower()
    in_man = len(surname) > 3 and surname in manuscript
    if str(fm.get("quote_form", "")).strip() == "verbatim" and in_man:
        return 1
    if in_man:
        return 2
    return 3


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book_root")
    ap.add_argument("--per-packet", type=int, default=8)
    ap.add_argument("--max-tier", type=int, default=2,
                    help="highest tier number to include (default 2 = manuscript only)")
    args = ap.parse_args()

    cdir = os.path.join(args.book_root, "okf", "citations")
    mpath = os.path.join(args.book_root, "manuscript.md")
    manuscript = ""
    if os.path.exists(mpath):
        with open(mpath, encoding="utf-8") as fh:
            manuscript = fh.read().lower()

    entries = []
    for name in sorted(os.listdir(cdir)):
        if not name.endswith(".md"):
            continue
        slug = name[:-3]
        fm, body = parse_frontmatter(os.path.join(cdir, name))
        status = str(fm.get("status", "")).strip()
        if status in ("verified", "superseded"):
            continue
        # Already checked externally — a re-run should yield only what is left,
        # so the loop can be run repeatedly without re-asking settled questions.
        if "# External Verification" in body:
            continue
        t = tier_of(slug, fm, body, manuscript)
        if t > args.max_tier:
            continue
        entries.append({
            "tier": t,
            "slug": slug,
            "title": str(fm.get("title", "")).strip(),
            "status": status,
            "quote_form": str(fm.get("quote_form", "")).strip() or "unset",
            "resource": " ".join(str(fm.get("resource", "") or "").split()),
            "note": " ".join(str(fm.get("verification_note", "") or "").split()),
            "quote": extract_quote(body),
        })

    entries.sort(key=lambda e: (e["tier"], e["slug"]))
    outdir = os.path.join(args.book_root, "sources", "verification")
    os.makedirs(outdir, exist_ok=True)

    chunks = [entries[i:i + args.per_packet]
              for i in range(0, len(entries), args.per_packet)]
    book_title = os.path.basename(args.book_root.rstrip("/"))

    for i, chunk in enumerate(chunks, 1):
        lines = [PREAMBLE.format(n=i, total=len(chunks), schema=SCHEMA,
                                 book_title=book_title)]
        for e in chunk:
            lines.append(f"### `{e['slug']}`\n")
            lines.append(f"**Tier {e['tier']}** — "
                         + ("an exact quote already in the compiled manuscript"
                            if e["tier"] == 1 else
                            "a claim asserted in the compiled manuscript"))
            lines.append(f"\n**What we think it is:** {e['title']}")
            if e["resource"]:
                lines.append(f"\n**Source as recorded:** {e['resource']}")
            lines.append(f"\n**Quote form:** {e['quote_form']} "
                         f"(verbatim = the wording must match exactly; "
                         f"paraphrase = only the claim needs to hold)")
            if e["quote"]:
                lines.append(f"\n**Wording we currently have:**\n\n> {e['quote']}")
            else:
                lines.append("\n**Wording we currently have:** none recorded — "
                             "we need the source's own words.")
            if e["note"]:
                lines.append(f"\n**What is already known to be uncertain:** {e['note']}")
            lines.append("\n---\n")
        path = os.path.join(outdir, f"packet-{i:02d}.md")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
        print(f"wrote {path}  ({len(chunk)} entries)")

    counts = {}
    for e in entries:
        counts[e["tier"]] = counts.get(e["tier"], 0) + 1
    print(f"\n{len(entries)} entries across {len(chunks)} packets "
          f"(tier 1: {counts.get(1,0)}, tier 2: {counts.get(2,0)})")
    print("Tier 3 backlog excluded; pass --max-tier 3 to include it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
