---
name: capital-allocation
description: "Evaluates where to spend limited capital. Investment appraisal, hurdle rates, payback, and comparing proposals that are not alike. Use this to evaluate an investment or major purchase, compare competing funding requests, set a hurdle rate, decide between building and buying, or review whether past investments delivered what was claimed."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: finance
metadata:
  hermes:
    category: finance
    tags: [finance, investment-appraisal, npv, hurdle-rate, payback]
    related_skills: [chief-financial-officer, financial-modeling, portfolio-strategy]
---

# Capital allocation

Choosing among investments is choosing what not to do. This is the appraisal of individual
proposals; which businesses and bets the company should be in belongs to
`enterprise/corporate-strategy/portfolio-strategy`.

## When to Use

- Evaluating an investment or major purchase.
- Comparing competing funding requests.
- Setting a hurdle rate.
- Deciding between building and buying.
- Reviewing whether past investments delivered what was claimed.

## Procedure

### Appraise on incremental cash

Only cash flows that change because of the decision belong in the analysis:

- **Sunk costs are irrelevant.** Money already spent is not a reason to continue, though it is
  reliably presented as one.
- **Allocated overhead is usually irrelevant.** If the cost occurs anyway, it does not belong in the
  incremental case.
- **Opportunity cost is relevant**, including the capacity consumed that then cannot serve anything
  else.
- **Working capital is a real outflow.** Growth that consumes cash is not free because it is growth.

Discount for time and risk. A hurdle rate should reflect the risk of the specific proposal — applying
one company-wide rate systematically overfunds risky projects and starves safe ones.

### Read payback for what it tells you

Payback ignores everything after the threshold and so is a poor ranking tool. It is a good *liquidity
and uncertainty* measure: how long capital is at risk, and how far into an uncertain future the case
depends on.

Use net present value to decide, payback to understand exposure. A proposal with strong NPV whose
returns all arrive in years four and five is a forecasting question as much as an investment one.

### Interrogate the case, not the sponsor

Every proposal arrives advocated for. The useful questions are structural:

- What has to be true for this to work, and which of those is least certain?
- What is the counterfactual — what happens if we do nothing?
- Where is the optionality: can it be staged so a small commitment buys information before the large
  one?
- Who is accountable for the benefit after approval?

Stage-gating dominates all-or-nothing commitment where uncertainty is high. Paying for information
first is usually cheaper than being right by luck.

## Pitfalls

- Including sunk cost in a forward case.
- Applying one hurdle rate to proposals of different risk.
- Ranking by payback.
- Approving a benefit with no owner after approval.
- Comparing proposals on pre-tax returns. After-tax returns are the only ones that matter.

## Verification

Look back, or the numbers stay fictional. Compare realized outcomes against the approved case, and
make it routine rather than punitive. Where nobody looks back, forecasts drift optimistic because
optimism is rewarded at approval and never tested afterwards.

Report the incremental case with sunk costs excluded, the risk-adjusted hurdle used and why, NPV as
the decision basis with payback stated as exposure, the named owner of the benefit, and the date the
look-back happens.

## Related

- `enterprise/corporate-strategy/portfolio-strategy` — which businesses to be in at all.
- `enterprise/finance/financial-modeling` — the model behind the case.
- `enterprise/finance/tax` — after-tax returns are the only ones that matter.
