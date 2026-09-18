# Source and Citation Policy

*Foundation artifact. Hand-authored and locked, revised via `/book-feedback
06-sources` — never regenerated. Same pattern as `04-archetype.md` and
`05-framework.md`.*

*Established 2026-09-07, after nine citation defects reached compiled prose and
six were printed. Extended 2026-09-08 with two rights findings. Read by
`/book-verify` at Step 0.*

---

## House translations

| Author | Edition | Status |
|---|---|---|
| Marcus Aurelius | **George Long** (Little, Brown, 1889) | Public domain |
| Epictetus | **George Long** (George Bell & Sons, 1877) | Public domain |
| Seneca, *Letters* | **Richard Gummere** (Loeb, 1917–25) | Public domain (US) |

**Decided on evidence, not inheritance.** Three verified-clean samples were
compared directly. Haines was expected to win on readability and did not — his
*Meditations* VI.8 (*"The ruling Reason it is that can arouse and deflect
itself"*) is denser than Long, whose *Enchiridion* 8 uses a modern "you." Rights
and readability point the same way, and the book is self-published, so permissions
work for Hays (Modern Library) or Hammond (Penguin) is a real cost with no
offsetting gain.

**One ratified exception:** *Meditations* VI.8 in Ch2 stays **Haines** (Loeb,
1916). It is public domain, already printed, and verified clean against the 1916
scan. No reason to churn it.

**Known caveat, accepted.** Long's Marcus uses *thee/thy*, which sits against
`01-voice.md`'s counted 6th-grade reading target. Mitigated — partially, not
totally — by the "old language, then translate in plain English" move established
in Ch10. Where a Long passage would fight the register badly, prefer rendering the
idea in the author's own words over forcing the quotation.

## Editions that are NOT house standard

Not because they are bad, but because they do not fit the public-domain posture:

- **Gregory Hays** (Modern Library, 2002) — in copyright. Currently the source of
  three verbatim citations awaiting swap.
- **Martin Hammond** (Penguin, 2006) — in copyright. Two printed citations, both
  also carrying wrong locators.
- **A. S. L. Farquharson** (Clarendon, 1944) — rights ambiguous. One printed
  citation.
- **Cora Lutz** (Yale Classical Studies, 1947) — Musonius Rufus. Almost certainly
  still in copyright. Fine while the chapter paraphrases; needs a decision before
  any verbatim quotation.
- **John Basore** (Loeb, 1935) — Seneca's *De Beneficiis*. In copyright. The
  public-domain alternative is **Aubrey Stewart (1887)**, which is what this
  standard points to.

## Evidence bar

The full schema is `.claude/OKF.md`, "The three citation axes." The rule that
governs everything else:

> **Search may LOCATE a source or FLAG a defect. It may never TRANSCRIBE a
> quotation.**

A `quote_form: verbatim` citation cannot reach `verifiable` on `search-synthesis`,
`database-abstract`, or no evidence. `scripts/okf_validate.py --strict` enforces
it; `/book-chapter-refine` and `/book-compile` run that gate before writing prose.

**Why this bar and not a softer one:** asked for *Meditations* 10.3 in Long, a web
search returned a fluent answer that silently welded Long together with an
unrelated 18th-century translation, and did not hedge. Search fails
*confidently*. Six of the nine original defects trace to that failure mode.

**Only the author sets `verified`,** against his own copy — CLAUDE.md Rule 11.
Autonomous work tops out at `verifiable`.

## Quoting rules

- **Quotation marks are a claim about wording.** If the prose puts words in quotes
  and attributes them, `quote_form` is `verbatim` regardless of what was intended.
  A paraphrase printed inside quotation marks is a misquotation. (This is how
  defect #10 survived — filed `paraphrase`, printed as a quotation.)
- **Name the translator** whenever wording could differ between editions. An
  unattributed classical quotation reads as edition-neutral, and none of them are.
- **Never splice with a bare ellipsis** across non-adjacent passages. Two defects
  are of exactly this kind (*Letter* 91, silently; *Letter* 81, marked but
  unconfirmed). Quote the parts separately, or mark the omission and verify the
  fragments are contiguous enough to join.
- **Em dashes inside a quotation** survive `01-voice.md`'s ban only where the
  citation's `verification_note` records that the dash is the translator's own,
  confirmed against a printed page.

## Publishing posture

Self-published. Every quotation should be free to print without permissions work,
which is what the public-domain standard above buys. If a licensed translation
ever becomes worth the cost, that is a deliberate decision recorded here — not
something that arrives by a drafter picking a nicer-sounding rendering.

## Retrofit outstanding

Six verbatim swaps to bring printed prose onto the house standard, plus one
attribution fix. Tracked in `quality/citation-defects.md`. **Applied 2026-09-09**
from Long's Gutenberg texts (see `quality/citation-defects.md`, "Resolved
2026-09-09 (second pass)"); the Ch11 4.49 row needed no swap because the chapter
carries the idea without quoting it. Ch9's *Meditations* 12.4 (Hays) was swapped
in the same pass. Remaining items: parking-lot #35.

| Chapter | Citation | Current | Action |
|---|---|---|---|
| Ch3 | *Meditations* 11.18 | Farquharson 1944 | → Long |
| Ch4 | *Meditations* 6.20 → **XI.18** | Hammond 2006 | → Long, and fix the locator |
| Ch5 | *Meditations* 9.28 → **IX.30** | Hammond 2006 | → Long, and fix the locator |
| Ch11 | *Meditations* 4.3 → **VI.52** | Hays / Hicks | → Long, and fix the locator |
| Ch11 | *Meditations* 10.3 | Hays 2002 | → Long |
| Ch11 | *Meditations* 4.49 | Hays 2002 | → Long |
| Ch2 | *Enchiridion* 1 | labelled Carter, is MIT text | → Long, fix the attribution |
