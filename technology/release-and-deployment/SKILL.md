---
name: release-and-deployment
description: "Ships changes safely and often. Pipelines, deployment strategies, feature flags, rollback, and database changes. Use this to design a deployment pipeline, reduce release risk, roll out a risky change gradually, plan a schema migration, or work out why releases are infrequent and frightening."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: technology
metadata:
  hermes:
    category: technology
    tags: [technology, deployment, feature-flags, rollback, migrations]
    related_skills: [cloud-infrastructure, observability-and-reliability, test-driven-development, branch-and-worktree-workflow]
---

# Release and deployment

Release risk is dominated by batch size. Large infrequent releases are dangerous because many changes
land at once and nobody can tell which one broke it — so teams release less often, which makes each
release larger. The loop is the problem.

## When to Use

- Designing a deployment pipeline.
- Reducing release risk.
- Rolling out a risky change gradually.
- Planning a schema migration.
- Working out why releases are infrequent and frightening.

## Procedure

### Separate deploy from release

Deploying code and exposing behavior to users are different acts, and coupling them forces every
deployment to be a business decision.

Decouple with flags: deploy continuously, expose deliberately. This makes rollback a configuration
change rather than a redeployment, which is the difference between seconds and minutes at the worst
possible time.

Flags are inventory and rot. Give each an owner and a removal date; a codebase full of stale flags
has combinatorial states nobody has tested.

### The pipeline is the quality gate

Automate everything between commit and production, and let the pipeline reject. Manual steps get
skipped under pressure, which is exactly when they matter.

Order gates fast-to-slow so failure is cheap: lint and unit tests, then integration, then anything
requiring a deployed environment. A pipeline slow enough to be circumvented is worse than a fast one
with fewer checks, because it will be circumvented.

Build once and promote the same artifact through environments. Rebuilding per environment means the
thing you tested is not the thing you shipped.

### Roll out gradually

Expose to a small population first and watch real signals before widening. Canary or percentage
rollout turns a total failure into a contained one.

Define the abort condition **before** starting, with a threshold and a named decision-maker. Under
pressure, and with the change fresh, the instinct is always to wait a little longer and see.

### Database changes are the asymmetric risk

Code rolls back; data does not. Make schema changes backward-compatible and multi-step: add the new
structure, write to both, migrate, switch reads, then remove the old — with the application tolerant
of both shapes throughout.

## Pitfalls

- Coupling deploying code to exposing behavior.
- Promoting a different artifact than the one that was tested.
- Beginning a rollout without a defined abort condition.
- Shipping a schema change that requires the application and database to deploy simultaneously.
- Feature flags with no owner and no removal date, producing combinatorial states nobody has tested.
- A pipeline slow enough to be circumvented, which will be.

## Verification

Test the migration against production-scale data. A migration that is instant on a development
dataset can lock a large table for a length of time nobody modeled.

Before a rollout, confirm the abort condition has a threshold and a named decision-maker, and that
rollback has been exercised rather than assumed. During it, watch real user-facing signals from
`enterprise/technology/observability-and-reliability`, not deployment status.

## Related

- `enterprise/technology/observability-and-reliability` — the signals a rollout is watched on.
- `enterprise/technology/test-driven-development` — the gates in the pipeline.
- `enterprise/it-operations/systems-administration` — change control for the corporate estate.
