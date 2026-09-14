#!/usr/bin/env python3
"""
inbox.py - the exceptions inbox: everything waiting on the author, in one place.

WHY THIS EXISTS
    The two-touch design (the interview and the verdict) only works if everything
    a cold desk could not decide reliably reaches the author. Sub-agents cannot
    ask him anything, so without a collection point a desk either blocks the
    pipeline or resolves the question silently. The book's parking item #28
    recorded the silent version twice before it was settled.

    This is that collection point. If the inbox is weak, the desks quietly make
    decisions that were his to make, and the design fails in the one way that is
    hard to notice.

FORMAT
    Items live as markdown files under inbox/, one per item:

        ---
        id: 004
        status: open            # open | resolved
        raised_by: gw-lineeditor
        chapter: 12
        opened: 2026-09-12 21:04
        ---
        # The question, in one line

        Context the author needs to answer without scrolling back.

        **What unblocks this:** the specific ruling needed.

    A desk that cannot write one of these has not finished its job.

USAGE
    python3 scripts/inbox.py                      # list open items
    python3 scripts/inbox.py --all
    python3 scripts/inbox.py --add "question" --raised-by gw-researcher --chapter 12
    python3 scripts/inbox.py --close 4 --resolution "text"
    python3 scripts/inbox.py --add "question" --recommend "..." --evidence "..." \
                             --context "..." --unblocks "..."   # all four required
    python3 scripts/inbox.py --json
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
INBOX = os.path.join(REPO, "inbox")


def now():
    """Read the clock. Never supply a plausible time - a wrong timestamp passes
    every format check and looks correct forever."""
    try:
        out = subprocess.run(["date", "+%Y-%m-%d %H:%M"], capture_output=True,
                             text=True, check=True).stdout.strip()
        if out:
            return out
    except Exception:
        pass
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


def parse(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        return {"path": path, "malformed": True, "status": "open",
                "id": None, "title": os.path.basename(path), "body": text}
    fm = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    body = m.group(2).strip()
    title = next((l.lstrip("# ").strip() for l in body.split("\n")
                  if l.startswith("#")), body.split("\n")[0][:80])
    return {
        "path": path, "malformed": False,
        "id": fm.get("id"), "status": fm.get("status", "open").lower(),
        "raised_by": fm.get("raised_by", "?"), "chapter": fm.get("chapter", "-"),
        "opened": fm.get("opened", "?"), "resolved": fm.get("resolved"),
        "title": title, "body": body, "frontmatter": fm,
    }


def load_all():
    items = [parse(p) for p in sorted(glob.glob(os.path.join(INBOX, "*.md")))]
    return sorted(items, key=lambda i: (i.get("id") or "999"))


def next_id(items):
    nums = [int(i["id"]) for i in items if i.get("id") and i["id"].isdigit()]
    return f"{(max(nums) + 1) if nums else 1:03d}"


def do_add(a, items):
    """Open an item. Refuses without a recommendation and its evidence.

    On 2026-09-14 the author worked five items in one sitting. All five handed
    him a menu - three opened their unblocks line "Either (a)... or (b)..." -
    and he said so: "You aren't clear on what you recommend, please speak
    plainly." Two of the five also asserted something false, each from a
    filename and a header rather than from opening the file.

    A desk that cannot commit to one recommendation has not finished thinking,
    and a recommendation with no command behind it is an impression. Both are
    required here rather than urged in a skill file, because the soft version
    of this rule was already written down and was skipped five times out of
    five.
    """
    missing = [n for n, v in (("--recommend", a.recommend), ("--evidence", a.evidence),
                              ("--context", a.context), ("--unblocks", a.unblocks)) if not v]
    if missing:
        print(f"inbox: refusing to open an item without {', '.join(missing)}.")
        print("  --recommend  one recommendation, not a menu. Name the option you would take.")
        print("  --evidence   the command you ran and what it printed. Rule 5: counted, never estimated.")
        print("  --context    what he needs to rule cold, without scrolling back.")
        print("  --unblocks   the specific ruling this waits on.")
        return 2
    os.makedirs(INBOX, exist_ok=True)
    nid = next_id(items)
    slug = re.sub(r"[^a-z0-9]+", "-", a.add.lower()).strip("-")[:48] or "item"
    path = os.path.join(INBOX, f"{nid}-{slug}.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"---\nid: {nid}\nstatus: open\n"
                 f"raised_by: {a.raised_by or '?'}\nchapter: {a.chapter or '-'}\n"
                 f"opened: {now()}\n---\n\n# {a.add}\n\n"
                 f"{a.context}\n\n"
                 f"**Recommendation:** {a.recommend}\n\n"
                 f"**Checked:**\n\n```\n{a.evidence}\n```\n\n"
                 f"**What unblocks this:** {a.unblocks}\n")
    print(f"inbox: opened #{nid} -> {os.path.relpath(path, REPO)}")
    return 0


def do_close(a, items):
    target = f"{int(a.close):03d}"
    for it in items:
        if it.get("id") == target:
            with open(it["path"], encoding="utf-8") as fh:
                text = fh.read()
            text = re.sub(r"^status:\s*open\s*$", "status: resolved",
                          text, count=1, flags=re.MULTILINE)
            if "resolved:" not in text:
                text = text.replace("---\n\n", f"resolved: {now()}\n---\n\n", 1)
            text = text.rstrip() + f"\n\n**Resolution ({now()}):** {a.resolution or '_not recorded_'}\n"
            with open(it["path"], "w", encoding="utf-8") as fh:
                fh.write(text)
            print(f"inbox: closed #{target} - {it['title']}")
            if not a.resolution:
                print("  warning: no resolution text recorded. The next reader will")
                print("           not know what was decided, only that it was.")
            return 0
    print(f"inbox: no item #{target}", file=sys.stderr)
    return 1


def render(items, show_all):
    open_items = [i for i in items if i["status"] == "open"]
    shown = items if show_all else open_items
    if not shown:
        return ("inbox: nothing waiting on the author."
                if not show_all else "inbox: empty.")
    L = [f"inbox: {len(open_items)} open"
         + (f", {len(items) - len(open_items)} resolved" if show_all else "")]
    L.append("")
    for i in shown:
        if i["malformed"]:
            L.append(f"  [!] {os.path.basename(i['path'])} - malformed frontmatter")
            continue
        flag = "open" if i["status"] == "open" else "done"
        L.append(f"  #{i['id']} [{flag}] ch{i['chapter']}  {i['title']}")
        L.append(f"        raised by {i['raised_by']} at {i['opened']}")
        for line in i["body"].split("\n"):
            if line.strip().startswith("**What unblocks this:**"):
                L.append(f"        {line.strip()}")
    L.append("")
    L.append("  Full text: inbox/*.md   Close: scripts/inbox.py --close N --resolution '...'")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="The exceptions inbox.")
    ap.add_argument("--all", action="store_true", help="include resolved items")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--add", metavar="QUESTION")
    ap.add_argument("--context", default="")
    ap.add_argument("--unblocks", default="")
    ap.add_argument("--raised-by", default="")
    ap.add_argument("--chapter", default="")
    ap.add_argument("--recommend", default="",
                    help="required with --add: one recommendation, not a menu.")
    ap.add_argument("--evidence", default="",
                    help="required with --add: the command run and its output, verbatim.")
    ap.add_argument("--close", metavar="N")
    ap.add_argument("--resolution", default="",
                    help="the author's ruling, in his own words. Recorded verbatim "
                         "on the closed item; without it the close warns and the "
                         "next reader learns only that something was decided.")
    a = ap.parse_args()

    items = load_all()
    if a.add:
        return do_add(a, items)
    if a.close:
        return do_close(a, items)
    if a.json:
        print(json.dumps({"open": [i for i in items if i["status"] == "open"],
                          "resolved": [i for i in items if i["status"] != "open"]},
                         indent=2, default=str))
        return 0
    print(render(items, a.all))
    return 0


if __name__ == "__main__":
    sys.exit(main())
