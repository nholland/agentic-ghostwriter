# Gaps

*What the old pipeline does that this house does not, recorded so it is deferred
rather than lost. Re-audited 2026-09-13 against all 40 `book-*` commands, by
deliverable rather than by keyword (the first audit's loose grep claimed 34 of
40; checking for the actual outputs found 27): **40 covered, 0 deferred.** Two
are covered by a view rather than a desk, and one by an inventory rather than
an integration; each is named below so nobody mistakes coverage for parity.*

---

## Closed 2026-09-13

| Was missing | Now | Note |
|---|---|---|
| `marketing`, `pitch`, `publish-path`, `indie-plan`, `review-strategy`, `club-guide` | `/gw-publish <mode>` | One skill, one desk (the Publicist), because the six share every input. The skill states the arc's coverage before producing anything and puts it in the filename. |
| `substack-connect` | `/gw-publish channels` | **An inventory, not an integration.** It lists what posting channels exist and what the author would need to supply to connect one. The old command performed the connection (cookie extraction); this house makes no connection on his behalf. If he wants a channel wired, that is a deliberate act with a name, not a side effect of a marketing skill. |
| `intro` | `/gw-found intro` | Interviewed like a chapter, written for a book this engine owns, a diff otherwise; revised with `/gw-edit introduction`, never regenerated. |
| `distill --refresh` / `--all` | `/gw-refine --distill-only NN` / `--distill-all` | The fleet-wide refresh after a bulk edit. |
| `switch` | `resolve_book.py --list-books`; `--book <slug>` / `$GW_BOOK_SLUG` | **A view, not a write.** The old command rewrote the manifest's `bookRoot`; this house never writes the book repo's manifest, so the switch is per session and the manifest's active book stays what the book pipeline set. |
| `feedback` for `prologue`, `introduction`, `part[N]` | `/gw-edit prologue` / `introduction` / `part-N` | Chapters were already covered by `/gw-edit`; the three hand-authored artifacts now are too. |
| `park --review` / `--close` | `scripts/parked.py` | The first `/gw-note park` appended to a file nothing read again. |
| `orchestrate`'s cross-chapter parallelism | `/gw-floor` | The old orchestrator could not run here (unattended sub-agents). The floor dispatches only what `next.py --floor` lists, in one turn, and parks a chapter rather than looping. |

## Still true, by design

- **`/gw-found` refuses to write a book another pipeline ships.** The Stoic
  Husband's foundation is the book pipeline's; `/gw-revise` produces a diff.
  Not a gap: the alternative is two sources of truth for a premise.
- **The engine never writes `book-manifest.json`.** Stage state for a shadow run
  is derived from `runs/` by `next.py`. At migration switch 2 the design's
  `stage_done.py` becomes the one writer, in this repo. Until then a chapter
  the house refined is "refined here", never "refined" in the book's registry.
- **Four production scripts still live in the book repo** (`okf_validate.py`,
  `citation_queue.py`, `verification_probe.py`, `chapter_pdf.py`, plus the
  packet loop). Declared in `config/house.json`, verified at session start,
  wrapped rather than copied. They move when the legacy pipeline retires.

## How this file stays honest

It is a point-in-time audit, so per standing rule 15 it states its basis: **40
`book-*` commands, audited 2026-09-13 by deliverable, 40 covered.** Re-run the
audit when desks are added or the old pipeline changes; an uncounted gap
register is the `citation-manifest.md` failure wearing a new name.

The Archivist reads this file under its "what was missing" lens. A capability
the author works around by hand more than once is a gap this file failed to
record, and that is exactly the kind of thing the session review exists to notice.
