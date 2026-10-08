---
name: customer-research
description: "Plans, runs, and synthesizes customer research. Interviews, surveys, win-loss analysis, and message testing, turned into findings that change decisions. Use this when the customer is being guessed at, before positioning or a major launch, when churn or conversion has an unexplained cause, or when a team is arguing from anecdotes. Also use to turn raw interview notes into usable findings."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: marketing
metadata:
  hermes:
    category: marketing
    tags: [marketing, research, interviews, win-loss, synthesis]
    related_skills: [chief-marketing-officer, positioning-and-messaging, voice-of-customer, ux-product-auditor]
---

# Customer research

Research earns its cost only if a decision hangs on it. Name that decision before recruiting anyone.

## When to Use

- The customer is being guessed at.
- Before positioning, or before a major launch.
- Churn or conversion has an unexplained cause.
- A team is arguing from anecdotes.
- Turning raw interview notes into usable findings.

## Procedure

### Choose the method by question

- **Why did this happen / what do they actually do** — interviews. Small n, deep.
- **How common is this** — survey. Only after interviews have told you what to ask; a survey written
  from assumptions returns your assumptions.
- **Why did we win or lose** — win-loss, with losses weighted higher. Losses are where the truth is
  and are systematically under-sampled.
- **Which framing works** — message testing against a real choice, not a preference rating.

### Interviewing

Ask about the past, not the future. "What did you do last time" is evidence; "would you use this"
is politeness.

- Open broad, follow the energy, and go quiet after their first answer — the second one is where the
  substance is.
- Chase specifics: when, what happened next, what did that cost you, who else was involved.
- Never describe your solution before you have their problem in their words. Once they know what you
  want to hear, the interview is over.
- Watch for the workaround. Anything someone has built a spreadsheet to survive is a validated
  problem.

### Synthesizing

Code the transcripts before forming a view — findings assembled to support an existing belief will
be. For each finding record: the claim, how many independently said it, a verbatim quote, and what
would change if it is true. A finding that changes nothing is trivia.

Separate what people **said**, what they **did**, and what you **inferred**. Conflating the three is
the most common way research misleads.

## Pitfalls

- Recruiting only happy customers. The sample that answers your email is not your market.
- Leading: "How much would this feature help?" has one answer.
- Presenting a single interview as a finding.
- Writing a survey from assumptions, which returns your assumptions.
- Describing your solution before you have their problem in their words.
- Under-sampling losses, which is where the truth is.

## Verification

Every finding carries: the claim, how many people independently said it, a verbatim quote, and what
decision changes if it is true. Findings are labeled as said, did, or inferred — conflating those
three is the most common way research misleads. Name the decision the research served before
recruiting, and report whether it moved.

## Related

- `enterprise/marketing/positioning-and-messaging` — the most common consumer of these findings.
- `enterprise/customer-experience/voice-of-customer` — the continuous, unprompted counterpart.
- `enterprise/product/ux-product-auditor` — the product-side evidence on the same questions.
