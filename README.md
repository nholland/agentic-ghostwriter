# The Agentic Ghostwriter

The engine half of a Level 3 book production house. The book itself stays in
`Playground-260420`; this repo holds the desks, the scripts, and the gates.

**Status: the cold half is built and unproven.** No desk has drafted a chapter.
Stage 0's counted script is built and calibrated (see `FINDINGS.md`).

---

## The boundary, which is the whole point

| Lives here | Lives in `Playground-260420` |
|---|---|
| Desk definitions (`.claude/agents/gw-*.md`) | The book: premise, voice, outline, OKF bundle |
| Desk commands (`.claude/skills/gw-*/`) | Every `refined.md` that ships |
| Scripts and gates (`scripts/`) | `progress.md`, `parking-lot.md`, the manifest |
| Shadow-run outputs (`runs/chNN/`) | The working pipeline, untouched |
| Bake-off packets (`bakeoff/chNN/`) | — |

**Nothing here ever writes inside the book repo.** That is enforced by
instruction in every skill and is the reason the two systems can run at once.
The book is read-only input to this repo.

`config/house.json` holds the path to the book and every counted threshold,
each one transcribed from `01-voice.md` with its source quoted. No threshold in
this repo was invented.

---

## Why the commands are named `gw-`

Two mechanical facts about how Claude Code loads things:

1. **Skills namespace cleanly.** A plugin skill is `/gw:draft`; a project skill is
   `/book-chapter-draft`. Both stay available — one does not shadow the other.
   That is what lets the two pipelines coexist in one session.
2. **Agents do NOT.** Project and user `.claude/agents/` definitions *override*
   same-named plugin agents. An agent here called `editor` or `researcher` or
   `chapter-writer` would be silently replaced by the playground repo's version,
   and a bake-off would quietly test the old desks while reporting on the new
   ones. Every agent here is prefixed `gw-` so that collision cannot happen.

The `gw-` prefix on the *skills* is belt-and-suspenders: in a cloud session the
repo is attached and its `.claude/` loads directly, with no plugin namespace to
lean on. The prefix makes the names safe either way.

### Loading it

- **Cloud / web session** (the usual case): attach this repo to the session. Its
  `.claude/` skills and agents load on the next turn.
- **Local CLI, for development:** `claude --plugin-dir ./agentic-ghostwriter`
- **Later, to distribute:** `.claude-plugin/plugin.json` is already here; the
  plugin layout wants `skills/` and `agents/` at the repo root rather than under
  `.claude/`, which is a `cp -r` when that day comes. Canonical copies stay in
  `.claude/` because that is what the author's actual sessions load.

---

## Running the bake-off

The design doc's migration plan proposed proving each desk on a real chapter.
That still holds, but it cannot mean running the author's interview twice: a
second interview already knows the first one's answers, and it is his most
expensive time. So the two halves are tested separately.

### Experiment 1 — Ch12 shadow run (tests the cold half)

Chapter 12 ships on the **old** pipeline as normal. Then this one re-runs it cold
from the *same* `research.md`, into `runs/ch12/`.

```
/gw-draft 12        # Ghostwriter, gated by brief review + voice_check + conformance
/gw-refine 12       # Line Editor, gated by voice_check + conformance, re-run independently
/gw-bakeoff 12      # blind comparison packet
```

Author cost: zero extra. Risk to the book: zero — the shipped chapter is the old
pipeline's, and nothing here writes into the book repo.

What it measures: whether the cold stages, with agents reviewing agents, match or
beat the current draft-plus-five-editing-passes on the same brief.

What it cannot measure: the interview. Ch12 is also a soft test — 1,000–1,300
words, low research burden. If the result is close, run the shadow again on a
meatier chapter before concluding anything.

### Experiment 2 — Ch13 lead run (tests the warm half)

The Developmental Editor desk leads the interview. The measurement already has a
baseline: Ch11's brief took **five rounds** of author correction, and four of the
ideas the chapter rests on exist only because he was in the room. Fewer rounds to
a brief that passes the Ghostwriter's plan-only review is the result worth having.

That desk is not built yet. It is next, and it is deliberately after the cold half
is proven, because a desk that interviews badly costs the author time directly.

### The blind read

`scripts/bakeoff.py` writes `variant-1.md` / `variant-2.md`, a counted comparison
labelled by variant rather than by system, and a sealed mapping. The author reads
cold and fills in `verdict.md`; the script refuses to unseal until he has. He is
the judge and also the person who wants the new system to win, so the blind is
protecting the measurement from the judge's preference, which is ordinary good
practice and not a comment on him.

---

## Scripts

| Script | Does |
|---|---|
| `scripts/voice_check.py` | The counted voice rules by literal count. Separates HARD facts from CAND candidates a regex cannot decide, and reports SKIP — explicitly *not* a pass — for anything it could not check. |
| `scripts/bakeoff.py` | Builds the blind comparison packet; refuses to unseal before the verdict is written. |

`voice_check.py` exists because self-reported counts were wrong on Ch9, Ch10 and
the Prologue, once hiding a live violation. Its first run found two bugs in
itself, both caught by checking its output against a number that was already
known. See `FINDINGS.md`.

---

## What is deliberately NOT here yet

- **The Developmental Editor and Researcher desks.** Experiment 2.
- **The corpus collapse.** The design doc's Stage 5 targets ~23,000 words against
  the current ~83,000. It is the most satisfying item on the list and the most
  dangerous to do on a clean repo, because the corpus is large for a reason: Rule
  9 exists because of two dating incidents, Rule 11 because nine citation defects
  reached printed prose, Rule 15 because of a bulk-edit near-miss. A fresh start
  makes it frictionless to write an elegant system that silently drops the rules
  that only exist because something broke. The collapse happens last, in the book
  repo, with the migration ledger — after desks have shipped real chapters.
- **Any change to the playground pipeline.** None. That repo is untouched.

## Migration, when the bake-off earns it

Three switches, each independently reversible:

1. **Reading** — the book repo stays the source of truth for book content forever.
   This never changes.
2. **Producing** — `/gw-*` writes into `{bookRoot}/chapters/` instead of `runs/`.
   One path change per skill.
3. **Defaulting** — the old `/book-chapter-*` commands are retired, with the
   migration ledger mapping every deleted rule to the desk or script now
   enforcing it.

Nothing is retired before its replacement has shipped a real chapter the author
approved. Until switch 2, the worst case for a failed experiment is a directory
of prose nobody uses.

---

*Design of record: `docs/AGENTIC-PUBLISHING-HOUSE.md` in `Playground-260420`,
written 2026-09-09. Parked there as item #34. This repo builds it in stages and
records what actually happened in `FINDINGS.md`.*
