# Parking-lot triage — P-003, read 2026-10-03

*Basis (Rule 15): `books/the-stoic-husband/parking-lot.md` as of 2026-10-03, every
item not marked RESOLVED, checked against this house's files. **Proposal only.**
Nothing in the parking lot, `runs/parked.md`, the outline or the inbox was
changed. The old parking lot stays read-only history (CLAUDE.md, Layers); a
closed item is recorded in `runs/parked.md`, not edited in place.*

**Count:** 21 open items (#5 to #39) plus the "Explore JEV" block. Verdicts:
**8 done or superseded** (#8, #21, #22, #30, #31, #34, #36, #37), **9 still live**
(#5, #9, #12, #23, #29, #32, #33, #35, and #39, which governs #36/#37),
**4 need an author answer** (#20, #24, #26, #38; #38's trigger has also already
fired). The JEV block is a fifth question, not a numbered item. P-004 (this
house's own file) has a stale chapter reference, found on the way.

## Done or superseded — propose closing, each with a one-line note

| # | Item | Evidence it is done |
|---|---|---|
| 34 | Build the Agentic Publishing House | This repo is that house; CLAUDE.md "The house ships the book." |
| 31 | Rename Parts IV and V (Desert, Orchard) | Outline revision note 2026-10-02 says "Resolves parking-lot item #31"; `parts/part-4-the-desert.md` and `part-5-the-orchard.md` exist; manifest Part keys renamed. |
| 8 | Buffer auto-posting | Carried in `GAPS.md` (publication stack, with its trigger). |
| 30 | `/book-status` reports Part-opening state | The need was discovering a declared-but-unwritten Part opening. All five Part pages exist now. `/book-status` is gone. |
| 21 | Reverify sub-agent stats; scan repeated rhetorical devices | Rule 7 (agents review agents; the skill reruns the script) and `voice_check.py` `check_devices` (`rhetorical_device_max`). |
| 22 | Chapter-retitle playbook | `gw-revise` SKILL.md "If the change is a chapter retitle"; exercised on 2026-10-01 and 10-02. |
| 36, 37 | Oak growth line; canyon tie and Part title rule | Already re-triggered by #39 / P-005 to "once the arcs are complete". Nothing to do but cross-reference. |

## Still live — keep, move to `runs/parked.md` with a real trigger

| # | Item | Trigger (confirmed) | Note |
|---|---|---|---|
| 5 | Stoic Evening Review as a recurring motif | Ch24 research | **Risk:** Ch24's outline spec does not mention it; the plan lives only in `okf/frameworks/the-evening-review-stoic-night-practice.md`. A one-line pointer in the Ch24 spec would stop it being forgotten. That is a constitution edit, so it needs his word. |
| 9 | Stoic content baked into shared desks | Before a second book | Seven desk and skill files and `config/house.json` (`stoic_terms`, mirrored thresholds) still name Stoic things. Same coupling as `switch_book.py`'s voice-mirror warning. |
| 12 | Three one-sided-reciprocity incidents | Ch26 research (*Friendship Is the Hidden Engine*, number unchanged); the audiobook scene to **Ch23** (*Repair*, was Ch17) | Chapter numbers in the old item are stale after the 2026-10-02 renumber. |
| 23 | Trepidation about sharing with his wife | His call; natural point is after `/gw-qa` | Personal. Leave as written. |
| 29 | Line-by-line lesson dissection | A chapter reads padded and nobody can say which sentences | Related to inbox #101 and #111, not duplicated by them. |
| 32 | Close the Lane C verbatim citations | A session on his laptop | **The "22" is stale.** `citations.py` now says 140 total, 136 open (100 verifiable, 36 unverified). Recount at the time. |
| 33 | `verification_packet.py` renumbers packets on every run | Before the next packet generation | Not fixed: the script has no stable-id logic. |
| 35 | House-translation retrofit | (1) his read of Ch10; (2) with #32 | (3), the Gutenberg-mirror route, is now in `gw-factchecker.md`. Marcus and Epictetus ids are there; Seneca's is not. |

## Needs one author answer

1. **#26 / #24 — Ch10.** "You hold it anyway" is in the landed prose three times,
   and the chapter's notes still call it a placeholder for "The oak holds firm."
   Inbox 099 changed Ch10 on 2026-10-02 without ruling on it. *Is "You hold it
   anyway" the final refrain, or does something replace it?* (#24 asks the same of
   two composite moments, the Tier 1 anger pressure and the Tier 3 Christmas
   morning: real material or keep the composites.)
2. **#20 — read aloud.** He already listens on an audio reader (FINDINGS.md, the
   spaced-letters fix). *Should the verdict package say "read it aloud first", or
   is that already how he works?* A prompt in the package is a rule edit, so his word.
3. **JEV (Explore JEV block).** Still advisory, no API key, and it cites 233
   fixtures; the suite is 310. *Keep parked, or drop?*
4. **#38 — whole-set plate findings.** See below.

## A trigger has already fired

**#38** said "at the first Part III chapter plate, whichever comes first." Part III
has begun: Ch12 (*the-thing-with-no-deadline*) and Ch13 (*keep-learning-her…*)
have plates in `design/plates/`. Finding (2), that no plate in the set draws
warmth, was "cheapest to act on before Part III plates exist." Those two plates now
exist, so the question is live: *did they break the damage-avoided pattern, and
does Ch14's plate get an explicit warmth brief?* The "no rethinks" ruling's status
is not recorded anywhere I could find.

## Found on the way

**P-004's trigger is stale.** It says "the Chapter 23 interview." After the
2026-10-02 renumber, Chapter 23 is *Repair Quickly, Love Deliberately*. The
endurance-versus-cowardice material belongs to **Chapter 22, *Fear Is Not
Commitment*** (retitled from "The Difference Between Endurance and Cowardice").
Left unfixed, the commission would be offered at the wrong interview and then
"die there," as P-004 says it will.

## Proposed next steps (none taken)

- Record the 7 closures and 8 live items in `runs/parked.md` (one line each, naming
  what superseded or what trigger), and amend P-004's chapter reference.
- Put the four author questions in the inbox as one item each, or have him answer
  them in session.
