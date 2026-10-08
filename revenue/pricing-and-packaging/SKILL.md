---
name: pricing-and-packaging
description: "Sets price, tiers, and the surfaces that carry them. The pricing metric, packaging structure, upgrade paths, paywalls, and offer construction. Use this to set or change pricing, design or restructure tiers, choose a pricing metric, build an offer, design upgrade prompts and paywalls, or evaluate whether a pricing change is safe to make."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: revenue
metadata:
  hermes:
    category: revenue
    tags: [revenue, pricing, packaging, paywalls, willingness-to-pay]
    related_skills: [chief-revenue-officer, unit-economics, revenue-recognition, behavioral-marketing, positioning-and-messaging]
---

# Pricing and packaging

The highest-leverage number in the business and the least examined. Most companies are underpriced
and have never tested it.

## When to Use

- Setting or changing pricing.
- Designing or restructuring tiers.
- Choosing a pricing metric.
- Building an offer.
- Designing upgrade prompts and paywalls.
- Evaluating whether a pricing change is safe to make.

## Procedure

### The pricing metric

Choose what you charge *per* before choosing how much. It should scale with the value the customer
receives, be predictable enough to budget, and be something they cannot easily game.

Get this wrong and no amount of tuning the number fixes it — a metric that scales with your cost
rather than their value creates a permanent argument at every renewal.

### Setting the level

Anchor on value delivered, not cost incurred. Cost sets a floor and nothing else.

Evidence to gather: what the alternative costs them today including labor, what similar categories
charge, and what current customers say about price — with the caveat that nobody says a price is too
low. Willingness-to-pay research is directional, not decisive; people misreport.

If nobody ever objects to your price, it is too low. Some loss on price is correct.

### Packaging

Tiers should map to distinguishable segments with different needs, not to arbitrary feature counts.
Three is usually right; more creates paralysis and support load.

Each tier needs one obvious reason to upgrade, tied to something that grows with the customer's
success. Gating on a feature they will never need does not drive upgrades; gating on a limit they
will hit does.

Name tiers for who they are for, not by metal. "Team" and "Business" tell a buyer where they belong.

### Monetization surfaces

Upgrade prompts and paywalls should appear at the moment of blocked value — when someone is trying
to do the thing the tier does not allow, not on a schedule.

Explain what is behind the gate and why the limit exists. An unexplained wall reads as extraction.
Show the value already received before asking for payment, and make declining easy — dark patterns
buy one conversion and lose the account.

### Changing price

- Grandfather existing customers, or expect churn well beyond the price-sensitive segment.
- Announce with real notice and a clear reason.
- Change one thing at a time — price and packaging together makes the result unreadable.

## Pitfalls

- Choosing the amount before choosing the metric.
- A pricing metric that scales with your cost rather than the customer's value.
- Never losing a deal on price, which means the price is too low.
- Tiers built on arbitrary feature counts, or gating on features nobody wants rather than limits
  people hit.
- Prompting for upgrade on a schedule rather than at the moment of blocked value.
- Dark patterns at the paywall, which buy one conversion and lose the account.
- Changing price and packaging together, which makes the result unreadable.

## Verification

Model the downside first: at what churn rate does this increase lose money? Report that number
alongside the expected gain, and state the grandfathering decision explicitly — its absence produces
churn well beyond the price-sensitive segment.

Treat willingness-to-pay research as directional, never decisive, and say so when reporting it.

## Related

- `enterprise/finance/unit-economics` — the contribution the price has to produce.
- `enterprise/finance/revenue-recognition` — packaging changes what the accounting looks like.
- `enterprise/marketing/behavioral-marketing` — anchoring, tiers, and choice overload.
