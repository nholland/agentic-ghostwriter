# Citation Manifest — Retired

*This file was retired 2026-08-14 and replaced by a generated queue.*

**Where to look now:** [`../citation-queue.md`](../citation-queue.md) — the
verification queue, regenerated from the citation ledger by
`scripts/citation_queue.py`. Start there when you want to know what still
needs checking before print.

**Why it was retired.** CLAUDE.md Rule 11 described this file as "a derived,
human-readable table regenerated from those concepts — never a separate source
of truth." Neither half held. Nothing regenerated it, and it carried
quote-level data (verbatim wording, translator, confirmed punctuation) that
existed nowhere else. Being neither derived nor primary, it drifted without
anyone noticing: its "Author Verification Queue" read *"None at this time"*
while seven concepts required a physical-copy check, and ten of its fourteen
quote rows had no concept counterpart at all.

**Nothing was lost.** All fourteen quote rows now live in
[`../okf/citations/`](../okf/index.md) as typed concepts. The ten that had no
counterpart were migrated the same day, carrying their verbatim wording,
translator attribution, and confirmation status. Two of them
(`marcus-aurelius-meditations-11-18-wrongdoing-is-ignorance`,
`marcus-aurelius-meditations-9-28-view-from-above`) carry the confirmation
that `01-voice.md`'s em-dash exception depends on — that the em-dash is the
translator's own punctuation, not house style.

**The old status vocabulary is gone.** `WEB VERIFY` / `AI PARAPHRASE` /
`AUTHOR VERIFY` collapsed onto two independent axes:

| | |
|---|---|
| `status` | `unverified` → `verifiable` → `verified` — how confirmed it is. Only the author sets `verified`, per Rule 11. |
| `quote_form` | `verbatim` / `paraphrase` / `none` — what kind of check it needs. |

`WEB VERIFY` became `status: verifiable` + `quote_form: verbatim`;
`AI PARAPHRASE` became `quote_form: paraphrase` with status judged per source.
Nothing was upgraded to `verified` during the migration.
