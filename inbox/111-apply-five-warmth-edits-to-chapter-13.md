---
id: 111
status: open
raised_by: Publisher
chapter: 13
opened: 2026-10-02 08:40
---

# Apply five warmth edits to Chapter 13?

Cold review (runs/qa/2026-10-02-warmth-ch13.md) said Ch13 is warm and concrete but ends on a study caveat and 'put the phone down'. Proposed edits, one section at a time via /gw-edit: (1) 'She's working out whether this is a change or just an evening' becomes 'Give it time, and keep asking.'; (2) after 'letting an hour belong to the two of you' add 'The ordinary hour with her is the point.'; (3) add a line he can say: "Something as simple as 'I saw how you handled that, and I'm proud of you' is enough." (suggested wording, yours to approve); (4) move 'Guard against going through every shared hour as though there were nothing left to find out' to the end of the Perel paragraph so the study paragraph ends on 'The show you watch every week can be familiar and good.'; (5) close on 'She's still telling you who she is, a little at a time, and tonight you get to listen.' You said 'Approved' to editing 11-13 in order 13, 12, 11; the section-by-section yes is still needed.

**Recommendation:** Say yes (or send changes) and I will apply Chapter 13 first, in one commit, then re-run voice_check and the practice sync.

**Checked:**

```
$ grep -n 'change or just an evening\|Guard against\|Put the phone down' books/the-stoic-husband/chapters/ch13/refined.md | cut -c1-140
41:When you finally start asking again, she may not open up the way you pictured. Give it time. She's working out whether this is a change o
57:In 2009, Tsapelas, Aron and Orbuch looked at married couples who had been followed for sixteen years. Spouses who said their marriage fel
61:Put the phone down, and give her the evening you came to share.
```

**What unblocks this:** Edits to the landed Chapter 13 (its own commit, distillation and practice guide re-checked), then Chapter 12 and Chapter 11.
