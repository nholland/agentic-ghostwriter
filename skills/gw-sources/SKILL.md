---
description: The Researcher ingests raw source material into typed OKF concepts - frameworks, stories, citations. Raw intake stays raw; curation is proposed, not written. Run before chapter work and whenever new material arrives.
---

<!-- DERIVED FILE - DO NOT EDIT.
     Canonical copy: .claude/skills/gw-sources/SKILL.md
     Regenerate: python3 scripts/sync_plugin_layout.py -->
# /gw-sources — raw material into typed knowledge

Argument: optional path or description of what arrived. `$ARGUMENTS`

## Step 0

```
python3 scripts/resolve_book.py
python3 scripts/okf_gate.py
```

`resolve_book.py` is blocking. The citation gate **reports** and does not stop the run (Rule 4): an unverified citation is unfinished work, not a defect. A structural failure there still blocks.
— that is the format contract, and this skill must not invent a concept shape.

## The two directories, which are not the same thing

- `{bookRoot}/sources/` — **raw, unprocessed intake.** Whatever arrived, as it
  arrived. Never edit it into shape.
- `{bookRoot}/okf/` — **curated typed concepts.** frameworks, stories, citations,
  signals. Every one has frontmatter and provenance.

Ingestion moves understanding from the first to the second. It never moves files.

## Step 1 — dispatch the Researcher

Dispatch `gw-researcher` over the raw material. It returns proposed concepts.

**Chapter references go by slug, not number.** `chapter_slugs:
[not-everyone-gets-a-vote]`, never `chapters: [ch10]`. Numbers are position and
shift when the outline is revised; slugs are identity.

## Step 2 — the write rule, which splits

Per the book's Rule 13, and the split is not optional:

- **Gap markers** — a citation concept whose entire content is "this claim needs a
  source and nobody has found one" — may be written immediately. The file *is* the
  flag; there is nothing to approve.
- **Source findings** — what an external source says, at `status: unverified`
  — may be written immediately too (Rule 9).
- **Content concepts** — a framework, a story, the author's own material — are
  **shown first.** What goes in one is a claim about what
  the author thinks, and only he can confirm it. Present proposed frontmatter and
  body; write after he responds.

When you cannot tell which a concept is, ask. Do not default to writing.

## Step 3 — citations

Never invent one. Never set `verified`. Never let a search transcribe a quotation:
`quote_form: verbatim` may not sit at `verifiable` with `evidence_source:
search-synthesis`. Quote the house editions from `06-sources.md`; never invent a
house translation.

This applies to sources **the author** supplies too. A title he cites as
research-backed often is not — pop self-help especially. Verify before treating it
as citable, and log it `unverified` and say so plainly if you cannot.

## Step 4 — provenance and dates

Record in each concept's `provenance` where the material came from and, where the
author pushed back on an earlier pass, how many rounds it took and what each
changed. Stamp from `date '+%Y-%m-%d %H:%M'` — never a plausible date.

## Step 5 — gate and report

Re-run `python3 scripts/okf_gate.py`. Report concepts created by type, what was
proposed and is awaiting his response, what was left raw and why, and any claim you
could not source.
