# OKF — The Knowledge Layer Format

This is the canonical specification for the **knowledge layer** used by every book
in this repository. It adapts Google's [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
(OKF v0.1) to the book-writing pipeline. Every command and agent that reads or
writes evidence, research, citations, reader feedback, QA findings, or author
notes MUST follow this spec. Do not redefine the format elsewhere — link here.

## Core principle

Knowledge is markdown. One knowledge unit per file. Each file ("concept") has YAML
frontmatter (required: `type`) and a markdown body that prefers structure
(headings, tables) over prose. Concepts link to each other with ordinary markdown
links. Consumers are **permissive**: never fail on unknown fields, unknown types,
or broken links (a broken link may be knowledge not yet authored).

The knowledge layer is for the material *behind* the book. It is NOT for the
manuscript (`draft.md`, `refined.md`), voice, or foundational docs (`00`–`04`).

## Bundle location and structure

Each book's bundle lives at `{bookRoot}/okf/`:

```
{bookRoot}/okf/
├── index.md        # readable rollup + okf_version (reserved)
├── log.md          # append-only change history (reserved)
├── frameworks/     # type: Framework      — author IP models/lenses
├── stories/        # type: Story          — anecdotes, audience signals, author stories
├── citations/      # type: Citation       — external sources, with status lifecycle
├── signals/        # type: Reader Signal  — reader responses from /book-signal
├── findings/       # type: QA Finding     — from human/argue/beta/tension/sweep
└── notes/          # type: Author Note    — substantive author notes worth keeping
```

`{bookRoot}/sources/` remains **raw intake only** — unprocessed material
(`interviews/`, `articles/`, `audience-signals.md`, `author-notes.md`,
`synthesis.md`). `/book-source-prep` curates raw `sources/` material *into* `okf/`
concepts. There is no `sources/evidence-library.md` anymore; it has been retired
in favor of this bundle.

## Frontmatter schema

**Required (all concepts):**
- `type` — one of: `Framework`, `Story`, `Citation`, `Reader Signal`, `QA Finding`, `Author Note`

**Recommended (all concepts):**
- `title` — human-readable name
- `description` — one- or two-sentence summary
- `provenance` — where it came from + confirmation date
- `ip` — `author` | `author-synthesis` | `audience-signal` | `external`
- `tags` — list of *topical* tags only (e.g. `scorekeeping`, `desire-discrepancy`).
  Do not put chapter numbers here — see `chapter_slugs` below.
- `chapter_slugs` — list of chapter slugs this concept serves (the reverse
  index) — see **Chapter references** below. This replaced a numeric
  `chapters: [ch01, ch16]` field; see Migration note.
- `timestamp` — ISO 8601

**Type-specific:**
- **Citation:** `resource` (canonical URL), `status` (`unverified` | `verifiable` | `verified` | `superseded`), `quote_form` (`verbatim` | `paraphrase` | `none`), `evidence_source` (`author-copy` | `page-image` | `page-text` | `database-abstract` | `search-synthesis` | `none`), `verification_note`, `gap_type` (`research` | `structural`, citations only — see **Gap types** below). The first three are **required on every Citation** — see **The three citation axes** below.
- **Story:** `disclosure` (`composite` | `identified` | `private`)
- **Reader Signal:** `platform`, `signal_category` (`resonance` | `confusion` | `objection` | `gift` | `extension` | `noise`), `gift_type` (`supporting` | `complicating` | `contradicting`), `resolves` (path to the citation it answers)
- **QA Finding:** `audit` (`human` | `argue` | `beta` | `tension` | `sweep`), `severity` (`minor` | `significant` | `devastating`), `status` (`open` | `addressed` | `resolved`), `chapter`
- **Author Note:** `topic`

Producers may add custom fields. Consumers must tolerate unknown fields.

## Chapter references: slugs, not numbers

Chapter **numbers** are position, not identity — outlines get revised,
chapters get inserted, and every existing chapter after the insertion point
shifts. A concept file that says `chapters: [ch12]` silently points at the
wrong chapter the moment position 12 changes hands. (This happened: inserting
one chapter into `the-stoic-husband`'s outline required renumbering 62 concept
files by hand, including prose mentions a frontmatter-only pass missed.)

Concepts instead reference chapters by **slug** — the kebab-case form of the
chapter's exact title in `03-outline.md` at the time of writing (e.g., Chapter
10, "Not Everyone Gets a Vote," → `not-everyone-gets-a-vote`). A chapter's slug
only changes if its *title* changes, which is a deliberate, rare edit — not an
automatic side effect of inserting or reordering other chapters.

```yaml
chapter_slugs: [not-everyone-gets-a-vote, living-separate-lives]
```

**Resolving a slug to a chapter, at read time:** any command that needs "which
concepts serve chapter N" (e.g. `book-chapter-research`) reads `03-outline.md`,
finds the heading for chapter N, slugifies its title, and matches concepts
whose `chapter_slugs` contains that slug. This makes the outline the single
source of truth for chapter identity; concepts never hardcode position.

**Known limitation:** this solves drift in the `okf/` layer only. Physical
chapter folders (`chapters/chNN/`) and `book-manifest.json`'s per-chapter
`stages` keys are still numeric, tied to files already on disk. Inserting a
chapter *after* later chapters already have drafted folders still requires
renaming those folders and remapping manifest keys by hand (or a future
script) — slugs don't make that part of the problem disappear, only the OKF
tagging part.

## Gap types (Citations only)

A `Citation` with `status: unverified` is a gap, but not all gaps are the same
kind of open question, and conflating them wastes research effort:

- `gap_type: research` — the topic belongs in the book somewhere; what's
  missing is a real, citable source. A researcher should go find one.
- `gap_type: structural` — it's not yet settled *whether* this belongs in the
  book, or where. This needs an author decision (fold into an existing
  chapter? a new chapter? cut?) before any research is worth doing.
  `book-chapter-research` must not spend effort sourcing a `structural` gap
  that hasn't been resolved.

**When a structural gap gets resolved** (the author decides where it lives —
e.g., a new chapter gets created for it): update the citation's
`chapter_slugs` to point at the resolving chapter, and reword `description`/
`# Status` to say so — but do **not** change `status`. The structural question
and the research question are independent; a chapter being written doesn't
make the underlying claim any more sourced. `gap_type` stays `structural` as
a record of how this gap originated, even after the structural half is
settled — the citation only leaves the ledger via `status`, which still
requires a real source. See `okf/citations/in-law-family-of-origin-boundaries.md`
for the worked example.

## The `superseded` status

`superseded` means **a citation gap was replaced by a more complete OKF
concept** — typically, real research was found and built into a proper
`Framework`. It does *not* mean "a chapter was written that touches this
topic" (that's a resolved `structural` gap, above — a different event that
doesn't change `status` at all). When superseding a citation:

- Set `status: superseded`.
- Add a `verification_note` (or extend `# Status`) pointing to the concept
  that replaced it.
- Keep the file — it's a historical record of the original gap, not a
  duplicate to delete.
- Exclude `superseded` citations from open-gap counts in `book-status`.

## Body conventions

Use markdown headings. Conventional sections (use the ones that apply):
- `# Schema` — structured breakdown (definitions, tables, the moving parts)
- `# Examples` — usage examples or scenarios
- `# Related` — links to neighboring concepts
- `# Citations` — external sources backing claims (numbered; for author IP, state "None — author IP")

## Linking

Absolute links from bundle root, beginning with `/`:
```
See [Attachment vs. Devotion](/frameworks/attachment-vs-devotion.md).
```
Links assert untyped relationships; meaning comes from surrounding prose. Links to
not-yet-authored concepts are valid and expected — never fail on them.

## Naming conventions

- Frameworks/stories/citations: kebab-case slug from the title — `the-virtue-question.md`, `gottman-four-horsemen.md`.
- Reader Signals and Author Notes: date-prefixed — `2026-06-14-roommates-resonance.md`.
- QA Findings: `{audit}-chNN-slug.md` — `argue-ch21-endurance-is-cowardice.md`.

## Citation status lifecycle (the no-fabrication ledger)

`okf/citations/` IS the verification ledger for CLAUDE.md Rule 3.

- `unverified` — a gap; the claim needs external research. Equivalent to the old
  "what still needs research" list. Never present as fact in the manuscript.
- `verifiable` — a real, locatable source identified, but exact quote/details not
  yet confirmed verbatim.
- `verified` — confirmed; `resource` and the exact quote are filled in.
- `superseded` — this gap was replaced by a more complete OKF concept (see
  **The `superseded` status**, above). Not an open gap; excluded from counts.

**Only the author sets `verified`,** against his own copy — CLAUDE.md Rule 11.
No command and no agent may set it. Autonomous work tops out at `verifiable`.

*(Corrected 2026-09-07. This paragraph previously read "The editor agent moves a
citation to `verified` when it resolves a public placeholder via WebSearch,"
which contradicted both Rule 11 and `.claude/agents/editor.md`'s own explicit
ceiling. The spec was the most authoritative place the wrong rule was written
down.)*

`/book-status` and `/book-sweep` audit `status:` to report what still needs
verification, instead of only grepping `[PLACEHOLDER]`.

## The three citation axes

`status` alone cannot describe a citation's safety, because three independent
things can be true or false about it. Every `Citation` carries all three, and
all three are **required**:

| Axis | Question it answers | Values |
|---|---|---|
| `status` | How confirmed is it? | `unverified` \| `verifiable` \| `verified` \| `superseded` |
| `quote_form` | What kind of check is owed? | `verbatim` \| `paraphrase` \| `none` |
| `evidence_source` | What was actually looked at? | `author-copy` \| `page-image` \| `page-text` \| `database-abstract` \| `search-synthesis` \| `none` |

They are independent by design. Rule 11 already established why the first two
cannot be collapsed: *"a paraphrase from a confirmed source and a paraphrase
from an unchecked one are different problems, and one column can't say so."*
`evidence_source` exists for the same reason — neither of the other two can
distinguish a page someone opened from a page a search engine described.

**`quote_form` describes how the *manuscript* uses the source,** not what the
concept file contains:
- `verbatim` — the prose quotes exact wording. Needs wording *and* punctuation
  checked against a specific edition. If the quote contains an em dash, say so
  in `verification_note`; `01-voice.md`'s em-dash exception depends on it.
- `paraphrase` — the idea is rendered loosely; no verbatim claim is made.
- `none` — the source is cited or named, never quoted.

**Set `quote_form` from the prose, not from intent.** If the manuscript puts the
words in quotation marks and attributes them, `quote_form` is `verbatim` —
regardless of whether the wording was *meant* as a loose rendering. Quotation
marks are a claim about wording, and the reader cannot see intent. A paraphrase
printed inside quotation marks is a misquotation, not a paraphrase.

*Added 2026-09-08, after a backfill pass found a Chapter 1 quotation whose own
concept recorded it as "not a verbatim line in any standard translation" while
the prose set it in italics and quotation marks directly after describing Marcus
Aurelius writing his notes. It was filed `quote_form: paraphrase`, which is
exactly why the transcription rule did not fire on it. The axis has to describe
what the reader is shown.*

**`evidence_source` records the strongest evidence actually obtained:**
- `author-copy` — the author checked his own physical copy. The only route to `verified`.
- `page-image` — a scan or facsimile of the printed page was viewed.
- `page-text` — the source page itself was retrieved and read (e.g. `WebFetch`).
- `database-abstract` — a bibliographic record or abstract, not the source text.
- `search-synthesis` — a search engine's summary. **Nobody opened the page.**
- `none` — a gap marker; nothing has been looked at yet.

### The transcription rule

> **Search may LOCATE a source or FLAG a defect. It may never TRANSCRIBE a quotation.**

Formally: a citation with `quote_form: verbatim` may **not** hold `status:
verifiable` or `verified` while `evidence_source` is `search-synthesis`,
`database-abstract`, or `none`. `scripts/okf_validate.py --strict` enforces this.

This is not stylistic caution. Asked for *Meditations* 10.3 in the George Long
translation, a web search returned a fluent answer that silently welded Long
together with an unrelated 18th-century translation and presented it as one
passage. Search fails *confidently*, which is the one failure mode a ledger
must never launder into evidence. Six of the nine defects recorded in
`the-stoic-husband`'s `quality/citation-defects.md` trace to this.

A search result may still fill a verbatim placeholder — as `status:
unverified` + `evidence_source: search-synthesis`, flagged for a real check.
What it may not do is claim the wording is confirmed.

## index.md and log.md (reserved files)

- **index.md** — the readable rollup. Carries `okf_version: "0.1"` and lists every
  concept grouped by type with one-line descriptions. This restores the
  skim-in-one-place quality the old `evidence-library.md` had (progressive
  disclosure: read the index, then open only the concepts you need).
- **log.md** — append-only history. Every command that writes concepts appends a
  dated line describing what changed.

## How each command/agent interacts with the bundle

| Command / Agent | Interaction |
|---|---|
| `book-source-prep` | Curates raw `sources/` → `frameworks/`, `stories/`, `citations/` concepts; cross-references candidate gaps against `03-outline.md` (not just existing OKF concepts) before flagging one; gaps become `citations` with `status: unverified` and a `gap_type` (`research` or `structural`); rebuilds `index.md`; appends `log.md`; calls out any new `structural` gaps in its check-in summary. |
| `book-chapter-research` / `researcher` | Reads `index.md`, resolves the current chapter's slug from `03-outline.md`, pulls concepts whose `chapter_slugs` match (plus topical `tags`), emits cross-links in `research.md`; creates `unverified` citations (`gap_type: research`) for new gaps; skips `gap_type: structural` gaps that aren't yet resolved. |
| `book-chapter-draft` / `chapter-writer` | Carries the backing citation path into placeholders: `[PLACEHOLDER: … — see /okf/citations/x.md]`. |
| `editor` | Resolves public placeholders and updates the citation concept (fills `resource`, `verification_note`, all three axes). Ceiling is `verifiable`, and only when `evidence_source` satisfies the transcription rule; a WebSearch-only resolution of a `verbatim` quote stays `unverified`. **Never sets `verified`** — Rule 11. Appends `log.md`. |
| `book-signal` | Emits each substantive reader response as a `Reader Signal`; GIFTs that answer a gap set `resolves:` and can advance a citation's `status`. |
| `book-human` / `argue` / `beta` / `tension` / `sweep` | Keep the human-readable report in `quality/`; also emit each actionable finding as a `QA Finding` concept (`status: open`). |
| `book-note` | Logs verbatim to `progress.md`; if the note asserts a framework/belief/evidence decision, also creates an `Author Note` concept. |
| `book-status` / `book-resume` | Report concept counts, unverified-citation count (excluding `superseded`), open `structural` gaps by name, and open-finding count. |
| `book-import` | Extracts evidence/frameworks/citations from imported content into concepts. |

## Conformance (OKF v0.1)

A bundle conforms if every non-reserved `.md` file under `okf/` has parseable YAML
frontmatter with a non-empty `type`. Reserved files (`index.md`, `log.md`) are
exempt. Consumers must not reject a bundle for missing optional fields, unknown
types, unknown keys, broken links, or a missing index.

## Future (documented, not yet built)

A shared cross-book bundle at `books/_shared/okf/` for durable frameworks reusable
across books (e.g., the Stoic cardinal virtues). Deferred: requires cross-bundle
link resolution in every consuming command. Per-book bundles only for now.
