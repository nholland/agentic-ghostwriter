---
id: 097
status: open
raised_by: Publisher
chapter: 9
opened: 2026-09-23 06:53
---

# Repair the Chapter 4 repair reference and Chapter 8–9 promise/callback mismatch?

Affected scope: Ch4, Ch8, Ch9; current outline Ch17 destination. User explicitly deferred these findings: "Add the consistency items to the inbox, we can address those later." This is a later author-ruling backlog only. No manuscript changes are authorized now; this item does not block Chapter 13. Evidence below is the exact review-report excerpt, not a claim of a new independent manuscript audit.

**Recommendation:** Point Ch4 to the repair chapter (currently Ch17); narrow Ch8's promise to self-silencing and unspoken repayment, and make Ch9's claim stand directly instead of crediting nonexistent Ch8 analysis. Record temperament asymmetry for an author placement decision.

**Checked:**

```
$ sed -n '28,35p' runs/ch13/slop-coherence-ch01-ch13.md
### 4. High — promised mechanism missing from the claimed chapter, Ch8 / Ch9

Exact: Ch8 line 53, “It isn't about labor or money or recognition. It's about temperament, how much of the emotional room in the house one of you takes up at any given moment. The next chapter takes that one on.” Ch9 line 51, “Chapter 8 already showed you what happens when the calmer person in a marriage never says what they think.” Ch8 never delivered that analysis. Ch9 mainly delivers unspoken reciprocity and self-silencing, then asserts that the analysis already happened. **Fix:** replace Ch8's promise with “The next chapter looks at what happens when you stay quiet and expect something back.” Replace the Ch9 backward claim with a direct, scoped statement: “If you keep your concerns to yourself, the decisions can end up reflecting only what she has said.” Author should decide whether the separate temperament-asymmetry OKF deserves restoration elsewhere.

### 5. High — repair chapter reference is stale, Ch4 / current outline

Exact Ch4 line 97: “What's already in the fence is Chapter 16's work.” Current outline assigns repair to Chapter 17; Chapter 16 now concerns partnership. **Fix:** reference “the chapter on repair,” or update to 17 if numbered references remain house style. This is not a Ch13 defect.

$ sed -n '61,70p' runs/ch13/persona-coherence-ch01-ch13.md
### 6. Two definite broken callbacks and one drifting physical metaphor undermine the chapter-at-a-time reader

**Personas:** continuity editor; Paul. **Scope:** older-book mechanical/local fixes. **Severity:** medium.

- Chapter 4 ends “What's already in the fence is Chapter 16's work.” Repair now belongs to Chapter 17; Chapter 16 is warmth/armor. Use the correct chapter/title.
- Chapter 9 says “Chapter 8 already showed you what happens when the calmer person in a marriage never says what they think.” Landed Chapter 8 does not show that mechanism; it only forecasts temperament unfairness at its end. Remove the false retrospective or make the point stand on its own.
- Chapter 4's nails are harmful outbursts; apology removes the nail but leaves a hole. Chapter 5's “trigger with the nail in it” makes the nail an existing wound, then says “An apology will end the fight. The nail will stay in.” The reader is asked to carry one image whose referent and apology mechanics change. Preserve the two different ideas in plain language rather than extending the same object across them.

Most other callbacks work: Chapter 2 restates the gap, Chapter 5 restates the Four D's, Chapter 11 distinguishes its decision-to-speak from Chapter 5's conduct-inside-conflict. Chapter 13 does not require obscure terminology recalled from weeks earlier.
```

**What unblocks this:** Author approval of callback corrections and disposition of the temperament-asymmetry promise. Deferred; Chapter 13 can proceed.
