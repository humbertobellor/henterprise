---
name: head-of-pmo
description: "Runs the PMO, and keeps it worth funding. What it governs, what it must never become, and how it earns standing rather than compliance. Use this to stand up or reform a PMO, decide what it should and should not control, judge whether it is adding value or overhead, or work out why teams route around it."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: pmo
metadata:
  hermes:
    category: pmo
    tags: [pmo, governance, capacity, gates, standing]
    related_skills: [portfolio-governance, program-management, project-delivery, benefits-realization, change-and-adoption]
---

# Head of the PMO

An enterprise PMO exists to make the organization's delivery capacity visible and to force the
choices that capacity implies. It does not exist to collect status.

## When to Use

- Standing up or reforming a PMO.
- Deciding what it should and should not control.
- Judging whether it is adding value or overhead.
- Working out why teams route around it.

## Procedure

### The two failure modes

Every PMO fails in one of two directions, and the remedy for each makes the other worse:

- **The reporting PMO.** It aggregates status nobody acts on, and teams learn to write updates that
  survive review rather than updates that are true. Its meetings are attended and its findings
  ignored. This is the common one.
- **The controlling PMO.** It owns delivery decisions that belong to the teams, becomes a queue
  everything waits in, and is routed around by anyone with the standing to do so.

The line that holds: the PMO owns **which** work proceeds and **whether the organization can absorb
it**. Teams own **how** the work gets done.

### What it governs

- `enterprise/pmo/portfolio-governance` — intake, prioritization against real capacity, stage gates
  that can stop things, and resource contention across projects
- `enterprise/pmo/program-management` and `enterprise/pmo/project-delivery` — the delivery
  disciplines themselves
- `enterprise/pmo/dependency-and-risk-management` — the seams between teams, where programs actually
  fail
- `enterprise/pmo/benefits-realization` — whether the value claimed at approval ever appeared
- `enterprise/pmo/change-and-adoption` — whether anyone uses what was delivered

Benefits and adoption are the two that make a PMO worth funding. A PMO that governs intake but never
checks outcomes has only made the front door more expensive.

### Reporting line, and why it matters

The EPMO reports to the COO, not into any function whose work it governs. A PMO housed inside the
largest delivery organization will, over time, prioritize that organization's work — not through bad
faith but through proximity.

It has no write surface over the departments it governs. Its authority is procedural: it runs the
gate, it holds the capacity number, and it publishes what was decided.

### Earning standing

A PMO is obeyed when it is useful and circumvented when it is ceremony. What makes it useful:

- **Say no visibly, and say why.** A gate that has never stopped anything is a gate nobody respects.
- **Hold the capacity number and defend it.** The PMO is usually the only function that can see the
  organization is committed past what it can deliver, and saying so is most of the job.
- **Kill things.** Stopping a dead project releases capacity the whole portfolio needs, and
  organizations are structurally bad at it — see `enterprise/pmo/portfolio-governance`.
- **Make reporting cost less than it returns.** Every status template is a tax on delivery. Ask for
  what changes a decision and nothing else.

## Pitfalls

- Collecting status that feeds no decision.
- Taking a delivery decision that belongs to the team doing the work.
- Running a portfolio gate that has never stopped anything.
- Letting the PMO report into the function whose work it governs.
- Governing intake but never checking outcomes, which only makes the front door more expensive.

## Verification

The PMO is working when it can point to things it stopped, a capacity number it defended, and
benefits it checked after delivery. Report those three rather than throughput of governance
activity. Every reporting template in use should be traceable to a decision it changes; if it is
not, remove it and say so.

## Related

- `enterprise/operations/chief-operating-officer` — the reporting line, deliberately outside delivery.
- `enterprise/pmo/portfolio-governance` — the gate and the capacity line.
- `enterprise/pmo/benefits-realization` — the outcome check that justifies the function.
