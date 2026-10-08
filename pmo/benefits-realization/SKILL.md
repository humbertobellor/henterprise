---
name: benefits-realization
description: "Ensures projects deliver the value they promised. Defining measurable benefits, baselining, tracking after delivery, and honest post-implementation review. Use this to define benefits for a business case, set a baseline, track whether value actually landed, or run a post-implementation review that produces something useful."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: pmo
metadata:
  hermes:
    category: pmo
    tags: [pmo, benefits, baselines, post-implementation-review, value]
    related_skills: [head-of-pmo, portfolio-governance, change-and-adoption, capital-allocation]
---

# Benefits realization

Projects are approved on promised benefits and closed on delivered scope. The gap between those two
sentences is why organizations repeat expensive mistakes with confidence.

## When to Use

- Defining benefits for a business case.
- Setting a baseline.
- Tracking whether value actually landed.
- Running a post-implementation review that produces something useful.

## Procedure

### Define benefits so they can be disproved

A benefit that cannot fail to be claimed is not a benefit. Each needs a measure, a current baseline,
a target, a date by which it should appear, and an owner who is accountable **after** the project
closes — usually the operational owner, not the project manager, who has moved on.

Distinguish honestly:

- **Cashable** — the budget actually reduces. Someone can point at the line.
- **Non-cashable** — time is released. Real, but only becomes value if that time is redeployed to
  something that matters, which is a separate management act nobody schedules.
- **Cost avoidance** — a future cost does not occur. Legitimate and unverifiable, so treat claims
  sceptically.
- **Non-financial** — risk reduction, compliance, experience. Often the actual reason. Say so rather
  than manufacturing a financial number nobody believes.

The most common failure is a business case padded with non-cashable savings presented as though the
budget will fall. It will not, and the credibility loss lands on the next case.

### Baseline before you change anything

A baseline captured after go-live is not a baseline. Measure first, and record how it was measured —
by the time anyone checks, the method will be disputed and nobody will remember.

### Tracking happens after the project ends

Benefits appear months after delivery, when the project team has dispersed and attention has moved.
This is precisely why it does not happen, and why it needs to be owned by the operational line and
scheduled at approval rather than intended.

Set review points at meaningful intervals — ninety days, six months, a year — and hold them
regardless of what the answer looks like.

## Pitfalls

- Approving a case whose benefits have no owner after the project closes.
- Presenting non-cashable savings as budget reduction.
- Baselining after implementation.
- Running a review that punishes honesty — it will produce reviews saying the project was a success.
- Manufacturing a financial number for a benefit that is really risk reduction or compliance.

## Verification

A post-implementation review worth the hour asks two questions: did the benefits appear, and would we
make the same decision knowing what we now know?

Include estimation accuracy, since the systematic bias in an organization's estimates is one of the
most useful things it can know about itself and is discoverable only by looking back.

Make it non-punitive or it will produce nothing true. Feed the findings back to
`enterprise/pmo/portfolio-governance` and `enterprise/finance/capital-allocation`, which are where
the next set of approvals gets made.

## Related

- `enterprise/pmo/change-and-adoption` — without adoption there is nothing to realize.
- `enterprise/pmo/portfolio-governance` — where the findings change the next approval.
- `enterprise/finance/capital-allocation` — the look-back on the approved case.
