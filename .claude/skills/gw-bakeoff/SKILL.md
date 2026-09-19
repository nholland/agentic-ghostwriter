---
description: Run or resume the parallel bake-off between the old book pipeline and this one for a given chapter - build the blind comparison packet, walk the author through the blind read, then unseal. Use when comparing the two systems on the same chapter.
---

# /gw-bakeoff — compare the two pipelines on one chapter, blind

Argument: a chapter number, or `--unseal NN`. `$ARGUMENTS`

## Why blind

The author is the judge and also the person who wants the new system to win. If
he knows which draft is which, that preference is what gets measured. So the
counted comparison is labelled by variant, the prose files are neutrally named,
and the mapping stays sealed until the verdict is written down.

## Build

Resolve the book first. The control side is the old pipeline's chapter — and
since the 2026-09-18 migration those came over with the book, so they are here,
in `{bookRoot}/chapters/`, not in the archive. **Nothing about a bake-off needs
Playground-260420 cloned.** Ch1-11, the prologue and the introduction are the old
pipeline's prose; Ch12 onward is this house's own and has no control, so there is
no bake-off to run for it:

```
python3 scripts/resolve_book.py
```

Stop if it exits non-zero. Take `bookRoot` from its output; never assume a path.

Require both sides to exist:

- control: `{bookRoot}/chapters/chNN/refined.md` — the old pipeline's prose, migrated (Ch1-11, prologue, introduction)
- variant: `runs/chNN/refined.md` (this pipeline, from `/gw-draft` + `/gw-refine`)

```
python3 scripts/bakeoff.py --chapter NN \
  --control {bookRoot}/chapters/chNN/refined.md \
  --variant runs/chNN/refined.md \
  --metaphor-family "<declared in Draft Notes>"
```

Then dispatch `gw-specchecker` **twice** — once per variant, each time with only
the outline section and that variant's prose, and never told which pipeline made
it. Append both results to `bakeoff/chNN/comparison.md` labelled by variant.

## The read

Hand the author `bakeoff/chNN/variant-1.md` and `variant-2.md`. Ask him to read
cold, in that order, and answer the four questions in `verdict.md` — the one that
matters most is *did either say something you did not tell it?* That is the
question the counts cannot answer and the whole exercise exists to surface.

Do not show him `comparison.md` before the read if he would rather not see counts
first; ask which he prefers.

## Unseal

Only after `verdict.md` has an answer:

```
python3 scripts/bakeoff.py --unseal bakeoff/chNN
```

The script refuses while the verdict is unfilled. That refusal is the feature.

## Record the result

Append to `FINDINGS.md` in this repo: the chapter, the counted diff, the blind
verdict, and which pipeline it turned out to be. One honest row per chapter. If
the new pipeline lost, write that down in the same detail — a bake-off that only
records wins is decoration.
