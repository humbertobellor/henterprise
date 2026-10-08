---
name: supply-chain-and-logistics
description: "Manages the flow of goods and inputs. Sourcing, inventory, lead times, fulfillment, and supply risk. Use this to reduce stockouts or excess inventory, plan for a supplier failure, decide reorder points and safety stock, improve fulfillment reliability, or assess concentration risk in a supply base."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: operations
metadata:
  hermes:
    category: operations
    tags: [operations, supply-chain, inventory, lead-time, fulfillment]
    related_skills: [vendor-management, business-continuity-and-resilience, capacity-and-demand-planning, treasury-and-liquidity]
---

# Supply chain and logistics

Supply chains fail at variability, not at averages. A chain planned on average demand and average
lead time will disappoint at both ends: stockouts when either runs long, dead stock when they do not.

## When to Use

- Reducing stockouts or excess inventory.
- Planning for a supplier failure.
- Deciding reorder points and safety stock.
- Improving fulfillment reliability.
- Assessing concentration risk in a supply base.

## Procedure

### Inventory is a bet on uncertainty

Safety stock exists to absorb variation in demand and in lead time. Sizing it needs both the average
and the spread — a supplier averaging 20 days at ±2 is a different proposition from one averaging 20
days at ±15, and treating them the same guarantees you are wrong about one.

Set reorder points on lead-time demand plus safety stock, and revisit them when either input moves.
A reorder point set once is a reorder point that is now wrong.

Hold inventory where it is most flexible. Stock held as components serves several finished
configurations; the same value held as finished goods serves one and obsoletes faster.

### Lead time is a distribution

Quoted lead time is a marketing number. Plan against your own measured receipt dates, including the
bad months. Track the variance explicitly — reliability of lead time usually matters more than its
length, because a long predictable lead time can be planned around and a short erratic one cannot.

### Concentration is the risk that actually bites

Map dependencies past the first tier. Two suppliers on paper who share a single sub-supplier, a
single port, or a single region are one supplier with extra paperwork.

For each critical input know: who else could supply it, how long qualifying them takes, and whether
anything in the design makes switching hard. That answer is worth having before you need it —
qualifying an alternate under pressure is where quality problems enter.

Supplier commercial terms and exit rights belong with `enterprise/operations/vendor-management`;
continuity of the wider business process belongs with
`enterprise/operations/business-continuity-and-resilience`.

## Pitfalls

- Sizing safety stock from average demand without accounting for variability.
- Treating a quoted lead time as a planning input when you have measured data.
- Counting two suppliers as redundancy without tracing where their chains converge.
- Reporting on-time and in-full separately to make the number look better.
- Setting a reorder point once and never revisiting it.
- Holding value as finished goods where components would serve several configurations.

## Verification

Measure on-time-in-full, not on-time and in-full separately — partial shipments that arrive on
schedule are a way of appearing to hit a target while failing the customer.

Diagnose misses by cause: supply, capacity, information, or process. The remedies do not overlap,
and a fulfillment problem attributed to the wrong one gets more expensive rather than better. Report
lead time as a distribution with its variance, not as a single number.

## Related

- `enterprise/operations/vendor-management` — supplier terms and exit rights.
- `enterprise/operations/business-continuity-and-resilience` — supplier failure as a continuity event.
- `enterprise/finance/treasury-and-liquidity` — inventory as cash on a shelf.
