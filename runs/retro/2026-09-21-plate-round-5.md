# Retro: plate round 5 — 2026-09-21 12:41

Window `ac273d3..9c3b822` (from `.claude/state/retro-window`), ten commits, five
substantive: `e893baf`, `7641396`, `72d3dcf`, `6bc51bd`, `fee3d8f`.
`retro-last-sha` already read `9c3b822` at review time — the documented collapse
(#030) — and the window file was used instead, as it should be. That mechanism
worked.

## What broke: a verification confirmed a claim it could not have refuted

The Panel reported the cached rasters stale. The Publisher did the right
instinct — checked that rendering was deterministic first, so a byte comparison
would mean something — then hashed, got a mismatch, and recorded the
confirmation in `72d3dcf`'s commit message.

**The rasters were not stale. They are byte-identical to their SVGs, and were
at `72d3dcf` too.**

The comparison had an uncontrolled variable. `runs/chNN/pdf/plate.png` is stored
at scale 2 (1280px against a 640px viewBox); `svg_to_png`'s default is scale 3.
Re-rendering at the default and hashing compares a 1920px render against a
1280px file, which cannot match no matter what the art says:

    ch01 cached=(1280, 680)  fresh at default=(1920, 1020)

Re-rendered at the cached file's own scale, all twelve match, now and at the
commit where the claim was made:

    ch01..ch12 at HEAD:     match  (12/12)
    ch01, 06, 07, 12 at 72d3dcf: match

Determinism was verified and was real; it just was not the variable that
mattered. The test returned the answer the claim predicted, and nothing in it
could have returned any other.

Two consequences. The conclusion "no build ships old art" is still **true**, but
not for the stated reason: `plate_packet.py` re-renders unconditionally
(line 186, no `isfile` guard) and `compile.py` embeds the SVG directly rather
than any PNG. Nothing in the repo *reads* `runs/chNN/pdf/plate.png` at all — the
only writer is a hand-typed one-liner in `gw-plate/SKILL.md` line 83, and its
only consumer is the author's eyes at line 110. So the real exposure was never
the build; it is that **a verdict can be given on a stale image**, because the
one artifact the author looks at is refreshed by a command a desk has to
remember. That is a Rule 14 problem, not a tracking problem.

Second: the finding was parked as "the stale files on disk are inbox #076".
#076 is about `runs/manuscript/` tracking regenerable PNGs and stamped
filenames. It does not cover `runs/chNN/pdf/`. A false conclusion was filed
under an item that would never have revisited it.

**Shape:** a plausible number, no error, not run against a known-right answer.
FINDINGS.md line 316 calls this the Archivist's first standing instruction and
line 703 logs instance eight. This is **instance nine**, with a new wrinkle
worth naming: the measurement was *partly* hardened — determinism was checked —
and the partial hardening made the result feel earned. A half-controlled
experiment reads as a controlled one.

## What was missing: `grounded` trusts text nobody wrote as book copy

The author asked whether the provenance tag is honest. The tag itself is fine:
`plate_brief.py` round-trips `- <date>: <text>` through regeneration, so
"[reader feedback, endorsed by the author 2026-09-21]" is durable, and eleven
briefs carry it. Recording endorsed copy as endorsed, rather than as his own, is
the honest call.

The weakness is underneath it. `plate_check.py` line 276 appends the **whole**
brief file to the grounding corpus. The brief is generated, and its boilerplate
is therefore legal plate copy. Measured:

    LEGAL   'the drawing carries the argument'
    LEGAL   'a man who never read the chapter'
    LEGAL   'Nothing here is invented'
    LEGAL   'endorsed by the author'

A plate could print "The drawing carries the argument" as its closing line and
pass `grounded`. So the row that makes the endorsement safe is looser than the
guarantee it is trusted for — it cannot distinguish the chapter's words from the
brief's own furniture, or from the provenance tag added to mark foreign copy.

Narrowing the corpus to the distillation fields and the Author-additions
bullets, with the bracketed tag stripped, was tested against the live set:

    chapters failing grounded: []      (0 of 12 regress)
    refused 'the drawing carries the argument'
    refused 'endorsed by the author'
    LEGAL   'Between what she says'
    LEGAL   'Your marriage lives there'

The endorsed lines stay legal; the furniture stops being. This is a
**narrowing**, so it pays for itself.

A smaller companion: `plate_brief.py` generates the sentence "The Author
additions section is the one place words from the author's own mouth are
recorded." Eleven briefs now print that line directly above copy from another
model. The tag on each bullet is honest; the generated sentence above them is
now false.

## What worked

- **Rule 7 held exactly.** Re-running `plate_check.py` on all twelve
  independently reproduced the desks' self-reports with no discrepancy: no FAIL
  rows, two WARNs, both title-vs-Mechanism under #065. Self-reported counts
  matching the script is the thing that was wrong on Ch9, Ch10 and the Prologue.
- **The `grounded` rule did its job in the live case.** The Designer refused the
  Panel's supplied Ch4 copy ("Hot or cold, both drive a nail") because the
  chapter says neither phrase, and used the chapter's words instead. Checked
  set-wide: `grounded` printed clean on all twelve, so nothing ungrounded
  reached a plate this round. A cold desk declining a reviewer's words is the
  rule working before anyone had to enforce it.
- **Ch5's WARN is not a data error.** 'The Remaining Nails' genuinely continues
  Ch4's 'The Hole Maker'; #065 covers it correctly. Checked, clean.
- **`fee3d8f`'s extractor reasoning was right.** Bounding the context paragraph
  by the next `**Label:**` rather than a blank line reads Ch11 correctly where a
  paragraph-break rule would have printed nothing and said nothing. That is the
  house's own recurring shape, caught *before* it shipped rather than after.

## What was too hard

`plate_packet.py` has no fixture in `tests/run.py` — `plate_check_cases()`
exists, nothing for the packet. The Ch11 catch above was a human noticing, and
the identical silent-fallback defect in the same file is already open as #075
(`curated_names()` falling back to 'Chapter N'). Two known silent fallbacks, one
file, zero cases. This is evidence for #075, not a new item; the text is in the
suggestions below.

Corpus stands at 18,540 words (17,017 on 2026-09-19). The window changed no
rules — the growth predates it — so it is context, not a finding of this
session.

## Not re-filed

#048, #065, #070, #071, #073, #074, #075, #076, #077, #078, #079, #080.
