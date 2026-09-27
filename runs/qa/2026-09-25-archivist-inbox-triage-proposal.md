# Proposed Archivist Inbox triage — 2026-09-25

Publisher proposal, prepared in session; not a cold Archivist finding. No rule changes applied. The author approved the current audit and asked whether the Archivist should do this periodically; this file makes the possible change reviewable without treating that question as an adopted mandate.

**Recommendation:** Incorporate triage into existing batched and end-of-session reviews. Keep the Publisher accountable for the readable Inbox and follow-through. Do not add an independent recurring automation or another desk.

**Evidence:** inbox.py currently reports 56 open records and one ruled record. The complete audit routes all 57 once and identifies four superseded requests and three partly completed requests. The desk currently reads only items opened or closed this session; that misses old unresolved entries. The current hook already batches at three watched-path commits following resolved #092.

**Exact replacement:** `.claude/agents/gw-retro.md`, the Inbox bullet under Read. Before applying, also inspect the mirrored desk definition and use the repository’s synchronization procedure. This does not authorize changing that file now.

Replace:

```text
- Inbox items opened or closed this session, with their resolutions in the author's words.
```

With:

```text
- Inbox items opened or closed this session, plus pending items whose evidence,
  dependencies, or authorization changed. On the existing batched or end-of-session
  review, group related items; check for stale questions, completed work, and
  already-authorized implementation. Recommend evidence-backed closures without
  inventing author rulings. Return only live decisions in plain language, each
  with context and one recommendation. The Publisher maintains the Inbox and
  carries out authorized work; this triage creates no separate review trigger.
```

**Measured word cost** (`wc -w` on the exact two blocks):

```text
      15 /tmp/inbox-audit-old-bullet.txt
      73 /tmp/inbox-audit-new-bullet.txt
      88 total
```

One desk definition replaces 15 words with 73, net +58. Any mirrored copy carries the same change; repository-wide duplication cost has not been measured. No other text is proposed for deletion.

**Deletion scope:** One existing bullet only; retain all original Inbox records, resolutions, evidence, and the rest of the desk brief. The replacement retains attention to this session’s changes and broadens it to affected pending work. This is a rule-edit proposal, not a new Inbox question about another rule-edit proposal.

**Acceptance:** A future review with an old superseded request identifies the current evidence and recommends retirement; an already-authorized task is routed to implementation; an unresolved biographical or editorial choice remains with the author. It must not mark a proposal approved merely because some code or a weak completion command already passes. Do not use a grep of this wording as proof of effective triage.

**Status:** Proposed, not scheduled or applied. Covered by the existing author gate in CLAUDE.md Rule 17. No separate full retrospective was commissioned or performed.
