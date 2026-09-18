# Archivist Review — 2026-09-16 — the three defects were already fixed once

Scope: since `runs/retro/2026-09-16-verification-failures.md`. PROPOSALS ONLY (Rule 17).

## The finding

The three formatting defects found by rendering Ch12 and looking at the page are
not three discoveries. They are **the three transforms already implemented,
numbered and dated** in the book repo's `scripts/chapter_pdf.py`, function
`markup()`, whose docstring opens: *"Three transforms, each fixing a defect the
author found in a shipped PDF."*

1. a bold-only line renders as body text rather than a beat label
2. consecutive `**Label:** value` lines merge into one paragraph — its docstring
   names *"the Distillation's Mechanism, Conversation, Lesson, Challenge"*
3. a paragraph that is entirely an italicised quotation must be a blockquote

**Three for three.** Verified against the book's source. Fixed there 2026-08-23;
re-found by the author today in output from `chapter_pdf_local.py`, which was
written from scratch rather than porting that function.

This is the incident `gw-compile/SKILL.md` names as its own reason: *"its
predecessor was two copies of the same stylesheet that shipped the same two
defects and had only one fixed."* **The rule existed, was correct, and was
invisible at the moment the fallback was written.** The register of defects lives
in a docstring nobody is required to read.

The second renderer is justified — the book's cannot run here. It is a
**registered gap whose registration was never written**, and its own docstring
claims `GAPS.md` registration that does not exist.

## `voice_rules_check.py` accepts too much — and Rule 8 now rests on it

Verified by mutation, `house.json` restored bit-for-bit:

| mutation | result |
|---|---|
| `em_dash_max` 0 → **9** | `[ok]`, exit 0 |
| `bold_max_per_piece` 1 → **7** | `[ok]`, exit 0 |
| `you_density_min_per_1000` 40 → **1** | `[ok]`, exit 0 |

Two holes. The probe span for the first two contains no digits, so **nothing is
compared and `[ok]` is printed anyway** — a SKIP reported as a PASS, Rule 12's
exact shape, inside the gate. And the check accepts *any* number anywhere in the
matched span: `1` passes because it appears inside "1,000".

The metaphor-cap regression passed only because 3 is the only digit in its probe.
**Rule 8's new condition (e) depends on this script**, so this outranks
everything else here.

Fix: an explicit `spec_number` per rule (or `null` with a stated reason), compared
against that one number, printing `NUMBER-UNCHECKED` — never `ok` — where it is
null. Deletes the `nums`/`accepted`/`value * 100` heuristic added this session.

## The rest, ranked

**`scripts/pdf_format_check.py` with a caller.** A 12-line fixture carrying the
three shapes, asserted against the emitted HTML. The renderer already writes its
HTML beside the PDF, so the check has an input today. Skill text 49 words,
**deletes** the 60-word "One renderer, not two" section. Net −11 and a check.

**`practice_sync.py`'s root input is the wrong file.** `refined.md`'s
`## Distillation` is byte-identical to `distillation.md` minus its H1, so
`distillation.md` is a derived file with nothing deriving it. Generate it from
the chapter and compare guide ← chapter. **Deletes** a hand-maintained artifact.

**Two RULED inbox items can never close.** `#012` and `#014` grep the whole file,
and the only remaining matches are in Editor's and Draft Notes — the apparatus
recording the fix. **The record of the change blocks the change.** `next.py`
overstates unlanded rulings by at least 2. `voice_check.py` already strips
apparatus; expose it as `--prose-only` and point the conditions at it.

**The manual's stale half — and my diagnosis named the wrong file.** Both false
sentences live in `scripts/manual.py`'s `NARRATIVE`, not `manual_content.py`.
Verified. Acting on my commit message would have edited the wrong file. Fix:
derive `NARRATIVE["never"]` from CLAUDE.md's rule headings and add `CLAUDE.md` to
`inputs_digest()`, so any rule edit fails `--check`.

**Brevity: the cause was found last retro and not acted on.** `git log` shows no
file under `.claude/` changed this arc. `gw-draft/SKILL.md:88–91` still mandates a
five-item status dump. The third ask has the same answer as the second.

**Proposals have no queue.** 0 of the prior retro's 7 suggestions were applied;
the only two changes that landed were the two the author approved live. The
"two tokens, net zero words" fix to `gw-designer.md` is still unapplied — and the
Designer redrew a plate this arc, without Bash, pointed at the wrong directory.

## What worked

- Four rulings closing themselves off the rewrite: the auto-close mechanism doing
  its job.
- The Rule 8 exception ships with **its own deletion trigger**. First rule in this
  repo to carry an expiry.
- `svgcheck.py` now derives the right margin from the file's own viewBox; the fix
  generalises rather than patching one case.
- `chapter_pdf_local.py` rasterises plates and omits running heads **because the
  author listens to the PDF** — a real decision for a reader nobody else modelled.

## Unexecuted

The book's `chapter_pdf.py` could not be run (weasyprint absent). The
three-for-three mapping is textual comparison against its source, not a rendered
diff.
