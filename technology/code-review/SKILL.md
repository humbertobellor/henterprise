---
name: code-review
description: "Conducts and responds to code review. Reviewing a change for correctness, design, and risk, and evaluating review feedback received on your own work. Use this before merging, when asked to review a diff or pull request, when review feedback has arrived and needs acting on, or when feedback seems wrong and needs a reasoned response rather than compliance."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: technology
metadata:
  hermes:
    category: technology
    tags: [technology, code-review, correctness, feedback, blast-radius]
    related_skills: [branch-and-worktree-workflow, security-architecture-review, test-driven-development, completion-verification]
---

# Code review

Two directions, one skill: reviewing, and being reviewed.

## When to Use

- Before merging.
- Asked to review a diff or pull request.
- Review feedback has arrived and needs acting on.
- Feedback seems wrong and needs a reasoned response rather than compliance.

## Procedure

### Reviewing

Read the diff against what the change is *for*, not against your preferences. Order matters — spend
attention where damage is expensive:

1. **Correctness** — does it do what it claims, including at the boundaries and on the error path?
2. **Blast radius** — what else consumes this? Signature and schema changes are the ones that break
   things far away.
3. **Security and data** — untrusted input, authorization, anything logged or persisted.
4. **Tests** — do they pin the new behavior, or do they pass regardless?
5. **Design** — will this shape hold under the next change?
6. **Style** — last, and only where a linter cannot.

Say which category each comment is, and whether it blocks. A review that mixes a data-loss bug with
a naming preference in one undifferentiated list wastes the author's judgment.

### Receiving

Feedback is a report of a reader's experience, and that part is always valid — if the reviewer
misread it, the code is misleading. The proposed remedy is a separate thing and may be wrong.

- **Verify before implementing.** A suggestion that would break behavior gets a reply, not a commit.
- **Disagreeing is fine; ignoring is not.** Answer every comment: changed, or why not.
- **Do not batch-accept.** Applying every suggestion without judgment is how good code becomes
  incoherent.
- Where a reviewer is factually wrong, show the evidence — the test, the spec, the failing case —
  rather than asserting.

## Pitfalls

- Approving your own work, or a change you authored under another name.
- Leaving a blocking comment without saying what would unblock it.
- Rewriting the author's approach in a review comment. Propose it, and let them decide.
- Mixing a data-loss bug and a naming preference in one undifferentiated list.
- Batch-accepting suggestions, which is how good code becomes incoherent.
- Leading with style, which spends the review's attention where damage is cheapest.

## Verification

Every comment carries its category and whether it blocks. Every comment received is answered:
changed, or why not — an unanswered comment is an unresolved review whatever the approval says.

Where a reviewer's reading was wrong, that is still a finding: the code misled a competent reader.
Fix the code or the comment, not the reviewer.

## Related

- `enterprise/security/security-architecture-review` — the security-specific pass.
- `enterprise/technology/test-driven-development` — whether the tests pin the behavior.
- `enterprise/technology/completion-verification` — proving the change actually works.
