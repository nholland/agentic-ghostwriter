#!/usr/bin/env python3
"""
manual_content.py - the AUTHORED half of the house manual.

manual.py derives the roster, the commands, the counted thresholds and the
production scripts from the repo, so those can never drift. This file holds the
half no file can supply: the mandate behind each desk, the incidents that
produced the gates, the vocabulary, and the walkthrough.

Rescued verbatim from the 2026-09-13 hand-written manual rather than retyped, so
nothing written there is lost in the move to a generated page.

HOW THE TWO HALVES ARE KEPT HONEST
    DESK_NOTES is keyed by agent name. manual.py checks the keys against
    .claude/agents/ both ways: a desk with no note renders from its frontmatter
    and says its mandate is unwritten, and a note for a desk that no longer
    exists is reported. Neither can be silent, which is the whole point.

    Nothing named here may be absent from disk: manual.py's probe checks every
    script and command this file mentions and fails --check when one is missing.
    Two gate rows published on 2026-09-14 named term_check.py and okf_new.py,
    which exist in neither repo. They were extracted programmatically from the
    previous page and therefore trusted. Provenance is not verification.
"""

# Desks that run in the session as the Publisher's own voice. No agent file by
# design: a sub-agent cannot ask the author anything, which is exactly why these
# two are not cold.
IN_SESSION = [
    {
        'name': 'The Publisher',
        'handle': 'you talk to it; it is CLAUDE.md',
        'owns': 'State, routing, the inbox, the gates, relaying to desks.',
        'body': "<p><b>Mandate.</b> The front door. Never writes prose, never argues a chapter's merits. Routes, relays, and keeps the board honest. Names every desk it dispatches so you always know who is working.</p><p><b>Reads.</b> The oracle and the inbox before anything else, every session. Never determines what is next by reading files and reasoning.</p><p><b>Never.</b> Lands on main unprompted. Makes you remember a phrase. Computes next on its own. Resolves an inbox item on your behalf.</p>",
    },
    {
        'name': 'The Developmental Editor',
        'handle': '/gw-interview · /gw-found · /gw-revise · /gw-edit',
        'owns': 'The foundation of a new book, the chapter interview, revisions to locked artifacts, the interactive re-edit.',
        'body': '<p><b>Mandate.</b> The dialogue is the work. Every artifact here is a claim about what you think, so it runs as the session, never as a sub-agent. Ends an interview by writing the substance of what you said into the record the Researcher works from.</p><p><b>Reviewed by.</b> You, at the check-in, before the hand-off.</p><p><b>Never.</b> Regenerates a locked artifact (the voice spec pairs most rules with the incident that produced them; regeneration deletes that history). Regenerates a locked artifact; it revises in place, on your word, as its own commit.</p>',
    },
]

# Keyed by agent name in .claude/agents/. Checked both ways by manual.py.
DESK_NOTES = {
    'gw-researcher': {
        'title': 'The Researcher',
        'owns': 'The brief, gap-marker citations, the cross-chapter reuse check, source ingestion.',
        'body': '<p><b>Mandate.</b> Builds the scaffolding a writer needs. Assembles and verifies; never decides what the chapter argues. When the interview record does not settle something, it writes the gap down.</p><p><b>Reviewed by.</b> The Ghostwriter in plan-only mode, and the citation gate.</p><p><b>Never.</b> Invents a citation, including one you cited. Sets verified. Writes a content concept without proposing it first. Supplies a plausible date instead of reading the clock.</p>',
    },
    'gw-ghostwriter': {
        'title': 'The Ghostwriter',
        'owns': "The draft. In plan-only mode, the brief's reviewer.",
        'body': '<p><b>Mandate.</b> Writes real prose in your voice from the brief. Where something is missing, writes around it and says so in Draft Notes; never invents the missing thing, least of all your own story.</p><p><b>Reviewed by.</b> voice_check.py on every counted rule; the Conformance Checker on every commissioned element.</p><p><b>Never.</b> Em-dashes. A source that reads well and does not exist. A number that is yours. A chapter that fits the word budget by dropping a required element.</p>',
    },
    'gw-lineeditor': {
        'title': 'The Line Editor',
        'owns': "Public placeholders to the ledger's ceiling, the refinement passes, the distillation, the practice-guide section.",
        'body': '<p><b>Mandate.</b> Sharpens; does not rewrite. Five passes: approachability, voice, clarity, flow, anti-slop. Runs the counted script itself and pastes the result, and the Publisher runs it again anyway.</p><p><b>Reviewed by.</b> voice_check.py independently, the Anti-Slop Reader, the Conformance Checker.</p><p><b>Never.</b> Resolves a placeholder with invented content. Confirms a verbatim quotation from a search result. Sets verified. Skips the script because the prose reads clean.</p>',
    },
    'gw-specchecker': {
        'title': 'The Conformance Checker',
        'owns': 'Spec conformance and the attribution audit.',
        'body': "<p><b>Mandate.</b> A clean-room reader with a deliberately starved input set: the chapter's outline section and the prose, nothing else. Not the brief, not the notes, not which pipeline wrote it. It answers one question element by element: did this prose deliver what the outline commissioned?</p><p><b>Why it exists.</b> Chapter 10 shipped having silently dropped its four-virtue structure, both Stoic sources, both named researchers, its central story and its reader ah-ha, and four editing passes reported clean, because the editing stage read only the word target.</p><p><b>Never.</b> Edits. Softens a FAIL because the substitution seems sensible. Reports a PASS it cannot quote. Estimates a word count; it is handed one or reports NOT SUPPLIED.</p>",
    },
    'gw-slopreader': {
        'title': 'The Anti-Slop Reader',
        'owns': 'The qualitative half of the anti-slop check, and the cross-chapter patterns only a whole-book read reveals.',
        'body': '<p><b>Mandate.</b> Owns exactly what no script can count: invented foils, indirection, scenes watched from outside, windups, the wife cast as a threat, universal claims about all men. At book level: the same opening structure twice across Parts, anchor metaphors that contradict each other, a term used as established that nothing defined.</p><p><b>Never.</b> Edits. Duplicates a counted rule. Lets silence be read as a pass: it ends by naming what it did not read.</p>',
    },
    'gw-factchecker': {
        'title': 'The Fact-Checker',
        'owns': 'The citation ledger from unverified up to verifiable, the external verification packets, the defects register.',
        'body': '<p><b>Mandate.</b> Search may locate a source or flag a defect; it may never transcribe a quotation. Probes what this machine can reach rather than reasoning about it, because reachability differs between the cloud and your laptop. Routes each citation by tier and reachability; packages the rest for a session with real access.</p><p><b>Never.</b> Sets verified; only you can, against your copy. Invents a house translation. Rewrites printed prose silently; it proposes.</p>',
    },
    'gw-panel': {
        'title': 'The Reader Panel',
        'owns': 'The whole-book readers: the Skeptic, the beta readers, the tension reader, the continuity editor.',
        'body': '<p><b>Mandate.</b> Runs several readers over the manuscript and returns one synthesised ranked list, not four reports stapled together. Where two personas disagree, it keeps both; the disagreement is the finding.</p><p><b>Runs under.</b> /gw-qa, with the Anti-Slop Reader alongside. Needs at least half the arc or it says so, because a tension audit over a third of a book reports a flat arc that is simply incomplete.</p><p><b>Never.</b> Fixes anything. Averages two readings into a moderate one.</p>',
    },
    'gw-publicist': {
        'title': 'The Publicist',
        'owns': 'Substack posts, social teasers, the callouts pass, and the whole-book publication stack.',
        'body': "<p><b>Mandate.</b> Drafts everything that leaves the building short of the book. Per chapter: identifies the four to six publishable concepts first, as a list you choose from. Whole book, late: positioning, pitch, publishing path, indie plan, review strategy, book-club guide, a channel inventory. States the arc's coverage before producing anything and carries it in the filename.</p><p><b>Never.</b> Posts, submits, connects, or implies any of those happened. Invents a statistic to make a hook land. Quotes a Stoic source below verifiable. Claims reader numbers it was not given.</p>",
    },
    'gw-designer': {
        'title': 'The Designer',
        'owns': "Concept plates and Part closing plates, drawn from the book's design layer and never invented to fill a layout.",
        'body': "<p><b>Mandate.</b> Design elements are derived from approved content, never invented to complete a design. Reuses the four house marks; matches the concept-plate idiom for a chapter and the Part idiom (6x9, black line, captioned with the opening page's last sentence) for a Part's close; draws only concepts the generated candidate register lists as reader-facing. Renders before returning, because two rejected marks and two rejected plates were invisible in the markup.</p><p><b>Why concept first.</b> Drawing the Incomplete Husband plate exposed a sixth failure mode the framework did not name. It was proposed, approved, and written into the concept before it was drawn. A gap the drawing exposes goes to the inbox; the Designer never fills it.</p><p><b>Never.</b> Redraws a mark. Mixes the two idioms. Puts a cardinal-virtue name, an unsourced number, or an unverifiable quotation on a plate. Blocks a chapter.</p>",
    },
    'gw-retro': {
        'title': 'The Archivist',
        'owns': 'The session review: what broke, what was missing, what was too hard, what worked, what recurs.',
        'body': "<p><b>Mandate.</b> Dispatched once three commits touching the work have piled up, or when you say you are done. Reads the session's diff, the log, the inbox, all of FINDINGS.md and the old pipeline's incident archive, then reviews through five lenses and suggests only if necessary. Every suggestion is typed and priced, and every addition names a deletion.</p><p><b>Why it proposes and never applies.</b> A learning loop that edits its own rules grew the old ledger from 739 to 6,026 words in 27 days and spent five of nine sessions on maintenance instead of the book.</p><p><b>Never.</b> Edits a rule file. Manufactures a finding. Shows you more than two suggestions; the full review goes to runs/retro/, and if nothing clears the bar you get one line.</p>",
    },
}

# The gates, as rows: name, kind, catches, blocks, on-fail.
GATES = [
    ['<code>resolve_book.py</code>', '<span class="who script">Script</span>', 'No book, a missing voice spec, a missing dependency. A skill reading a missing voice spec does not crash; it writes generic prose.', 'Every desk', 'Nothing runs until it resolves'],
    ['<code>okf_gate.py</code>', '<span class="who script">Script</span>', 'A citation bundle breaking the transcription rule; a voice threshold that no longer matches the spec', 'Every prose-writing skill', 'No prose is written'],
    ['Plan-only review', '<span class="who cold">Cold desk</span>', 'A brief that cannot be written from cold: the Ghostwriter answers one question, <em>could someone who never read the interview write this from this file alone?</em>', 'Draft', 'One round back to the Researcher, then the gaps only you can close go to the inbox'],
    ['<code>voice_check.py</code>', '<span class="who script">Script</span>', "Em-dashes, bold as a crutch, the long-sentence share, direct-address density, the anchor metaphor's family count. Literal counts against the thresholds in your voice spec.", 'Draft, refine, every short-form piece', 'Two cold rounds, then the inbox'],
    ['Conformance Checker', '<span class="who cold">Cold desk</span>', 'An outline row the prose did not deliver; a source used but not named where the reader can see it. Two verdicts, PASS and FAIL, a quote behind every PASS.', 'Draft, refine', 'Two cold rounds, then the inbox'],
    ['Anti-Slop Reader', '<span class="who cold">Cold desk</span>', 'The half no script can count: invented foils, indirection, scenes watched from outside, the wife cast as a threat, a term relabelled between chapters', 'Refine (findings routed, never auto-applied)', 'Plain fixes to the Line Editor; anything that changes the argument to you'],
    ['The inbox', '<span class="who author">Author</span>', 'Everything a cold desk could not decide', 'Nothing; it collects', 'You rule, in your words, and the desk resumes'],
]

# The vocabulary: what the author says, what happens, who does it.
PHRASES = [
    ['/gw', 'The menu: what is next (from the oracle), what is waiting on you, and the few things you might say. Never stale, because it is computed.', 'script'],
    ['12 · chapter 12 · do the next chapter', 'Runs Chapter 12 end to end, pausing at the interview, the concept confirmation, and the verdict. Resumes from wherever it stopped.', 'author'],
    ['shadow 12 · draft 12 from their brief · run 12 in parallel', "Drafts Chapter 12 cold from the book pipeline's brief, into runs/, with every gate from the draft onward. The board offers this on its own when the brief exists.", 'cold'],
    ["run the floor · work while I'm gone · do all the cold stuff", 'Every chapter whose next stage needs no author, dispatched at once. A chapter that fails a gate twice is parked; the others continue.', 'cold'],
    ['next · go · continue · what now', "Runs the oracle's next action. Never a guess.", 'script'],
    ["status · where are we · how's it going", 'The board: every chapter, the inbox, parked questions, the floor.', 'script'],
    ['inbox · what do you need from me · waiting on me', 'The questions cold desks could not decide, each with the context to answer cold. Your ruling is recorded in your words and the desk resumes.', 'author'],
    ['readers said… · feedback · someone told me', 'Each response is logged as a signal (proposed first, written after you confirm), then routed by what it is: lost reader, argued objection, factual challenge, gift, new scope.', 'cold'],
    ['compile · pdf · send to readers · print it', "A clean PDF through the book's one renderer, citation gate first, word count compared with the previous compile.", 'script'],
    ['compare · bake-off · which is better · old vs new', 'The blind packet for a chapter the old pipeline also refined (Ch1-11, control in the frozen archive). You read two neutral variants; the mapping stays sealed until your verdict is written.', 'author'],
    ['verify · citations · are the sources right · check the quotes', 'The Fact-Checker works the citation queue: probes reachability, transcribes real pages where it can, confirms claims by search where that is enough, packages the rest. Never sets verified.', 'cold'],
    ['qa · whole book · does it hold together · beta', 'The Reader Panel and the Anti-Slop Reader over the manuscript, merged into one ranked list. Reports; opens no fix loop.', 'cold'],
    ['substack · social · post · newsletter', "The Publicist identifies a chapter's publishable concepts as a list you choose from, then drafts. Nothing is posted.", 'cold'],
    ['positioning · taglines · pitch · proposal · query letter · KDP · ARC · book club · traditional or self', 'The publication stack, one mode per deliverable. The coverage of the arc is stated first and carried in the filename.', 'cold'],
    ['new book · I have an idea for…', 'The Foundation phase with the Developmental Editor: premise, archetype, voice, audience, outline, each shown and ratified before the next.', 'author'],
    ['change the voice · fix the outline · the premise is wrong', 'Revise a locked artifact with the history kept. For a book the book pipeline ships, a diff for you to apply there.', 'author'],
    ['I have material · read these · ingest', 'Raw sources into typed knowledge: gap markers and source findings written, content concepts proposed for your yes.', 'cold'],
    ['edit 12 · that line is wrong · fix the opening · edit the introduction', 'Section by section, in the room, your wording kept, counts re-run afterwards. Also the prologue, the introduction, and the part pages.', 'author'],
    ['remember that · write that down · for the record', "Your words, verbatim, clock-stamped. Never on a desk's initiative.", 'author'],
    ["park that · not now · let's decide later", 'A deferred question with a revisit trigger (an event, not a date). Raised again when the trigger arrives.', 'author'],
    ['parked · what did we defer · come back to', "The parked list, with each question's trigger.", 'script'],
    ["what's missing · what can't you do yet", 'Answered from GAPS.md, which registers each deferred capability with the trigger that closes it. Say "not yet, and here is what it waits on" rather than discovering the gap when you need it.', 'script'],
    ['interview 12 · research 12 · draft 12 · refine 12', 'One stage, for a deliberate re-run. Not the normal path.', 'cold'],
    ['put it on main · land · ship it · make it official', 'Fast-forward only, on your word alone. The branch is named in the reply.', 'script'],
    ['push · save · back this up', 'Pushes the session branch and says its name. Not main.', 'script'],
    ["is my work safe · where's my stuff · what branch", 'Branch, ahead and behind main, unpushed, uncommitted, in plain words.', 'script'],
    ["done · that's it · bye · see you tomorrow", 'The Archivist reviews the session if it has not yet; then two lines on where your work is and an offer to put it on main. Nothing lands unless you say so.', 'author'],
    ['retro · what did we learn · what went wrong', 'The Archivist, cold. Proposals shown; nothing applied without your yes.', 'cold'],
    ['switch to… · which books', 'Lists the registry; views another registered book for this session without touching the manifest.', 'script'],
    ['how does this work · explain the house · show me the map', 'This page.', 'script'],
    ['help · what can you do', 'The full table, one line each, then the menu.', 'script'],
]


# What each foundation document is for. Keyed by filename so manual.py can check
# both ways against resolve_book.py's own lists: a file the house requires but
# nobody described renders as unlabelled rather than silently missing, and a
# description for a file no longer required is reported.
FOUNDATION_ROLES = {
    "00-premise.md": ("The premise",
        "What the book argues and who it is for, in under a page. Every desk reads it; "
        "a chapter that drifts from it is drifting from the book."),
    "01-voice.md": ("The voice constitution",
        "How the prose sounds, and the counted rules that enforce it. Most of its rules "
        "are paired with the incident that produced them, which is why it is revised "
        "and never regenerated."),
    "02-audience.md": ("The audience map",
        "Who is reading, what they already believe, and what they will not sit still for."),
    "03-outline.md": ("The outline",
        "The commission. Each chapter's required elements, and what the Conformance "
        "Checker grades the prose against, row by row."),
    "04-archetype.md": ("The archetype",
        "The book's shape - how a chapter opens, turns and closes - so chapters feel "
        "like one book rather than a collection."),
    "05-framework.md": ("The framework",
        "The book's central model, and which chapter carries which cell of it."),
    "06-sources.md": ("The sources policy",
        "Which editions and translations are the house's, so two chapters never quote "
        "the same passage from two different books."),
    "progress.md": ("The progress log",
        "The old pipeline's memory, migrated with the book. Read for history; this house's memory is FINDINGS.md and the inbox."),
    "parking-lot.md": ("The parking lot",
        "Questions deliberately deferred, each with the trigger that brings it back - "
        "not a date, an event."),
}

# Where everything the house produces actually lands. Authored because it is the
# house's own contract rather than a fact in any file; the boundary it describes
# is CLAUDE.md Rule 8: apparatus in runs/, the book in books/, landed after the verdict.
ARTIFACTS = [
    ("runs/chNN/", "engine",
     "Everything a chapter run produces: the interview record, the brief, the draft, "
     "the refined prose, the distillation, the plate. The worst case for a failed "
     "experiment is a directory of prose nobody uses."),
    ("runs/manuscript/", "engine",
     "Compiled manuscripts and their PDFs, each filename carrying its coverage and "
     "date. A file called manuscript.pdf claims to be current forever."),
    ("runs/revisions/", "engine",
     "Proposed diffs to the constitution, kept until the author rules; applied on his "
     "word as their own commit."),
    ("runs/qa/, runs/marketing/", "engine",
     "Whole-book reads and publicity drafts, also named by the range they cover."),
    ("inbox/", "engine",
     "The only durable record this repo keeps. Questions a cold desk could not "
     "decide, and rulings whose change has not landed yet."),
    ("okf/", "book",
     "The knowledge layer. Gap markers and source findings land with a chapter; content concepts only "
     "after the author confirms them; every status change through the validator."),
    ("chapters/chNN/", "book",
     "The chapters that ship. Landed by the Publisher after the verdict, via land.py; "
     "never written by a desk."),
]
