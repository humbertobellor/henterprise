---
name: program-management
description: "Plans and drives cross-functional programs. Scope, sequencing, dependencies, status, risk, and the escalations that keep work moving. Use this to run a multi-team initiative, recover a program that is slipping, build a delivery plan with dependencies, structure status reporting, or diagnose why cross-team work keeps missing dates."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: pmo
metadata:
  hermes:
    category: pmo
    tags: [pmo, programs, sequencing, status, escalation]
    related_skills: [project-delivery, dependency-and-risk-management, head-of-pmo, change-and-adoption]
---

# Program management

Programs fail at the seams between teams, not inside them. The job is the seams.

## When to Use

- Running a multi-team initiative.
- Recovering a program that is slipping.
- Building a delivery plan with dependencies.
- Structuring status reporting.
- Diagnosing why cross-team work keeps missing dates.

## Procedure

### Set up

- **One outcome, stated as a business result** with a date. Programs with several equal objectives
  have none.
- **A named accountable owner** — one person, not a committee. The program manager drives; the owner
  decides.
- **Scope written as inclusions and exclusions.** The exclusions do the work; unwritten exclusions
  return as assumptions.
- **Dependencies mapped and agreed by the teams that owe them**, with dates they have actually
  committed to. A dependency in your plan that the owning team has not agreed to is a wish.

### Sequencing

Order by dependency and risk, not by team convenience. Front-load the things that could invalidate
the plan — the technical unknown, the vendor decision, the approval that might not come. Discovering
in month four that the plan was impossible is the characteristic program failure.

Build in slack at integration points, not at the end. End-loaded buffer gets consumed early and
silently.

### When it slips

Establish whether it is a scope problem, a capacity problem, or a dependency problem — the remedies
are entirely different and applying the wrong one makes it worse.

Then present options with consequences: cut scope (name what), extend (say by how much and what else
is affected), or add capacity (which rarely helps late, and often hurts).

Re-baseline once, visibly, rather than slipping a week at a time. Serial small slips destroy
credibility far faster than one honest reset.

## Pitfalls

- Reporting green on a program with an unresolved blocker.
- Accepting a dependency date the owning team has not confirmed.
- Adding people to a late program and assuming it accelerates.
- Several equal objectives, which means none.
- End-loaded buffer, which gets consumed early and silently.
- Serial one-week slips instead of one honest re-baseline.

## Verification

Status that is worth reading has three things, every time: are we on track for the date, what changed
since last time, and what decision or unblock is needed. Everything else is appendix.

Track status against **committed dates**, not effort. "80% complete" is not information; "the
integration is done, the migration starts Monday, the sign-off is the risk" is.

Escalate early and specifically. An escalation naming the decision needed and the date it is needed
by gets resolved; a general statement of concern gets acknowledged and nothing happens.

## Related

- `enterprise/pmo/project-delivery` — a single bounded project rather than several.
- `enterprise/pmo/dependency-and-risk-management` — the seams in detail.
- `enterprise/pmo/change-and-adoption` — whether the delivery gets used.
