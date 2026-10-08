---
name: events-and-field-marketing
description: "Plans and runs events that produce pipeline. Conferences, trade shows, webinars, field programs, and measuring whether any of it worked. Use this to decide whether to sponsor an event, plan a conference presence or webinar, design a field program, or work out why event spend is not producing pipeline."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: marketing
metadata:
  hermes:
    category: marketing
    tags: [marketing, events, webinars, field-marketing, pipeline]
    related_skills: [chief-marketing-officer, marketing-campaign-planner, lifecycle-messaging, revenue-operations]
---

# Events and field marketing

Events are the most expensive marketing channel per contact and the easiest to spend badly on,
because the outputs — booth traffic, badge scans, attendance — feel like results and are not.

## When to Use

- Deciding whether to sponsor an event.
- Planning a conference presence or a webinar.
- Designing a field program.
- Working out why event spend is not producing pipeline.

## Procedure

### Decide before you sponsor

The question is never "should we be at this event" but "what specifically do we expect, and what is
that worth." Answer three things first:

- **Who is actually there.** Attendee seniority and function, not the headline number. A
  ten-thousand-person event where forty of your buyers attend is a forty-person event.
- **What the goal is**, and pick one: pipeline from new accounts, advancing deals already open,
  customer retention and advocacy, or category presence. These need different booths, different
  staff, and different follow-up, and an event asked to do all four does none.
- **Total cost.** Sponsorship is often under half. Add booth build, shipping, travel, staff time out
  of the field, and the content produced for it. The fully loaded figure changes decisions.

Small, self-hosted, targeted formats — a dinner for fifteen right accounts, a focused workshop —
routinely outperform large sponsorships per dollar for enterprise pipeline, and are unglamorous
enough that they get proposed rarely.

### Follow-up is where the money is lost

Most event spend is wasted after the event, not during it. A scanned badge is not a lead, and the
value decays in days.

Agree before the event: who follows up, in what timeframe, with what message, and how those contacts
are treated differently from inbound. Route it through
`enterprise/revenue/revenue-operations` so the tracking exists in advance, and hand the sequence to
`enterprise/demand-generation/lifecycle-messaging`.

Score contacts honestly. Everyone who took a branded item is not a lead, and passing them to sales
as if they were is how sales stops working the source at all.

### Webinars and digital formats

Same discipline, different economics. Registration is not attendance and attendance is not interest;
the segment worth pursuing is people who stayed and asked something.

The recording usually outperforms the live event over time, so plan the content as a durable asset —
`enterprise/marketing/content-strategy` and `enterprise/marketing/video-content` — rather than as a
one-time performance.

## Pitfalls

- Sponsoring an event without a single stated goal.
- Reporting badge scans as leads.
- Leaving follow-up ownership undecided until after the event.
- Claiming event-influenced revenue without stating the attribution assumption.
- Costing an event on sponsorship alone, which is often under half the total.
- Treating registration as attendance, or attendance as interest.

## Verification

Events are structurally hard to attribute: they influence deals that close months later through
paths no model captures cleanly. Overclaiming destroys the channel's credibility; refusing to
measure destroys its funding.

Track influenced pipeline **with the assumption stated**, alongside the honest direct-source number,
and compare cost per opportunity against your other channels through
`enterprise/demand-generation/marketing-analytics`.

## Related

- `enterprise/demand-generation/lifecycle-messaging` — the follow-up sequence.
- `enterprise/revenue/revenue-operations` — the tracking that must exist before the event.
- `enterprise/demand-generation/marketing-analytics` — cost per opportunity across channels.
