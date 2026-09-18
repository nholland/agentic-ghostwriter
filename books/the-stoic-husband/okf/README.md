# OKF Pilot — Assessment & Integration Notes

*A side project inside The Stoic Husband. Created 2026-06-14.*

> **Status note (updated 2026-06-14):** This document is the original *pilot
> assessment* — it describes the initial proof-of-concept (3 frameworks, 1 story,
> 2 citations) and the rationale for adopting OKF. It is **not** the current
> inventory. The bundle has since been fully migrated and is now the book's
> canonical knowledge layer (48 frameworks, 8 stories, 21 citations).
> For the current contents see [`index.md`](/index.md); for change history see
> [`log.md`](/log.md). Keep this file as the design rationale, not a file list.

This folder is a proof-of-concept that re-expresses part of the book's evidence
layer as an [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
bundle. It exists to answer three questions: **Is OKF helpful? Does it buy future
flexibility? How would it plug into the product?** Nothing in the existing
pipeline was changed.

---

## What OKF actually is (one paragraph)

OKF is a deliberately minimal convention for knowledge-as-markdown: a directory
of `.md` files, each with YAML frontmatter whose only required field is `type`,
a body that prefers structure (headings, tables) over prose, cross-links written
as ordinary markdown links (`/frameworks/x.md`), plus two optional reserved
files — `index.md` (a table of contents for progressive disclosure) and `log.md`
(a change history). Consumers must be *permissive*: never reject a bundle for
unknown fields, unknown types, or broken links. That's the whole spec. It is not
a database, not a taxonomy, not a replacement for our pipeline — it's a portable
shape for the knowledge we already keep.

## Why it fits this project specifically

Our `sources/` layer is *already* OKF in spirit — markdown knowledge in a git
repo. OKF just adds three things we don't currently have:

1. **Atomization** — one knowledge unit per file instead of one 290-line
   `evidence-library.md`. A framework, a story, or a citation becomes
   independently linkable, taggable, and movable.
2. **Typed frontmatter** — `type`, `tags`, `chapters`, `status`, `provenance`
   become queryable metadata instead of prose conventions a human has to parse.
3. **Cross-links as a graph** — a chapter's research can point at the exact
   evidence concepts it draws from, and a citation knows which chapters use it.

## Answering the three questions

### 1. Would it be helpful? — Yes, for the knowledge layer; no, for the manuscript.

The clear win is the evidence/research/citation layer. Concrete payoffs:

- **Provenance & the no-fabrication rule.** Every citation carries an explicit
  `status: verified | unverified | verifiable` field (see
  [gottman-four-horsemen.md](/citations/gottman-four-horsemen.md)). The "what
  still needs external research" list in `evidence-library.md` stops being a
  prose afterthought and becomes a queryable property of each source. This is
  CLAUDE.md Rule 3 enforced by structure, not memory.
- **Traceability.** When a chapter draft makes a claim, it can link to the
  concept that backs it. Reverse lookups become trivial: "which chapters depend
  on the Perel citation?" is answered by that file's `chapters` field, not a
  grep.
- **Agent efficiency.** Researcher/chapter-writer/editor sub-agents can read an
  `index.md` first (progressive disclosure) and pull only the concepts they
  need, instead of loading a monolithic library into context every time.

Where it does **not** help: the manuscript itself (`draft.md`, `refined.md`).
Forcing frontmatter and structural headings onto finished prose fights the voice
rules (CLAUDE.md Rule 4). OKF is for the knowledge *behind* the book, not the
book.

### 2. Does it give future flexibility? — Yes, and this is the strongest argument.

- **Portability.** "If you can `git clone` it, you can ship it." The evidence
  base becomes a tool-agnostic artifact you could hand to another writer, a
  different AI tool, or a future you, with zero lock-in.
- **Cross-book reuse.** When book #2 sparks, the durable Stoic frameworks
  (dichotomy of control, the cardinal virtues) can live in a *shared* OKF bundle
  that multiple books link into. The current flat-file model can't share cleanly.
- **Graceful growth.** Permissive consumption means a half-finished concept, a
  broken link to a not-yet-written piece, or a new custom field never breaks
  anything. The format is built for material that arrives messy and over time —
  which is exactly how feedback, interviews, and QA findings arrive.

### 3. How would it be incorporated into the product?

OKF is best understood as the **intake and evidence bus** for the pipeline. Every
stream that currently dumps into a prose file becomes a typed concept:

| Pipeline activity | Today | With OKF |
|---|---|---|
| **Source prep** (`/book-source-prep`) | appends to `evidence-library.md` | writes one concept per item under `frameworks/`, `stories/`, `citations/`; appends to `log.md` |
| **Chapter research** (`/book-chapter-research N`) | reads the whole library, writes `research.md` | reads `index.md`, pulls tagged concepts (`chapters: chNN`), and *links* the brief to them |
| **Author notes** (`/book-note`, interviews) | prose in `author-notes.md` | `type: Author Note` / `type: Author Anecdote` concepts with `disclosure` and `chapters` tags, instantly routable |
| **QA findings** (`/book-human`, `/book-argue`, `/book-beta`, `/book-tension`) | standalone reports in `quality/` | each finding a `type: QA Finding` concept linked to the chapter and the claim it challenges; status tracked open→resolved |
| **Reader feedback** (`/book-signal`) | dated files in `signal/` | `type: Reader Signal` concepts tagged to chapters, feeding back as evidence |
| **Citations / verification** | flagged in prose under "needs research" | first-class `type: Citation` concepts with a `status` field a script can audit |

The integration is incremental and low-risk:

- **Phase 0 (this folder):** prove the shape on real content. Done.
- **Phase 1:** point `/book-source-prep` at the bundle so new material lands as
  concepts. Existing commands keep working unchanged.
- **Phase 2:** teach `/book-chapter-research` to read the index and emit links,
  giving us claim→evidence traceability.
- **Phase 3:** route QA, reader signals, and author notes in as typed concepts so
  the whole feedback economy is one queryable graph.

At no phase does adopting OKF require a big-bang migration or touching the
manuscript.

## The honest risk

A format layer only pays off if something reads it. If we create concepts but the
commands never traverse them, it's dead metadata and pure overhead. So the
recommendation is **not** "convert everything now." It is: keep this pilot, and
adopt OKF only one phase at a time, each phase justified by a command that
actually consumes the structure.

## Recommendation

Adopt OKF for the **evidence/research/feedback layer only**, starting at Phase 1,
and leave the manuscript layer untouched. The portability and traceability are
real and compounding; the cost is bounded because the format is "just markdown
with a header." This pilot is the artifact to look at before deciding whether to
take Phase 1.

## What's in this pilot

```
okf/
├── index.md                         root table of contents (okf_version: 0.1)
├── log.md                           change history
├── README.md                        this assessment
├── frameworks/
│   ├── the-virtue-question.md       author IP — the daily tool
│   ├── attachment-vs-devotion.md    author IP — Stoic Romance
│   └── the-village-problem.md       author synthesis — links to Perel citation
├── stories/
│   └── sexless-and-roommates.md     audience signal — composite, links to village problem
└── citations/
    ├── gottman-four-horsemen.md     status: unverified
    └── perel-mating-in-captivity.md status: verifiable
```

All content is faithfully drawn from `sources/evidence-library.md` and
`sources/author-notes.md`. Nothing was invented.
