---
description: The Publicist desk identifies a refined chapter's publishable concepts and drafts Substack posts and social teasers from them. Drafts only - nothing is ever posted. Use after a chapter is refined.
---

<!-- DERIVED FILE - DO NOT EDIT.
     Canonical copy: .claude/skills/gw-market/SKILL.md
     Regenerate: python3 scripts/sync_plugin_layout.py -->
# /gw-market — the Publicist

Argument: a chapter number, optionally `--all`. `$ARGUMENTS`

**Nothing this command produces is published.** It drafts. The author decides when
and whether anything goes out, and you never imply something has been posted.

## Step 0

`python3 scripts/resolve_book.py`. Require a refined chapter — either
`{bookRoot}/chapters/chNN/refined.md` or this pipeline's `runs/chNN/refined.md`.
**Say which one you are working from.** Drafting social copy from a shadow-run
chapter the author never approved is how an unapproved draft reaches an audience.

## If he asked for callouts, not a chapter

`/gw-market callouts` is the whole-book pull-quote pass: dispatch `gw-publicist`
over every refined chapter, output to `runs/marketing/callouts-ch01-chNN.md` with
the coverage in the filename. Then stop; the rest of this skill is per-chapter.

## Step 1 — concepts first

Dispatch `gw-publicist` to identify the chapter's 4–6 publishable concepts and
return them as a list, **before** drafting anything. The list is its own
deliverable; he chooses from it. Do not draft all of them unprompted.

## Step 2 — draft what he picked

Funnel: social (3–4 sentences) → Substack (400–600 words) → the book. Single
posts, not threads.

Short-form rules are **stricter** than chapter rules, not looser: the same count
of metaphor repetitions reads far denser in 500 words than 2,500, and the bold and
rhetorical-device caps still apply.

## Step 3 — counted gate on every piece

```
python3 scripts/voice_check.py <file> --short-form --metaphor-family "..."
```

Paste the output. Short-form is where these caps break most easily and where the
author is least likely to re-read closely.

## Step 4 — citation gate

Any Stoic quotation in a post must be at least `verifiable` with an
`evidence_source` that is not a search. The transcription rule does not relax
because the audience is social. Run `python3 scripts/okf_gate.py`.

## Step 5 — check in

Per concept, show him the draft and get a response before saving. Then state
plainly what he must approve before anything is posted, and that nothing has been.

Write to `runs/marketing/chNN/`. Never into the book repo.
