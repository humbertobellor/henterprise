---
name: it-asset-management
description: "Tracks hardware and software assets through their life. Procurement, ownership, licensing, refresh, and disposal. Use this to build an asset register, prepare for a software audit, plan a refresh cycle, control license spend, or dispose of equipment safely."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: it-operations
metadata:
  hermes:
    category: it-operations
    tags: [it-operations, asset-register, licensing, refresh, disposal]
    related_skills: [chief-information-officer, endpoint-management, systems-administration, backup-and-recovery]
---

# IT asset management

The register exists to answer operational questions: what do we have, who has it, is it supported, is
it licensed, and when does it need replacing. An inventory that answers none of those is an
accounting artifact.

## When to Use

- Building an asset register.
- Preparing for a software audit.
- Planning a refresh cycle.
- Controlling license spend.
- Disposing of equipment safely.

## Procedure

### One register, reconciled against reality

A register maintained by hand diverges immediately. Feed it from discovery — what is actually on the
network and enrolled in management — and reconcile against procurement and finance records.

The valuable output is the **discrepancy list**: assets in the register that discovery cannot find,
and devices discovery finds that the register does not know about. The second category is the
security problem, since an unknown device is unmanaged by definition.

### Ownership, not just location

Every asset needs a named accountable person. "The engineering team" is not an owner; when the device
needs patching, returning or replacing, a team does not answer.

Track state through the lifecycle — ordered, in stock, assigned, in repair, retired, disposed — and
require the state change at the moment of handover. A register updated in batches is a register that
is wrong between batches, which is most of the time.

### Software licensing

Under-licensing is a financial and legal exposure that surfaces at audit; over-licensing is money
spent on nothing, and it is usually the larger number.

Reconcile entitlements against actual installs and actual use. Reclaiming licenses from people who
stopped using a tool typically funds a meaningful fraction of the next renewal, and the data for it
already exists.

Watch license models that change cost with infrastructure — per-core, per-socket, per-user in a
system that provisions freely. A routine infrastructure change can multiply a license bill with no
procurement decision anywhere in the path.

### Refresh and disposal

Plan refresh on a cycle and budget it as a steady cost through
`enterprise/finance/budgeting-and-forecasting`. Refresh driven by failure produces an unpredictable
expense and a worse experience, and it always arrives at the wrong moment.

Disposal is where data escapes. Require certified destruction or verified wipe, keep the certificate,
and treat storage devices as data until proven otherwise. A drive in a cupboard nobody logged is a
breach with no date attached.

## Pitfalls

- Maintaining a register by hand and trusting it.
- Recording a team as an asset owner.
- Renewing licenses without reconciling against actual use.
- Disposing of storage without evidence of destruction or wipe.
- Updating the register in batches, so it is wrong between them.
- Missing license models that scale with infrastructure rather than with procurement decisions.

## Verification

The discrepancy list is the output that proves the register: assets recorded but not discovered, and
devices discovered but not recorded — the second being a security finding, since an unknown device is
unmanaged by definition. Confirm every asset has a named person, that entitlements reconcile against
actual installs and use, and that every disposal has its destruction or wipe certificate on file.

## Related

- `enterprise/it-operations/endpoint-management` — the discovery feed for the fleet.
- `enterprise/it-operations/backup-and-recovery` — coverage is reconciled against this register.
- `enterprise/operations/procurement-and-sourcing` — how assets enter the lifecycle.
