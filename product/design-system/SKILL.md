---
name: design-system
description: "Builds and maintains the design system. Tokens for color, type, spacing and elevation, component contracts, and the rules that keep them coherent as the product grows. Use this when starting a new interface, when screens have drifted apart visually, when the same component exists three times in slightly different forms, or when a token or component needs adding without breaking what exists."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: product
metadata:
  hermes:
    category: product
    tags: [product, design-system, tokens, components, accessibility]
    related_skills: [interface-craft, design-styles, brand-identity, interface-redesign]
---

# Design system

A design system is a set of constraints that makes consistency the cheap path. If the system is
harder to follow than to ignore, it will be ignored.

## When to Use

- Starting a new interface.
- Screens have drifted apart visually.
- The same component exists three times in slightly different forms.
- A token or component needs adding without breaking what exists.

## Procedure

### Tokens first

Define the primitives before any component. Every visual decision references a token; nothing
hard-codes a value.

- **Color** — semantic names, not literal ones. `surface`, `surface-raised`, `text-primary`,
  `text-muted`, `border`, `accent`, `danger`. A token named `blue-500` cannot be re-themed.
- **Type** — a scale with a stated ratio, and a line-height per step. Four to six steps. More than
  that and nobody can tell them apart.
- **Spacing** — one scale, geometric, used for every gap and inset. Arbitrary spacing is the single
  most common source of "it looks off but I can't say why."
- **Radius, elevation, motion** — small closed sets. Two or three each.

Every token needs a light and dark value defined together. Adding dark mode later means auditing
every surface.

### Component contracts

A component in the system carries: the states it supports (default, hover, focus, active, disabled,
loading, error, empty), the props that vary it, and what it will *not* do. The last one matters
most — a component that accepts arbitrary overrides is a styling function, not a component.

Every interactive component needs a visible focus state and a target big enough to hit. This is not
a polish item; it is whether people can use it.

### Growth rules

- A new component enters the system only after the same need appears three times. Before that it is
  local.
- Changing a token is a system-wide change — treat it like an API change, because it is.

## Pitfalls

- Literal color names. A token called `blue-500` cannot be re-themed.
- More type steps than anyone can distinguish.
- Arbitrary spacing outside the scale — the source of "it looks off but I can't say why."
- Defining dark values later, which means auditing every surface.
- A component that accepts arbitrary overrides. That is a styling function, not a component.
- Removing a token or component because it looks unused. You cannot see every consumer from inside
  the system — deprecate, announce, then remove.

## Verification

Report tokens added or changed, components affected, anything now inconsistent with the system, and
what needs migrating.

Treat a token change like an API change: enumerate consumers before making it, and announce a
deprecation rather than a removal. A component is only in the system once its full state set —
default, hover, focus, active, disabled, loading, error, empty — is defined, not just its default.

## Related

- `enterprise/product/interface-craft` — applying the system well on a given screen.
- `enterprise/product/design-styles` — the direction the token values express.
- `enterprise/product/brand-identity` — where the palette and type come from.
