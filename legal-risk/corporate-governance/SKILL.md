---
name: corporate-governance
description: "Maintains the corporate record and governance machinery. Entity records, board and committee support, resolutions and minutes, delegations of authority, insurance, and business continuity. Use this to prepare board or committee materials, record a decision that needs to be minuted, set or check approval authority, review insurance and continuity coverage, establish a retention policy, or work out where a responsibility belongs when it falls between functions."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: legal-risk
metadata:
  hermes:
    category: legal-risk
    tags: [legal-risk, governance, board, delegation, retention]
    related_skills: [chief-legal-and-risk-officer, enterprise-risk, internal-controls-and-audit, business-continuity-and-resilience]
---

# Corporate governance

The record of what the company decided, who was allowed to decide it, and what happens when
something goes wrong. Unglamorous until it is the only thing that matters.

## When to Use

- Preparing board or committee materials.
- Recording a decision that needs to be minuted.
- Setting or checking approval authority.
- Reviewing insurance and continuity coverage.
- Establishing a retention policy.
- Working out where a responsibility belongs when it falls between functions.

## Procedure

### The corporate record

One authoritative place holding: formation and entity documents, ownership and cap table, board and
shareholder resolutions, minutes, signed agreements above the review threshold, insurance policies,
and material licenses and registrations.

The failure mode is not losing a document; it is not knowing which version is current. Every record
carries its effective date, and superseded versions are marked superseded rather than deleted —
"what was in force in March" is a question that gets asked in exactly the circumstances where you
cannot afford to guess.

### Board and committee support

Materials go out with enough notice to actually be read — a deck delivered the night before produces
a meeting where the deck is presented rather than discussed.

Each item is labeled by what it needs: **decide**, **discuss**, or **note**. Meetings run long
because everything is presented as if it needs all three.

Minutes record decisions, who was present, who abstained or recused, and the basis on which a
decision was taken. They are not a transcript. Where a decision was contested, that is worth
recording — it is evidence the board exercised judgment rather than rubber-stamping.

### Delegations of authority

Write down who can commit the company to what, at which value, and what requires escalation. Cover
spending, contracts, hiring, and anything creating a long-term obligation.

Two failures, both common: thresholds so low that everything escalates and the process is routed
around, and thresholds nobody wrote down, so authority is whatever was not challenged last time.

Review after any material change in size or structure.

### Insurance and continuity

Know what is covered, what is excluded, what the limits are, and who to call. The exclusions matter
more than the coverage and are read least.

For continuity: what are the handful of things the business cannot operate without, what happens if
each is unavailable for a week, and who decides.

### Records retention

A policy naming, per record type, how long it is kept and what happens at the end. Then a mechanism
that actually enforces it, because retention by intention keeps everything forever.

Retention periods are set by statute and by what you might need to defend, whichever is longer.

### Orphaned responsibilities

Some responsibilities sit between functions and get dropped. When one appears, do not debate the
right home in the abstract — assign it to whoever bears the consequence if it fails, and record the
assignment. An owner who is imperfect beats an owner who is undecided.

## Pitfalls

- Deleting a superseded record instead of marking it superseded, so "what was in force in March"
  cannot be answered.
- Sending board materials the night before, which produces presentation rather than discussion.
- Thresholds so low everything escalates, or thresholds nobody wrote down.
- A retention policy with no enforcing mechanism, which keeps everything forever.
- Destroying anything under a legal hold, or not knowing who can place one.
- Debating the right home for an orphaned responsibility instead of assigning it.

## Verification

An untested continuity plan is a document, not a capability — walk through one scenario annually
rather than writing more of them. For governance itself: confirm every record carries an effective
date, that the delegation of authority is written and current after any material change in size or
structure, and that the retention policy has a mechanism behind it rather than an intention.

## Related

- `enterprise/legal-risk/enterprise-risk` — the register the board reviews.
- `enterprise/finance/internal-controls-and-audit` — approval thresholds as a financial control.
- `enterprise/operations/business-continuity-and-resilience` — the operational depth behind continuity.
