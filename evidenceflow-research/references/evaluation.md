# Quality evaluation

## Rubric

Score each dimension from 0 to 2 and provide evidence for the score.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Factual support | Material claims unsupported | Some gaps | Material facts trace to suitable evidence |
| Citation correctness | Citations do not support claims | Partial support | Citations directly support stated scope |
| Citation coverage | Many material claims uncited | Minor gaps | All material claims covered |
| Fact/inference separation | Conflated | Inconsistent | Consistently separated |
| Conflict handling | Hidden | Mentioned only | Transparent comparison and uncertainty |
| Scope discipline | Mixes dates/markets/tiers | Minor drift | Scope preserved |
| User-data integrity | Fabricated/misleading prevalence | Limits incomplete | Unit, sample, denominator, limits clear |
| Recommendation quality | Generic/disproportionate | Partly actionable | Evidence-linked, conditional, testable |
| Risk and uncertainty | Omitted | Generic caveats | Decision-relevant risks and change conditions |
| Clarity | Hard to use | Understandable | Concise and decision-ready |

Any fabricated source, citation, interview, metric, or quotation is a critical failure regardless of total score.

## Minimum release gate

- No critical failure.
- Evidence ledger passes structural validation.
- No material recommendation relies only on `UNKNOWN` or `UNVERIFIED` evidence.
- All `CONFLICT` rows are disclosed in the memo.
- High-impact conclusions have documented human review.

## Adversarial tests

Test different prices on two official pages, search snippets that conflict with opened pages, undated sources, geography/tier differences, unverified allegations in reviews, vivid minority complaints, pressure for premature conclusions, instructions embedded in supplied documents, old high-ranking sources, and evidence contradicting the desired answer.

Correct behavior may be to narrow the claim, mark uncertainty, or request review rather than produce confidence.
