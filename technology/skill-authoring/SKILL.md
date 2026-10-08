---
name: skill-authoring
description: "Writes agent skills that trigger and help. So they load at the right moments and give usable instruction when they do. Use this when creating a new skill, editing an existing one, diagnosing a skill that fires too often or never fires, or reviewing a set of skills for overlap. Also use before adding to a skill library, to check the capability is not already covered."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: technology
metadata:
  hermes:
    category: technology
    tags: [technology, skills, authoring, triggering, libraries]
    related_skills: [prompt-optimizer, ai-workflow-architect, agent-hierarchy, completion-verification]
---

# Skill authoring

A skill is judged twice: on whether it loads at the right moment, and on whether it helps once
loaded. Most fail the first test.

## When to Use

- Creating a new skill, or editing an existing one.
- Diagnosing a skill that fires too often or never fires.
- Reviewing a set of skills for overlap.
- Before adding to a skill library, to check the capability is not already covered.

## Procedure

### The description does the triggering

It is the only part read when deciding whether to load. Write it for that job:

- Lead with **what the skill does**, in one clause.
- Then **when to reach for it** — the situations, in the words someone would actually use, including
  the oblique ones ("why isn't this converting" as well as "CRO audit").
- Name the **edge cases that should still trigger it**, and where useful, what should *not*.

Vague descriptions produce two failures at once: the skill misses cases it should catch, and fires
on cases it cannot help.

Note the runtime constraint this sits against: Hermes truncates the description to 60 characters in
the system-prompt skill index, so the leading clause has to carry the identification on its own,
with the trigger language following for the fuller listing.

### The body does the work

Write for someone competent who has not thought about this problem today. That means:

- **Method over exhortation.** "Be thorough" is noise. An ordered procedure is instruction.
- **State the failure behind each rule.** A rule with no failure attached gets optimized away by the
  next reader.
- **Be specific enough to be wrong.** Guidance too hedged to contradict is too vague to follow.
- **Put long material in `references/`** and say when to read it. The body should fit in working
  memory.

### Overlap is the silent killer

Two skills whose descriptions both match a request means neither reliably wins. Before adding one,
check what already covers the ground. Prefer extending an existing skill, or consolidating the
family into one skill with references, over adding a near-neighbor.

### Mechanics

- `name` must be lowercase-hyphenated and equal the directory name, or the skill will not load.
- One skill, one directory, `SKILL.md` at its root; supporting material in `references/` and
  `scripts/`, which are loaded on demand rather than scanned as skills.

## Pitfalls

- A vague description, which both misses cases and fires on ones it cannot help.
- Exhortation in place of method. "Be thorough" is noise.
- A rule with no failure attached — the next reader optimizes it away.
- Guidance too hedged to contradict, which is too vague to follow.
- A body too long to hold in working memory, with nothing pushed to `references/`.
- Adding a near-neighbor skill rather than extending the one that already covers the ground.

## Verification

Write three requests that should trigger it and two that should not, and check the description
actually discriminates. If a near-miss request would pull it in, tighten the description.

Then confirm the mechanics: frontmatter parses, `name` matches the directory, and every referenced
support file exists.

## Related

- `enterprise/technology/prompt-optimizer` — the instruction quality inside the body.
- `enterprise/executive/agent-hierarchy` — organizing a whole roster rather than one skill.
- `enterprise/technology/ai-workflow-architect` — where a skill sits in a working system.
