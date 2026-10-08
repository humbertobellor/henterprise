---
name: support-operations
description: "Designs and runs the support function. Channels, queues, routing, staffing, service levels, quality, and the metrics that show whether it is working. Use this to set up or fix support operations, choose channels, size a team, set or renegotiate service levels, reduce cost per contact, diagnose long queues or poor quality, or decide what to automate."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: customer-experience
metadata:
  hermes:
    category: customer-experience
    tags: [customer-experience, support, staffing, service-levels, queues]
    related_skills: [chief-customer-officer, self-service-and-knowledge, escalation-management, service-level-management]
---

# Support operations

The operating design of the support function: what generates contacts, how they are handled, and at
what cost.

## When to Use

- Setting up or fixing support operations.
- Choosing channels, or sizing a team.
- Setting or renegotiating service levels.
- Reducing cost per contact.
- Diagnosing long queues or poor quality.
- Deciding what to automate.

## Procedure

### Understand demand before designing supply

Categorize a real sample of recent contacts — a few hundred, read individually, not a report. Almost
every support operation finds the same shape: a small number of causes generating most of the
volume, and most of those are preventable rather than answerable.

That analysis decides everything downstream. Staffing to demand you have not examined means staffing
to demand you could have eliminated.

### The hierarchy of handling

In order of cost, cheapest first. Push volume up this list rather than getting faster at the bottom:

1. **Eliminate** — fix the product defect or confusing flow generating the contact.
2. **Deflect** — answer it in the interface at the moment of confusion, not in a help center nobody
   visits.
3. **Self-serve** — findable documentation for people who go looking.
4. **Automate** — genuine resolution of routine requests, not a bot that stalls people before a
   human.
5. **Assist** — a person.

Most support improvement programs work on level 5 exclusively, because it is the visible one.

### Channels

Pick by what the work needs, not by what is fashionable. Asynchronous channels are cheaper and
better for anything requiring investigation. Synchronous channels are worth their cost for urgency,
high-value accounts, and anything where a customer is stuck mid-task.

Every channel you open must be staffed to its expectation. An unstaffed live-chat widget is worse
than no chat.

### Service levels

Set by severity and customer tier, published internally, and — this is the part usually missing —
**checked against actual capacity before being promised**. A commitment the staffing cannot meet is
a commitment to fail visibly.

Measure first response and time to resolution separately. They have different causes: first response
is a staffing problem, resolution is usually a product or escalation problem.

### Staffing

Size to peak-hour concurrency, not to daily volume — queues form in hours, not days. Model the
shrinkage honestly: training, breaks, meetings, leave. A plan assuming full utilization understaffs
by a wide margin and then blames the team.

### Quality

Review a sample of resolved contacts against a rubric agreed with the team, and coach against it.
Reviewing only escalations trains for defense rather than quality.

## Pitfalls

- Working exclusively on level 5 of the hierarchy, because it is the visible one.
- Opening a channel you cannot staff to its expectation.
- Promising a service level without checking it against actual capacity.
- Sizing staff to daily volume rather than peak-hour concurrency, and assuming full utilization.
- Leaning on time-to-close and volume handled. Both are easily gamed and both reward closing over
  solving.
- Reviewing only escalations, which trains for defense rather than quality.

## Verification

Report against metrics that mean something:

- **Contacts per active customer**, trending. The only metric that captures whether the product is
  getting better rather than the team getting faster.
- **First-contact resolution** — reopens are the honest signal.
- **Backlog age distribution**, not average age. Averages hide the tickets rotting at the back, and
  those are the ones that become complaints.
- **Customer-effort**, asked at resolution.

## Related

- `enterprise/customer-experience/chief-customer-officer` — owns the service-level commitments.
- `enterprise/customer-experience/self-service-and-knowledge` — levels 2 and 3 of the hierarchy.
- `enterprise/operations/service-level-management` — service levels across the whole business.
