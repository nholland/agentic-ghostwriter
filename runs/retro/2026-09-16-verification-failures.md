# Archivist Review — 2026-09-16 — the verification failures

Scope: since `runs/retro/2026-09-16-ch12-second-half.md`. PROPOSALS ONLY (Rule 17).
Ran cold, without the Publisher's findings. Ch12 rewrite in flight, not waited on.

**One shape covers the session: a true measurement stated wider than it covers.**
Five instances, three the Publisher's, two a desk's. Rule 12 covers a check that
*did not run*. None of these failed that way — each ran, against a proxy for the
thing.

| Call | What was actually measured |
|---|---|
| "PubMed is reachable" | `status=203, size=5565` — a proof-of-work challenge page. True of the status line, false of the content. |
| "The plate margins are clean," **twice** | Liberation Serif, where the renderer falls back ~40–50% wider; and page margins only, never whether two strings touch. The author photographed the collision. |
| "You now have Bash" | `gw-designer.md:5` still reads `tools: Read, Write, Glob`. |
| "Every primary-text host is blocked" | False of Gutenberg (200, 562,123 bytes). Cost the chapter a printed Democritus defect. |
| "Do not build on the five love languages" | True of the matching literature, false of the author's own usage. He reversed it and was right. |

**The two that stayed corrected are the two that left a re-runnable artifact** —
`research-round2.md` §1 and `svgcheck.py`. The three that recurred left nothing
but a sentence in the chat. **A verification with no re-runnable artifact is a
claim, not a check.**

Rule 7 makes the Publisher the reviewer of every desk's counted work and names
nothing that reviews the Publisher. That is a scope question for the author.

---

## The register was wrong and every gate was green

The author's note — *"light and loving oriented. This is the SUN!"* — is the
session's most consequential edit. **No desk raised it across seven runs.**

`parts/part-3-warm-sun.md` opens: *"The sun is warm, and it gives that warmth
away. That's the whole of its work. It doesn't wait to feel like it, and it
doesn't wait to be asked."* The chapter's thesis and its register, in the
author's own book, one page before Chapter 12.

**Verified: `grep -rn 'parts/' .claude/ scripts/ CLAUDE.md` returns 0.** Nothing
routes the Part register to any desk. The chapter→Part mapping is mechanical and
already parsed by a book-repo script. The desk that should own this —
`gw-slopreader`, whose remit includes vocabulary drift against the surrounding
arc — reads only `01-voice.md` and is structurally incapable of catching it.

Not a gate failure. A missing input.

## The Designer was pointed at the wrong directory the whole time

`gw-designer.md:17` reads `{bookRoot}/visuals/*.svg` — one deprecated sans plate.
The ratified style is `design/plates/`, nine files. The desk found the conflict
itself and went to the inbox (#015). **It should not have had to.** This is the
root cause of the blank plate, the wrong style question, and the collisions.

---

## Proposals, ranked

**S1 — two tokens, net zero words.** `gw-designer.md`: add `Bash` to line 5;
repoint line 17 from `{bookRoot}/visuals/*.svg` to `{bookRoot}/design/plates/*.svg`.
*Replaces* a path resolving to one deprecated file. Makes "you now have Bash" true.

**S2 — promote `svgcheck.py` to `scripts/svg_check.py` with a caller.** Three
defects as committed: it lives in an output tree, it has no caller, and it
imports its sibling from a session-scoped temp dir. It is a **proven** check —
against the three historical `ch01-distillation.svg` revisions it flags both
defective ones and passes only the fixed one. Add the blank-render test the
Archivist drafted and executed; it flags **all nine** book plates as invisible
standalone. **Deletes** the prose in `gw-designer.md` a script now enforces.

**S3 — `voice_rules_check.py` must compare the number, not just find the phrase.**
Proven by execution: with `value` mutated 3→5 and `01-voice.md` still reading
"~3 mentions", it prints `[ok] metaphor_family_max_per_1000 = 5` and exits 0.
The check built against two sources of truth has that drift inside it.
**Apply before the metaphor-cap amendment, not after.**

**S4 — `scripts/fetch_source.py`, carried from 2026-09-16 second-half, still
unbuilt.** The PubMed error now defines its contract: **assert retrieved content,
never a status line.** Regression cases: PubMed at 203/5,565 bytes must exit
non-zero; Gutenberg #15877 at 200/562,123 must exit 0 and print `Translator:`.

**S5 — open item, names no deletion.** Route the Part register to the desks.
Free half-measure: add `parts/` to `resolve_book.py`'s optional files so it at
least prints at session start. Makes it visible; does not route it.

**S6 — open item.** Nothing reviews the Publisher. Scope question for the author.

**S7 — `GAPS.md`:** compile, and standalone plate rendering.

## What held

Rule 8: book repo `git status` clean, `visuals/ch01-distillation.svg` untouched.
Three cold desks wrote to the inbox rather than deciding. Round-2 research
retracted its own generalisation in writing and tested the map instead of
assuming it. The Designer's #015 is the session's best desk work: it verified
nine-against-one, named the greyscale print failure, and refused to write the
style file.

## Recurrences, unfixed, stated once

`citations.py --chapter 12` reports 1 against 22. `okf_gate.py` blind to `runs/`.
`next.py` still says `-> /gw-compile 12` with 8 rulings unapplied.
`session-start-sha` re-anchored again, mid-arc.
