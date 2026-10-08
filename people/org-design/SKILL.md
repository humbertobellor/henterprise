---
name: org-design
description: "Designs how an organization is structured. Reporting lines, team boundaries, spans and layers, role definition, and workforce planning against the strategy. Use this to structure a new team, restructure an existing one, resolve unclear ownership between teams, plan headcount, or diagnose why a team underperforms for structural rather than individual reasons."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: people
metadata:
  hermes:
    category: people
    tags: [people, org-design, spans, ownership, restructuring]
    related_skills: [chief-human-resources-officer, workforce-planning, compensation-and-leveling, agent-hierarchy]
---

# Org design

Structure determines what is easy and what requires heroics. Most persistent coordination problems
are structural and cannot be fixed by asking people to communicate better.

## When to Use

- Structuring a new team, or restructuring an existing one.
- Resolving unclear ownership between teams.
- Planning headcount.
- Diagnosing why a team underperforms for structural rather than individual reasons.

## Procedure

### Design from the work

Start with the work that must happen and its natural boundaries — where handoffs are expensive, and
where they are cheap. Draw team lines at the cheap handoffs.

Then check: can each team deliver something meaningful without waiting on another? A team that
cannot ship without three dependencies is not a team, it is a queue.

**Design the org for the work, not around the people currently in it.** Then reconcile deliberately,
noting where you have compromised and why. Structures built around individuals fail when those
individuals leave, and everyone can see they were built that way.

### Spans and layers

Wide spans push decisions down and starve people of attention. Narrow spans give attention and breed
layers, which add latency to every decision.

Roughly: five to nine reports for a manager whose people need coaching; more where the work is
consistent and the people are experienced. Every layer must add decision value — a layer that only
passes information along should be removed, and it is usually obvious which one it is.

### Ownership

Every outcome has exactly one owner. Where two teams share an outcome, neither owns it, and it fails
in the gap. Where an owner lacks the authority to deliver, the accountability is fictional.

Write down the boundaries — what each team decides alone, what needs consultation, what needs
approval. Ambiguity between senior teams is expensive and does not resolve itself.

### Restructuring

- Say why, plainly, and what problem it solves. People fill silence with worse explanations than the
  truth.
- Announce the whole change at once. Serial reorganizations cost more in sustained uncertainty than
  one larger change.
- Anything touching an individual's role, level, or pay goes through the people function before
  announcement, without exception.

## Pitfalls

- Restructuring to avoid a performance conversation.
- Creating a role to retain someone the structure does not need.
- Leaving an outcome with two owners.
- Designing around the people currently in the seats.
- A layer that only passes information along.
- Serial reorganizations, which cost more in sustained uncertainty than one larger change.

## Verification

Test the design against the work: can each team deliver something meaningful without waiting on
another? Every outcome traced to exactly one owner who has the authority to deliver it — where they
do not, the accountability is fictional and the design is not finished.

Write the decision boundaries down: what each team decides alone, what needs consultation, what needs
approval. If those cannot be stated, the ambiguity will be discovered later and expensively.

## Related

- `enterprise/people/workforce-planning` — the same decision spread over twelve months.
- `enterprise/people/compensation-and-leveling` — levels must describe real scope.
- `enterprise/executive/agent-hierarchy` — the same split applied to an agent roster.
