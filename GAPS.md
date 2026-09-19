# Gaps

*What the old pipeline does that this house does not, recorded so it is deferred
rather than lost. Audited 2026-09-13 against all 40 `book-*` commands: **27
covered, 13 not.** The covered ones are mapped in `FLOW.md` and the roster table
in `CLAUDE.md`.*

A gap is listed with the **trigger** that should close it — the condition under
which building it becomes the right use of a session. Building any of these before
its trigger is building the least-validated part of the system furthest from the
current work.

---

## Now: built this pass

| Was missing | Now |
|---|---|
| `edit` — interactive chapter re-edit | `/gw-edit` — section by section, in session, then refreshes distillation, practice guide and plate |
| `note` — the author's own words into memory | `/gw-note` — notes and parked questions, his wording, real clock |
| `park` — a deferred question | `/gw-note park` — a revisit **trigger**, not a date; distinct from the inbox, which is what blocks a desk |

---

## Deferred: the PDF renderer, 1 gap, environmental

| Gap | What it waits on |
|---|---|
| The book's `chapter_pdf.py` cannot run in the cloud container | A container carrying weasyprint. (The migration in `#007` moved the script here; it did not bring the renderer's dependency.) |
| `books/<slug>/manuscript.md` and `manuscript.pdf` are the old pipeline's last compile and go stale from here | `/gw-compile` writing its whole-book output into the book tree with the coverage in the filename, and retiring these two |
| Desks still write to `runs/chNN/`; a chapter reaches `books/` only through `land.py` after the verdict ("switch 2" in `FLOW.md`) | A chapter landing that `land.py` could not do, or the apparatus/output split costing more than the landing-step defects it catches (two so far: #029's broken links, the round-1/round-2 brief choice) |

`weasyprint`, `pandoc` and `wkhtmltopdf` are all absent here and pip cannot reach
PyPI through the egress proxy, so the book repo's one renderer fails at the point
of use. `scripts/chapter_pdf_local.py` stands in, driving the headless Chromium
the container already has, and `scripts/package_check.py` guards what it emits.

**Registered because it was discovered at the point of use, twice.** The fallback
was also written from scratch rather than porting the book renderer's `markup()`,
which cost three formatting defects the author had already had fixed once. Whoever
closes this gap deletes the fallback rather than maintaining two.

---

## Deferred: the publication stack — 7 gaps, one trigger

**Trigger: the author approves the whole-book QA pass (`/gw-qa`) and says the book
is close.** Every one of these needs the finished arc, the QA findings, and the
callouts to be accurate. With 17 of 29 chapters unwritten, each would be built on
a book that does not exist yet — and `/book-marketing`'s own note says as much:
*"It requires the full arc, QA results, and callouts before it can be accurate."*

| Gap | Old command | What it produces |
|---|---|---|
| Whole-book positioning | `marketing` | Amazon description, taglines, comp titles, category strategy |
| Publisher pitch | `pitch` | Proposal and query letter |
| Publishing path | `publish-path` | Traditional versus indie, decided on evidence |
| Indie launch plan | `indie-plan` | KDP / IngramSpark strategy |
| Review strategy | `review-strategy` | ARC programme and early reviews |
| Book club guide | `club-guide` | Reading group materials |
| Substack integration | `substack-connect` | Pushing a drafted post to Substack, not just writing one |

**Substack, checked rather than assumed, 2026-09-19.** `ListConnectors` against this
session returns **zero** Substack connectors — there is no MCP credential attached
here at all, regardless of the shared trigger above. `book-manifest.json`'s
`integrations.substack.status: "connected"` does **not** mean this system can post:
read closely, it is the author's own publication existing at that URL, a business
fact carried over from the old pipeline's manifest, not a technical credential.
That old pipeline's own `scripts/pipeline_state.py` describes what a real
integration looked like: "the Substack MCP integration can push drafts but can't
read publish status back" — push-only, and even then the author confirmed what
was actually live, because self-reported "posted" status drifted. **Nothing here
changes `gw-publicist`'s mandate** ("nothing is ever posted, and publishing
decisions stay the author's") — closing this gap means a draft can be pushed to
Substack as a draft for the author to publish, never that this house posts
unattended. Until it is closed, a drafted post is copied out and posted by hand,
same as today.

**Owner when built: the Publicist.** Not seven skills — the old pipeline's shape.
One `/gw-publish` with a mode per deliverable, because they share their inputs (the
arc, the QA findings, the callouts, the positioning) and splitting them is how ten
marketing commands happened. The Publicist's mandate already forbids posting
anything; that does not change.

---

## Deferred: smaller, with their own triggers

| Gap | Old command | Trigger |
|---|---|---|
| The Introduction as "chapter zero" | `intro` | **Starting a new book.** It is not a numbered chapter: it is the author's own credibility and the misconception to defuse before Chapter 1, and it must not plant questions later chapters owe an answer to. The Stoic Husband's already exists. |
| Distillation refresh as a standalone | `distill --refresh` | **A bulk editing pass across many chapters.** `/gw-edit` already refreshes the chapter it touched; a fleet-wide refresh is a different job. |
| Switch active book | `switch` | **A second book exists.** The book repo's manifest already holds a registry keyed by path; the engine reads `bookRoot` from it, so this is a one-line change to `resolve_book.py` when it is needed, not a desk. |

---

## How this file stays honest

It is a point-in-time audit, so per standing rule 15 it states its basis: **40
`book-*` commands, audited 2026-09-13, 27 covered.** Re-run the audit when desks
are added or the old pipeline changes; an uncounted gap register is the
`citation-manifest.md` failure wearing a new name.

The Archivist reads this file under its "what was missing" lens. A gap the author
works around by hand more than once is a gap whose trigger has fired early, and
that is exactly the kind of thing the session review exists to notice.
