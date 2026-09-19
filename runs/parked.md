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
