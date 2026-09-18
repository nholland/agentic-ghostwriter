# External citation verification

**The problem.** This repo's Claude Code environment routes all outbound
traffic through an egress proxy that blocks every host carrying a primary text
or a paywalled paper: Project Gutenberg, Wikisource, archive.org,
classics.mit.edu, Standard Ebooks, sacred-texts, PubMed, SAGE, Taylor &
Francis, ZORA, and others. Citations here therefore reach `status: verifiable`
on the strength of multiple independent secondary listings and stop. As of the
first run, 84 of 89 were waiting.

**The workaround.** Do the lookups in a session that has real web or computer
access — Claude Desktop, ChatGPT, a browser and an afternoon — and bring
structured results back.

## The loop

1. **Generate.** `python3 scripts/verification_packet.py books/the-stoic-husband`
   writes `packet-NN.md` here, 8 citations each, hardest-hitting first.
2. **Run.** Paste one packet into a session with web access. One packet per
   conversation; they are sized so the model can be careful rather than fast.
3. **Save** the returned JSON array as `results-NN.json` in this directory.
4. **Ingest.** `python3 scripts/verification_ingest.py books/the-stoic-husband
   sources/verification/results-NN.json --dry-run` first, then without
   `--dry-run`.
5. **Regenerate the queue.** `python3 scripts/citation_queue.py books/the-stoic-husband`

## Tiers

Ordered by what breaks if the citation is wrong.

- **Tier 1 (16)** — an exact quote already sitting in compiled manuscript
  prose. Wrong wording here is a wrong book. Fourteen are public-domain
  classical texts, which makes this both the most urgent tier and the one an
  external agent can actually close.
- **Tier 2 (33)** — a research finding asserted in compiled prose. Wording is
  irrelevant; whether the source supports the claim is everything.
- **Tier 3** — filed for chapters not yet drafted. Excluded by default; pass
  `--max-tier 3`.

## What this cannot do

**It cannot mark anything `verified`.** CLAUDE.md Rule 11 reserves that for the
author, against his own copy. External evidence moves a citation to
`verifiable` and stages the exact wording, edition, and locator so the author's
own check becomes a fast confirmation instead of a research project. The
`--author-confirmed` flag exists only for when the author is doing the checking
himself in that sitting.

**It never edits prose.** A `DIFFERENT_WORDING` verdict on a verbatim quote is
reported loudly and left alone, because changing a quotation inside a sentence
can break the sentence around it. A human applies those.

## The design problem the prompt is built around

An external model asked to "verify these quotes" will confirm things it has not
seen. That failure mode would be worse than the current state, because it
launders a guess into the ledger as evidence. The packet prompt is built
against it:

- **"NOT_FOUND is a correct and welcome answer"** is stated up front and
  repeated. Removing the pressure to produce a confirmation is the single most
  important line in the prompt.
- **`surrounding_context` is required** for any CONFIRMED or DIFFERENT_WORDING
  verdict, and `verification_ingest.py` **refuses** the result without it. A
  model that did not open the source cannot produce the forty words around the
  quote. This is a mechanical check, not a request.
- **Quote aggregators are named and excluded** — Goodreads, Pinterest,
  listicles, "commonly attributed to." Several suspect entries here are
  believed to have come from exactly those.
- **Translator and year are mandatory.** "Meditations 4.49" is not a verified
  quote; the wordings genuinely differ between Long, Farquharson, Hays, and
  Haines, and the book is standardizing on Long and Gummere.
- **`WRONG_ATTRIBUTION` is an available verdict**, so a model that finds the
  text belongs to someone else has somewhere to put that rather than forcing it
  into a confirm/not-found binary.

## Highest-value single packet

`packet-01.md`. It is entirely Tier 1 and mostly Marcus Aurelius and Epictetus
in public-domain translations, which are the most findable texts on this list
and the ones already printed in the manuscript.
