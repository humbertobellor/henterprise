---
name: chief-information-officer
description: "Runs the technology the company works on. Service quality, IT spend, and the boundary with product engineering. Use this to set IT priorities, decide what IT owns versus engineering, structure IT spend or an IT roadmap, judge whether to build, buy or outsource, or work out why IT is seen as a cost center rather than an enabler."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: it-operations
metadata:
  hermes:
    category: it-operations
    tags: [it-operations, executive, it-spend, sourcing, service-quality]
    related_skills: [service-desk, systems-administration, network-administration, endpoint-management, backup-and-recovery]
---

# Chief Information Officer

The CIO runs the technology the company works *on*. The CTO runs the technology the company
*sells*. Confusing the two is why IT ends up owning a product roadmap it cannot resource, or why
engineering ends up running a help desk badly.

## When to Use

- Setting IT priorities.
- Deciding what IT owns versus engineering.
- Structuring IT spend or an IT roadmap.
- Judging whether to build, buy, or outsource.
- Working out why IT is seen as a cost center rather than an enabler.

## Procedure

### What this department owns

The systems every employee depends on and nobody markets: identity, endpoints, network, corporate
applications, the service desk, and the backup and restore path. Its output is measured in
availability, time-to-resolution, and how little anyone has to think about it.

- `enterprise/it-operations/service-desk` — the front door, and the honest measure of whether any of
  this works
- `enterprise/it-operations/systems-administration` and
  `enterprise/it-operations/network-administration` — the estate
- `enterprise/it-operations/endpoint-management` — the most exposed surface, because it leaves the
  building
- `enterprise/it-operations/identity-lifecycle-administration` — execution of joiner-mover-leaver
- `enterprise/it-operations/it-asset-management` — what you have, who has it, what it costs
- `enterprise/it-operations/backup-and-recovery` — the restore, tested rather than assumed

### The boundaries that cause arguments

State them once, in writing, and the recurring turf disputes stop:

- **Security sets policy; IT executes it.** `enterprise/security/access-and-identity` decides what a
  role should be entitled to; this department provisions it.
  `enterprise/security/vulnerability-management` decides what is urgent;
  `enterprise/it-operations/systems-administration` runs the cadence.
- **Engineering owns the product estate; IT owns the corporate estate.**
  `enterprise/technology/cloud-infrastructure` designs the environment the product runs in. Where a
  corporate system runs in the same cloud, ownership follows who the users are, not where it is
  hosted.
- **Continuity objectives are the business's; the restore is IT's.**
  `enterprise/operations/business-continuity-and-resilience` sets RTO and RPO with the process
  owners; this department has to deliver against them and should say plainly when it cannot.

### Build, buy, or outsource

Default to buy for anything that is not a differentiator. Building an internal tool that a mature
product already solves is a decision to maintain it forever, staffed by people who would rather be
doing something else.

Outsource where the work is commoditized and the failure is recoverable — first-line support out of
hours, hardware logistics. Keep in-house what needs institutional context or carries irreversible
risk: identity, data, and anything where a bad decision is discovered a year later.

### Spend, and the cost-center trap

Attribute IT cost to the functions consuming it rather than reporting one aggregate. An
undifferentiated IT budget invites across-the-board cuts, because nobody can see what any of it buys.

The trap is real: a department judged only on cost is asked only to be cheaper, and the first
casualties are refresh cycles and patching, which surface as incidents two years later with no
visible cause.

## Pitfalls

- Accepting a continuity objective you have not demonstrated you can meet.
- Letting identity policy and identity execution sit with the same reviewer.
- Building an internal tool for a solved commodity problem.
- Reporting IT cost without reporting what it delivered.
- Outsourcing work that needs institutional context or carries irreversible risk.

## Verification

Report service outcomes alongside cost, attributed to the functions consuming it, and be specific
about what a proposed cut removes. Availability, time to resolution at the percentile users feel, and
tested restore times are the evidence; an aggregate budget line with no outcomes attached is what
invites the across-the-board cut.

## Related

- `enterprise/technology/chief-technology-officer` — the technology the company sells.
- `enterprise/security/access-and-identity` — sets the policy this department executes.
- `enterprise/operations/business-continuity-and-resilience` — sets the objectives this delivers against.
