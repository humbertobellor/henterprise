---
name: implementation-planning
description: "Turns a spec into a plan another session can run. And drives that plan through review checkpoints. Use this before touching code on any multi-step task, when work needs handing to someone else, when a task keeps sprawling mid-implementation, or when a plan exists and needs executing in order with verification between steps."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: technology
metadata:
  hermes:
    category: technology
    tags: [technology, planning, checkpoints, handoff, scope]
    related_skills: [completion-verification, solution-architecture, parallel-agent-delivery, project-delivery]
---

# Implementation planning

Turning intent into an ordered, verifiable plan that survives being handed to someone who was not in
the conversation.

## When to Use

- Before touching code on any multi-step task.
- Work needs handing to someone else.
- A task keeps sprawling mid-implementation.
- A plan exists and needs executing in order with verification between steps.

## Prerequisites

A plan is worth writing at more than about three steps, more than one file of consequence, or any
work that will be handed off. Below that, planning costs more than it saves.

## Procedure

### Writing the plan

A plan is executable when someone who was not in the conversation can follow it without guessing.
That means every step names:

- **The change** — the file or surface, and what it should do afterward.
- **The proof** — the command that shows it worked. "Run the tests" is not a step; the exact
  invocation is.
- **The checkpoint** — whether a human reviews before the next step starts.

Order steps so the system is working at the end of each one. A plan whose midpoint is a broken build
cannot be paused, and every plan gets paused.

State up front what is **out of scope**. Plans fail by accretion far more often than by being wrong.

### Executing

- One step at a time, in order. Finish and verify before starting the next.
- **Stop at checkpoints.** The point of a checkpoint is that continuing without it is a mistake.
- When reality contradicts the plan, stop and amend the plan. Do not improvise past it silently —
  the plan is the shared state, and a stale plan is worse than none.
- Track status *in* the plan as you go, so an interrupted run can resume.

## Pitfalls

- Starting to write code because the plan felt obvious. If it was obvious, writing it costs a minute.
- Marking a step done without running its proof.
- Expanding scope mid-execution. Note it, finish the plan, then decide.
- A step whose proof is "run the tests" rather than the exact invocation.
- A plan whose midpoint leaves the build broken, so it cannot be paused.
- Improvising past a contradicted plan, which makes the shared state stale.

## Verification

Every step carries its proof command, and a step is not done until that command has been run and its
output read. The plan itself is the status record — an interrupted run resumes from it, so it must
reflect reality rather than intent.

Test the plan for handoff by asking whether someone with no context could follow it without
guessing. If they would have to ask a question, that question is a missing line.

## Related

- `enterprise/technology/completion-verification` — the proof at each step and at the end.
- `enterprise/technology/parallel-agent-delivery` — when the plan's steps can run at once.
- `enterprise/pmo/project-delivery` — the same discipline at project scale.
