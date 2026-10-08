---
name: retention
description: "Diagnoses and reduces churn. Cancellation flows, save offers, failed-payment recovery, at-risk detection, and the product and service causes underneath. Use this when churn is rising or unexplained, to design a cancellation or win-back flow, to recover involuntary churn, to identify at-risk accounts before they leave, or to decide whether a retention problem is a product problem."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: revenue
metadata:
  hermes:
    category: revenue
    tags: [revenue, churn, dunning, cancellation, at-risk]
    related_skills: [activation, chief-revenue-officer, unit-economics, voice-of-customer, pricing-and-packaging]
---

# Retention

Churn has two causes with nothing in common but the outcome. Separating them is the first move.

## When to Use

- Churn is rising or unexplained.
- Designing a cancellation or win-back flow.
- Recovering involuntary churn.
- Identifying at-risk accounts before they leave.
- Deciding whether a retention problem is really a product problem.

## Procedure

### Separate the two churns first

- **Involuntary** — payment failed. Often a large share of total churn, entirely mechanical, and the
  cheapest thing to fix in the whole business.
- **Voluntary** — they chose to leave.

Fix involuntary first. Card retries on a sensible schedule, dunning emails that reach a human,
pre-expiry notification, and a grace period that does not immediately cut off access. This is
recoverable revenue sitting untouched in most companies.

### Diagnosing voluntary churn

Ask when the decision was actually made. It is almost never at cancellation — it is weeks earlier,
at a failed expectation, an unresolved support issue, or a champion leaving.

Segment churn by tenure, plan, acquisition channel, and activation status. Concentrations tell you
the cause:

- **Early churn** — activation problem, not retention. Fix onboarding.
- **Churn at renewal** — value not visible enough to justify the line item.
- **Churn after a specific event** — find the event: a price change, an outage, a redesign, a
  champion departure.
- **Churn concentrated in one channel** — an acquisition problem. You are buying the wrong
  customers, and no retention work fixes that.

### Cancellation flow

Make canceling straightforward. Obstruction generates chargebacks, public complaints, and in a
growing number of jurisdictions, regulatory exposure.

Do ask why, with specific options plus free text — this is the highest-quality product feedback you
will ever receive, from people with no reason to be polite.

Offer a save only where it addresses the stated reason. A discount offered to someone leaving
because a feature is missing confirms you were not listening. Pause is often the better offer and is
rarely available.

### At-risk detection

Build a simple signal from declining usage, a support escalation, a champion going quiet, or a seat
count dropping. Then act on it while intervention is still possible — a health score nobody works is
a dashboard, not a program.

## Pitfalls

- Counting a saved cancellation as retained without checking whether they stayed a quarter later.
- Treating retention as a service problem when the data says it is a product or acquisition problem.
- Making cancellation require a phone call.
- Working voluntary churn before fixing involuntary, which is mechanical and cheaper.
- Offering a discount to someone leaving over a missing feature.
- A health score nobody acts on.

## Verification

Report the two churns separately, always — a blended number hides the mechanical half that is
cheapest to fix. Segment voluntary churn by tenure, plan, channel, and activation status before
concluding a cause; the concentration is the diagnosis.

For every save, check the cohort a quarter later. A save that churns in ninety days was a deferral,
not a retention.

## Related

- `enterprise/revenue/activation` — early churn belongs there.
- `enterprise/customer-experience/voice-of-customer` — cancellation reasons as product feedback.
- `enterprise/finance/unit-economics` — retention is the input to lifetime value.
