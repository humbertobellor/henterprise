---
name: solution-architecture
description: "Designs system structure and records the why. Boundaries, coupling, trade-offs, and decisions that survive the people who made them. Use this to design a new system or major component, choose between architectural options, review an existing design, decide where a boundary belongs, or document an architectural decision so it survives the people who made it."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: technology
metadata:
  hermes:
    category: technology
    tags: [technology, architecture, boundaries, trade-offs, decision-records]
    related_skills: [chief-technology-officer, solution-exploration, api-design, threat-modeling, cloud-infrastructure]
---

# Solution architecture

Architecture is the set of decisions that are expensive to reverse. Everything cheap to change later
is design, and does not need this level of ceremony.

## When to Use

- Designing a new system or major component.
- Choosing between architectural options.
- Reviewing an existing design.
- Deciding where a boundary belongs.
- Documenting an architectural decision so it survives the people who made it.

## Procedure

### Start from what constrains, not from what appeals

Architecture is driven by quality attributes, not by features. Establish the ones that actually bind
before drawing anything: expected load and its shape, latency the user notices, availability the
business will fund, data residency and retention obligations, the rate of change the team needs to
sustain, and the size and skills of the team who will operate it.

Vague attributes produce vague architecture. "Scalable" is not a requirement; "20,000 concurrent
sessions with p99 under 300ms" is a constraint that eliminates options.

### Boundaries are the whole game

Draw boundaries where change is independent and where data has a single owner. A boundary in the
right place absorbs change; a boundary in the wrong place turns every feature into a negotiation
across three teams.

The reliable test: if a routine change requires coordinated deployment across two components, the
boundary is wrong regardless of how clean the diagram looks.

Prefer coarse boundaries until you have evidence for finer ones. Distributed systems convert simple
in-process failures into network, partial-failure and consistency problems — a cost worth paying for
independent scaling or independent deployment, and not worth paying for tidiness.

### Trade-offs, stated

Every architecture sacrifices something. The failure is not choosing badly; it is choosing without
naming what was given up, so nobody later understands why the constraint exists.

Present options with their costs: what each makes easy, what each makes hard, what it costs to
operate, and what it would take to reverse. Two credible options and an honest comparison beat one
recommendation.

### Record decisions

Write down the decision, the context at the time, the options considered, and the consequences
accepted. Architecture rots because the reasoning evaporates while the structure remains, and the
next team reads a constraint as an accident.

Keep records short and immutable — supersede rather than edit, so the history of thinking survives.

## Pitfalls

- Designing against quality attributes nobody has quantified.
- Splitting a system into services to make the diagram tidy.
- Presenting a single option as though no trade-off was made.
- Leaving an expensive-to-reverse decision undocumented.
- Editing a decision record instead of superseding it, which erases the history of thinking.

## Verification

Apply the boundary test to the design as drawn: does any routine change require coordinated
deployment across two components? If so the boundary is wrong, regardless of how clean the diagram
looks.

Check every quality attribute is quantified — a number and a percentile, not an adjective — and that
the decision record names the options considered and the consequences accepted, not only the choice.

## Related

- `enterprise/technology/solution-exploration` — the option generation before this.
- `enterprise/security/threat-modeling` — the boundaries examined for attack.
- `enterprise/technology/api-design` — how the boundaries are expressed.
