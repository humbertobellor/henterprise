---
name: parallel-agent-delivery
description: "Splits work across agents running at once. Keeping their surfaces disjoint so results merge cleanly. Use this when facing several independent tasks with no shared state, when a plan has parallelizable steps, when a broad search or audit would be faster fanned out, or when deciding whether work can safely be split at all."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: technology
metadata:
  hermes:
    category: technology
    tags: [technology, agents, parallelism, dispatch, integration]
    related_skills: [agent-hierarchy, implementation-planning, branch-and-worktree-workflow, ai-workflow-architect]
---

# Parallel agent delivery

Parallelism is a property of the work, not a preference. Establish it before dispatching.

## When to Use

- Several independent tasks with no shared state.
- A plan has parallelizable steps.
- A broad search or audit would be faster fanned out.
- Deciding whether work can safely be split at all.

## Prerequisites

All three must hold, or run sequentially:

1. **Disjoint write surfaces** — no two agents touch the same file. Not "unlikely to conflict";
   provably disjoint.
2. **No sequential dependency** — none needs another's output to start.
3. **Independently verifiable** — each result can be judged on its own.

Two agents editing one file produces a merge conflict at best and a silent lost update at worst.

## Procedure

### Dispatching

Each agent gets a self-contained brief: the goal, its exclusive surface, the context it cannot see
for itself, and the shape of the answer expected. Agents share no memory — anything you leave out is
gone.

Ask for a **structured return**, the same shape from each, so results can be compared rather than
re-read.

### Read-only fan-out is the easy case

Searching, auditing, and reviewing have no write surface at all, so they parallelize without risk.
Reach for parallelism here first and freely.

### Integrating

- Review each result against its brief before merging any of them.
- Where two disagree on a shared fact, neither is authoritative — resolve it yourself.
- One agent returning nothing useful is a normal outcome, not a failure to retry blindly.

## Pitfalls

- Splitting work to look faster when the steps are actually sequential.
- Letting two agents write to one surface because "they probably won't collide."
- Merging a result you have not read.
- A brief that assumes shared context. Agents share no memory; anything left out is gone.
- Unstructured returns, which have to be re-read rather than compared.
- Retrying an empty result blindly rather than treating it as an outcome.

## Verification

Prove the three preconditions before dispatch, in writing — especially disjointness, which is the one
people assert rather than check. Then review each returned result against its own brief before any of
them are merged; a batch merged together hides which agent's result was wrong.

## Related

- `enterprise/executive/agent-hierarchy` — the standing roster and its surface map.
- `enterprise/technology/implementation-planning` — where parallelizable steps are identified.
- `enterprise/technology/branch-and-worktree-workflow` — the isolated workspace per agent.
