---
name: privacy-and-data-protection
description: "Assesses how personal data is collected and used. Data mapping, lawful basis, consent, processor agreements, subject rights, retention, and breach obligations. Use this before launching anything that handles personal data, when adding a vendor that will process it, when a data subject request arrives, when assessing exposure under GDPR or US state privacy laws, or when preparing for a privacy review."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: legal-risk
metadata:
  hermes:
    category: legal-risk
    tags: [legal-risk, privacy, gdpr, data-mapping, subject-rights]
    related_skills: [chief-legal-and-risk-officer, regulatory-compliance, data-governance, ai-ml-governance]
---

# Privacy and data protection

> Not legal advice. Regimes differ by jurisdiction and change; material questions need qualified
> counsel. This structures the assessment and identifies what to escalate.

## When to Use

- Before launching anything that handles personal data.
- Adding a vendor that will process it.
- A data subject request arrives.
- Assessing exposure under GDPR or US state privacy laws.
- Preparing for a privacy review.

## Procedure

### Start from the data map

You cannot assess what you have not inventoried. For each category of personal data:

- What is collected, from whom, and where it came from.
- Why — the specific purpose, and the lawful basis where one is required.
- Where it lives, who can reach it, and which vendors receive it.
- How long it is kept, and what deletes it. "Indefinitely" is a finding, not an answer.
- Whether it crosses a border, and under what mechanism.

Most privacy failures are inventory failures: data nobody remembered was being collected, in a
system nobody owned.

### Design decisions that prevent problems

- **Collect less.** Every field is a liability with a maintenance cost. The cheapest way to protect
  data is not to hold it.
- **Purpose limitation is real.** Data collected for one purpose is not automatically available for
  another — particularly for training models, which is where this most often goes wrong now.
- **Separate identifiers from behavior** where analysis does not require linkage.
- **Retention with an enforcing mechanism.** A policy with no deletion job is a statement of intent.

### Consent, where it applies

Specific, informed, freely given, and as easy to withdraw as to give. Pre-ticked boxes, bundled
consent, and cookie walls that offer no genuine choice fail on their face in the regimes that
require consent.

Note that consent is one lawful basis among several and often the weakest — it can be withdrawn,
and then the processing must stop.

### Vendors

Any third party processing personal data on your behalf needs a written agreement covering purpose,
security, sub-processors, deletion, and assistance with subject rights. Sending data to a vendor
without one is a common and easily avoided violation.

Assess the vendor's actual security, not their questionnaire answers, in proportion to the
sensitivity of what they will hold.

### Subject rights and breaches

Have a working process before the first request: how it arrives, how identity is verified, how the
data is located across systems, and the deadline. Locating the data is the part that fails.

For breaches, know your notification clock before you need it — several regimes measure it in hours
from awareness. Decide in advance who determines that awareness has occurred.

## Pitfalls

- Assessing without a data map. Most privacy failures are inventory failures.
- "Indefinitely" as a retention answer, or a retention policy with no deletion job behind it.
- Reusing data collected for one purpose to train a model, without a basis that covers it.
- Sending personal data to a vendor with no written processing agreement.
- Relying on a vendor's questionnaire answers rather than their actual security.
- Discovering the breach notification clock after the breach, or leaving it undecided who determines
  that awareness has occurred.

## Verification

Exercise the subject-rights process before the first real request: verify identity, locate the data
across every system in the map, and time it against the statutory deadline. Locating the data is the
part that fails, and a process never walked through is a document.

Report the data map with lawful basis and retention per category, the processing agreements in
place, and the named person who decides that breach awareness has occurred. Escalate material
questions to qualified counsel rather than concluding them.

## Related

- `enterprise/legal-risk/regulatory-compliance` — the wider obligation map this sits inside.
- `enterprise/data-analytics/data-governance` — access and lineage on the same data.
- `enterprise/data-analytics/ai-ml-governance` — the training-data basis question.
