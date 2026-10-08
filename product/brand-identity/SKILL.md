---
name: brand-identity
description: "Defines and applies visual brand. Logo usage, palette, typography, imagery direction, and the guidelines that keep expression consistent across product and marketing surfaces. Use this to establish a brand from scratch, audit whether an existing brand is being applied consistently, build brand guidelines, or decide how a brand should express itself in an unfamiliar format."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: product
metadata:
  hermes:
    category: product
    tags: [product, brand, palette, typography, guidelines]
    related_skills: [design-system, interface-craft, brand-voice, visual-content]
---

# Brand identity

Brand is the accumulated impression of every surface someone encounters. Consistency is most of it;
the rest is having a point of view.

## When to Use

- Establishing a brand from scratch.
- Auditing whether an existing brand is applied consistently.
- Building brand guidelines.
- Deciding how a brand should express itself in an unfamiliar format.

## Procedure

### Establishing

Before any visual decision, settle three things in writing:

- **What the brand is for** — the promise it makes, in one sentence.
- **Who it is for** — and, more usefully, who it is not for.
- **What it is not** — the three adjectives it should never earn. These constrain far better than
  aspirational ones, because "modern" and "trustworthy" rule nothing out.

### The system

**Palette.** One primary, one accent, a full neutral ramp, and semantic states. The neutral ramp does
most of the visible work and gets the least attention — spend time on it. Every color needs a
verified contrast ratio against the surfaces it will actually sit on, not against white.

**Typography.** One display family, one text family, and a rule for when each is used. Both must
work at the smallest size they will appear at, on a real device, before selection.

**Logo.** Define clear space, minimum size, and permitted variants. Then define misuse explicitly:
no stretching, no recoloring outside the permitted set, no effects, no re-typesetting the wordmark.
Guidelines fail by omission — what is not forbidden gets done.

**Imagery.** A stated direction, with examples of both what fits and what does not. "Authentic
photography" means nothing without a counter-example.

### Applying

The test of a brand system is an unfamiliar format: an error email, a conference badge, a slide
nobody planned for. If the system does not say what to do, it is a mood board, not a system.

## Pitfalls

- Aspirational adjectives — "modern," "trustworthy" — which rule nothing out.
- Verifying contrast against white rather than against the surfaces the color will sit on.
- Choosing type without testing it at the smallest size it will appear at, on a real device.
- Guidelines that say what is permitted and not what is forbidden. What is not forbidden gets done.
- An imagery direction with no counter-example.
- Neglecting the neutral ramp, which does most of the visible work.

## Verification

Audit against real surfaces — product, marketing site, email, social, sales collateral — placed side
by side. Look for palette drift, more type families than the system defines, logo variants nobody
sanctioned, and tone that changes between surfaces.

Report by severity, and separate what breaks the system from what merely was not specified. The
second category is the backlog for the guidelines themselves.

## Related

- `enterprise/product/design-system` — the tokens the brand resolves into.
- `enterprise/marketing/brand-voice` — the verbal counterpart.
- `enterprise/marketing/visual-content` — where the system gets applied at volume.
