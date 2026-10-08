---
name: interface-redesign
description: "Upgrades an interface without rebuilding it. Auditing what is there, identifying what reads as generic or unfinished, and sequencing changes by impact. Use this when a product works but looks dated or default, when a redesign is being considered, when deciding whether to restyle or rebuild, or when a screen needs to look substantially better with limited effort."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: product
metadata:
  hermes:
    category: product
    tags: [product, redesign, audit, sequencing, tokens]
    related_skills: [interface-craft, design-system, design-styles, ux-product-auditor]
---

# Interface redesign

Most interfaces do not need rebuilding. They need a dozen specific things fixed, in the right order.

## When to Use

- A product works but looks dated or default.
- A redesign is being considered.
- Deciding whether to restyle or rebuild.
- A screen needs to look substantially better with limited effort.

## Procedure

### Audit first

Go through the real product, on a real device, doing a real task. Record what you find in these
categories — the order is the priority order:

1. **Structural** — unclear primary action, competing focal points, navigation that does not match
   the mental model. These are the only ones worth a rebuild.
2. **Systemic** — inconsistent spacing, more type sizes than a scale would allow, palette drift,
   components that exist in variants. High impact, mechanical to fix.
3. **Craft** — weak hierarchy, poor contrast, unfinished states, cramped density.
4. **Cosmetic** — dated shadows, default border radii, stock illustration.

### Sequencing

Fix in this order, because each makes the next easier to see:

1. Tokens — spacing scale, type scale, palette. This alone resolves most systemic findings.
2. Hierarchy on the two or three highest-traffic screens.
3. States: empty, loading, error, overflow.
4. Component consolidation.
5. Cosmetic pass.

### Restyle or rebuild

Rebuild only when the structure is wrong — when the information architecture does not match how
people work. Everything else is a restyle, and a restyle that ships beats a rebuild that stalls.

## Pitfalls

The generic-product tells. These are the specific things that make a product read as unconsidered,
and they are all cheap to fix:

- Default framework styling left in place — the untouched button, the starter-template card.
- One accent color used for every emphasis, so nothing is emphasized.
- Uniform spacing everywhere, so nothing groups.
- Centered everything, including body copy.
- Emoji standing in for iconography.
- Gradients on surfaces that carry no meaning.
- Empty and error states that were never designed.

And in the approach itself: rebuilding when only the surface is wrong, starting with the cosmetic
pass, and auditing screens rather than doing a real task on a real device.

## Verification

Report findings by category with severity, the sequenced plan, what you would do first if only one
day were available, and what you deliberately are not touching.

The token pass is the checkpoint: after spacing, type, and palette are on a scale, re-walk the same
task and see how many systemic findings survived. Most will not, and the remainder are the real list.

## Related

- `enterprise/product/design-system` — the tokens step 1 fixes.
- `enterprise/product/interface-craft` — the craft layer.
- `enterprise/product/ux-product-auditor` — structural findings, evidenced against outcomes.
