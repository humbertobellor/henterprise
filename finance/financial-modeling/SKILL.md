---
name: financial-modeling
description: "Builds and stress-tests financial models. For forecasting, scenario planning, and decision support - revenue build, cost structure, driver logic, and the sensitivities that show where a plan breaks. Use this to model a decision's financial consequence, build a forecast or long-range plan, evaluate an investment or hire, or pressure-test someone else's model before relying on it."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: finance
metadata:
  hermes:
    category: finance
    tags: [finance, modeling, sensitivity, forecasting, drivers]
    related_skills: [chief-financial-officer, budgeting-and-forecasting, unit-economics, capital-allocation]
---

# Financial modeling

A model is an argument about how the business works, expressed in arithmetic. Its value is the
argument, not the output precision.

## When to Use

- Modeling a decision's financial consequence.
- Building a forecast or long-range plan.
- Evaluating an investment or a hire.
- Pressure-testing someone else's model before relying on it.

## Procedure

### Structure

Three separated layers, always:

1. **Inputs** — every assumption, in one place, each with a source and a date. An assumption buried
   inside a formula is invisible and therefore never challenged.
2. **Calculations** — no hard-coded numbers. Ever. A constant inside a formula is an untraceable
   assumption.
3. **Outputs** — the statements and the summary a decision-maker actually reads.

One row, one calculation, carried consistently across periods. Models become unauditable through
inconsistent rows more than through complexity.

### Build revenue from drivers

Never grow a top-line by a percentage. Build it: volume × price, or accounts × retention ×
expansion. Driver-based models can be argued with, and being argued with is the point — a growth
rate cannot be wrong, only optimistic.

Cost structure separated into fixed, variable, and step-fixed. The step-fixed items are where plans
break, because they move in jumps nobody modeled.

### Sensitivities are the deliverable

A single-scenario model tells you nothing about risk. For every model, produce:

- **Which two or three assumptions actually move the answer.** Usually far fewer than expected.
- **Breakeven on each** — how wrong can this be before the decision reverses?
- **Downside case** — not a haircut on the base case, but a coherent story where things go badly.

If a plan only works in the base case, that is the finding.

### Presenting

Lead with the answer, then the two assumptions it rests on most heavily, then what would change it.

## Pitfalls

- Reporting a number to more precision than the assumptions support. Five significant figures from a
  guessed growth rate is false confidence.
- Building a model whose logic you cannot explain in three sentences.
- Changing an assumption to reach a desired output without labeling it as a target case.
- Hard-coding a constant inside a formula, which is an untraceable assumption.
- Growing a top line by a percentage. A growth rate cannot be wrong, only optimistic.
- A downside case that is a haircut on the base case rather than a coherent story.

## Verification

Never present a model without stating what it is most sensitive to — the recipient will assume
robustness you did not claim. The deliverable is not the output: it is the two or three assumptions
that move the answer, the breakeven on each, and a downside case that hangs together. If the plan
only works in the base case, say so as the finding.

## Related

- `enterprise/finance/budgeting-and-forecasting` — the plan this model feeds.
- `enterprise/finance/unit-economics` — the per-unit logic underneath the revenue build.
- `enterprise/corporate-strategy/scenario-planning` — the non-financial version of the same discipline.
