# Layers

*Written 2026-09-12, in answer to: "if we accidentally lost the playground folder,
what functionality and context and artifacts would we lose?" That question is a
dependency audit, and the audit is below. The short answer is that this repo is
currently an **add-on to the book repo, not a system** — it can refine a chapter of
a book that already exists, in a repo that still exists.*

---

## The seven layers

The author's instinct was four: *the agentic layer, the book-specific artifacts,
phases like beginning-versus-per-chapter, and structured items that don't change
structurally but do change in content, like OKF.* That is right, and splitting two
of them makes the ownership question answerable.

| # | Layer | Changes when | Book-specific? | Should live in |
|---|---|---|---|---|
| **L0** | **Harness** — Claude Code: skills, agents, hooks, plugin loading | Anthropic ships | No | Neither repo |
| **L1** | **The House** — the ten desks, their gates, the orchestration | The method improves | No | **Engine** |
| **L2** | **Production tooling** — validators, state oracles, probes, compile, PDF | A mechanic is fixed | No | **Engine** |
| **L3** | **Format contracts** — the OKF schema, manifest schema, `chNN/` layout, frontmatter rules | A format changes | No | **Engine** |
| **L4** | **Book constitution** — premise, voice, audience + personas, outline, archetype, framework, sources | Phase 1, then rarely | **Yes** | Book |
| **L5** | **Book knowledge** — the OKF bundle, 185 typed concepts | Continuously, per chapter | **Yes** | Book |
| **L6** | **Book output** — chapters, manuscript, marketing, quality reports | Per chapter | **Yes** | Book |
| **L7** | **Book memory** — `progress.md`, `parking-lot.md`, manifest state | Every session | **Yes** | Book |

**The dividing line is L3/L4, and it is not where the files currently sit.** L2 and
L3 are book-agnostic code and spec, and both live in the book repo today. That is
the whole reason this repo cannot stand alone.

L5 is the layer the author identified precisely: **structurally stable, continuously
changing in content.** The OKF *schema* is L3 and belongs to the engine; the 185
concepts are L5 and belong to the book. Keeping those two apart is what lets a
second book reuse the format without inheriting this book's evidence.

---

## Phases are a property of L4–L6, not a layer

Phase is *when* an artifact is produced, and it maps onto the layers rather than
sitting beside them:

| Phase | Produces | Layer | Cadence |
|---|---|---|---|
| Foundation | premise, voice, audience, outline, archetype, framework, sources | L4 | **Once per book** |
| Per chapter | interview, brief, draft, refined, distillation | L5 → L6 | **29 times** |
| Whole book | QA reports, manuscript, callouts | L6 | A few times, late |
| Continuous | OKF concepts, citations, progress, parking lot | L5, L7 | Always |

This matters for what to build next: **every desk in this repo serves the
per-chapter phase.** Nothing here serves Foundation. A book cannot be started with
this system, only continued.

---

## If the book repo disappeared tonight

### Lost permanently — nothing here holds a copy

| What | Scale | Layer |
|---|---|---|
| The outline | 29 chapters with premise, takeaway, key points, story slot, Stoic lesson, ah-ha, word target and transition each | L4 |
| The voice constitution | every Never Do rule, the counted rules, the incident history behind them | L4 |
| Premise, audience + both reader personas, archetype, framework, source policy | 6 hand-authored documents | L4 |
| The OKF bundle | **185 concepts** — 89 citations, 75 frameworks, 12 stories, 6 signals | L5 |
| Refined chapters | **13**, plus drafts, research briefs and distillations | L6 |
| Parts pages, appendix, marketing, signal, quality reports, manuscript | ~90 files | L6 |
| `progress.md` | every session's decisions and the author's own words | L7 |
| `parking-lot.md` | open questions #32–#35 and their resolution history | L7 |

This is the irreplaceable column. None of it is reconstructible from this repo, and
most of it is not reconstructible at all — the outline "took a lot of initial work"
and the 185 concepts are the accumulated record of what the author actually thinks.

### Lost but rebuildable — engine code sitting in the wrong repo

| Script | What breaks here without it |
|---|---|
| `okf_validate.py` | **`okf_gate.py` fails closed permanently.** Every prose-writing skill stops. |
| `citation_queue.py` | `/gw-verify` cannot regenerate the author's queue |
| `verification_probe.py` | `/gw-verify` must guess reachability — the one thing it is told never to do |
| `pipeline_state.py` | `/gw-board` loses the book pipeline's state oracle |
| `chapter_pdf.py`, `verification_packet.py`, `verification_ingest.py` | No verdict PDF, no external verification loop |

Four of these are called by name in this repo's skills. **They are L2 — engine, not
book content — and they are the real coupling.**

### Survives

The ten desks, seven scripts (`resolve_book`, `okf_gate`, `voice_check`,
`voice_rules_check`, `inbox`, `bakeoff`, `sync_plugin_layout`), the gate wiring,
`CLAUDE.md`, the SessionStart hook, `FINDINGS.md`.

### Capability gap, counted

The book repo has **41 commands**; this repo has **10 skills**. Nothing here covers:

- **The entire Foundation phase** — `spark`, `voice`, `audience`, `outline`,
  `archetype`, `source-prep`, `intro`, `import`. A new book cannot be started.
- **Compile and PDF** — `compile`, and no verdict package.
- **Session memory** — `resume`, `status`, `note`, `park`, `switch`, `feedback`.
  `/gw-board` reads state; it writes no memory, and this repo has no `progress.md`
  of its own.
- **Per-chapter extras** — `distill` as a refresh tool, `edit`, `signal`.
- **Most of publishing** — `pitch`, `publish-path`, `indie-plan`,
  `review-strategy`, `club-guide`, `substack-connect`.

---

## The author's three questions, answered

**1. Which agent gathers the premise documents?**

**None does, today.** Per the design's roster the Developmental Editor owns
"premise, voice, audience, outline, archetype, framework" — but only its
chapter-interview half is built (`/gw-interview`). There is no `/gw-spark`,
`/gw-voice`, `/gw-audience`, `/gw-outline`. Every cold desk *reads* L4 and no desk
*writes* it. For the shadow run that is fine, because the foundation already
exists. For a second book it is the blocking gap.

**2. Are we providing structures around voice?**

Partly, and the split is worth naming:

- **Counted rules** — structured in `config/house.json`: eight thresholds, each
  with the quote it came from and a `spec_probe` regex. `voice_check.py` enforces
  them; `voice_rules_check.py` proves the config still agrees with `01-voice.md`
  and `okf_gate.py` calls it, so the check has a caller.
- **Qualitative rules** — structured only as prose, in `gw-slopreader`'s mandate.
  That is correct: they are judgement calls, and a regex claiming to decide them
  would be worse than a desk reading for them.
- **The voice spec itself** — **unstructured and ungenerated here.** `01-voice.md`
  is hand-authored in the book repo with 200-plus lines of rule-plus-incident. No
  desk produces it, no schema constrains it, and that is the largest piece of L4
  this repo does not model.

**3. Will the new system use the artifacts we discovered along the way?**

It reads most of L4 and L5 already: `00-premise`, `01-voice`, `02-audience`
(**including both reader personas — they are sections inside that file, not
separate documents**), `03-outline`, `04-archetype`, `05-framework` conditionally,
`06-sources`, and `okf/`. It does **not** touch `callouts.md`,
`elevator-pitch.md`, `tactics-review.md`, `sweep-report.md`, `parts/`,
`appendix/`, or `visuals/` — several of which are real discovered artifacts that
earned their place and currently have no desk.

---

## What to do about it

Three moves, in dependency order. None is urgent for the Ch12 shadow run, which
works precisely *because* both repos are present.

**1. Move L2 and L3 into the engine repo.** The eight production scripts and the
OKF format spec are book-agnostic. While they live in the book repo, this repo is
an add-on. Do this by *moving*, not copying — two validators drift, and that is the
failure this whole repo keeps citing. Until then, `resolve_book.py` at least makes
the dependency explicit and loud rather than silent.

**2. Build the Foundation half of the Developmental Editor.** Without it the
system continues books but cannot start one, which makes "an agentic publishing
house" an overstatement.

**3. Then extract the book into its own repo.** Once L1–L3 are in the engine and
L4–L7 are the only things left, the split is clean and mechanical rather than a
judgement call about each file.

The ordering is deliberate: extracting the book first would leave the engine
scripts stranded with the content, which is the position we are in now.

---

## Standing rule this produces

> **Any artifact that is not specific to one book belongs in the engine repo, and
> any artifact specific to one book belongs in the book repo. Where one is in the
> wrong place, say so in writing rather than letting the coupling go unrecorded.**

`config/house.json` was the first violation found: eight thresholds copied by hand
from `01-voice.md`, a derived file with nothing deriving it. Fixed with a probe per
threshold and a gate that calls the checker. The four L2 scripts are the second,
and they are still open.
