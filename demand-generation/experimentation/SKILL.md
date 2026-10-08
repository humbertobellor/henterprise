---
name: experimentation
description: "Designs, runs, and reads A/B tests. Hypothesis, sample size, duration, guardrails, and honest interpretation. Use this to plan a test, judge whether a result is real, build an experimentation program, decide what to test next, or diagnose why tests keep producing inconclusive or non-replicating results."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: demand-generation
metadata:
  hermes:
    category: demand-generation
    tags: [demand-generation, experimentation, ab-testing, statistics, guardrails]
    related_skills: [landing-page-cro-expert, marketing-analytics, business-intelligence, activation]
---

# Experimentation

Most A/B testing programs produce confident conclusions from insufficient data. The discipline is
almost entirely in what you do before launch.

## When to Use

- Planning a test.
- Judging whether a result is real.
- Building an experimentation program.
- Deciding what to test next.
- Diagnosing why tests keep producing inconclusive or non-replicating results.

## Procedure

### Before running

- **Hypothesis with a mechanism.** "Moving the pricing table above the fold will raise trial starts,
  because visitors currently leave before seeing pricing." Not "let's try a green button."
- **One primary metric**, chosen in advance. Secondary metrics are context, never the verdict.
- **Sample size calculated in advance**, from your baseline rate and the smallest lift that would
  change a decision. If the required sample is unreachable, do not run the test — decide by judgment
  and say so.
- **Duration set in advance**, covering at least one full weekly cycle, and two if the buying cycle
  is long.
- **Guardrail metrics** that would make you reject a win: refunds, support volume, downstream
  retention.

### While running

Do not look at results and act on them mid-flight. Peeking and stopping at significance is the
single most common way to generate false positives, and it is very effective at it.

Check only that the test is running correctly — even split, no broken variant, tracking firing.

### Program level

Test where the traffic and the leverage are. Most sites can only run a handful of adequately powered
tests a year — spend them on structural questions, not button colors.

Keep a log of every test: hypothesis, result, decision. Without it, teams re-run the same tests every
eighteen months and re-learn the same things.

## Pitfalls

- Peeking and stopping at significance. It is the most effective way to manufacture a false positive.
- Extending a test because it is nearly significant. Extending until significance manufactures it.
- Treating a secondary metric as the verdict.
- Running a test whose required sample is unreachable.
- Segmenting afterward for verdicts. Slice enough ways and something is always significant.
- Spending scarce test capacity on button colors.

## Verification

Read at the pre-set duration, not before and not extended. Then:

- **Significance is not size.** A statistically significant 0.3% lift may not be worth shipping.
- **Inconclusive is a real result** and the most common one. It means the change did not matter
  enough to detect, which is useful.
- **Check the guardrails** before declaring a win.
- **Segment afterward for hypotheses only**, never for verdicts.

Log hypothesis, result, and decision for every test, including the inconclusive ones.

## Related

- `enterprise/demand-generation/landing-page-cro-expert` — what is worth testing on a page.
- `enterprise/demand-generation/marketing-analytics` — the tracking the test depends on.
- `enterprise/revenue/activation` — the downstream metric most guardrails watch.
