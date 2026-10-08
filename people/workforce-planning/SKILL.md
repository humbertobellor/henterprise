---
name: workforce-planning
description: "Plans the shape and size of the workforce. Demand for roles, build-versus-buy, attrition, and sequencing hiring against budget. Use this to build a hiring plan, decide which roles to open and in what order, model attrition and backfill, plan for a growth or contraction scenario, or connect headcount plans to the budget."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: people
metadata:
  hermes:
    category: people
    tags: [people, workforce-planning, headcount, attrition, sequencing]
    related_skills: [org-design, hiring-and-interviewing, budgeting-and-forecasting, learning-and-development, capacity-and-demand-planning]
---

# Workforce planning

A hiring plan is an org design decision spread over twelve months and a large financial commitment
made in small pieces. It deserves the scrutiny of both.

## When to Use

- Building a hiring plan.
- Deciding which roles to open and in what order.
- Modeling attrition and backfill.
- Planning for a growth or contraction scenario.
- Connecting headcount plans to the budget.

## Procedure

### Plan capability, not headcount

Headcount is an input. Start from what the organization must be able to do that it currently cannot,
then work out what closes the gap — hiring, developing existing people, contracting, or not doing the
work.

The shape follows from `enterprise/people/org-design`; this is about sequencing and quantity over
time, funded against `enterprise/finance/budgeting-and-forecasting` on fully loaded cost rather than
salary. Salary is typically well under the true cost, and plans built on it are wrong by a wide and
consistent margin.

### Sequence matters more than total

Twelve hires in a year is not one number; it is twelve dated decisions with dependencies.

- **Hire the people who make other hires productive first.** A manager, a lead, or the person who can
  onboard the next five. Hiring five juniors before the person who will develop them wastes most of
  the investment.
- **Respect absorption capacity.** An organization can only integrate so many people at once before
  onboarding quality falls and existing output drops. Growth past that rate makes things slower for
  a quarter, reliably.
- **Front-load long-lead roles.** Scarce skills take months to find. Plotting them at the same lead
  time as abundant ones is how plans silently slip.

### Attrition is a planning input

Some attrition is expected and healthy; the planning error is treating it as noise. Model it by
segment — teams, levels and tenure bands differ substantially — and plan backfill lead time from the
resignation date, not the leaving date.

### Scenarios, including down

Plan the base case, the growth case and the contraction case. Knowing in advance what you would stop
doing, and which commitments are hard to reverse, is what makes a downturn a decision rather than a
scramble.

Offers, notice periods and some contractor arrangements are commitments before anyone starts. Know
which parts of the plan can still be unwound and by when.

## Pitfalls

- Building a plan on salary rather than fully loaded cost.
- Hiring faster than the organization can absorb and expecting output to rise.
- Treating attrition as a residual instead of a modeled input.
- Reporting aggregate attrition without looking at it by team and by manager.
- Plotting long-lead and abundant roles at the same lead time.
- Hiring juniors before the person who will develop them.

## Verification

Watch **regretted** attrition specifically, and by manager. Aggregate attrition looks fine while one
team is bleeding people, and the aggregate is what gets reported.

Report the plan as dated decisions with dependencies and lead times, on fully loaded cost, with the
absorption rate stated. For each scenario, name which commitments can still be unwound and by when —
that list is what turns a downturn into a decision.

## Related

- `enterprise/people/org-design` — the shape this sequences.
- `enterprise/finance/budgeting-and-forecasting` — where fully loaded cost is funded.
- `enterprise/operations/capacity-and-demand-planning` — throughput rather than shape.
