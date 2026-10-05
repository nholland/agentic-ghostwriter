---
name: gw-inbox
description: The one inbox. Shows everything he might need to act on, in three categories (decisions, parked questions, capability gaps), and takes his answers. Use for "show me the inbox", "what's in the inbox", "let's work the inbox", "what's waiting on me", "what do I need to do".
---

<!-- DERIVED FILE - DO NOT EDIT.
     Canonical copy: .claude/skills/gw-inbox/SKILL.md
     Regenerate: python3 scripts/sync_plugin_layout.py -->
# /gw-inbox — the exceptions queue

Argument: optional item number, or `--all`. `$ARGUMENTS`

```
python3 scripts/inbox.py          # everything, by category; --all adds resolved
python3 scripts/inbox.py --kind parked    # one category
```

**"Show me" means write it in the reply.** Terminal output from a script is not
reliably visible to him, and he reads these replies on a phone. After running the
script, post the inbox **in the reply text itself**, formatted to read on a phone:
a short heading per category, one line per item with its number, what it is, and
what he would do about it (decisions) or what brings it back (parked, gaps). End
with **Your next move**: `next.py`'s `NEXT_ACTION` in plain words (for example,
"Chapter 14 is at review, waiting on your verdict"), because the inbox must be
everything he has to do and a chapter verdict is not an inbox item. A reply that
says "here is the inbox" and shows nothing has not shown it.

**One inbox, three kinds.** He asked for one place to look, so this shows all of
them, decisions first:

- **Needs your decision:** a cold desk could not answer it. Blocks work. Closes with
  his ruling and an OKF receipt.
- **Parked:** he chose to defer it. Nothing is blocked. Each carries a trigger, the
  event that brings it back.
- **Capability gaps:** something the house cannot do yet, with the trigger that
  should close it. `GAPS.md` is generated from these.

"Show me the inbox" means print the whole list and summarise it in a few lines:
how many need him, what is ruled but not landed, and the parked and gap counts.
"Work the inbox" means walk it, below.

## Working the inbox

Take **decisions first**, easiest first, each with your one recommendation. Then
offer the parked items **whose trigger has fired** (check each trigger against the
book's current state; do not guess). Do not walk all of the parked and gap items
unless he asks; name how many remain and move on. For a parked or gap item, the
only questions are: is the trigger still right, has it fired, or should it close?
Closing needs only his word:

```
python3 scripts/inbox.py --close N --resolution "his words"     # parked or gap: no receipt
```

To park something new: `python3 scripts/inbox.py --add "title" --kind parked
--trigger "the event, never a date" --context "what it is, in his words"`. To
register a gap, `--kind gap`. After any gap change, `python3 scripts/gaps_md.py`.

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

## Closing a decision

Only after he has actually ruled:

```
python3 scripts/inbox.py --close N --okf-receipt runs/reconciliation/BATCH.json --resolution "what he decided, in his words"
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

## Knowledge completion

Before handoff or completion, follow the reconciliation procedure in `.claude/OKF.md`.
Reconcile durable knowledge, record the receipt and report its disposition.
Author-approved facts need no repeated approval; unapproved interpretations remain proposals.
