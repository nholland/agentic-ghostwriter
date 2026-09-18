# The Flow

*How a chapter moves through the house. Companion to `ARCHITECTURE.md`, which says
what lives where; this says what happens, in what order, and who touches it.*

---

## The one principle everything else follows from

**The brief is the automation boundary.** Upstream of a good research brief the
author must be in the room, because that is where the chapter's ideas come from.
Downstream of it, everything can run cold — a desk with clean context that never
read the conversation, gated by a script and by another desk. The test for whether
a brief is done is not tidiness: *could someone who never read the interview write
this chapter from this file alone?*

Established on Chapter 11 of The Stoic Husband. Its draft ran cold and came back
clean on every counted constraint. Its research could not have: five of eight
exchanges were the author correcting the brief, and four of the ideas the chapter
rests on exist only because he was there to say them.

Everything below is that principle made mechanical.

---

## Four cadences

| Cadence | What runs | Author present | Happens |
|---|---|---|---|
| **Foundation** | `/gw-found` — premise, archetype, voice, audience, outline | Throughout | Once per book |
| **Per chapter** | interview → research → draft → refine → verdict | Twice | 29 times |
| **Whole book** | `/gw-qa`, `/gw-verify`, compile | At the gate | A few times, late |
| **Publishing loop** | `/gw-market` | Approves, decides | Concurrent, per refined chapter |

The per-chapter cadence is the one the house is built around, and the only one
that has to be right 29 times.

---

## The per-chapter flow

```
  AUTHOR  ─┐
           │  1. /gw-interview N          The Developmental Editor, in session.
           │     └─ runs/chNN/interview.md   His words, his corrections, dated.
           │
  cold ────┤  2. /gw-research N           The Researcher builds the brief.
           │     ├─ gate: Ghostwriter plan-only review ("writable from this alone?")
           │     ├─ gate: okf_gate.py (citation bundle conforms)
           │     └─ runs/chNN/research.md + proposed concepts → author check-in
           │
  cold ────┤  3. /gw-draft N              The Ghostwriter writes.
           │     ├─ gate: voice_check.py   (counted rules, literal)
           │     ├─ gate: gw-specchecker   (clean-room: outline + prose, nothing else)
           │     └─ runs/chNN/draft.md with Draft Notes (declares metaphor family)
           │
  cold ────┤  4. /gw-refine N             The Line Editor sharpens.
           │     ├─ gate: voice_check.py   run INDEPENDENTLY of what the desk reported
           │     ├─ gate: gw-slopreader    (the qualitative half no script can count)
           │     ├─ gate: gw-specchecker   (refinement can break conformance)
           │     └─ runs/chNN/refined.md + distillation.md
           │
  cold ────┤  5. plate                     The Designer draws the mechanism.
           │     └─ runs/chNN/plate.svg     One image, the chapter's anchor metaphor,
           │                                the book's existing visual style. Never blocks.
           │
  script ──┤  6. /gw-compile N             The PDF readers actually receive.
           │     └─ gate: okf_gate.py, then the book repo's one renderer
           │
  AUTHOR  ─┘  7. The verdict              He reads. He says whether it landed.
                 └─ /gw-inbox              Everything a cold desk could not decide.
```

**One door for all of it: `/gw`.** `/gw 12` runs the sequence; The Publisher runs the sequence
and pauses at the interview, a short confirmation of content concepts, and the
verdict. Resumable from whatever stage the chapter stopped at. The desk-level
commands stay for re-running one stage.

**Two touches.** The interview and the verdict. Everything between runs without
him. That is the design's whole claim, and it is unproven until a chapter goes
through.

**Two rounds, then the inbox.** A cold desk that fails a gate is handed the gate's
output and revises, cold. Twice. On the third failure the pipeline stops and writes
an inbox item with the context he needs to rule without scrolling back. It never
loops, and it never resolves the question silently — the silent version was
recorded twice on the old pipeline before it was settled.

**Agents review agents.** No desk grades its own counted work. The skill re-runs
`voice_check.py` on the Line Editor's output regardless of what the Line Editor
reported, and **a discrepancy between the two is itself a finding.** Self-reported
counts were wrong on Ch9, Ch10 and the Prologue, once hiding a live violation.

**The checker is starved on purpose.** `gw-specchecker` receives the outline
section and the prose. Not the brief, not the notes, not which pipeline wrote it.
It catches what the producer cannot see because the producer knew what it meant
to write.

---

## The companion artifacts, and which desk owns each

The old pipeline accumulated seven artifacts outside the chapter flow. Four are
owned here; three were orphans and two of those are decisions, not gaps.

| Artifact | Ships to readers? | Owner here |
|---|---|---|
| `parts/part-N-*.md` — Part opening pages | **Yes**, inside the manuscript | `/gw-compile` emits them before each Part's first chapter |
| `appendix/practice-guide.md` — the accumulating field guide | **Yes**, as a companion | The Line Editor appends a section per chapter at refine |
| `visuals/*.svg` — one plate per chapter | **Yes** | The Designer |
| `sweep-report.md` — whole-book coherence | No, internal | `/gw-qa`, written to `runs/qa/<date>-qa.md` |
| `callouts.md` — pull quotes feeding marketing | No, feedstock | The Publicist, to `runs/marketing/callouts-ch01-chNN.md` |
| `tactics-review.md` — reader-facing practice companion | **Yes**, if kept | **Open** — overlaps the practice guide; merge or retire |
| `elevator-pitch.md` — the river/oak/sun triad | No, positioning | **Open** — names the five Parts; probably belongs in `00-premise.md` |

The two open rows are in the inbox. They are author decisions: inventing a desk
for an artifact that may simply be a duplicate is how a roster grows past its use.

## Where reader feedback goes

The author hands it to the Publisher through `/gw-signal N` and never has to pick
a desk. The Publicist logs each response as a signal concept (proposed, then
written). Then routing is by what the response *is*: a reader who got lost goes
to the Line Editor; an argued objection to the Reader Panel's Skeptic; a factual
challenge to the Fact-Checker; a gift — a story, a counter-example — to the
Developmental Editor, because it is the author's material now; an extension of
scope to the inbox, because only he decides scope. A reaction with no argument is
recorded and not routed: a pattern of them is data, one is a mood.

## Coherence across chapters

The old pipeline's `/book-sweep`, `/book-tension`, `/book-argue`, `/book-beta`
and `/book-human` were five whole-book reads. Here they are two desks under one
command, `/gw-qa`: the **Reader Panel** carries the Skeptic, the beta readers, the
tension reader and the **Continuity Editor** (the sweep — contradictions between
chapters, a mechanism renamed mid-book, a term used as established that nothing
defined, a callback to material the reader was never given); the **Anti-Slop
Reader** carries the cross-chapter patterns no per-chapter pass can see — the same
opening structure twice across Parts, anchor metaphors that contradict each
other. Both return findings; neither fixes. Disagreements between them are kept,
not averaged.

## The gates, and what each one is for

| Gate | Kind | Catches | Blocks? |
|---|---|---|---|
| `resolve_book.py` | Script | No book, missing constitution, missing dependency | Every desk |
| `okf_gate.py` | Script | Citation bundle violating the transcription rule; voice thresholds drifting from the spec | Every prose-writing skill |
| Plan-only review | Desk | A brief that cannot be written from cold | Draft |
| `voice_check.py` | Script | Em-dashes, bold, long-sentence share, you-density, metaphor family — by count | Draft, refine, market |
| `gw-specchecker` | Desk | Outline rows unmet; sources unnamed in prose | Draft, refine |
| `gw-slopreader` | Desk | Invented foils, indirection, windups, the wife as threat | Refine (findings routed, not auto-applied) |
| The inbox | Author | Anything a cold desk could not decide | Nothing — it collects |

A gate that cannot run **fails closed**. `okf_gate.py` blocks when it cannot find
the validator, and `voice_check.py` reports `SKIP` — explicitly not a pass — for a
metaphor family nobody declared. Nothing here reports a pass for something it did
not look at.

---

## Where things land

| What | Where | Written by |
|---|---|---|
| A chapter's apparatus: interview, brief, draft, conformance rows, notes, plate | `runs/chNN/` | the desks, cold |
| The chapter that ships: prose, distillation, brief, interview record, plate, its citation concepts, its practice-guide section | `books/<slug>/` | the Publisher, after the verdict, via `scripts/land.py`, as its own commit |
| The constitution (L4) | `books/<slug>/0*.md`, `sources/` | the Publisher, in session, on the author's word |
| Questions and rulings | `inbox/` | any desk raises; only he rules |
| Blind packets, for Ch1-11 only | `bakeoff/chNN/` | `bakeoff.py` |

Migration switch 1 (2026-09-18, inbox #007) moved the book into this repo and
froze the old pipeline's repo as an archive. The worst case for a failed
experiment is still a directory of prose nobody uses: nothing lands in `books/`
without a verdict, and `land.py` refuses to overwrite a chapter already there.
What was planned as switch 2 — desks writing straight into the book tree — is
registered in `GAPS.md`, not done: the apparatus/output split has caught real
defects at the landing step and is kept on purpose.

---

## What is cold and what is not, and why it cannot be otherwise

A sub-agent cannot ask the author anything. That is not a limitation to work
around; it is the dividing line.

| Runs in session (as the Publisher) | Runs cold (dispatched) |
|---|---|
| `/gw-interview` — the ideas come from him | `gw-researcher` — assembles, never decides |
| `/gw-found` — every artifact is a claim about what he thinks | `gw-ghostwriter` — executes a brief |
| `/gw-revise` — regeneration would erase history | `gw-lineeditor` — sharpens, flags judgement calls |
| `/gw-inbox` — his rulings, in his words | `gw-specchecker`, `gw-slopreader`, `gw-panel` — read-only reviewers |
| The verdict | `gw-factchecker` — up to `verifiable`, never beyond |
| | `gw-publicist` — drafts, never posts |

---

## Sessions, branches, and landing on main

None of this is a desk. It is two hooks and a script, because the incident record
is unambiguous: every git failure was a model following rule text, and every fix
was a check that ran on its own.

| Moment | What runs | Does |
|---|---|---|
| Session start | `session-start.sh` | On `main` in a remote session → creates `session/<stamp>` from origin/main. Behind → fast-forwards. Diverged → says so, touches nothing. Then the clock, the book, the board. |
| Session stop | `session-stop.sh` | Commits **work paths only** (`runs/`, `bakeoff/`, `inbox/`, `FINDINGS.md`). Appends a derived entry to `runs/log.md`. Pushes a `session/` branch so nothing is stranded (never `main`). Then, once per session, asks for the Archivist's review. |
| Author says "land it" | `sync.py --land` | Fast-forward only. Refuses if diverged. Prints the branch and the sha. |
| Anytime | `sync.py --status` | Which branch, ahead/behind main, unpushed, uncommitted. `/gw` shows the same line. |

Rule files are **not** auto-committed. Editing the rules is a deliberate act the
author should see as its own commit.

`runs/log.md` is the engine's session memory and it is derived, never typed: the
real clock, the branch, the files that changed, and NEXT_ACTION from the oracle.
It cannot carry a wrong date or a stale "next" — the two ways the old
`progress.md` failed. What it cannot carry is the author's own words; those stay
where he said them, in `runs/chNN/interview.md` and on each inbox resolution.

## The session review, which is not optional

Once per session that touched the work, the Stop hook asks the Publisher to
dispatch the Archivist. It reviews through five lenses — **what broke, what was
missing, what was too hard, what worked, what recurs** — assesses whether each
is a one-off or a pattern, and suggests only if necessary: a rule edit, a new
desk or skill, a check with a caller, a deletion, a simplification. The old
hook's two questions survive inside the first lens, in order: *which existing rules did we violate or
ignore, and why?* and only then *what is worth promoting into a rule?* Findings go
to `FINDINGS.md`, which is an incident archive, not a ruleset. Additions are
net-zero: a proposed rule must name what it replaces.

Rule-file paths are deliberately not watched. When they were, editing the ruleset
counted toward the threshold that triggered the next rule-editing retrospective — a
loop with no damping that grew the old ledger from 739 to 6,026 words in 27 days
and spent five of nine sessions on pipeline maintenance instead of the book. **A
retrospective is triggered by writing, not by its own output.**

The retrospective is run by a desk, the **Archivist** (`gw-retro`), cold, when the
hook fires. It reads the range, answers the three questions, and reads all of
`FINDINGS.md` for a failure *shape* recurring — six defects in one week shared one
shape. It **proposes and never applies**: the author approves every change, and
every addition names a deletion. That is the difference between a house that
learns and one that edits its own rules until nobody can find them.

For this house there is a third question the old pipeline never had to ask: *did
a cold desk decide something silently that should have gone to the inbox?* The
two-touch design fails in exactly one hard-to-notice way, and that is it.

---

## From the author's side

*The designed experience. No chapter has been through it yet.*

You open a session on the engine repo. The hook prints the real clock, the book
it found, and what is waiting on you. You type `/gw`. It shows you what is next
and what is waiting. You type `/gw 12`, or just say what you want in plain words.
That is the whole instruction.

**You are needed three times.** The interview — a conversation with the
Developmental Editor about the chapter, where your corrections are the product.
A short confirmation after research — *here is what the Researcher thinks you
think*, each proposed concept with its wording; yes, no, or a fix. The verdict —
a PDF, the plate, the counts as the scripts printed them, the conformance rows,
and the inbox. You read. You say whether it landed.

**What you never do.** Pick a desk: feedback, questions and chapters all go to the
Publisher. Run a stage: `/gw-draft 12` exists for a deliberate re-run, not the
normal path. Estimate a count: every number came from a script, pasted verbatim.
Read a draft twice: gates and reviewers read it before you do. Decide something a
desk resolved on its own: if it was yours, it is in the inbox. Open the book repo
by hand, unless you are editing the outline yourself.

**When a desk gets stuck.** It gets the gate's output back and revises without
you, twice. The third failure stops the chapter and writes an inbox item. The old
pipeline's failure mode was the silent version — a desk that could not decide
picked an answer and kept going — and parking item #28 recorded it twice before it
was settled.

**When readers write back.** `/gw-signal 12` and paste what they said. The
Publicist logs each response; the Publisher routes it by what it is — a lost
reader to the Line Editor, an argued objection to the Skeptic, a factual challenge
to the Fact-Checker, a gift to the Developmental Editor because it is your
material now, new scope to the inbox because only you decide scope. A reaction
with no argument is recorded, not routed.

**Where things live.** The book never moves. Today the engine reads the book repo
and writes only to its own `runs/`, so nothing it does can damage the book.
Migration is one write arrow changing destination, then the old commands retiring.
Which repo do you go to? *Is this about this book, or about how books get made?*

A day with the house: open a session, say the chapter number, talk for a while,
confirm a short list, walk away, come back to a PDF. When readers respond, paste
what they said. When you are lost, `/gw`. When something is waiting on you,
`/gw` again. That is the entire surface.
