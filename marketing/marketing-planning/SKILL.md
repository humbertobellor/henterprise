---
name: marketing-planning
description: "Builds the marketing plan of record. Objectives, channel mix, budget allocation, sequencing, and the measurement that says whether it worked. Use this for annual or quarterly planning, when budget must be allocated or defended, when marketing activity feels busy but undirected, or when a plan needs pressure-testing before commitment."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: marketing
metadata:
  hermes:
    category: marketing
    tags: [marketing, planning, budget, channel-mix, kill-criteria]
    related_skills: [chief-marketing-officer, marketing-campaign-planner, positioning-and-messaging, marketing-analytics]
---

# Marketing planning

The plan of record: objectives, channel mix, budget, sequencing, and how you will know. For a
bounded push around one story, use `enterprise/marketing/marketing-campaign-planner` instead.

## When to Use

- Annual or quarterly planning.
- Budget must be allocated or defended.
- Marketing activity feels busy but undirected.
- A plan needs pressure-testing before commitment.

## Procedure

### Start from the constraint, not the calendar

Name the single thing limiting growth right now: not enough people know, not enough of the right
people know, they know but do not believe, they believe but do not act, or they act but do not stay.
Each implies a different plan. A plan that funds all five funds none properly.

### Structure

1. **Objective** — one primary number with a date. Supporting metrics are supporting.
2. **The constraint** and the evidence for it.
3. **Segments** — who, in priority order, and who is explicitly out of scope this period.
4. **Channel mix** — three tiers:
   - **Proven** — working now; fund to capacity, then stop. Most channels have a ceiling and
     spending past it buys worse customers.
   - **Scaling** — evidence but not yet at capacity; the growth budget.
   - **Experimental** — capped at a share you can lose entirely without missing the objective.
5. **Sequencing** — what has to be true before each thing starts. Content before paid, positioning
   before content.
6. **Budget** — by tier and channel, with the fixed-versus-variable split visible.
7. **Measurement** — the leading indicator per channel and when it should first move. A channel with
   no stated read-by date runs forever.
8. **Kill criteria** — what result stops each experiment. Decided in advance, when it is cheap.

## Pitfalls

- Planning channel activity before positioning is settled.
- Funding an experiment you cannot afford to have fail.
- Reporting a plan without stating what did not get funded and why.
- Funding all five constraints, which funds none properly.
- Spending past a proven channel's ceiling, which buys worse customers.
- A channel with no read-by date, which runs forever.

## Verification

Pressure-test before committing:

- What must be true for this to work, and which of those is least certain?
- What happens at half the budget? If the plan collapses, it has no core.
- Which line item would you cut first? If nothing, the plan is not prioritized.
- Where does this depend on another team delivering, and have they agreed?

Report the plan with the constraint and its evidence, the three-tier channel mix with budget, the
leading indicator and read-by date per channel, the kill criteria decided in advance, and what did
not get funded and why.

## Related

- `enterprise/marketing/chief-marketing-officer` — owns budget allocation.
- `enterprise/marketing/positioning-and-messaging` — must be settled before channel activity.
- `enterprise/demand-generation/marketing-analytics` — where the leading indicators are measured.
