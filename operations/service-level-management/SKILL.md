---
name: service-level-management
description: "Defines and manages service levels. Setting targets that reflect what customers need, measuring honestly, and handling breaches. Use this to write or negotiate an SLA, decide what to measure and at what threshold, respond to a missed service level, or work out why a service that meets its targets still has unhappy customers."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: operations
metadata:
  hermes:
    category: operations
    tags: [operations, sla, percentiles, breaches, commitments]
    related_skills: [chief-operating-officer, support-operations, contract-review, observability-and-reliability, escalation-management]
---

# Service level management

A service level is a promise with a number attached. The number is the easy part; choosing what to
measure is where these go wrong.

## When to Use

- Writing or negotiating an SLA.
- Deciding what to measure and at what threshold.
- Responding to a missed service level.
- Working out why a service that meets its targets still has unhappy customers.

## Procedure

### Measure what the customer feels

The characteristic failure is a service meeting every target while customers are angry. It happens
when the measure is chosen for availability of data rather than relevance:

- **Uptime that excludes degraded operation.** Technically up and unusably slow is down.
- **Response time instead of resolution time.** An instant acknowledgment that resolves nothing
  measures the autoresponder.
- **Averages instead of percentiles.** A mean hides the tail, and the tail is who complains. Commit
  at p95 or p99, not the mean.
- **Measurement from inside your own perimeter**, which excludes the part of the path the customer
  actually traverses.

### Set targets you would fund

A target is a spending decision. Each added nine costs disproportionately more than the last, so the
question is never "what would be good?" but "what is the gap worth to the customer, and does it
exceed what closing it costs?"

Set the internal objective tighter than the external commitment. The gap between them is your
warning margin; without it, the first thing you learn about a breach is the breach.

### Write them so both sides can tell

An unmeasurable clause is a future dispute. Every service level needs: what is measured, where it is
measured from, how it is calculated, what is excluded, over what window, and what happens when it is
missed.

Exclusions are the substance — planned maintenance, force majeure, customer-caused failures,
dependencies outside your control. Vague exclusions get read narrowly when it matters. For anything
with contractual teeth, `enterprise/legal-risk/contract-review` owns the remedy language; this skill
owns whether the number is achievable.

### When you breach

Say so before the customer does. A breach reported by the provider with a cause and a fix costs far
less trust than one the customer discovers and raises.

Then separate the incident from the pattern. One breach is an incident, handled by
`enterprise/customer-experience/escalation-management`. Repeated breaches of the same target mean the
target was never fundable — renegotiate it honestly rather than continuing to miss it.

## Pitfalls

- Committing to a level you have not measured yourself achieving for a sustained period.
- Reporting availability on a mean when the customer experiences the tail.
- Agreeing an SLA whose exclusions are undefined.
- Letting a target stand that you have missed repeatedly without either funding it or renegotiating
  it.
- Measuring from inside your own perimeter.
- Measuring response time and calling it resolution.

## Verification

Before committing externally, measure yourself achieving the level for a sustained period, at the
percentile you intend to promise, from outside your own perimeter. Keep the internal objective
tighter than the external commitment so a breach is preceded by a warning rather than announced by a
customer. Report at p95 or p99 with the exclusions and measurement window stated.

## Related

- `enterprise/legal-risk/contract-review` — the remedy language behind the number.
- `enterprise/technology/observability-and-reliability` — where the measurement comes from.
- `enterprise/customer-experience/escalation-management` — a single breach as an incident.
