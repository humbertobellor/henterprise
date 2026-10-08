---
name: internal-controls-and-audit
description: "Designs and tests controls over financial reporting. Segregation of duties, approval limits, evidence, and preparing for audit. Use this to design controls for a process, prepare for an external audit, respond to an audit finding, set approval thresholds, or assess where a small team's segregation of duties is genuinely broken."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: finance
metadata:
  hermes:
    category: finance
    tags: [finance, controls, audit, segregation-of-duties, approvals]
    related_skills: [chief-financial-officer, financial-reporting-and-close, corporate-governance, enterprise-risk]
---

# Internal controls and audit

Controls exist because a single person who can initiate, approve and record a transaction can also
conceal one. Everything else is elaboration on that.

> This structures control design and audit readiness. Statutory audit requirements, and regimes such
> as SOX where they apply, are matters for your auditors and qualified advisers.

## When to Use

- Designing controls for a process.
- Preparing for an external audit.
- Responding to an audit finding.
- Setting approval thresholds.
- Assessing where a small team's segregation of duties is genuinely broken.

## Procedure

### Segregation of duties

Four capabilities should not sit with one person: **initiating** a transaction, **approving** it,
**recording** it, and **holding the asset**. Any two combined is a risk; three is an unmonitored
opportunity.

Small teams cannot always separate these. That is a normal constraint and pretending otherwise
produces a fictional control matrix. Where separation is impossible, compensate visibly:

- Review by someone outside the process, on a defined cadence rather than when convenient.
- Exception reporting that goes to someone who is not the preparer.
- Bank confirmations and reconciliations reviewed independently of whoever performs them.

Document the gap and the compensating control. An acknowledged, mitigated gap is a defensible
position; an unacknowledged one is a finding waiting to be written.

### Design controls that leave evidence

A control that happened but left no trace did not happen, as far as an auditor can determine. Each
control needs a stated owner, frequency, what is examined, and an artifact produced as a by-product
of doing the work — not assembled afterwards for the audit.

Prefer **preventive** controls, which stop the transaction, over **detective** ones, which find it
afterwards. Prefer automated over manual: system-enforced approval limits do not have busy weeks.

### Approval thresholds

Set limits by value and by risk, not value alone. A low-value payment to a new supplier deserves more
scrutiny than a large one to an established counterparty on contracted terms.

Watch for splitting — transactions repeatedly landing just under a threshold is the pattern the
threshold creates, and it is straightforward to monitor for.

### Audit findings

Treat a finding as information. Fix the cause rather than the instance, and be skeptical of
remediation that consists of more careful behavior: the same conditions will reproduce the finding
with different people.

Related but distinct: `enterprise/legal-risk/corporate-governance` owns board and entity governance,
`enterprise/legal-risk/enterprise-risk` owns the risk framework. This skill owns controls over
financial reporting.

## Pitfalls

- Signing a control matrix that describes separation the team does not actually have.
- Accepting a control with no evidence produced in the ordinary course of performing it.
- Remediating a finding with a commitment to be more careful.
- Setting approval limits on value alone and not monitoring for splitting.
- Preferring detective controls where a preventive one was available.

## Verification

Each control names its owner, its frequency, what is examined, and the artifact it produces as a
by-product — not assembled afterwards. Every unseparated duty is documented alongside its
compensating control. Test by walking a real transaction end to end and producing the evidence the
control was supposed to leave; if it cannot be produced, the control did not operate.

## Related

- `enterprise/finance/financial-reporting-and-close` — the process these controls sit over.
- `enterprise/legal-risk/corporate-governance` — board and entity governance.
- `enterprise/legal-risk/enterprise-risk` — the risk framework.
