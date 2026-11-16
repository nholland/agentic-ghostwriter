# Proposed signal concepts: Marcus (reader), 2026-11-16

**Status: PROPOSED. Nothing here is in `okf/signals/`.** The author confirms (or
re-categorises, or drops) each concept before the Publisher writes it.

- **Drafted by:** gw-publicist (/gw-signal Step 1), 2026-11-16
- **Source:** Marcus (reader), friend of the author. **Not Marcus Aurelius.** Every
  "Marcus" in this file is the reader. Filenames use `marcus-reader-` so a later
  search for Marcus Aurelius cannot land here.
- **Inputs:** `runs/signals/2026-11-16-marcus-chat1.md` (Prologue only, per the
  author) and `runs/signals/2026-11-16-marcus-chat2.md` (whole book through
  Chapter 8 plus the Introduction; Marcus *listened* for about an hour while
  running and could not say how far he got).
- **Version read:** the compile committed 2026-11-10 (`output/compiled/book.pdf`).
- **Attribution:** speaker labels are machine-assigned and unreliable. Every quote
  below was attributed by content. Lines labelled "You" were used only where noted.
  Quotes are verbatim from the transcripts, including their transcription errors
  and asterisks; `...` marks an omitted span, `/` joins consecutive transcript lines.
- **Privacy:** nothing about Marcus's own marriage, and nothing about whether the
  author's wife has read the book, appears in this file. Quotes were cut short
  where the next words turned to either.

## Two format questions for the Publisher

1. **Category vocabulary.** The routing categories requested (prose-problem,
   argued-objection, reaction, gift, factual-challenge, extension) are the
   `/gw-signal` Step 2 table. The OKF schema's `signal_category` enum
   (`.claude/OKF.md`) is different: `resonance | confusion | objection | gift |
   extension | noise`. Each concept below carries both: `signal_category` in the
   schema's vocabulary, and a custom `routing_category` field (the schema allows
   producer-added fields). Mapping used: reaction -> resonance, argued-objection ->
   objection, prose-problem -> objection (precedent:
   `2026-06-19-metaphor-saturation-objection.md` filed a prose complaint as
   objection). If the house wants one vocabulary, that is an inbox item, not mine.
2. **Introduction slug.** Existing concepts use both `introduction` and
   `the-man-without-a-blueprint`. I used `introduction`, the more common one. No
   existing concept carries `prologue`; I used it.

## Summary

| # | Proposed file | routing_category | Scope |
|---|---|---|---|
| 1 | 2026-11-16-marcus-reader-not-ai-sounding.md | reaction | Prologue |
| 2 | 2026-11-16-marcus-reader-humble-disclosure-landed.md | reaction | Prologue |
| 3 | 2026-11-16-marcus-reader-prologue-second-half-meanders.md | prose-problem | Prologue |
| 4 | 2026-11-16-marcus-reader-abrupt-stoic-turn.md | argued-objection | Prologue |
| 5 | 2026-11-16-marcus-reader-no-promise-no-limits.md | argued-objection | Prologue |
| 6 | 2026-11-16-marcus-reader-no-stories-risked-nothing.md | argued-objection | Whole book through Ch8 |
| 7 | 2026-11-16-marcus-reader-introduction-formula-no-stakes.md | argued-objection | Introduction |
| 8 | 2026-11-16-marcus-reader-divorce-never-named.md | argued-objection | Whole book through Ch8 |
| 9 | 2026-11-16-marcus-reader-too-safe-no-debate.md | argued-objection | Whole book through Ch8 |
| 10 | 2026-11-16-marcus-reader-community-reputation-stakes.md | extension | Whole book through Ch8 |
| 11 | 2026-11-16-marcus-reader-empathy-theme-landed.md | reaction | Whole book through Ch8 |

11 concepts: 6 argued-objection, 3 reaction, 1 prose-problem, 1 extension,
0 gift, 0 factual-challenge.

---

## 1. Not AI-sounding; reads as autobiographical

```yaml
---
type: Reader Signal
title: Prologue did not read as AI; it read as autobiographical
description: Reader who knew the author uses AI said the Prologue would not have struck him as AI-written, because it is autobiographical, and that it did not sound sloppy.
platform: spoken conversation (transcript pasted by author)
signal_category: resonance
routing_category: reaction
provenance: Reader response (Marcus (reader), friend of the author; not Marcus Aurelius), conversation 1, 2026-11-16; version read, compile committed 2026-11-10
ip: audience-signal
tags: [voice, ai-detection, autobiography]
chapter_slugs: [prologue]
timestamp: 2026-11-16T13:21:00Z
---
```

**Reader said:** "I was surprised knowing how much you've been using AI at. / ...
You know much, I wouldn't have thought it was AI because it's very
autobiographical." And: "No, no, it didn't that? No, I mean, it didn't. It really
didn't sound sloppish at all, actually."

**Category:** reaction. No argument offered; recorded, not routed. Note the reader
knew in advance the author used AI, so this is a primed reader, not a blind one.

---

## 2. Humble, with expertise; the income disclosure landed

```yaml
---
type: Reader Signal
title: Prologue balanced humility and expertise; the income disclosure read as good vulnerability
description: Reader named the Prologue's disclosure about living on his wife's salary while building the business as good vulnerability and good modeling.
platform: spoken conversation (transcript pasted by author)
signal_category: resonance
routing_category: reaction
provenance: Reader response (Marcus (reader), friend of the author; not Marcus Aurelius), conversation 1, 2026-11-16; version read, compile committed 2026-11-10
ip: audience-signal
tags: [vulnerability, disclosure, authority]
chapter_slugs: [prologue]
timestamp: 2026-11-16T13:21:00Z
---
```

**Reader said:** "You were sufficiently humble. / ... You know, but also. / You know,
demonstrated your expertise. I thought the part where you talked about. / Living
off of Brandy salary while you build the business. / You know, that was, that was
a good disclosure. / Good vulnerability there. / ... Um, good modeling, right?"

**Category:** reaction. Worth reading next to #6: the one disclosure he praised is
exactly the kind of risk he later says the book does not take enough of. The
passage is in the published Prologue (`chapters/prologue/refined.md`, para 17
region), so naming it here discloses nothing the book does not.

---

## 3. Prologue's second half meanders; the metaphors feel like filler

```yaml
---
type: Reader Signal
title: Prologue first half strong; second half meanders into metaphor that reads as filler
description: Reader said the Prologue moves from story to a run of analogies and metaphors toward the end, which felt like filler, and that the second half could be cut.
platform: spoken conversation (transcript pasted by author)
signal_category: objection
routing_category: prose-problem
provenance: Reader response (Marcus (reader), friend of the author; not Marcus Aurelius), conversation 1, 2026-11-16; version read, compile committed 2026-11-10
ip: audience-signal
tags: [pacing, metaphor, filler, cuts]
chapter_slugs: [prologue]
timestamp: 2026-11-16T13:21:00Z
---
```

**Reader said:** "In the beginning. / You were telling your story and then, by the
end, you started using like a bunch of. / Analogies and metaphors. / ... And it
just felt like filler. / ... You know, um, where you could have been? / More to the
point." And: "Say, the first half of it was was really strong. Second half
meandered a little bit, and you could probably find some some Cuts there. Yeah,
yeah, the first half was great. First half was great."

**Category:** prose-problem, routes to the Line Editor (fix proposed, not applied).
Precedent: `2026-06-19-metaphor-saturation-objection.md`, the same complaint from
a different reader on a different piece.

**Excluded on attribution:** "Meaning, meaning... The gist of the book is about
helping men reading it. You don't need to go so deep on your own damn story." is
labelled "You" and may be Marcus restated or may be the author. It also points the
opposite way from Marcus's later, unambiguous ask for *more* personal story (#6).
Not used in any concept until the author says whose it is.

---

## 4. The turn to Stoicism was abrupt, and he stopped listening

```yaml
---
type: Reader Signal
title: Prologue's turn to Stoicism arrived unannounced and cost the reader's attention
description: Reader did not expect the book to be about Stoicism; when the Prologue turned to it, his own associations took over and he partly stopped listening. He contrasts his own book, where frameworks were a part of a chapter, not the purpose.
platform: spoken conversation (transcript pasted by author)
signal_category: objection
routing_category: argued-objection
provenance: Reader response (Marcus (reader), friend of the author; not Marcus Aurelius), conversation 1, 2026-11-16; version read, compile committed 2026-11-10
ip: audience-signal
tags: [stoicism-framing, reader-expectation, positioning]
chapter_slugs: [prologue]
timestamp: 2026-11-16T13:21:00Z
---
```

**Reader said:** "I think, at the point where you went to stoicism. / Uh, well, let
me ask you is the book about stoicism." Then: "I just noticed for me that when you
did that, it like, I felt like it was a. / Uh, all the stuff in my head. / ... From
stoicism, you know, and, and I almost like, stop listening to you as much. / ...
Uh, because I was, like, oh, this guy is about to tell me how he implemented
stoicism in his?" And: "it did catch me off guard to hear you kind of. / Go there
in the book". On his own book: "they should maybe were not the whole purpose, you
know, I mean, they were like? / A chapter, and they were a part of a chapter here
and there." And: "I just didn't expect it, and so."

**Category:** argued-objection, routes to the Reader Panel (Skeptic). The argument:
an unsignalled frame triggers the reader's prior baggage about that frame, and
attention drops. He is not against Stoicism ("I think it's good"); his complaint
is surprise. Note he read the compiled PDF, whose cover carries the subtitle; the
Panel should check whether the signal fires before the Prologue does.

**Not Marcus's:** the line "didn't make the stoic angle clear, and so it felt like
an abrupt turn towards the second half and also felt a bit loaded on that, uh
terminology and Concepts" is the author reading out his own note summarising
Marcus. It agrees with Marcus but is the author's wording; do not quote it as the
reader's.

---

## 5. The Prologue never says what the book promises, or what it cannot

```yaml
---
type: Reader Signal
title: Prologue gets close to its point but never lands what the book offers, or its limits
description: Reader wanted the Prologue to commit at its end to what the book is (what practicing Stoicism in marriage did for the author) and to be explicit about limits, above all that a husband does not control his wife and the book cannot promise she will respond.
platform: spoken conversation (transcript pasted by author)
signal_category: objection
routing_category: argued-objection
provenance: Reader response (Marcus (reader), friend of the author; not Marcus Aurelius), conversation 1, 2026-11-16; version read, compile committed 2026-11-10
ip: audience-signal
tags: [reader-promise, limits, control, dichotomy-of-control]
chapter_slugs: [prologue]
timestamp: 2026-11-16T13:21:00Z
---
```

**Reader said:** "If you would have committed more? / At the end of the prologue to
the fact that this book? / You sharing what you learned in your practice of storage
principles in your marriage." Then: "what's what? Is the f****** point here, right,
and and I? And I, and I feel like, you got close, but you didn't quite. You didn't
quite stick to Landing after, after all the stuff". On limits: "you can only
control what happens on your side and you're not promising them. You know, you
can't promise them that their marriage is even going to work. You can't promise
them. They married the right person". On the missing payoff: "Stoicism. What did
practicing stoicism? / In your marriage do for you? / In your estimation in terms
of. / Making you a better husband and a better person." And: "This book is for men
trying to be better husbands. It cannot promise that the woman is gonna respond to
that Improvement. / Right. And, and so I feel like you didn't quite say that." And:
"Be clear about what it promises and what its limits are right. I mean, stoicism is
it's about acceptance, but it's also about controlling the controllables. And you
know, I think you need to be really explicit. You don't control your wife."

**Category:** argued-objection, routes to the Reader Panel (Skeptic). Two linked
asks: a stated benefit (what it did for the author) and a stated limit (it cannot
change her). The author's answer in the room ("more reflection", "more tools",
"more control over how I was going to show up") is author material, not signal;
see the section at the foot.

---

## 6. No stories, nothing risked; the shadow side is know-it-all

```yaml
---
type: Reader Signal
title: The book is heavy on instruction, light on story, and the author risks nothing, which reads as know-it-all
description: Reader's "biggest critique" of the book through Chapter 8. Without stories or stakes, and with the author exposing his father and grandfather more than himself, the instruction reads as preachy; a reader who did not know the author would have nothing to discount it against.
platform: spoken conversation (transcript pasted by author)
signal_category: objection
routing_category: argued-objection
provenance: Reader response (Marcus (reader), friend of the author; not Marcus Aurelius), conversation 2, 2026-11-16; version read, compile committed 2026-11-10; listened, roughly one hour, extent unknown
ip: audience-signal
tags: [story-ratio, authority, vulnerability, stakes, preachiness]
chapter_slugs: [prologue, introduction, the-three-second-window, stop-outsourcing-your-peace, stop-defending-yourself, anger-is-failed-leadership, how-to-fight-without-becoming-small, duty-without-resentment, the-end-of-scorekeeping, when-your-marriage-feels-unfair]
timestamp: 2026-11-16T13:26:00Z
---
```

**Reader said:** "You're heavy, you're heavy on the instruction. / You haven't
really established the stakes. / ... This is like the biggest critique. / ... You
really have no stories, and you personally have risked nothing."

On the two routes: "If you want to have a voice of research, then you can collect
other people's stories ... that's what Ryan holiday does right when he's when he's
teaching stoicism. He's teaching it as a history student." And: "You can do it from
first person Authority, but you have to be willing to risk that right." And: "if
you don't want to risk it? / ... You might want to go to research route, and you
might want to capture people's stories." And a third: "you could say I'm not
willing to do the research for the parable thing, and and I'm not willing to tell
the story, and this will just have to be a limitation of it."

On why stories carry it: "it's credibility. / Um, it's credibility. It's
relatability, right? Because, like, I'm I'm not? / Putting myself on a perfect
pedestal?" And: "people sort of intuitively know a lot of what's learned in life
comes through failure, not success." And: "I think people will learn more through
stories than they will through. / ... You, you, you asserting, yeah, you asserting
Axiom after accident after accident after action after action." (transcription of
"axiom after axiom")

On the personality: "Your shadow side fan is like, you're a little bit of a
know-it-all." And: "you, you, you risk nothing, but you're telling everybody, what
the f*** they're supposed to do?" And, on listening: "it's a whole lot of you
talking at me ... and it takes the right kind of person to sort of. / ... Manage
themselves and actually benefit from that."

On the ancestors: "you actually were willing to out your dad and Grandad more than
you were willing to out yourself?" And: "You know, you throw your ancestors under
the f****** bus, but you won't take a shot at all at all."

On his own filter: "Because I know you like, I could get past all that. Like, I
know what you've actually been through. So, I just like I, I ran it through that
filter".

On craft: "I might go check. / Brian holiday and Fox. / ... and just sort of see
how he. / Manages to do it because I feel like his chapters are not that long. /
... It still manages to kind of get a little Parable in there." (Ryan Holiday;
title garbled in transcript, not identified here.)

**Category:** argued-objection, routes to the Reader Panel (Skeptic), and is
likely an inbox decision for the author (voice and story policy are his). The
last-but-one quote matters most: the reader says his own friendship supplied the
credibility the text does not, which means a stranger would not have it.
"70% stories, 30% instructions" is his description of his own book, not a
measurement of this one.

---

## 7. The Introduction reads as a formula, with no stakes

```yaml
---
type: Reader Signal
title: Introduction reads as a balancing equation of River, Oak and Sun and never says why the reader should care
description: Reader found the Introduction's River/Oak/Sun framing a formula ("science equation", "boot camp") that never addresses why a man would want to do this work, when the man picking up the book is probably already in trouble.
platform: spoken conversation (transcript pasted by author)
signal_category: objection
routing_category: argued-objection
provenance: Reader response (Marcus (reader), friend of the author; not Marcus Aurelius), conversation 2, 2026-11-16; version read, compile committed 2026-11-10
ip: audience-signal
tags: [stakes, framework-presentation, reader-state, motivation]
chapter_slugs: [introduction]
timestamp: 2026-11-16T13:26:00Z
---
```

**Reader said:** "your introduction is, just like. / ... The river and the Sun and
the oak and too much of this and this and too much of this and this. And it's just
like, you know, what I mean, like, like, okay, but like, why do I even care and,
and it's like, you know, you're putting me through a boot camp?" And: "I feel like
the introduction was way too like. / ... Science equation like, you know, here's
the perfect balance. We need to get a river so Sun Oak in order to, you know, in
order to achieve, you know, maximum husband and and and, and, and it didn't, kind
of like address. / Why the f***? / What, what, like, like, like, like, why the
f***, would you even want to work hard at this? Like, I know, you're married, but,
but if you're picking this up, you're probably at the point where you kind of
realize, oh s***, this is not quite what I thought it was going to be, right?"
Later, on the Oak specifically: "see the thing I couldn't really get is why it
matters?"

**Category:** argued-objection, routes to the Reader Panel (Skeptic). Bears on
`02-audience.md`'s reader-state assumption; the author agreed in the room ("does
anybody read this in a good state? / Probably not"), which is author material, not
signal.

---

## 8. Divorce is never named

```yaml
---
type: Reader Signal
title: A marriage book that never talks about divorce, or about consequences
description: Reader said he did not hear the word divorce at all, and that the book needs to be willing to talk about consequences.
platform: spoken conversation (transcript pasted by author)
signal_category: objection
routing_category: argued-objection
provenance: Reader response (Marcus (reader), friend of the author; not Marcus Aurelius), conversation 2, 2026-11-16; version read, compile committed 2026-11-10; listened, roughly one hour, extent unknown
ip: audience-signal
tags: [divorce, consequences, stakes]
chapter_slugs: [prologue, introduction, the-three-second-window, stop-outsourcing-your-peace, stop-defending-yourself, anger-is-failed-leadership, how-to-fight-without-becoming-small, duty-without-resentment, the-end-of-scorekeeping, when-your-marriage-feels-unfair]
timestamp: 2026-11-16T13:26:00Z
---
```

**Reader said:** "The consequences. / ... Consequences like, like, I mean, I think
you need to be more more willing to to talk about the consequence. Like, I feel
like I didn't hear the word divorce. / ... At all. You know what I mean, and and
I'm like, how can you talk have a book about marriage in an era where one of every
two marriages breaks up?" And: "you didn't even talk about it. You didn't even
f****** talk about it".

**Category:** argued-objection, routes to the Reader Panel (Skeptic).

**Checked, current refined text (not the 2026-11-10 PDF):** `divorc` appears once
across the Prologue, Introduction and Chapters 1-8, in Ch4 (`ch04/refined.md`
line 77, the Gottman contempt sentence). He listened for about an hour and may
not have reached it; either way the book does not take divorce up as a subject,
so the substance of his point stands.

**Do not adopt the statistic.** "one of every two marriages breaks up" is the
reader's figure, unsourced. It must not enter prose or marketing without the
Fact-Checker.

---

## 9. Too safe: it asserts, it does not debate

```yaml
---
type: Reader Signal
title: The book enters the arena of ideas about men without engaging the rival ideas, and says little anyone would disagree with
description: Reader said the book asserts its way without debating the other voices telling men what matters, that it is "overly safe", and that it should say things people will disagree with, ideally on record before they become obvious.
platform: spoken conversation (transcript pasted by author)
signal_category: objection
routing_category: argued-objection
provenance: Reader response (Marcus (reader), friend of the author; not Marcus Aurelius), conversation 2, 2026-11-16; version read, compile committed 2026-11-10
ip: audience-signal
tags: [positioning, rival-ideas, risk, contrarian-claims]
chapter_slugs: [prologue, introduction, the-three-second-window, stop-outsourcing-your-peace, stop-defending-yourself, anger-is-failed-leadership, how-to-fight-without-becoming-small, duty-without-resentment, the-end-of-scorekeeping, when-your-marriage-feels-unfair]
timestamp: 2026-11-16T13:26:00Z
---
```

**Reader said:** "You're gonna write a book and you're and what you're really
doing is you're entering the arena of ideas with a whole lot of other
m************ who are out there, telling men why, what they are saying, matters
right, and you're just asserting this is the way you know, I mean, but but you,
but you haven't. You haven't actually like debated with the other ideas." And:
"It's just like this book of Axiom that's just overly safe and and, and is
missing, the s*** that is missing this. It's missing the ship is making. It makes
it compelling like you have to take risks." And: "you got to say these things
knowing. / ... People will absolutely disagree with them. It's like, it's like you,
it's like you said a lot of things that are unlikely to get people to disagree
with them. / ... And that's not really the goal, right?" And: "you want to be on
record before some things becomes obvious. / ... But that's, that's when you
really get get leverage." Earlier, on opinion: "you're the author, so you can be
very opinionated. There's no problem with that."

**Category:** argued-objection, routes to the Reader Panel (Skeptic); a decision
about the book's positioning is the author's (inbox). He cites his own book's
first chapter taking on "the assertion, that college is always good" as his
example; that is his book, not a claim for this one. The rival the author named in
the room (Andrew Tate) is the author's, not Marcus's; see the foot.

---

## 10. Community and reputation as stakes

```yaml
---
type: Reader Signal
title: Name what a husband's conduct costs or earns outside the marriage: community, reputation, opportunity
description: Reader suggested the book talk about community and reputation, how people speak of you when you are not in the room, and what that does to income, belonging and leadership opportunities.
platform: spoken conversation (transcript pasted by author)
signal_category: extension
routing_category: extension
provenance: Reader response (Marcus (reader), friend of the author; not Marcus Aurelius), conversation 2, 2026-11-16; version read, compile committed 2026-11-10
ip: audience-signal
tags: [community, reputation, consequences, scope]
chapter_slugs: [prologue, introduction, the-three-second-window, stop-outsourcing-your-peace, stop-defending-yourself, anger-is-failed-leadership, how-to-fight-without-becoming-small, duty-without-resentment, the-end-of-scorekeeping, when-your-marriage-feels-unfair]
timestamp: 2026-11-16T13:26:00Z
---
```

**Reader said:** "I think, like, you have to sort of talk about the importance of
community, the importance of your reputation, like the importance of? / ... Of,
uh, you know, the way people speak about you when you're not in the room, right?
... all these things actually have a lot to do with how much money you'll be able
to make, you know, um, you know whether or not you'll be able to to be to be part
of, uh, you know, societies and Gatherings and celebrations? And like, you know,
just with all these leadership, like, will you get leadership opportunities,
right?"

**Category:** extension, routes to the inbox (only the author decides scope). It
grows out of #8: he raised it as a further consequence. The interjected words
"reputation, trust, dependability" and "leadership" are the author's, not his.

---

## 11. The empathy theme landed

```yaml
---
type: Reader Signal
title: The repeated empathy theme landed: engaged, listening, not self-focused, not ruled by emotion
description: Despite his critique, the reader named one clear theme he took and used: stop thinking about yourself, show your wife you have empathy for her, stay engaged rather than shutting down, and do not be driven by emotion.
platform: spoken conversation (transcript pasted by author)
signal_category: resonance
routing_category: reaction
provenance: Reader response (Marcus (reader), friend of the author; not Marcus Aurelius), conversation 2, 2026-11-16; version read, compile committed 2026-11-10
ip: audience-signal
tags: [empathy, engagement, emotional-regulation, repetition]
chapter_slugs: [prologue, introduction, the-three-second-window, stop-outsourcing-your-peace, stop-defending-yourself, anger-is-failed-leadership, how-to-fight-without-becoming-small, duty-without-resentment, the-end-of-scorekeeping, when-your-marriage-feels-unfair]
timestamp: 2026-11-16T13:26:00Z
---
```

**Reader said:** "you reiterated it enough times where, like, I really was reminded
of it. / ... Was basically like? / ... Stop f****** thinking about yourself and
have some empathy for your wife and actually try to show up in a way where she
will see that you have empathy for her. Like, I mean, you said that in, like 30
different f****** ways". And: "that was a very clear theme, you know, and, and it
wasn't, it wasn't do it. It wasn't be safe, and it wasn't like, shut down, you
know. It was like, actually, engaged, actually engaged, but engaged in a way where
you are listening and you are respecting, and you're thinking about all the blind
spots that you both have." And: "I listened to it and and I found a lot of good in
it."

**Category:** reaction; recorded, not routed. Two-edged: "like 30 different
f****** ways" is praise for clarity and also a count of repetition. The Panel may
want it next to #6's "Axiom after accident".

---

## Author material surfaced (for the Developmental Editor)

Not signals. These are the author's own words in the two conversations, and they
are his material. Listed so the Developmental Editor can take them up in session;
none is proposed for `okf/signals/`.

1. **Say it once, kindly, then release it** (chat 1, the author's turns from "I'll
   tell you like one little story that I might work in there" to "It's dope. It's
   a great win-win."). Leaving things unsaid became baggage; the unlock was saying
   his piece kindly and under control, then releasing any need for validation or
   change; the first response was often defensive, and the change came later
   ("the time scale changes"). He says he talks about it later in the book; the
   Developmental Editor should check where, and whether it belongs in the Prologue
   as his answer to #5.
2. **What missing Oak, River or Sun costs** (chat 2, the author's turns from "if
   divorce is like the end game, the worst part scenario" through "And that's the
   warmth side."): without the Oak she sees weakness; without the River he is a
   hothead who is unsafe to everyone; without the Sun he becomes "a stone" no one
   likes. Divorce as the worst end game. Preceded by the screamer friend whose
   family walks on eggshells, which is the River failure in a person, and the
   point where Marcus said "You're scratching at it now". This is the author's
   direct answer to #7 and #8. The biology claims inside it ("women don't like weak
   men", hormonal and evolutionary framing) are the author's opinions and would
   need the Fact-Checker before any of them is stated as fact.

Also surfaced, for the Developmental Editor to weigh, all the author's:
- His own reader-notes on the Prologue, read out in chat 1: dislikes "the way the
  author bragged about being three steps ahead"; the story of coming to Stoicism
  is "too vague"; the religion passage leaves it unclear whether he is Mormon now
  or criticising Mormons. These are his, not Marcus's.
- What Stoicism did for him, said off the cuff: more reflection, more tools, more
  control over how he shows up (answer to #5).
- The reflection question "was I the best husband that I could be? / Despite how
  crazy ass somebody acted around you?" and its answer (used his brain, self-control,
  did not run, kind in what he had to say).
- The chapter-length cap (sub-2,000, aiming at 1,500) pushing stories out in favour
  of quotes and research, plus his rule against painting his wife badly; his own
  diagnosis of #6.
- Reader state: nobody picks this up in a good state; he came to philosophy
  because his life was falling apart.
- Positioning against the manosphere (named: Andrew Tate): agrees on strength and
  protection, disagrees on self-control. Bears on #9.
- Possible story sources: composite or interviewed men with names changed, which
  Marcus endorsed ("You can always change the names as long as they're a real
  Source"). Any such story is a disclosure and sourcing decision for the author.

## Not signals, and why

- Marcus's account of his own writing coach ("Keep writing") and his own book's
  structure: his framing for the critique, not a response to this book.
- Lines whose attribution is uncertain (see #3): held, not used.
- Anything touching Marcus's own marriage, or whether the author's wife has read
  the book: excluded by rule. Not quoted, not paraphrased, not summarised.
