# Final scoped coherence review — Chapter 13 (revised 2026-09-24)

FAIL: seven essential findings. The revised chapter is materially better than the pre-feedback draft on research honesty (no Rosenfeld, no GSS, boredom claim correctly scoped) and it obeys the author's removal order, but it repeats Chapter 12's love-languages explanation against the author's explicit boundary, it leans on one instructional sentence-shape five times, and it ends with a recap paragraph that functions as a second ending.

---

## Essential findings (ranked)

### E1. The love-languages paragraph re-explains what Chapter 12 already explained

Ch13 line 33: *"The five love languages are a popular way to remember that care has more than one form: time together, words, service, gifts, and touch. They aren't a scientific rule that every person has one fixed language. They're useful here because they can show you what you've let fall away."*

Ch12 line 41 (landed): *"You've probably met the five love languages. It's a popular list rather than a science, and nobody has shown that matching hers changes anything. As a tactic rather than a philosophy it does one thing well: it makes you look at all five instead of the one you'd reach for."*

Same three moves in the same order: name the list, deny it is science, state its one use as a checklist against the form you default to. The author's boundary (`author-feedback-2026-09-24.md` line 21) is explicit: *"It can briefly recall the list but should not repeat chapter 12's explanation of it."* A reader going chapter to chapter meets the identical caveat twice in two thousand words.

**Fix:** collapse to a recall, drop the caveat and the theory-of-use. For example: *"Time together, words, service, gifts, touch. Run down the list and find the one you've let fall away. If you mostly talk about how much you love her, what else has she been missing?"* That keeps the section's working sentence (the question) and loses the re-teaching.

### E2. One sentence-shape carries the chapter: the three-short-imperatives list

The cap in `01-voice.md` is two instances of any single construction per chapter. The short imperative triad appears at least five times, once per section, plus a sixth in the close:

- L29: *"Tell her when you admire the way she handled something. Thank her for what she did today, especially the thing nobody else saw. Say she's beautiful when you think it."*
- L31: *"Reach for her hand on a walk. Sit close enough on the couch to feel that you're together. Learn whether a hug helps her feel loved at the end of a hard day."*
- L51: *"Hold on to those details. On Thursday, ask how it went. On Saturday, make the reservation."*
- L53: *"Plan the dinner she would enjoy. Write down a memory that still makes you glad she's your wife. Give yourself enough time to mean it."*
- L65: six imperatives in a row (see E3).

`voice_check.py` reported *"rhetorical-device repetition no detectable shape over cap 2"* and its own output says regex cannot see every sentence-shape. This is the shape it missed, and it is the chapter's default gear. The four bolded run-in headers are themselves imperatives (*"Be there for the time you share." "Do the thing before she asks." "Keep romance from becoming an appointment." "Don't let knowing her become the end of learning her."*), which doubles the instructional register.

**Fix:** keep two of the triads (L31 and L53 are the most concrete) and convert the others to a different mood. L29 as a statement of what already happens: *"She handled something hard this week and you noticed. She has no way of knowing that unless you say it."* L51 as a scene rather than a schedule: *"She told you Monday that this week would be hard. Thursday is when asking about it means something."*

### E3. Line 65 is a summary paragraph, and functionally a second ending

*"Keep asking what she enjoys, then act on what you've learned. Give your full attention to an ordinary evening. Take some work off her hands without making her manage it. Tell her what you admire. Bring home the small thing you remembered. Plan a date with enough care that it feels like you still want to be there."*

Six clauses, each one a section of the chapter restated in order. This is the moral wrap-up the voice spec bans ("Never wrap up with a moral") and the formulaic-list failure in its purest form. The counted single-ending check passes only because the divider and the one-sentence close sit after it; to a reader the chapter ends twice, once in a checklist and once in an image.

**Fix:** cut the paragraph entirely. L63 ends on *"It can wear on a couple to go through every shared hour as if there were nothing left to notice,"* which hands straight to the close. Nothing in L65 is new.

### E4. "From habit" makes habit the failure, one chapter after Ch12 made habit the answer

Ch13 line 53: *"Anniversaries and Valentine's Day can lose their meaning when you handle them from habit."*

Ch12 built its entire argument on the opposite valence, through a quoted Epictetus: *"Every habit and faculty is maintained and increased by the corresponding actions"* (Ch12 L31), then *"Romance works like any muscle: the more you use it, the better you get at it"* (Ch12 L33). Ch12's promise is that habit is what saves romance. Ch13 uses the same word for what kills it. The mechanism is not actually in conflict, the vocabulary is, and the cheap fix is in the unlanded chapter.

**Fix:** *"...when you handle them by rote"* or *"...when you handle them without thinking about her."* Keep "habit" for the Ch12 sense throughout the book.

### E5. Ch12's forgotten-anniversary beat is handed back to the reader as his own

Ch13 line 55: *"You may both be tired, or laugh together because the anniversary passed before either of you noticed."*

Ch12 line 25: *"My wife has gotten every bit as busy, and we've both forgotten our anniversary in a hard year. Get far enough in and you can laugh about it. We do."*

This is the same specific detail — forgotten anniversary, shared laugh — a chapter later, converted from the author's evidence into the reader's hypothetical. The prior panel named Ch12's version as one of the two details that finally make the marriage desirable on the page; reusing it drains it, and a chapter-at-a-time reader will feel the recycling.

**Fix:** keep the permission, change the instance. *"Some years are crowded and hard. You may both be too tired to plan anything, and a quiet evening is the honest version of the day. You do need to notice if thoughtfulness has become rare everywhere else too."*

### E6. Cold open: no orientation before the scene

The chapter starts inside the scene at L3 (*"She asks if you want to watch a show together"*). `01-voice.md` requires 1–3 sentences of orientation first ("A compass, not a curtain-raiser") and lists "Cold open without orientation" as a Red Flag. The orienting statement exists but arrives at L7, after both scenes: *"You made time for her both nights."* Ch12 does this correctly (L3: *"The question that woke me up in my own marriage came in a normal conversation, from a woman who wasn't angry, and it had the answer sitting inside it."*).

**Fix:** one plain compass sentence ahead of L3, no windup. *"There's a difference between the time you gave her and the time she actually got."* Then the show, then the dinner.

### E7. No line from anyone else lands the turn; Seneca is paraphrased into neutrality

Line 61: *"In Letter 58 of his Moral Letters to Lucilius, the Stoic philosopher Seneca draws on Heraclitus's image of a river. Its water changes even while you recognize the river."*

`01-voice.md` Always Do: *"Let someone else's line land the punchline"*, and under Relationship with Evidence: *"Quote them in their actual voice, not paraphrased into neutrality."* Every landed chapter I read alongside this one lands a real quotation at its turn (Ch12 quotes *Discourses* 2.18 and paraphrases *Meditations* 4.24 with attribution). Ch13 has no quotation at all, and its one classical passage sits in the second-to-last section doing thematic work rather than turning anything. The outline's assigned Stoic principle for Ch13 — *"Sustained deliberate choice — love as ongoing election, not past event"* — is also not the principle the river delivers; the river delivers change, which serves key point 3 only.

I am not recommending that anyone transcribe a quotation to fix this (Rule 3). `research-addendum-2026-09-24.md` already names the live options and their constraints: Seneca Ep. 58.23 (Heraclitus river, verbatim wording unconfirmed), Musonius Rufus XIIIA (Lutz translation in copyright, paraphrase only), Epictetus *Enchiridion* 30 (OKF card's evidence provenance disputed in the addendum). **Fix:** an author/citation decision, not a writer's. The smallest version is a confirmed Seneca line at the river paragraph, moved earlier so it turns the chapter; the addendum's own recommendation (Musonius on mutual devotion) would also match the outline's stated principle better than the river does.

### E8. Outline/author-ruling conflict — inbox item, not a prose blocker

Two outline entries are now out of step with the author's 2026-09-24 ruling, and I am reporting rather than resolving them per my brief.

- `03-outline.md` line 279, **Transition to Chapter 14:** *"Pursuit keeps a man reaching for his wife. But reaching isn't the same as being satisfied once he has her — and the same brain that used to chase her is capable of chasing someone else instead. Chapter 14 names that mechanism before it becomes a problem."* The author instructed: *"Remove the passage about noticing other women. Do not use it as a transition."* The outline's prescribed bridge is now forbidden in the prose.
- `03-outline.md` line 278, **Word count target:** 1,000–1,300. The chapter is 1,501 by the house counter, on the author's explicit instruction to expand.

**On the substantive question the brief asks:** yes, the chapter still hands off to Ch14 sensibly without the removed passage. L59 (Perel on familiarity settling into routine, curiosity and novelty keeping desire alive) and L63 (boredom predicting lower satisfaction nine years later) set up Ch14's hedonic-treadmill and "contentment as practiced discipline" material without pre-teaching miswanting or the composite rival, and the close returns to the wife, which is what the panel asked for. Ch12 landed with no forward reference in its prose at all, so no bridge sentence is owed by house style. My recommendation to the author: rewrite the outline transition to run through routine and boredom (*"Pursuit keeps a man reaching for his wife. What it can't settle is what happens when the reaching stops feeling urgent. Chapter 14 takes on contentment as something practiced rather than waited for."*) and restate the Ch13 word target. No Ch13 prose change required.

---

## Optional findings

1. **L7, indirection at the opening's hinge.** *"She wanted the part of you that came with it."* The voice rule's test (can the clause be swapped for the plain noun?) says yes: attention. *"She wanted your attention, and you had it somewhere else."*
2. **L17, freestanding abstraction.** *"The effort that follows deserves just as much of you."* A one-line mini-moral between two concrete passages, and "the effort that follows" gestures at marriage rather than naming it. Either cut it or name it: *"Marriage asks for the same effort courtship did."*
3. **Supposition markers stack up.** *"Imagine asking your wife out after twelve years of marriage"* (L19), *"Suppose acts of service mean a great deal to your wife"* (L37), *"Maybe she pointed out a book weeks ago. Maybe she loves a particular pastry"* (L45), *"Romance in your marriage might be..."* (L49). The book's default is to put the reader in the moment, not to ask him to picture one. L19's hypothetical framing is deliberate and was praised by the panel (it prevents a false biographical claim), so keep that one; L37 can go direct (*"Acts of service matter to your wife"* → the section already assumes it).
4. **L21, filler.** *"Ask sometimes, of course."* Drop "of course." Same line: *"The easy way to find out what she'd enjoy is to keep noticing her"* is a windup for the instruction that follows it.
5. **L27, "Presence" as a noun** (*"Presence is more than a good conversation"*) is the closest thing in the chapter to counseling-brochure register. *"It isn't only about talking."*
6. **L49 echoes Ch12's opening question.** *"Can you name the last romantic thing you did for your wife? If you have to work back through months to find it, start there."* Ch12 opens on his wife asking when he last took her on a date and him counting back *"Close to five months."* The author asked for this question in Ch13, so keep it, but the count-back-in-months unit is Ch12's; consider making the distinction explicit (a date is one thing, a romantic gesture is a wider category) or changing the unit.

## Claims against the research check (item 4 of the brief): clean

- **Rosenfeld** and the **GSS infidelity analysis** appear nowhere in the prose. Correct, per the feedback's instruction to leave both out.
- **2009 boredom study, L63:** *"In one long-term study, couples who described their marriage as boring were less satisfied nine years later, even after the researchers accounted for how satisfied they were at the start."* The baseline-control clause is not in `author-feedback-2026-09-24.md`, but it is documented in `research-addendum-2026-09-24.md` line 14 from a direct reading of Tsapelas, Aron & Orbuch (2009) — year-seven boredom predicting year-sixteen satisfaction, baseline controlled, 123 still-married couples. Supported, and the following sentence correctly refuses the causal reading. One low note: the study is the only source in the chapter not named in-prose while Perel and Seneca are; the citation apparatus should carry it.
- **Perel, L59:** *"writes about how familiarity can settle into routine, and how curiosity and new experiences can help keep desire alive"* — her own argument, hedged with "can," not dressed as a measured result. Supported.
- **Love-languages review, L33:** the not-a-fixed-language denial is exactly what Impett, Park & Muise supports. Supported (the problem with this sentence is duplication, E1, not accuracy).
- **Mental load, L37–41:** the distinction is made in plain language with no research asserted, and L41 (*"She may prefer to handle something you thought would help with. Let her tell you."*) respects the addendum's warning against universalizing one woman's preference. Clean.
- **Gifts, L43–45:** *"You were giving her the pleasure of being remembered"* is stated as an outcome rather than an intention, which is a shade past the addendum's "avoid promising that every recipient reads thought or expense as love." Very low; *"You were trying to let her know she was on your mind"* removes it.

## Things I checked and found sound

No wife-as-threat framing. No universal claim about all men in the narrator's voice. No corporate or therapy-speak beyond item 5 above. No scene from the outside; the reader is the man in every scene. No performative vulnerability (no first-person material at all, which is also why no new biographical contradiction is created). No absolutist dialogue. The removal ordered by the author is complete: no noticing-other-women passage, no comparison transition. Terminology is otherwise consistent with Ch12 (acts of service, touch, words, gifts; "worked to win her" sits comfortably with Ch12's "trying to win favor"), and no factual or mechanical contradiction with Ch12 exists. The phone frame (L3 → L25 → L69) is a genuine structural anchor and the close, *"Put the phone down, and give her the evening you came to share,"* is the author's own image and one sentence.

## Coverage

I read in full: `runs/ch13/refined.md` (chapter prose and Editor's Notes), `books/the-stoic-husband/chapters/ch12/refined.md`, `books/the-stoic-husband/01-voice.md`, `runs/ch13/author-feedback-2026-09-24.md`, `runs/ch13/revision-notes-2026-09-24.md`, `runs/ch13/research-addendum-2026-09-24.md`, `runs/ch13/persona-coherence-ch01-ch13.md`, and `runs/ch13/slop-coherence-ch01-ch13.md`. In `books/the-stoic-husband/03-outline.md` I read lines 255–305: the Ch12 entry's tail and its transition to Ch13, the full Ch13 entry, the full Ch14 entry and its transition, and the head of Ch15; I did not read the rest of the outline.

I did not read: `runs/ch13/draft.md`, `refined-before-feedback.md`, the stale `coherence-refined.md`, the distillation, practice-guide section, plate, or review PDF; any chapter other than Ch12 (so all cross-chapter claims about Ch01–Ch11, the Prologue and the Introduction in this report are carried from the two prior whole-book reports, not independently re-verified); `02-audience.md`, `00-premise.md`, `05-framework.md`, `06-sources.md`; any OKF concept or citation file; and the text of inbox items #094–#102 — my E4 and E5 touch landed Ch12 prose, and although I recommend fixing both inside unlanded Ch13 instead, I cannot certify they do not overlap a deferred older-book item.

I ran no counts. `voice_check.py` owns every counted rule, and I neither re-ran it nor verified the block quoted in the Editor's Notes; E2 is a qualitative read of a sentence-shape that script's own output says regex cannot see, not a dispute with a number it reported. I did not verify any source externally, did not confirm the wording of any translation, and this report certifies no citation status, no plate, no PDF, and no counted-rule compliance.
