---
name: treasury-and-liquidity
description: "Manages cash and liquidity. Cash forecasting, runway, working capital, banking structure, and currency and counterparty exposure. Use this to build a cash forecast, extend runway, improve working capital, decide where cash should sit, or assess exposure to a bank, currency, or customer concentration."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: finance
metadata:
  hermes:
    category: finance
    tags: [finance, treasury, cash-forecast, runway, working-capital]
    related_skills: [chief-financial-officer, budgeting-and-forecasting, unit-economics, supply-chain-and-logistics]
---

# Treasury and liquidity

Profitable companies fail on cash. Earnings are an opinion arrived at through accruals; cash is a
balance you either have on the day or do not.

## When to Use

- Building a cash forecast.
- Extending runway.
- Improving working capital.
- Deciding where cash should sit.
- Assessing exposure to a bank, a currency, or customer concentration.

## Procedure

### Forecast cash directly

The indirect method — net income adjusted for non-cash items — is right for reporting and nearly
useless for operating. Build a direct forecast of receipts and disbursements by week, from actual
expected timing.

Thirteen weeks is the working horizon: long enough to act, short enough to be accurate. Roll it
weekly and **compare last week's forecast against what happened**. A forecast never checked against
outturn does not improve, and its errors are the most useful information it produces.

Model timing, not just amount. A receipt that arrives four days late is the same money and a
different liquidity position.

### Runway is a decision variable

Runway is cash divided by net burn, but the useful version is scenario-based: the plan, a downside
where revenue underperforms, and the case where a large receivable slips.

Know your decision points in advance — the date by which a raise must start, the date a cost
reduction must be committed to take effect in time. Decision dates always precede the cash-out date,
often by more than people assume, and discovering that late removes the good options.

### Working capital is free financing, or a leak

Cash is trapped in the cycle between paying for inputs and being paid for output:

- **Receivables** — invoice promptly and accurately; disputed invoices age indefinitely, and most
  disputes trace to an invoice that did not match the contract. Watch the aging trend, not the
  average.
- **Payables** — take terms offered, pay on time rather than early, and do not fund suppliers who did
  not ask to be funded.
- **Inventory** — every unit is cash on a shelf. See
  `enterprise/operations/supply-chain-and-logistics`.

A week off the cycle is permanent working capital released, and it costs nothing in interest.

### Where cash sits

Concentration in one bank is a single point of failure, as depositors have periodically rediscovered.
Spread operating balances against counterparty limits, and hold reserves in instruments whose
maturity matches when the money is needed.

Do not reach for yield with money you have a date for. The return on operating cash is not worth the
liquidity risk, and treasury losses of this kind are always described afterwards as conservative
investments.

## Pitfalls

- Running the business on an indirect cash forecast.
- Reporting runway as a single number without a downside case.
- Letting the decision date for financing pass while watching the cash-out date.
- Concentrating operating cash in one counterparty because the relationship is convenient.
- Reaching for yield with money that has a date on it.
- Watching average receivable age rather than the aging trend.

## Verification

Roll the thirteen-week direct forecast weekly and compare last week's forecast against what actually
happened — the errors are the most useful output. Report runway as a set of scenarios with the
decision dates named, not as one number. State counterparty concentration against limits, and the
maturity of anything cash is held in against when the money is needed.

## Related

- `enterprise/finance/chief-financial-officer` — owns cash and runway.
- `enterprise/finance/budgeting-and-forecasting` — the plan the downside case departs from.
- `enterprise/operations/supply-chain-and-logistics` — inventory as cash on a shelf.
