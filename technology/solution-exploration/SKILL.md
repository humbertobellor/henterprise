---
name: solution-exploration
description: "Explores the problem before any code is written. Clarifying what is actually being asked, surfacing options with their tradeoffs, and converging on one. Use this at the start of any feature, component, or behavior change, when a request is ambiguous, when the first idea is the only idea on the table, or when a design decision needs pressure-testing before commitment."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: technology
metadata:
  hermes:
    category: technology
    tags: [technology, exploration, options, requirements, convergence]
    related_skills: [solution-architecture, implementation-planning, chief-technology-officer, ceo-advisor]
---

# Solution exploration

The most expensive bugs are decisions, not defects. This runs before implementation, not instead of
it.

## When to Use

- At the start of any feature, component, or behavior change.
- A request is ambiguous.
- The first idea is the only idea on the table.
- A design decision needs pressure-testing before commitment.

## Procedure

### Establish what is actually wanted

The stated request is a proposed solution wearing the clothes of a requirement. Get underneath it:

- What outcome does the person want? What breaks today without it?
- Who else touches this, and what do they assume about it now?
- What is explicitly **not** being asked for?
- How will we know it worked — the observable difference.

If the answers conflict, stop and resolve that first. Building the average of two requirements
satisfies neither.

### Generate genuinely different options

Two variations of the same idea are one option. Force real range:

- The smallest thing that could work.
- The version that assumes this doubles in scope next quarter.
- The version that requires no new moving parts.
- Buy, borrow, or do nothing.

For each: what it costs, what it forecloses, and what has to be true for it to be right.

### Converge

Recommend one and say why the others lost. A comparison that ends without a recommendation has
moved the work, not done it.

Name the assumption the recommendation rests on most heavily — that is where the plan will break if
it breaks.

## Pitfalls

- Presenting options you would not accept, as padding around the one you want.
- Skipping this because the task "is simple." Simple tasks take five minutes here.
- Letting a preference stand in for a reason.
- Two variations of one idea presented as two options.
- Building the average of two conflicting requirements, which satisfies neither.
- Ending without a recommendation, which moves the work rather than doing it.

## Verification

The output is checkable: the outcome wanted and what breaks without it, what is explicitly out of
scope, the observable difference that will show it worked, genuinely distinct options with costs and
what each forecloses, one recommendation with the reasons the others lost, and the assumption it
rests on most heavily.

If any of those is missing, the exploration is not finished — and the missing one is usually the
assumption.

## Related

- `enterprise/technology/solution-architecture` — where the chosen option becomes structure.
- `enterprise/technology/implementation-planning` — turning the choice into ordered steps.
- `enterprise/executive/ceo-advisor` — the same interrogation applied to a business decision.
