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
        status: open            # open | ruled | resolved
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
import subprocess
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
        # The proof command for a ruling whose action lives outside this repo.
        # Surfaced as a top-level key because reconcile() reads it on every run;
        # leaving it buried in frontmatter is how a check silently sees nothing.
        "applied_by": fm.get("applied_by", ""),
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
    # gw-retro's own brief ends every proposal with a --applied-by command (its
    # own rule: "a proof that cannot be re-run is a comment"). 8 of the first 18
    # gw-retro items landed with no proof command anyway, because --applied-by
    # passed here was silently dropped (only --close ever wrote it) and nothing
    # forced the desk - or the Publisher relaying it - to notice. Enforced only
    # for gw-retro: other desks raise items with no outside-repo action to prove.
    if (a.raised_by or "").lower().startswith("gw-retro") and not a.applied_by:
        print("inbox: refusing to open a gw-retro item without --applied-by.")
        print("  Your own brief's convention ends every proposal with one - a proof")
        print("  that cannot be re-run is a comment. If the proposal adds or fixes a")
        print("  check, point it at tests/run.py, never a grep for the fix's own text.")
        return 2
    # A proof command that was never run red first is not a proof - it is an
    # assertion that happens to say "checked". #039 closed on exactly this
    # twice inside one hour: its own fixture case was renamed to describe the
    # defect it was meant to catch without ever being run against the buggy
    # code, so it passed both the pre-fix and post-fix trees identically. Any
    # gw-retro item whose --applied-by touches tests/run.py must show a
    # `[FAIL]` line in --evidence, proving someone actually watched it fail
    # before trusting it to pass.
    if ((a.raised_by or "").lower().startswith("gw-retro") and "tests/run.py" in a.applied_by
            and "[FAIL]" not in a.evidence):
        print("inbox: refusing - --applied-by names tests/run.py but --evidence has no [FAIL] line.")
        print("  A case that has never failed has never been proved to discriminate.")
        print("  Run it against the pre-fix code first, paste the [FAIL] line, then the [ ok ].")
        return 2
    os.makedirs(INBOX, exist_ok=True)
    nid = next_id(items)
    slug = re.sub(r"[^a-z0-9]+", "-", a.add.lower()).strip("-")[:48] or "item"
    path = os.path.join(INBOX, f"{nid}-{slug}.md")
    applied_line = f"applied_by: {a.applied_by}\n" if a.applied_by else ""
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"---\nid: {nid}\nstatus: open\n"
                 f"raised_by: {a.raised_by or '?'}\nchapter: {a.chapter or '-'}\n"
                 f"opened: {now()}\n{applied_line}---\n\n# {a.add}\n\n"
                 f"{a.context}\n\n"
                 f"**Recommendation:** {a.recommend}\n\n"
                 f"**Checked:**\n\n```\n{a.evidence}\n```\n\n"
                 f"**What unblocks this:** {a.unblocks}\n")
    print(f"inbox: opened #{nid} -> {os.path.relpath(path, REPO)}")
    return 0


def applied(cmd):
    """Run the proof command. Exit 0 means the ruling actually landed.

    Read-only by construction: a proof command looks and declines to call a
    thing done. It never makes the change it is checking for.
    """
    try:
        r = subprocess.run(cmd, shell=True, cwd=REPO, timeout=120,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return r.returncode == 0
    except Exception:
        return False


def reconcile(items):
    """Flip any 'ruled' item to 'resolved' once its proof command passes.

    Called on every listing, so the reconciliation happens wherever the author
    already looks rather than somewhere he has to remember to go.
    """
    flipped = []
    for it in items:
        if it["status"] != "ruled" or not it.get("applied_by"):
            continue
        if applied(it["applied_by"]):
            with open(it["path"], encoding="utf-8") as fh:
                text = fh.read()
            text = re.sub(r"^status:\s*ruled\s*$", "status: resolved",
                          text, count=1, flags=re.MULTILINE)
            text = text.rstrip() + (
                f"\n\n**Applied, confirmed {now()}:** `{it['applied_by']}` now exits 0.\n")
            with open(it["path"], "w", encoding="utf-8") as fh:
                fh.write(text)
            it["status"] = "resolved"
            flipped.append(it)
    return flipped


def do_close(a, items):
    target = f"{int(a.close):03d}"
    for it in items:
        if it.get("id") == target:
            # --close with no --applied-by falls back to whatever the item's own
            # frontmatter already carries (written by --add, per gw-retro's
            # convention) rather than silently dropping it - closing #033 and
            # #034 this way was the exact miss that made "8 of 18 gw-retro items
            # have no proof command" true.
            applied_by = a.applied_by or it.get("applied_by", "")
            with open(it["path"], encoding="utf-8") as fh:
                text = fh.read()
            # A ruling whose action lives outside this repo is RULED, not
            # resolved, until the command that proves it exits 0. On 2026-09-14
            # three items closed as resolved with their rulings recorded and
            # never applied; inbox.py reported "nothing waiting on the author"
            # while okf_gate.py was still red. "Resolved" has to mean the thing
            # is true, not that he said something.
            done = "resolved" if not applied_by else "ruled"
            text = re.sub(r"^status:\s*open\s*$", f"status: {done}",
                          text, count=1, flags=re.MULTILINE)
            if "resolved:" not in text:
                text = text.replace("---\n\n", f"resolved: {now()}\n---\n\n", 1)
            if applied_by:
                if re.search(r"^applied_by:.*$", text, flags=re.MULTILINE):
                    text = re.sub(r"^applied_by:.*$", f"applied_by: {applied_by}",
                                  text, count=1, flags=re.MULTILINE)
                else:
                    text = text.replace("---\n\n", f"applied_by: {applied_by}\n---\n\n", 1)
            text = text.rstrip() + f"\n\n**Resolution ({now()}):** {a.resolution or '_not recorded_'}\n"
            if applied_by:
                text += (f"\n**Not applied yet.** This ruling lands outside this repo. "
                         f"It closes when `{applied_by}` exits 0.\n")
            with open(it["path"], "w", encoding="utf-8") as fh:
                fh.write(text)

            if applied_by:
                it["status"], it["applied_by"] = "ruled", applied_by
                if applied(applied_by):
                    reconcile([it])
                    print(f"inbox: closed #{target} - {it['title']}")
                    print(f"  confirmed applied: `{applied_by}` exits 0.")
                else:
                    print(f"inbox: #{target} RULED, not yet applied - {it['title']}")
                    print(f"  your ruling is recorded. `{applied_by}` still fails,")
                    print("  so the item stays visible until the change actually lands.")
            else:
                print(f"inbox: closed #{target} - {it['title']}")
                print("  note: closed without a proof command, so nothing checked that")
                print("        the ruling reached the world. Use --applied-by for a")
                print("        ruling whose action lives outside this repo.")
            if not a.resolution:
                print("  warning: no resolution text recorded. The next reader will")
                print("           not know what was decided, only that it was.")
            return 0
    print(f"inbox: no item #{target}", file=sys.stderr)
    return 1


def render(items, show_all):
    open_items = [i for i in items if i["status"] == "open"]
    ruled = [i for i in items if i["status"] == "ruled"]
    shown = items if show_all else (open_items + ruled)
    if not shown:
        return ("inbox: nothing waiting on the author."
                if not show_all else "inbox: empty.")
    head = f"inbox: {len(open_items)} open"
    if ruled:
        head += f", {len(ruled)} ruled but not yet applied"
    if show_all:
        head += f", {len([i for i in items if i['status'] == 'resolved'])} resolved"
    L = [head]
    L.append("")
    for i in shown:
        if i["malformed"]:
            L.append(f"  [!] {os.path.basename(i['path'])} - malformed frontmatter")
            continue
        flag = {"open": "open", "ruled": "RULED"}.get(i["status"], "done")
        L.append(f"  #{i['id']} [{flag}] ch{i['chapter']}  {i['title']}")
        L.append(f"        raised by {i['raised_by']} at {i['opened']}")
        if i["status"] == "ruled":
            L.append("        You ruled on this. The change has not landed yet.")
            L.append(f"        Closes on its own when: {i.get('applied_by', '(no command recorded)')}")
        for line in i["body"].split("\n"):
            if line.strip().startswith("**What unblocks this:**"):
                L.append(f"        {line.strip()}")
    L.append("")
    L.append("  Full text: inbox/*.md   Close: scripts/inbox.py --close N --resolution '...'")
    if ruled:
        L.append("  A RULED item is your decision waiting on a change that has not landed")
        L.append("  yet. It closes itself once its proof command passes.")
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
    ap.add_argument("--applied-by", default="", metavar="COMMAND",
                    help="shell command that exits 0 only once this ruling has "
                         "actually landed. Use it whenever the change has not "
                         "landed yet: a recorded ruling is not an applied one.")
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

    # Reconcile before reporting: a ruling that has since landed should not still
    # be listed as waiting, and the author should not have to run anything to
    # find that out. This reads; a proof command never makes the change it checks for.
    for it in reconcile(items):
        print(f"inbox: #{it['id']} is now applied - closing it. ({it['title']})")

    # --chapter on a read call filters. Before this, --chapter was accepted,
    # exited 0, and printed every item under a header claiming the whole
    # inbox's counts - a desk (or the Publisher, writing FINDINGS.md by hand)
    # asking "what did chapter 12 raise" got a plausible answer covering all
    # 30 items, no error. That silent miss produced three disagreeing counts
    # for Chapter 12 in one commit (19, 11, 12) before this filter existed.
    if a.chapter:
        items = [i for i in items if i["chapter"] == a.chapter]

    if a.json:
        print(json.dumps({"open": [i for i in items if i["status"] == "open"],
                          "ruled": [i for i in items if i["status"] == "ruled"],
                          "resolved": [i for i in items if i["status"] == "resolved"]},
                         indent=2, default=str))
        return 0
    print(render(items, a.all))
    return 0


if __name__ == "__main__":
    sys.exit(main())
