---
description: Show what is waiting on the author and take his answers, closing each item with the ruling recorded. Use when he wants to clear decisions the cold desks could not make.
---

<!-- DERIVED FILE - DO NOT EDIT.
     Canonical copy: .claude/skills/gw-inbox/SKILL.md
     Regenerate: python3 scripts/sync_plugin_layout.py -->
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

Where an item has a recommendation, give it. He asked for a house, not a queue of
open questions.

## Closing

Only after he has actually ruled:

```
python3 scripts/inbox.py --close N --resolution "what he decided, in his words"
```

Record **his** wording, not your summary of it. The next reader needs to know what
was decided and why, not that something was.

## What this command must not do

- Close an item he did not rule on.
- Decide an item on his behalf because it seems obvious. If it were obvious the
  desk would not have raised it — and a desk that raises obvious items is a
  separate finding worth recording.
- Invent an item's context from the conversation rather than the file.
