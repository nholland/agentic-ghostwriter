# Parked Questions

Questions the author chose to defer. Nothing is blocked on these — a blocked
question is an inbox item, not a parked one. Each carries a revisit **trigger**,
not a date.

---

## P-001 — Does the "internet zeitgeist" material belong in this book at all?

**Parked:** 2026-09-15 16:41
**Raised at:** the Chapter 12 interview, round 2
**Revisit trigger:** the Chapter 13 interview (*Pursue Her After You Have Her* —
the nearest adjacent chapter and the most likely home). If Ch13 does not take it,
it escalates to the first whole-book QA pass, because "does it belong in the
book" is a book-level question that no single chapter can answer.

**His words:**

> "Should we add it to a parking lot item? I'm wondering if it has any place in
> the book because it effectively touches on what happens when you don't put in
> the effort and you get caught up in the concept of the internet zeitgeist: the
> blaming, the scapegoating, the social media. Even married men can fall prey to
> that."

**The material itself, from round 1, verbatim:**

> "I think a lot about the effort that I have noticed in men when they are
> outside of a relationship. All they think about is trying to land a date so
> they work out in the gym, they effectively buy cologne, they try to dress well,
> and they're trying to make themselves presentable. The men who don't do this
> effectively, I think, feed into the incel and red pill part of the internet.
> Effectively it's easier to blame and hate than to compete."

> "In a world where you used to have lots of opportunities to meet girls at
> dances and bars and church, the internet has provided a darker opportunity for
> people to just lash out and blame than to actually get out and entertain."

**What has to be true for it to earn a place:** his own framing supplies the test
— "even married men can fall prey to that." The material is in scope for a book
written for married men only if it is about a married man's grievance. As stated
it is about single men, which is a different book. Whoever picks this up should
answer that first, before finding it a chapter.

**Status in Ch12:** out. The Researcher did not build on it; the Ghostwriter does
not use it.

**Note on where this lives:** the book repo has its own `parking-lot.md`. This
engine never writes in the book repo, so parked questions raised here live here.
If the migration in inbox #007 goes ahead, the two merge.

---

## P-002 — Reach parity or beyond with the old pipeline before treating the migration as done in spirit, not just in file location

**Parked:** 2026-09-19 00:30
**Raised at:** this session, discussing the Playground → agentic-ghostwriter
migration's rationale and future evolution with the author.

**His words:**

> "Let's add the new items we should do, as well as Gaps, to the parking lot.
> We need parity or beyond on the new system."

**What this tracks, and what it deliberately does not duplicate:** `GAPS.md` is
already the live, trigger-based list of what the old pipeline could do that this
house cannot yet — the PDF renderer (environmental, waits on a container with
weasyprint), the seven-item publication stack (one shared trigger: the author
approves the whole-book QA pass and says the book is close), and three smaller
gaps each with their own trigger. As of this session it audited 27 of 40 old
commands covered, 13 not, 3 of those 13 closed this pass (`edit`, `note`, `park`).
Copying that list into this file would be the `citation-manifest.md` failure
again — two files claiming to be the same record, with nothing keeping them
equal. This item is the standing bar the gap list is measured against, not a
second copy of it.

**Revisit trigger:** every whole-book QA pass (`/gw-qa`), and whenever a gap's
own trigger fires in `GAPS.md` — check the closed gap against *this* bar
("parity or beyond"), not only against its own trigger, since closing a gap and
actually reaching parity are not automatically the same thing. Also revisit at
the next full command audit (the last one is dated 2026-09-13, predates the
migration) — the 40-command baseline was counted against the old pipeline before
it was frozen, and re-auditing after the freeze may turn up commands whose
correct answer changed once there was one repo instead of two.

---

**Correction, 2026-09-19, to P-001's closing note.** That note predicted "if the
migration in inbox #007 goes ahead, the two [parking-lot.md and this file]
merge." The migration went ahead; the files did not merge. `books/the-stoic-husband/parking-lot.md`
is the old pipeline's record and was migrated as history — read, never
extended (`CLAUDE.md`, Layers section). This file, `runs/parked.md`, stays the
one live parking lot. Recorded here rather than silently editing the original
note, since a prediction that didn't happen the way it predicted is itself
worth knowing.

---

## P-003 — Triage the old pipeline's ~17 still-OPEN parking-lot items against the new house

**Parked:** 2026-09-19 00:46
**Raised at:** the author asking "what else did you miss" after the Substack
finding, which led to actually reading `books/the-stoic-husband/parking-lot.md`
in full rather than trusting `CLAUDE.md`'s "read for history" framing to mean
"nothing in it is still live."

**What was found:** `parking-lot.md` has roughly 17 items still marked `OPEN`
(numbers #5, #8, #9, #12, #20–#24, #26, #27, #29–#35), spanning 2026-06-12 through
2026-09-10 — content decisions, not just tooling. Two examples surfaced already:
`#8` (Buffer social auto-posting, now in `GAPS.md`) and the general shape that
`#7` in `.claude/LEARNINGS.md` warned about (a manifest field asserting a state
nobody re-checked). "Migrated as history, read never extended" is correct for
*resolved* items; it silently mis-describes an *open* one, since an open item is
undecided business, not a record of something that already happened.

**Why not done in this pass:** 17 items, each needing a judgment call about
current relevance (has this house since decided it? is it superseded by
something in `FINDINGS.md` or `progress.md`'s later entries? is it still live?)
is a real read-through, not a grep. Guessing at 17 answers to look responsive
would be worse than flagging it plainly.

**Revisit trigger:** the next session with room for a dedicated pass, or before
the whole-book QA trigger fires (P-002) — QA is a bad time to discover a decision
was never actually made. Each item that's still genuinely open moves to this file
with a real trigger; each one superseded gets a one-line note saying by what.

---

## P-004 — The contrast-chapter commission for Ch23 (*The Difference Between Endurance and Cowardice*)

**Parked:** 2026-09-19 07:00
**Raised at:** the `/gw` session routing the fabricated Ch11 feedback (see
`runs/notes.md` N-001). Author's word: *"Approved."*
**Revisit trigger:** the **Chapter 23 interview**. If Ch23's interview does not
take it, it dies there rather than escalating — this is material looking for a
home, not a question blocking anything.

**Provenance, stated plainly:** these ideas reached the author inside a
fabricated editor's log produced by ChatGPT against a chapter it invented. He
read them and they landed. That makes them **his** material from this point, not
a reader's and not the tool's. Nothing here is attributed to a reader, and none
of the originating prose is reusable — it failed the counted voice spec (N-001).
What follows is the idea, restated, for an interview to work from.

**The commission:** Ch23 already argues *"staying from fear is not a virtue."*
That is the negative pole. The material supplies the positive one — **staying
when staying actually costs something** — and an architecture for putting the
two in contact.

1. **Endurance against its counterfeit, repeatedly.** Not "here is what
   endurance is," but "here is what it is not, four times." Withdrawal that
   calls itself discipline. Going quiet because conflict is unpleasant, and
   naming it strength. Disappearing inward while remaining in the room.

2. **The vow as the strongest available illustration.** *"For richer or poorer,
   in sickness and in health"* describes endurance at its deepest: the spouse
   who changes beyond recognition, the able-bodied partner who becomes seriously
   ill or disabled, the life neither person planned for. The force of it is that
   it says *I am still here when staying costs something.* Note for the
   interview: the phrase appears **0 times** anywhere in the book today.

3. **Better everyday examples than the ones in circulation.** Continuing to
   carry your share of the house when exhausted. Staying patient while she is
   struggling. Reading her state without converting it into a statement about
   you. (The originating text offered "sitting on the couch even when you're
   tired," which the author rejected as demonstrating nothing. Recorded so the
   interview does not rediscover it.)

**Already covered — do not re-commission:** the endurance/withdrawal distinction
itself is *not* new to the book. `05-framework.md` names it as **Oak × Courage —
Active Steadiness**, failure mode **The Ghost**: *"Physically present,
emotionally checked out — technically 'enduring,' actually disappearing. He's in
the room, but he's not there."* Ch23 is already mapped to that cell. And Ch11
executes the distinction better than the originating text did, with four
outcomes rather than two and the counterfeits named: *"Numbness is quiet.
Holding it in is quiet. Steadiness is also quiet."* **Ch23's job is the callback,
not the introduction.**

**Research-required before use — flagged, not cleared.** The parent-child
analogy: that children behave worst with the caregiver they feel safest with,
and that a good parent does not put love up for renegotiation over a meltdown.
The author's own note on it was *"Verify the science before making that claim."*
There is a real attachment literature in the vicinity; whether it supports this
specific claim is unestablished. This is Fact-Checker work at the Ch23 research
stage, and the claim does not enter prose before the ledger does (Rule 2).

**Loose, unassigned:** grace and discernment — that not every slight needs
acknowledging, and that *letting it go means actually letting it go, not storing
it as ammunition for a later argument.* This may not be Ch23's. It sits between
Ch7 (*The End of Scorekeeping*) and Ch17 (*Repair Quickly, Love Deliberately*),
and a candidate home in `05-framework.md` was identified this session — see the
open proposal on **Oak × Justice / The Scoreboard**. Whoever takes Ch23 should
check that proposal's outcome before claiming this.
