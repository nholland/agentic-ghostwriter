---
id: 117
status: open
kind: parked
trigger: every whole-book QA pass (/gw-qa), and whenever a gap's own trigger fires
aka: P-002
raised_by: author
chapter: -
opened: 2026-09-19 00:30
---

# Reach parity or beyond with the old pipeline before treating the migration as done

*Migrated 2026-10-04 from runs/parked.md (P-002); the id is kept as an alias.*

**Parked:** 2026-09-19 00:30
**Raised at:** this session, discussing the Playground → agentic-ghostwriter
migration's rationale and future evolution with the author.

**His words:**

> "Let's add the new items we should do, as well as Gaps, to the parking lot.
> We need parity or beyond on the new system."

**What this tracks, and what it deliberately does not duplicate:** `GAPS.md` is
already the live, trigger-based list of what the old pipeline could do that this
house cannot yet — the PDF renderer (environmental, waits on a container with
weasyprint), the seven-item publication stack (one shared trigger: the author
approves the whole-book QA pass and says the book is close), and three smaller
gaps each with their own trigger. As of this session it audited 27 of 40 old
commands covered, 13 not, 3 of those 13 closed this pass (`edit`, `note`, `park`).
Copying that list into this file would be the `citation-manifest.md` failure
again — two files claiming to be the same record, with nothing keeping them
equal. This item is the standing bar the gap list is measured against, not a
second copy of it.

**Revisit trigger:** every whole-book QA pass (`/gw-qa`), and whenever a gap's
own trigger fires in `GAPS.md` — check the closed gap against *this* bar
("parity or beyond"), not only against its own trigger, since closing a gap and
actually reaching parity are not automatically the same thing. Also revisit at
the next full command audit (the last one is dated 2026-09-13, predates the
migration) — the 40-command baseline was counted against the old pipeline before
it was frozen, and re-auditing after the freeze may turn up commands whose
correct answer changed once there was one repo instead of two.
