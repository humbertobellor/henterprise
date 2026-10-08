---
name: agent-hierarchy
description: "Designs orchestrator-and-subagent hierarchies. Splits agents by exclusive write surface, pairs every producer with an independent auditor, and enforces the split with a script that runs in CI. Use this whenever the user wants to set up, expand, audit, or fix a multi-agent or subagent structure for a codebase; asks how to divide work between agents; wants agent charters, roles, or a surface map written; or is hitting agents that collide on the same files, review their own work, or drift from their remit. Also use when sizing a roster or deciding whether a new agent is justified."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: executive
metadata:
  hermes:
    category: executive
    tags: [executive, agents, orchestration, org-design, ci]
    related_skills: [chief-executive, org-design, parallel-agent-delivery]
---

# Agent hierarchy

A method for standing up an orchestrator → specialist-subagent hierarchy, extracted from a
working implementation of ~24 agents over a 1,500-file monorepo, machine-checked on every PR.

## When to Use

- Setting up, expanding, auditing, or fixing a multi-agent or subagent structure for a codebase.
- Deciding how to divide work between agents.
- Writing agent charters, roles, or a surface map.
- Agents are colliding on the same files, reviewing their own work, or drifting from their remit.
- Sizing a roster, or deciding whether a new agent is justified.

## Prerequisites

- A repository you can enumerate with `git ls-files`.
- Node available, to run `scripts/agent-guard.mjs` from this skill package.
- A CI configuration you can add a check to. The guard is only worth writing if it runs.

## The whole method in one paragraph

Split agents by **write surface, not by topic**. Two classes only: **builders**, which edit
inside exactly one exclusive surface and never commit, and **reviewers**, which are permanently
read-only and can always run in parallel. The orchestrator — the main chat — is the sole
committer. Write the surface map **before** any charters, keep it in one Markdown file, and
enforce it with a script that runs in CI. Each row also carries an **authority** — `autonomous`,
`proposes`, or `escalates` — which answers the separate question of whether that agent's work may
land without a decision; most rows are `autonomous`, and gating everything makes the gate
meaningless. Producer and auditor are never the same agent. For
each class of fact, exactly one file owns it and everyone else derives.

## Why topic splits fail

"One agent on SEO, one on UI" is the intuitive split and it breaks immediately: both end up
editing `tokens.css`. Neither is wrong, and neither can be held responsible. A surface split
has no such overlap by construction — which is exactly what makes it checkable.

## Procedure

Do not start writing charters early; the order is the method.

1. **Inventory the real tree** — run `git ls-files | sed 's|/[^/]*$||' | sort -u` through the
   terminal tool. Report what is actually there before proposing anything.
2. **Propose the roster** — the smallest set where no two agents share a file. Each needs an
   id, a class, a one-line remit, and its exact globs. An agent whose surface cannot be stated
   in globs is not an agent; fold it in.
3. **Write the surface map** — one Markdown file, one row per agent.
4. **Wire the guard** — `scripts/agent-guard.mjs check` proves the map is coherent (no path
   claimed twice, no path unowned); `agent-guard.mjs diff <agent>` proves a given diff obeyed
   it. Both are needed: once the orchestrator commits, the authorship that `diff` checks is
   gone, so it has to run while the work is still attributable.
5. **Write charters last**, in the format in the playbook: why the agent exists, what it must
   never do, the verification its surface implies, and a six-section return contract.

## Rules that carry a failure behind them

- **Producer and auditor are never the same agent.** An agent that reviews its own output
  reliably approves it.
- **The orchestrator is not one of the two classes.** It is the sole committer, and giving it
  a surface makes it a builder that can also merge.
- **One file owns each class of fact.** Everything else derives from it, or the two copies
  diverge and nobody notices which is stale.
- **Never remove a shared-core export because it looks unused.** You cannot see the consumers
  from inside the core. Deprecate, announce, then remove.

## The decision log

Keep a live decision log — the format is in `references/playbook.md`. When a decision is raised,
assign it the next number immediately, before it is answered, and give it lettered options with an
explicit recommendation. Never renumber, never reuse a number, and record resolutions in place
rather than deleting them.

The source repository this method came from keeps its own instance at `docs/DECISION-LOG.md`; use
that as the worked example of the format.

## Pitfalls

- Splitting agents by topic. Two topic agents inevitably edit the same file, and neither can be
  held responsible.
- Writing charters before the surface map. The order is the method.
- Giving the orchestrator a surface, which makes it a builder that can also merge.
- Gating every row with `proposes` or `escalates`, which makes the gate meaningless.
- Letting the same agent produce and audit. It will approve itself.
- Running `agent-guard.mjs diff` after the orchestrator has committed, when the authorship it
  checks is already gone.

## Verification

Both guard modes must pass, run through the terminal tool from the repository root:

```
node scripts/agent-guard.mjs check
```

`check` proves the map is coherent: no path claimed by two agents, no path unowned. `diff <agent>`
proves a given change obeyed the map, and must run while the work is still attributable — before
the orchestrator commits. Wire both into CI; a guard that does not run in CI is documentation.

Report the roster with each agent's class, remit, and globs; the surface map file; the guard output
for both modes; and any path deliberately left unowned, named as such.

## References

- `references/playbook.md` — the full 415-line playbook: surface splitting, the guard, the
  registry, the decision log, anti-patterns with their failure modes, sizing, multi-repo and
  shared-core layouts, the charter format, and a day-one checklist.
- `references/starter-rosters.md` — concrete rosters for a mobile-app portfolio, a game
  portfolio, and a shared core, with producer/auditor pairings.
- `references/bootstrap-prompt.md` — the prompt that stands the hierarchy up from scratch.
- `scripts/agent-guard.mjs` — the guard itself.

## Related

- `enterprise/executive/chief-executive` — the orchestrator role this method assumes.
- `enterprise/people/org-design` — the same split applied to human teams.
- `enterprise/technology/parallel-agent-delivery` — running the resulting roster in parallel.
