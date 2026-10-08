---
name: project-delivery
description: "Plans and delivers a single project. Scope, estimation, scheduling, critical path, tracking, and recovering when it slips. Use this to plan a project, build or challenge a schedule, estimate credibly, track progress meaningfully, or recover a project that is late."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: pmo
metadata:
  hermes:
    category: pmo
    tags: [pmo, project-management, estimation, critical-path, recovery]
    related_skills: [program-management, dependency-and-risk-management, head-of-pmo, implementation-planning]
---

# Project delivery

A project is one bounded piece of work with an end. Coordinating several toward a shared outcome is
`enterprise/pmo/program-management`.

## When to Use

- Planning a project.
- Building or challenging a schedule.
- Estimating credibly.
- Tracking progress meaningfully.
- Recovering a project that is late.

## Procedure

### Scope by exclusion

Inclusions are agreed easily and understood differently. The exclusions do the work: what this
project will *not* deliver, written down and acknowledged by the sponsor.

Unwritten exclusions return as assumptions, always late, always framed as something obviously
included. Fixing that at the end is called scope creep; it is usually a documentation failure at the
start.

### Estimate as a range, and say what the range means

A single-point estimate is a forecast presented as a commitment. Give a range with the assumptions
that would move it, and be explicit about confidence.

Estimate the work, not the desired date. Estimates negotiated downward do not change the work; they
change when you find out, and the finding-out happens at the least recoverable moment.

Decompose until the pieces are comprehensible. Estimating a large unknown produces a number
correlated with optimism rather than with the work.

### The critical path is where attention belongs

Not everything late matters. Slippage on the critical path moves the end date; slippage elsewhere
consumes float. Knowing which is which is the difference between useful concern and generalised
anxiety.

Recalculate as things change — the critical path moves, and a team watching the original one is
watching the wrong thing.

Hold buffer at the project level rather than padding each task. Padded tasks absorb their own buffer
and deliver no earlier, because work expands and nobody reports finishing early.

### Recovery

Diagnose first, since remedies do not overlap: scope larger than understood, capacity lower than
planned, dependencies not delivering, or an estimate that was never realistic.

Then present options with consequences — cut scope and name what, extend and say by how much, or add
capacity, which late in a project usually slows things further. Re-baseline once, visibly. Serial
one-week slips destroy credibility far faster than a single honest reset.

## Pitfalls

- Agreeing scope without written exclusions.
- Presenting a single-point estimate as a commitment.
- Reporting progress as percentage complete.
- Adding people to a late project and expecting it to accelerate.
- Padding each task instead of holding buffer at the project level.
- Watching the original critical path after it has moved.

## Verification

Track completion, not effort. Percentage complete is self-reported optimism, and it famously stalls
at 90%. Track binary completion of defined deliverables — done or not done, judged against a
definition agreed in advance.

Watch the trend: whether the amount remaining is falling at the rate required. A project where
remaining work is not decreasing is a project that is late, whatever the reported percentage.

## Related

- `enterprise/pmo/program-management` — several projects toward one outcome.
- `enterprise/pmo/dependency-and-risk-management` — what could stop it.
- `enterprise/technology/implementation-planning` — the engineering-side plan.
