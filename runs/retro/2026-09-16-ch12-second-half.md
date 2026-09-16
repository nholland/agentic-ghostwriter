# Archivist Review — 2026-09-16 — Ch12, draft through author rulings

Scope: only what followed `runs/retro/2026-09-15-ch12-dry-run.md`. PROPOSALS ONLY
(Rule 17). Ran cold, without the Publisher's findings.

**Verdict: the second half mostly worked.** Seven desk runs, 1,202 words passing
every counted check, the book repo untouched throughout. Two things would have
shipped a wrong chapter.

---

## 1. A desk's environment claim was false, and the chapter prints a fact because of it

The Ch12 Marcus citation records: *"The text of IV.24 was NOT retrieved: the
Gutenberg fetch truncated before Book IV and every other candidate host was
proxy-blocked."* Executed today, one curl: `gutenberg.org` returns **200,
451,529 bytes**. Long's IV.24: *"Occupy thyself with few things, **says the
philosopher**, if thou wouldst be tranquil."* The philosopher is unnamed;
"Democritus" appears nowhere near IV.24 in Long's text or notes.

`refined.md:21` and `ch12-reader.md:21` print *"an old line he credits to the
philosopher Democritus."* The desk correctly refused the **quotation** and then
let the **attribution** through. A 450 KB file truncating in WebFetch was read as
"unreachable" rather than "wrong tool" — the desk had Bash and did not use it.

**The fix was already written down.** `playground-260420/.claude/LEARNINGS.md`,
2026-09-09: *"Promote, by replacement: a reachable primary-text channel... It
carries Long's Marcus (#15877)."* Seven days old, the exact ebook id, invisible
to the desk that needed it. Its GITenberg mirror is now blocked; `gutenberg.org`
direct is not — so the recorded channel was both correct in substance and stale
in detail, which prose cannot self-correct and a probe can.

**Chapter fix needed before the verdict:** line 21 must not say Marcus credits
the line to Democritus.

## 2. `next.py` calls for a verdict over the author's own unapplied rulings

```
$ python3 scripts/next.py --chapter 12
ch12: next stage is verdict (refined; plate present) -> /gw-compile 12
$ python3 scripts/inbox.py
inbox: 6 open, 7 ruled but not yet applied
```

Items #008, #009 and #014 are his rulings on this chapter's prose, made after
refine round 2 finished. Close-conditions executed: `ton of bricks` 0 hits,
`grilling` 0 hits, `ebbs and flows` 2 hits where it needs 0. **The inbox is
correct; the oracle cannot see it.** Same blind spot as yesterday's finding #1,
now in a second form: the author would be asked to sign off on prose missing the
scene he supplied and still carrying the cushion he cut.

## 3. The clean-room checker is handed the answers by the skill, twice

`gw-draft/SKILL.md:82` and `gw-refine/SKILL.md:63` both say to hand
`gw-specchecker` the file that contains `## Draft Notes` / `## Editor's Notes` —
2,546 apparatus words beside 1,202 of prose. Starvation is the mechanism and the
skill names the file that defeats it. The Publisher stripped apparatus by hand
both times. **A gate that holds only because someone deviated from the skill is
not a gate.** `voice_check.py:117` already has `prose_only()`.

## 4. Rule 15, fourth form, created this session

`runs/ch12/draft.md` was edited **in place** by the revise round, so
`conformance.md` now describes a draft that no longer exists and looks current,
in the same directory. The cold draft is the bake-off's evidence and survives
only in git.

## 5. The one HARD check that can silently skip reads a field that is in the file

`refined.md:315` declares `metaphor_family: muscl,atroph`. Without the flag the
script prints `[skip] ... UNCHECKED, not passed` and then `RESULT: all HARD
checks passed`. The datum was in the file the script had already read. This is
yesterday's finding #4 with its cause identified.

## 6. Compile is environmentally impossible and was discovered at point of use

No weasyprint, pandoc or wkhtmltopdf; pip cannot reach PyPI. The renderer fails
honestly. But `resolve_book.py` reports `8/8 optional present` — it checks that
`chapter_pdf.py` **exists**, not that it can **run**. Rule 16 says a deferred
capability is registered; `GAPS.md` has no compile entry.

---

## What held

- **Three cold desks wrote to the inbox rather than deciding:** the Anti-Slop
  Reader (#012–#014), the Designer (#015 — refused to invent a style file), the
  Conformance Checker (#011 — caught a desk overriding a ruling).
- The refined-prose conformance re-run earned its cost: the objection row failed
  on the draft and passes on the refined text.
- `plate.svg` parses clean, produced by a desk with no way to check that.
- **Rule 8 held across seven desk runs.**

## Recurrences, unfixed, stated once

`citations.py` still reports 1 against 8. `okf_gate.py` still cannot see `runs/`.
`session-start-sha` re-anchored again, so this review's window covered one commit
of a nine-commit arc.

---

## Proposals, ranked

1. **`scripts/fetch_source.py`** — curl a Gutenberg id, assert the `Translator:`
   line, print the passage, exit non-zero on a real block. Callers:
   `gw-researcher`, `/gw-verify`. Replaces a prose channel that went stale in
   seven days. *Would have shipped a wrong chapter.*
2. **`next.py` does not send a chapter to verdict while any inbox item for it is
   open, or ruled with its close-condition still false.** 41 words. **Deletes**
   the dead `if "inbox.md" in have:` branch already named yesterday. One change,
   not two. *Would have shipped a wrong chapter.*
3. **`voice_check.py --emit-prose`**, and the two skills call it. **Deletes** 44
   words of skill text; net −20, and the Publisher's deviation becomes the
   instruction.
4. **The revise loop stops overwriting the cold draft** (`draft-rN.md`); pair
   with yesterday's `brief-gaps-r1.md` rename as one Rule 15 fix.
5. **`voice_check.py` reads `metaphor_family:` from the file** when the flag is
   absent. **Deletes** the skip-branch instruction string and retires yesterday's
   "exit 2 on SKIP" proposal — a check that cannot silently skip needs neither.
6. **Register compile in `GAPS.md`** with the trigger that closes it.
7. **Add `Bash` to `gw-designer`** (one word) so it can parse its own SVG. No SVG
   gate yet — one plate is not evidence.
8. **Nothing counts rounds.** Rule 6 held twice because a model remembered.
   `grep` finds no round counter in any script. Register it.
9. **The verbosity the author named has a source in the instructions.**
   `gw-draft/SKILL.md:88-91` mandates a five-item status dump at every stage;
   three other skills have their own. Rule 18 says answer short and loses,
   because the per-skill blocks are read at the moment of reporting and Rule 18
   is not. Proposal: those blocks describe what goes in the **artifact**; the
   reply carries only what the author must decide.

**Open item, book repo (Rule 8):** `playground-260420/scripts/verification_packet.py`'s
docstring claims the environment "blocks every host that carries a primary text."
Executed today: false. The 2026-09-09 learning already flagged it as "now half
true" and it was never corrected.
