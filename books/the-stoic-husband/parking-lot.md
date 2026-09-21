# Parking Lot

## Open Items

### [#38] — [2026-09-21 13:12]
**Question:** Two whole-set findings from the Reader Panel's cold read that cannot be fixed under the current "no rethinks" ruling. Do they get a round when that ruling lifts?
**Context:** Both come from `runs/design/2026-09-21-plate-standalone-read.md`, the Panel's cold read of all twelve chapter plates, and both are only visible having looked at the whole set rather than any one plate. Recorded here because they were reported to the author in conversation and nowhere durable, which is the failure he corrected on 2026-09-21.
**(1) Ch7 and Ch11 have converged on one composition.** Solid full box on the left, dashed empty box on the right, same proportions and same positions. Ch11 is one of the two strongest plates in the set and will be read less carefully for looking like something the reader has already seen four chapters earlier. Separating them means changing the objects on one of the two, which is a rethink and therefore outside the current ruling.
**(2) Nothing in twelve plates depicts warmth.** Every right answer in the set is drawn as damage avoided: a hole not made, a scale not tipped, a door not closed, a line not crossed. That is the correct register for Parts I and II, but Part III is the Warm Sun, and the visual language has no vocabulary for the thing that Part is about. Worth knowing before Part III's chapters get plates of their own, because the pattern will either continue by default or have to be broken deliberately.
**When to revisit:** When the "no rethinks" ruling lifts, or at the first Part III chapter plate, whichever comes first. (2) is the more consequential of the two and is cheapest to act on before Part III plates exist rather than after.
**Status:** OPEN, non-blocking.

### [#36] — [2026-09-21 13:05]
**Question:** The Oak Part plate was told to say "something about how each year it grows stronger." The drawing now says it; no words on the plate do. What sentence carries it, and does it go on the plate or on the Part II page?
**Context:** The author's instruction on 2026-09-21 was to keep the rings and make them mean growth rather than age, after outside feedback caught that tree rings depict a tree already cut down, which argues against a husband still standing. The drawing was changed and works: rings run off all four sides so nothing closes, there is no bark line and no cut end, ring widths widen from core to edge, and the first ring after each hard band is the heaviest line on the plate. The caption is unchanged and is still the Part II page's last sentence, verbatim per the Part idiom: *"The storm comes through, and in the morning the oak is still there."* That sentence is about survival, not accumulation, so the growth idea is carried entirely by the picture.
**Why nothing was written:** A corpus search finds no sentence in the book tying the oak to growing stronger over years. The Part II page is about holding weight and losing branches without ceasing to be the tree. `05-framework.md` gives "The oak's strength isn't announced; it's revealed when weight is placed on it" and "active steadiness through the hard, slow seasons" — neither is about becoming stronger each year. So a plate line would be new book content, which Rule 9 says is proposed and never written cold, and the Part idiom allows no text but the caption anyway.
**Options, none chosen:** (a) leave it to the drawing, which is where it stands now; (b) an Author addition the author writes, used as a second line on the plate, which also needs the caption rule relaxed (see #37); (c) a new last sentence on `parts/part-2-sturdy-oak.md`, which then becomes the caption for free and keeps the idiom intact. (c) is the cheapest if he wants words.
**When to revisit:** Before the Part plates are landed into `books/`, since landing fixes the caption. Draft is at `runs/parts/plate-2-sturdy-oak.svg`.
**Status:** OPEN, non-blocking.

### [#37] — [2026-09-21 13:05]
**Question:** Tie the river's canyon to something the marriage gained, and settle the Part plate title rule the drawn plates now break.
**Context:** The author asked on 2026-09-21 to "tie back carving a canyon to something positive in the marriage," and separately to add titles to the Part plates. Titles were added (THE STEADY RIVER, THE STURDY OAK) and the river now fills the canyon it cut instead of leaving an empty wedge. The canyon-to-marriage tie was **not** delivered.
**Why nothing was written:** "Canyon" appears in exactly one place in the book's prose — the Part I page's last sentence, which is already the plate's caption. The river's vocabulary elsewhere is all *accepts the landscape / keeps flowing / holds its direction*, never what the patience built. Verified independently of the desk that first reported it. So the tie would be new content, and the Designer correctly proposed rather than invented. Its proposal: *"The canyon is not the damage. It is what the ordinary days built."* Both halves are close to the book's own words — "built" is Part V's ("Stand in the summer you built") and the Introduction's ("We built it as we went"), and "ordinary days" is the existing caption's ("one ordinary day at a time") — but the sentence itself is nowhere in the book.
**The title rule, same item because the same file fixes both:** `parts/README.md` permits no text on a Part plate except the caption. The two drawn plates now carry titles on the author's instruction, so the written rule and the artifacts disagree, and Parts III, IV and V still have no titles, so the furniture stops at Part II and reads as an accident rather than a decision.
**When to revisit:** Before landing the Part plates. Landing them without settling this puts a rule-breaking plate into `books/` and leaves three of five without titles.
**Status:** OPEN, non-blocking.

### [#34] — [2026-09-09 11:57]
**Question:** Build the Agentic Publishing House, the Level 3 redesign of this book system, and if so, when relative to the remaining chapters?
**Context:** Designed 2026-09-09 at the author's request; written up in full at `docs/AGENTIC-PUBLISHING-HOUSE.md` (repo root, not the book folder, because it governs the system rather than this book). The design: ten named desks (Publisher, Developmental Editor, Researcher, Ghostwriter, Line Editor, Conformance Checker, Anti-Slop Reader, Fact-Checker, Reader Panel, Publicist) addressed through a front-door Publisher persona that relays conversations with desks and keeps their context; agents reviewing agents at every cold stage; the author kept to two touches per chapter (the interview and the verdict) plus a generated exceptions inbox; and the mechanics that have failed repeatedly as rule text (timestamps, manifest writes, the git-sync block copied into 20 skills, counted voice rules) moved into scripts and hooks. Corpus target about 23,000 words against today's 81,000, with a ledger mapping every deleted rule to the desk or script that now enforces it. Four decisions were already made: interview + verdict + exceptions; design only for now; aggressive corpus collapse; subagents plus relay. Nothing is built or in force. Three smaller questions are open inside the doc (Part 8): desk handles vs. personas; PDF vs. audio for the verdict (see #20); whether `/book-status` survives as an alias for `/board`.
**When to revisit:** Before `/book-chapter-refine 11`, because the doc's Part 7 proposes proving the first desk (the Line Editor, with its gates) on exactly that refine, and Stage 0 (the production scripts) removes the timestamp and self-report failure classes before any desk exists. If Ch11 proceeds on the current pipeline instead, revisit at the Ch12 interview, the next natural seam.
**Status:** OPEN, non-blocking.

### [#35] — [2026-09-10 02:33]
**Question:** Finish the house-translation retrofit (`06-sources.md`): three items remain after the 2026-09-09 pass, plus a reachable primary-text channel that `/book-verify` should know about.
**Context:** On 2026-09-09 the author asked for the most modern public-domain translations to be found and applied; a parallel session had locked the same standard in `06-sources.md` two days earlier (Long for Marcus and Epictetus, Gummere for Seneca, Haines VI.8 in Ch2 as the one ratified exception). Every printed quotation in `06-sources.md`'s "Retrofit outstanding" table is now done except the Ch11 *Meditations* 4.49 row, which needed no swap because the chapter carries the idea without quoting it. Long's wording came from Project Gutenberg through its GitHub mirror: `https://raw.githubusercontent.com/GITenberg/<Title-Slug>_<id>/master/<id>.txt` (Marcus #15877, Epictetus #10661), which this container can reach even though gutenberg.org itself is blocked. The file's own `Translator:` line is what identifies the edition; #2680 is Casaubon and #45109 is Higginson, not Long or Carter as their titles suggest.
**Still open:** (1) Ch10 *Enchiridion* 30 prints Carter-style wording with no translator credited and should move to Long's XXX, but Long's "to submit when he is reproachful, when he inflicts blows" is harsher than the current line in a chapter about holding a boundary with a tired wife, so the swap needs the author's read. (2) Seneca *Letter* 91 §4's tail ("and we should consider, not what is wont to happen, but what can happen") is printed but not yet transcribed from a Gummere page; Lane C. (3) `/book-verify`'s Lane A should treat the GITenberg mirror as a Gutenberg route: `scripts/verification_probe.py` already probes raw.githubusercontent.com as a dev host, but nothing maps a Gutenberg id to its mirror URL, so the command cannot use it yet. A small table of ids for the house editions would make Long's texts Lane A from the cloud container.
**When to revisit:** (1) at the author's read of Ch10 or the laptop verification pass; (2) with parking-lot #32; (3) next time `/book-verify` is edited.
**Status:** OPEN, non-blocking.

### [#33] — [2026-09-10]
**Question:** Fix `scripts/verification_packet.py` so packet numbers are stable, and decide what to do about the three packet/result pairs already orphaned.

**The bug.** The script numbers packets by splitting *whatever is still outstanding* into chunks of eight, starting from 1. So every regeneration renumbers everything. `packet-01.md` today is not the `packet-01.md` that `results-01.json` was produced from — it now lists `cloud-townsend-boundaries` and `epictetus-discourses-2-18`, while `results-01.json` answers `brown-clear-is-kind` and `epictetus-discourses-3-16`. Same for 02 and 03. `packet-06.md` was deleted outright when the remaining set shrank.

**Where it came from.** Commit `7b2d4d9` (2026-09-04), *"chore: regenerate verification packets after Tier 1 completion"* — a routine regeneration that silently rewrote the record of work already done. Not a mistake anyone made; the script is built this way. It was found again on 2026-09-07 when a read-only run of the script clobbered the same three files, which was reverted.

**Why it is not urgent.** Nothing depends on the mapping. The evidence that matters — edition, locator, wording, surrounding context, verdict — lives in each citation's own `# External Verification` block, which is durable and correctly attributed. What is lost is only the audit trail of *which packet produced which answers*.

**Why it is still worth fixing.** This is the same defect class as the retired `citation-manifest.md`: a file that presents itself as a record while nothing keeps it true. A future session comparing `packet-02.md` against `results-02.json` would draw wrong conclusions and have no way to know it.

**Scope if built:** derive packet ids from content (a hash of the slug set) or make them append-only against a small persisted ledger, so regeneration adds new packets rather than renumbering existing ones. Roughly an hour. The already-orphaned 1-3 mapping probably cannot be reconstructed — the honest fix there is a note in `sources/verification/README.md` recording that packets 1-3 and their results predate stable numbering and should not be cross-referenced.

**When to revisit:** Before the next packet generation, i.e. before the Lane C work in #32 runs via the packet path. Not blocking if that work runs from the laptop instead, since Lane A never builds a packet.
**Status:** OPEN, non-blocking.

### [#32] — [2026-09-09]
**Question:** Close the 22 Lane C verbatim citations — the word-for-word quotations whose wording has never been checked against an actual page.

**Context:** These are `quote_form: verbatim` citations already sitting in `manuscript.md`. A wrong quotation in printed prose is a wrong book, which is why they are the highest-risk set in the ledger. They are Lane C **only because of where the work has been happening**: this repo's cloud container routes through an egress proxy that blocks Standard Ebooks, Wikisource, Project Gutenberg, archive.org, PubMed and every author-hosted PDF. Verified 2026-09-07 — `curl` and `WebFetch` agree, and both are blocked for every scholarly and literary host.

**Why this is smaller than it looks.** On the author's laptop there is no proxy, and the house translations settled 2026-09-07 — Long for Marcus and Epictetus, Gummere for Seneca — are all public domain and freely readable on exactly the hosts that are blocked here. Run `/book-verify` from the laptop and `scripts/verification_probe.py` detects the difference automatically: most of these 22 become **Lane A**, meaning the page is opened and the wording transcribed directly, `evidence_source: page-text`. No ChatGPT session, no packet, no pasting results back.

**The packet path stays as the fallback it was designed to be.** `scripts/verification_packet.py` builds a text packet for an outside session with browsing. That is the right tool when the laptop is not available; it is not the default.

**What this does NOT get to.** Nothing here reaches `status: verified` — CLAUDE.md Rule 11 reserves that for the author against his own copy. Lane A closes the *wording* question with page evidence and stages the edition and locator so the author's own check is a thirty-second confirmation instead of an afternoon.

**Known live items inside this set:** the seven quotations dropped from `verifiable` to `unverified` on 2026-09-08 by the transcription rule; the suspected *Letter* 81 splice (defect #11); and the two already-known `DIFFERENT_WORDING` defects at `Enchiridion` 1 and *Meditations* 4.49.

**What `/book-verify` actually does when you run it — read this first, you will not remember.**

You type `/book-verify`. Nothing else. Everything below happens without you.

1. **It checks what your machine can reach** (`scripts/verification_probe.py`) — it
   does not assume, and it does not trust anything written in an earlier session,
   because the answer is different on the laptop than in the cloud.
2. **It picks the riskiest citations first** — the word-for-word quotes already
   sitting in the manuscript. A wrong quotation in printed prose is a wrong book.
3. **It opens the real pages** and transcribes what they actually say, with the
   edition, the section number as that source numbers it, and enough surrounding
   text to prove it was on the right page.
4. **It shows you what it found before writing anything** — and if a source says
   something different from what the book says, it tells you side by side and
   changes nothing. Broken quotes get reported to `quality/citation-defects.md`;
   fixing the prose stays yours.
5. **It never marks anything confirmed.** That is yours alone, against your own
   copy — Rule 11. What this does is stage the edition, locator and exact wording
   so your check takes thirty seconds instead of an afternoon.

Work happens 8 at a time, with a check-in between batches. Stop whenever; the
ledger is always in a consistent state.

**If the laptop is not available:** `/book-verify` detects that too and builds a
text packet instead, which it pastes into the chat for you to drop into ChatGPT or
Claude with browsing on. Bring back whatever it returns, in any format, and paste
it here — no files, no JSON, no commands. That is the fallback, not the plan.

**When to revisit:** Next session run from the author's laptop. Nothing blocks in the meantime — the compile gate (`okf_validate.py --strict` in `/book-compile` Step 4.4) already prevents any of these from being presented as confirmed, and the ledger currently states their status honestly.
**Status:** OPEN, non-blocking.

### [#31] — [2026-08-28] — reasoning corrected [2026-08-31]
**Question:** Rename Parts IV and V to **The Desert** and **The Orchard**?

**Correction, recorded because the first version of this item misread the author's own precedent and argued against him on that basis.** This item originally claimed the rename "reverses his 2026-08-23 structural fix," which it described as *single nouns name a state, and Parts IV and V are movements*. That is not what he ruled. His actual objection to "The Winter" was narrower and better: **winter is one state inside a cycle of four**, and naming a Part after one quarter of a cycle the book never otherwise uses is incoherent. In his words: "my previous advice was misconstrued that I just didn't want to have one state in a cycle of four."

**Why Desert and Orchard are not subject to that objection at all:** they are not a cycle. That is the entire point, and it is the strongest argument for them.
- **A desert does not pass.** You can walk into one and die there, and a great many marriages do exactly that. Fall-to-Winter promises an ending that a desert refuses to promise, and Part IV is sexlessness, separate lives, and betrayal — the section where that promise is least honest.
- **An orchard sustains rather than arrives.** It bears fruit and it gives shade. It is not the good quarter of a wheel that comes back around; it is a place that feeds you because it was planted and tended.

**This inverts the objection the original version of this item raised.** That version warned that the rename breaks the matched closing lines of both Part pages — `part-4-fall-to-winter.md`'s "Every winter ends. No winter is the last one." and `part-5-spring-to-summer.md`'s "No summer is the last one." — because deserts and orchards do not recur. Correct on the mechanics, backwards on the significance. **The recurrence promise is the defect, not the feature.** "Every winter ends" tells a man in Part IV's territory that his winter ends on its own, which is the same false comfort that killed "The Breeze" for Part V during #27 (rejected because a breeze says the good part arrives without you). The seasonal frame smuggles that promise into both pages, and nobody caught it at the time because the frame made it feel like weather rather than a claim.

**So the closing lines need rewriting either way**, and the rename is what surfaces it. Both pages also carry seasonal imagery throughout, not only in their closers, so this is a rewrite of both paragraphs rather than a swap of two sentences.

**Still worth checking before committing:** the #27 rule that a closing section cannot be specific to one element. **The Orchard** plausibly satisfies it better than anything yet proposed — an orchard needs water, trees, and light, which is all three. **The Desert** is defined by the *absence* of water, which makes it River-specific by negation. That may be fine, or even right, since Part IV is the section where what the man built is missing. Author's call, not a blocker.

**Consequence for Chapter 11:** Ch11 has been using "the desert" informally for a bounded dry spell. If Part IV takes the name, a Part II chapter using Part IV's title for a narrower meaning collides, and it cuts against the standing rule that a Part's identity language reaches the reader once per Part. **Ch11 carries the idea in plain language and does not use the word.** Already recorded in `chapters/ch11/research.md`.
**When to revisit:** Before Part IV is compiled for any real reader, and before any chapter in Parts IV or V is drafted. Parts IV and V begin at Ch18 and Ch24, neither drafted, so nothing blocks.
**Status:** OPEN, non-blocking.

### [#30] — [2026-08-23]
**Question:** Should `/book-status` report Part-opening state — which Parts have an opening page, which declared one via a pointer line but haven't written it yet, and which have none by choice?
**Context:** Split out from the 2026-08-23 audit that found Part openings documented in `CLAUDE.md` and `README.md` but invisible to the three skills that need them. Two of those were defect repairs and were fixed: `/book-outline` now offers openings when Parts are confirmed and writes the pointer line, and `/book-feedback part-N` now resolves (it was named in three docs while the artifact table had no row for it, so the documented command did nothing). This third one is different in kind: it is **additive**, a new report line rather than a repair, so under the net-zero retrospective policy it is not yet earned and no deletion candidate was nameable.
**What it would buy:** the only way an author currently discovers that Part III has a declared-but-unwritten opening is by running `/book-compile` and reading the summary line. A status line would surface it without a compile.
**Why it can wait:** exactly one book uses Part openings, and its five pages are all written. There is no drift to detect yet. Revisit when a second book adopts them, or when this book adds a Part after the fact and the pointer sits unwritten long enough to be forgotten.
**Scope if built:** `status-reporter` reads `stages.parts` plus the pointer lines in `03-outline.md`, and `/book-status` prints one line per Part only when the book has Parts at all. Books without Parts must show nothing.
**Status:** OPEN, non-blocking.

### [#29] — [2026-08-23]
**Question:** Should the line-by-line lesson dissection become an enforced pass, and if so at what scale? The author's ruling today: **not as a rule** — too hard to enforce across a full chapter. Parked as an idea worth evaluating later, aimed at the broader goal of every sentence carrying real meaning rather than fluff.
**Context:** During the Part openings session the author asked for a table dissecting every line against the lesson a reader would infer, with instructions to cut anything that didn't map. On five 62–66 word pages it removed three items that four prior review rounds had left in place: "and nothing grows in the dark" (rhythm, not meaning) and two connective fragments in Parts IV and V. The finding underneath it is that reading prose for *rhythm* and reading it for *inferable content* are different passes, and the second one catches things the first cannot. **Why it doesn't scale as written:** a 2,500-word chapter is roughly 150 sentences against a section page's six. A full dissection table per chapter is impractical, and a rule that gets skipped is worse than no rule (see `.claude/LEARNINGS.md` on rules that are routinely bypassed). It is also currently unfunded under the net-zero policy — no deletion candidate was nameable.
**Possible scaled-down forms, if revisited:** apply it only to a chapter's opening and closing paragraphs; apply it only to sections flagged by another pass; or run it as an occasional spot-check rather than a gate. None evaluated yet.
**Where it lives now:** `parts/README.md` records it as a form rule for the five Part pages only, where the scale makes it trivial. That is the whole of its current scope.
**When to revisit:** after a few more chapters are refined, or the next time a chapter reads as padded and nobody can say which sentences are doing the padding.
**Status:** OPEN, non-blocking.

### [#26] — [2026-08-17]
**Question:** What replaces "the oak holds firm" as Chapter 10's per-tier refrain?
**Context:** The original refrain is the author's own phrase from the 2026-08-08 research check-in, and it closed each of the chapter's three tiers. It was cut in the second draft because it names an element directly (see #27). The current draft uses **"You hold it anyway."** as a placeholder replacement, three times, one per tier. It does the same structural job, avoids the element reference, and is second person, which helps the chapter's direct-address count. The alternative considered was "The line holds," which reads sturdier but drops the second person. The author wrote the original and should pick its replacement rather than inheriting the drafter's choice by default.
**When to revisit:** During `/book-chapter-refine 10`, or on the author's read of the refined chapter.
**Status:** OPEN, blocking nothing — the draft is coherent with the placeholder in place.

### [#24] — [2026-08-17]
**Question:** Chapter 10 carries two composite moments that would be stronger with real material: Tier 1's anger pressure, and Tier 3's Christmas-morning assumption.
**Context:** These are items 7 and 8 from `chapters/ch10/research.md`, deliberately written as composites rather than left as `[STORY NEEDED]` blockers, per the research-phase decision that Tiers 1 and 3 run on recognizable moments rather than personal stories (the chapter has one personal story, the one-time loan, anchoring Tier 2). Composite is the archetype's primary evidence type, so neither is a defect. But the anger pressure is the thinnest thing in the chapter and reads like a construction, and the Christmas moment is entirely the drafter's invention. Either would land harder with something the author has actually lived.
**When to revisit:** During `/book-chapter-refine 10`, or any later `/book-edit 10`.
**Status:** OPEN, non-blocking.

### [#23] — [2026-08-04] — originally logged as [#20]; renumbered 2026-08-14 (number collided with the LEARNINGS.md migration batch)
**Question:** Real trepidation about actually sharing the manuscript with the author's wife once it's ready.
**Context:** Split out from #14, which originally bundled this with an unrelated story-material question — this thread isn't chapter content at all, it's a personal decision about the book project itself. Worth its own conversation once there's something substantive to actually show her, rather than staying a stray line under a content-development item.
**When to revisit:** Naturally around Gate 3 (after `/book-sweep`, once there's a complete, QA'd manuscript) rather than earlier — showing a partial or unpolished draft isn't the same decision as showing the finished thing.
**Status:** OPEN, non-blocking.

### [#22] — [2026-08-13] — migrated from `.claude/LEARNINGS.md` [#3]
**Question:** Document the chapter-retitle migration playbook as a repeatable procedure, so the next retitle doesn't start from first principles again.
**Context:** Retitling a chapter mid-research (Ch9, "Boundaries Are Not Betrayal" → "Silence Is Not Peace") required migrating every OKF file's `chapter_slugs` tag off the old slug plus fixing every plain-text title mention across the book's reference docs. This was the second chapter-identity change forcing a manual multi-file sweep (the first was Ch10's insertion, 2026-07-06, which produced the slug-based-reference fix now in CLAUDE.md Rule 6). That earlier fix assumed numbers were the only unstable part of a chapter reference — it didn't anticipate that the slug is derived from the title and breaks the same way when the title changes. The Ch9 sweep was reconstructed by hand: grep the old slug across `okf/`, grep the old title text across the book directory, count occurrences before touching anything (per CLAUDE.md Rule 15), edit individually, re-grep to confirm zero remain. It worked; nothing documents it.
**When to revisit:** Next chapter retitle, or when touching `book-feedback.md`'s outline-revision path. Candidate homes: a new step there, or a CLAUDE.md rule adjacent to Rule 6.
**Status:** OPEN

### [#21] — [2026-08-13] — migrated from `.claude/LEARNINGS.md` [#5]
**Question:** Should `book-chapter-draft.md` require independent reverification of a sub-agent's self-reported stats, and add rhetorical-device repetition as a sixth Step 4.5 scan?
**Context:** Ch9's draft was delegated to `chapter-writer`. Its self-reported stats were checked against an independent count rather than trusted, and were wrong: word count self-reported ~1,235 vs. actual 1,293; direct-address density ~77/1,000w vs. actual 68.1. More seriously, it failed to self-report a real violation — the "That's not X, it's Y" reframe appeared 6-7 times against `01-voice.md`'s cap of 2, a counted rule in that file's own "Verification, Not Impression" section. Nothing in `book-chapter-draft.md` tells the orchestrating session that a sub-agent's self-report is exactly the "impression" that section warns against trusting, and Step 4.5's five scans don't include device repetition at all.
**Partially addressed [2026-08-13]:** The `spec-checker` gate (`.claude/agents/spec-checker.md`, wired into `book-chapter-refine.md` Step 3.6) establishes the principle structurally for conformance — a checker with a starved input set, whose findings must be reproduced verbatim rather than summarized. It does not cover the draft-stage counted-rule scans, which is what remains open here.
**When to revisit:** Next time `book-chapter-draft.md` is edited, or as part of the deferred draft/refine consolidation.
**Status:** OPEN

### [#20] — [2026-08-13] — migrated from `.claude/LEARNINGS.md` [#7]
**Question:** Should reading a chapter aloud (or a PDF/TTS pass) become a suggested step before final approval, rather than something that happens by chance?
**Context:** Ch9 went through two full refine-stage revision rounds before the author was satisfied, and both were triggered by engaging with the chapter in a different mode than the in-session text check-in: once after reading a generated PDF, once after listening to it read aloud. The audio pass surfaced the session's single biggest structural finding (the "blowup" mechanism reading as watered down) — a problem that survived two rounds of text-based check-in. Ch10's failure was also caught by the author reading it, not by any automated pass. Text and audio review appear to catch different failure classes: pacing, whether an idea lands without visual re-reading, and whether a callback assumes too much of the reader all surface more readily by ear.
**Note:** No longer a single data point — Ch9 (twice) and Ch10. Worth reconsidering as a real gate rather than an optional nudge, given it has now caught two structural failures that four automated passes each missed.
**When to revisit:** Author's call. Candidate: a line in `book-chapter-refine.md`'s Step 6 check-in prompt.
**Status:** OPEN

### [#12] — [2026-07-20] — merged with #14, #15 on 2026-08-04
**Question:** Three one-sided reciprocity incidents, all the same underlying pattern — is there story material here, and if so, where?
**Context:** Merged 2026-08-04 after the author supplied the specifics that were missing from the original three separate, under-detailed entries. All three are "I do this for her, she won't do the equivalent for me" (or the reverse), in a different domain each time:
1. **The audiobook incident (formerly #15):** the author was listening to a book together with his wife, chapter by chapter, as a connective gesture. A car-ride conversation about progress on it turned into critique, then an argument over exact timing, then a stonewalling silence — no repair.
2. **The manuscript-reading reluctance (formerly #14):** the author's wife doesn't want to read the Stoic Husband manuscript, and the reason she's given traces back to incident 1 — he wouldn't listen to an audiobook of hers, so she's reciprocating (or protecting herself from reciprocating) the same way. This is likely the *actual mechanism behind* the audiobook incident's tension, not a separate pattern — worth researching as one continuous story, not two.
3. **The mahjong asymmetry (formerly #12):** she doesn't want to play the games the author wants to play, but wants him to play mahjong. Same one-sided-reciprocity shape as 1 and 2, different domain (games instead of books), likely a separate example rather than the same incident.
Likely chapter home: **Ch26 (Friendship Is the Hidden Engine)** for the general reciprocity-in-shared-interests pattern (mahjong + the reading dynamic as two examples of the same principle), with **Ch17 (Repair Quickly, Love Deliberately)** as a secondary candidate specifically for the audiobook incident's rupture-without-repair arc, if it's developed as its own scene rather than folded into Ch26's broader point. See also #20 (the separate, non-story question of when/how to actually share the manuscript with her) — related in origin but a different kind of decision.
**When to revisit:** Ch26's research pass (primary), or Ch17's if the audiobook incident gets developed as its own scene.
**Status:** OPEN, non-blocking.

### [#9] — [2026-07-08]
**Question:** Extract the Stoic-specific content baked directly into shared `.claude/commands/` skill files, so the agentic book-writing framework stays portable to a non-Stoicism book.
**Context:** Surfaced during the Ch2 Substack retrospective (2026-07-08, see `.claude/LEARNINGS.md`). `book-substack.md`'s Voice Constitution hardcodes: *"Light Stoic tie-in — required... every post should contain at least one earned connection to Stoic thinking."* The mechanism — every post needs one earned tie-in to whatever the book's organizing tradition/frame is — is durable across books; naming Stoicism specifically is not. The intended seam already exists: `04-archetype.md` is documented in `CLAUDE.md` as the "genre profile" file for exactly this kind of book-specific-but-structured content. Fix would be: (1) audit `book-substack.md` and other command files for other hardcoded Stoic-specific language beyond the tie-in line, (2) move the specific tie-in requirement (and anything else found) into this book's `04-archetype.md`, (3) reword the shared command file(s) to reference `{bookRoot}/04-archetype.md` generically instead of naming Stoicism directly.
**When to revisit:** Before this framework is reused for a second book — not blocking any current Stoic Husband work.
**Status:** OPEN, non-blocking, deferred.

### [#5] — [2026-06-12]
**Question:** Where does the Stoic Evening Review ("the Stoic Prayer" — Seneca's nightly self-examination: What did I do well? What did I do poorly? What did I leave undone?) belong as a recurring motif across the book?
**Context:** The author wants to highlight this practice — documented in `sources/author-notes.md` (line 223, "Evening self-examination (Seneca)"; lines 328-329, "The Evening Stoic Review (What the Author Calls 'The Stoic Prayer')") — and ties it directly to the book's "man lying in bed reflecting" bookend (resolved this session, replacing the earlier "man in his car" opening — see `03-outline.md` Introduction/Conclusion edits, 2026-06-12). The Conclusion's "final charge" bullet now anchors the three questions as the book's closing image. Open question was whether it should ALSO appear earlier.
**Decision (2026-08-04):** Not the Introduction — that's locked, author-finalized manifesto text (revise only via `/book-feedback introduction`), and adding a whole new practice there risks diluting a piece that's already done. Instead, a three-beat arc: (1) **Ch1** already has an unnamed taste of it — its Practice item #2 ("that night, or the next morning, walk back through what happened and ask, *was I being the best husband I could be?*") is structurally the same move, using the four virtues instead of Seneca's three questions; (2) **Ch24 (The Marriage You Build Every Day)** formally names it and grounds it in Seneca's own practice — its whole thesis is daily-practice-compounds-over-time, the natural place to introduce it by name rather than as an abstract front-matter gesture; (3) the **Conclusion** (already planned) echoes it as the closing image. No change needed to the Introduction or Prologue.
**When to revisit:** Ch24's research/draft pass, to actually write the Seneca-grounded version described above.
**Status:** OPEN, non-blocking, no urgency — plan decided, not yet executed.

### [#8] — [2026-06-17]
**Question:** Connect Buffer for automated social media posting to X, Instagram, and Facebook at the end of `/book-chapter-publish`.
**Context:** Discussed 2026-06-17. Buffer ($6/mo) has an MCP server, supports X/IG/FB (the three target platforms), and would let Claude push social.md content to Buffer drafts immediately after the Substack push step. Author has a premium X account and existing IG/FB presence. Deferred to complete Substack integration first — Buffer is the natural next layer once the Substack draft push is stable and the onboarding pattern is proven.
**When to revisit:** After the Substack MCP integration (`/book-substack-connect`) is working end-to-end — natural next session.
**Status:** OPEN, non-blocking, deferred.

## Resolved Items

### [#28] — [2026-08-17] — Resolved [2026-09-01]
**Question:** What should happen when the author rejects prose that the outline commissions? Nothing in the corpus covered the collision, and resolving it silently cost a full gate cycle on Chapter 10.
**Resolution (2026-09-01):** The second occurrence arrived during Ch11 and funded the answer, exactly as this item predicted it would. **The rule is: when author feedback and a commissioned spec element disagree, say so out loud in the same turn, then revise the spec rather than keeping prose he rejected.**

Ch11 made the answer obvious because the collision was not marginal there. The author re-scoped the chapter across three exchanges, which invalidated the premise, all key points, the central story, the Stoic principle, and the ah-ha. Keeping the outline stale would have failed the finished chapter at the conformance gate for elements it no longer contained — the Ch10 failure again, one chapter later, at five times the size.

**What was actually done, and is now the pattern:** the `03-outline.md` entry was rewritten alongside the brief, in the same pass, with the reason recorded inline in the entry itself. Every such revision carries a dated note saying what the spec used to say, what changed, and why. Ch9, Ch10, and now Ch11 all carry one. The gate reads the outline, so the outline is what has to move.

**Why this needs no new rule.** The existing precedent already said it — "a spec revision is legitimate when the specification was genuinely wrong, and the reason has to survive in writing," recorded in the Ch9 and Ch10 outline notes. What was missing was not a rule but the instruction to *raise the conflict at the moment it appears* instead of resolving it silently and discovering it two stages later. That now sits in `book-chapter-research.md`'s Step 3.5, which surfaces the frame before a brief is built on it, and it is the same fix: name the disagreement early, where it costs one exchange instead of a cycle.
**Status:** RESOLVED

### [#25] — [2026-08-17] — Resolved [2026-08-27]
**Question:** Is "no references to other chapters in prose" a standing rule for the whole book, or a preference applied to Chapter 10 only?
**Resolution (2026-08-27, author):** **Neither. Referencing is allowed; the requirement is on how.** In his words: "yes, you can name it. just make sure it's a complete thought so that the chapter could theoretically stand on its own... my biggest concern was somebody coming back to the book after putting it down for a week and being lost because they can't remember a previous chapter. So it's more about how you reference the previous chapter, not the actual referencing itself."

**The operative test:** a reader who has forgotten the earlier chapter entirely, or who is reading this chapter first, must lose nothing. A reference must therefore carry the referenced idea with it, not point at it. "Chapter 7 covered the ledger" fails the test, because it hands a reader with no memory of Chapter 7 a dead pointer. "Chapter 7 was about the tally you keep of who does more around the house" passes, because the sentence contains what it refers to.

This reframes the Ch10 objection: what he cut there was not a reference, it was an *inefficient* one. It also means the existing 21 instances across nine chapters need auditing against the test rather than removal, and `04-archetype.md`'s "Callback" opening type stands unchanged.

**Not yet recorded as a rule.** The natural home is `01-voice.md`'s Always Do list, and it would be an addition under a net-zero policy. Proposed, not applied.
**Status:** RESOLVED

### [#27] — [2026-08-17]
**Question:** Write a short preamble before each of Parts I, II, and III introducing that Part's element (the calming river, the sturdy oak, the warm sun), so the elements reach the reader once per Part instead of inside individual chapters.
**Context:** Surfaced during the Chapter 10 draft check-in, as the author's stated reason for cutting that chapter's "the oak holds firm" refrain: the elements get one clear introduction per five-or-six-chapter arc, and chapters then run on their own language without naming the element again. This is consistent with what the book already does everywhere else — a scan this session found that no numbered chapter has ever named an element in prose; only the Introduction does, 27 times, as the manifesto. The Ch10 first draft was the sole exception and has been corrected. **This item is load-bearing for Ch10 specifically:** that chapter's mechanism (boundaries are the structure everything grows inside) is now carried in plain language on the assumption that a Part II preamble supplies the oak. If the preambles never get written, Ch10 is the chapter that quietly loses its grounding, and nobody will remember why. No skill generates Part preambles today; `03-outline.md` has Part headers with a one-line italic arc descriptor, which is the natural home.
**When to revisit:** Before Part II is compiled for any real reader, or whenever the Part-header structure in `03-outline.md` is next revised.
**Resolution (2026-08-23):** Done, and expanded past the original scope.
All five Parts got an opening, not just I–III: with pages on only three of
five, the book's furniture visibly disappears at Part IV. Parts IV and V
were retitled from descriptions to movements ("Fall to Winter," "Spring to
Summer") so a reader sees three nouns and two movements on the contents
page and perceives two kinds of thing. They name all three elements rather
than introducing a fourth, which is what keeps River/Oak/Sun the identity
set. Part I was renamed The Steady River in the same pass, since "calming"
promised conflict avoidance against Chapter 5's argument. Stored at
`parts/part-N-<slug>.md`, tracked as `stages.parts` in the manifest, emitted
by `/book-compile` Step 2.6; form rules in `parts/README.md`. **Ch10's
grounding is now supplied** — this item flagged that the chapter's
plain-language boundaries material assumed a Part II opening would carry
the oak, and `part-2-sturdy-oak.md` does.

**Status:** RESOLVED


### [#4] — [2026-06-11] — Resolved [2026-08-04]
**Question:** Should `05-framework.md` (the Oak/River/Sun × Four-Virtues reference matrix) be wired into the chapter pipeline as a conditional reference, mirroring `04-archetype.md`'s "if it exists, read..." pattern?
**Resolution:** Items (a) and (c) completed, closing out the partial resolution from 2026-07-11 (item (b), the `book-feedback.md` alias rows, was already done). (a): added a conditional "if it exists, look up this chapter in the Chapter Traceability Index and read its Cell Details entry" step to `book-chapter-research.md` (Step 2), `book-chapter-draft.md` (Step 2), and `book-chapter-refine.md` (Step 2) — same placement pattern as each file's existing `04-archetype.md` read, additive and a no-op for books without the file. (c): added a "`05-framework.md` (optional reference matrix)" paragraph to `CLAUDE.md` documenting the pattern for future books, placed after the Phase 1 command block. Done now (before Chapter 10) rather than deferred, since the remaining 20 chapters are exactly where automated cell-grounding starts paying for itself over ad hoc awareness.

### [#18] — [2026-07-28 10:30] — Resolved [2026-08-04]
**Question:** Audit `/book-chapter-refine`'s auto-generated Practice sections (distillation) across the book for whether they skew reactive-only, and reframe them to include proactive countermeasures where a chapter's lesson supports it — not just after-the-fact fixes.
**Resolution:** Folded into a broader `/book-distill --refresh` pass across Chapters 1-9, triggered by the author comparing Ch9's distillation quality (written under the fully current pipeline) against Ch1-8's, which had only ever been bulk-retrofitted on 2026-07-28, not independently regenerated. That retrofit had backfilled `Lesson`/`Challenge` fields from `tactics-review.md` rather than composing them fresh, producing near-verbatim duplication against each chapter's Full Distillation paragraph in Ch01, Ch03, Ch04, Ch05, Ch06, and Ch08 — a real defect this audit surfaced as a side effect of reviewing every chapter's content closely. Fixed alongside the proactive/reactive review: reviewed all nine chapters' Practice sections against the reactive-vs-proactive distinction this item asked for (not just Ch5/Ch8, which were the only two touched by the original 2026-07-28 partial fix). Three chapters got a genuine proactive item added or swapped in, replacing a redundant or purely reactive item: Ch3 (a weekly direct question to her, replacing a reactive clarifying-question tactic), Ch6 (a weekly habit of naming one item from her "bucket" of unscheduled work, replacing a one-time reflective exercise), and Ch9 (a weekly habit of voicing one want before it joins the unspoken list, replacing a near-duplicate reactive item). Ch1, Ch2, Ch5, Ch7 already had a genuine proactive anchor and were left structurally as-is (Lesson/Challenge text tightened for the duplication issue, Practice unchanged). Ch4 and Ch8 were judged legitimately reactive-heavy or already balanced, per `book-distill.md`'s own guidance not to force a proactive item where the chapter's principle is genuinely about catching something as it fires. Ch9's distillation also had its `Lesson`/`Challenge` fields added for the first time, having been rebuilt on 2026-08-03 after the schema existed but before those fields were populated. `appendix/practice-guide.md` updated to match the three changed Practice lists. See `progress.md`, 2026-08-04 entry, for the full per-chapter breakdown.

### [#19] — [2026-07-28 14:00] — Resolved [2026-08-04]
**Question:** Delete stale remote branches from your laptop (or the GitHub Branches UI) — this cloud session cannot remove them itself.
**Resolution:** Author deleted the branches directly from their desktop, where the HTTP 403 this cloud session hits on `git push origin --delete` doesn't apply. Not independently re-verified by this session — if any of the 14 confirmed-merged branches or the `claude/book-next-mf6x9d` citation-recovery case turn out to still be present, re-open. **Verified 2026-08-14:** re-audited from the laptop. The 14 merged branches were gone; `claude/book-next-mf6x9d` was still present but its citation commit had already reached `main` (0 commits ahead), so it was deleted along with `claude/chapter-9-review-5nx8w5`. Nothing was lost.

### [#16] — [2026-07-24] — Resolved [2026-08-04]
**Question:** Should Chapter 7 get a scoped re-refine pass to bring its sentence-length distribution back under the new counted rule in `01-voice.md`?
**Resolution:** Initially accepted as a grandfathered exception, then reconsidered same day — the cap was deliberately calibrated below Ch7's own value specifically so future chapters wouldn't drift that high, so documenting a permanent exception left a real asterisk on the rule. Ran the scoped pass instead: 10 of 14 long sentences (25+ words) split using the same surgical approach as Ch8's recalibration, content unchanged. Verified by recount: 13.9% (14/101) down to 3.5% (4/113), comfortably under the ≤10% cap. See `chapters/ch07/refined.md`'s Editor's Notes (2026-08-04 session) for the full breakdown. Closes `.claude/LEARNINGS.md` item #2.

### [#6] — [2026-06-15] — Resolved [2026-08-04]
**Question:** Delete the five stale remote branches that couldn't be removed from the OKF-integration session, and recover the Chapter 6 research if it still exists on the laptop.
**Resolution:** Author deleted the five branches directly from their desktop. Chapter 6 research recovery is moot — Chapter 6 has since been fully researched, drafted, and refined through the normal pipeline (see `progress.md`), so the original research draft was never needed.

### [#17] — [2026-07-27] — Resolved [2026-07-28]
**Question:** Delete four now-fully-merged remote branches that this cloud session cannot remove itself.
**Context:** `claude/book-resume-p53zua`, `claude/book-status-endpoint-uwycjl`, `claude/parking-lot-review-ivkcul`, and `claude/stoic-husband-writing-style-eoumnm` were merged into `main` this session (Chapter 8, the Prologue/Introduction split, and assorted agentic-system fixes — see progress.md 2026-07-27 entries). All four were confirmed 0 commits ahead of `main` post-merge — safe to delete. `git push origin --delete` returns **HTTP 403 Forbidden** from this environment's git proxy, and the GitHub MCP server exposes no delete-branch tool — the same wall hit before (see resolved item #6 below, 2026-06-15).
**Resolution:** Superseded by item #19. A broader audit on 2026-07-28 (`git branch -r --merged origin/main`, the direct git mechanism rather than a manual diff check) found these same 4 branches plus 10 more all fully merged, and one additional branch with real unmerged content needing review. Item #19 carries the consolidated list and the single delete command; this item is closed rather than duplicated.

### [#11] — [2026-07-11] — Resolved [2026-07-26]
**Question:** Finish the personal-story half of the Introduction.
**Resolution:** Restructured rather than simply finished. The single-file "manifesto + personal story" plan from 2026-07-11 was abandoned: the two pieces are now split into a separate Prologue (the author's personal story) and Introduction (the River/Oak/Sun manifesto, unchanged from the author's finalized text). The author completed the interview across this session and two prior turns. Along the way, an initial personal-story draft opened on a man lying awake replaying a fight — the author caught that this duplicated Chapter 1's actual opening ("The Three-Second Window") almost beat for beat, and also felt the draft "wasn't positive enough." Rewritten to open on direct-address truisms (marriage is hard but worth it, men are strong everywhere except this one domain, everyone is quietly making it up as he goes) and bridge into the author's story with "I was in the same boat, same as you. And that was fine. Until it wasn't." — a line that also closes the piece. The `chapter-writer` sub-agent (Opus) then produced the final prose pass for closer voice match; its self-reported counted-rule verification undercounted the "not X, it's Y" reframe device (claimed 2 instances, actually 3) and a three-sentence parallel run ("A man who is only steady... only warm... only strong...") repeating one sentence shape three times — both caught and fixed on independent verification before saving, per the voice constitution's "count, don't estimate" rule.

Both pieces are now stored and tracked exactly like a numbered chapter, just without a number: `chapters/prologue/refined.md` and `chapters/introduction/refined.md`, tracked in `book-manifest.json` as `stages.chapters.prologue.refined` / `stages.chapters.introduction.refined` (non-numeric keys sharing the `chapters` dict with numbered chapters). This required a real fix to `scripts/pipeline_state.py`: its `phase_label` refined-chapter count was summing over all dict values regardless of key, so it briefly reported "9/28 chapters refined" instead of 7/28 until the count was scoped to zero-padded numeric keys only. `03-outline.md` now has a proper Prologue entry and a corrected Introduction entry (word count targets no longer forced to the old single-file 1,800–2,200 range; Prologue ~1,700–1,900, Introduction ~950–1,050 as its natural manifesto length). `.claude/commands/book-compile.md`, `book-intro.md`, and `book-feedback.md`'s alias table were updated so this convention persists on future runs and compiles rather than being a one-off manual save. `CLAUDE.md`'s Prologue/Epilogue paragraph updated to reflect that a Prologue is no longer purely hypothetical.

### [#10] — [2026-07-11] — Resolved [2026-07-11]
**Question:** Should `ch02/refined.md`'s "flat water doesn't test anything" passage and its "armor"/"foundation the warmth stands on" passage be re-edited to pull from the now-canonical River/Oak/Sun language?
**Resolution:** Split decision. The "flat water"/"sea legs" passage (lines 52–54) was actually nautical/ocean imagery, not river imagery — swapped for river language ("hold steady when the current's easy," "keep flowing when the terrain changes"), a same-family fix rather than a new stacked metaphor, since `05-framework.md` already classifies this chapter as River × Temperance ("Governed Inner Weather"). The "armor"/"foundation the warmth stands on" passage was left untouched — "armor" is a deliberate cross-book motif (it's the Sun × Justice failure-mode name in the hidden matrix, and Ch2's own corrective section already builds toward it), and pulling in Oak's "load-bearing" language would mismatch this River-chapter and stack a third metaphor family. Edited via a scoped `/book-edit`-style pass (not a full chapter re-edit) — see `chapters/ch02/refined-prev.md` for the prior version.

### [#7] — [2026-06-15] — Resolved [2026-07-11]
**Question:** Should "Brave enough to stay engaged" (the fourth virtue from Ch1) be explicitly identified as the Stoic cardinal virtue of Courage — i.e., framed as "Courage, translated to: brave enough to stay engaged" — rather than standing as an unlabeled fourth item?
**Resolution:** All four virtues got the treatment, not just Courage (Wisdom → Logical, Justice → Kind, Temperance → Self-controlled, Courage → Brave enough to stay engaged), applied only at Ch1's first introduction of the four beats — not at the later callbacks (Ch1's own "Mistake I Made First" section, or Ch3's "the fourth virtue from Chapter 1" line), which stay in plain language since the reader already has the definition by then. The bold beat labels themselves (**Logical.**, **Kind.**, etc.) were left unchanged — `04-archetype.md` references them by name as the reference implementation of the beat-label convention, and the classical names read better as a one-clause follow-on than as part of the label itself. Each of the four follow-on sentences uses a different construction to avoid the counted rhetorical-device-repetition rule. See `chapters/ch01/refined-prev.md` for the prior version.

### [#2] — [2026-06-10 10:25] — Resolved [2026-06-11]
**Question:** The outline's per-chapter "Word count target" ranges sum to roughly 37,000 words across all 27 chapters, but `03-outline.md` states "Target total word count: 50,000–65,000 words." Which number is the real target — and how should the gap close: lengthen per-chapter targets, account for additional content (Introduction, Conclusion, appendix) toward the total, or revise the stated range down to match the chapter-level math?
**Resolution:** Tight field manual, by design. Real numbers: 27 chapter targets sum to ~33,450 words (midpoint); chapters 1–5 are actually running ~1,400 words avg (manuscript.md = 6,998 words / 5 chapters), slightly above target — not an underwriting problem. Adding Introduction (2,000) + Conclusion (1,750) + current-pace appendix (~2,200 across 27) lands the realistic total at ~43,000–46,000 words — a normal length for a tight, practical field manual (comps: *Make Your Bed* ~28K, *The Coaching Habit* ~38K), and the brevity matches the "no fluff" Stoic brand. `03-outline.md`'s stated target revised to **42,000–50,000 words (tight field-manual format)**. No per-chapter padding — chapters 1–5 are landing well at their current length and stretching them risks diluting voice that's already working. The practice guide appendix (currently ~80 words/chapter) remains a lever to expand later if more length is wanted — not committed now, can be revisited any time via `/book-distill --refresh`.

### [#1] — [2026-06-10 10:25] — Resolved [2026-06-11]
**Question:** Should the four virtues from Ch1 (logical, kind, self-controlled, brave enough to stay engaged — mapped to the Stoic cardinal virtues) function as explicit signposts in later chapter transitions, especially across Part II, or remain background architecture established in the Introduction and Ch1?
**Resolution:** Background architecture. `05-framework.md`'s "reader-facing rule" settles this — the full Oak/River/Sun × Four-Virtues matrix is internal architecture; no chapter shows the reader the whole grid, and each chapter lives inside one cell. The four virtues inform chapter tone and content via the framework reference, not as explicit "this is the Wisdom chapter" signposts in transitions. Ch1's existing four-virtues framing in the Introduction/Ch1 stands as already decided; later chapters don't need to echo it explicitly.
**Clarifying note (2026-07-11):** This resolution still stands for the four cardinal virtues (Layer 2 of `05-framework.md`'s matrix) — they remain background architecture, unchanged. What changed on 2026-07-11 is Layer 1 only: the River/Oak/Sun elements themselves (not the virtues inside them) are now explicit, reader-facing content via `00-premise.md` and `okf/frameworks/the-river-the-oak-and-the-sun.md`. Do not read that change as reopening this item — the virtues stay hidden either way.

### [#3] — [2026-06-11 11:25] — Resolved [2026-06-11]
**Question:** EPIC / ROLLOUT TRACKER — Execute the Oak/River/Sun × Four-Virtues architecture rollout across the book (originally an 8-piece multi-session checklist).
**Resolution:** Superseded by a scoped-down approach. `05-framework.md` is trimmed to pure reference content (the 3×4 matrix, Part→element map, cell details, and chapter-traceability index), following the same "optional reference document" pattern as `04-archetype.md` — read informally, revised via `/book-feedback`, not a synced source of truth. Part I–III renamed in `03-outline.md` (The Calming River / The Sturdy Oak / The Warm Sun). No bespoke propagation protocol or decision log — future edits to `05-framework.md` go through `/book-feedback`, with downstream impact (if any) surfaced via `/book-sweep` and addressed per-chapter via `/book-edit`/`/book-chapter-refine`, exactly like any other foundation artifact. If the author later wants to revisit premise or voice with the framework's anti-"cold" thesis in mind, that's an ordinary `/book-feedback premise`/`voice` session — no tracking needed. Remaining optional pipeline-wiring work moved to new lightweight item #4.
