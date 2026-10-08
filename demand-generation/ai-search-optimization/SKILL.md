---
name: ai-search-optimization
description: "Optimizes for AI assistants and generated answers. Being retrievable, being cited, and being represented accurately when a model answers on your behalf. Use this when traffic is shifting from links to AI answers, when a brand is misrepresented or absent in AI responses, when planning content for retrieval rather than ranking, or when deciding how AI search changes an existing SEO program."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: demand-generation
metadata:
  hermes:
    category: demand-generation
    tags: [demand-generation, ai-search, retrieval, citation, seo]
    related_skills: [seo-strategy, programmatic-seo, content-strategy, marketing-analytics]
---

# AI search optimization

Classical SEO optimizes to be *clicked*. This optimizes to be *quoted* — often with no click at all.
That changes what a good page looks like.

## When to Use

- Traffic is shifting from links to AI answers.
- A brand is misrepresented or absent in AI responses.
- Planning content for retrieval rather than ranking.
- Deciding how AI search changes an existing SEO program.

## Procedure

### What gets cited

- **Self-contained passages.** A retrieved chunk arrives without the surrounding page. Each section
  must make sense alone, with its subject named rather than pronominalized.
- **Direct answers near the question.** Bury the answer under three paragraphs of context and the
  passage retrieved will be the context.
- **Specific, checkable facts** — numbers, dates, named methods, stated conditions. Vague claims are
  neither retrievable nor quotable.
- **Attributable expertise.** Named authors, stated credentials, dated content, and cited sources.
  Anonymous undated content is weakly weighted.
- **Structure that survives extraction** — real headings, real lists, real tables. Layout implied by
  styling disappears.

### Practical moves

- Answer the question in the first sentence under each heading, then elaborate.
- Write headings as the questions people actually ask.
- Define your own terms on your own pages, so the model's definition traces to you.
- Keep facts consistent across your site. Contradictions get resolved against you.
- Maintain the boring canonical pages — pricing, comparisons, specifications, FAQ. These are heavily
  retrieved and usually neglected.

### Being represented accurately

Assistants assemble an answer about you from whatever is available, weighted toward third-party and
structured sources. Where those are thin or stale, the answer will be wrong.

## Pitfalls

- Pronominalized sections that lose their subject once retrieved out of context.
- Burying the answer under context, so the context is what gets quoted.
- Layout implied by styling rather than by real headings, lists, and tables.
- Anonymous, undated content.
- Contradictory facts across the site — they get resolved against you.
- Judging the program on organic sessions, which will say you are losing while you are winning.

## Verification

Audit periodically: ask several assistants what your company does, who it is for, what it costs, and
how it compares. Note the errors and trace them to a source. The fix is almost always publishing or
correcting the source, not the assistant.

Measure citation and mention frequency, and downstream branded search and direct traffic. Click-
through will fall on informational queries even as influence rises — report both, with the shift
named.

## Related

- `enterprise/demand-generation/seo-strategy` — the ranking program this sits alongside.
- `enterprise/marketing/content-strategy` — territory and the canonical pages.
- `enterprise/demand-generation/marketing-analytics` — measuring a channel whose clicks fall.
