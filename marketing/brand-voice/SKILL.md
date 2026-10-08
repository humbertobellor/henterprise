---
name: brand-voice
description: "Captures how a brand actually writes. And turns it into reusable voice instructions every other content skill draws from. Use this before drafting any content for a new brand or client, when output keeps coming back sounding generic, when several writers need to sound like one, or when a voice needs defining without existing samples to learn from."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: marketing
metadata:
  hermes:
    category: marketing
    tags: [marketing, brand, voice, writing, style-guide]
    related_skills: [chief-content-officer, marketing-copywriting, newsletter-writer, positioning-and-messaging, brand-identity]
---

# Brand voice

The upstream dependency for every writing skill. Draft before this exists and it comes back sounding
like everyone else.

## When to Use

- Before drafting any content for a new brand or client.
- Output keeps coming back sounding generic.
- Several writers need to sound like one.
- A voice needs defining with no existing samples to learn from.

## Procedure

### With existing samples

Collect ten to twenty real pieces the person considers representative — their best, not their most
recent. Then extract, with evidence:

- **Sentence rhythm** — average length, and whether they vary it deliberately. Most distinctive
  voices are distinguished by rhythm before vocabulary.
- **Vocabulary tells** — the words they reach for and the register they avoid. Note both.
- **Opening moves** — how they start. Most writers have two or three habitual openings.
- **Stance** — do they assert, hedge, question, or provoke? Who do they assume the reader is?
- **Humor and its absence** — where it appears and where it never does.
- **Formatting habits** — paragraph length, list usage, emphasis.

Quote a real example for each. A voice guide with adjectives and no samples is unusable.

### Without samples

Build from a choice rather than a blank page. Offer archetypes — the practitioner showing their
work, the analyst, the contrarian, the teacher, the insider, the enthusiast — with a written
paragraph in each. Let them react. People cannot describe their voice but recognize it instantly.

Then interview around the choice: who are you writing for, what do you want them to feel, what would
you never say.

### The output

Produce two artifacts other skills read:

- **`voice.md`** — the rules, each with a real example and a counter-example.
- **`about-me.md`** — background, expertise, recurring themes, and the stories available to draw on.

Include a **do-not** list. Voice guides fail on what they permit, not what they prescribe.

## Pitfalls

- A voice guide of adjectives with no samples. It is unusable by anyone, human or model.
- Collecting the most recent pieces rather than the ones the person considers their best.
- Asking someone to describe their voice from a blank page. They cannot; they can only recognize it.
- Omitting the do-not list. Voice guides fail on what they permit, not what they prescribe.

## Verification

Draft two paragraphs and read them to the person cold. If they say "close, but I wouldn't say it
that way," ask exactly what they would say — that correction is the most valuable data in the
process, and it goes back into `voice.md` as a rule with its counter-example.

## Related

- `enterprise/marketing/marketing-copywriting` — the first consumer of the voice artifacts.
- `enterprise/marketing/newsletter-writer` — long-form in the same voice.
- `enterprise/product/brand-identity` — the visual counterpart.
