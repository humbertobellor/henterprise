---
name: systems-administration
description: "Runs servers and corporate systems. Patching, configuration baselines, change control, capacity, and the routine that prevents incidents. Use this to establish a patching cadence, standardize server configuration, plan a maintenance window, decide change control for infrastructure, or clean up systems that have drifted from any known state."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: it-operations
metadata:
  hermes:
    category: it-operations
    tags: [it-operations, patching, baselines, change-control, drift]
    related_skills: [chief-information-officer, it-asset-management, network-administration, vulnerability-management, cloud-infrastructure]
---

# Systems administration

Well-run systems are boring. The work is in the routine that keeps them that way, and almost every
serious incident traces back to a routine that was skipped.

Cloud environment design belongs to `enterprise/technology/cloud-infrastructure`; this is operating
the systems the company runs on.

## When to Use

- Establishing a patching cadence.
- Standardizing server configuration.
- Planning a maintenance window.
- Deciding change control for infrastructure.
- Cleaning up systems that have drifted from any known state.

## Procedure

### Configuration baselines and drift

Every system class needs a defined baseline: build, hardening, agents, logging, accounts. Systems
built by hand from memory diverge immediately and cannot be reasoned about as a group.

Drift is the real enemy. Detect it continuously and correct rather than document — a system that no
longer matches its baseline is a system whose behavior under patching or failover is unknown.

The strongest form is disposability: rebuild rather than repair. A system you can rebuild in an hour
never accumulates the sediment of a decade of manual fixes.

### Patching as a cadence

Set a regular, predictable window and hold it. Ad hoc patching means patching happens when someone
worries, which is never in proportion to actual risk.

Tier by exposure: internet-facing systems on the shortest cycle, then internal, then isolated.
Emergency patching is a separate path with its own authority, used for actively exploited
vulnerabilities — `enterprise/security/vulnerability-management` decides what is urgent, this skill
executes it.

### Change control proportionate to risk

Heavyweight approval for trivial changes produces circumvention, and circumvention produces
unrecorded changes, which is worse than no process.

Tier it: standard pre-approved changes, normal changes with review, emergency changes with
after-the-fact record. Every change needs an owner, a back-out plan, and a record — the back-out plan
being the part most often assumed rather than written.

Maintenance windows exist to make disruption predictable. Announce them, keep them, and finish inside
them.

### Know what you have

An unmanaged system is a system nobody patches. Reconcile what is running against
`enterprise/it-operations/it-asset-management` regularly, and treat anything unaccounted for as
urgent — the server nobody owns is the one still running an unsupported operating system.

## Pitfalls

- Repairing a drifted system without correcting the baseline that let it drift.
- Patching on worry rather than cadence.
- Making a change with no back-out plan.
- Leaving a discovered unmanaged system unclaimed.
- Heavyweight approval for trivial changes, which produces unrecorded changes.

## Verification

Track **coverage**, not activity. "Patching is running" is not an answer; "97% of servers are within
30 days, here are the twelve that are not and why" is. Prove drift detection by showing a corrected
system and the baseline change that prevents recurrence, and prove change control by producing the
back-out plan before the change rather than after it.

## Related

- `enterprise/technology/cloud-infrastructure` — designing the environment the product runs in.
- `enterprise/security/vulnerability-management` — decides what is urgent; this executes it.
- `enterprise/it-operations/it-asset-management` — what running systems are reconciled against.
