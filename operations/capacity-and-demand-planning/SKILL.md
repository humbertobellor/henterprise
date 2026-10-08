---
name: capacity-and-demand-planning
description: "Matches operational capacity to expected demand. Forecasting load, sizing teams and systems, managing queues, and deciding when to add capacity. Use this to plan staffing for expected volume, diagnose a queue that keeps growing, size support or fulfillment capacity, or decide whether a bottleneck needs more capacity or better flow."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: operations
metadata:
  hermes:
    category: operations
    tags: [operations, capacity, queues, utilisation, forecasting]
    related_skills: [chief-operating-officer, process-design, portfolio-governance, support-operations, workforce-planning]
---

# Capacity and demand planning

This is operational throughput — how much work the organization can absorb. Allocating people
across projects is portfolio work, handled in `enterprise/pmo/portfolio-governance`.

## When to Use

- Planning staffing for expected volume.
- Diagnosing a queue that keeps growing.
- Sizing support or fulfillment capacity.
- Deciding whether a bottleneck needs more capacity or better flow.

## Procedure

### Forecast demand honestly

Separate the three components, because they need different treatment:

- **Baseline** — the steady rate, best estimated from your own history rather than from a plan.
- **Trend** — the direction, measured over enough periods to distinguish it from noise.
- **Spikes** — launches, seasonality, campaigns, incidents. Known spikes are a planning input;
  unknown ones are what headroom is for.

Forecast in the unit the work actually arrives in — tickets, orders, shipments, minutes of handling
— not in revenue. Revenue divided by an average is a forecast of an average, and averages are where
capacity planning goes to die.

### Capacity is not headcount

Usable capacity is people multiplied by available hours multiplied by the fraction spent on the work
in question. The last term is the one everyone omits and it is rarely above 70%: meetings, training,
holiday, and the interruptions that come with the job are real.

Plan against realistic effective capacity. Planning at 100% guarantees the plan fails on its first
ordinary week.

### Queues tell you before the dashboard does

Utilisation above roughly 80% makes wait times rise sharply and non-linearly — a system at 95% is not
slightly slower than one at 85%, it is qualitatively worse. This is why "we have spare capacity on
paper" coexists with a queue that never clears.

Watch the **trend in queue age**, not the queue length. A stable-length queue whose oldest item keeps
getting older is a queue that is quietly failing its slowest customers.

### Add capacity or fix flow

Before adding capacity, establish which it is:

- **Genuine capacity shortfall** — arrival rate exceeds service rate at reasonable utilisation. Add
  capacity.
- **Flow problem** — rework, handoffs, waiting on another team, batching. Adding capacity here adds
  cost and often makes throughput worse by increasing coordination. Send this to
  `enterprise/operations/process-design`.

The tell: if work spends most of its life waiting rather than being worked, it is a flow problem.

## Pitfalls

- Planning against nominal headcount rather than effective capacity.
- Running a critical queue at sustained high utilisation and treating the wait times as a mystery.
- Adding capacity to a process you have not measured.
- Forecasting in aggregate currency when work arrives in discrete units.
- Watching queue length rather than the trend in queue age.

## Verification

Report the forecast decomposed into baseline, trend, and spikes, in the unit work actually arrives
in. Report capacity as effective capacity with the utilisation fraction stated — not as headcount.
Show queue age distribution over time rather than length, and state which diagnosis applies: capacity
shortfall or flow problem, with the waiting-versus-working ratio as the evidence.

## Related

- `enterprise/operations/process-design` — where flow problems go.
- `enterprise/pmo/portfolio-governance` — allocating people across projects.
- `enterprise/customer-experience/support-operations` — the same discipline in a support queue.
