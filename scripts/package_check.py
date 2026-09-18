#!/usr/bin/env python3
"""package_check.py - check the artifact a reader actually receives.

WHY THIS EXISTS. Four defects reached the author in rendered output before this
existed: a blank plate, two overlapping labels, three formatting defects already
fixed once in the book repo's own renderer, and a PDF that opened on the
distillation. He found all four by opening the file, because no script in this
repo read a rendered artifact. Every gate stopped at markdown.
`gw-compile/SKILL.md` states the stake - "Nothing else in the house matters to a
reader" - and nothing executable stood behind the sentence.

The distillation case is the one that named the rule. `compile.py` lifts only the
Practice block out of a distillation and strips the rest, and the book's shipped
manuscript contains the word "distillation" zero times: it is working apparatus
that feeds the back-of-book practice guide. The renderer put it on page one. Two
parts of this repo disagreed about what a reader receives and nothing compared
them.

REWRITTEN 2026-09-18 (#025). The first version matched `<section\b[^>]*>` with a
flat regex and read `class="..."` only - six escapes reached the author's own
retro: a single-quoted class, a `<div>` container, a distillation nested INSIDE
the chapter section (which the flat scan counted as "last" by index, though more
chapter prose followed it on the page), an HTML entity in a heading, an `<h4>`
apparatus heading (the scan was h1-h3), and - the one that mattered on the live
artifact - a first section with NO class at all, which `sections[0] or "chapter"`
silently called "chapter" without checking. `opens on: chapter` was the default
value of a variable, never a verified claim.

This version walks the real tree with `html.parser.HTMLParser` instead: quote
style and entities are the parser's problem, not a regex's; nesting is tracked
so a distillation buried inside another container is caught by depth, not index;
and a top-level container is only ever called "chapter" because it holds an h1 -
never because nothing marked it otherwise. Anything that is neither classed
`dist` nor holds an h1 is UNRECOGNISED and fails closed.

WHAT IT CANNOT DO. It reads the emitted HTML, not the rendered page, so it sees
ordering and apparatus and cannot see overlapping glyphs or a plate that renders
blank on someone else's machine. Those stay with the author and with
runs/design/svgcheck.py. A clean run here is not "the package is good"; it is
"the package does not have the faults we have already shipped".

USAGE
    python3 scripts/package_check.py <package.html> [...]

EXIT
    0  every check passed
    1  at least one failed
    2  bad usage / unreadable input
"""
import sys
from html.parser import HTMLParser

# Headings that are working apparatus. A reader must never meet one.
APPARATUS = ("Draft Notes", "Editor's Notes", "Editors Notes", "Provenance",
             "Research Brief", "Brief Gaps", "Conformance")
CONTAINER_TAGS = {"section", "div", "article"}
HEADING_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}


class _Node:
    """A container tag and everything that happened while it was open, in
    order - text and child containers interleaved, so 'more content after
    this child' is a question this node can answer about itself."""

    def __init__(self, tag, classes, parent):
        self.tag = tag
        self.classes = classes
        self.parent = parent
        self.events = []       # ("text", str) | ("child", _Node)
        self.headings = []     # (tag, text) opened while this node was current

    @property
    def is_dist(self):
        return "dist" in self.classes

    @property
    def has_h1(self):
        return any(t == "h1" for t, _ in self.top_level_headings())

    def top_level_headings(self):
        """Headings that belong to THIS node, not to a nested child container -
        a distillation's own <h2> must not make its parent chapter 'headed'."""
        out = []
        for kind, val in self.events:
            if kind == "heading":
                out.append(val)
        return out

    def children(self):
        return [n for kind, n in self.events if kind == "child"]

    def text_after(self, child):
        """True if this node has any non-whitespace text, or any other
        child, after the given child in document order."""
        seen = False
        for kind, val in self.events:
            if seen:
                if kind == "text" and val.strip():
                    return True
                if kind == "child" and val is not child:
                    return True
            if kind == "child" and val is child:
                seen = True
        return False


class _Walker(HTMLParser):
    """Builds the container tree. convert_charrefs (default True) means
    handle_data already receives entities decoded - '&#39;' arrives as an
    apostrophe, not a string a heading scan could miss."""

    def __init__(self):
        super().__init__()
        self.root = _Node("#root", set(), None)
        self.stack = [self.root]
        self._heading_stack = []   # [tag, buffer] while inside h1-h6
        self.all_dist_nodes = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag in CONTAINER_TAGS:
            classes = set((d.get("class") or "").split())
            node = _Node(tag, classes, self.stack[-1])
            self.stack[-1].events.append(("child", node))
            self.stack.append(node)
            if node.is_dist:
                self.all_dist_nodes.append(node)
        if tag in HEADING_TAGS:
            self._heading_stack.append([tag, []])

    def handle_startendtag(self, tag, attrs):
        pass  # self-closing tags carry no text or nesting relevant here

    def handle_endtag(self, tag):
        if tag in HEADING_TAGS and self._heading_stack and self._heading_stack[-1][0] == tag:
            t, buf = self._heading_stack.pop()
            text = "".join(buf).strip()
            self.stack[-1].events.append(("heading", (t, text)))
        if tag in CONTAINER_TAGS and len(self.stack) > 1 and self.stack[-1].tag == tag:
            self.stack.pop()

    def handle_data(self, data):
        if self._heading_stack:
            self._heading_stack[-1][1].append(data)
        elif self.stack[-1] is not self.root:
            self.stack[-1].events.append(("text", data))


def check(path):
    try:
        html = open(path, encoding="utf-8").read()
    except Exception as exc:
        return [f"UNREADABLE {path}: {exc}"], None

    fails = []
    w = _Walker()
    w.feed(html)
    top = w.root.children()

    # 1. The package opens on the chapter, never on apparatus, and "chapter"
    #    is never assumed - it is verified by the container's own h1. A
    #    container that is neither classed 'dist' nor holds an h1 is
    #    unrecognised and fails closed, rather than defaulting to "chapter".
    if not top:
        fails.append("no top-level <section>/<div>/<article> found; "
                      "cannot tell what the package opens on")
        first = None
    else:
        head = top[0]
        if head.is_dist:
            first = "distillation"
            fails.append("opens on the distillation; the shipped manuscript has none")
        elif head.has_h1:
            first = "chapter"
        else:
            first = "unrecognised"
            fails.append(f"opens on an unrecognised <{head.tag}>: no 'dist' class "
                         "and no h1 - cannot verify this is the chapter")

    # 2. Any distillation container is last among its own siblings, and never
    #    nested inside another container. Nesting is the escape a flat,
    #    index-based scan could not see: a distillation buried inside the
    #    chapter section is "last" by index while more chapter prose follows
    #    it on the actual page.
    for node in w.all_dist_nodes:
        if node.parent is not w.root:
            fails.append(f"a distillation section is nested inside <{node.parent.tag}>, "
                         "not a standalone top-level element")
        elif node.parent.text_after(node):
            fails.append("a distillation section is followed by more top-level "
                         "content; it must be last")

    # 3. Any distillation container is labelled as apparatus, not silently
    #    trailing.
    if w.all_dist_nodes:
        if not any("distback" in n.classes for n in w.all_dist_nodes):
            fails.append("a distillation section is not marked distback")
        if "Not part of the chapter" not in html:
            fails.append("apparatus present but not labelled as apparatus")

    # 4. No apparatus heading reached the reader, h1-h6, entities decoded and
    #    inner tags stripped by the parser rather than a regex.
    def _walk_headings(node):
        for kind, val in node.events:
            if kind == "heading":
                _, text = val
                for word in APPARATUS:
                    if word.lower() in text.lower():
                        fails.append(f"apparatus heading in reader output: {word!r}")
            elif kind == "child":
                _walk_headings(val)
    _walk_headings(w.root)

    return fails, first


def main(argv):
    if len(argv) < 2:
        print(__doc__.strip().split("USAGE")[-1].strip(), file=sys.stderr)
        return 2
    bad = 0
    for path in argv[1:]:
        fails, first = check(path)
        if fails and fails[0].startswith("UNREADABLE"):
            print(f"[SKIP] {path}\n       {fails[0]}")
            return 2
        print(f"{'[FAIL]' if fails else '[ ok ]'} {path}")
        if first:
            print(f"       opens on: {first}")
        for f in fails:
            print(f"       {f}")
        bad += bool(fails)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
