---
name: revenue-recognition
description: "Determines when and how revenue is recognized. Performance obligations, contract terms that change the answer, and the deal structures that create accounting problems. Use this to work out how a contract should be recognized, review a non-standard deal before it is signed, understand deferred revenue, or spot terms that would delay or reverse recognition."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: finance
metadata:
  hermes:
    category: finance
    tags: [finance, revenue-recognition, contracts, deferred-revenue, asc-606]
    related_skills: [chief-financial-officer, financial-reporting-and-close, pricing-and-packaging, contract-review]
---

# Revenue recognition

Cash received is not revenue earned. The gap between them is where deals get restructured after
signature and where quarters get restated.

> This structures the question and tells you what to ask. Revenue recognition is a technical
> accounting matter under standards such as ASC 606 and IFRS 15 — conclusions on a material or
> unusual contract need your auditors or a qualified accountant, not a checklist.

## When to Use

- Working out how a contract should be recognized.
- Reviewing a non-standard deal before it is signed.
- Understanding deferred revenue.
- Spotting terms that would delay or reverse recognition.

## Procedure

### The shape of the question

Recognition follows the transfer of control to the customer, worked through in five steps: identify
the contract, identify the distinct performance obligations, determine the transaction price,
allocate it across the obligations, then recognize as each is satisfied.

Most disputes happen at step two and step four. What sales sold as one thing is frequently several
obligations for accounting purposes — software plus implementation plus support — and the price has
to be allocated across them on standalone selling price, not on how the quote was written.

### Terms that change the answer

These belong in a pre-signature review, because after signature the only remedy is an amendment the
customer has no reason to agree to:

- **Acceptance clauses** — a customer right to reject can defer recognition until acceptance.
- **Termination for convenience** — a short-notice exit can shorten the contract term for accounting
  purposes, however long the stated term is.
- **Contingent or milestone fees** — variable consideration, constrained until it is probable there
  will be no significant reversal.
- **Material rights** — a renewal or upgrade priced below standalone value can itself be a
  performance obligation carved out of today's price.
- **Extended payment terms** — payment far from delivery can introduce a financing component.
- **Side letters.** Any promise made outside the contract is still part of the contract. They are the
  single most common cause of restatement, and by construction finance does not know they exist.

### Working with sales

Recognition treatment is a deal input, not a post-signature discovery. A concession that costs
nothing commercially can move revenue across a period boundary, and by the time finance sees the
signed paper the trade has already been made.

Give `enterprise/revenue/chief-revenue-officer` and `enterprise/revenue/pricing-and-packaging` a
small set of standard structures that recognize cleanly, and route anything outside them through
review before signature — alongside `enterprise/legal-risk/contract-review`, which owns the legal
exposure the same clauses create.

### Deferred revenue is an obligation

The deferred balance is work owed, not money banked. Track it by cohort and obligation so you can
answer what it is composed of and when it releases. A balance nobody can decompose is one that
surprises you.

## Pitfalls

- Recognizing on invoice date or cash receipt as a shortcut.
- Allocating price across obligations the way the quote happened to be laid out.
- Letting a side letter exist.
- Concluding a material or novel contract's treatment without your auditors.
- Discovering the recognition treatment after signature, when the trade has already been made.

## Verification

For each contract: the distinct performance obligations identified, the transaction price allocated
on standalone selling price, and the trigger that satisfies each obligation. The deferred balance
decomposes by cohort and obligation with a release schedule. Any of the listed terms present is
named explicitly, with its effect stated. Anything material or novel is routed to the auditors
rather than concluded here.

## Related

- `enterprise/legal-risk/contract-review` — the legal exposure the same clauses create.
- `enterprise/revenue/pricing-and-packaging` — the structures that recognize cleanly.
- `enterprise/finance/financial-reporting-and-close` — where the treatment lands.
