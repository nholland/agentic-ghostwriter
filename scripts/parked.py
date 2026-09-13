#!/usr/bin/env python3
"""
parked.py - questions the author chose to defer, and notes in his own words.

TWO THINGS, KEPT APART
    The INBOX (inbox.py) is what a cold desk needs ruled to keep working.
    PARKED questions are ones the author chose not to decide yet. Nothing is
    blocked on them. They carry a REVISIT TRIGGER - an event the board can
    check ("at the Ch13 interview", "before the first compile of Part III") -
    not a date, because a date on a deferred question is a guess.

    NOTES are decisions already made, kept in the author's words because the
    engine's session log is derived and cannot carry what he actually said.

    The book repo's /book-park had --review and --close; the first version of
    this house had neither, so a parked question was appended to a file nothing
    read again. This closes that.

FORMAT
    runs/parked/NNN-slug.md      one file per question, inbox-style frontmatter
    runs/notes.md                append-only, clock-stamped

USAGE
    python3 scripts/parked.py                                # open parked questions
    python3 scripts/parked.py --all
    python3 scripts/parked.py --add "question" --trigger "at the Ch13 interview" [--context "..."]
    python3 scripts/parked.py --close 3 --resolution "what he decided, in his words"
    python3 scripts/parked.py --note "what he said, verbatim"
    python3 scripts/parked.py --count            # for next.py
    python3 scripts/parked.py --json
"""

import argparse
import datetime
import glob
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
STATE = os.environ.get("GW_STATE_ROOT", REPO)
PARKED = os.path.join(STATE, "runs", "parked")
NOTES = os.path.join(STATE, "runs", "notes.md")


def now():
    try:
        out = subprocess.run(["date", "+%Y-%m-%d %H:%M"], capture_output=True, text=True, check=True).stdout.strip()
        if out:
            return out
    except Exception:
        pass
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


def parse(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        return {"path": path, "malformed": True, "id": None, "status": "open", "title": os.path.basename(path)}
    fm = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    body = m.group(2).strip()
    title = next((l.lstrip("# ").strip() for l in body.split("\n") if l.startswith("#")), body[:80])
    return {"path": path, "malformed": False, "id": fm.get("id"), "status": fm.get("status", "open").lower(),
            "opened": fm.get("opened", "?"), "trigger": fm.get("trigger", "?"), "closed": fm.get("closed"),
            "title": title, "body": body}


def load_all():
    return sorted((parse(p) for p in glob.glob(os.path.join(PARKED, "*.md"))), key=lambda i: i.get("id") or "999")


def next_id(items):
    nums = [int(i["id"]) for i in items if i.get("id") and i["id"].isdigit()]
    return f"{(max(nums) + 1) if nums else 1:03d}"


def do_add(a, items):
    if not a.trigger:
        print("parked: refusing - a parked question needs --trigger, the event that brings it back. "
              "A date is a guess; a trigger is a condition the board can check.")
        return 1
    os.makedirs(PARKED, exist_ok=True)
    nid = next_id(items)
    slug = re.sub(r"[^a-z0-9]+", "-", a.add.lower()).strip("-")[:48] or "question"
    path = os.path.join(PARKED, f"{nid}-{slug}.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"---\nid: {nid}\nstatus: open\nopened: {now()}\ntrigger: {a.trigger}\n---\n\n"
                 f"# {a.add}\n\n{a.context or '_No context recorded._'}\n\n**Revisit when:** {a.trigger}\n")
    print(f"parked: #{nid} -> {os.path.relpath(path, REPO)}  (revisit: {a.trigger})")
    return 0


def do_close(a, items):
    target = f"{int(a.close):03d}"
    for it in items:
        if it.get("id") == target:
            text = open(it["path"], encoding="utf-8").read()
            text = re.sub(r"^status:\s*open\s*$", "status: resolved", text, count=1, flags=re.M)
            if "closed:" not in text:
                text = text.replace("\n---\n\n", f"\nclosed: {now()}\n---\n\n", 1)
            text = text.rstrip() + f"\n\n**Resolution ({now()}):** {a.resolution or '_not recorded_'}\n"
            open(it["path"], "w", encoding="utf-8").write(text)
            print(f"parked: closed #{target} - {it['title']}")
            if not a.resolution:
                print("  warning: no resolution recorded; the next reader learns only that it was decided.")
            return 0
    print(f"parked: no item #{target}", file=sys.stderr)
    return 1


def do_note(text):
    os.makedirs(os.path.dirname(NOTES), exist_ok=True)
    new = not os.path.isfile(NOTES)
    with open(NOTES, "a", encoding="utf-8") as fh:
        if new:
            fh.write("# Notes\n\nThe author's own words, kept because the session log is derived and cannot carry them. "
                     "Never written on a desk's initiative.\n")
        fh.write(f"\n## {now()}\n\n{text.strip()}\n")
    print(f"parked: note appended to runs/notes.md at {now()}")
    return 0


def render(items, show_all):
    open_items = [i for i in items if i["status"] == "open"]
    shown = items if show_all else open_items
    if not shown:
        return "parked: nothing deferred." if not show_all else "parked: empty."
    L = [f"parked: {len(open_items)} open" + (f", {len(items) - len(open_items)} resolved" if show_all else ""), ""]
    for i in shown:
        if i.get("malformed"):
            L.append(f"  [!] {os.path.basename(i['path'])} - malformed"); continue
        L.append(f"  #{i['id']} [{'open' if i['status'] == 'open' else 'done'}]  {i['title']}")
        L.append(f"        revisit when: {i['trigger']}   (parked {i['opened']})")
    L += ["", "  Close: scripts/parked.py --close N --resolution '...'"]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="Parked questions and author notes.")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--count", action="store_true")
    ap.add_argument("--add", metavar="QUESTION")
    ap.add_argument("--trigger", default="")
    ap.add_argument("--context", default="")
    ap.add_argument("--close", metavar="N")
    ap.add_argument("--resolution", default="")
    ap.add_argument("--note", metavar="TEXT")
    a = ap.parse_args()
    items = load_all()
    if a.add:
        return do_add(a, items)
    if a.close:
        return do_close(a, items)
    if a.note:
        return do_note(a.note)
    if a.count:
        print(len([i for i in items if i["status"] == "open"])); return 0
    if a.json:
        print(json.dumps({"open": [i for i in items if i["status"] == "open"],
                          "resolved": [i for i in items if i["status"] != "open"]}, indent=2, default=str)); return 0
    print(render(items, a.all))
    return 0


if __name__ == "__main__":
    sys.exit(main())
