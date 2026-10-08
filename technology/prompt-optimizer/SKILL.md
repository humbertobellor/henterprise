---
name: prompt-optimizer
description: "Turns rough intent into a reliable prompt. Diagnosing why output is inconsistent, restructuring the instruction, and adapting it across models. Use this when a prompt is not producing what was wanted, when output varies run to run, when writing a prompt for a repeated task, when moving a prompt between models, or when someone describes what they want an AI to do and needs it written properly."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: technology
metadata:
  hermes:
    category: technology
    tags: [technology, prompting, evaluation, variance, models]
    related_skills: [ai-workflow-architect, ai-ml-governance, skill-authoring, agent-hierarchy]
---

# Prompt optimizer

Diagnosing why a prompt underperforms, restructuring it, and testing it against the worst case rather
than the average.

## When to Use

- A prompt is not producing what was wanted.
- Output varies run to run.
- Writing a prompt for a repeated task.
- Moving a prompt between models.
- Someone describes what they want an AI to do and needs it written properly.

## Procedure

### Diagnose before rewriting

Bad output has a small number of causes, and the fix differs entirely by cause:

- **Underspecified** — the model is guessing at something you know. Most common by far.
- **Overspecified** — so many constraints that they conflict, and the model satisfies some
  arbitrarily.
- **Wrong shape** — asking for a paragraph when you want a table, or a decision when you want
  options.
- **No success criterion** — nothing in the prompt says what good looks like, so quality varies with
  nothing.
- **Buried instruction** — the actual task is in the middle of context and gets weighted like
  context.
- **Genuinely hard** — the task needs information the model does not have, and no prompt fixes that.
  Say so rather than iterating.

Read the actual bad output before rewriting. The failure mode names the cause.

### What reliably helps

- **Say what to do, not what to avoid.** Negative instructions are weaker than positive ones and
  often summon the thing named.
- **Give the shape of the output** — the sections, the length, the format. If format matters, show
  an example rather than describing it.
- **Provide one worked example** where the task is judgment-heavy. Examples carry more instruction
  per token than description does, and one good one beats three mediocre.
- **State the audience and purpose.** "For a technical reader deciding whether to adopt this" changes
  the output more than most adjectives.
- **Ask for reasoning before the answer** on analytical tasks — order matters, since a conclusion
  stated first is defended rather than derived.
- **Give an out.** Tell it what to do when the input is insufficient, or it will invent something.

### Structure

Put the task first, context second, and any output format last where it will be closest to
generation. Long context between instruction and output is where instructions get lost.

For repeated prompts, separate the fixed instruction from the variable input explicitly, so the
model can tell which is which.

### Producing variations

When a prompt matters enough to optimize, produce genuinely different versions rather than variants
of one phrasing:

- **Terse** — instruction only, minimal framing. Often outperforms, and it is cheapest.
- **Structured** — explicit sections, numbered constraints, defined output shape.
- **Exemplar-led** — one worked example carrying most of the instruction.
- **Role-framed** — audience and stance set before the task.

Test all four on the same inputs. Which wins is genuinely hard to predict, and the intuition that a
longer prompt is better is wrong about as often as it is right.

### Moving between models

Do not assume a prompt transfers. Models differ in how they weight system versus user instruction,
how they handle long context, and how they respond to formatting. Re-test on the target model, and
be especially suspicious of prompts tuned through many small iterations — those are often fitted to
one model's quirks.

## Pitfalls

What does not help: politeness, threats, incentives, insisting on importance, and stacked
superlatives. These consume tokens and change little. So does repeating an instruction in three
phrasings — it usually signals the instruction is unclear rather than reinforcing it.

And in the method: rewriting before reading the bad output, negative instructions that summon the
thing named, burying the task in the middle of context, iterating on a task the model cannot do, and
assuming a tuned prompt transfers to another model.

## Verification

A prompt is not done because one run looked good. Run it three to five times on the same input and
look at the variance — that is the actual quality. Then run it on the awkward inputs: empty, far too
long, ambiguous, adversarial.

Fix the worst case, not the average. The average is what you see in testing; the worst case is what
your users see.

Judge against criteria written before seeing results, or you will rationalize whatever came back.
For most tasks: did it do the task, is it correct, is it the right shape and length, is it usable
without editing. Score each run rather than forming an overall impression — impressions are
dominated by the best run, and the worst run is what matters.

## Related

- `enterprise/technology/ai-workflow-architect` — where the prompt sits in a system.
- `enterprise/technology/skill-authoring` — turning a good prompt into a reusable skill.
- `enterprise/data-analytics/ai-ml-governance` — evaluation once it reaches production.
