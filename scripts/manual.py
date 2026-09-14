#!/usr/bin/env python3
"""
manual.py - derive the house manual (docs/manual.html) from the house itself.

WHY THIS EXISTS
    On 2026-09-14 four sources disagreed about one fact. `.claude/agents/` held
    ten cold desks; CLAUDE.md said "Nine run cold" above a table of ten; README.md
    said "Ten desks" in total; and the published manual said "Twelve". The manual
    also said four inbox items when there were five, and credited a test suite
    that does not exist in this repo. Every one of those numbers was written by
    hand and was right on the day it was typed.

    That is the citation-manifest.md failure and the sweep-report.md failure in a
    third costume, and CLAUDE.md Rule 15 already names the fix: an artifact either
    carries its coverage or is regenerated wholesale. A manual cannot carry a
    range, so it is regenerated. The roster, the commands, the counted thresholds
    and the production scripts are READ FROM THE HOUSE, never transcribed.

WHY NO "DOCUMENTARIAN" DESK
    Because the author kept having to remind the model to update the README, and
    a desk whose mandate is remembering is the same mechanism that failed. This
    follows the rule CLAUDE.md states for git: every failure there was a model
    following rule text, and every fix was a check that ran on its own. So the
    manual is derived by this script and a --check runs from the Stop hook.
    sync_plugin_layout.py's docstring says it plainly: any file that calls itself
    derived must have a script deriving it, and any check that calls itself
    enforcement must have a caller.

WHAT IS AUTHORED AND WHAT IS DERIVED
    Derived (cannot drift): the desk roster and each desk's mandate line and
    tools, the command list and what each one does, the counted voice thresholds
    and their sources, the production scripts and their one-line purposes, and
    every count computed from those.

    Authored (edit NARRATIVE below): the stage walkthrough, the explanation of
    what a gate is for, where things live, and the glossary. Prose that states a
    fact a file already holds belongs in the derived half instead.

WHAT IS DELIBERATELY ABSENT
    Live state. No inbox count, no chapter progress, no "next action". Those are
    stale the moment they are written, which is the whole defect this script
    exists to end, and `/gw` reports them from the oracle on demand. The page
    says "run /gw" and means it.

USAGE
    python3 scripts/manual.py            # derive docs/manual.html
    python3 scripts/manual.py --check    # exit 1 if the house changed since

EXIT CODES
    0  written, or --check found no drift
    1  --check found drift: regenerate and republish
"""

import argparse
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
AGENTS = os.path.join(REPO, ".claude", "agents")
SKILLS = os.path.join(REPO, ".claude", "skills")
SCRIPTS = os.path.join(REPO, "scripts")
CONFIG = os.path.join(REPO, "config", "house.json")
OUT = os.path.join(REPO, "docs", "manual.html")

sys.path.insert(0, HERE)
from manual_content import IN_SESSION, DESK_NOTES, GATES, PHRASES  # noqa: E402


# ---------------------------------------------------------------------------
# AUTHORED HALF. Prose only. If you are about to write a number or a name here,
# it belongs in the derived half instead.
# ---------------------------------------------------------------------------
NARRATIVE = {
    "thesis": "You say what the chapter is, and whether it landed. "
              "The house does everything in between, and asks you only what only you can answer.",
    "lede": "A book production house that runs on Claude Code. You are the expert the house "
            "recruited. You talk to the Publisher; the Publisher runs the desks. Every desk is "
            "either someone in the room with you, a cold sub-agent that never saw the "
            "conversation, or a script that cannot be talked past.",
    "start": [
        ("Open a session on the engine repo",
         "Pick <b>agentic-ghostwriter</b> as the repository. The start hook prints the real "
         "clock, the book it resolved, and the board."),
        ("The book repo gets attached",
         "A cloud session clones one repository, and the house needs two: this engine, and the "
         "book it reads. If the book is not on disk, <code>resolve_book.py</code> stops "
         "everything and says so. Attaching it takes seconds and the Publisher does it."),
        ("Say <code>/gw</code>",
         "One door. On its own it shows what is next and what is waiting on you. With words "
         "after it, the Publisher reads what you mean. Nothing here needs remembering: when a "
         "phrase matters, the menu says it at that moment."),
    ],
    "stages": [
        {"name": "The interview", "who": "author", "desk": "The Developmental Editor, in session",
         "cmd": "/gw-interview N",
         "what": "The chapter's ideas come from you here or they do not exist. The Editor opens "
                 "with what the outline already commits the chapter to, so you react to something "
                 "concrete, then works the gaps: the memory behind the story slot, where your own "
                 "experience contradicts the premise, what you believe that you have not seen "
                 "written anywhere. It pushes back once on anything that sounds received rather "
                 "than yours. Your corrections are the product.",
         "gate": "None. Your sign-off that the record is complete is the gate."},
        {"name": "The brief", "who": "cold", "desk": "The Researcher", "cmd": "/gw-research N",
         "what": "The automation boundary. Everything upstream of a good brief needs you; "
                 "everything downstream can run cold. The Researcher reads your interview record "
                 "and the book's own files, and writes gap markers for claims nobody has sourced.",
         "gate": "The Ghostwriter reads it in plan-only mode and answers one question: could "
                 "someone who never read the interview write this chapter from this file alone?"},
        {"name": "The draft", "who": "cold", "desk": "The Ghostwriter", "cmd": "/gw-draft N",
         "what": "A complete chapter, written cold from the brief. It ends in Draft Notes that "
                 "declare the anchor metaphor, every placeholder, and any outline row it could "
                 "not satisfy. It never pauses to check in.",
         "gate": "The counted voice script, pasted verbatim, then the Conformance Checker, which "
                 "is shown only the outline section and the prose so it cannot be persuaded by "
                 "the reasons behind a substitution."},
        {"name": "The refine", "who": "cold", "desk": "The Line Editor, then the Anti-Slop Reader",
         "cmd": "/gw-refine N",
         "what": "Refinement passes into finished prose, plus the distillation the compile reads. "
                 "The Anti-Slop Reader then judges the half no script can count: invented foils, "
                 "scenes watched from outside, a term relabelled between chapters.",
         "gate": "The voice script again, run by the Publisher independently of what the editor "
                 "reported. A discrepancy between the two is itself a finding."},
        {"name": "The plate", "who": "cold", "desk": "The Designer", "cmd": "part of /gw-chapter",
         "what": "One diagram per chapter, drawn in the book's established visual style from the "
                 "distillation's mechanism and the declared anchor metaphor. It reuses the house "
                 "marks rather than redrawing them, and introduces no content of its own.",
         "gate": "The prose rules apply to the labels. Never blocks a chapter."},
        {"name": "The package", "who": "script", "desk": "Production", "cmd": "/gw-compile N",
         "what": "The chapter as a reader meets it, through the book repo's one renderer. There "
                 "is one renderer because its predecessor was two copies of a stylesheet that "
                 "shipped the same two defects and had only one fixed.",
         "gate": "The citation gate runs before anything is assembled: a manuscript is the one "
                 "artifact that leaves the building."},
        {"name": "The verdict", "who": "author", "desk": "You", "cmd": "read the package",
         "what": "You come back to the PDF, the plate, the counts as the scripts printed them, "
                 "the conformance rows, and the inbox. You say whether it landed. If you want a "
                 "line changed, <code>/gw-edit N</code> walks the chapter with you section by "
                 "section and re-runs the counts, because an edit can break a count that passed.",
         "gate": "You are the gate. Only you can say whether it landed."},
    ],
    "gates_intro": "A producer's work is not done until a different reader says so, and that "
                   "reader is a script or another desk, never the producer's own report. "
                   "Self-reported counts were wrong on Chapters 9 and 10 and the Prologue, and "
                   "once hid a live violation. So the counts come from a script and are pasted "
                   "verbatim. A gate that cannot run fails closed: the citation gate blocks when "
                   "it cannot find its validator, and the voice script reports UNCHECKED, which "
                   "is explicitly not a pass.",
    "never": [
        "Invent a citation, a statistic, or a story.",
        "Mark a citation <code>verified</code>. That is yours, against your physical copy.",
        "Let a search transcribe a quotation. Search may locate a source or flag a defect, never quote it.",
        "Write the book's constitution, its chapters, or its manifest.",
        "Resolve a question that was yours. It goes to the inbox instead.",
        "Edit its own rules. The Archivist proposes; you apply.",
        "Move <code>main</code>. Only <code>sync.py --land</code> does that, and only when you say so in words.",
        "Claim a check passed that did not run. SKIP is not PASS, and unchecked is the honest word.",
    ],
    "where": [
        ("The book", "Playground-260420",
         "The premise, voice, audience and outline every desk reads. The knowledge ledger. The "
         "chapters the proven pipeline ships. Read-only to this engine, with one exception: the "
         "ledger, written only through the book repo's own validator."),
        ("The engine", "agentic-ghostwriter",
         "The desks, the commands, the gates, the oracle, the inbox, and everything the house "
         "produces under <code>runs/chNN/</code>. Change how books get made here."),
    ],
    "where_rule": "Two repositories, permanently. Book two is a new folder in the book repo, "
                  "never a third repository. When you are editing by hand the question is one "
                  "line: is this about this book, or about how books get made?",
    "glossary": [
        ("Cold", "Running as a sub-agent with clean context. It never saw the conversation, so it "
                 "cannot be persuaded by the reasons behind a choice, and it cannot ask you "
                 "anything, which is why anything only you can decide goes to the inbox."),
        ("The board", "What the state oracle prints. Computed from files, never reasoned about, "
                      "so it cannot be stale. Say <code>/gw</code>."),
        ("The brief", "The research brief. The automation boundary: everything upstream needs "
                      "you, everything downstream runs cold."),
        ("The inbox", "Questions a cold desk could not decide. Each carries the context you need "
                      "to answer it without scrolling back, and what your answer unblocks."),
        ("Gap marker", "A citation concept whose whole content is \"this claim needs a source and "
                       "nobody has found one.\" Written immediately; the file is the flag. A "
                       "content concept, which captures what you think, is shown to you first."),
        ("The ledger", "The book's knowledge bundle. Every citation carries three independent "
                       "axes: its status, whether it is quoted verbatim, and what evidence was "
                       "actually looked at."),
        ("Shadow run", "The house running a chapter's cold stages from a brief the book pipeline "
                       "produced, in parallel, without touching the book."),
        ("The two touches", "The interview and the verdict. The design's whole claim."),
    ],
}


# ---------------------------------------------------------------------------
# DERIVED HALF. Everything below is read from the house.
# ---------------------------------------------------------------------------
def frontmatter(path):
    """Return the YAML-ish frontmatter of a markdown file as a dict.

    Deliberately not a YAML parser: these files use a flat key: value shape and
    a dependency for eight keys would be a dependency to keep current.
    """
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return {}
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    out = {}
    for line in text[3:end].splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip()
    return out


def first_sentence(text):
    """The desk's mandate line: its description up to the first sentence stop."""
    m = re.match(r"(.+?\.)(?:\s|$)", text.strip())
    return m.group(1) if m else text.strip()


def read_desks():
    """Cold desks, from .claude/agents/ frontmatter. The roster, not a copy of it."""
    out = []
    for fn in sorted(os.listdir(AGENTS)) if os.path.isdir(AGENTS) else []:
        if not fn.endswith(".md"):
            continue
        fm = frontmatter(os.path.join(AGENTS, fn))
        name = fm.get("name", fn[:-3])
        desc = fm.get("description", "")
        # The shared "Prefixed gw- so it can never be shadowed" clause is a fact
        # about the file layout, not about the desk. It is stated once, in the
        # note under the roster, rather than eleven times in the cards.
        desc = re.sub(r"\s*Prefixed gw-.*?agent\.\s*", " ", desc).strip()
        note = DESK_NOTES.get(name)
        out.append({
            "name": name,
            # The authored title is the desk's house name ("The Researcher");
            # the frontmatter sentence is the fallback when none is written.
            "title": note["title"] + " \u2014 " + note["owns"] if note
                     else first_sentence(desc).rstrip("."),
            "body": note["body"] if note else
                    (desc[len(first_sentence(desc)):].strip()
                     + "<p><b>No extended mandate is written for this desk yet.</b> "
                       "Add one to scripts/manual_content.py.</p>"),
            "tools": [t.strip() for t in fm.get("tools", "").split(",") if t.strip()],
            "authored": bool(note),
        })
    return out


def roster_drift(desks):
    """Notes for desks that no longer exist, and desks with no note.

    Checked BOTH ways on purpose. A one-way check is how a desk gets deleted and
    its mandate keeps being published.
    """
    on_disk = {d["name"] for d in desks}
    return (sorted(set(DESK_NOTES) - on_disk), sorted(d["name"] for d in desks if not d["authored"]))


def read_commands():
    """Commands, from .claude/skills/*/SKILL.md frontmatter."""
    out = []
    for d in sorted(os.listdir(SKILLS)) if os.path.isdir(SKILLS) else []:
        p = os.path.join(SKILLS, d, "SKILL.md")
        if not os.path.isfile(p):
            continue
        desc = frontmatter(p).get("description", "")
        out.append({"name": "/" + d, "title": first_sentence(desc).rstrip("."),
                    "body": desc[len(first_sentence(desc)):].strip()})
    return out


def read_scripts():
    """Production scripts, from the first line of each module docstring."""
    out = []
    for fn in sorted(os.listdir(SCRIPTS)):
        if not fn.endswith(".py") or fn.startswith("_"):
            continue
        purpose = ""
        try:
            with open(os.path.join(SCRIPTS, fn), encoding="utf-8") as fh:
                body = fh.read(4000)
            m = re.search(r'"""\s*(.+)', body)
            if m:
                purpose = m.group(1).strip()
                purpose = re.sub(r"^" + re.escape(fn) + r"\s*-\s*", "", purpose)
        except OSError:
            pass
        out.append({"name": fn, "purpose": purpose})
    return out


def read_thresholds():
    """The counted voice rules, from config/house.json - the same file the script enforces."""
    try:
        with open(CONFIG, encoding="utf-8") as fh:
            cfg = json.load(fh)
    except (OSError, ValueError):
        return []
    out = []
    for key, rule in cfg.get("voice_rules", {}).items():
        if key.startswith("_") or not isinstance(rule, dict) or "value" not in rule:
            continue
        out.append({"key": key, "value": rule["value"],
                    "source": rule.get("source", ""), "note": rule.get("note", "")})
    return out


def phantom_references(commands):
    """Every script and command the AUTHORED half names must exist on disk.

    Two gate rows published on 2026-09-14 named term_check.py and okf_new.py as
    gates. Neither exists in either repo. They were extracted programmatically
    from the previous page rather than retyped, and were therefore trusted:
    provenance is not verification. This is the same shape as house.json's
    spec_probe, which asserts a threshold still matches the spec it claims to
    come from, and the same fix - the claim is checked against the thing.
    """
    blob = json.dumps([GATES, PHRASES, NARRATIVE, DESK_NOTES], default=str)
    known_cmds = {c["name"] for c in commands}
    try:
        with open(CONFIG, encoding="utf-8") as fh:
            deps = json.load(fh).get("book_repo_dependencies", {})
        book = {os.path.basename(k) for grp in ("required", "optional")
                for k in deps.get(grp, {})}
    except (OSError, ValueError):
        book = set()

    missing = []
    for name in sorted(set(re.findall(r"\b([a-z_]+\.py)\b", blob))):
        if not os.path.isfile(os.path.join(SCRIPTS, name)) and name not in book:
            missing.append(name)
    for cmd in sorted(set(re.findall(r"(/gw[a-z-]*)", blob))):
        if cmd not in known_cmds:
            missing.append(cmd)
    return missing


def inputs_digest(desks, commands, scripts, thresholds):
    """Hash of everything derived, plus this file. --check compares against it.

    Live state is excluded by construction: nothing above reads the inbox or the
    chapter board, so a new inbox item does not make the manual stale.
    """
    h = hashlib.sha256()
    h.update(json.dumps([desks, commands, scripts, thresholds, IN_SESSION,
                         DESK_NOTES, GATES, PHRASES, NARRATIVE],
                        sort_keys=True, default=str).encode())
    try:
        with open(os.path.join(HERE, "manual_content.py"), "rb") as fh:
            h.update(fh.read())
    except OSError:
        pass
    try:
        with open(os.path.abspath(__file__), "rb") as fh:
            h.update(fh.read())
    except OSError:
        pass
    return h.hexdigest()[:16]


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------
def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def esc_attr(s):
    return esc(s).replace('"', "&quot;")


CSS = """
:root{
  --paper:#fbfaf7; --paper-2:#f2f0ea; --ink:#17151a; --ink-2:#4a4750; --ink-3:#7b7884;
  --rule:#dcd9d1; --pencil:#2f5fa8; --pencil-soft:#e4ebf7; --author:#b8412f;
  --author-soft:#f7e6e2; --graphite:#5f6470; --graphite-soft:#e9eaee; --code-bg:#f1efe9;
  --display:'Fraunces',Georgia,'Times New Roman',serif;
  --body:'Public Sans',-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
  --mono:'IBM Plex Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --paper:#14161a; --paper-2:#1c1f25; --ink:#ece9e2; --ink-2:#bdb8ae; --ink-3:#8a8780;
  --rule:#2c3038; --pencil:#7ea3e6; --pencil-soft:#1d2a40; --author:#e07a66;
  --author-soft:#3a221d; --graphite:#a2a7b3; --graphite-soft:#252930; --code-bg:#1c1f25;
}}
:root[data-theme="dark"]{
  --paper:#14161a; --paper-2:#1c1f25; --ink:#ece9e2; --ink-2:#bdb8ae; --ink-3:#8a8780;
  --rule:#2c3038; --pencil:#7ea3e6; --pencil-soft:#1d2a40; --author:#e07a66;
  --author-soft:#3a221d; --graphite:#a2a7b3; --graphite-soft:#252930; --code-bg:#1c1f25;
}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--body);
  font-size:16px;line-height:1.55;-webkit-font-smoothing:antialiased}
a{color:var(--pencil);text-underline-offset:2px}
a:focus-visible,button:focus-visible,input:focus-visible,summary:focus-visible{
  outline:2px solid var(--pencil);outline-offset:2px;border-radius:3px}
code{font-family:var(--mono);font-size:.88em;background:var(--code-bg);padding:.1em .35em;border-radius:3px}
h1,h2,h3{font-family:var(--display);font-weight:600;line-height:1.12;margin:0;letter-spacing:-.01em;text-wrap:balance}
h1{font-size:clamp(2.1rem,7vw,4rem)}
h2{font-size:clamp(1.5rem,4.5vw,2.1rem);margin-bottom:.35em}
h3{font-size:1.15rem;margin:1.5rem 0 .4rem}
p{margin:0 0 1em;max-width:68ch}
ul,ol{max-width:68ch;padding-left:1.25em;margin:0 0 1em}
li{margin-bottom:.35em}
.eyebrow{font-size:.72rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;
  color:var(--ink-3);margin-bottom:.55rem}
.lede{font-size:1.1rem;color:var(--ink-2);max-width:62ch}
.wrap{max-width:1140px;margin:0 auto;padding:2rem 20px 4rem}
@media (min-width:940px){
  .wrap{display:grid;grid-template-columns:210px minmax(0,1fr);gap:3rem;padding-top:2.5rem}
  nav.toc{position:sticky;top:1.5rem;align-self:start}
}
nav.toc ol{list-style:none;padding:0;margin:0;font-size:.9rem}
@media (min-width:940px){nav.toc ol{border-left:1px solid var(--rule)}}
nav.toc li{margin:0}
nav.toc a{display:block;padding:.3rem .75rem;color:var(--ink-2);text-decoration:none;
  border-left:2px solid transparent;margin-left:-1px}
nav.toc a.active{color:var(--pencil);border-left-color:var(--pencil)}
@media (max-width:939px){
  nav.toc{margin-bottom:1.5rem;overflow-x:auto;-webkit-overflow-scrolling:touch}
  nav.toc ol{display:flex;gap:.4rem;white-space:nowrap;padding-bottom:.3rem}
  nav.toc a{border:1px solid var(--rule);border-radius:999px;padding:.35rem .8rem}
  nav.toc a.active{background:var(--ink);color:var(--paper);border-color:var(--ink)}
}
section{padding-block:2.2rem;border-top:1px solid var(--rule);scroll-margin-top:1rem}
section:first-of-type{border-top:0;padding-top:0}
header.mast{padding-bottom:2rem}
.thesis{font-family:var(--display);font-size:clamp(1.15rem,3.4vw,1.5rem);font-weight:400;
  color:var(--ink-2);max-width:30ch;line-height:1.3;margin:.9rem 0 1.5rem}
.keys{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:.9rem;
  border-block:1px solid var(--rule);padding-block:1rem;max-width:760px}
.keys b{display:block;font-family:var(--display);font-size:1.6rem;line-height:1;margin-bottom:.25rem;
  font-variant-numeric:tabular-nums}
.keys span{font-size:.8rem;color:var(--ink-3)}
.who{display:inline-flex;align-items:center;gap:.4em;font-size:.68rem;font-weight:600;
  letter-spacing:.08em;text-transform:uppercase;padding:.18em .55em;border-radius:3px;white-space:nowrap}
.who::before{content:"";width:.5em;height:.5em;border-radius:50%;background:currentColor}
.who.author{color:var(--author);background:var(--author-soft)}
.who.cold{color:var(--pencil);background:var(--pencil-soft)}
.who.script{color:var(--graphite);background:var(--graphite-soft)}
.legend{display:flex;flex-wrap:wrap;gap:.5rem .9rem;margin:.3rem 0 1.3rem;font-size:.88rem;
  color:var(--ink-2);align-items:center}
.start{list-style:none;padding:0;margin:1rem 0 0;counter-reset:s}
.start li{counter-increment:s;display:grid;grid-template-columns:2rem 1fr;gap:.9rem;
  padding:.8rem 0;border-top:1px solid var(--rule)}
.start li::before{content:counter(s);font-family:var(--mono);font-size:.85rem;color:var(--ink-3);
  border:1px solid var(--rule);border-radius:50%;width:2rem;height:2rem;display:grid;place-items:center}
.start b{display:block;margin-bottom:.2rem}
.start p{margin:0;font-size:.95rem;color:var(--ink-2)}
.stagebar{display:flex;gap:.4rem;overflow-x:auto;padding-bottom:.5rem;margin:1rem 0 .2rem;
  -webkit-overflow-scrolling:touch;scrollbar-width:thin}
.stagebar button{all:unset;cursor:pointer;flex:0 0 auto;padding:.45rem .85rem;border:1px solid var(--rule);
  border-radius:999px;font-size:.88rem;font-weight:500;color:var(--ink-2);white-space:nowrap}
.stagebar button[aria-selected="true"]{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.panel{background:var(--paper-2);border-radius:10px;padding:1.2rem 1.3rem;margin-top:.6rem}
.panel h3{margin-top:0;display:flex;gap:.7rem;align-items:center;flex-wrap:wrap}
.panel dt{font-size:.7rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;
  color:var(--ink-3);margin-top:.9rem}
.panel dd{margin:.25rem 0 0}
.panel dl{margin:0}
.filter{display:flex;gap:.6rem;align-items:center;margin:.8rem 0 1rem;max-width:520px}
.filter input{flex:1;min-width:0;font:inherit;padding:.6rem .85rem;border:1px solid var(--rule);
  border-radius:8px;background:var(--paper);color:var(--ink)}
.filter span{font-size:.85rem;color:var(--ink-3);white-space:nowrap;font-variant-numeric:tabular-nums}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:.8rem}
.card{border:1px solid var(--rule);border-radius:10px;background:var(--paper)}
.card[hidden]{display:none}
#phrases tr[hidden]{display:none}
.say{font-family:var(--display);font-style:italic;font-size:1rem}
.card summary{list-style:none;cursor:pointer;padding:.9rem 1rem;display:grid;gap:.35rem}
.card summary::-webkit-details-marker{display:none}
.card summary::after{content:"+";position:absolute;right:1rem;color:var(--ink-3);font-family:var(--mono)}
.card[open] summary::after{content:"\\2212"}
.card summary{position:relative;padding-right:2.2rem}
.card .nm{font-family:var(--mono);font-size:.8rem;color:var(--ink-3)}
.card .ti{font-weight:600;line-height:1.3}
.card .bd{padding:0 1rem 1rem;font-size:.92rem;color:var(--ink-2)}
.card[open] .bd{border-top:1px solid var(--rule);padding-top:.8rem}
.tools{display:flex;flex-wrap:wrap;gap:.3rem;margin-top:.7rem}
.tools i{font-style:normal;font-family:var(--mono);font-size:.72rem;color:var(--ink-3);
  border:1px solid var(--rule);border-radius:4px;padding:.1em .4em}
.tbl{overflow-x:auto;margin:1rem 0 1.4rem}
table{border-collapse:collapse;width:100%;font-size:.92rem;min-width:420px}
th,td{text-align:left;vertical-align:top;padding:.6rem .7rem;border-bottom:1px solid var(--rule)}
th{font-size:.72rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3)}
td code{white-space:nowrap}
.note{border-left:3px solid var(--pencil);padding:.15rem 0 .15rem 1rem;color:var(--ink-2);
  max-width:66ch;margin:1rem 0}
.note.author{border-left-color:var(--author)}
.repos{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1rem;margin:1.2rem 0}
.repo{border:1px solid var(--rule);border-radius:10px;padding:1.1rem 1.2rem;background:var(--paper-2)}
.repo h3{margin-top:0}
.repo .path{font-family:var(--mono);font-size:.78rem;color:var(--ink-3);margin-bottom:.7rem}
dl.gloss dt{font-weight:600;margin-top:.85rem}
dl.gloss dd{margin:.15rem 0 0;color:var(--ink-2);max-width:68ch}
footer{color:var(--ink-3);font-size:.85rem;border-top:1px solid var(--rule);
  padding-top:1.3rem;margin-top:2.5rem;max-width:68ch}
footer code{font-size:.8em}
"""

JS = """
(function(){
  var bar=document.getElementById('stagebar'),pan=document.getElementById('stagepanel');
  if(bar&&pan){
    var data=JSON.parse(document.getElementById('stagedata').textContent);
    function draw(i){
      var s=data[i];
      pan.innerHTML='<h3><span>'+(i+1)+'. '+s.name+'</span><span class="who '+s.who+'">'+s.label+'</span></h3>'
        +'<dl><dt>Say</dt><dd><code>'+s.cmd+'</code></dd>'
        +'<dt>Who</dt><dd>'+s.desk+'</dd>'
        +'<dt>What happens</dt><dd>'+s.what+'</dd>'
        +'<dt>Gated by</dt><dd>'+s.gate+'</dd></dl>';
      Array.prototype.forEach.call(bar.children,function(b,j){
        b.setAttribute('aria-selected',String(j===i));});
    }
    Array.prototype.forEach.call(bar.children,function(b,j){
      b.addEventListener('click',function(){draw(j);});});
    draw(0);
  }
  function wire(inputId,countId,scope){
    var q=document.getElementById(inputId),c=document.getElementById(countId),
        root=document.getElementById(scope);
    if(!q||!root)return;
    var items=Array.prototype.slice.call(root.querySelectorAll('.card'));
    function run(){
      var v=q.value.trim().toLowerCase(),n=0;
      items.forEach(function(el){
        var hit=!v||el.textContent.toLowerCase().indexOf(v)>-1;
        el.hidden=!hit; if(hit)n++;
      });
      if(c)c.textContent=v?(n+' of '+items.length):(items.length+' total');
    }
    q.addEventListener('input',run); run();
  }
  (function(){
    var q=document.getElementById('qsay'),c=document.getElementById('qsayn'),
        tb=document.querySelector('#phrases tbody');
    if(!q||!tb)return;
    var rows=Array.prototype.slice.call(tb.querySelectorAll('tr'));
    function run(){
      var v=q.value.trim().toLowerCase(),n=0;
      rows.forEach(function(tr){
        var hit=!v||tr.textContent.toLowerCase().indexOf(v)>-1;
        tr.hidden=!hit; if(hit)n++;
      });
      if(c)c.textContent=v?(n+' of '+rows.length):(rows.length+' total');
    }
    q.addEventListener('input',run); run();
  })();
  wire('qdesk','qdeskn','desks');
  wire('qcmd','qcmdn','commands');
  var links=Array.prototype.slice.call(document.querySelectorAll('nav.toc a')),
      secs=links.map(function(a){return document.querySelector(a.getAttribute('href'));});
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(!e.isIntersecting)return;
        var i=secs.indexOf(e.target);
        if(i>-1)links.forEach(function(a,j){a.classList.toggle('active',j===i);});
      });
    },{rootMargin:'-10% 0px -80% 0px'});
    secs.forEach(function(s){if(s)io.observe(s);});
  }
})();
"""


def card(name, title, body, tools=None):
    t = ""
    if tools:
        t = '<div class="tools">' + "".join("<i>%s</i>" % esc(x) for x in tools) + "</div>"
    return (
        '<details class="card"><summary>'
        '<span class="nm">%s</span><span class="ti">%s</span></summary>'
        '<div class="bd">%s%s</div></details>'
        % (esc(name), esc(title), body or "<em>No further detail in the mandate.</em>", t)
    )


def render(desks, commands, scripts, thresholds, digest):
    n_cold, n_room = len(desks), len(IN_SESSION)
    stage_json = json.dumps([
        {"name": s["name"], "who": s["who"],
         "label": {"author": "You", "cold": "Cold desk", "script": "Script"}[s["who"]],
         "desk": s["desk"], "cmd": s["cmd"], "what": s["what"], "gate": s["gate"]}
        for s in NARRATIVE["stages"]])

    h = []
    a = h.append
    a("<title>The House Manual</title>")
    a('<link rel="preconnect" href="https://fonts.googleapis.com">')
    a('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    a('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
      'family=Fraunces:opsz,wght@9..144,400;9..144,600&'
      'family=Public+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400&display=swap">')
    a("<style>%s</style>" % CSS)

    secs = [("start", "Start here"), ("flow", "How a chapter moves"), ("desks", "Who works here"),
            ("commands", "What to say"), ("gates", "The counted rules"),
            ("production", "Scripts and hooks"), ("where", "Where things live"),
            ("never", "What it never does"), ("glossary", "Glossary")]

    a('<div class="wrap">')
    a('<nav class="toc" aria-label="Sections"><ol>')
    for sid, label in secs:
        a('<li><a href="#%s">%s</a></li>' % (sid, esc(label)))
    a("</ol></nav><main>")

    # masthead
    a('<header class="mast"><div class="eyebrow">The house manual &middot; for the author</div>')
    a("<h1>The Agentic Ghostwriter</h1>")
    a('<p class="thesis">%s</p>' % NARRATIVE["thesis"])
    a('<div class="keys">')
    for val, lab in [(2, "touches per chapter: the interview and the verdict"),
                     (n_cold + n_room, "desks, %d of them in the room with you" % n_room),
                     (len(commands), "commands, though you only need one"),
                     (1, "door to remember: <code>/gw</code>")]:
        a("<div><b>%s</b><span>%s</span></div>" % (val, lab))
    a("</div>")
    a('<p class="lede" style="margin-top:1.4rem">%s</p>' % NARRATIVE["lede"])
    a('<div class="legend">'
      '<span class="who author">You</span><span>in the room</span>'
      '<span class="who cold">Cold desk</span><span>a sub-agent that never saw the conversation</span>'
      '<span class="who script">Script</span><span>counts, checks, refuses; cannot be persuaded</span>'
      "</div></header>")

    # start
    a('<section id="start"><div class="eyebrow">Section 1</div><h2>Start here</h2>')
    a('<ol class="start">')
    for t, d in NARRATIVE["start"]:
        a("<li><div><b>%s</b><p>%s</p></div></li>" % (t, d))
    a("</ol>")
    a('<p class="note">This page describes the system. It deliberately carries no inbox count '
      "and no chapter progress: those are stale the moment they are written, which is the defect "
      "this page is generated to avoid. Say <code>/gw</code> for live state.</p></section>")

    # flow
    a('<section id="flow"><div class="eyebrow">Section 2</div>'
      "<h2>How a chapter moves</h2>"
      "<p>Seven stages. Tap one to see who runs it and what stops it. You are needed at two of "
      "them; everything between runs cold.</p>")
    a('<div class="stagebar" id="stagebar" role="tablist">')
    for i, s in enumerate(NARRATIVE["stages"]):
        a('<button type="button" role="tab" aria-selected="%s">%d. %s</button>'
          % ("true" if i == 0 else "false", i + 1, esc(s["name"])))
    a("</div>")
    a('<div class="panel" id="stagepanel" role="tabpanel"></div>')
    a('<script type="application/json" id="stagedata">%s</script>' % stage_json)
    a('<p class="note">The brief is the automation boundary. Upstream of it you must be in the '
      "room, because that is where the chapter's ideas come from. Downstream, everything can run "
      "cold.</p></section>")

    # desks
    a('<section id="desks"><div class="eyebrow">Section 3</div><h2>Who works here</h2>')
    a("<p>%d desks. %d run in the session as the voice you are talking to, because a sub-agent "
      "cannot ask you anything. %d run cold. Tap any desk for its mandate.</p>"
      % (n_cold + n_room, n_room, n_cold))
    a('<div class="filter"><input id="qdesk" type="search" placeholder="Filter desks…" '
      'aria-label="Filter desks"><span id="qdeskn"></span></div>')
    a('<div class="cards" id="desks-list">')
    for nm, handle, owns, body in IN_SESSION:
        a(card(handle, nm + " — " + owns, body))
    for d in desks:
        a(card(d["name"], d["title"], d["body"], d["tools"]))
    a("</div>")
    orphans, unwritten = roster_drift(desks)
    if orphans or unwritten:
        msg = []
        if orphans:
            msg.append("a mandate is published for %s, which no longer exists in "
                       "<code>.claude/agents/</code>" % ", ".join("<code>%s</code>" % esc(o) for o in orphans))
        if unwritten:
            msg.append("no extended mandate is written for %s"
                       % ", ".join("<code>%s</code>" % esc(u) for u in unwritten))
        a('<p class="note author"><b>Roster drift:</b> %s. Fix in '
          "<code>scripts/manual_content.py</code>.</p>" % "; and ".join(msg))
    a('<p class="note">Every cold desk is prefixed <code>gw-</code> for a mechanical reason: a '
      "project's own agent definitions override same-named plugin agents, so a desk called "
      "<code>editor</code> here would be silently replaced by the book repo's version, and a "
      "comparison would test the old desks while reporting on the new ones.</p></section>")

    # commands
    a('<section id="commands"><div class="eyebrow">Section 4</div><h2>What to say</h2>')
    a("<p>You hold one door: <code>/gw</code>. On its own it shows a menu built from the state "
      "oracle, so it cannot be stale. With words after it, the Publisher reads what you mean — "
      "<em>readers said…</em>, <em>put it on main</em>, <em>do chapter 12</em>. The other %d "
      "commands are for deliberately re-running one stage; they are not secret, just not the "
      "front door.</p>" % (len(commands) - 1))
    a('<div class="filter"><input id="qcmd" type="search" placeholder="Filter commands…" '
      'aria-label="Filter commands"><span id="qcmdn"></span></div>')
    a('<div class="cards" id="commands-list">')
    for c in commands:
        a(card(c["name"], c["title"], c["body"]))
    a("</div>")
    a("<h3>Or just say it in your own words</h3>")
    a("<p>The Publisher reads intent, so the phrasing below is a sample, not a syntax. If nothing "
      "matches it asks one question with the likely readings rather than guessing: a wrong guess "
      "on <em>status</em> costs nothing, a wrong guess on <em>draft 12</em> costs a chapter "
      "run.</p>")
    a('<div class="filter"><input id="qsay" type="search" placeholder="Try: readers said, put it '
      'on main, floor…" aria-label="Filter phrases"><span id="qsayn"></span></div>')
    a('<div class="tbl"><table id="phrases"><thead><tr><th>You say something like</th>'
      "<th>What happens</th><th>Who</th></tr></thead><tbody>")
    for say, does, who in PHRASES:
        a('<tr><td class="say">%s</td><td>%s</td><td><span class="who %s">%s</span></td></tr>'
          % (say, does, who, {"author": "You", "cold": "Cold desk", "script": "Script"}[who]))
    a("</tbody></table></div></section>")

    # gates
    a('<section id="gates"><div class="eyebrow">Section 5</div><h2>The gates</h2>')
    a("<p>%s</p>" % NARRATIVE["gates_intro"])
    a('<div class="tbl"><table><thead><tr><th>Gate</th><th>Kind</th><th>Catches</th>'
      "<th>Blocks</th><th>On fail</th></tr></thead><tbody>")
    for row in GATES:
        a("<tr>" + "".join("<td>%s</td>" % c for c in row) + "</tr>")
    a("</tbody></table></div>")
    a("<p>A gate that cannot run fails closed. The citation gate blocks when it cannot find its "
      "validator; the voice script reports <code>UNCHECKED</code>, explicitly not a pass, for a "
      "metaphor family nobody declared. Nothing here reports a pass for something it did not "
      "look at.</p>")
    a("<h3>The counted thresholds</h3>")
    a('<div class="tbl"><table><thead><tr><th>Rule</th><th>Threshold</th>'
      "<th>Where it comes from</th></tr></thead><tbody>")
    for t in thresholds:
        src = t["source"] or "—"
        if t["note"]:
            src += " <span style='color:var(--ink-3)'>· " + esc(t["note"]) + "</span>"
        a("<tr><td><code>%s</code></td><td>%s</td><td>%s</td></tr>"
          % (esc(t["key"]), esc(t["value"]), src))
    a("</tbody></table></div>")
    a('<p class="note">Every threshold above is read from <code>config/house.json</code>, the '
      "same file <code>voice_check.py</code> enforces, and each carries a probe asserting it "
      "still matches the book's voice spec. A threshold the author changes in the spec cannot "
      "silently diverge from the copy the script enforces.</p></section>")

    # production
    a('<section id="production"><div class="eyebrow">Section 6</div><h2>Scripts and hooks</h2>')
    a("<p>Production is scripts and hooks, never a desk. Every git failure in the old pipeline's "
      "incident archive was a model following rule text, and every fix was a check that ran on "
      "its own. A session agent would be that failure mode with a title.</p>")
    a('<div class="tbl"><table><thead><tr><th>Script</th><th>Does</th></tr></thead><tbody>')
    for s in scripts:
        a("<tr><td><code>%s</code></td><td>%s</td></tr>" % (esc(s["name"]), esc(s["purpose"])))
    a("</tbody></table></div></section>")

    # where
    a('<section id="where"><div class="eyebrow">Section 7</div><h2>Where things live</h2>')
    a("<p>%s</p>" % NARRATIVE["where_rule"])
    a('<div class="repos">')
    for title, path, body in NARRATIVE["where"]:
        a('<div class="repo"><h3>%s</h3><div class="path">%s</div><p>%s</p></div>'
          % (esc(title), esc(path), body))
    a("</div></section>")

    # never
    a('<section id="never"><div class="eyebrow">Section 8</div><h2>What it never does</h2><ul>')
    for n in NARRATIVE["never"]:
        a("<li>%s</li>" % n)
    a("</ul></section>")

    # glossary
    a('<section id="glossary"><div class="eyebrow">Section 9</div><h2>Glossary</h2>'
      '<dl class="gloss">')
    for term, d in NARRATIVE["glossary"]:
        a("<dt>%s</dt><dd>%s</dd>" % (esc(term), d))
    a("</dl></section>")

    a("<footer><p>This page is <b>derived</b>. The roster, the commands, the thresholds and the "
      "scripts are read from the house itself by <code>scripts/manual.py</code>; only the "
      "narrative is written by hand. Regenerate with <code>python3 scripts/manual.py</code>. "
      "The Stop hook runs <code>--check</code> and says so when the house has changed.</p>"
      "<p>Source of record: <code>CLAUDE.md</code>, <code>ARCHITECTURE.md</code>, "
      "<code>FLOW.md</code>, <code>GAPS.md</code> and <code>FINDINGS.md</code>. Where this page "
      "and those disagree, they win.</p></footer>")
    a("</main></div>")
    a("<script>%s</script>" % JS)
    a("<!-- inputs-digest: %s -->" % digest)
    return "\n".join(h) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Derive the house manual from the house.")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if the house changed since the manual was generated")
    args = ap.parse_args()

    desks = read_desks()
    commands = read_commands()
    scripts = read_scripts()
    thresholds = read_thresholds()
    digest = inputs_digest(desks, commands, scripts, thresholds)

    phantoms = phantom_references(commands)
    if phantoms:
        print("manual: the authored half names %d thing(s) that do not exist on disk:"
              % len(phantoms))
        for x in phantoms:
            print("  x %s" % x)
        print("  Fix scripts/manual_content.py. A manual that invents a gate is the "
              "defect this house exists to prevent.")
        return 1

    if args.check:
        try:
            with open(OUT, encoding="utf-8") as fh:
                current = fh.read()
        except OSError:
            print("manual: docs/manual.html does not exist. Run: python3 scripts/manual.py")
            return 1
        m = re.search(r"<!-- inputs-digest: ([0-9a-f]+) -->", current)
        if not m:
            print("manual: no digest in docs/manual.html. Run: python3 scripts/manual.py")
            return 1
        if m.group(1) != digest:
            print("manual: STALE. The house changed since docs/manual.html was generated.")
            print("  %d cold desks, %d commands, %d scripts, %d counted rules on disk now."
                  % (len(desks), len(commands), len(scripts), len(thresholds)))
            print("  Regenerate: python3 scripts/manual.py")
            print("  Then republish the artifact so the author's link is not stale.")
            return 1
        print("manual: in sync (%d cold desks, %d commands)." % (len(desks), len(commands)))
        return 0

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(render(desks, commands, scripts, thresholds, digest))
    print("manual: wrote %s" % os.path.relpath(OUT, REPO))
    print("  %d desks (%d cold, %d in session), %d commands, %d scripts, %d counted rules"
          % (len(desks) + len(IN_SESSION), len(desks), len(IN_SESSION),
             len(commands), len(scripts), len(thresholds)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
