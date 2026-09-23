# Findings

One honest row per experiment. A bake-off that only records wins is decoration.

**Still unproven: every desk, the Archivist included.** Nothing in this house
has drafted a chapter. That line stood at the foot of nine entries; it belongs
once, here, until it stops being true.

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



---

## 2026-09-13 — Session management and learning: hooks and a proposing desk, not agents

The author asked whether to add a Session Agent for git and the manifest, and a
Learnings Agent that recursively improves the system. The incident record answers
both, and the answer is the same: **no agent — hooks, scripts, and one desk that
proposes and never applies.**

**Git.** Every git failure in `LEARNINGS.md` was a model following rule text: the
sync block copied into twenty skills with eighteen wrong; a session 13 commits
behind main that bypassed the freshness guard by hand; a branch scan that reasoned
about commit counts and misreported four branches until it diffed actual trees. The
confusion the author actually reported was simpler than any of them: not knowing
whether "pushed" meant the session branch or main. So the engine now has what the
book repo's hooks proved: `session-start.sh` handles branches (session/ branch from
main, fast-forward when behind, hands off when diverged); `session-stop.sh` commits
**work paths only** and writes a derived `runs/log.md`; `sync.py` does push,
merge-main and a fast-forward-only land, and prints the branch by name every time.
Rule files are deliberately not auto-committed.

**The manifest** does not need managing yet: the engine reads the book's manifest
and may not write it, and its own state is derived from artifacts by `next.py`.
The question returns at migration switch 2, and the answer then is `stage_done.py`
from the design doc — a script.

**Session memory** is `runs/log.md`, appended by the Stop hook from git and the
oracle. It cannot carry a wrong date or a stale "next" — the two ways
`progress.md` failed. The author's own words stay where he said them.

**Learning.** A system that recursively improves itself is the loop the retro hook
was redesigned to break: the old ledger grew from 739 to 6,026 words in 27 days
when retrospectives fed on their own output, and five of nine sessions went to
maintenance instead of the book. The safe version is the **Archivist**
(`gw-retro`): dispatched cold when the hook fires, it answers the three questions,
reads all of `FINDINGS.md` for a recurring failure *shape*, and proposes — every
addition paired with a deletion, preferring a check with a caller over rule text.
It never edits a rule. The author does, or nobody does.



**Seventh same-shape defect, in the script built to remove ambiguity.**
`sync.py --status` reported "0 ahead, 0 behind" and "branch not on origin" for
`main`, which was on origin. `git branch -r` was empty: this repo was cloned while
the remote was empty, and an empty clone never writes `remote.origin.fetch`, so no
fetch ever created `refs/remotes/origin/*`. Every `rev-list --count ...origin/main`
errored, and `int(behind or 0)` turned the error into zero. The session-start hook
had the same hole and would have fast-forwarded against nothing.

Fixed in three places with one principle: **unknown is rendered as unknown, never
as 0.** `sync.py` and the hook now write the standard refspec when it is missing
and fetch; a missing `origin/main` prints UNKNOWN and makes `--land` refuse;
`next.py`'s branch line says "vs main: UNKNOWN" instead of inventing a comparison.
Seven defects now share the shape - a plausible number, no error - and every one
was caught the same way, by running the thing where the right answer was already
known. That pattern is the Archivist's first standing instruction.


---

## 2026-09-13 — The Archivist widens; nothing to remember

**The Archivist now reviews, not audits.** The author's point: he wants to learn
from each session organically — rules broken, yes, but also desks or skills that
should exist, and ways to simplify. The desk now reads the session through five
lenses (what broke, what was missing, what was too hard, what worked, what recurs),
assesses one-off versus pattern, and suggests only if necessary, with every
suggestion typed and priced: rule edit, new desk or skill, check with a caller,
deletion, simplification, open item. "What worked" is a lens on purpose — a later
collapse needs to know what is load-bearing before it deletes anything.

**It runs per session now, not every N commits.** The old threshold existed to
break a loop: retrospectives edited rule files, rule edits counted toward the next
retrospective, the ledger grew 8x. That loop is cut at the root here — the Archivist
never applies, and rule paths are not watched — so frequency is no longer the
danger. The damper that remains is the desk's own exit: nothing substantive, three
lines, stop.

**"No author will remember *land it*."** Correct, and the fix is a principle, not a
synonym list: **a command that matters now is said now, in plain words.** The menu
shows "3 commits saved here, not yet on main — say *put it on main* when ready"
only when that is true. Saying *done* or *bye* gets two lines on where the work is
and an offer. The Stop hook pushes `session/` branches automatically so nothing is
ever stranded (a rule once sat unpushed for five weeks); `main` still moves only on
his word. Recorded as standing rule 14: a phrase he has to recall is a design
defect, not a training problem.


---

## 2026-09-13 — The seven orphan artifacts, assessed rather than re-listed

They had been listed twice as "no desk" without anyone asking whether they were
needed. Assessed against what ships, what references them, and what they claim:

**Three were already covered, and one of those is better covered than before.**
`parts/` (five reader-facing Part opening pages) is emitted by `/gw-compile`
before each Part's first chapter. `visuals/` belongs to the Designer.
`sweep-report.md` is replaced by `/gw-qa` writing `runs/qa/<date>-qa.md` — dated
by construction, so it cannot silently claim to be current.

**One was a real gap.** `appendix/practice-guide.md` is a **third output of every
refine** in the old pipeline, committed alongside `refined.md` and
`distillation.md`, and it is reader-facing: an accumulating field guide meant to be
read on its own. Nothing in this house produced it. The Line Editor now appends a
section per chapter, and the skill carries the warning that the file is shared —
the old compile once lost all ten Practice sections because a generator looked for
a `## Practice` heading while the field was `**Practice:**`, and nothing errored.

**Two were author decisions and both were ruled on 2026-09-14 — and both items
overstated their case.** #003 said the practice guide was stale; it had a section
for every chapter 1 through 11. #004 called the elevator pitch the cleanest
statement of the premise in the repo; the *file* was orphaned, the *content* was
already canonical in `00-premise.md` and in the river/oak/sun Framework concept.
Both claims came from a filename and a header, not from reading to the end of the
file. Rulings: the tactics review is archived under its range and the practice
guide becomes the tagged back-of-book guide; the pitch becomes a Publicist asset.

**One got a home.** `callouts.md` feeds marketing and is referenced by ten old
command files; the Publicist now owns the whole-book pull-quote pass.

**The finding underneath all of it, and it is the same shape again.** Three of the
seven describe a book that no longer exists: `callouts.md` and `tactics-review.md`
say "Chapters 1–8", `sweep-report.md` says "Ch01–Ch05", and eleven chapters are
refined. Each file looks current. That is `citation-manifest.md` in a third form —
a file presenting itself as live while nothing keeps it true. Generalized as
standing rule 15: **a point-in-time artifact carries its coverage in its filename,
or it is regenerated wholesale.** Hence `runs/qa/<date>-qa.md` and
`runs/marketing/callouts-ch01-chNN.md`; a name that states its range cannot lie
about being current. An artifact that accumulates appends and never rewrites.



---

## 2026-09-13 — Coverage audit: 27 of 40, not the 34 a loose grep claimed

The author corrected a real misfiling — `callouts` is a *skill* in the old pipeline,
something run periodically, and it had been assessed as an artifact. That correction
was worth more than the item: if one was misfiled, the coverage claim itself was
untested. So all 40 `book-*` commands were mapped.

**The first pass of that audit was wrong, in the usual direction.** A grep for each
command's keywords reported 34 of 40 covered. But a hit on the word "pitch" is not a
pitch package, and "park" appears in `gw-chapter` only as "the chapter is parked".
Checking for the actual deliverables — Amazon description, taglines, comp titles,
query letter, ARC, KDP — returned **zero hits across every skill and desk.** Real
coverage is **27 of 40**. Eighth defect of the same shape this week: a plausible
number, no error, caught only by checking against the thing itself rather than a
proxy for it.

**The 13 gaps cluster, and the cluster decides what to build.** Seven are Phase 4/5
publication work — positioning, pitch, publish-path, indie-plan, review-strategy,
club-guide, substack-connect — and every one of them needs the finished arc, the QA
findings and the callouts to be accurate. `/book-marketing` says so itself. With 18
of 29 chapters unwritten, building them now means building the least-validated part
of the house furthest from the work.

**Built now, because they are needed now:** `/gw-edit` (interactive re-edit, in
session, then refreshes the distillation, the practice-guide section and the plate —
an edit can break a count that passed, so the gates re-run) and `/gw-note`, which
closes a real hole: the engine's session log is *derived*, so it cannot carry a wrong
date, and equally cannot carry the author's own words. `/gw-note park` is kept
distinct from the inbox on purpose — the inbox is what a desk needs ruled to keep
working; a parked question is one he chose to defer, and it carries a **revisit
trigger** rather than a date, because a date on a deferred question is a guess.

**Registered, not forgotten:** `GAPS.md`, each gap with the trigger that should close
it, and — per standing rule 15 — the basis of its own audit stated in the file. When
the publication stack is built it should be **one** `/gw-publish` with a mode per
deliverable, not seven skills: they share every input, and splitting them is how ten
marketing commands happened the first time.


---

## 2026-09-18 — Chapter 12 shipped: the house's first chapter, end to end

Interview (two rounds, five rulings), research, draft, refine (2 rounds — Rule 6's
last, the objection row moved FAIL→PASS on the refined prose, confirmed by a fresh
clean-room desk), plate, verdict. Three pauses happened as designed and no others.
**12 inbox items raised on this chapter, all resolved** (`scripts/inbox.py --all
--chapter 12`, counted - a hand enumeration first put this at 19, caught by the
Archivist the same session): the citation claiming more than its evidence (#005),
the scene the Ghostwriter had no permission to invent (#008), a concrete instance
for an abstract paragraph (#009), a trademark hedge (#010), a key point a desk
moved without ruling (#011), a redundant mechanism with Ch11 (#012), a definition
collision with Ch6 (#013), a cushioned admission (#014), a love-language claim
against the chapter's own source (#016, #017 — the correction itself is #018,
tagged ch0, since it landed outside this chapter), a plate drawn against a
mechanism the chapter no longer had after the author's atrophy reframe (#019),
and a staged citation link that would have broken on landing (#029).

**What worked:** the two-touch design held under real pressure — every content
concept was proposed and answered before being written, never inferred. Rule 8(e)
fired correctly and unprompted: a wording change to satisfy #001 broke
`bold_max_per_piece`'s probe the same session, `okf_gate.py` caught it as structural
DRIFT, one commit fixed it. `--applied-by` closed the standing complaint that 0 of
16 Archivist proposals had ever actually landed — seven of nine items closed this
arc closed on a re-runnable proof command instead of a status field.

**What was too hard, alone:** landing the chapter into the book repo needed real
judgment calls a script couldn't make — which of two research rounds to ship
(round 2 only; round 1 is working apparatus, not a second source of truth),
whether "supersedes nothing" in a file's own header overrides a later shipping
decision (it doesn't), what a "prose-only" chapter file means against a sibling
chapter's full-apparatus convention. Each was resolved by reading the actual
target convention rather than trusting either source's self-description.

**What broke, caught only by re-deriving it:** two structural bugs surfaced during
this chapter's landing that had nothing to do with the chapter itself. `next.py`
had no terminal chapter stage — a shipped chapter reported "waiting on your
verdict" forever, which would have silently pinned the oracle on Ch12 the moment
Ch13 existed (fixed: #028, a `verdict.md` file is now the exit, written only when
the author actually gives the verdict). Five of Ch12's 23 staged citation files
carried internal links written for the shadow tree, not the book's own convention
— 9 links that would have broken on arrival, caught by eye, then closed
structurally so the next chapter's citations are checked before they land (#029).
Ninth and tenth instances of the same house shape: a plausible answer, no error,
caught only by running it against a state whose right answer was already known.

**Recurs:** every defect this arc found was in something no script read — the
oracle's own terminal state, a staged bundle's internal links, a review window
keyed to the wrong commit. The prose gates are earning their keep; the state and
staging layers are where the house is still finding its own blind spots.

---

## 2026-09-19 — The #030 lineage closed, on a fixture and zero rule words

Three sessions and four inbox items (#030, #033, #034) chased one defect: the
Archivist's review window. #030 fixed it and closed on a grep for a variable
name; the same collapse recurred on 2026-09-18 and went unnoticed until
2026-09-19. #033 moved the window into its own file, written before the dedupe
pointer, and backed it with `retro_window_cases()` — a fixture that builds a real
git repo and runs the actual hook. #034, raised by the Archivist against #033's
own fixture, guarded its second read of `retro-window` so a future regression
reports a named `[FAIL]` instead of a traceback that discards the rows already
computed, and added the one assertion the fixture was missing: that the dispatch
message carries the range inline, since that text — not the file — is the channel
the Publisher actually reads.

Reviewed cold, both assertions are real, not decorative. Stripping
`($START..$HEAD_SHA)` from the hook's message drops the suite to 36/37 with the
new row named; deleting the `retro-window` write drops it to 35/37 with two named
rows and no traceback. `tests/run.py` exits 1 on a failing tree and 0 on a clean
one, so it is a sound `--applied-by` target. The two dispatches in real history
chain exactly — the prior window ended at `b26879c`, this one starts there —
which is the property #030 broke.

The lens this lit is **what recurs**, and the answer is the shape the old
pipeline already wrote down: a fix that closes on a grep is a comment. What is
worth recording is the cost. The whole repair added **zero words** to the rules
corpus (16,904 at the end of 2026-09-18, 16,979 after — the entire +75 is
`gw-retro.md`'s own edit describing the fix). It landed in `tests/run.py` and one
line of `.gitignore`. Three sessions of defect, and the rule text did not grow —
that is the intended shape, and it is the first time it could be measured.

**A second, smaller recurrence in the same window:** `gw-retro`'s own inbox
items keep landing without their required proof command — 8 of the first 18,
including #033 and #034 themselves, closed with no `applied_by` field, because
`inbox.py --add` silently discarded `--applied-by` (only `--close` ever wrote
it) and nothing forced either the desk or the Publisher relaying it to notice.
Fixed the same session: `--add` now refuses a `gw-retro` item outright without
the flag, records it into the new item's frontmatter, and `--close` carries that
value forward if not repeated — closing the gap `--applied-by` was meant to close
in the first place.

---

## 2026-09-19 06:35 — The dedup fix shipped green and duplicated on its first real Stop

`session_log.py`'s dedup guard (above) landed, closed on `python3 tests/run.py`,
and wrote a duplicate `runs/log.md` entry on its very next real Stop anyway.
Cause: `last_entry_files()` kept `runs/log.md` in its returned set while the
current file set had it stripped, so the two could never be equal once the log
itself entered the cumulative diff — which the fixture's synthetic repo never
did, so it tested only the happy path. Found and reproduced by the Archivist
reviewing this session's own commit; independently reproduced here before
fixing. Same shape as #030 (closed on a grep, recurred) one level up: a fixture
that never exercises the real sequence certifies a guard that does not guard.
Fixed both sides — `last_entry_files()` now strips `runs/log.md` too, and the
fixture commits the log between runs, matching what the Stop hook actually
does. Cleaned the one duplicate block this produced.

---

## 2026-09-19 06:44 — The fixed fixture was renamed, not fixed

The fixture above (`session_log_dedup_cases()`) was renamed for the #039
defect without ever running it against the pre-fix code. Reproduced
independently: with only `scripts/session_log.py` reverted to `c17f979`, the
renamed case still printed `[ok]` — entry 1 is written before `runs/log.md` is
ever committed, so it never contains the one thing the defect needs to see.
Fourth instance of one shape: #030's grep, `voice_rules_check` passing its own
defect, the dedup half-fix, now the fixture written for that half-fix. Added a
fourth run that commits a *second* logged entry (which genuinely lists
`runs/log.md`) before re-checking — confirmed `[FAIL]` on the exact pre-fix
script, `[ok]` on the fix. Also made this class of miss structural rather than
relying on the next Archivist to notice by hand: `inbox.py --add` now refuses
a `gw-retro` item whose `--applied-by` names `tests/run.py` unless `--evidence`
shows a `[FAIL]` line, verified the same way (red on the pre-guard `inbox.py`,
green on the fix). This supersedes last session's still-undecided proposal to
require every `--applied-by` to name a case — that proposal's own item, #039,
named its case and was still unproven.

---

## 2026-09-19 06:54 — The guard against unproven proofs was itself unproven

The `[FAIL]`-substring guard above (#041) checked that `--evidence` contained
the text `[FAIL]` — an attestation, not a measurement. Demonstrated gameable
before building the replacement: an item filed with `--evidence "I did not run
anything. [FAIL] is a string I typed."` was accepted, exit 0. Fifth instance of
the shape this session (#030's grep, a check passing its own defect, a
half-fixed guard, an unproven fixture, now an unproven proof-of-proof). Each
prior fix raised the floor by measuring something new; a typed-string check
does not measure anything.

Replaced with `tests/prove.py`: given `--file`, `--at` (a commit) and `--case`
(an exact fixture case name), it reverts the file to that commit's content in
a throwaway `git worktree` — never the live tree, which would race the Stop
hook's own auto-commit — runs the worktree's own `tests/run.py`, confirms the
case is `[FAIL]`, restores the file, confirms `[ ok ]`. `inbox.py --add` now
shells out to it instead of reading a string the agent wrote. Proved both
directions against real repo history (`PROVED` on a genuinely discriminating
case, `REFUSED` on one that wasn't) before wiring it in, then re-ran the exact
fabrication that broke #041 against the new code and confirmed it refuses.
Five new fixtures in `prove_cases()`, built against a synthetic repo rather
than real commit history, so nothing here depends on a specific SHA staying
reachable. Corpus unchanged (17,017) — this landed entirely in `tests/` and
`scripts/`.

---

## 2026-09-19 07:03 — The mechanical proof measured something, but not this change

`tests/prove.py` (above) genuinely runs the red pass — that part held. What
didn't: nothing bound the proved case to the item being filed. `git worktree
add` checks out HEAD, blind to uncommitted work, so the only triples that
could ever pass were older, already-committed ones — unrelated to whatever
was actually being proposed. Demonstrated cold: a "should the house adopt a
mascot?" item, `--evidence "I ran nothing at all. This evidence is
fabricated."`, reusing prove.py's own worked example as `--prove-*` — accepted,
exit 0. #042's own first use had done exactly this by accident: it proved a
`session_log` case that entered `tests/run.py` in the *previous* window's
commit, not this one's.

Fixed both halves, since either alone makes the other worse: `prove.py` now
copies every `git status`-dirty path into the worktree right after creating
it, so a case that only exists in uncommitted work is provable at all;
`inbox.py` reads `.claude/state/retro-window`'s start commit and refuses a
`--prove-case` that already existed in `tests/run.py` there. Deleted
`prove.py`'s literal copy-pasteable `USAGE` example — the exact string the
mascot attack reused — for a placeholder. Re-ran the mascot attack against the
fixed code and confirmed it now refuses. Six new fixtures added, mutation-
tested both directions (each half reverted individually to confirm the
corresponding case goes red). Corpus unchanged (17,017).

Sixth instance of "the check meant to catch X doesn't actually catch X" this
session, and the first where the *mechanism* (running the case at all) was
sound and only the *binding* (which case, to what) was missing — a different
failure than the five before it, which is why it surfaced only once the
measuring itself was solid enough to expose it.

---

## 2026-09-19 07:11 — The window guard narrowed the hole; it did not close it, and it cannot

Seven rounds now on one lineage: #036, #039, #040, #041, #042, #043, this one.
Each built a guard; each next review broke it inside ten minutes. This time,
three bypasses survived the window-start guard above, all verified
independently before acting: renaming a few words of an older, unrelated,
genuinely-discriminating case makes its string "new" while it still
discriminates against its own old commit; reusing a case *this window itself*
already added needs no rename at all, since the guard only excludes cases
older than the window start; and an unreadable window state (all three
`.claude/state/*` files absent, or pointing at a commit `tests/run.py` can't be
read from — all three files gitignored, so a fresh clone has this off by
default) used to skip the check with no output whatsoever.

The reason is structural, not a bug the next layer fixes: deciding whether a
fixture case is actually *about* an English proposal is a semantic judgment,
and any caller who can edit `tests/run.py` and pass arbitrary `--prove-*` flags
can always construct something that discriminates but isn't related. Round
eight would be broken too, the same way. This is the same conclusion
`LEARNINGS.md` already reached once, in a different shape: no amount of check
text closes a problem that is not mechanically decidable, and recording that
plainly is worth more than a fifth (here, eighth) proposed clause.

**Decision: stop hardening this lineage.** The residual bypasses all require
deliberate effort that leaves a rename or a corrupted state file visible in
the diff — a different, much higher bar than the accidental reuse that
actually happened twice (#042, and this guard's own first design). Landed only
the honest version instead: `inbox.py` now prints a `NOTE` when the freshness
check cannot run at all, rather than passing in silence, and `tests/prove.py`
carries a `WHAT THIS DOES NOT DO` section naming all three holes explicitly,
closing with an instruction not to add a ninth layer. Corpus unchanged
(17,017). 70+ commits went into this machinery since 2026-09-18 12:00 while
`next.py` read `/gw 13` throughout — next up.

---

## 2026-09-20 15:09 — Two sessions, one set of records: the house's memory does not survive concurrency

Nine work commits landed from three branches in one window, merged twice. Both
of the house's own records were damaged by that concurrency, in opposite ways,
and neither had a check that could see it.

**The inbox is one file per item, so a clean merge hid a collision.** Two
branches each correctly computed `next_id()` as 045 and filed a different item;
git merged both with no conflict, and `--close 045` would have bound the
author's ruling to whichever slug sorted first. Caught by hand, renumbered to
#048. `LEARNINGS.md` L1346-1353 holds the same collision from the old
pipeline, "caught by hand, not by anything structural"; `runs/parked.md` P-002
was the second instance; this is the third. #046, the proposal for a
structural guard, was already open and unruled when it happened.

**`runs/log.md` is one shared file, so a line-level merge ate two entries.**
The 2026-09-19 06:38 entry lost its last file and its whole `**Next:**` line;
the 13:45 entry was left a bare header. Both mid-log, so nothing appended
after could notice. `next_action_streak()` then read each gap as a change of
direction and reported `unchanged for 6 log entries` where the true run was 13
of the last 14 — a plausible number, no error, in the one script whose job is
telling the author honestly whether the house is working on the book or on
itself. Repaired both entries from pre-merge git history (fully recoverable);
`next_action_streak()` now skips a malformed entry and reports how many it
skipped instead of silently undercounting.

**Then the correction itself repeated the shape it was fixing.** Inbox #047's
evidence (a real `sync.py` landing-mechanics defect) contained two fabricated-
looking git measurements; corrected once, and the correction carried forward a
stale SHA and mis-dated an event by two days, because it cited positional
reflog references (`@{N}`) that shift on every fetch or push instead of dated
SHAs. Corrected a second time, every line re-run fresh. Filed as inbox #051,
open: whether to guard this mechanically conflicts with this file's own
2026-09-19 07:11 entry ("stop hardening this lineage"), so it is left for the
author rather than decided here.

Lenses: what broke, and what recurs — the collision, instance three; the
plausible number, instance eight; a correction re-fabricating what it
corrected, new. What worked: the pulled-in window's own four-pass tombstone
guard fix, the OKF index reconciliation (0 warnings, down from 5, without
touching a human sentence), and the cutover finish all held under independent
re-verification.

---

## 2026-09-20 15:23 — The repair's own proof was blind, and the correction of the correction needed a third correction

The Archivist's review of the entry above found the entry above wrong in two
more places, verified independently before acting on any of them.

**The streak fixture didn't test the fix it shipped with.** Its malformed
entry sat next to a genuine direction change (`/gw 5`), so `break` and
`continue` on the missing-`Next:` branch both returned `(2, 1)` — reverting
just that one line left the suite at 97/97 with the case still `[ ok ]`.
Reshaped so the gap sits between two matching entries on both sides; now
`break` gives `(2, 1)` and `continue` gives the correct `(4, 1)`, a real
`[FAIL]`/`[ ok ]` split. Given a tolerant int-or-tuple unpack (14 words), the
case now runs through `tests/prove.py` for a mechanical red-then-green proof —
the "interface change means this can't be proved" reasoning in the prior entry
was true of the fixture as shipped and false as a general claim.

**The number in the prior entry's own evidence was wrong.** It said the fix
produced `(13, 0)`; measured fresh, it was `(26, 0)` at the repair commit and
`(27, 0)` by the next one. 13 was carried forward from an earlier review's
prose instead of re-run — inside the item whose entire subject was that habit.
Corrected in both inbox #050 and here; this file does not edit its own past
entries, so the wrong number above stands as the historical record and this
one carries the fix forward.

**And #047's evidence needed a third correction, not a second.** Its "second"
correction (prior entry) fixed the notation (dated SHAs instead of `@{N}`) but
not the habit: it asserted what git state existed at the moment of filing and
still got it wrong — main was already reset by then, not still on its old
root. Deleted the historical narrative outright rather than attempt a fourth
rewrite; the code defect it names never needed a story about timing to stand.

**Two structural gaps, fixed.** `inbox.py`'s proof-freshness guard applied
only to items whose `raised_by` started with `gw-retro` — a string the filer
chooses, and exactly what let #050 ship a blind fixture with a flagless proof
by being filed under a different name. Now applies to any item whose
`--applied-by` names `tests/run.py`, regardless of filer. And #051 carried
`applied_by: true` — a tautology that would have auto-confirmed on ruling with
nothing landed. Caught and fixed there; **caught again in #052, filed minutes
later with the identical mistake, before it was committed.** Left unfixed
mechanically — the proposal to guard it is #052 itself, open, because building
it would reopen the 2026-09-19 07:11 decision without the author's word.

Lens: what recurs, three more times in one review (the blind check, the
plausible number, the re-fabricated correction), and what worked: catching the
third recurrence in the same sitting it was made, before it left the working
tree. Corpus unchanged; every fix above lives in `tests/`, `scripts/`, or
`inbox/`.

---

## 2026-09-20 15:35 — The fixes held; the eighth guard didn't, and it was applied without a ruling

Three claims from the entry above were re-verified and stood: the reshaped
streak fixture genuinely discriminates, `(26, 0)`/`(27, 0)` are correct, and
`#047`'s code claim (`sync.py` L78-79 vs L162-163) is exact.

Two did not. First: that same commit widened `inbox.py`'s `tests/run.py`
proof-freshness guard from `gw-retro`-scoped to every filer — an eighth layer
on the lineage this file decided at 07:11 to stop hardening, applied directly
rather than filed, in the same commit that correctly deferred a *smaller*
guard (`#052`) to the author. Measured, the widening refused legitimate
filings (a deletion proof, any not-yet-applied proposal) and was evaded by
`cd tests && python3 run.py`. Reverted to `gw-retro` scope; filed `#053` for
the author to rule on rather than decided again here. Second: `#047`'s
"deleted the historical narrative" claim was true of its **Checked** block
only — the same wrong forced-update SHA and wrong cause survived in the
item's body untouched. Cut there too, this time; the code defect never needed
either copy.

Lens: what recurs — a fix applying the fix it just correctly declined to
apply elsewhere in the same breath. Corpus unchanged; every change lives in
`tests/`, `scripts/`, or `inbox/`.

---

## 2026-09-20 15:37 — #047's history, wrong a fourth time, deleted rather than corrected a fifth

The guard revert held under independent re-verification (`gw-retro` still
refused without `--prove-*`; a non-`gw-retro` filer citing `tests/run.py`
incidentally was accepted again). One thing didn't: the sentence left standing
after the last cut — "the original engine root c74fe66 is NOT an ancestor of
origin/main, i.e. local main and origin/main were genuinely unrelated
histories at that moment" — was itself wrong. `main` was reset to
`origin/main` on 2026-09-18, a day before the incident this item describes;
its root on 2026-09-19 was already `d34a3ec`, an ancestor of `origin/main`,
not `c74fe66`. Four corrections, four different wrong claims. Removed the
narrative outright this time rather than attempting a fifth rewrite — the
item's actual defect (`sync.py` measures `origin/main`, acts on local `main`)
never needed an account of any specific incident to stand, and now has none.
This closes the #047-history sub-thread; nothing about it should need a sixth
look.

## 2026-09-23 08:02 — Scoped chapter review and reader-friendly PDF openings

Author authority: “Let's make the changes.” Chapter handoff now calls existing persona/coherence desks with relevant context and checks revision-bound evidence before verdict. Archivist assessment distinguishes repairing one instance from preventing recurrence; neutral dispatch replaces recommendation-minimizing steering. No new desk or whole-book reread requirement. Independent forward testing caught null scope acceptance, now rejected. Older author-deferred findings remain separate.

The author reported spaced chapter letters and an undifferentiated title in his audio reader. Both PDF backends now share ordinary chapter labels, explicit bold titles and flush-left openings. Actual PDF integration checks reject the old export and pass the new one; seven pages inspected and extracted content preserved. Chromium rendering now closes explicitly through the existing Playwright dependency. No claim of testing the author's particular reader. Regression suite: 123/123 with local font-path override, followed by 15/15 focused tests including three new scope cases. Instruction word changes are recorded in runs/ch13/workflow-word-costs.txt; generated plugin copies synced.
