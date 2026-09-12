---
description: The Developmental Editor runs the Foundation phase with the author - premise, archetype, voice, audience, outline - for a NEW book, or reports what a book already has. Runs in session, never as a sub-agent. Resumable mid-sequence.
---

# /gw-found — the Foundation phase

Argument: optional `--import` (start from existing drafts/posts), or a book slug.
`$ARGUMENTS`

**Runs as you, in session.** Never dispatch this to a sub-agent. Every artifact
here is a claim about what the author thinks, and a cold desk cannot ask him.

## The write rule, and its one exception

Every other skill in this repo is forbidden from writing inside the book repo.
**This one is the exception, and only for a book nobody else is shipping.**

At Step 0 decide which case you are in, out loud:

| Case | What you may do |
|---|---|
| **New book** | Create `{bookRepo}/books/<slug>/` and author L4 there. The engine owns a book it created from the first file. |
| **Existing book with a complete foundation** | **Write nothing.** Report what exists and stop. Offer `/gw-revise <artifact>`. |
| **Existing book, partial foundation** | Propose the missing artifacts. Do not write them until the author says which pipeline owns this book. |

The Stoic Husband is the second case. Its foundation is locked, the other pipeline
ships it, and a second system authoring its premise is how two sources of truth
start. Say so plainly rather than helpfully producing a file.

## Step 0

```
python3 scripts/resolve_book.py
```

Read `{bookRepo}/book-manifest.json` for the registry and whether this slug exists.
Then state the case before doing anything else.

## The sequence

Each artifact is generated, shown, revised, and only then saved. Do not batch
them: each one constrains the next, and a premise the author has not ratified
makes every downstream artifact wrong in the same direction.

```
00-premise.md     the seed. What the book argues and who it is for.
04-archetype.md   genre profile: arc type, evidence style, chapter format,
                  the QA patterns this genre fails on
01-voice.md       the voice constitution
02-audience.md    the reader map - BOTH reader personas live in this file as
                  sections, plus what the reader already believes, what he is
                  doing wrong, his objections, vocabulary calibration
03-outline.md     the full narrative architecture
```

Resumable: check which files already exist and start at the first missing one. Say
where you are resuming from.

## On the outline, which is the expensive one

It is the highest-leverage artifact in the book and the one the author said took
the most work. Every chapter is researched and drafted from it. Per chapter it
needs: premise, reader takeaway, key points, central story or example, the lesson
or principle, the reader ah-ha, research burden, word-count target, and the
transition to the next chapter.

Group into Parts when there are 15+ chapters. **Do not generate 29 chapters and
present them as done.** Produce the arc and the Part structure first, get a ruling
on that, then fill chapters within the ratified arc.

## `--import`

Existing drafts or posts: read them first and reverse-engineer the foundation from
what is actually there, rather than interviewing for material already written.
Show him what you inferred and what you could not infer. His corrections to the
inferred voice are the most valuable output.

## Gate

The author reviews the outline and says go. That is the highest-leverage review
point in the whole system. Do not proceed past it on implied approval, and do not
summarise his "looks good" into a ratification he did not give.

## Then

`/gw-interview 1` for the first chapter. Record the foundation in the manifest and
say which pipeline owns this book from here.
