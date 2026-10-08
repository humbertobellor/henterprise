---
name: data-modeling
description: "Designs the warehouse and semantic layer. Source-to-mart structure, dimensional modeling, grain, slowly changing dimensions, and the metric layer analytics reads through. Use this to design or restructure a warehouse, model a new source, decide on grain or table structure, build a semantic or metric layer, or diagnose why queries are slow, wrong, or impossible to write."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: data-analytics
metadata:
  hermes:
    category: data-analytics
    tags: [data-analytics, warehouse, dimensional-modeling, semantic-layer, grain]
    related_skills: [data-engineering, data-governance, business-intelligence, chief-data-officer]
---

# Data modeling

The structure between raw source data and the questions people ask of it — layers, grain,
dimensions, and the semantic layer every consumer reads through.

## When to Use

- Designing or restructuring a warehouse.
- Modeling a new source.
- Deciding on grain or table structure.
- Building a semantic or metric layer.
- Diagnosing why queries are slow, wrong, or impossible to write.

## Procedure

### Layers, and why the middle one matters

Three layers, each with one job:

1. **Raw** — source data, append-only, otherwise unmodified. Do not apply *business* logic on
   ingest: you cannot recover what you discarded, and the logic will need to change retroactively.

   **Privacy and security transformations are the exception, and belong at ingest.** Credentials and
   secrets should never land in the warehouse at all. Personal data that is not needed should be
   dropped rather than stored and governed later, and identifiers you must keep but rarely need in
   the clear should be tokenized or encrypted on arrival. Retention and deletion apply from ingest,
   not from the marts.

   The distinction: strip what you must not hold, keep everything you are entitled to hold, and
   leave interpretation for later.
2. **Staging** — cleaned and conformed: consistent types, standardized names, deduplicated, no
   business logic yet.
3. **Marts** — business-facing models shaped for how questions are asked.

The discipline that pays is keeping business logic out of layers 1 and 2. Logic embedded in ingestion
cannot be changed retroactively, and it will need to change.

### Grain is the decision everything follows from

State the grain of every table in one sentence: *one row per what*. "One row per order line per day"
is a grain. "Order data" is not.

Most modeling errors are grain errors, and they surface as fan-out — a join multiplying rows so every
downstream sum is inflated. If a number is mysteriously too high, check the grain before checking the
logic.

### Dimensional structure

Facts for events and measurements; dimensions for the things being described. Keep facts narrow and
long, dimensions wide and short.

Conform dimensions across facts — one customer dimension, used everywhere. Separate customer tables
per domain is how the same customer gets counted differently in two reports.

**Handle history deliberately.** Overwriting a dimension attribute rewrites the past: last year's
revenue silently re-attributes to this year's segment. Decide per attribute whether history matters,
and where it does, keep versions with valid-from and valid-to.

### The semantic layer

Define metrics once, above the marts, and have every consumer read through it. Without it, the same
metric is reimplemented in each dashboard and they drift — not because anyone is careless, but
because a filter differs.

The semantic layer is where the metric dictionary becomes executable rather than documentary.

### Performance

Model for the query pattern you actually have. Pre-aggregate what is queried constantly; leave the
long tail to compute on demand.

Partition and cluster on what people filter by — usually time, then a tenant or entity key. Most slow
warehouse queries are full scans of a table that could have been partitioned by date.

Denormalize deliberately, and write down why. Undocumented denormalization is indistinguishable from
a modeling error six months later.

## Pitfalls

- Building a mart directly on raw. The coupling means every source change breaks the business layer.
- Mixing grains in one table.
- Letting a dashboard contain business logic the warehouse does not. That logic is invisible and
  unversioned.
- Overwriting a dimension attribute and silently rewriting the past.
- Undocumented denormalization, indistinguishable from a modeling error six months later.

## Verification

Every table states its grain in one sentence — *one row per what* — and a reviewer can check it.
Confirm dimensions are conformed across facts, that attributes where history matters carry
valid-from and valid-to, and that every consumer reads metrics through the semantic layer rather
than reimplementing them. When a number looks too high, check the grain before the logic and report
which it was.

## Related

- `enterprise/data-analytics/data-engineering` — the pipelines that land and move this data.
- `enterprise/data-analytics/data-governance` — the metric dictionary this makes executable.
- `enterprise/data-analytics/business-intelligence` — the consumers reading through the semantic layer.
