---
name: process-design
description: "Designs, documents, and fixes operational processes. Mapping the current state, finding where work actually stalls, redesigning the flow, and building controls that hold. Use this when the same failure keeps recurring, when a handoff between teams is unreliable, when onboarding a repeated task, when work takes far longer than the work itself, or when deciding whether to automate, standardize, or eliminate a process."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: operations
metadata:
  hermes:
    category: operations
    tags: [operations, process, constraints, flow, controls]
    related_skills: [chief-operating-officer, capacity-and-demand-planning, quality-management, service-level-management]
---

# Process design

Mapping what actually happens, finding the constraint, redesigning the flow, and building controls
that hold without discipline.

## When to Use

- The same failure keeps recurring.
- A handoff between teams is unreliable.
- Onboarding a repeated task.
- Work takes far longer than the work itself.
- Deciding whether to automate, standardize, or eliminate a process.

## Procedure

### Map what happens, not what is supposed to happen

Follow a real instance end to end and record every step, handoff, wait, and rework loop. Talk to the
people doing it, who will describe several steps that exist nowhere in the documentation and one or
two that everyone has quietly stopped doing.

Then measure two things:

- **Touch time** — how long the work actually takes.
- **Elapsed time** — how long it takes to get through.

The gap between them is the process. In most broken processes, work is waiting more than ninety
percent of the time, which means speeding up the work changes almost nothing. Attack the waits.

### Find the real constraint

One step governs throughput. Improving anything else produces inventory in front of the constraint
and no more output. Find it: the step with a queue in front of it.

Common constraints that are not the obvious step: a single approver, a specialist everything routes
through, a system that only one team can access, and a batch cycle that makes everything wait for
the weekly run.

### Redesign

In this order, because the order is the leverage:

1. **Eliminate.** Does this step need to exist? Many exist to catch a failure that a different fix
   would prevent entirely.
2. **Simplify.** Fewer handoffs, fewer approvals, fewer systems. Every handoff is a place work
   stops.
3. **Standardize.** One way of doing it, written down, with the decision rules explicit.
4. **Automate.** Last. Automating an unexamined process makes a bad process faster and much harder
   to change.

Push approval to the lowest level that can be accountable, and set thresholds so routine cases do
not queue behind exceptional ones.

### Make it hold

A documented process that relies on discipline degrades within a quarter. Build the control into the
system: required fields, blocking gates, defaults that are correct, automated handoffs.

## Pitfalls

- Fixing a recurring failure with a reminder. If people are forgetting a step, the system permits
  forgetting it — fix that.
- Mapping the documented process rather than following a real instance.
- Speeding up the work when the work is waiting ninety percent of the time.
- Improving a step that is not the constraint, which produces inventory and no more output.
- Automating before eliminating and simplifying, which makes a bad process faster and harder to
  change.
- Adding a step without naming what it prevents.

## Verification

Report current state with elapsed and touch time, the constraint and its evidence, the redesign,
what it costs to implement, and the measure that will show it worked.

Then re-measure elapsed time after the change, not touch time — the gap is the process, and closing
it is the only proof the redesign worked.

## Related

- `enterprise/operations/capacity-and-demand-planning` — whether it is flow or genuine shortfall.
- `enterprise/operations/quality-management` — defects as a process signal.
- `enterprise/finance/internal-controls-and-audit` — controls that leave evidence.
