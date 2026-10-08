---
name: enterprise-risk
description: "Identifies, assesses, and tracks organizational risk. Building and maintaining a risk register, scoring exposure, assigning owners and treatments, and preparing for audit. Use this to stand up a risk program, assess the risk in a decision or initiative, prepare for a certification or audit, decide whether a risk should be accepted, mitigated, transferred, or avoided, or report risk posture to leadership."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: legal-risk
metadata:
  hermes:
    category: legal-risk
    tags: [legal-risk, risk-register, treatment, audit-readiness, residual-risk]
    related_skills: [chief-legal-and-risk-officer, regulatory-compliance, internal-controls-and-audit, threat-modeling]
---

# Enterprise risk

The discipline of writing risk down with an owner, scoring it honestly, and deciding what to do
about it.

## When to Use

- Standing up a risk program.
- Assessing the risk in a decision or initiative.
- Preparing for a certification or audit.
- Deciding whether a risk should be accepted, mitigated, transferred, or avoided.
- Reporting risk posture to leadership.

## Procedure

### The register is the artifact

A risk that is not written down with an owner is not managed. Each entry carries:

- **The risk stated as a cause and consequence** — "if X happens, then Y." "Cybersecurity" is a
  category, not a risk. "If an employee's credentials are phished, an attacker reaches customer
  records" is a risk you can do something about.
- **Likelihood and impact**, on a stated scale, with the reasoning. The reasoning matters more than
  the score.
- **Current controls** and an honest view of whether they work.
- **Residual risk** after those controls — the number that actually matters and the one most often
  omitted.
- **A named owner.** A person, not a department.
- **Treatment and a date.**

### Treatment is a decision with four options

**Mitigate** (reduce it), **transfer** (insure or contract it away), **avoid** (do not do the
thing), or **accept**. Accepting is legitimate and often correct — but acceptance must be explicit,
at the right level of authority, and recorded. Risk accepted by silence is risk nobody owns.

Anything above the threshold that only the chief executive can accept goes to them. Never let an
unacceptable risk be quietly downgraded to fit an existing authority.

### Scoring honestly

Two failure modes, both common:

- **Everything is high.** The register stops discriminating and gets ignored.
- **Scores drift downward** as items age without the underlying exposure changing.

Re-assess on a schedule and require evidence for any reduction. A control's existence is not
evidence it works; a test of the control is.

### Reporting

Leadership needs the few risks whose residual exposure is above appetite, what is being done, and
what needs a decision. Not the whole register. A risk report that requires reading forty rows to
find the three that matter will not be read.

## Pitfalls

- Recording a category ("cybersecurity") rather than a cause-and-consequence risk.
- Omitting residual risk, which is the number that actually matters.
- Assigning a department rather than a person as owner.
- Accepting risk by silence, or downgrading an unacceptable risk to fit an existing authority.
- Reducing a score without evidence that the control works.
- Reporting the whole register instead of the few above appetite.

## Verification

Audit readiness is continuous, not a project. What auditors need: documented policies, evidence they
are followed, records of exceptions and approvals, and a clear line from the framework's requirement
to your control to the evidence.

Collect evidence as work happens. Assembling a year of it retrospectively is expensive, and gaps
found then cannot be fixed retroactively. For any score reduction, produce the test of the control,
not its existence.

## Related

- `enterprise/legal-risk/chief-legal-and-risk-officer` — owns the register.
- `enterprise/finance/internal-controls-and-audit` — the control design pattern behind the evidence.
- `enterprise/security/threat-modeling` — where technical risks are identified in the first place.
