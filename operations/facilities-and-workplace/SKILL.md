---
name: facilities-and-workplace
description: "Runs the physical and hybrid workplace. Space planning, leases, health and safety, office services, and the operational side of where people work. Use this to plan space, evaluate a lease or office move, set up a hybrid workplace, handle facilities incidents, or decide what office services are worth funding."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: operations
metadata:
  hermes:
    category: operations
    tags: [operations, facilities, workplace, leases, health-and-safety]
    related_skills: [chief-operating-officer, vendor-management, capital-allocation, contract-review]
---

# Facilities and workplace

Facilities is invisible when it works and is the loudest topic in the company when it does not. It
is also, after payroll, frequently the largest fixed commitment a business makes.

> Occupational health and safety, accessibility, and building compliance are legally regulated and
> vary by jurisdiction — and in the United States by state as well as federally. This structures the
> decision and names what to ask; it is not a substitute for qualified advice or a licensed
> inspection.

## When to Use

- Planning space.
- Evaluating a lease or an office move.
- Setting up a hybrid workplace.
- Handling facilities incidents.
- Deciding what office services are worth funding.

## Procedure

### Space follows how people actually work

Plan from observed attendance, not from headcount or from policy. A hybrid organization with a
three-day expectation does not need desks for everyone, and does need more of the rooms people
compete for — small meeting spaces and focus rooms, which are chronically undersupplied because
they are easy to convert into desks.

Measure before committing: actual peak occupancy by day, room utilization, and what people leave
the building to do. Most offices are simultaneously too large in aggregate and too small on
Wednesday.

### Leases are the commitment nobody models

A lease is a multi-year fixed obligation signed on a headcount forecast that will be wrong. Treat it
as the capital decision it is — `enterprise/finance/capital-allocation` for the appraisal,
`enterprise/legal-risk/contract-review` for the terms.

The terms that matter later: break clauses and what they cost, expansion and contraction rights,
what "restore to original condition" obliges you to spend at exit, and who pays for what when the
building fails. Dilapidations at lease end routinely surprise organizations that never read the
clause.

### Health, safety, and the duty of care

The obligation follows the worker, not the building. Home workers, field staff and contractors are
in scope in most jurisdictions, which organizations discover late.

Keep the fundamentals current and evidenced: risk assessments, fire and evacuation, first aid,
accident recording, and the statutory inspections the building requires.

Physical access control sits with `enterprise/security/access-and-identity` for policy; site
incidents that disrupt operations escalate to
`enterprise/operations/business-continuity-and-resilience`.

### Office services, and what is worth funding

Services are judged on whether they remove friction, not on generosity. Reliable connectivity,
rooms that work on the first attempt, and somewhere to take a call beat perks that photograph well.

This absorbs the administrative-services function — mail, reception, supplies, workplace vendors —
which sits here rather than as a separate department, alongside
`enterprise/operations/vendor-management` for the suppliers delivering it.

## Pitfalls

- Sizing space from headcount rather than observed occupancy.
- Signing a lease without modeling the exit and the dilapidations.
- Treating health and safety as applying only to the office.
- Funding visible perks while rooms and connectivity fail daily.
- Converting focus and meeting rooms into desks because they are the easy conversion.

## Verification

Evidence produced as a by-product of doing the work survives scrutiny; evidence assembled after an
incident does not. Confirm risk assessments, evacuation, first aid, accident records, and statutory
inspections are current and dated.

For space, report observed peak occupancy by day and room utilization against the committed
footprint — not headcount. For a lease, report the exit cost, including dilapidations, alongside the
rent.

## Related

- `enterprise/finance/capital-allocation` — a lease is a capital decision.
- `enterprise/legal-risk/contract-review` — the lease terms themselves.
- `enterprise/operations/business-continuity-and-resilience` — site failure.
