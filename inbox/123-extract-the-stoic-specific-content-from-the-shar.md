---
id: 123
status: open
kind: parked
trigger: before the framework is reused for a second book
aka: old-#9
raised_by: author
chapter: -
opened: 2026-07-08
---

# Extract the Stoic-specific content from the shared desks so the framework is portable

*Migrated 2026-10-04 from books/the-stoic-husband/parking-lot.md #9, still live after the 2026-10-03 triage (runs/qa/2026-10-03-parking-lot-triage.md). Triage note: Seven desk and skill files and config/house.json (stoic_terms, mirrored voice thresholds) still name Stoic things. Same coupling as scripts/switch_book.py's voice-mirror warning.*

**Question:** Extract the Stoic-specific content baked directly into shared `.claude/commands/` skill files, so the agentic book-writing framework stays portable to a non-Stoicism book.
**Context:** Surfaced during the Ch2 Substack retrospective (2026-07-08, see `.claude/LEARNINGS.md`). `book-substack.md`'s Voice Constitution hardcodes: *"Light Stoic tie-in — required... every post should contain at least one earned connection to Stoic thinking."* The mechanism — every post needs one earned tie-in to whatever the book's organizing tradition/frame is — is durable across books; naming Stoicism specifically is not. The intended seam already exists: `04-archetype.md` is documented in `CLAUDE.md` as the "genre profile" file for exactly this kind of book-specific-but-structured content. Fix would be: (1) audit `book-substack.md` and other command files for other hardcoded Stoic-specific language beyond the tie-in line, (2) move the specific tie-in requirement (and anything else found) into this book's `04-archetype.md`, (3) reword the shared command file(s) to reference `{bookRoot}/04-archetype.md` generically instead of naming Stoicism directly.
**When to revisit:** Before this framework is reused for a second book — not blocking any current Stoic Husband work.
**Status:** OPEN, non-blocking, deferred.
