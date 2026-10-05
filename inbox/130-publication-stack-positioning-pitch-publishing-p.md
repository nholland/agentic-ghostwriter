---
id: 130
status: open
kind: gap
trigger: the author approves the whole-book QA pass (/gw-qa) and says the book is close
raised_by: Publisher
chapter: -
opened: 2026-09-13 00:00
---

# Publication stack: positioning, pitch, publishing path, indie plan, review strategy, book club guide, Substack push, Buffer

*Migrated 2026-10-04 from GAPS.md.*

**Audit basis:** the 2026-09-13 audit of all 40 old `book-*` commands found 27 covered and 13 not; re-counted 2026-10-03 after building edit, note, park, switch and distill --refresh: 32 covered, 1 not needed until a second book (`intro`), 7 open (the publication stack below). Re-run the audit when desks are added or the old pipeline changes; an uncounted gap register is the citation-manifest.md failure wearing a new name.

**Trigger: the author approves the whole-book QA pass (`/gw-qa`) and says the book
is close.** Every one of these needs the finished arc, the QA findings, and the
callouts to be accurate. With 15 of 28 chapters not yet landed (as of 2026-10-03), each would be built on
a book that does not exist yet — and `/book-marketing`'s own note says as much:
*"It requires the full arc, QA results, and callouts before it can be accurate."*

| Gap | Old command | What it produces |
|---|---|---|
| Whole-book positioning | `marketing` | Amazon description, taglines, comp titles, category strategy |
| Publisher pitch | `pitch` | Proposal and query letter |
| Publishing path | `publish-path` | Traditional versus indie, decided on evidence |
| Indie launch plan | `indie-plan` | KDP / IngramSpark strategy |
| Review strategy | `review-strategy` | ARC programme and early reviews |
| Book club guide | `club-guide` | Reading group materials |
| Substack integration | `substack-connect` | Pushing a drafted post to Substack, not just writing one |
| Buffer integration | *never built* | Auto-posting social.md content to X/IG/FB after the Substack push |

**Substack, checked rather than assumed, 2026-09-19.** Two separate things were
checked, not one. First: this session's org-level connectors (`ListConnectors`,
full list) are Gmail, Google Calendar, Google Drive and Linear — nothing
publishing-related at all. Second, and more precise: the old pipeline's Substack
tool was never an org connector to begin with. `progress.md` (2026-07-08) records
it as `substack-mcp`, a locally-installed npm package on the author's own machine,
cookie-authenticated, configured in a `.mcp.json` the book repo's own `.gitignore`
explicitly excludes ("contains live credentials, never commit"). So nothing was
lost migrating it — it was never in either repo to lose. `book-manifest.json`'s
`integrations.substack.status: "connected"` (as it read then) does **not** mean this system can post:
read closely, it is the author's own publication existing at that URL, a business
fact, not a technical credential live in this session. Rechecked 2026-10-02 from this cloud session: substack.com is unreachable (HTTP 000) and the npm registry returns 403, so a push cannot run here at all; it waits on a session on the author's own machine, where the cookie and the MCP already work.

**This exact failure already happened once and is on record.** `.claude/LEARNINGS.md`
item 7 (migrated with the book): *"Manifest state can lie about live session
capability. `book-manifest.json` said Substack was `"connected"`, but no MCP tool
was actually loaded in this (cloud) session."* The old pipeline's fix was a live
tool-availability check at the point of use, in `/book-substack` Step 3.5. This
house doesn't need that specific fix — `gw-publicist` never attempts a live push,
so there's no point of use to check at — but the stale manifest field itself rode
along unflagged until asked about directly here. The manifest field was corrected
2026-10-03: `integrations.substack.status` now reads `"author-hosted"`, which
states the business fact without implying a live credential.

**Buffer was never audited in, because it was never a command.** The 2026-09-13
audit covered the 40 `book-*` commands; Buffer (`parking-lot.md` #8, 2026-06-17)
was a parked idea for extending one of them, deferred behind "Substack working
end-to-end" and never implemented, so it had no command to be counted against.
Same shape as the Substack finding: `gw-publicist`'s mandate covers it exactly the
same way (drafts only; if built, pushes a draft, never posts unattended).

**Nothing above changes `gw-publicist`'s mandate** ("nothing is ever posted, and
publishing decisions stay the author's") for either row — closing them means a
draft can be pushed as a draft for the author to publish, never that this house
posts unattended. Until they're closed, a drafted post is copied out and posted by
hand, same as today.


**Owner when built: the Publicist.** Not seven skills — the old pipeline's shape.
One `/gw-publish` with a mode per deliverable, because they share their inputs (the
arc, the QA findings, the callouts, the positioning) and splitting them is how ten
marketing commands happened. The Publicist's mandate already forbids posting
anything; that does not change.
