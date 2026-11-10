# ePub design review: book-draft.epub (Prologue to Chapter 16)

Designer desk, review mode. 2026-11-07 14:44. Nothing in the book or the build was changed.

**What I checked:** `output/compiled/book-draft.epub` (1.88 MB, EPUBCheck 0/0 per the brief; not re-run here). I unzipped it to the scratchpad and rendered every `EPUB/text/*.xhtml`, plus the title page and the nav, in Chromium with the book's stylesheet. I used a 16px reader margin at 390x844 (phone) and 768x1024 (tablet). That gave 136 screenshots: the opening of each file, every plate, and every "Putting into Practice" section. I compared them against `books/the-stoic-husband/design/plates/README.md` and pages 1, 12, 13, 21 and 52 of `output/compiled/book.pdf`.

**Caveat:** Chromium in scroll mode is not a real e-reader. It shows the CSS and the markup faithfully, but not how pages break. Page-break findings come from reading the markup.

**Screenshots** (in `runs/epub/epub-review-shots/`):
- `phone-*`, `tablet-*`: the ePub as built.
- `fix-phone-ch004-*`: the same chapter with the fixes in items 1 to 5 applied to a scratch copy.
- `print-reference-strip.png`: the approved print pages.

## Ranked findings

### 1. The practice page lost its look, and its kicker sits in the wrong section (all 16 chapters)
`prep.py` removes every `<div>` and `<section>`, which takes the classes `kicker`, `rule`, `runin`, `dist` and `distback` with them. Then pandoc splits sections at the demoted `h2`. The result:
- "Putting into Practice" becomes a plain left-aligned `<p>` stranded at the end of the chapter's last beat section, *before* the practice heading (`<p>Putting into Practice</p>` then `</section>`). Screen readers and the EPUB structure treat it as part of the chapter's closing prose.
- The title is a large bold left `h2`. In print it is a smaller, centred 14pt title.
- The short centred rule is now a full-width grooved `<hr>`.
- "Practice" is a bold heading as big as the beat headings. In print it is a grey spaced small-caps label with a hairline under it.
- Nothing starts the practice section on a fresh page. In print, `.distback` does.

**Fix:** in `prep.py`, before flattening, rewrite `<p class="kicker">Putting into Practice</p><h1>` as `<h2 class="dist-title"><span class="kicker">Putting into Practice</span>`. Pandoc keeps header classes and spans. Then add to `epub.css`:

```css
section.dist-title{page-break-before:always;break-before:page}
h2.dist-title{text-align:center;font-size:1.2em;font-weight:600;margin:0 0 .3em}
h2.dist-title .kicker{display:block;font-style:italic;font-weight:normal;font-size:.75em;letter-spacing:.06em;color:#5a5a5a;margin-bottom:.4em}
h2.dist-title + hr{width:40%;margin:.4em auto 1em}
section.dist-title p{margin:0 0 .5em}
section.level2:not(.beat-heading):not(.dist-title) > h2{font-size:.8em;letter-spacing:.16em;text-transform:uppercase;color:#5a5a5a;border-bottom:1px solid #ddd;padding-bottom:.2em}
```

Verified in `fix-phone-ch004-practice.png`: it now matches the print page.

### 2. Plates are drawn 23% narrower than the screen on phones, and ch1 to ch11 are not readable there even at full width
Pandoc wraps each plate in `<figure>`. The stylesheet never resets the browser's default figure margin (`1em 40px`), so on a 390 phone every chapter plate renders at **262 CSS px** inside a 342 px text column (`phone-ch004-plate0.png`). On the tablet they render at 640 px, which is fine. Sharpness is fine everywhere: the PNGs are 1920 px wide, three times the display size.

**Fix:**
```css
figure{margin:0}
figure.plate{page-break-before:always;break-before:page;page-break-inside:avoid;text-align:center}
figure.plate img{width:100%;max-height:95vh;margin:0 auto}
```
This is what print does: a plate is a page of its own. Verified in `fix-phone-ch004-plate.png`: the plate goes from 262 to 342 px.

**Author ruling needed (not an ePub fix).** Even at full width, the ch1 to ch11 plates set captions at 12 to 13.5px on a 640 canvas. On a phone that is about 6.4 CSS px, below legible: "he becomes small without deciding to" on ch5 cannot be read (`phone-ch008-plate0.png`). The ch12 to ch16 plates use 19 to 24px type and read fine. The Designer's own standard is "legible at phone width". The options are:
- (a) accept tap-to-zoom (Apple Books and Kindle both support it) for ch1 to ch11;
- (b) re-set those plates' type to the ch12 to ch16 sizes, which is a revision through `/gw-plate`.

### 3. The chapter openings do not match the house format
Print sets a small grey "Chapter 1" label, then the bold title on its own line. `prep.py` merges them into one heading, "Chapter 1: The Three-Second Window", which on a phone wraps to two ragged lines (`phone-ch004-open.png`).

**Fix:** keep the label as a span:
```
<h1 class="chapter-heading"><span class="num">Chapter 1<span class="sep">: </span></span>The Three-Second Window</h1>
```
with:
```css
h1.chapter-heading .num{display:block;font-size:.55em;font-weight:normal;color:#444;margin-bottom:.5em}
h1.chapter-heading .sep{display:none}
```
The contents list keeps "Chapter 1: The Three-Second Window". Verified in `fix-phone-ch004-open.png`. Beat headings (`h2.beat-heading`) should also drop to `1em` bold to match print's 11pt run, since they now compete with the chapter title.

### 4. Section rules are full-width grooved lines
Every beat ends with an `<hr />` (61 in total). Print draws them as a 1.1in hairline. Here they are the browser default: a full-width, two-tone, inset rule.

**Fix:**
```css
hr{border:0;border-top:1px solid #cfcfcf;width:30%;margin:1.6em auto}
```
There are no empty headings and no doubled rules, but in all 16 chapters a rule sits directly before the plate. Once the plate has its own page, that rule is harmless.

### 5. The Part closing plates can overflow a tablet page and do not get a page of their own
The three 600x900 closing plates (end of ch5, ch11 and ch16) sit in a bare `<p>` directly under the last practice item. On a 768x1024 tablet they render 900 px tall with 1.5em margins, which leaves no room for reader chrome (`tablet-ch008-plate1.png`). Print bounds them by height and isolates them.

**Fix:** have `prep.py` give that paragraph a class (`p.closing-plate`), then:
```css
p.closing-plate{page-break-before:always;text-align:center;margin:0}
p.closing-plate img{max-height:95vh;width:auto}
```

### 6. The title page is bare, and no author is named anywhere
The title page is a left-aligned h1 with the subtitle as body text (`phone-title_page-open.png`). The OPF has no `dc:creator`, so stores and libraries will list the author as "Unknown". `book-manifest.json` does not record the author's name either, and I have not supplied one.

**Fix:** centre `.titlepage`, which pandoc emits but `epub.css` never styles:
```css
.titlepage{text-align:center;margin-top:30%}
.titlepage h1{text-align:center}
```
Pass `--metadata author="..."` once the author gives his name as it should appear (ruling). The title also needs a ruling: both cover candidates read "RIVER. OAK. SUN. / THE STOIC HUSBAND", while the ePub and the manifest say "River, Oak, Sun: The Stoic Husband".

### 7. There is no cover
**Is one needed?** Yes, for anything beyond review copies:
- Apple Books and Kindle show a generic grey tile without one.
- KDP requires a separate cover upload.
- Send-to-Kindle uses the first image if there is no cover, which here would be the Chapter 1 plate.

For a draft passed between readers it is optional.

**What it should be.** The author has two candidate directions in `books/the-stoic-husband/design/covers/`. Neither is ratified: per `source-prompt.md`, "Feedback split; both directions retained as candidates".
- **design-one:** the brown-leather "Heirloom Field Manual", gold-stamped RIVER. OAK. SUN., an oak leaf.
- **design-two:** black cloth, debossed type.

Both are 1254x1254 mock-up composites, not usable cover art. An ePub cover is a portrait image of about 1600x2560. Its type has to stay readable as a thumbnail.

I did not make one. The author needs to pick a direction first. Until he does, the honest interim is no cover, or a plain typographic cover he approves.

### 8. Contents list and heading hierarchy
- The structure is correct: Part pages are h1, chapters are h1, beats are h2. The nav has 21 flat entries and so does `toc.ncx`.
- **Issue:** Parts do not nest their chapters, so a phone reader sees one long flat numbered list with blue underlined links (`phone-nav-open.png`).
- **Fix:** add `ol.toc{list-style:none;padding:0}` and `ol.toc a{text-decoration:none;color:inherit}`. Optionally nest chapters under their Part, either by post-processing `nav.xhtml` or by building the Part pages as h1 and the chapters as h2 with `--split-level=2`.
- **Author ruling:** the Part titles "PART I — THE STEADY RIVER" carry an em-dash in the contents list, on the Part pages, and in every practice title ("Chapter 1 — The Three-Second Window"). The house rule bans em-dashes on plates and in prose. Print has the same dashes, so this is not an ePub regression; it is a question for the author.

### 9. Smaller points
- **Body text:** flush left, zero indent, `.8em` paragraph gap. This matches the house format.
- **Italics:** survive everywhere (Part epigraphs, Latin and Greek terms, practice questions).
- **Run-in labels:** "Mechanism:", "The idea in one sentence:", "Lesson:" and "Challenge:" survive as `<strong>`. They read correctly, but at full bold, where print uses 600 weight. That is acceptable.
- **Blockquotes** (ch10, ch12) use the browser default: a 40px indent on both sides, upright text and no rule, which wastes phone width. Print uses italic text with a left hairline. **Fix:** `blockquote{margin:1em 1.2em;padding-left:.8em;border-left:2px solid #d4d4d4} blockquote p{font-style:italic}`. The citation line ("*Discourses* 2.18, Long trans.") should also come out of italics in a class, as print's `cite` does.
- **Plate alt text** is "Plate, Chapter 1". Screen readers will announce nothing useful. **Fix:** alt text = the plate's title plus its one caption line, taken from the SVG.
- **Part pages** match print: left bold caps title, italic epigraph. The book's River, Oak and Sun marks (`design/marks/`) are an option for these pages, but only on the author's word, since print does not use them.
- **Landmarks** list only the title page and the contents, so Kindle's "Go to Beginning" opens on the title page. **Fix:** add a `bodymatter` landmark pointing at `ch001.xhtml`, by post-processing `nav.xhtml` or with pandoc's `epub:type` on the Prologue.
- **Tablet line length** is about 95 characters at 768 px. Readers add their own margins, so leave it.

## Kindle vs Apple Books
- **Fonts:** `com.apple.ibooks.display-options.xml` sets `specified-fonts=true`, so Apple Books honours Georgia until the reader picks another font. Kindle ignores publisher fonts unless "Publisher Font" is chosen, and falls back to Bookerly. Georgia is not embedded, and Android readers have no Georgia, so the serif fallback applies there.
- **Page breaks:** Apple Books paginates each XHTML file separately and honours `page-break-before` inside a file in paginated mode. Kindle (KF8 through Send-to-Kindle or KDP conversion) honours `page-break-before:always`, but not `break-before`, so keep both, as written above. Neither app honours `vh` everywhere. `max-height:95vh` works in Apple Books and current Kindle apps; on older e-ink Kindles it is ignored, and the image is still scaled to the screen.
- **Plates:** both apps let you double-tap a plate to zoom it full screen. On Kindle e-ink this only works for images inside a block, which they are. The thin grey lines in the ch1 to ch11 plates will look washed out on e-ink. The darker ch12 to ch16 line weights survive better.
- **Headings and colour:** Kindle drops `color` on e-ink, which is harmless. Kindle forces a first-line indent on paragraphs only when none is set; ours is set to 0, which is correct.
- **Cover:** KDP takes the cover as a separate upload and ignores an in-book cover page. Apple Books takes it from the OPF `cover-image` property (pandoc `--epub-cover-image`).

## For the author to rule on
1. Plate type size for ch1 to ch11 at phone width: accept tap-to-zoom, or revise the plates (item 2).
2. The author's name as it should appear, and the title form: colon, or "RIVER. OAK. SUN." (item 6).
3. Which cover direction, if any, before a public build (item 7).
4. Em-dashes in Part titles and practice titles (item 8).
