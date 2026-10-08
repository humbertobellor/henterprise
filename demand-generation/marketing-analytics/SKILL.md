---
name: marketing-analytics
description: "Sets up and audits marketing measurement. Tracking plans, event schemas, attribution models, and the dashboards built on them. Use this to instrument a site or product, audit tracking nobody trusts, choose or interpret an attribution model, build reporting that answers a specific question, or reconcile numbers that disagree between tools."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: demand-generation
metadata:
  hermes:
    category: demand-generation
    tags: [demand-generation, analytics, tracking-plan, attribution, reporting]
    related_skills: [experimentation, business-intelligence, data-governance, paid-advertising]
---

# Marketing analytics

Dashboards built on bad instrumentation are confident and wrong, which is worse than having none.

## When to Use

- Instrumenting a site or product.
- Auditing tracking nobody trusts.
- Choosing or interpreting an attribution model.
- Building reporting that answers a specific question.
- Reconciling numbers that disagree between tools.

## Procedure

### The tracking plan comes first

Define, in writing, before implementing: every event, when it fires, its properties and their types,
and the question each one exists to answer. An event with no question behind it is noise that will
be maintained forever.

Naming convention decided once and enforced: `object_action`, lowercase, past tense. Inconsistent
naming is unfixable later without breaking historical data.

### Auditing existing tracking

Numbers nobody trusts usually come from one of:

- **Double-firing** on route changes in single-page apps.
- **Events that stopped** when someone changed a selector or a component.
- **Definition drift** — two tools counting "signup" at different moments.
- **Bot and internal traffic** never filtered out.
- **Consent and blockers** removing a meaningful and non-random share of data.

### Attribution

Every model is wrong in a known direction. Pick deliberately and state the bias:

- **Last-touch** — over-credits closing channels: brand search, retargeting. Under-credits
  everything that created demand.
- **First-touch** — the mirror image; over-credits discovery.
- **Multi-touch** — better, and dependent on complete tracking you probably do not have.
- **Incrementality testing** — the only method that answers "would this have happened anyway." The
  most expensive and the most trustworthy.

Use one model consistently for decisions, and check it periodically against a holdout. Switching
models to make a channel look better is how organizations mislead themselves.

### Reporting

Every report answers one question for one audience. Reports built to display everything get read by
nobody.

Show the metric, its comparison period, and the decision it informs. A number with no comparison is
not information. Where a number moved, the report should say why or say that the cause is unknown —
"unknown" is a legitimate and useful finding.

## Pitfalls

- Implementing events before the tracking plan is written.
- An event with no question behind it, which becomes noise maintained forever.
- Inconsistent naming, unfixable later without breaking historical data.
- Switching attribution models to make a channel look better.
- Reading a dashboard to verify tracking.
- A report with no comparison period attached to its numbers.

## Verification

Verify by doing the action yourself and watching the event arrive with the properties you expect.
Not by reading the dashboard.

Then check the audit list end to end: no double-firing on route changes, no silently stopped events,
one definition per metric across tools, bot and internal traffic filtered, and the share of data lost
to consent and blockers stated rather than ignored. Check the attribution model against a holdout on
a cadence.

## Related

- `enterprise/demand-generation/experimentation` — depends entirely on this instrumentation.
- `enterprise/data-analytics/business-intelligence` — the dashboards built on top.
- `enterprise/data-analytics/data-governance` — one definition of record per metric.
