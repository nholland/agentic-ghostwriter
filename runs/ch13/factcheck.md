# Chapter 13 fact-check audit

Checked 2026-09-23 06:36 CDT. Scope: `runs/ch13/draft.md` against the research brief, `books/the-stoic-husband/06-sources.md`, and the Seneca citation concept. This is a review-readiness audit, not author-copy verification. No chapter, citation ledger, source status, or derived queue was changed.

## Primary source checked

- [Seneca, Moral Letters to Lucilius, Letter 58](https://en.wikisource.org/wiki/Moral_letters_to_Lucilius/Letter_58), sections 22–23; page revision 14886399. Directly opened and read the page text, including surrounding sections 21 and 24–27.
- [Collection title page](https://en.wikisource.org/wiki/Moral_letters_to_Lucilius), translator credit: Richard M. Gummere. This matches the house translator. The displayed front matter identifies a 1925 reprint.
- Reachability probe: `python3 scripts/verification_probe.py books/the-stoic-husband --hosts en.wikisource.org --json` reported the shell egress lane blocked. The web tool successfully opened the actual primary text and title-page text. Evidence is page-text, not search synthesis or an inspected page image.

## Findings

The philosophical paragraph is supported. Section 22 discusses continual change in human beings across age and from day to day. Section 23 explicitly invokes Heraclitus's river and explains the continuing name alongside passing water, extending the comparison to people. The draft accurately paraphrases this through Seneca, rather than presenting a modern river maxim as authenticated ancient wording.

The original discussion concerns flux, bodily impermanence, and mortality within a philosophical argument. It does not establish advice about spouses' interests. The draft's transition, “Bring that thought home,” adequately marks the marriage application as the author's own. Preserve that separation during refinement.

No source quotation appears in the chapter. Its quoted conversational phrases are illustrative dialogue, not attributed classical wording. The twelve-year scenario is explicitly imagined; it is not presented as biography or a research finding.

No unsupported statistical, comparative-frequency, or guaranteed causal claim was found. The draft omits the outline's unsupported ranking of stopped pursuit as the most common and costly mistake. Its observations about feeling unseen or talking less are qualified possibilities and authorial practical guidance, not claims proven by the classical source. “Pre-commitment paradox” functions as the author's descriptive label; this audit does not authenticate it as a named scientific construct. Do not promote it to one without further evidence.

The research brief's optional modern studies and Perel attributions do not appear in the draft and were not independently reverified for this audit. This report does not certify that entire research bibliography.

## Citation axes and remaining work

`seneca-letter-58-heraclitus-river-and-change`: existing status **verifiable**, quote form **paraphrase**, evidence source **page-text**. The independent reading supports those existing axes; no status change was made. Nothing was marked **verified**.

The author must still compare Letter 58.22–23 against his own Gummere copy before assigning **verified**, confirming the locator and the paraphrase's fit in context. No author-copy evidence was available here. No exact ancient quotation has been authenticated or authorized by this audit.

Ready for author review on the source merits of the current draft, with author-copy verification outstanding. No factual correction to the current philosophical paraphrase is proposed. The owning workflow remains responsible for structural gates and any eventual queue regeneration; this narrowly authorized audit writes only this report.
