---
name: visual-reference-generation
description: "Produces design reference imagery before building. Screen concepts, layout directions, and flows for web or mobile that make a verbal brief concrete enough to argue with. Use this when a brief needs visualizing before anyone builds, when comparing layout directions, when handing a developer a target, or when stakeholders are describing different things with the same words."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: product
metadata:
  hermes:
    category: product
    tags: [product, concepts, mockups, mobile, web]
    related_skills: [design-styles, interface-craft, design-system, presentation-design]
---

# Visual reference generation

Arguing about an image costs an hour. Arguing about a build costs a sprint. Generate the picture
first.

## When to Use

- A brief needs visualizing before anyone builds.
- Comparing layout directions.
- Handing a developer a target.
- Stakeholders are describing different things with the same words.

## Prerequisites

Settle these, or the output is decoration:

- **Surface and platform** — web page, native mobile screen, dashboard. These are not the same
  problem at different aspect ratios: touch targets, native chrome, and scroll behavior change what
  a good layout is.
- **What it optimizes for** — one conversion, one task completion, one first impression. Stated, so
  the image can be judged against something.
- **Content reality** — real headline lengths, real data volumes, real edge cases. A concept built
  on three-word labels collapses on contact with actual copy.

## Procedure

### Generating

- **One concept per image.** Tiling several ideas onto one canvas makes them impossible to compare
  or iterate separately.
- **Generate genuinely different directions**, not variations of one. Three near-identical options
  is one option presented three times.
- Include the states that will exist: a populated view and an empty one, at minimum.

### Web versus mobile

**Web** — the fold is a real constraint but not a hard one; horizontal space allows genuine layout
choices; hover exists. Design for a range of widths, and decide what the narrow case does.

**Mobile** — thumb reach dictates where primary actions sit; native navigation patterns are
expectations, not suggestions; there is no hover, so affordance must be visible. Design the scroll,
not the screenshot.

## Pitfalls

- Generating before surface, optimization target, and content reality are settled.
- Tiling several concepts onto one canvas.
- Three near-identical options, which is one option presented three times.
- Concepts built on three-word labels, which collapse on contact with real copy.
- Treating a mobile screen as a web page at a different aspect ratio.
- Designing the screenshot rather than the scroll.

## Verification

Say explicitly what in the reference is **direction** and what is **placeholder**. A developer
handed a concept will otherwise implement the lorem ipsum faithfully.

Judge each concept against the stated optimization target, not against taste, and check it holds with
real headline lengths, real data volumes, and the empty state included.

## Related

- `enterprise/product/design-styles` — the direction the concept expresses.
- `enterprise/product/design-system` — the tokens the build will actually use.
- `enterprise/product/interface-craft` — turning an accepted concept into a finished screen.
