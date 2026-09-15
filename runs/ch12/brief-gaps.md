# Chapter 12 — Brief Gap List
**Gate:** the Ghostwriter desk, plan-only mode, clean-room
**Run:** 2026-09-15 17:2x
**Verdict:** NOT YET DELEGABLE — 10 gaps
**Clean-room integrity:** the gate confirmed it did not read `interview.md`. Test valid.

The question asked: *could someone who never read the interview write this chapter
from `research.md` alone?* Ten gaps. Two need the author. Eight go back to the
Researcher for one amendment round (Rule 6: one round, then the inbox).

---

## Author-only — inbox items raised

### G-A1 — the chapter has no scene, and no permission to build one
The brief rules out the anniversary dinner, the Walgreens scene, any substitute
cheap-gift scene, and third-person vignettes. What is left is the grandfather
(secondhand advice, not a scene) and one admission sentence. But `01-voice.md`
calls the voice "story-first" and `04-archetype.md` makes the reader-as-subject
scene the primary evidence vehicle. The brief never says whether the Ghostwriter
may construct a second-person composite moment. A cold writer must guess between
"invent nothing" and "invent a recognition moment" — and either way the chapter
comes out nearly all assertion.
**→ inbox #008**

### G-A2 — the platinum paragraph has no concrete instance
The brief calls it the chapter's most useful single paragraph and supplies only
the abstraction. `01-voice.md` is explicit: "Use specific, named detail. Not 'she
was upset.' What she said, what he did." An abstract platinum paragraph is a
voice failure by the spec's own words.
**→ inbox #009**

---

## Back to the Researcher — one amendment round

**G-3 — the infidelity section hedges inside a section titled "the ruling."**
It offers (a) and (b) with (a) "Recommended" while simultaneously sending the
question to the author. A cold writer can proceed on (a), but "recommended"
under a heading that says "ruling" is how two different drafts get written.
Make it an instruction with the alternative as a named one-clause insert.

**G-4 — three outline rows are neither satisfied nor superseded.**
The §0 supersession table covers mechanism, central story, key point 1, research
burden and the ah-ha. It is silent on **key point 3** (romance after ten years —
specific attention, not grand gestures), on the master table's **audience
objection** column ("I've applied Stoicism already — why marriage-specific?"),
and on whether the **"Transition to Chapter 13"** row is printed or editorial.
This matters beyond the draft: `gw-specchecker` grades against the outline row by
row, so a row the brief never mentions becomes a conformance FAIL that nobody
intended.

**G-5 — the declared metaphor family contains a word that breaks the script.**
**Verified mechanically by the Publisher, not taken on report.** `voice_check.py`
matches family terms by prefix (`x == t or x.startswith(t)`), and the metaphor
family is a HARD check. Declaring `use` therefore counts `used`, `useful`,
`using`, `uses`. Demonstrated on a 26-word probe: family `muscle,atrophy` → 1
hit; family `muscle,use,atrophy` → 6 hits, 5 of them from non-metaphorical
`use`. The author's own mandated line ("the more you use it, the more you get
good at it") spends one on its own. **Drop `use` from the declared family.** Do
not instead write "non-metaphorical use is not counted" — the script cannot
honour that, and a rule the script cannot honour is not a rule.

**G-6 — the boundary of the banned accounting register is undrawn.**
R-2 bans budget/ledger/spend/line-item. §10's own beat label is "The first thing
cut." and the brief's prose uses "energy budget," "first line item cut,"
"over-committed." A cold writer can reasonably read the brief's vocabulary as
licensed. State the banned family as a literal list, and say plainly that "cut"
is ordinary English and does not count.
*(The ban itself is workable and "muscle" is a usable replacement — the gate
confirmed that. Only the boundary is missing.)*

**G-7 — the Marcus instruction is clear in G-2 and loose at the point of use.**
Two fixes. (a) G-2 phrases it as a fork — "either someone reads Long against a
page, or the fallback" — and a cold desk cannot execute the first branch, so make
it an instruction. (b) §10's beat 2 says only "Marcus and the necessary things"
with no no-quote reminder there, while `01-voice.md` says "the climax belongs to
Marcus Aurelius" and `04-archetype.md` says Stoic texts are "quoted directly in
prose." State once, at the point of use, that **this chapter prints no quotation
at all** and the turn is carried by paraphrase — otherwise the writer is caught
between the brief and the constitution and will resolve it by quoting.

**G-8 — no cut priority against the word target.**
1,000–1,300 is achievable (Ch2 runs 1,361 and Ch7 1,411 prose-only, so short
chapters exist in this book) but the mandatory inventory is long and leaves no
room for the concrete texture G-A1 and G-A2 are asking for. The brief says "cut
early" but never ranks what goes first. It also does not mention that
`01-voice.md` carries an explicit "err longer" bias, or that refine applies a 15%
tolerance. Say which governs, and rank the cut order.

**G-9 — deliverable shape is unstated.**
Whether the output carries a `# Chapter 12: Romance Is a Discipline` heading
(house format per `chapters/ch07/refined.md`), and the apparent collision between
"at most one bolded sentence" in the counted rules and the archetype's required
3–5 **bold beat labels**. A one-to-four-word label is not a sentence, but the
brief puts both on the page without reconciling them.

**G-10 — Ch12 opens Part III and the brief does not say so.**
It is the first chapter after `parts/part-3-warm-sun.md`; the Sun has just been
introduced to the reader on the facing page; the preceding chapter sits in a
different Part. Recoverable from the outline, but not carried by the brief.

---

## Correction to the brief — the Publisher verified this one

§10 forbids the bounded-paragraph opening on the grounds that the format plus an
explicit callback in the same chapter is "flagged in the archetype as a
compounding echo." **That reason is wrong.** `04-archetype.md` line 64 flags the
combination across **two consecutive chapters** — the Ch7→Ch8 case — not within
one chapter. Verified against the file.

The *instruction* still stands and blocks nothing: Ch10 and Ch11 both opened in
plain prose, so bounded is technically available, but the brief's choice of the
callback type is independently correct. **The stated reason must not be reused as
precedent**, and the amendment should fix the rationale rather than the choice.

---

## What the gate probed and found clean

- **The grandfather anchor is closable from the brief alone.** §7's renderings of
  Ch1 and Ch7 were checked against the real chapters and are accurate. A cold
  writer does not need to go read them.
- **Love languages is operational.** §5 says write the idea, never name the
  framework, never attribute responsiveness. Nothing tempts a cold writer toward
  a name he does not have.
- **§0 wins cleanly on every point it actually covers.** The only guessing is on
  the rows it omits (G-4).
