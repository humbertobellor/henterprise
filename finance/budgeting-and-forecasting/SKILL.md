---
name: budgeting-and-forecasting
description: "Runs the planning cycle. Annual budget, rolling forecast, consolidation of business unit inputs, and the variance analysis that explains actuals against plan. Use this to build or challenge a budget, run a forecast cycle, consolidate departmental submissions, explain why results diverged from plan, or improve forecast accuracy."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: finance
metadata:
  hermes:
    category: finance
    tags: [finance, budgeting, forecasting, variance, planning]
    related_skills: [chief-financial-officer, financial-modeling, financial-reporting-and-close]
---

# Budgeting and forecasting

The planning cycle and the analysis that explains what actually happened against it.

## When to Use

- Building or challenging a budget.
- Running a forecast cycle.
- Consolidating departmental submissions.
- Explaining why results diverged from plan.
- Improving forecast accuracy.

## Procedure

### The budget is a commitment, the forecast is a belief

Keep them separate. A budget re-cut every month is not a commitment; a forecast held to the original
budget is not a belief. Both failures make the numbers useless for different reasons.

### Running the cycle

1. **Set the frame first** — targets, headcount envelope, and the assumptions everyone builds on
   (pricing, attrition, timing). Distributed teams building on different assumptions produces a
   consolidation that cannot be reconciled.
2. **Collect in a fixed template.** Free-form submissions cost more to normalize than to build.
3. **Challenge the inputs**, specifically: what is the volume driver, what is this per unit, what
   happens if it comes in at half. Budget submissions are negotiating positions and should be
   treated as such without hostility.
4. **Consolidate and find the gap** between bottom-up and top-down. There always is one. Close it
   explicitly by cutting something named, not by proportional trimming — proportional cuts damage
   the highest-return line as much as the lowest.
5. **Publish what was not funded** and why. This prevents the same request arriving three times.

### Rolling forecast

Re-forecast on a fixed cadence over a constant horizon. Update only what has changed and say what
changed and why. A re-forecast with no narrative is a new set of numbers with no information in it.

### Variance analysis

Variance is only useful decomposed. For each material variance, separate:

- **Volume** — did the quantity change?
- **Rate** — did the price or cost per unit change?
- **Timing** — did it move between periods?
- **Mix** — did the composition shift?

Timing variances need no action and are constantly mistaken for performance. Rate variances on
recurring costs compound and are constantly under-reacted to.

Explain the top few by value, not every line. A variance report covering everything gets read as
nothing.

## Pitfalls

- Presenting a forecast without saying what changed since the last one.
- Letting a department own an assumption that drives another department's numbers.
- Closing the top-down gap by proportional trimming, which damages the highest-return line as much
  as the lowest.
- Mistaking a timing variance for performance.
- A variance report covering every line, which gets read as nothing.

## Verification

Report accuracy by measuring it. Track forecast error over time — it improves quickly once visible
and never improves while unmeasured. Every forecast states what changed since the last one and why;
every material variance is decomposed into volume, rate, timing, and mix; and the unfunded list is
published with reasons.

## Related

- `enterprise/finance/chief-financial-officer` — owns the budget of record.
- `enterprise/finance/financial-modeling` — the driver logic underneath the plan.
- `enterprise/finance/financial-reporting-and-close` — the actuals the variance is measured against.
