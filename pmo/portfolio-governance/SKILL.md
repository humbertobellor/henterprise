---
name: portfolio-governance
description: "Governs the portfolio of work. Intake, prioritization, stage gates, resource contention, and stopping things. Use this to set up intake and prioritization, run a stage gate, decide between competing initiatives, resolve resource contention across projects, or work out why everything is in flight and nothing is finishing."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: pmo
metadata:
  hermes:
    category: pmo
    tags: [pmo, portfolio, intake, stage-gates, work-in-progress]
    related_skills: [head-of-pmo, capacity-and-demand-planning, benefits-realization, dependency-and-risk-management, portfolio-strategy]
---

# Portfolio governance

The portfolio question is not which projects are good. Most proposed work is defensible in isolation.
It is which projects the organization can actually finish, given that finishing is what produces
value and starting produces none.

## When to Use

- Setting up intake and prioritization.
- Running a stage gate.
- Deciding between competing initiatives.
- Resolving resource contention across projects.
- Working out why everything is in flight and nothing is finishing.

## Procedure

### Intake as a real gate

Without a single front door, work enters through relationships and volume, and the portfolio becomes
the sum of who asked most persistently.

Require the same minimum from every proposal regardless of who is asking: the outcome sought, the
evidence it matters, a rough size, the accountable owner, and what will not happen if it proceeds.
That last one is the honest part — capacity is fixed, so approving anything is declining something
else, whether or not the decline is ever stated.

### Prioritize against capacity, not against merit

Ranking by value produces a list where everything above the line is approved and the line is
imaginary. Prioritization only means something when the cut is made at real, measured delivery
capacity — see `enterprise/operations/capacity-and-demand-planning` for the throughput side.

**Limit work in progress.** An organization running twenty concurrent initiatives with capacity for
eight does not deliver twenty slowly; it delivers roughly eight, considerably later, with the
overhead of context-switching across all twenty. Fewer things, finished, is faster in wall-clock
terms — which is counter-intuitive and is why the discipline requires governance rather than good
intentions.

### Stage gates that can say no

A gate whose only outcome is approval is a status meeting. Each gate must be able to stop, pause, or
redirect, and needs a named decision-maker with the authority to do it.

Gate on what has been learned since the last one, not on whether documentation was produced. The
useful question is whether the case still holds now that more is known — and it frequently does not,
which is exactly the information the gate exists to surface.

### Stopping is the hardest and most valuable act

Organizations start well and stop badly. Sunk cost, sponsor prestige and the discomfort of admitting
error keep dead projects consuming capacity that the whole portfolio needs.

Make stopping a normal, non-punitive outcome. Where stopping is treated as failure, projects are
never stopped — they are quietly starved, which is the same cost with none of the released capacity
and no decision anyone can point to.

### Resource contention

Contention across projects is resolved here, at the portfolio, not by the projects negotiating among
themselves. Left to negotiation, the outcome reflects seniority of the sponsors rather than value to
the organization.

Watch for the same scarce specialist appearing on the critical path of several initiatives — the
most common invisible cause of portfolio-wide slippage.

## Pitfalls

- Approving work without naming what it displaces.
- Setting a priority order without a line drawn at real capacity.
- Running a gate that cannot stop anything.
- Starving a project instead of stopping it.
- Letting projects negotiate resource contention among themselves.
- Gating on whether documentation was produced rather than on what has been learned.

## Verification

The honest test of the portfolio is the count of things stopped and the work-in-progress number
against measured capacity — not the size of the approved list. Report both, plus every scarce
specialist appearing on more than one critical path.

For each approval, the record states what it displaced. If nothing was displaced, capacity was not
the basis for the decision.

## Related

- `enterprise/operations/capacity-and-demand-planning` — the throughput number the line is drawn at.
- `enterprise/corporate-strategy/portfolio-strategy` — which businesses to be in, a different question.
- `enterprise/pmo/benefits-realization` — what the gate should be checking against later.
