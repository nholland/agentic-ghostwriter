# Findings

One honest row per experiment. A bake-off that only records wins is decoration.

---

## 2026-09-12 — Stage 0: `voice_check.py` validated against the existing corpus

Before any desk ran, the counted-rules script was calibrated against chapters
whose numbers were already reported, then run across the refined corpus.

**Calibration against Ch11** (reported: 2,828 words, em-dashes 0, long sentences
5.6%, you-density 47.7, door family 2.1/1,000):

| Measure | Reported | Script | Note |
|---|---|---|---|
| Prose words | 2,828 | 2,833 | within 5; hyphenate/possessive tokenisation |
| Em-dashes | 0 | 0 | match |
| Long-sentence share | 5.6% | 5.8% | sentence-split variance |
| You-density | 47.7 | 43.1 | consistent direction; denominator likely differs |
| Door family / 1,000 | 2.1 | 2.8 | prefix matching catches more conjugations |

Ch09 and Ch11 pass every HARD check, which is what their "clean by count" reports
claimed. The script agrees with the record where the record was right.

**Two findings where it does not agree.**

1. **`you-density` is below its floor on three artifacts.** Floor is 40 per 1,000
   (added 2026-07-23 after Ch8 ran at 28). Measured: **ch01 33.0, prologue 30.5,
   introduction 30.8**. All three are below a counted floor and none was flagged.
   The likely cause is the same class as the wife's-mood rule that sat on an
   unpushed branch for five weeks: the floor arrived after ch01 was written, and
   nothing back-scanned the artifacts that predated it. Worth a pass.

2. **The bold cap fails every numbered chapter, and the chapters are not wrong.**
   `01-voice.md` caps bold at one genuine pull-quote per piece. Every numbered
   chapter uses bolded run-in section headers (`**No door.**` alone on its line
   after a divider): ch01 has 5, ch05/ch10/ch11 have 5, ch09 has 4. Prologue and
   Introduction have none. This is a convention the spec never contemplated, not
   eleven defects. The script now counts only *inline* bold against the cap and
   reports run-in headers separately as needing an author ruling — it does not
   exempt them silently, because loosening a counted rule is the author's call.
   Under that split, **ch01 still has 4 genuine inline bolds against a cap of 1.**

**Two defects found in the script itself, both by checking its output against a
known number rather than trusting it.** It first reported Ch11 at 4,325 words and
a "164-word sentence": the apparatus splitter cut each `Editor's Notes` section
individually and resumed counting at the next heading, letting ~1,500 words of
conformance tables back in, and markdown table rows were being counted as
sentences. Prose now ends at the *first* apparatus heading, one boundary, and
table rows are dropped. The general lesson is the compile word-count lesson again:
a counting bug does not error, it just returns a plausible number.

**Status:** no desk has drafted anything yet. Ch12 shadow run is next.

---

## 2026-09-12 — V1 roster wired; three defects found in this repo's own tooling

All ten desks now exist, the two author-facing ones as session modes rather than
sub-agents (a sub-agent cannot ask the author anything, which is the constraint the
architecture is built around). Shared context resolved **by reference**: a copy of
the book was ruled out as the `citation-manifest.md` failure at repo scale.

**The citation-gate regression, found and closed.** The first version of this
repo's `gw-refine` ran no citation check at all, while the book pipeline's
`/book-chapter-refine` and `/book-compile` both run `okf_validate.py --strict` as
a *blocking* gate before writing prose. For a day this replacement pipeline was
**less safe on citations than the pipeline it replaces**, in the exact area where
nine defects reached compiled prose, six of them printed. `scripts/okf_gate.py`
now wraps the book repo's own validator — wraps, not reimplements, because two
validators would drift — and fails closed when it cannot find it. Wired as
blocking into `gw-draft`, `gw-refine`, `gw-research`, `gw-verify` and `gw-market`.

**The hardcoded book path.** `config/house.json` originally held
`../Playground-260420/books/the-stoic-husband`, which resolved only because two
repos happened to be cloned as siblings with those exact names in one session.
Replaced by `scripts/resolve_book.py`: discovery, then validation of every required
artifact, then a non-zero exit that stops every desk. Both the discovery fallback
and the total-failure path were tested, not assumed. The reason this mattered more
than it looks: a skill reading a missing voice spec does not crash, it writes
generic prose.

**`claude plugin validate` caught a bug in the mirror script.**
`sync_plugin_layout.py` prepended a DO-NOT-EDIT banner to each derived file, which
put it *above* the YAML frontmatter — so the frontmatter was no longer at the top
of the file and `description` stopped parsing. Every mirrored skill would have
loaded without the metadata that makes it findable, and nothing would have
errored. The banner now goes after the frontmatter block, and `--check` detects
drift (verified by tampering with a file and confirming exit 1).

Three defects, all three the same shape as the two in the previous entry: **a
plausible wrong answer that raises no error.** None was found by reading the code.
Each was found by running something that could disagree — a known number, a probe,
a validator.

**Two items seeded into `inbox/` from the previous entry's findings**, as the real
first test of whether the inbox holds what the author would want to rule on:
#001 whether bolded run-in section headers are legal, #002 the three artifacts
below the you-density floor.

**Still unproven:** every desk. Nothing here has drafted a chapter.

---

## 2026-09-12 — Dependency audit: this repo is an add-on, not a system

Prompted by the author's question: *if we accidentally lost the playground folder,
what would we lose?* Answered empirically rather than by reasoning. Full model and
tables in `ARCHITECTURE.md`; the findings that changed the picture:

**Four of the book repo's scripts are engine code, not book content, and this repo
calls them by name.** `okf_validate.py`, `citation_queue.py`,
`verification_probe.py`, `pipeline_state.py`. Losing the book repo would make
`okf_gate.py` fail closed permanently, stopping every prose-writing skill. The
dividing line between the two repos is supposed to be book-specific versus
book-agnostic, and these four sit on the wrong side of it. Recorded as open; the fix
is to *move* them, never to copy, since two validators drift.

**Nothing here serves the Foundation phase.** The book repo has 41 commands; this
repo has 10 skills, and all ten serve the per-chapter phase. There is no
`/gw-spark`, `/gw-voice`, `/gw-audience`, `/gw-outline`. Every cold desk *reads* the
premise, voice, audience and outline; **no desk writes any of them.** So this system
can continue a book and cannot start one, which makes "publishing house" an
overstatement until the Developmental Editor's foundation half exists.

**Personas were already covered, by accident rather than design.** Both reader
personas are sections inside `02-audience.md`, not separate documents, and three
desks already read that file. Worth recording because the question "are personas
handled" had a yes answer that nobody had verified.

**`config/house.json` was a derived file with nothing deriving it — the
citation-manifest.md failure, committed inside a repo whose README cites that
failure three times.** Eight counted thresholds were transcribed by hand from
`01-voice.md`. Had the author raised the you-density floor in the spec,
`voice_check.py` would have gone on enforcing 40 forever and reported PASS.

Fixed as far as it honestly can be: each threshold now carries a `spec_probe` regex
that must still match `01-voice.md`, `voice_rules_check.py` asserts all eight, and
`okf_gate.py` calls it so the check has a caller. Full derivation is not possible —
the spec states its thresholds in prose, and parsing prose into numbers would layer
a new guess on the old one — so the check proves the *source wording* is still
present and fails loudly when it is not. Verified by tampering with one probe and
confirming the gate blocks.

**Artifacts with no desk:** `callouts.md`, `elevator-pitch.md`,
`tactics-review.md`, `sweep-report.md`, `parts/`, `appendix/`, `visuals/`. Several
are real discovered artifacts that earned their place. Not lost, but not served.

**Still unproven:** every desk. Nothing here has drafted a chapter.

---

## 2026-09-12 — Plan corrected on the author's challenge; Foundation phase built

The author approved moving the shared tooling and building the Foundation desks, and
questioned the third recommendation. Both halves of that were right to question.

**"Extract the book into its own repo" was muddled and is withdrawn.** The book repo
already *is* the book repo; once the engine leaves, that is all it is, and nothing
needs extracting. It also already scales to more books — `books/<slug>/`, a registry
keyed by path in the manifest, `/book-switch`, `/book-spark` detecting an existing
`bookRoot`. Book two is a folder, not a repository. What that recommendation was
actually reaching for was retiring the legacy pipeline, which is migration switch 3
and was already written down elsewhere. **Two repos, permanently.**

**Moving the shared scripts would have broken the pipeline still shipping chapters,
and this was not checked before recommending it.** The book pipeline makes 16 calls
to `python3 scripts/*.py` across 8 command files, relative to its own root, and
`.claude/OKF.md` is read by 8 more commands plus an agent. With 16 of 29 chapters
left, moving them breaks `/book-chapter-refine` and `/book-compile`.

Broken down by actual caller, "L2" is not one block: `okf_validate.py` is genuinely
shared (3 book callers, 1 here); `pipeline_state.py` has 5 book callers and 0 here;
`chapter_pdf.py`, `verification_packet.py` and `verification_ingest.py` have none
here at all. Each sits with its current primary caller, so none is misplaced yet.
Copying would create drifting validators; pointing the book pipeline at the engine
would invert the dependency so losing the engine breaks the book. Both worse than
today.

**So the coupling is now explicit and checked rather than moved.**
`config/house.json` declares all eight book-repo dependencies with reasons, split
required from optional; `resolve_book.py` verifies each at session start. A missing
required one blocks every desk; a missing optional one names the unavailable feature.
Verified by adding a fake required dependency and confirming exit 1.

**The Foundation phase surfaced a genuine conflict.** Every other skill is forbidden
from writing inside the book repo, but Foundation must write L4 somewhere. Resolved
by scope, not by exception: `/gw-found` authors in place only for a book this engine
created; for a book with a locked foundation that another pipeline ships it **reports
and refuses**, and `/gw-revise` produces a diff for the author to apply there. The
Stoic Husband is that case. A second system authoring its premise is precisely how
two sources of truth start.

`/gw-found`, `/gw-revise` and `/gw-sources` now cover roughly ten of the old
commands. `/gw-revise` carries the rule that revision is not regeneration: `01-voice.md`
pairs most rules with the incident that produced them, and regenerating it deletes
that history silently.

**Still unproven:** every desk. Nothing here has drafted a chapter.


---

## 2026-09-13 — Five questions, one finding about the visuals

**Compile and PDF** are now `/gw-compile`, wrapping the book repo's single
renderer (`chapter_pdf.py`) rather than writing a second one. The old compile once
had two copies of the same stylesheet that shipped the same two defects with only
one fixed; the skill says so and carries the word-count-delta check that caught the
1,700-word silent drop.

**Reader feedback** arrives through `/gw-signal` to the Publisher, who routes by
what the response is. The author never picks a desk.

**Cross-chapter coherence** was already covered — the old sweep is the Reader
Panel's Continuity Editor persona, the cross-chapter slop patterns belong to the
Anti-Slop Reader, both under `/gw-qa` — but nothing said so. Now `FLOW.md` does.

**The one-agent handle** is `/gw-chapter N`: the Publisher runs a chapter end to
end with three pauses. This is the practical difference between Level 3 and Level
4 in this house: Level 3 is the desks and their gates, which the author still drives
stage by stage; Level 4 is the author stating the outcome once. Both are now
present, and the stage commands stay for deliberate re-runs.

**A Designer desk exists, and the visuals it is meant to match mostly do not.**
The author remembers "a whole bunch of design elements" he liked from a few sessions
ago. The repo has exactly one: `visuals/ch01-distillation.svg`, committed
2026-08-17, an 800×420 mechanism diagram in an implicit house style (near-black,
amber, slate, system sans). `git log --all` confirms nothing else was ever
committed. The others lived in a conversation and were never saved — the same
class as the wife's-mood rule stranded on an unpushed branch, with no branch to
recover from. `gw-designer` treats the one survivor as the style standard and
proposes a written `visuals/style.md` for the author to ratify rather than
inventing one.

**Still unproven:** every desk. Nothing here has drafted a chapter.

---

## 2026-09-13 — One door: `/gw`

The author asked for the simplest possible surface: type `/gw` and whatever he is
thinking, and one agent works out the rest; `/gw` alone shows a short menu. Built
as a router skill the Publisher follows — a bare number runs that chapter, plain
words map to a desk by an intent table, nothing matched gets one clarifying
question and the menu, never a guess into an action that spends his time.

**"Next" comes from a script, not from the model.** The book repo's Rule 10 —
`/book-resume` takes NEXT_ACTION from `pipeline_state.py` and the model may not
compute it from files or reasoning — is the rule that held when others did not.
`scripts/next.py` is this house's equivalent: first match wins across parked
chapters, unread bake-off packets, chapters in progress, the lowest unstarted
chapter, then QA. `/gw` shows its answer; `/gw-chapter` resumes from it.

**Its first run gave a plausible wrong answer.** "0 shipped on the book pipeline"
and "start at chapter 1" for a book with eleven numbered chapters refined. Cause:
`resolve_book.py` reports directory names (`ch01`), and the oracle checked
`name.isdigit()`, which matched nothing. Same shape as every other defect in this
ledger — no error, a number that looks fine — and caught the same way, by running
it against the real repo where the right answer was already known. The comment in
the script now records this so the next reader does not "simplify" it back.

**Still unproven:** every desk. Nothing here has drafted a chapter.
