---
name: vendor-management
description: "Selects, contracts, and manages suppliers. Requirements, evaluation, negotiation support, onboarding, performance management, and exit. Use this to choose a vendor, run a selection process, structure a service agreement's operational terms, manage an underperforming supplier, plan an exit or migration, or assess concentration and continuity risk."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: operations
metadata:
  hermes:
    category: operations
    tags: [operations, vendors, evaluation, renewals, exit]
    related_skills: [procurement-and-sourcing, chief-operating-officer, contract-review, business-continuity-and-resilience, it-asset-management]
---

# Vendor management

Everything from requirements through to exit. The pre-signature sourcing process itself belongs to
`enterprise/operations/procurement-and-sourcing`.

## When to Use

- Choosing a vendor, or running a selection process.
- Structuring a service agreement's operational terms.
- Managing an underperforming supplier.
- Planning an exit or a migration.
- Assessing concentration and continuity risk.

## Procedure

### Define requirements before looking at options

Written before any demo: what the vendor must do, the volume and service level required, what must
integrate with what, and the constraints that are genuinely non-negotiable.

Requirements written after seeing a product describe that product. This is the most common way
selections are decided before they are run.

Separate **must-have** from **nice-to-have** and weight them in advance. Weighting after scoring is
how a preferred vendor wins a process designed to be objective.

### Evaluating

- **Reference checks with customers of your size and use case.** A reference running a tenth of your
  volume tells you nothing about whether it scales.
- **Test the actual failure modes**, not the demo path. What happens when data is malformed, volume
  spikes, or an integration times out?
- **Assess the vendor, not just the product** — financial stability, roadmap direction, support
  responsiveness, and whether you are a meaningful customer to them. Being a rounding error to your
  critical supplier is a risk in itself.
- **Total cost including your side**: implementation, integration, migration, training, and the
  ongoing effort to operate it. License cost is frequently the smaller half.

### Terms that matter operationally

Beyond the legal review: service levels with real remedies, support response times by severity,
data export in a usable format on demand, notice periods that give you time to migrate, and price
protection at renewal. The absence of the last two is what makes exit expensive later.

### Managing

- **One named owner** on your side. Vendors without an internal owner drift and renew automatically.
- **Review on a schedule against the service levels**, with evidence. Vendor-supplied performance
  reports mark their own work.
- **Log issues.** At renewal, a documented pattern is leverage; a recollection is not.
- **Diarize renewals well before the notice deadline.** Auto-renewal past an unnoticed deadline is
  the most common and most avoidable vendor loss.

### Concentration and exit

Know which vendors you could not operate without and what happens if one fails, is acquired, or
triples its price. For each, know the exit path and roughly what it costs — an exit plan that has
never been thought through is not an option, it is a hope.

## Pitfalls

- Writing requirements after seeing a product, which describes that product.
- Weighting criteria after scoring.
- Reference checks with customers a fraction of your size.
- Evaluating the demo path rather than the failure modes.
- No named internal owner, so the vendor drifts and renews automatically.
- Accepting vendor-supplied performance reports, which mark their own work.
- Missing a notice deadline — the most common and most avoidable vendor loss.

## Verification

Review on a schedule against the service levels, with your own evidence rather than the vendor's
report. Confirm the renewal notice date is diarized ahead of the deadline, that the issue log exists
and is current, and that data export in a usable format has actually been exercised — not merely
promised.

Maintain your own copy of your data continuously where the vendor holds anything critical.

## Related

- `enterprise/operations/procurement-and-sourcing` — the process before signature.
- `enterprise/legal-risk/contract-review` — the legal terms alongside the operational ones.
- `enterprise/operations/business-continuity-and-resilience` — vendor failure as a continuity event.
