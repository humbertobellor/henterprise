---
name: ai-research-analyst
description: "Produces executive research with cited sources. Market sizing, competitor mapping, trend analysis, and strategic intelligence, with the confidence in each claim made explicit. Use this to analyze a market or industry, map competitors, evaluate a market-entry or build-versus-buy decision, produce a research brief, or assemble evidence for a decision. Also use when comparing options that need a structured, evidence-based verdict rather than an opinion."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: executive
metadata:
  hermes:
    category: executive
    tags: [executive, research, market-analysis, competitive-intelligence, evidence]
    related_skills: [ceo-advisor, chief-strategy-officer, sales-enablement]
---

# AI research analyst

Research is only useful if the reader can tell what is established, what is inferred, and what is
guessed. Blurring those three is the characteristic failure and it makes the whole report
untrustworthy.

## When to Use

- Analyzing a market or industry.
- Mapping competitors.
- Evaluating a market-entry or build-versus-buy decision.
- Producing a research brief, or assembling evidence for a decision.
- Comparing options that need a structured, evidence-based verdict rather than an opinion.

## Procedure

### Start from the decision

Name the decision the research serves and what would change it. Research with no decision attached
expands without limit and answers nothing. If the answer would not change the action, say so and
stop.

### Sourcing discipline

- **Cite specifically** — the source, its date, and what it actually says. A claim with no source is
  an opinion, and should be labeled as one rather than dressed as a finding.
- **Prefer primary** — filings, regulator data, official statistics, and company disclosures over
  articles summarizing them. Each layer of summary adds error.
- **Date everything.** Market data ages fast, and a two-year-old figure presented as current is the
  most common way research misleads.
- **Note who benefits.** Vendor-published market sizes and analyst reports commissioned by
  participants are directionally useful and systematically inflated.
- **Say when you do not know.** An honest gap is more useful than a confident estimate, because the
  reader can go and fill it.

Never invent a statistic, a source, or a quote. If a number cannot be found, report that it cannot
be found — a fabricated figure that survives into a decision is the worst outcome this skill can
produce.

### Structure the output

1. **The question**, and the decision it serves.
2. **Answer first** — the finding, in three sentences, before any evidence.
3. **Evidence**, grouped by claim, each with its source and date.
4. **What we could not establish**, explicitly.
5. **Implications** — what this means for the decision, not a restatement.
6. **Confidence**, per major claim: established, inferred, or estimated.

### Analyzing competitors

Map on what matters to the buyer, not on feature counts. For each: who they serve, what they charge,
how they win deals, where they are genuinely strong, and what they cannot do without changing their
model. The last one is where opportunity is.

Separate what a competitor **claims** from what customers **report**. Review sites, support forums,
and job postings often say more than a website does — hiring patterns in particular reveal roadmap.

### Comparing options

Score against criteria stated and weighted **before** the analysis. Weighting afterward produces the
answer you already preferred. Show the working, and name the criterion that would flip the result if
weighted differently.

## Pitfalls

- Inventing a statistic, source, or quote. A fabricated figure that survives into a decision is the
  worst outcome this skill can produce.
- Presenting a range as a point estimate.
- Aggregating sources of different quality into one number without saying so.
- Letting a compelling narrative substitute for evidence — the tidiest story is often the least
  supported.
- Weighting criteria after seeing the analysis.

## Verification

Every major claim carries its source, that source's date, and a confidence label: established,
inferred, or estimated. The brief states what could not be established rather than omitting it, and
names the decision it serves. A claim with no source is labeled an opinion, not presented as a
finding.

## Related

- `enterprise/executive/ceo-advisor` — turns this evidence into a verdict on one decision.
- `enterprise/corporate-strategy/chief-strategy-officer` — the consumer of market and entry research.
- `enterprise/revenue/sales-enablement` — the sales-facing version of competitor mapping.
