---
name: threat-modeling
description: "Identifies what could go wrong before it is built. The assets worth attacking, the entry points, the trust boundaries, and the controls that actually address the realistic threats. Use this when designing a feature or system, when a change touches authentication, data handling, payments, or external input, before a security review, or when deciding which security work is worth doing at all."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: security
metadata:
  hermes:
    category: security
    tags: [security, threat-modeling, trust-boundaries, design, stride]
    related_skills: [security-architecture-review, chief-information-security-officer, solution-architecture, enterprise-risk]
---

# Threat modeling

Done at design time this is cheap and changes the design. Done after launch it produces a list of
things that are expensive to fix, so the timing is most of the value.

## When to Use

- Designing a feature or system.
- A change touches authentication, data handling, payments, or external input.
- Before a security review.
- Deciding which security work is worth doing at all.

## Procedure

### 1. What are we building?

A diagram of the actual data flow — not the org chart, not the marketing architecture. Components,
the data moving between them, and where each store lives. If nobody can draw it, that is the first
finding.

Mark the **trust boundaries**: every point where data crosses from something you control to
something you do not, or from one privilege level to another. Almost every real vulnerability lives
on a boundary.

### 2. What can go wrong?

Walk each boundary and each asset. A usable prompt set:

- **Spoofing** — can someone claim to be another user, service, or system?
- **Tampering** — can data be modified in transit, at rest, or in the client?
- **Repudiation** — can someone deny an action, and would we be able to show otherwise?
- **Information disclosure** — what leaks: to other users, to logs, to error messages, to the
  client bundle?
- **Denial of service** — what is unbounded? Uploads, queries, retries, fan-out.
- **Elevation of privilege** — can a user reach data or actions belonging to another tenant, role,
  or account?

Two that catch more real bugs than the classic list: **what does the client enforce that the server
does not**, and **what happens on the second attempt** — replay, race, and double-submit.

### 3. What are we going to do about it?

For each realistic threat: mitigate, transfer, avoid, or accept. Accepting is legitimate; accepting
silently is not.

Prioritize by attacker effort against impact, not by how alarming it sounds. A trivially exploitable
tenant-isolation bug outranks a theoretical timing attack every time.

### Scoping

Model per feature or per boundary, not per system. A whole-system model is too big to finish and too
vague to act on.

Timebox it. An hour on a specific feature with the engineers who will build it beats a week-long
exercise producing a document nobody reads.

## Pitfalls

- Modeling the system as designed rather than as built. Ask what actually got shipped.
- Assuming internal traffic is trusted. That assumption is what turns one compromised service into
  an incident.
- Accepting "the framework handles that" without checking that it is configured to.
- Prioritizing by how alarming a threat sounds rather than by attacker effort against impact.
- Accepting a threat silently.
- Modeling a whole system, which is too big to finish and too vague to act on.

## Verification

Re-check the model when the design changes. A threat model that describes last quarter's
architecture is worse than none, because it produces false confidence.

The output is checkable: a data-flow diagram someone can draw, the trust boundaries marked, each
boundary walked against the prompt set, and every realistic threat carrying a decision — mitigate,
transfer, avoid, or accept with a name against it.

## Related

- `enterprise/security/security-architecture-review` — the same questions, later and more expensive.
- `enterprise/technology/solution-architecture` — the design this examines.
- `enterprise/legal-risk/enterprise-risk` — where accepted threats are registered.
