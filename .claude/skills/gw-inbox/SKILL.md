---
description: Show what is waiting on the author and take his answers, closing each item with the ruling recorded. Use when he wants to clear decisions the cold desks could not make.
---

# /gw-inbox — the exceptions queue

Argument: optional item number, or `--all`. `$ARGUMENTS`

```
python3 scripts/inbox.py          # or --all for resolved too
```

## Presenting an item

Read the item's full file from `inbox/`. Give him, in this order: the question in
one line, the context he needs to answer **without scrolling back**, and what
specifically unblocks it. If an item lacks that context, say so — and treat the
gap as a defect in the desk that raised it, not as a reason to ask him to
reconstruct it.

**A ruling whose change has not landed yet closes with `--applied-by`.** Pass a
command that exits 0 only once the change is real - a fixture in `tests/run.py`
for a check, a grep against the file for a text change. The item becomes `ruled`
and closes itself when that passes; a ruling recorded is not a ruling applied.

## Closing

Only after he has actually ruled:

```
python3 scripts/inbox.py --close N --resolution "what he decided, in his words"
# add --applied-by "<command>" when the change has not landed yet
```

Record **his** wording, not your summary of it. The next reader needs to know what
was decided and why, not that something was.

## What this command must not do

- Close an item he did not rule on.
- Decide an item on his behalf because it seems obvious. If it were obvious the
  desk would not have raised it — and a desk that raises obvious items is a
  separate finding worth recording.
- Invent an item's context from the conversation rather than the file.
