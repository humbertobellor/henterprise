---
name: business-continuity-and-resilience
description: "Plans for operating through disruption. Impact analysis, recovery objectives, continuity plans, and the exercises that prove they work. Use this to run a business impact analysis, set RTO and RPO, write or test a continuity plan, prepare for a supplier or site failure, or answer a customer's resilience questionnaire."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: operations
metadata:
  hermes:
    category: operations
    tags: [operations, continuity, rto, rpo, exercises]
    related_skills: [chief-operating-officer, backup-and-recovery, corporate-governance, vendor-management]
---

# Business continuity and resilience

Continuity is a business question wearing technical clothing. The technical restore is covered by
`enterprise/it-operations/backup-and-recovery`; this is about which processes must keep running, for
whom, and how long you can survive without them.

## When to Use

- Running a business impact analysis.
- Setting RTO and RPO.
- Writing or testing a continuity plan.
- Preparing for a supplier or site failure.
- Answering a customer's resilience questionnaire.

## Procedure

### Start with impact, not systems

A business impact analysis asks, per process: what breaks downstream, how fast, and who notices.
Work outward from the customer-visible failure, not inward from the asset register — an inventory of
systems tells you what you own, never what matters.

For each critical process establish:

- **Maximum tolerable outage** — the point past which the damage is not recoverable by working harder
  afterwards. This is a business judgment, made by the process owner, not by IT.
- **RTO** — how quickly it must be back. Always shorter than someone wants to pay for.
- **RPO** — how much data you can afford to lose, measured in time. An RPO of zero is a claim about
  spending, not about intent.

RTO and RPO that were not signed by the person accountable for the process are aspirations.

### Plans people can follow badly

A continuity plan is read by a stressed person at 03:00 who did not write it. Optimize for that
reader: named roles rather than names, decision authority stated explicitly, and the first three
actions on the first page.

Include what to do when the plan's assumptions fail — the alternate site is also affected, the key
person is unreachable, the supplier is not answering. Plans that only handle the anticipated failure
handle almost nothing.

### Concentration risk

Resilience fails where dependencies converge invisibly: three suppliers who all sit on one cloud
region, redundant network paths in the same physical duct, a manual workaround that requires a
system you have just lost. Map dependencies to the point where they stop being yours, and check
whether the redundancy is real or just contractual.

## Pitfalls

- Setting an RTO without the process owner agreeing to what it costs.
- Counting a plan as tested because it was reviewed.
- Treating a backup as continuity — an unrestored backup is an untested assumption.
- Writing a plan whose first step requires the system that has just failed.
- Working inward from the asset register, which tells you what you own and never what matters.
- Redundancy that is contractual rather than real.

## Verification

Untested plans are documents, not capabilities. Escalate the rigour:

1. **Walkthrough** — read it aloud together and find the steps nobody can actually perform.
2. **Tabletop** — inject a scenario and make the decisions under time pressure.
3. **Live failover** — actually run on the alternate path, in production, with the real people.

The exercise produces findings or it was theatre. Track them as work with owners and dates, and
re-run the scenario that failed rather than a fresh one, so improvement is demonstrable.

## Related

- `enterprise/it-operations/backup-and-recovery` — delivers the technical restore against these objectives.
- `enterprise/operations/vendor-management` — supplier concentration and their own continuity.
- `enterprise/legal-risk/corporate-governance` — insurance and the board-level view.
