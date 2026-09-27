# OKF reconciliation: approved inbox 070–100

Recorded 2026-09-27T15:07:00.780871-05:00. Branch: session/inbox-audit-2026-09-25.

Authority: “Okay, let's continue, please make the changes” following the proposed
explicit OKF completion contract, workflow integration, and mechanical check.

## House change

Replaced Rule 9 (53 words removed) with a knowledge capture and reconciliation
contract. Clarified gw-note's author-invoked command restriction (33 words replaced)
so it cannot be mistaken for a ban on automatic OKF capture. Added shared completion
instructions to interview, research, chapter, edit, revision, feedback, note and
inbox workflows; regenerated plugin mirrors and the manual.

Inbox closure and automatic proof reconciliation require a disposition receipt.
Chapter landing requires a receipt covering current run prose and distillation;
force cannot bypass it. Stop and sync require receipts covering changed book
Markdown and run interviews, compared with upstream or main, including committed,
staged and untracked files. Each receipt cites authority, reason and (for knowledge
dispositions) concept paths. Hashes identify the artifact version reconciled.

Limits: this checks recorded coverage, not semantic truth or completeness. The
Publisher must read and reconcile contradictory knowledge. Raw git pushes bypass
the check. Earlier changes outside the comparison window require an explicit audit
or --since. Historical resolved inbox items are not reopened; legacy ruled items
need a receipt before automatic completion and display that requirement.

## Knowledge backfill

- 094: exact 1991/1995/2003 chronology replaces the ambiguous 23-years-together claim.
- 070/084/095: nail/apology/hole mapping, accumulation caption and courage-to-return mechanism.
- 096: prohairesis wording and Chapter 6 practical meaning.
- 097: repair placement, next-chapter promise and qualified silence consequence;
  retained temperament framework now explicitly distinguishes relevance from coverage.
- 100: effort may require apology; no guaranteed reciprocal response.
- 098/099: scope approved, exact wording pending; proposals remain unapplied and items open.
- 045: feedback preservation/routing is an engine workflow change, no new book claim.
  Other tooling-only changes and declines do not become author beliefs.

Five existing framework concepts were reconciled; one Author Note records authority,
accepted meanings and pending exclusions. Index annotations were preserved (one row
added); log history was appended. Receipt: runs/reconciliation/2026-09-27-approved-inbox-knowledge.json.

## Validation

```text
233/233 fixtures pass
okf_reconcile: PASS — 8 changed file(s) covered; semantic completeness requires Publisher review.
okf_index: index.md agrees with the bundle (77 frameworks, 12 stories, 122 citations, 6 signals).
PASS — bundle conforms (warnings above are non-fatal).
okf_gate: PASS - the caller may write prose.
```

Existing citation warnings retain their evidence status. No manuscript prose changed
in this backfill. The previous Prologue/Chapter 1 voice-density failures are not
claimed fixed. Mirror/manual checks and git diff --check pass.
