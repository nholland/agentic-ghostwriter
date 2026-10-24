---
id: 149
status: resolved
raised_by: Publisher
chapter: 15
opened: 2026-10-23 15:16
resolved: 2026-10-24 00:27
okf_receipt: runs/reconciliation/2026-10-24-inbox-149.json
---

# Which translation is the house edition for Seneca's dialogues (De Ira, On Clemency, On the Happy Life)?

06-sources.md names Gummere for the Letters and Stewart 1887 for De Beneficiis only. Chapter 4 prints De Ira as 'trans. Basore'. The Ch15 research read Stewart 1889 (Minor Dialogues, Gutenberg #64576, public domain) for De Ira II.34.5, On Clemency II.5-6 and De Vita Beata XXIV. Basore's 1928 Loeb may now be public domain but the date was not confirmed. Raised by the Researcher in both Ch15 passes.

**Recommendation:** Name Stewart 1889 as the house edition for the dialogues (public domain, already read), and note Ch4's 'Basore' for correction at its next edit.

**Checked:**

```
$ grep -n -i -E 'seneca|stewart|gummere|basore' books/the-stoic-husband/06-sources.md
19:| Seneca, *Letters* | **Richard Gummere** (Loeb, 1917–25) | Public domain (US) |
52:- **John Basore** (Loeb, 1935) — Seneca's *De Beneficiis*. In copyright. The
53:  public-domain alternative is **Aubrey Stewart (1887)**, which is what this
```

**What unblocks this:** Whether Chapter 15 may quote Seneca De Ira II.34.5 (the best anchor for 'it takes two men to fight') or On Clemency, and in whose English

## Check, 2026-10-24 (Publisher, at the author's request: "Can we check Basore?")

Read Basore's De Ira II.34 and II.4 in the archive.org scan of the 1928 Loeb volume I (moralessayswithe01seneuoft).
- Basore's English for II.34.5: "Animosity, if abandoned by one side, forthwith dies; it takes two to make a fight. But if anger shall be rife on both sides, if the conflict comes, he is the better man who first withdraws; the vanquished is the one who wins." (OCR; see the staged concept.)
- Ch4's printed De Ira II.4 wording is Basore's; its translator label is correct.
- Volume I is a 1928 publication, so it entered the US public domain on 1 January 2024. De Beneficiis (Basore 1935, volume III) is still in copyright; Stewart 1887 stays the house pick for it. Non-US status unconfirmed.
- Updated recommendation: Basore (1928) for the essays in volume I, which already matches Ch4; Stewart 1889 only if the author prefers "the winner is the real loser".

**Resolution (2026-10-24 00:27):** A (2026-10-24): Basore (Loeb, Moral Essays I, 1928) is the house edition for Seneca's essays. Applied in commit e72cde6.
