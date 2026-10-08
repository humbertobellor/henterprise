---
name: observability-and-reliability
description: "Makes systems debuggable and reliably operable. Instrumentation, alerting that is worth waking for, service objectives, and learning from failure. Use this to instrument a service, fix alerting that is ignored, set error budgets or reliability targets, prepare for on-call, or run a blameless post-incident review."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: technology
metadata:
  hermes:
    category: technology
    tags: [technology, observability, alerting, slo, post-incident]
    related_skills: [cloud-infrastructure, systematic-debugging, service-level-management, incident-response, release-and-deployment]
---

# Observability and reliability

Monitoring tells you a thing you predicted is happening. Observability lets you ask a question you
did not anticipate. Production failures are mostly the unanticipated kind.

## When to Use

- Instrumenting a service.
- Fixing alerting that is ignored.
- Setting error budgets or reliability targets.
- Preparing for on-call.
- Running a blameless post-incident review.

## Procedure

### Instrument for questions you have not thought of yet

Emit structured events with enough context to slice afterwards — request identifiers, user or tenant,
version, dependency, outcome, duration. Free-text logs are unsearchable at volume and become
expensive noise.

Propagate a correlation identifier across every hop. Without it, a distributed system is a set of
independent stories and reconstructing one request is manual archaeology.

Measure what the user experiences at the percentile they experience it. A p50 latency graph is
mostly a graph of the people who were not affected.

### Alert on symptoms, not causes

Alert when users are affected or imminently will be. High CPU is not an alert; requests failing or
slowing is. Cause-based alerting produces pages for conditions the system handled and no page for
novel failures that hurt.

Every alert must be **actionable, urgent and specific**. If the recipient's honest response is to
look and close it, delete the alert — it is training the on-call to ignore the page, and the ignored
page is eventually the real one.

Alert fatigue is the actual reliability risk in most organizations. Fewer, better alerts beat
coverage.

### Objectives and error budgets

Set service level objectives from what users need, then treat the remainder as a budget to spend.
This converts a sterile argument between shipping and stability into arithmetic: budget remaining
means ship, budget exhausted means the next work is reliability.

Keep the internal objective tighter than any external commitment made through
`enterprise/operations/service-level-management`, so you find out before the customer does.

## Pitfalls

- Paging a human for something they cannot act on.
- Alerting on a cause when you can alert on the symptom.
- Reporting reliability as an average when users experience the tail.
- Closing an incident review with the finding that someone was careless.
- Free-text logs, which are unsearchable at volume and expensive.
- Chasing alert coverage rather than alert quality.

## Verification

Post-incident review exists to find what made the failure possible and hard to detect, not who
touched it last. Human error is a starting question, never the finding: what made the error easy,
and why did nothing catch it?

Track the time to *detect* separately from time to resolve. Long detection is an observability
defect, and it is the part that repeats.

Produce a small number of real actions with owners and dates. A review generating fifteen actions
generates none.

## Related

- `enterprise/operations/service-level-management` — the external commitment this sits inside.
- `enterprise/technology/systematic-debugging` — using the instrumentation on a live problem.
- `enterprise/security/incident-response` — when the failure is a compromise.
