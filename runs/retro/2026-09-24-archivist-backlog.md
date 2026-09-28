# Archivist review — 2026-09-24 07:44
Window: `1874e9b..8bc800e` (from `.claude/state/retro-window`), 11 commits.
Most of it is a Codex session merged from main: Chapter 13 drafted, revised and
refined; PDF consolidation; a scoped review stage in `next.py`; an edit to this
desk's own Assess section. This session's own work: the merge, and #092 applied.

## Proposed FINDINGS.md entry

## 2026-09-24 07:44 — #092 capped what the Archivist returns; nothing caps what it files

`#092` landed correctly and closed on a fixture, not a grep: `retro-check.sh`
now waits for three watched-path commits, `gw-retro` returns at most two
suggestions, and `tests/run.py` carries both halves of the discrimination — one
commit holds, three dispatch. That is the right shape, and it is the shape this
desk's mandate asks for.

It fixed the wrong end of the pipe. Counted this morning: **60 of the 103 inbox
items ever filed were raised by `gw-retro`, and 31 of the 55 now open are its**
— more than the other ten desks and the Publisher combined. The oldest open one
is from `2026-09-19 13:56`, five days ago. The last `gw-retro` item the author
ruled on is from `2026-09-20 14:54`, four days ago. Arrival did not stop; ruling
did. The `--applied-by` mechanism was built because 0 of 16 proposals across two
sessions were ever applied — proposals are prose in a file nobody greps. It
worked: a *ruled* proposal now closes itself. It does nothing for an *unruled*
one, and 31 of those are the same failure wearing the fix's own clothes.

Lens: what recurs, and the shape is the ledger's — the old one grew 739 to 6,026
words in 27 days and ate five of nine sessions. It has not grown here (FINDINGS
is 807 lines and this session added none of it); it relocated to `inbox/`, where
each entry is individually well-formed, closes itself if ruled, and costs the
author a decision he has not made in four days.

Proposed: `inbox.py --add` refuses a `gw-retro` filing while 20 or more
`gw-retro` items are open, naming the three oldest and saying `/gw inbox`. Not a
lapse timer — at five days, nothing would expire and nothing would change. A cap
binds today and is the same policy `#092` already applied to what this desk
*returns*, applied to what it *files*. Filed as an inbox item, per Rule 17.

Corpus: 18,789 words (`cat CLAUDE.md .claude/agents/*.md .claude/skills/*/SKILL.md
| wc -w`), against 17,017 on 2026-09-19 — +1,772 in five days, +10%. Not a
proposal, a number to carry.

---

## Suggestions

**1. New check with a caller — cap open `gw-retro` inbox items at 20.**
What it changes: `inbox.py --add` exits non-zero for `--raised-by gw-retro`
when 20+ `gw-retro` items are open, printing the three oldest IDs and `/gw
inbox`. Other filers unaffected (the 2026-09-20 widening of a different
`inbox.py` guard to all filers was measured harmful and reverted; #053).
Corpus cost: **0 words** — it is script behaviour, not rule text. No addition to
CLAUDE.md or any desk file.
What it replaces: nothing deleted from disk; it deletes the *open* count's
growth, which is the thing costing time. Filed as an item so the author rules,
not applied.
Proof: a fixture in `tests/run.py` (20 open gw-retro items → refusal; 19 →
accepted; a non-gw-retro filer at 20 → accepted). Closes on `tests/run.py`, not
a grep for its own text.

**2. Open item, not a suggestion — the corpus is up 10% in five days.**
18,789 vs 17,017. Two of the additions in this window were the Assess-section
rewrite (which removed the "most things that surface do not survive this step"
damper and added "judge author effort and book quality, not recommendation
count or rule-word savings") and `#092`'s two-suggestion cap (which adds a
damper back). Net direction unclear; one window is not a trend. Recorded here,
not filed. Count it again next review before anyone cites it.

## What worked

- **`#092` closed on its fixture.** `tests/run.py` was changed so that one
  watched-path commit must *not* dispatch and three must — the discrimination,
  not just the happy path. That is the standard `grep -q 'spec_number'` failed
  twice; it held here.
- **The PDF consolidation is a net deletion.** 5,218 insertions against 13,102
  deletions across 214 files, most of it point-in-time PDFs and HTML packets
  whose filenames (`...-ch12-plates-draft-2026-09-20-2200`) had done their Rule
  15 job and could then be thrown away. Shrinking is a finding.
- **The fixture suite grew with the code that needed it**: 123/123 at the
  2026-09-23 FINDINGS entry, 147/147 now, green including three scope cases for
  `next.py`'s new review gate.

## Looked at, found clean

- `retro-check.sh` below threshold: it exits before `touch "$DONE"` and before
  writing `retro-window`, so a 1- or 2-commit session defers its review rather
  than losing it. The `#064` window-overwrite hazard is unchanged but now rarer.
- The sub-threshold fallback named in the hook's comment is real, not a promise:
  `.claude/skills/gw/SKILL.md:77` dispatches `gw-retro` on "done"/"that's it".
- `next.py`'s new `chapter_review_issue`: hashes its inputs, rejects a null or
  blank scope, rejects a report that is also an input. Ch13 carries a valid
  `review.json` and reads `verdict`; ch01-ch12 are shipped and bypass it.
- `docs/manual.html` drift: regenerated and committed in `ac056dc` during this
  review; `python3 scripts/manual.py --check` → `manual: in sync (10 cold desks,
  20 commands)`.
- Working tree clean, `tests/run.py` 147/147, `runs/log.md` passes `log_check.py`
  (no damage reported at the last Stop).
