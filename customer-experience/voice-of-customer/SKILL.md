---
name: voice-of-customer
description: "Builds the loop from what customers say to what changes. Collecting feedback, distinguishing signal from noise, routing it to owners, and closing the loop back to the customer. Use this to set up a feedback program, design or interpret CSAT and NPS, decide what customer feedback deserves action, get product to act on recurring issues, or diagnose why feedback is collected but nothing changes."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: customer-experience
metadata:
  hermes:
    category: customer-experience
    tags: [customer-experience, feedback, nps, csat, research]
    related_skills: [chief-customer-officer, support-operations, customer-research]
---

# Voice of customer

Most feedback programs collect diligently and change nothing. The collection is the easy half; the
loop is the whole value.

## When to Use

- Setting up a feedback program.
- Designing or interpreting CSAT and NPS.
- Deciding what customer feedback deserves action.
- Getting product to act on recurring issues.
- Diagnosing why feedback is collected but nothing changes.

## Procedure

### Sources, weighted honestly

- **Support contacts** — the highest-volume and least *prompted* source, and the most under-used.
  People contacting you have a real problem nobody asked them about. But the sample is strongly
  self-selected: it excludes everyone who silently churned, worked around the problem, or would
  never contact you. Treat it as operational evidence to be normalized per active account and
  triangulated against churn and behavioral data — never as representative of the customer base.
- **Churn and loss reasons** — the most valuable and most under-sampled. People leaving have no
  reason to be polite.
- **Interviews** — depth, small n, best for understanding *why* something in the data is happening.
- **Surveys** — breadth, and only meaningful once you know what to ask.
- **Public reviews and forums** — biased toward extremes, useful for what people say when you are not
  in the room.

Anything a customer built a workaround for outranks anything they merely said in a survey.

### On CSAT and NPS

Both are useful as trends and misleading as targets. The moment a team is measured on a score, the
score improves faster than the experience does — asking at the favorable moment, coaching for the
rating, excluding difficult segments.

Treat the score as a prompt for the free-text answer, which is where the information is. Segment
before concluding: an overall score is an average of experiences that have nothing in common.

### Turning feedback into change

The failure is not collection, it is triage. Feedback needs:

- **Categorization against a stable taxonomy**, so volume per cause is countable across periods.
- **Quantification.** "Several customers mentioned" loses every argument. "Eighty-one contacts this
  quarter, four percent of active accounts, twelve of them on enterprise plans" wins.
- **A named owner per theme**, outside the feedback function. A theme owned by the team collecting
  it goes nowhere.
- **A standing review** where product, support, and success look at the same list together.

Distinguish requests from problems. Customers describe solutions; your job is to recover the problem
underneath, because the request is often not the best fix for it.

### Closing the loop

Tell the customer what changed and that they prompted it. Almost nobody does this, which is exactly
why it works — it converts a complainer into someone who reports the next issue instead of leaving.

Also close it internally: show the support team what shipped because of what they escalated, or they
stop escalating.

## Pitfalls

- Reporting themes without volume.
- Letting one loud enterprise account set the roadmap without checking how widely the problem is
  shared.
- Running a program with no mechanism for anything to change as a result. That is a survey habit,
  not a feedback loop.
- Targeting a score without also watching the behavior it is supposed to predict.
- Treating support contacts as representative of the customer base.

## Verification

Report each theme with its volume, normalized per active account and stated as a share of the base;
the named owner outside the feedback function; what shipped as a result; and the loop closed both
ways — to the customers who prompted it and to the team that escalated it. A theme with no volume
attached and no owner named is not a finding.

## Related

- `enterprise/customer-experience/chief-customer-officer` — owns the prioritized list of recurring pain.
- `enterprise/customer-experience/support-operations` — the highest-volume source.
- `enterprise/marketing/customer-research` — prompted research that complements this.
