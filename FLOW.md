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

**One handle for all of it: `/gw-chapter N`.** The Publisher runs the sequence
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

| While both pipelines run | After migration switch 2 |
|---|---|
| `runs/chNN/` in the engine | `{bookRoot}/chapters/chNN/` in the book repo |
| `bakeoff/chNN/` blind packets | — |
| `inbox/` | `inbox/` |
| The book repo untouched | The old commands retired (switch 3) |

Until switch 2, the worst case for a failed experiment is a directory of prose
nobody uses. The book repo cannot be damaged by anything the engine does, because
no engine skill is permitted to write there — with one scoped exception,
`/gw-found` authoring a book the engine itself created.

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

## The retrospective, which is not optional

Every twelve commits that touch the work — `runs/`, `scripts/`, `config/` — the
Stop hook asks two questions, in order: *which existing rules did we violate or
ignore, and why?* and only then *what is worth promoting into a rule?* Findings go
to `FINDINGS.md`, which is an incident archive, not a ruleset. Additions are
net-zero: a proposed rule must name what it replaces.

Rule-file paths are deliberately not watched. When they were, editing the ruleset
counted toward the threshold that triggered the next rule-editing retrospective — a
loop with no damping that grew the old ledger from 739 to 6,026 words in 27 days
and spent five of nine sessions on pipeline maintenance instead of the book. **A
retrospective is triggered by writing, not by its own output.**

For this house there is a third question the old pipeline never had to ask: *did
a cold desk decide something silently that should have gone to the inbox?* The
two-touch design fails in exactly one hard-to-notice way, and that is it.
