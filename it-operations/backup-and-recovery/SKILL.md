---
name: backup-and-recovery
description: "Protects and restores data. Backup coverage and scope, retention, immutability against ransomware, and proving restores actually work. Use this to design a backup regime, verify restores, plan retention, protect backups from ransomware, or recover from data loss."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: it-operations
metadata:
  hermes:
    category: it-operations
    tags: [it-operations, backup, restore, ransomware, retention]
    related_skills: [chief-information-officer, systems-administration, it-asset-management, business-continuity-and-resilience]
---

# Backup and recovery

Nobody wants backups; they want restores. The distinction is not pedantic — organizations discover
the difference during the only event that matters.

Recovery objectives and which processes must survive are set by
`enterprise/operations/business-continuity-and-resilience`. This skill delivers against them.

## When to Use

- Designing a backup regime.
- Verifying restores.
- Planning retention.
- Protecting backups from ransomware.
- Recovering from data loss.

## Procedure

### Coverage is where it fails first

Most backup gaps are things nobody thought to include: a database somebody stood up outside the
standard process, configuration that only exists in a running system, data in a SaaS platform assumed
to be the vendor's responsibility, or a developer's machine holding the only copy of something.

Reconcile backup coverage against the asset register from
`enterprise/it-operations/it-asset-management` on a cadence and treat the difference as a finding. An
untested assumption of coverage is the normal state of affairs.

Note that SaaS providers protect against **their** failures, not against your deletion or a malicious
insider. Read what the contract actually commits to, rather than what the marketing implies.

### The 3-2-1 shape, and why the offline copy matters

Three copies, two media or platforms, one off-site — and, since ransomware, **one immutable or
offline**.

Modern ransomware deliberately targets backups first, using the credentials it found on the way in.
A backup system reachable with production credentials will be encrypted alongside production.
Immutable storage or genuinely offline copies are what survive this, and it is the difference
between an outage and an extinction event.

### Retention is a policy decision, not a storage one

Retention has to satisfy operational recovery, legal and regulatory obligations, and data protection
requirements — which pull in opposite directions. Data protection law obliges deletion of personal
data you no longer have a basis to keep, and indefinite backup retention conflicts with that
directly. Settle it with `enterprise/legal-risk/privacy-and-data-protection`.

Know how you would satisfy a deletion request that touches backups, before one arrives.

## Pitfalls

- Reporting backup health from job success rather than tested restores.
- Leaving backups reachable with production credentials.
- Setting retention without reconciling legal obligation against deletion duty.
- Quoting an RTO you have not measured by actually restoring.
- Assuming a SaaS platform's own resilience covers your deletion or a malicious insider.

## Verification

Test restores, or you have nothing. A backup job reporting success proves a file was written. It says
nothing about whether the data is complete, uncorrupted, or restorable in a usable time.

Test on a schedule, restore to a separate environment, and verify the application actually works on
the restored data rather than that the bytes arrived. Record how long it took — that measurement is
the only honest input to an RTO, and it is invariably longer than assumed.

Test the full-scale case at least annually. Restoring one file proves the mechanism; restoring the
system proves the plan.

## Related

- `enterprise/operations/business-continuity-and-resilience` — sets the RTO and RPO this delivers against.
- `enterprise/it-operations/it-asset-management` — the register coverage is reconciled against.
- `enterprise/legal-risk/privacy-and-data-protection` — the deletion duty that limits retention.
