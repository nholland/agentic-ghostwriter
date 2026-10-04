---
id: 127
status: open
kind: parked
trigger: a session on the author's laptop, where there is no egress proxy
aka: old-#32
raised_by: author
chapter: -
opened: 2026-09-09
---

# Close the Lane C verbatim citations (needs a laptop session)

*Migrated 2026-10-04 from books/the-stoic-husband/parking-lot.md #32, still live after the 2026-10-03 triage (runs/qa/2026-10-03-parking-lot-triage.md). Triage note: The count of 22 is stale: scripts/citations.py reported 141 citations, 137 open, on 2026-10-04. Recount at the time.*

**Question:** Close the 22 Lane C verbatim citations — the word-for-word quotations whose wording has never been checked against an actual page.

**Context:** These are `quote_form: verbatim` citations already sitting in `manuscript.md`. A wrong quotation in printed prose is a wrong book, which is why they are the highest-risk set in the ledger. They are Lane C **only because of where the work has been happening**: this repo's cloud container routes through an egress proxy that blocks Standard Ebooks, Wikisource, Project Gutenberg, archive.org, PubMed and every author-hosted PDF. Verified 2026-09-07 — `curl` and `WebFetch` agree, and both are blocked for every scholarly and literary host.

**Why this is smaller than it looks.** On the author's laptop there is no proxy, and the house translations settled 2026-09-07 — Long for Marcus and Epictetus, Gummere for Seneca — are all public domain and freely readable on exactly the hosts that are blocked here. Run `/book-verify` from the laptop and `scripts/verification_probe.py` detects the difference automatically: most of these 22 become **Lane A**, meaning the page is opened and the wording transcribed directly, `evidence_source: page-text`. No ChatGPT session, no packet, no pasting results back.

**The packet path stays as the fallback it was designed to be.** `scripts/verification_packet.py` builds a text packet for an outside session with browsing. That is the right tool when the laptop is not available; it is not the default.

**What this does NOT get to.** Nothing here reaches `status: verified` — CLAUDE.md Rule 11 reserves that for the author against his own copy. Lane A closes the *wording* question with page evidence and stages the edition and locator so the author's own check is a thirty-second confirmation instead of an afternoon.

**Known live items inside this set:** the seven quotations dropped from `verifiable` to `unverified` on 2026-09-08 by the transcription rule; the suspected *Letter* 81 splice (defect #11); and the two already-known `DIFFERENT_WORDING` defects at `Enchiridion` 1 and *Meditations* 4.49.

**What `/book-verify` actually does when you run it — read this first, you will not remember.**

You type `/book-verify`. Nothing else. Everything below happens without you.

1. **It checks what your machine can reach** (`scripts/verification_probe.py`) — it
   does not assume, and it does not trust anything written in an earlier session,
   because the answer is different on the laptop than in the cloud.
2. **It picks the riskiest citations first** — the word-for-word quotes already
   sitting in the manuscript. A wrong quotation in printed prose is a wrong book.
3. **It opens the real pages** and transcribes what they actually say, with the
   edition, the section number as that source numbers it, and enough surrounding
   text to prove it was on the right page.
4. **It shows you what it found before writing anything** — and if a source says
   something different from what the book says, it tells you side by side and
   changes nothing. Broken quotes get reported to `quality/citation-defects.md`;
   fixing the prose stays yours.
5. **It never marks anything confirmed.** That is yours alone, against your own
   copy — Rule 11. What this does is stage the edition, locator and exact wording
   so your check takes thirty seconds instead of an afternoon.

Work happens 8 at a time, with a check-in between batches. Stop whenever; the
ledger is always in a consistent state.

**If the laptop is not available:** `/book-verify` detects that too and builds a
text packet instead, which it pastes into the chat for you to drop into ChatGPT or
Claude with browsing on. Bring back whatever it returns, in any format, and paste
it here — no files, no JSON, no commands. That is the fallback, not the plan.

**When to revisit:** Next session run from the author's laptop. Nothing blocks in the meantime — the compile gate (`okf_validate.py --strict` in `/book-compile` Step 4.4) already prevents any of these from being presented as confirmed, and the ledger currently states their status honestly.
**Status:** OPEN, non-blocking.
