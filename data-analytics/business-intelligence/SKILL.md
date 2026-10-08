---
name: business-intelligence
description: "Builds reporting and self-serve analytics people use. Metric trees, dashboard design, distribution, and the discipline that stops dashboards proliferating. Use this to build a dashboard or report, design a metrics framework, set up self-serve analytics, decide what to measure, or diagnose why reporting exists but nobody uses it or trusts it."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: data-analytics
metadata:
  hermes:
    category: data-analytics
    tags: [data-analytics, business-intelligence, dashboards, metrics, reporting]
    related_skills: [chief-data-officer, data-modeling, data-governance]
---

# Business intelligence

Most organizations have too many dashboards and too little insight. The two are related: when
everything is measured, nothing is watched.

## When to Use

- Building a dashboard or report.
- Designing a metrics framework.
- Setting up self-serve analytics.
- Deciding what to measure.
- Diagnosing why reporting exists but nobody uses it or trusts it.

## Procedure

### Start from the decision

Every report answers one question for one audience who can act on it. Before building, name the
decision it informs and what a viewer would do differently based on it.

If nothing would change, do not build it. That single filter removes most dashboard requests, and
the ones surviving it get used.

### Metric trees

Structure metrics as a tree, not a list. One primary outcome at the top, decomposed into the drivers
that mathematically produce it, each decomposed again.

Revenue = customers × average value. Customers = new + retained. New = traffic × conversion. And so
on.

This does two things a metric list cannot: when the top number moves, you can walk down to find
*where*; and it makes clear which metrics are levers and which are outcomes. Teams should be
measured on levers they control, not on outcomes they influence.

### Dashboard design

- **One screen, one question.** Scrolling dashboards are several dashboards that were not separated.
- **Lead with the answer** — the primary number, its comparison, and whether that is good. A number
  with no comparison is not information.
- **Comparison always**: prior period, target, or cohort. Choose deliberately, because each tells a
  different story.
- **Say what "good" is.** A viewer who cannot tell whether 4.2% is good will not act.
- **Annotate the anomalies.** The spike everyone asks about should carry its explanation, or you
  will explain it every month.
- **Cut the rest.** Charts nobody uses cost attention on every visit and make the useful ones harder
  to find.

### Self-serve

Self-serve works when the semantic layer is trustworthy and the questions are anticipated. It fails
when people are handed raw tables and left to define metrics themselves — that produces confident
wrong answers, which is worse than a queue.

Give governed metrics, curated datasets, and templates for common questions. Keep the raw layer for
analysts.

### Maintenance

Dashboards accumulate. Review usage periodically and retire what nobody opens — with a notice period,
since the one person using it may be using it for something important.

## Pitfalls

- Building a report where nothing would change as a result.
- Handing people raw tables and calling it self-serve. Confident wrong answers are worse than a queue.
- Serving stale data silently rather than surfacing the failure.
- Quietly correcting a wrong number. That is how a team learns to check every figure by hand.
- Retiring a dashboard with no notice period — the one person using it may be using it for something
  important.

## Verification

Reporting nobody trusts is not used, and trust is lost far faster than it is rebuilt. Before calling
a dashboard done, confirm: freshness is shown on the surface, failures are surfaced rather than
swallowed, anything financial reconciles against the system of record, and every primary number
carries a comparison and a statement of what good looks like. Name the decision the report informs
and what a viewer would do differently.

## Related

- `enterprise/data-analytics/data-modeling` — the semantic layer this reads through.
- `enterprise/data-analytics/data-governance` — the metric definitions behind the tree.
- `enterprise/data-analytics/chief-data-officer` — owns the definition of record.
