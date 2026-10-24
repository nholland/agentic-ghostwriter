# Chapter 15 conformance, round 2 (gw-specchecker, clean room)

2026-10-24 03:57. Inputs: the outline section and the round-2 prose cut (1,381 raw words). Nothing else.
Round 1 is `runs/ch15/conformance.md`. The checker split the spec into 51 rows; 44 PASS, 7 FAIL, 9 attribution findings.
PASS rows 1-20, 22, 24-28, 30-32, 34-38, 41-50 are the checker's, with its quoted evidence, and are not repeated here.

## FAIL rows, verbatim from the checker, with the Publisher's disposition

| Row | Checker | Disposition |
|---|---|---|
| 21 | "The ceiling, the sun." FAIL. The prose never uses "sun", "ceiling", "Oak" or "Sun" ... can't tell whether the word must appear. | **Declared**, deviation (c): the sun does not appear (brief section L). Verdict. |
| 23 | "Most husbands have only checked the floor." FAIL. Missing. | **Declared**, deviation (g). Verdict. |
| 29 | No detail beyond what he has given. FAIL. Lists "Saturday mornings", "busy weekends", "wakes up with", "sitting down talking to the kids", "asking for the status of things", "frustrated ... things to do", "maybe she isn't in a good mental state". | **Checker blind spot.** All are his own words (interview D21, D22, D24, D8; brief section C). "Saturday mornings" is also declared (f). No action. |
| 33 | Seneca, De Beneficiis II.1-2: second line "a man gives too late who gives what he has been asked for" missing. | **Declared**, deviation (d): Ch12 already prints "She can ask. She shouldn't have to ask for everything." Verdict. |
| 39 | At most two research clauses: neither is a clause. Gordon is three sentences; Impett a sentence plus two. | **Stuck, for the author.** Round 1 shortened each to one finding sentence plus his reading; the spec says "clauses". Verdict. |
| 40 | Gordon et al. 2022 for "relief plus appreciation": the prose gives a different finding. | **Stuck, for the author.** The spec's gloss and the researched finding differ (unfair split plus lower satisfaction, except where appreciated). The prose follows the researched finding. The spec wording needs a ruling; inbox item filed. |
| 51 | Transition to Ch16 missing second half. | **Declared**, deviation (n). Verdict. |

## Attribution findings (9), Publisher's routing

1-3 (Seneca De Ira, De Beneficiis, Marcus I.9): the quotations run past the spec's excerpt because the Researcher read the passages primary; the checker has only the spec. Fact-Checker queue (inbox #150) already carries them; the author checks his copy.
4 (glosses on philostorgia and "free from passion"): Fact-Checker.
5-6 (Gordon, Impett): finding wording is the brief's may-say; Fact-Checker. Impett's dating-to-marriage jump is real; the prose already names the Gordon scope gap and could name this one at refine.
7 ("right or married" origin): by design, first printing, "I tell people"; inbox 155.
8 ("you use what rewards"): the author's own, D4.
9 (Ch14 claim): checked by grep, `runs/ch14/refined.md` line 17: "Name something true about her, and stay with it long enough to remember why you value it." The Ch15 line is a fair paraphrase; the Line Editor should keep it close to that wording.

## Gate state

Round 2 of 2 used. Every remaining FAIL is a declared deviation, a checker blind spot, or a ruling only the author can give. No third Ghostwriter pass. Next: `/gw-refine 15`.
