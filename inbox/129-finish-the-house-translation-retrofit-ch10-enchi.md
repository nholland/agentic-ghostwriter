---
id: 129
status: open
kind: parked
trigger: (1) his read of Ch10 or the laptop verification pass; (2) with the Lane C citations item; (3) next time /gw-verify is edited
aka: old-#35
raised_by: author
chapter: -
opened: 2026-09-10 02:33
---

# Finish the house-translation retrofit (Ch10 Enchiridion 30, Seneca 91 tail, the Gutenberg mirror route)

*Migrated 2026-10-04 from books/the-stoic-husband/parking-lot.md #35, still live after the 2026-10-03 triage (runs/qa/2026-10-03-parking-lot-triage.md). Triage note: (3) is partly done: the GITenberg mirror route and the Marcus and Epictetus ids are in .claude/agents/gw-factchecker.md; Seneca's id is not.*

**Question:** Finish the house-translation retrofit (`06-sources.md`): three items remain after the 2026-09-09 pass, plus a reachable primary-text channel that `/book-verify` should know about.
**Context:** On 2026-09-09 the author asked for the most modern public-domain translations to be found and applied; a parallel session had locked the same standard in `06-sources.md` two days earlier (Long for Marcus and Epictetus, Gummere for Seneca, Haines VI.8 in Ch2 as the one ratified exception). Every printed quotation in `06-sources.md`'s "Retrofit outstanding" table is now done except the Ch11 *Meditations* 4.49 row, which needed no swap because the chapter carries the idea without quoting it. Long's wording came from Project Gutenberg through its GitHub mirror: `https://raw.githubusercontent.com/GITenberg/<Title-Slug>_<id>/master/<id>.txt` (Marcus #15877, Epictetus #10661), which this container can reach even though gutenberg.org itself is blocked. The file's own `Translator:` line is what identifies the edition; #2680 is Casaubon and #45109 is Higginson, not Long or Carter as their titles suggest.
**Still open:** (1) Ch10 *Enchiridion* 30 prints Carter-style wording with no translator credited and should move to Long's XXX, but Long's "to submit when he is reproachful, when he inflicts blows" is harsher than the current line in a chapter about holding a boundary with a tired wife, so the swap needs the author's read. (2) Seneca *Letter* 91 §4's tail ("and we should consider, not what is wont to happen, but what can happen") is printed but not yet transcribed from a Gummere page; Lane C. (3) `/book-verify`'s Lane A should treat the GITenberg mirror as a Gutenberg route: `scripts/verification_probe.py` already probes raw.githubusercontent.com as a dev host, but nothing maps a Gutenberg id to its mirror URL, so the command cannot use it yet. A small table of ids for the house editions would make Long's texts Lane A from the cloud container.
**When to revisit:** (1) at the author's read of Ch10 or the laptop verification pass; (2) with parking-lot #32; (3) next time `/book-verify` is edited.
**Status:** OPEN, non-blocking.
