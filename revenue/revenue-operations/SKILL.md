---
name: revenue-operations
description: "Runs the mechanics of the revenue engine. Lead lifecycle definitions, routing, CRM hygiene, forecasting process, pipeline reporting, and the marketing-to-sales handoff. Use this to fix a broken handoff, define lifecycle stages, improve forecast accuracy, clean up CRM data, design territory or routing rules, or diagnose why pipeline numbers are not trusted."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: revenue
metadata:
  hermes:
    category: revenue
    tags: [revenue, revops, forecasting, lead-scoring, crm]
    related_skills: [chief-revenue-officer, outbound-prospecting, marketing-analytics, sales-enablement, data-governance]
---

# Revenue operations

The mechanics underneath the revenue engine: definitions, routing, hygiene, and the forecast.

## When to Use

- Fixing a broken marketing-to-sales handoff.
- Defining lifecycle stages.
- Improving forecast accuracy.
- Cleaning up CRM data.
- Designing territory or routing rules.
- Diagnosing why pipeline numbers are not trusted.

## Procedure

### Definitions before dashboards

Most revenue reporting arguments are definitional. Write down and get agreement on, in one place:

- What each **lifecycle stage** means and the observable event that moves a record into it.
- What makes a lead **qualified** — and by whose judgment.
- When an opportunity is **created**, and what evidence is required.
- What each **pipeline stage** requires to be entered, stated as a buyer action rather than a seller
  feeling. "Prospect has confirmed budget" is observable; "showing strong interest" is not.
- What **closed-lost** means versus stalled, and when a stalled deal exits the pipeline
  automatically.

Without these, every number is negotiable and forecasting is a genre of fiction.

### The handoff

Where most revenue leaks. Specify: the exact criteria for passing a lead, the SLA for first contact,
what context transfers with it, and the route back when it is rejected — including the reason,
recorded.

A rejection loop with no recorded reason means marketing keeps sending the same unqualified leads,
and both sides believe the other is the problem.

### Lead scoring

Scoring exists to route attention, not to produce a number. If sellers do not change what they work
on because of the score, it is decoration.

Score on two independent dimensions and keep them separate:

- **Fit** — do they look like a customer? Company size, industry, geography, role and seniority,
  technology in use. Static, knowable before any engagement.
- **Intent** — are they acting like a buyer now? Pricing page visits, repeat sessions, demo request,
  content depth, response to outreach. Dynamic, and it decays.

Collapsing the two into one score is the standard mistake: a perfect-fit account with no activity
and a poor-fit account browsing aggressively land on the same number and get treated identically,
which is wrong in both directions.

Build the model from closed-won and closed-lost history, not intuition. Look at what actually
separated the two, and be prepared for the finding that a favored attribute has no predictive value.

Decay intent scores over time and recalibrate on a schedule. A scoring model built once and never
revisited drifts as the market and the product change, and nobody notices because it keeps producing
numbers.

### Forecasting

Forecast accuracy comes from process, not optimism.

- Stage-based probabilities derived from your own historical conversion, recalculated periodically —
  not from defaults.
- Commit, best case, and pipeline reported separately.
- Every forecasted deal has a date and a next step. A deal with neither is not in the forecast.

### CRM hygiene

Data quality decays continuously. Required fields at stage gates, validation at entry, scheduled
duplicate merges, and automatic aging of stale records. Rely on discipline alone and the data will
be unusable within two quarters.

## Pitfalls

- Building dashboards before the definitions are agreed.
- Pipeline stages defined by seller feeling rather than buyer action.
- A rejection loop with no recorded reason, so both sides believe the other is the problem.
- Collapsing fit and intent into one score.
- Stage probabilities taken from tool defaults rather than your own conversion history.
- Requiring a field whose value is not used in a decision. Every unnecessary field trains sellers to
  enter garbage in all of them.

## Verification

Track forecast accuracy itself, by rep. It is the only way to know whose numbers to trust and it
improves quickly once measured.

State the definitional gaps found, the process change proposed, what it costs sellers in time, and
the metric that will show it worked.

## Related

- `enterprise/revenue/chief-revenue-officer` — owns the forecast of record.
- `enterprise/demand-generation/marketing-analytics` — the upstream definitions must match.
- `enterprise/data-analytics/data-governance` — one definition per metric, organization-wide.
