---
name: programmatic-seo
description: "Builds search-targeted pages from a dataset. The location, comparison, integration, and use-case pages that capture long-tail demand at scale. Use this when there is a repeating query pattern with real volume, when a dataset could answer many similar searches, or to judge whether a programmatic approach is viable before building it."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: demand-generation
metadata:
  hermes:
    category: demand-generation
    tags: [demand-generation, seo, programmatic, templates, long-tail]
    related_skills: [seo-strategy, ai-search-optimization, listing-distribution, data-modeling]
---

# Programmatic SEO

Done well, one template covers thousands of real searches. Done badly, it is a mass of thin pages
that damages the whole domain.

## When to Use

- There is a repeating query pattern with real volume.
- A dataset could answer many similar searches.
- Judging whether a programmatic approach is viable before building it.

## Prerequisites

All four must hold, or the answer is fewer, better pages:

1. **A real query pattern** with verified volume across many instances — not one popular term and a
   long tail of zeroes.
2. **Data you actually have**, at quality, for most instances. Missing data produces empty pages,
   and empty pages are the failure mode.
3. **Genuine per-page value.** If two pages differ only by a swapped noun, they are duplicates
   however they are generated.
4. **A reason to be better** than what ranks now. Usually completeness, freshness, or data nobody
   else has.

## Procedure

- **Design the best single page first**, by hand, and confirm it is genuinely useful. Then find what
  in it is variable. Templating before you know the good page scales a mediocre one.
- **Vary the substance, not just the strings.** Each page needs data, comparisons, or context
  specific to it.
- **Set a minimum data threshold.** Below it, the page does not get generated. This single rule
  prevents most programmatic disasters.
- **Internal linking is not optional** — thousands of orphaned pages will not be crawled. Build hub
  pages and cross-links into the template.
- **Roll out in batches.** Publish a few hundred, wait for indexation and performance, then
  continue. A full launch that goes wrong is hard to unwind.

## Pitfalls

- Generating pages for instances with no data.
- Spinning text to create the appearance of uniqueness.
- Launching without a plan for removing what does not work.
- Templating before the hand-built page is proven useful.
- Orphaned pages with no internal links, which will not be crawled.
- Treating page volume as the goal.

## Verification

Roll out in batches and check indexation and performance on each before continuing — a full launch
that goes wrong is hard to unwind.

Stale programmatic pages rot faster than editorial ones because there are so many. Set a refresh
cadence tied to the data source, and prune: pages with no impressions after two quarters should be
consolidated or removed.

## Related

- `enterprise/demand-generation/seo-strategy` — indexation and architecture this depends on.
- `enterprise/demand-generation/ai-search-optimization` — retrievability of the generated pages.
- `enterprise/data-analytics/data-modeling` — the dataset behind the template.
