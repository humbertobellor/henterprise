---
name: tax
description: "Structures the tax questions a growing business faces. Corporate income, sales and use, payroll, nexus, and the obligations created by hiring or selling somewhere new. Use this to work out what a new state or country obligates you to, prepare for a tax filing or audit, understand sales tax on your product, or check what a remote hire or new market triggers."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: finance
metadata:
  hermes:
    category: finance
    tags: [finance, tax, nexus, sales-tax, compliance]
    related_skills: [chief-financial-officer, financial-reporting-and-close, capital-allocation, regulatory-compliance]
---

# Tax

Tax obligations are created by facts — where you sell, where people work, what you sell — not by
decisions anyone consciously makes. The characteristic failure is discovering an obligation years
after it began, with penalties and interest attached.

> This structures the question and tells you what to ask. Tax is technical, jurisdiction-specific,
> and changes frequently. Positions on anything material belong with a qualified tax adviser or CPA,
> not a checklist.

## When to Use

- Working out what a new state or country obligates you to.
- Preparing for a tax filing or audit.
- Understanding sales tax on your product.
- Checking what a remote hire or a new market triggers.

## Procedure

### Nexus: the thing that creates obligations quietly

Nexus is the connection that gives a jurisdiction the right to tax you. It is established by
activities most companies do not think of as tax events:

- **An employee working somewhere.** One remote hire in a new state commonly creates payroll
  registration, income tax withholding, and often corporate income tax nexus.
- **Economic activity without physical presence.** Since *Wayfair*, US states set sales-tax nexus on
  revenue or transaction thresholds — a few hundred thousand dollars, or a couple of hundred
  transactions, with the numbers differing by state.
- **Inventory held somewhere**, including in a third-party fulfillment warehouse you never visit.
- **Contractors, or attending trade shows**, in some jurisdictions.

Review nexus whenever you hire in a new location, cross a revenue threshold, or change how you
distribute. Registering late costs more than registering early, and voluntary disclosure programs
exist precisely because this is so common.

### Sales tax is about what you sell, not what you charge

Taxability of software and services varies enormously by state: SaaS is taxable in some, exempt in
others, and treated differently again if delivered with implementation services. The classification
of your own product is a determination worth getting in writing and revisiting when packaging
changes — see `enterprise/revenue/pricing-and-packaging`, because bundling can change the answer.

Exemption certificates for tax-exempt customers must be collected and kept current. In an audit,
missing certificates mean you owe the tax you did not collect.

### The calendar is most of the discipline

Tax failures are usually administrative, not technical: a missed registration, a late filing, an
estimated payment nobody scheduled. Maintain a calendar of every obligation by jurisdiction with an
owner, and treat it as part of `enterprise/finance/financial-reporting-and-close`.

### Where it meets the rest of finance

- `enterprise/finance/financial-reporting-and-close` — tax provision and the deferred position
- `enterprise/finance/capital-allocation` — after-tax returns are the only ones that matter for a
  decision
- `enterprise/people/workforce-planning` — every hire in a new jurisdiction is a tax question before
  it is a cost question
- `enterprise/finance/revenue-recognition` — book and tax treatment diverge, and the difference is
  itself something to track

## Pitfalls

- Assuming no obligation because there is no office in a jurisdiction.
- Treating your product's taxability as settled across states without a determination.
- Selling into exempt customers without current exemption certificates.
- Taking a position on a material matter without a qualified adviser.
- Letting the obligation calendar sit outside the close, where nobody owns it.

## Verification

The deliverable is a calendar: every obligation, by jurisdiction, with a named owner and a due date,
reviewed whenever you hire somewhere new, cross a threshold, or change distribution. Confirm
exemption certificates are current, that the product's taxability determination exists in writing
per jurisdiction, and that anything material has been put to a qualified adviser rather than
concluded here.

## Related

- `enterprise/finance/financial-reporting-and-close` — where the calendar lives.
- `enterprise/people/workforce-planning` — hiring somewhere new is a tax question first.
- `enterprise/legal-risk/regulatory-compliance` — the wider obligation-tracking discipline.
