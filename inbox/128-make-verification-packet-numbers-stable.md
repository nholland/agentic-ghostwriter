---
id: 128
status: open
kind: parked
trigger: before the next verification packet generation
aka: old-#33
raised_by: author
chapter: -
opened: 2026-09-10
---

# Make verification-packet numbers stable

*Migrated 2026-10-04 from books/the-stoic-husband/parking-lot.md #33, still live after the 2026-10-03 triage (runs/qa/2026-10-03-parking-lot-triage.md). Triage note: Not fixed as of 2026-10-03: scripts/verification_packet.py has no stable-id logic.*

**Question:** Fix `scripts/verification_packet.py` so packet numbers are stable, and decide what to do about the three packet/result pairs already orphaned.

**The bug.** The script numbers packets by splitting *whatever is still outstanding* into chunks of eight, starting from 1. So every regeneration renumbers everything. `packet-01.md` today is not the `packet-01.md` that `results-01.json` was produced from — it now lists `cloud-townsend-boundaries` and `epictetus-discourses-2-18`, while `results-01.json` answers `brown-clear-is-kind` and `epictetus-discourses-3-16`. Same for 02 and 03. `packet-06.md` was deleted outright when the remaining set shrank.

**Where it came from.** Commit `7b2d4d9` (2026-09-04), *"chore: regenerate verification packets after Tier 1 completion"* — a routine regeneration that silently rewrote the record of work already done. Not a mistake anyone made; the script is built this way. It was found again on 2026-09-07 when a read-only run of the script clobbered the same three files, which was reverted.

**Why it is not urgent.** Nothing depends on the mapping. The evidence that matters — edition, locator, wording, surrounding context, verdict — lives in each citation's own `# External Verification` block, which is durable and correctly attributed. What is lost is only the audit trail of *which packet produced which answers*.

**Why it is still worth fixing.** This is the same defect class as the retired `citation-manifest.md`: a file that presents itself as a record while nothing keeps it true. A future session comparing `packet-02.md` against `results-02.json` would draw wrong conclusions and have no way to know it.

**Scope if built:** derive packet ids from content (a hash of the slug set) or make them append-only against a small persisted ledger, so regeneration adds new packets rather than renumbering existing ones. Roughly an hour. The already-orphaned 1-3 mapping probably cannot be reconstructed — the honest fix there is a note in `sources/verification/README.md` recording that packets 1-3 and their results predate stable numbering and should not be cross-referenced.

**When to revisit:** Before the next packet generation, i.e. before the Lane C work in #32 runs via the packet path. Not blocking if that work runs from the laptop instead, since Lane A never builds a packet.
**Status:** OPEN, non-blocking.
