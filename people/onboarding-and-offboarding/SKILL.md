---
name: onboarding-and-offboarding
description: "Designs the joining and leaving experience. First-day readiness, ramp to productivity, knowledge capture, and clean exits. Use this to design or fix onboarding, shorten time to productivity, structure a leaver process, capture knowledge before someone leaves, or coordinate the access and asset steps around a joiner or leaver."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: people
metadata:
  hermes:
    category: people
    tags: [people, onboarding, offboarding, knowledge-capture, ramp]
    related_skills: [hiring-and-interviewing, identity-lifecycle-administration, endpoint-management, chief-human-resources-officer]
---

# Onboarding and offboarding

Both ends are cross-functional processes that fail at the handoffs. The failures are predictable,
which means they are preventable by design rather than by diligence.

## When to Use

- Designing or fixing onboarding.
- Shortening time to productivity.
- Structuring a leaver process.
- Capturing knowledge before someone leaves.
- Coordinating the access and asset steps around a joiner or leaver.

## Procedure

### Onboarding starts before day one

Everything procurable in advance should be ready: accounts, hardware, access, a first assignment, and
a named person responsible for the human side. A first day spent waiting for a laptop is a permanent
first impression, and it is entirely a coordination failure.

The identity and equipment steps are executed by
`enterprise/it-operations/identity-lifecycle-administration` and
`enterprise/it-operations/endpoint-management`; access policy — what a role should be entitled to —
belongs to `enterprise/security/access-and-identity`. This skill owns the sequence and whether it
actually completed.

### Ramp deliberately

Separate the three things a new person is learning, because they need different support:

- **The job** — often the part they already have.
- **The context** — the systems, the codebase, the customers, the history.
- **The people** — who decides what, who to ask, how things really get done.

The third is the one nobody plans and the one that most determines how quickly someone becomes
useful. Make introductions explicit assignments rather than leaving them to chance and extroversion.

Give real work early, scoped to succeed. A meaningful contribution in the first fortnight does more
for confidence and belonging than any amount of orientation material.

### Offboarding: knowledge before access

Knowledge capture has to precede the access cutoff, which means starting on the day notice is given,
not the day before departure.

Prioritize what is genuinely undocumented and only in one head: the systems they alone maintain, the
relationships they hold, the decisions whose reasoning exists nowhere. Ask directly — "what will
break, and who will not know why?" — because they know and will usually say.

Then run the mechanical steps as a checklist with an owner: access revoked across every system
including those outside single sign-on, assets returned, delegations and approvals reassigned, and
handover confirmed by the person receiving it rather than by the person leaving.

## Pitfalls

- Letting a start date arrive without access and equipment confirmed ready.
- Leaving relationship introductions to chance.
- Cutting access before knowledge capture has happened.
- Collecting exit feedback nobody ever reads in aggregate.
- Confirming handover with the person leaving rather than the person receiving.

## Verification

Check in at deliberate intervals — a week, a month, a quarter — with the question phrased so problems
can surface. "What has been more confusing than it should be?" gets an answer; "how's it going?" does
not.

Exits are data. Exit conversations produce candid information that is unavailable any other way, and
it is routinely collected and never used. Aggregate themes over time and look by manager and by team;
a single exit is an anecdote, a pattern across four is a finding for
`enterprise/people/chief-human-resources-officer`.

## Related

- `enterprise/it-operations/identity-lifecycle-administration` — executes the access steps.
- `enterprise/it-operations/endpoint-management` — equipment and wipe.
- `enterprise/people/hiring-and-interviewing` — everything before the start date.
