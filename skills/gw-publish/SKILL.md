---
description: The Publicist's whole-book publication stack in one command with a mode per deliverable - positioning, pitch, path, indie, reviews, club, channels. Replaces seven old commands that shared every input. Drafts only; nothing is posted or submitted.
---

<!-- DERIVED FILE - DO NOT EDIT.
     Canonical copy: .claude/skills/gw-publish/SKILL.md
     Regenerate: python3 scripts/sync_plugin_layout.py -->
# /gw-publish — the publication stack

Argument: a mode, optionally `--coverage` to state the arc's completeness first. `$ARGUMENTS`

Modes: `positioning` · `pitch` · `path` · `indie` · `reviews` · `club` · `channels`.
Bare `/gw-publish` lists them with what each produces and what it needs.

One command, not seven, on purpose: every deliverable here reads the same
inputs (the arc, the QA synthesis, the callouts, the audience map) and splitting
them is how the old pipeline ended up with ten marketing commands.

## Step 0

```
python3 scripts/resolve_book.py
python3 scripts/okf_gate.py
```

Both blocking. Then **state the coverage before doing anything**: how many
chapters are refined of how many planned, whether `/gw-qa` has run, whether a
callouts file exists (`runs/marketing/callouts-*.md` or the book repo's). The
old `/book-marketing` said it plainly: positioning needs the full arc, the QA
results and the callouts to be accurate. If the arc is incomplete, say so, say
what will change when it completes, and **put the coverage in every output
filename** (`positioning-ch01-ch11.md`), per standing rule 15.

## The modes

| Mode | Produces | Author input needed first |
|---|---|---|
| `positioning` | Amazon description, taglines, comp titles, category and keyword strategy, back-cover copy | none; reads the book |
| `pitch` | Book proposal and query letter | the platform facts only he knows (list size, prior publications) |
| `path` | Traditional vs. indie, decided on evidence with the reasoning shown | his answers on timeline, control, platform, revenue goals |
| `indie` | KDP and IngramSpark plan, pricing, launch sequence, first ninety days | `path` decided indie |
| `reviews` | ARC and early-review programme | `positioning` |
| `club` | Reading-group guide: questions per Part, exercises from the practice guide | the manuscript |
| `channels` | Inventory of posting integrations and what each needs from him to connect | none; makes no connection |

Where a mode needs his input first, **ask before dispatching** - a cold desk
cannot, and a plan built on a guessed platform size is a plan he will not use.

## Dispatch

Dispatch `gw-publicist` in the named mode with the inputs the table names.
Name the desk. It drafts; it never posts, submits, connects, or implies any of
those happened.

## Gates

Every reader-facing line of copy gets the counted check:

```
python3 scripts/voice_check.py <file> --short-form --metaphor-family "<the book's anchor images>"
```

Paste it. Any Stoic quotation in copy obeys the transcription rule exactly as in
the book. No invented figure anywhere: a comp title's sales, a category's size,
a review count are either sourced and cited in the file or absent.

## Check in, then save

Show him the deliverable. Get a response. Write to `runs/marketing/<mode>-<coverage>.md`
(or `runs/pitch/` for `pitch`). Never into the book repo.

Then say plainly what he must decide or approve before anything leaves the
building, and that nothing has.
