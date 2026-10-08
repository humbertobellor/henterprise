---
name: visual-content
description: "Designs the visual assets that carry content. Carousels, infographics, quote graphics, diagrams, and social imagery, including the generation prompts where they are AI-produced. Use this to turn a written piece into a visual format, design a carousel or infographic, create social graphics, or fix visuals that are not stopping the scroll."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: marketing
metadata:
  hermes:
    category: marketing
    tags: [marketing, visual-design, carousels, infographics, generated-imagery]
    related_skills: [social-post-craft, brand-identity, video-content, design-system]
---

# Visual content

The visual assets that carry content, and the format decision that comes before any of them.

## When to Use

- Turning a written piece into a visual format.
- Designing a carousel or an infographic.
- Creating social graphics.
- Fixing visuals that are not stopping the scroll.

## Procedure

### The format follows the content's shape

- **Sequence or process** → carousel. One step per slide, one idea per slide.
- **Comparison or relationship** → single diagram. A carousel would break what needs to be seen at
  once.
- **A single memorable claim** → quote graphic.
- **Quantity, trend, or proportion** → chart, with one message.
- **Anything with more than about seven elements** → it is two visuals.

Choosing format by what is fashionable rather than by the content's shape is why so many carousels
are a paragraph cut into ten pieces.

### Carousels

The first slide is the entire hook — treat it as a headline, not a title card. Every subsequent
slide must earn the swipe, which means each ends slightly incomplete.

Consistent template across slides: same margins, same type positions, same palette. Variation across
slides reads as error. Number them so the reader knows the commitment.

Last slide lands the idea. A last slide that only says "follow for more" wastes the only slide with
guaranteed attention from everyone who finished.

### Infographics and diagrams

A diagram earns its place when it shows a relationship prose would take three paragraphs to
establish. If it restates the text, cut it.

Label directly on the element. Legends make the reader hold a mapping in memory while looking
elsewhere. Strip anything not carrying meaning — decorative gradients, 3D effects, and drop shadows
on data.

### Designing for the actual context

Almost all of this is seen small, on a phone, in a feed, at speed. Test at that size before
finishing. If the headline is not readable at thumbnail scale, it does not exist.

High contrast between subject and background is what stops the scroll. Subtlety is a desktop luxury.

### Where images are generated

Write the prompt as a brief: subject, composition, lighting, palette, mood, and negative
constraints. Generate one concept per image.

## Pitfalls

- Choosing format by fashion rather than by the content's shape — which is why so many carousels are
  a paragraph cut into ten pieces.
- A first slide that reads as a title card rather than a headline.
- A last slide that only says "follow for more," wasting the one slide with guaranteed attention.
- A diagram that restates the text.
- Legends where direct labels would do.
- Decorative gradients, 3D effects, and drop shadows on data.
- Designing at desktop scale for something that will be seen on a phone at speed.

## Verification

Test at the size it will actually be seen — small, on a phone, in a feed. If the headline is not
readable at thumbnail scale, it does not exist.

For generated imagery, check the output actually renders any embedded text correctly and matches the
brand palette — generated imagery drifts, and drifted brand color is worse than no brand color.

## Related

- `enterprise/marketing/social-post-craft` — the post the visual accompanies.
- `enterprise/product/brand-identity` — the palette and type the visuals must hold.
- `enterprise/product/design-system` — where the templates live.
