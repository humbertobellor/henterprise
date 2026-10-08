---
name: financial-reporting-and-close
description: "Runs the period-end close and produces reporting. Close calendar, reconciliations, accruals, variance analysis, and reporting that gets read. Use this to shorten or stabilise a monthly close, design a close checklist, investigate a variance, structure management reporting, or work out why the numbers keep changing after close."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: finance
metadata:
  hermes:
    category: finance
    tags: [finance, close, reconciliation, accruals, reporting]
    related_skills: [chief-financial-officer, internal-controls-and-audit, budgeting-and-forecasting]
---

# Financial reporting and close

A close is a manufacturing process whose output is a number people will make decisions on. Treat it
as a process — sequence, dependencies, quality control — and it gets faster and more accurate
together, which sounds contradictory only if you think speed comes from cutting checks.

## When to Use

- Shortening or stabilising a monthly close.
- Designing a close checklist.
- Investigating a variance.
- Structuring management reporting.
- Working out why the numbers keep changing after close.

## Procedure

### Design the close as a critical path

Map every task with its owner, its dependencies and its duration. Most closes are slow because
independent work is running in series out of habit, not because any step is long.

Move work out of the close window wherever it does not depend on period-end: reconcile subledgers
continuously, book recurring accruals from a schedule, prepare consolidation structure in advance.
Anything you can do on day minus three is a day you are not doing on day two.

Set a **hard cutoff** and hold it. A close that stays open for late entries never finishes and
teaches everyone that deadlines are advisory.

### Reconciliations are the control

Every balance sheet account gets an owner and a reconciliation. The reconciliation is not the
schedule — it is the explanation of the difference and what will clear it.

Watch aged reconciling items specifically. An unexplained item that has survived three closes is not
a timing difference; it is an error that has been carried forward by people assuming someone else
understood it.

### Accruals and the honesty of estimates

Accrue on the best available evidence and document the basis. The basis matters more than the number,
because next period someone has to decide whether it still holds.

Track how estimates resolve against actuals. Consistent bias in one direction is information about
the estimator or the process, and it is invisible unless someone looks.

### Reporting that gets read

Explain variance against a stated expectation — budget, prior period, or forecast — and say which.
A variance without a baseline is a number.

Lead with the two or three things that changed and why, then supporting detail. A report that
requires the reader to find the story does not get read, and its absence of readership is discovered
during a crisis.

Separate **timing** from **run-rate**. A miss caused by something slipping a week is a different
business fact from a miss caused by demand falling, and conflating them produces the wrong reaction.

## Pitfalls

- Leaving the ledger open for late entries after the stated cutoff.
- Carrying an unexplained reconciling item forward a second time.
- Presenting a variance without saying what it is a variance from.
- Reporting a number you cannot trace to a reconciliation.
- Running independent close tasks in series out of habit.
- Conflating a timing miss with a run-rate miss.

## Verification

Every balance sheet account has a named owner and a reconciliation that explains the difference and
what will clear it. Every reported number traces to one. The close held its stated cutoff. Estimates
are tracked against how they resolved, so directional bias is visible. Report the critical path with
durations, so the next close can be shortened deliberately rather than by pressure.

## Related

- `enterprise/finance/internal-controls-and-audit` — the controls the close depends on.
- `enterprise/finance/budgeting-and-forecasting` — the baseline variance is measured against.
- `enterprise/finance/tax` — the provision and filing calendar belong in this cycle.
