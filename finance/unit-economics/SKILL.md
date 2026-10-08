---
name: unit-economics
description: "Establishes whether you make money on each customer. Contribution margin, acquisition cost, payback period, lifetime value, and the cohort behavior underneath. Use this to assess whether growth is profitable, evaluate a channel or segment, support a pricing decision, judge how fast the business can afford to grow, or diagnose why revenue growth is not producing profit."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: finance
metadata:
  hermes:
    category: finance
    tags: [finance, unit-economics, cac, ltv, payback, cohorts]
    related_skills: [chief-financial-officer, financial-modeling, business-growth-consultant, pricing-and-packaging]
---

# Unit economics

The question is simple and usually unanswered: does one more customer make the business better off,
and how long does that take?

## When to Use

- Assessing whether growth is profitable.
- Evaluating a channel or segment.
- Supporting a pricing decision.
- Judging how fast the business can afford to grow.
- Diagnosing why revenue growth is not producing profit.

## Procedure

Build it in this order:

1. **Define the unit.** A customer, an account, a seat, an order. State it, because most
   disagreements about unit economics are disagreements about the unit.
2. **Contribution margin** — revenue per unit minus the costs that vary with it. Include everything
   that actually varies: payment processing, hosting attributable to usage, support load, delivery,
   third-party fees. Understating variable cost is the single most common error and it flatters
   everything downstream.
3. **Acquisition cost** — fully loaded. All sales and marketing spend, including salaries, divided
   by customers acquired in the same period. Excluding people costs is the second most common error
   and typically understates by half or more.
4. **Payback period** — acquisition cost divided by monthly contribution. This is the number that
   governs how fast you can grow without financing it.
5. **Lifetime value** — contribution × expected lifetime, from observed retention. Not from a
   churn-rate assumption chosen because it produces a good ratio.

### Read it honestly

- **Ratios hide the constraint.** A healthy lifetime-value ratio with a long payback still means
  growth consumes cash faster than it produces it. Payback governs the growth rate; the ratio
  governs whether it is worth doing at all.
- **Segment before concluding.** Blended economics almost always conceal one segment subsidizing
  another. The average is the least useful number.
- **Use cohorts, not averages.** Retention improves or decays over time, and blended figures mask
  which. If early cohorts retain better than recent ones, the business is deteriorating while the
  average looks stable.
- **Do not extrapolate lifetime beyond your data.** A twelve-month-old company cannot observe a
  three-year lifetime, and assuming one is how unprofitable businesses appear profitable.

### What it should change

Good unit economics by segment tell you where to spend. Bad ones tell you to fix the model before
scaling — no acquisition efficiency rescues a negative contribution margin, it only reaches the
loss faster.

## Pitfalls

- Comparing acquisition cost against revenue rather than contribution.
- Reporting lifetime value without stating the retention data behind it and its observation window.
- Treating improving ratios as progress without checking whether the mix simply shifted.
- Understating variable cost, which flatters everything downstream.
- Excluding salaries from acquisition cost, which typically understates it by half or more.
- Extrapolating lifetime beyond the observation window.

## Verification

State the unit explicitly, then report contribution margin, fully loaded acquisition cost, payback,
and lifetime value **by segment and by cohort** — never blended. Name the observation window behind
the retention figure and refuse to extrapolate past it. Where the mix shifted, say so, or an
improving ratio will be read as progress.

## Related

- `enterprise/executive/business-growth-consultant` — the economics stage of the growth chain.
- `enterprise/revenue/pricing-and-packaging` — the lever that moves contribution.
- `enterprise/finance/financial-modeling` — where these drivers feed the plan.
