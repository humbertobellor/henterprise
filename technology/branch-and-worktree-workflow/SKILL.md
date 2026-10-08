---
name: branch-and-worktree-workflow
description: "Isolates feature work and integrates it cleanly. Branches and worktrees for parallel efforts, and the merge, rebase, or split when the work is done. Use this when starting work that should not disturb the current workspace, when several efforts must proceed in parallel on one repository, or when implementation is finished and the change needs merging, rebasing, or splitting for review."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: technology
metadata:
  hermes:
    category: technology
    tags: [technology, git, branching, worktrees, integration]
    related_skills: [code-review, release-and-deployment, parallel-agent-delivery, completion-verification]
---

# Branch and worktree workflow

Isolating work so parallel efforts do not disturb each other, and integrating it in a shape a
reviewer can actually review.

## When to Use

- Starting work that should not disturb the current workspace.
- Several efforts must proceed in parallel on one repository.
- Implementation is finished and the change needs merging, rebasing, or splitting for review.

## Procedure

### Starting

Work that will take more than one sitting, or that runs alongside other work, gets its own isolated
workspace. A worktree gives you a second checkout of the same repository on a different branch — two
efforts, two directories, one object store, no stashing.

Branch from the current upstream default, not from whatever is checked out. Branching off a stale
local branch is how unrelated commits end up in a review.

### While working

- Commit at points where the tree is coherent, not at the end of the day.
- Keep the branch current with its base often. A merge conflict found on day one is a five-minute
  fix; the same conflict found on day ten is an afternoon.
- One concern per branch. If you find an unrelated bug, note it and leave it.

### Finishing

Then decide how it integrates:

- **Small and coherent** — merge as is.
- **Several separable concerns** — split into stacked branches so each can be reviewed on its
  merits. A reviewer given three concerns in one diff reviews none of them well.
- **Exploratory** — keep the useful commits, drop the rest.

## Pitfalls

- Rewriting history on a branch someone else has checked out. Merge instead; a force-push breaks
  their working copy.
- Leaving a worktree behind after merging — stale worktrees hold references and confuse later work.
- Merging your own change with the checks green on an earlier commit rather than the final one.
- Branching off a stale local branch, which drags unrelated commits into the review.
- Several concerns in one diff, which a reviewer reviews none of well.

## Verification

Before proposing the work:

1. Rerun the full check the project actually gates on, not the subset you have been running.
2. Read your own diff top to bottom. Remove debug output, stray files, and commented-out code.
3. Confirm the branch merges cleanly into its base.

The checks must be green on the final commit, not an earlier one.

## Related

- `enterprise/technology/code-review` — what the reviewer does with the result.
- `enterprise/technology/parallel-agent-delivery` — many isolated workspaces at once.
- `enterprise/technology/release-and-deployment` — what happens after the merge.
