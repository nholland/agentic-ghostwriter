# Final scoped coherence review — Chapter 13 (round 2, 2026-09-27)

FAIL: all six round-1 prose essentials (E1–E6) are resolved and E7/E8 are correctly deferred to the author, but the rewrite introduced three new essentials — the negated-reframe construction now carries the chapter roughly eight times against a cap of two, the river reconciliation sentence contradicts the Introduction's own definition of the river, and Ch12's "asking again on Thursday" beat is now reused as the reader's hypothetical (the same failure class as round-1 E5, and my round-1 fix text is what introduced it). All three are one-sentence-scale repairs; none requires new research or an author ruling.

Separately, the Editor's Notes claim "no single prose sentence in the chapter runs 25 words" is false. At least six do.

---

## Round-1 essentials, judged

### E1 — love-languages re-explanation. RESOLVED.
Now L53: *"You met the five love languages a chapter ago: time together, words, service, gifts, touch. Use it as an inventory of what you've let fall away. If you mostly tell her you love her, what hasn't she gotten in a year?"*
The not-a-science caveat and the theory-of-use are gone; what remains is a recall plus the section's working question. The author's boundary (`author-feedback-2026-09-24.md` line 21) is met. One low note below on "a chapter ago."

### E2 — one sentence-shape carrying the chapter (short-imperative triad). RESOLVED as written.
Imperative triads are now two, exactly as the spec allows: L51 *"Reach for her hand on a walk. Sit close enough on the couch that she can feel you're there. Find out whether a hug is what helps at the end of a hard day, rather than assuming it is."* and L75 *"Plan the dinner she'd enjoy. Write down one memory that still makes you glad you married her. Start early enough to mean it."* The words-of-affirmation triad is now declarative (L49) and the remembering triad is now a Monday-to-Thursday scene (L73) — real mood changes, not vocabulary swaps, which is what `01-voice.md`'s "Register shifts" clause demands.
Caveat, reported as a new moderate finding (M1): the *three-short-parallel-sentences* block survives in five places with the mood varied, and the load the triad used to carry has landed on a different device entirely (see N1).

### E3 — recap paragraph as a second ending. RESOLVED.
The six-imperative summary is cut. L85 ends *"What wears on a marriage is going through every shared hour as though there were nothing left to find out,"* then the divider, then one closing sentence: *"Put the phone down, and give her the evening you came to share."* Nothing follows it.

### E4 — "from habit" against Ch12's positive habit. RESOLVED.
L75: *"Anniversaries and Valentine's Day lose their meaning when you handle them by rote."* The word "habit" appears nowhere in Ch13 prose, so Ch12's Epictetus valence is intact.

### E5 — Ch12's forgotten-anniversary beat handed to the reader. RESOLVED.
L77: *"Some years are crowded and hard. You may both be too tired to plan anything, and a quiet evening at home is the honest version of the day. You don't owe the calendar a performance."* The forgotten anniversary and the shared laugh are gone. But see N3: a different Ch12 detail took its place.

### E6 — cold open without orientation. RESOLVED.
L3: *"There's a difference between the time you gave your wife and the time she actually got. The gap between those two is small enough to miss for years."* Two compass sentences before the show scene, and the second carries content rather than winding up.

### E7 — no quotation lands the turn. DEFERRED TO THE AUTHOR (inbox #106). Not a blocker.
Still true of the prose: the chapter contains no quotation from anyone, and the Seneca/Heraclitus river remains a paraphrase in the second-to-last section. Fixing it needs a line confirmed against the author's own copy (Rule 3), which is his call. One thing did improve without a quotation: the outline's assigned principle now lands explicitly in prose at L19 — *"A choice isn't something you made once. It's something you either keep making or quietly stop making."* That closes round-1's O3 even while E7 stays open.

### E8 — outline transition and word target out of step with the author's ruling. DEFERRED TO THE AUTHOR (inbox #105). Not a blocker.
Prose is 1,803 words against the outline's 1,000–1,300, on the author's explicit expansion instruction; the Ch14 seam stays unbuilt per his removal order. My round-1 substantive answer stands: the chapter hands off to Ch14 sensibly through Perel (L81) and the boredom finding (L85) without pre-teaching miswanting or the composite rival, and the close returns to the wife. No Ch13 prose change is owed.

---

## New essential findings (introduced by the rewrite)

### N1. The negated-reframe construction is now the chapter's default gear — roughly eight instances against a cap of two.
`01-voice.md`: *"A reframe ('That's not X. That's Y.'), a negated comparison ... No single device repeats more than twice in one piece."* This is the first-named example in that rule, and the round-1 fix moved the chapter's instructional weight straight onto it. Instances, quoted:

- L17 *"You haven't stopped loving her. You may have stopped spending any thought on her."*
- L19 *"A choice isn't something you made once. It's something you either keep making or quietly stop making."*
- L37 *"she doesn't usually decide you've stopped loving her. She decides she's been accounted for."*
- L39 *"None of that arrives as an announcement. It arrives as a wife who has gotten used to asking for less."*
- L61 *"Taking initiative means being willing to notice and learn, not deciding you know her business better than she does."*
- L61 *"The point isn't that she never asks. It's that she doesn't have to ask for everything."*
- L63 *"But you were never handing her a slice of the bank balance. You were telling her she was on your mind while she wasn't in the room."*
- L71 *"The bar isn't a grand surprise. It's knowing her well enough that an ordinary gesture is unmistakably hers."*
- L85 *"That's a reason to watch the pattern, not a prediction about your marriage."*

Plus softer members of the same family at L9 (*"You made time for her both nights, and that counts for something. What she wanted was your attention, and you had it somewhere else."*) and L69 (*"Not the last date you took her on."*). `voice_check.py` reported *"no detectable shape over cap 2"* and its own output says regex cannot see every sentence-shape; this is the shape it missed, exactly as in round 1.

**Fix:** keep two — L19 (it is the chapter's assigned principle and the strongest) and L71. Convert the rest to flat assertions, questions or scene beats. L37: *"she decides she's been accounted for."* L39: *"That never arrives as an announcement. It shows up as a wife who has gotten used to asking for less."* → better still, cut the meta-sentence and let the three behaviors before it stand. L61a: *"Notice, then ask. You don't know her business better than she does."* L61b: *"She can ask. She shouldn't have to ask for everything."* L63: *"You were telling her she was on your mind while she wasn't in the room."* (drop the negated first half; the objection is already stated two sentences earlier). L85: *"Watch the pattern. It isn't a prediction about your marriage"* → *"That's a pattern worth watching. It says nothing about your marriage in particular."*

### N2. The river reconciliation misstates the book's own river.
L83: *"You know that picture from this book as your own steadiness under pressure. Seneca used it for change first."*
The Introduction (`chapters/introduction/refined.md` L19–25) defines the river as calm **and adaptable**, explicitly about change: *"The river does not demand that the world remain unchanged. It learns how to keep flowing through what has changed."* So the contrast the sentence builds is false on its own book — the reader has not met the river as steadiness-instead-of-change, he met it as steadiness *through* change, which is Seneca's use. This is a cross-chapter contradiction between anchor-metaphor definitions, and it is the one category the per-chapter pass cannot see.

**Fix, keeping the sentence:** *"You've met that river in this book as the man who keeps his direction while the water changes around him. Seneca pointed it at the person next to you."* Or take the Line Editor's own offer and cut both sentences; the paragraph works without them.

### N3. Ch12's "asking again on Thursday" beat is now the reader's hypothetical.
Ch13 L73: *"On Monday she said this week would be hard at work. Thursday is when asking about it means something."*
Ch12 L49 (landed): *"To her, love is you asking about the meeting she's been dreading, then asking again on Thursday, because you remembered there was a Thursday."*
Same beat, same device, same day-name, one chapter later. This is the E5 failure in a second instance, and it came from my own round-1 suggested replacement text — my error, and it should be corrected rather than inherited. Ch12's Thursday is one of the two lines that make its love-languages section land; reusing it drains it.

**Fix:** keep the Monday-to-later-in-the-week structure, change the instance and the day. *"She told you Monday that the review was Wednesday. Asking how it went on Wednesday night is the part she'd notice."*

---

## New non-essential findings, ranked

**M1. The three-short-parallel-sentences block is the chapter's default paragraph shape (five places).** L13 (*"You paid attention... You remembered... You brought her..."*), L39 (*"She stops mentioning... She organizes her own birthday. She says 'whatever you want'..."*), L51 (imperative), L59 (*"The dishes are visible. Her car is low on gas. There was an errand she mentioned yesterday."*), L75 (imperative). Each is a legal mood under the letter of E2's fix, and two of the five are genuinely good (L39's consequence chain, L59's inventory). I am not calling it a device violation, but a reader meets the same rhythm once per section. Breaking one of L13 or L59 into ordinary prose would settle it.

**M2. The Editor's Notes long-sentence claim is false.** The notes say *"no single prose sentence in the chapter runs 25 words."* At least six do, by hand count: L57 (31), L85 *"Spouses who called their marriage boring..."* (30), L31 *"The following Tuesday, you ask where the first bed is going..."* (30), L37 *"The plain word for that is being taken for granted..."* (29), L27 *"She's been saving pictures of a garden..."* (25), L75 *"Ten minutes from home you swing into Walgreens..."* (25). The script's 13/139 = 9.4% is not what I am disputing — I do not own counts, and I did not re-run anything. What I am reporting is that the notes' explanation of that number ("all artifacts of a run-in header joining the sentence before it") is wrong, which is a Rule 12 problem in the apparatus even though the apparatus does not land. The three header-concatenation artifacts the script printed are real; the conclusion drawn from them is not. If the split were corrected, the true long-share is plausibly still inside the cap, but nobody has counted it.

**M3. Metaphor stack.** Beyond the phone frame (L5 → L45 → L89, which is the chapter's real anchor and works), the prose carries *"furniture in her own marriage"* (L37), the river (L83), and *"you've been hearing her the way you hear the radio"* (L29). `01-voice.md`: *"One concrete image per chapter, max."* The furniture image is the outline's own wording and the Line Editor flagged it as reversible; the radio simile is the cheapest of the three and the easiest to drop (*"and you've been half-hearing it for months"*).

**M4. Late-chapter first-use gloss of "the Stoics."** L19: *"The Stoics were Greek and Roman teachers who cared less about what a man believed than about what he did on an ordinary Tuesday."* By Chapter 13 the reader has met them a dozen times; the house pattern (Ch12) glosses the individual figure at his own first substantial use, not the school. The second half of the sentence is the good part. Suggest: *"What the Stoics cared about was less what a man believed than what he did on an ordinary Tuesday."*

**M5. The hypothetical frame wears off, then addresses the reader as fact.** The section opens *"Say you decide to take her out after twelve years"* (L23), which is the right marker, but four paragraphs later L33 asserts *"She's had twelve years you didn't live inside, even though you were in the house for most of them"* as a statement about the reader. The garden, the lake town and the nursery are safely inside the frame; this sentence steps outside it. Suggest *"She's changed across the years you spent in the same house"* — the point survives without the number.

**M6. Indirection at L69.** *"A date is one evening; this is wider than that."* The clause gestures at the plain noun. *"A date is one evening. Romance is bigger than that."* Same line, the semicolon is also off-register for a 6th-grade target.

**M7. "You met the five love languages a chapter ago."** Ch12's backward reference (*"You've already had the one about giving sixty and expecting forty"*) does the same work without pointing at the book's structure. *"You've met the five love languages"* costs nothing and keeps the artifact standing on its own.

**M8. "Tuesday" three times** (L19 *"an ordinary Tuesday"*, L31 *"The following Tuesday"*, L85 *"The show you watch every Tuesday"*). Each earns its place locally; together they read as one writer's default day. Change L19 or L85.

---

## Claims against the addendum: clean, with one wording note

**Tsapelas, Aron and Orbuch (L85)** against `research-addendum-2026-09-24.md` line 14 (*"in 123 still-married couples, year-seven boredom predicted lower year-sixteen satisfaction after baseline satisfaction was controlled"*):
prose reads *"Spouses who called their marriage boring in year seven reported less satisfaction nine years later, even after the researchers accounted for how satisfied those spouses had been to start with."* Supported. Year seven to nine years later is year sixteen; "reported less satisfaction" is weaker than the addendum's "predicted lower satisfaction," which errs in the safe direction; the baseline control is stated; and the next sentence refuses the causal reading (*"That's a reason to watch the pattern, not a prediction about your marriage"*). The addendum's concession that ordinary familiar evenings are not the problem is honored at *"The show you watch every Tuesday can be familiar and good."*
One wording note, low: *"Tsapelas, Aron and Orbuch followed married couples for years and published the results in 2009"* implies the three authors ran the longitudinal study. They analyzed an existing long-running marriage panel. *"Tsapelas, Aron and Orbuch published a 2009 analysis of couples followed for sixteen years"* is truer and no longer. The sample restriction (couples who divorced before year sixteen are excluded) is not in prose and, given the scoped claim, does not need to be.

**Perel (L81):** *"Esther Perel is a therapist who writes about desire in long relationships. Her argument is that familiarity can settle into routine, and that curiosity and new experience help keep desire alive."* Framed as her argument, not a measured result, per the addendum. Supported. Round 1 had "can help keep"; the "can" is gone, which is marginally firmer, but "Her argument is that" carries the hedge.

**Rosenfeld and the GSS infidelity analysis:** absent from prose. Correct.
**Love languages, mental load, gifts:** no research asserted in prose; the gifts paragraph now reads *"You were telling her she was on your mind while she wasn't in the room,"* which is an intention rather than a promised outcome, clearing round-1 optional item 6.
**No quotation was added anywhere, no citation is marked verified, no placeholder stands in prose.** Confirmed by read.

---

## Things I checked and found sound

No wife-as-threat framing; no *undefended / absorb / infected / defense* aimed at her. No universal claim about all men in the narrator's voice; L37's *"she doesn't usually decide"* and L57's *"Maybe acts of service are what land best with her"* are correctly scoped. No moral-failure verdict: L15 earns L17 by naming why the effort faded and calling the security good before the diagnosis arrives. No scene from the outside — the reader is the man in every scene. No performative vulnerability (no first-person material at all, so no new biographical claim and no contradiction with Ch12's twenty-four years). No absolutist dialogue. No invented foil: the shared-bank-account objection (L63) and the familiar-Tuesday-show concession (L85) are both the author's own instructions, not planted doubts. No corporate or therapy register; round-1's *"Presence is more than a good conversation"* is now *"It isn't only about talking."* No windup sentences found. No "move/moves" as a transfer verb. Terminology matches Ch12 (acts of service, touch, words, gifts; *"worked to win her"* against Ch12's *"trying to win favor"*). The author's removal order holds: no noticing-other-women passage, no comparison transition. The phone frame is a genuine structural anchor and the close is one sentence in his own image.

---

## Coverage

I read in full: `/home/user/agentic-ghostwriter/runs/ch13/refined.md` (prose and Editor's Notes), my round-1 report `/home/user/agentic-ghostwriter/runs/ch13/coherence-refined.md`, `/home/user/agentic-ghostwriter/books/the-stoic-husband/chapters/ch12/refined.md`, `/home/user/agentic-ghostwriter/books/the-stoic-husband/01-voice.md`, `/home/user/agentic-ghostwriter/runs/ch13/author-feedback-2026-09-24.md`, and `/home/user/agentic-ghostwriter/runs/ch13/research-addendum-2026-09-24.md`. In `/home/user/agentic-ghostwriter/books/the-stoic-husband/03-outline.md` I read lines 255–324: the tail of Ch12, all of Ch13 and Ch14 with their transitions, and Ch15–16 for onward context. For N2 I read the river passages of `/home/user/agentic-ghostwriter/books/the-stoic-husband/chapters/introduction/refined.md` (lines 3–101 via search hits) and the river rows of `citation-queue.md` and `04-archetype.md`. Hand counts for M2 are my own tally of candidate long sentences, done by counting words in each; I did not re-run any script.

I did not read: `runs/ch13/draft.md`, `refined-before-feedback.md`, `persona-refined.md` (the Reader Panel's round-1 FAIL — so I cannot certify the rewrite satisfied the panel, only the coherence essentials), `revision-notes-2026-09-24.md`, the round-2 distillation, practice-guide section, plate or PDF; any chapter other than Ch12 and the Introduction's river sections, so every cross-chapter statement here about Ch01–Ch11 and the Prologue is carried from the two prior whole-book reports rather than re-verified; `02-audience.md`, `00-premise.md`, `05-framework.md`, `06-sources.md`; any OKF concept or citation file beyond the one `citation-queue.md` row; the text of inbox items #094–#106 other than the two the brief identified by number.

I ran no counts of the counted rules. `voice_check.py` owns those, I neither re-ran it nor verified the block quoted in the Editor's Notes, and M2 disputes a sentence of prose in that note, not a number the script printed. I verified no source externally, confirmed no translation wording, and this report certifies no citation status, no plate, no PDF, and no counted-rule compliance.
