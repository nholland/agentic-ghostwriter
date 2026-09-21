# Plate standalone read — all twelve, post-edit-round

**Date:** 2026-09-21
**Stage:** /gw-plate stage 5, cold standalone read
**Desk:** The Reader Panel
**Coverage:** Ch01–Ch12 chapter plates. Part plates not read.

## How these were read, and one thing the Publisher should know

Bash is disabled in this session, so I could not rasterise fresh. I did not judge
from SVG source. Instead I used the existing renders and then proved they were
current.

There are two PNG sets in the repo and **they disagree**. `runs/manuscript/chNN-plate.png`
is stale — the Ch01 copy still shows the old "chosen / inherited" construction that
is no longer in the SVG. `runs/chNN/pdf/plate.png` matches the current SVG text
string for string on all twelve. I read the `pdf/` set, and only after writing down
what I saw did I open the SVGs to confirm the match and then the briefs.

**Finding, free of charge:** `runs/manuscript/*-plate.png` is a stale point-in-time
artifact carrying no coverage in its name, and it is the set the compiled manuscript
draws from. Anyone reviewing the book right now is reviewing last round's plates.

---

## The table

| Ch | Plate title | Verdict | What I thought it meant, cold |
|---|---|---|---|
| 01 | The Three-Second Window | **FAIL** | There are three seconds between her words and your reply, and that is where your marriage is decided. |
| 02 | The Mood Mirror | **PASS** | Match her bad mood and the storm doubles; hold your own and it stays one storm. |
| 03 | The Closed Door | **PASS** | Every time you defend yourself, the room she has to bring you things shrinks, until it is gone. |
| 04 | The Hole Maker | **PASS** | Anger drives nails; an apology pulls the nail out but the hole stays, and they add up. |
| 05 | The Courage to Come Back | **PASS** | Walk out of a fight and never come back to say it and you shrink; go back and say it and you stay whole. |
| 06 | The Tally You Don't Read Aloud | **FAIL** | The week is long and tonight is a small slice of it. |
| 07 | The Private Tally | **PASS** | You keep a short list of your big contributions, you cannot read hers, and neither of you counts the mass of small stuff. |
| 08 | The Tipping Scale | **PASS** | Small things nobody counted pile up on one side until it tips; catch each one as it lands and it stays level. |
| 09 | The Bottomless Yes | **PASS** (marginal) | You gave, you expected something back, it never came, you never asked, and you are keeping a private list about it. |
| 10 | The Undecided Line | **PASS** | A rule you cannot explain caves the first time it is pushed; one you can name what it protects holds. |
| 11 | The Conversation She's Never Heard | **PASS** | You have run the argument over and over in your head and said none of it out loud. |
| 12 | The Thing With No Deadline | **PASS** | Everything with a deadline got done all week; the one thing for her stopped months ago and tonight is still empty. |

Ten pass, two fail. Both failures are fixable inside the "no rethinks" constraint.

---

## The three questions the Designers asked

**1. Ch6, one bar with a dashed frame — does it read?**
No. Cold, I got "the week is long, tonight is a sliver" — a statement about
proportion. The Conversation sentence is about *visibility*: "it comes from being
the only one who can see it." Nothing on the plate encodes seeing. The bar is
solid black all the way through, including inside the dashed frame, so there is no
visual difference between what you count and what she can see. The dashed box reads
as a crop mark or a highlight — the thing being selected — not as the limit of
someone's view.

The fix is available inside the constraint and needs no new object: **ghost the bar
outside the dashed frame** (light grey fill, or unfilled with a hairline) and leave
only the stretch inside the frame solid black. Then "THE WEEK" sits over the faint
part, "TONIGHT" over the solid part, and the argument is in the ink weight instead
of in the deck. Ch8 already does exactly this trick with its five faint pebbles and
one black one, and Ch8 is one of the two fastest plates in the book. Borrow it.

I will say plainly that the old two-bar version probably carried this better,
because two bars of different length compare two people, whereas one bar compares
two time spans. But re-splitting is a rethink, and the weighting fix gets most of it.

**2. Ch4, the loss of "Hot or cold, both drive a nail" — does it cost?**
Yes, and it is the most expensive single word-level change in the round. The plate
now says "outburst" three times over: the title is THE HOLE MAKER, the row label is
THE OUTBURST, the deck is "Anger isn't strength." Cold, this plate is about men who
shout. The cold, silent, withdrawing husband — who is the man Ch5 and Ch11 are
entirely about, and on the evidence of this book the primary reader — is let off
the hook in ten seconds flat. He thinks *I don't do that* and turns the page.

The guard line was doing real work and its absence is felt. Restore it as copy:
change the deck to **"Anger isn't strength. Hot or cold, both drive a nail."**
Copy-only, no drawn object touched, fully inside the constraint.

**3. Ch12, has the top row receded too far?**
No. The quieting worked. The grey ticks are dense enough that a full row still
reads as full against a nearly-empty row, and the greying buys the intended reading
order — eye lands on the black row, sees three marks and a long void, then goes up
and finds the comparison already made. Do not undo it.

One thing did not get quietened with it: **"THIS WEEK" is set in full-weight black
caps while the row it labels is grey**, and it sits on the same vertical axis as
"TONIGHT", also full-weight black caps, directly below. Two hard time-labels stacked
on one axis is the only place this plate stalls. Set "THIS WEEK" in the same grey as
its row. Pure weighting.

---

## Per plate

### Ch01 — The Three-Second Window — FAIL

**Cold:** There are three seconds between her words and your reply, and that is
where your marriage is decided.

**Against the Conversation sentence** ("Between what she says and your response is
three seconds. What fills it, **chosen or inherited**, is your marriage"): the plate
carries the first clause and drops the second. What a stranger takes away is *pause
before you answer*, which is the single most widely known piece of marriage advice
in circulation. He does not take away that the gap is *already being filled*, by
something he inherited, whether he participates or not. That is the chapter's actual
claim and the thing that makes it a Stoic book rather than a magazine tip.

**The honest version of this finding:** the plate matches the author's endorsed
2026-09-21 copy exactly. So this is not the Designer missing the brief. The endorsed
line is itself a truncation of the Conversation sentence, and the truncation removed
the load-bearing half. That is the author's call to revisit, not a drawing defect.

**Fix, inside the constraint, copy only:** keep both drawn objects. Change the
bottom caption from "Your marriage lives there." to **"What fills it is chosen, or
inherited. Either way it is your marriage."** Optionally relabel the black block
from "THE GAP" to "THE GAP — CHOSEN, OR INHERITED". Nothing new gets drawn.

**Skeptic's misreading:** a heavy solid black block sitting between "WHAT SHE SAYS"
and "WHAT YOU SAY NEXT" reads as a redaction bar. A defensive man gets *the book
wants me to shut up*. That reading is actively harmful here, because Ch5 and Ch11
are both arguments against staying silent, and this is the plate that opens the book.

**Cut:** the label "THE GAP". A black block between two named endpoints is
self-evidently the gap, and that label is the single most diagram-like thing on the
plate.

### Ch02 — The Mood Mirror — PASS

**Cold:** Match her bad mood and the storm doubles; hold your own and it stays one
storm.

**Against the CS** ("you've outsourced your peace to someone who never signed up to
carry it"): close enough. He gets *do not catch her mood, bring your own*, and the
chapter finishes the jurisdiction argument from there. The top row is good — a line
that physically thickens from the midpoint is escalation you feel before you read.

**The problem, and it is a real one.** The bottom row's "YOUR OWN WEATHER" labels a
bold vertical stroke standing across the horizontal line. Cold, a bold vertical
stroke across a line is a **barrier**. The takeaway on offer is *put up a wall
against her mood* — which is going cold, the exact failure the caption exists to
deny. When a caption has to say "Not to go cold," the drawing is inviting it.

**Fix, inside the constraint, rearrangement only:** move the "YOUR OWN WEATHER"
label to the right-hand end of the bottom line, mirroring "THE STORM DOUBLES" at the
right-hand end of the top line, and drop the vertical stroke to the same weight as
the horizontal. The two rows then read as a matched pair — same starting condition,
two different right-hand outcomes — and the unchanging line weight carries "your own
weather" without a label pointing at a wall.

**Cut:** "To bring something real through the door." There is no door on this plate.
Worse, the next chapter is titled THE CLOSED DOOR, so this caption borrows an image
the reader has not been given and will not be given for another sitting. A reader
taking one chapter a week gets a dangling reference on the second plate of the book.

### Ch03 — The Closed Door — PASS

**Cold:** Every time you defend yourself, the room she has to bring you things
shrinks, until it is gone.

That is the Conversation sentence. One of the three cleanest in the set. The black
advancing right-to-left is the right decision — it reads as her openness being eaten
rather than as a progress bar filling up.

**Skeptic's misreading:** three of the four row labels put the verb on her — SHE
BRINGS, SHE UPDATES, SHE STOPS — and only one on him. Cold, a defensive man can read
this as a plate about a woman who withdraws, with one row of his involvement. The
sequence logic saves it for a careful reader; it does not save it in ten seconds.
Cheap copy fix: "YOU DEFEND" is the only row that names him, so give it weight —
set it in the same black as the filled bars while the three "SHE" labels sit in grey.
Weighting only.

**Cut:** "SHE UPDATES". It is the abstract word on a plate otherwise made of plain
ones, and the row is squeezed between YOU DEFEND and SHE STOPS doing little work.
If the row must stay for the arithmetic of the bars, relabel it "SHE LEARNS".

### Ch04 — The Hole Maker — PASS

**Cold:** Anger drives nails; an apology pulls the nail out but the hole stays, and
they add up.

Carries the CS outright, and it is one of the two plates in the book that work as
symbols rather than diagrams. Nails are recognisable at a glance and the three-beat
sequence lands without effort.

**One muddle:** row 3 has ten dots where rows 1 and 2 had five. Cold, that says
*months on, twice as many holes* — an accumulation claim — while the sub-caption
says "The hole remains," a persistence claim. Two different arguments in one row.
Copy fix: change the sub-caption to **"The holes remain. And they keep coming."**
so the doubling is deliberate rather than a counting error.

See question 2 above for the "Hot or cold" restoration, which matters more than this.

**Cut:** "Stop making holes." It is the one flatly hectoring line in the set, it
instructs where every other caption observes, and the three sub-captions plus the
deck have already delivered the whole argument by the time the eye reaches it.

### Ch05 — The Courage to Come Back — PASS

**Cold:** Walk out of a fight and never come back to say it and you shrink; go back
and say it and you stay whole.

The sub-caption is the CS's final clause verbatim, and the shrunken bar with its
dashed ghost above it carries "becomes small without deciding to" cleanly.

**Person shift.** The deck says "if *you* come back," the caption says "before
silence says it for *you*," and the two sub-captions in the middle say "**he**
becomes small" and "**he** leaves the fight the same size." Cold, "he" is some other
guy, and this is precisely the plate where a reader is looking for an exit. Change
both to "you". Copy-only, trivial, and it is the highest-value fix on this plate.

**Cut:** the short dashed horizontal line sitting inside the solid bar in the GOES
BACK row. In the row above, dashed means "the part that is missing." Here it sits
inside a bar that is not missing anything, so it reads as leftover construction
geometry.

### Ch06 — The Tally You Don't Read Aloud — FAIL

**Cold:** The week is long and tonight is a small slice of it.

Full reasoning under question 1. Short version: I got proportion, the CS is about
visibility, and nothing in the ink distinguishes what you count from what she sees.
Fix is the ghosting of the bar outside the dashed frame, plus letting the two
existing labels carry the rest.

**Cut:** the second caption line. This is the only two-line caption in the first
half of the book and it is the longest stretch of prose on any plate, which is the
tell — the sentence is carrying the argument because the drawing is not. Once the
ghosting lands, "Resentment grows when you expect someone / to read a tally you
never showed them" can come down to one line. Keep the deck; it is the best sentence
on the plate.

### Ch07 — The Private Tally — PASS

**Cold:** You keep a short list of your big contributions, you cannot read hers, and
neither of you counts the mass of small stuff.

Best plate in the book. The scatter field of unregistered tick marks lands in about
one second on pure density, before any label is read, and the short list in an
oversized box quietly says "this is all you have" without a word. The CS's sting —
"it was always going to tell you that you're ahead" — survives the cold read intact.

**Cut:** "The coaching weekend." The other two items are instantly legible domestic
facts. This one stalls the eye — a work coaching seminar? coaching the kids' team?
whose weekend? — and on a plate whose whole virtue is speed, one stalling item is
expensive. Replace with something as plain as "Fixing the router."

### Ch08 — The Tipping Scale — PASS

**Cold:** Small things nobody counted pile up on one side until it tips; catch each
one as it lands and it stays level.

The other plate that works as a symbol. A tipping balance needs no instruction, and
the five faint pebbles against one black one is the sharpest use of ink weight
anywhere in the set — it is the technique Ch6 needs.

**Skeptic's misreading, and it is worth the author's attention.** On the right-hand
scale the pebbles are distributed across *both* pans. A defensive man reads that as
*if I name it, she has to carry half of it* — naming as offloading. The intended
reading is presumably that named things never accumulate on one side at all.
Copy fix inside the constraint: relabel the right panel from "NAMED WHEN IT LANDS"
to **"NAMED, SO IT NEVER PILES UP"**, which reframes the split pans as balance
rather than transfer.

**Cut:** the dashed trajectory lines on the right-hand scale. On the left they earn
their place — they say "these arrived over time, unnoticed." On the right they cross
each other, add clutter, and say nothing the pebbles do not already say.

### Ch09 — The Bottomless Yes — PASS (marginal)

**Cold:** You gave these three things expecting respect, warmth and being heard;
they never came; you never asked; and you are keeping a private list about it.

Content-wise that is the CS. The greying-out of Respect / Warmth / Being heard is
genuinely good — the returns are visibly not there.

**But this is the most diagram-like plate in the book.** Three separate devices
stacked vertically: a two-column arrow table, a long dashed return arrow, and a
stack of ruled lines. Ten seconds gets a stranger through the left column and no
further. It passes on content and fails on speed.

**Layout defect, and I think this one is a render finding rather than a taste call.**
On ten of the twelve plates the hairline divider means *caption follows*. On Ch09 it
sits in the **middle of the artwork** — the ruled-line stack and "a list only you are
keeping" both appear below it. A reader who has learned the template on eleven other
plates will read the list as caption furniture and skip it, and that list is the
"piled up quietly" half of the Conversation sentence. Move the divider down so only
the final caption sits beneath it. Pure rearrangement.

**Cut:** the long dashed left-pointing arrow labelled "you never asked for it". It
is the element that actually stops a cold reader — an arrow pointing leftward from
nothing to nothing, sitting at a height that belongs to neither column. The greyed
returns already say the things never arrived. Keep the words as a plain line under
the right-hand column and delete the arrow.

### Ch10 — The Undecided Line — PASS

**Cold:** A rule you cannot explain caves the first time it is pushed; one where you
can name what it protects holds.

Carries the CS fast. The V-dip is a good symbol, and "this protects ________" with
an actual blank rule to fill in is the cleverest single device in the book — it puts
the reader to work in half a second. The two downward arrows both read as pressure,
which makes the comparison work without a "becomes" arrow having to be explained.

**Set-consistency defect:** Ch10 is the only plate in twelve with **no hairline
divider and no bottom caption**. It stops dead on a black label box. Bound with the
other eleven it will look truncated, or like a page that lost its last line. The
author's endorsed Ch10 line is already spent as the deck, so a caption here is new
copy — that is an inbox question, not something I would have a Designer invent.

**Skeptic's misreading:** the DECIDED line is dead straight and does not yield at
all. A defensive man reads *a real man never bends*, and this is the one plate in
the set where the drawing flatters him rather than costing him anything. The deck's
preference/boundary distinction half-covers it; the picture alone rewards
stubbornness.

**Cut:** the faint dashed rectangle sitting behind the V-dip. It means nothing, it
is the only purely decorative object in the set, and at phone size it reads as a
selection box or a render artifact. The V carries the sag on its own.

### Ch11 — The Conversation She's Never Heard — PASS

**Cold:** You have run the argument over and over in your head and said none of it
out loud.

Fastest read in the book alongside Ch07. Seven heavy redaction bars in a solid box
against an empty dashed box needs no instruction at all.

**Cut:** the small grey dashed arrow between the two boxes. It asserts a flow that
by the chapter's own argument never happened — nothing crossed. The full box beside
the empty box says it better, and deleting the arrow makes the plate both faster and
more honest. This is the rare cut that improves the argument.

### Ch12 — The Thing With No Deadline — PASS

**Cold:** Everything with a deadline got done all week; the one thing for her stopped
months ago and tonight is still empty.

Good close to the book. The hollow open square at TONIGHT — the one unfilled mark in
twelve plates — reads as a slot still available, which is the right last note.

See question 3 for the "THIS WEEK" weighting fix.

**One cheap win.** The Conversation sentence has a number in it — "five months he
never felt go by" — and the plate has no number anywhere. "the stretch you never felt
go by" is vaguer than the sentence it comes from. Relabel the bracket **"five months
you never felt go by."** Copy only, and a number lands harder than "the stretch."

**Cut:** "you didn't stop loving her." It is the only consoling line in the set, it
sits inside the drawing area rather than in the caption where reassurance belongs,
and it arrives directly beneath the empty stretch whose whole job is to sting. The
bottom caption already lets him down gently. Let the void be a void for one beat.

---

## What is only visible having looked at all twelve

**1. Ch07 and Ch11 are the same drawing.** Solid bordered box on the left, full of
content; dashed bordered box on the right, empty, with one grey italic line floating
in it; bold caps label above each; same proportions, same positions, same size.
"YOUR PAGE / HER PAGE" and "INSIDE YOUR HEAD / IN THE ROOM." This is the most
damaging thing in the set. Per the audience note the reader takes one chapter at a
time, often days apart — which does not protect against this, it makes it worse. He
will not consciously think *I have seen this*; he will feel a dull familiarity and
read Ch11's plate less carefully than it deserves, and Ch11's plate is one of the
two best in the book. Differentiating them is a rethink of one or the other, so it
is outside this round's constraint. Name it for the author as a live decision rather
than fixing it quietly.

**2. The private-ledger cluster: Ch06, Ch07, Ch09.** Three plates in four chapters
whose ten-second takeaway is *you are keeping a count she cannot see*. Ch06 and Ch07
are adjacent and **both have "tally" in the title** — "THE TALLY YOU DON'T READ
ALOUD" followed immediately by "THE PRIVATE TALLY". Ch03's caption, "She's been
keeping track longer than you know," makes a fourth counting plate, though that one
is the mirror image and earns its place. The titling half of this is cheap to fix
and inside the constraint: retitle Ch06 off the word "tally" and the adjacency stops
announcing itself.

**3. The set is still mostly diagram, and it knows where its exceptions are.** Ch01,
Ch02, Ch03, Ch04 and Ch06 are all horizontal bars or lines with black fill or marks
along them — five of the first six plates. The set only breaks form at Ch05
(columns), Ch08 (a balance), Ch10 (a profile line). **Ch08 is the only plate in
twelve that draws a real-world object, and it is also one of the two fastest reads.**
Ch04's nails are the other fast read and they are the other recognisable object.
That correlation is exactly what the outside feedback was pointing at, and it
survives this round. The round did real good — Ch02's thickening line, Ch12's
quieted row, Ch08's faded pebbles are all better than they were — but the front of
the book still asks to be decoded.

**4. Dashed line means five different things.** Ch05: the part that is missing.
Ch06: a frame around a region. Ch07 and Ch11: a container that is empty or
unreadable. Ch08: a trajectory through the air. Ch09: an arrow that never fired.
Ch10: nothing at all. A reader one chapter a week never builds the vocabulary, so
every plate re-teaches it from scratch and spends its first second doing so. **This
is the cheapest set-wide improvement available.** Fix dashed to one meaning —
*absent, or not visible to you* — which is already what it means on Ch05, Ch07, Ch09,
Ch11, and on Ch06 the moment the ghosting fix lands. Only Ch08's trajectories and
Ch10's stray box would have to change, and both are cuts I have already recommended
on their own merits. Five plates would be brought into line by deleting two things.

**5. Caption furniture is inconsistent across the set.** Ten plates: hairline
divider, then one caption. Ch09: divider sits mid-drawing. Ch10: no divider, no
caption. Ch06, Ch11, Ch12: two-line captions. Bound together these will read as
three different templates. Ch09 and Ch10 are the two to fix.

**6. Nothing in twelve plates depicts warmth.** Ch02, Ch05, Ch08 and Ch10 each show
a right-hand way, and in every case the good outcome is drawn as the *absence of
damage*: a level scale, an unbroken line, a bar that did not shrink, a line that did
not sag. Twelve plates of harm avoided and none of good arrived. For a book whose
third part is called Warm Sun, that is worth the author knowing. It is not fixable
inside this round and it is not a defect in any single plate — it is only visible
from the whole set, which is why it is here.

---

## What I read, and what I did not

**Read:** all twelve chapter plates as rendered PNGs (`runs/chNN/pdf/plate.png`),
cold and in isolation, before opening anything else. Then all twelve
`runs/chNN/plate.svg` text layers, to prove the renders were current. Then all twelve
`runs/chNN/plate-brief.md` for the Conversation sentence and the author's endorsed
2026-09-21 copy additions.

**Not read, deliberately:** the chapter prose, the distillations, `plate-notes.md`,
`plate-concepts.md`, the stage-2 `plate-pick.md` files, and the prior
`plate-read.md` files. A cold read contaminated by the previous round's verdict is
not a cold read.

**Not read, as a limitation:** the part plates (`runs/parts/plate-*.svg`) were out of
scope and I did not look at them, so finding 6 about warmth is drawn from the twelve
chapter plates only and a part plate may already answer it.

**Not done:** I could not rasterise fresh, because Bash is disabled in this session.
I mitigated by proving the existing `pdf/` renders match the current SVG text on all
twelve, which catches stale copy but would **not** catch a purely geometric
regression — a shifted object or a clipped path with unchanged text. That residual
risk is unchecked, not passed.
