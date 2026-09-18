# How to actually run this

Four steps. You never touch a file or run a command.

---

## Step 1 — Get a packet

Ask Claude Code: **"send me verification packet 1"** (or 2, 3…). It arrives as
a file you can open and copy.

Packets are already ordered by urgency. Start at 1.

## Step 2 — Paste it into ChatGPT or Claude Desktop

Open a **brand new conversation**. Not one you've used for something else.

Paste the **entire packet file**, top to bottom. It contains its own
instructions; you don't need to write anything above it. Turn web search /
browsing **on**.

## Step 3 — Let it work, then copy whatever comes back

You do **not** need to make it produce clean JSON. If it returns a report, a
table, or a mess, that's fine.

## Step 4 — Paste the result back to Claude Code

Say: **"here are the verification results for packet 1"** and paste it.

Claude Code converts it, writes the file, runs the ingest, and tells you what
came back confirmed, what changed, and what couldn't be found.

---

# Which mode to use

**This is the part that matters, and it differs by packet.**

## Packets 1–2 — quotes. Use NORMAL mode with browsing. Not Deep Research.

These are 16 exact quotations already printed in the manuscript, mostly Marcus
Aurelius, Epictetus, and Seneca in public-domain translations.

These are **lookups, not research**. The text either says it or it doesn't.
Deep Research is built to synthesize across many sources, which is the wrong
instinct here — it will summarize *about* the passage instead of transcribing
it, and its report format fights the exact-wording transcription the packet
asks for. Normal browsing mode is faster and more accurate for this.

If a model stalls, point it at these directly: **archive.org**, **Project
Gutenberg**, **Wikisource**, **Perseus Digital Library**, **Standard Ebooks**.
All of them carry Long's Marcus Aurelius and Epictetus and Gummere's Seneca in
full text, free.

## Packets 3–7 — claims. Deep Research is GOOD here, and is what you want.

These are 33 research findings asserted in the manuscript: does Falconier
really report r = .45, does Bodenmann's model actually claim what we say it
claims, is the Gottman turning-toward statistic traceable to a real study.

Answering those means reading papers behind paywalls and reconciling what
secondary sources claim against what the primary actually found. **That is
exactly what Deep Research is for.** Use it.

**One adjustment when you use Deep Research:** it usually asks a clarifying
question before it starts. Answer with:

> Verify each entry independently. Do not synthesize across them. For each one
> I need: the specific edition or paper, a URL you actually opened, and whether
> the source supports the claim as stated. "Not found" is a valid and useful
> answer — I would rather know a citation is unsupported than have it
> confirmed on thin evidence.

---

# What to expect, so a bad result doesn't look like a failure

**Some of these will come back NOT_FOUND or WRONG_ATTRIBUTION. That is the
system working.** Several entries got into the ledger from secondary summaries
during sessions when the primary source was unreachable, which is precisely
where misattributions hide.

One is already suspected: the Gottman "86% vs 33%" turning-toward figures
appear in dozens of therapy blogs and, so far, in no peer-reviewed primary.
If that comes back unfounded, the fix is to drop the numbers and keep the
framework, and the manuscript never printed them.

**Nothing gets marked `verified` by this process.** External evidence stages
the exact wording, edition, and locator so that when you check your own copy it
takes thirty seconds instead of an afternoon. You still close it. That's Rule
11 and it isn't negotiable.
