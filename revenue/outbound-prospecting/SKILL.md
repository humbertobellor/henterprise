---
name: outbound-prospecting
description: "Finds, qualifies, and reaches prospects cold. List building, qualification criteria, cold email and multi-channel sequences, and the follow-up that actually gets replies. Use this to build a prospect list, write cold outreach, fix a sequence that is not getting responses, define qualification criteria, or decide whether a segment is worth pursuing."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: revenue
metadata:
  hermes:
    category: revenue
    tags: [revenue, outbound, cold-email, qualification, deliverability]
    related_skills: [sales-enablement, revenue-operations, chief-revenue-officer, lifecycle-messaging]
---

# Outbound prospecting

Reply rates are set by list quality far more than by copy. Most outbound problems are targeting
problems being solved as writing problems.

## When to Use

- Building a prospect list.
- Writing cold outreach.
- Fixing a sequence that is not getting responses.
- Defining qualification criteria.
- Deciding whether a segment is worth pursuing.

## Procedure

### Build the list before writing anything

Define the qualifying signal — the observable fact that means this account probably has the problem
you solve, right now. Hiring for a role, using a specific tool, a recent funding or expansion
announcement, a public complaint about the thing you fix.

Without a signal you are sending to a demographic, and a demographic has no reason to reply.

Then qualify each account against: do they have the problem, can they afford it, can this person
act, and is there a reason for now. Missing the last one is why good-fit prospects go quiet.

### Writing

- **Under a hundred words.** Longer gets skimmed and deleted.
- **Open with the signal, specifically.** Show you looked. Generic personalization tokens are worse
  than none — they signal automation while pretending otherwise.
- **One problem, in their language**, not your feature.
- **Ask for something small.** A specific question or a fifteen-minute call. "Interested in
  learning more" asks the recipient to do the work of defining the next step.
- **No attachments, minimal links** in a first message. Both hurt deliverability and trust.

### Sequencing

Three to five touches over two to three weeks. Each one adds something new — a different angle, a
relevant case, a useful resource. Never "just bumping this to the top of your inbox," which
communicates that the first message was not worth reading either.

Multi-channel works when the channels are coordinated and the sender is a person. It reads as
harassment when the same message arrives everywhere at once.

Stop after the sequence ends. Persistence past that converts nothing and costs reputation.

### Deliverability

Domain warmed, authentication configured, volume per mailbox kept low, list validated. A technically
broken send makes perfect copy irrelevant, and the damage to a sending domain takes months to
repair.

Use a subdomain for outbound so a reputation problem cannot take down your transactional mail.

## Pitfalls

- Sending to a demographic rather than to a signal.
- Generic personalization tokens, which signal automation while pretending otherwise.
- "Just bumping this," which says the first message was not worth reading either.
- Continuing past the end of the sequence.
- Sending outbound from your primary domain.
- Solving a targeting problem by rewriting copy.

## Verification

Read the results in this order, because each points at a different fix:

- **No opens** — deliverability or subject line. Check deliverability first.
- **Opens, no replies** — the message is not landing. Usually the ask, or an unclear problem
  statement.
- **Replies, no meetings** — a qualification problem: you are reaching people who cannot act.
- **Meetings, no pipeline** — the segment is wrong.

## Related

- `enterprise/revenue/sales-enablement` — what happens once a meeting is booked.
- `enterprise/revenue/revenue-operations` — the qualification definitions and routing.
- `enterprise/demand-generation/lifecycle-messaging` — the opted-in counterpart.
