---
description: The Developmental Editor desk interviews the author about a chapter and writes the interview record that the Researcher builds the brief from. Runs in session with the author, never as a sub-agent. Use before any drafting of a chapter.
---

<!-- DERIVED FILE - DO NOT EDIT.
     Canonical copy: .claude/skills/gw-interview/SKILL.md
     Regenerate: python3 scripts/sync_plugin_layout.py -->
# /gw-interview — the Developmental Editor, with the author in the room

Argument: a chapter number. `$ARGUMENTS`

**This desk runs as you, in session. Never dispatch it to a sub-agent.** A
sub-agent cannot ask the author anything, and this stage is nothing but asking.
The chapter's ideas come from him here or they do not exist.

## Step 0

`python3 scripts/resolve_book.py` — stop if it fails. Then read
`{bookRoot}/00-premise.md`, `01-voice.md`, `02-audience.md`, the chapter's section
of `03-outline.md`, `04-archetype.md`, and `05-framework.md` if present (this
chapter's Traceability cell). Read `okf/index.md` and grep it for anything already
captured on this chapter's theme — do not ask him for material the bundle already
holds.

## Why this stage cannot be automated

A cold pipeline cannot ask the author anything, and every chapter interviewed so
far has produced material nothing else could have supplied: on Ch11, five of
eight exchanges were him correcting the brief; on Ch12, round 2's five questions
produced five rulings that changed the chapter's central story and its central
claim (`runs/ch12/interview.md`, Provenance). See `FINDINGS.md` for the running
record, one entry per chapter — a single pinned example goes stale the moment a
later chapter makes a stronger one. Treat every one of his corrections as the
most valuable output of the session, not as friction.

## The interview

Open with what the outline already commits the chapter to, so he is reacting to
something concrete rather than facing a blank page. Then work the gaps. Useful
shapes:

- The specific memory behind the outline's story slot. **Never invent this.** The
  story is his; a plausible substitute is the worst thing you can produce here,
  because it reads fine.
- Where his own experience contradicts the outline's premise. That contradiction
  is usually the chapter.
- The thing he believes about this that he has not seen written anywhere.
- What a reader would get wrong after one pass.
- Which of the outline's key points he now thinks is wrong. Outlines are revisable
  and this is the cheapest moment to revise one.

**Push back once on anything that sounds like a received idea** rather than his
own. One round, not an interrogation. Record the round either way (Rule 10).

## Step 2 — write the record

`runs/chNN/interview.md`: what was asked, what he said, **in his words**, and
every correction with what it changed. This file is the Researcher's only access
to him, so a paraphrase that loses his phrasing loses the chapter's voice.

Stamp it with the real clock: `date '+%Y-%m-%d %H:%M'`.

## Step 3 — outline revisions

If he changed the commission, say exactly what changed and propose the edit to
`{bookRoot}/03-outline.md` — **as a proposal.** This skill does not write to the
book repo. He applies it, or tells you to hand it to the old pipeline.

## Step 4 — check in, then hand off

Show him the record. Ask what is missing. Only when he is satisfied:

`/gw-research NN`
