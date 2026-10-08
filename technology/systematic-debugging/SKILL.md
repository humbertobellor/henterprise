---
name: systematic-debugging
description: "Finds the root cause before proposing a fix. For a bug, test failure, or unexpected behavior. Use this whenever something is broken and the cause is not yet proven - a failing test, a production error, intermittent behavior, or a symptom that appeared after a change. Also use when a fix has been attempted and did not work, or when the same bug keeps coming back."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: technology
metadata:
  hermes:
    category: technology
    tags: [technology, debugging, root-cause, reproduction, hypothesis]
    related_skills: [test-driven-development, observability-and-reliability, completion-verification, quality-management]
---

# Systematic debugging

**No fix before the cause is proven.** A change that makes a symptom disappear without an
explanation has not fixed anything — it has moved the failure somewhere you are not looking.

## When to Use

- Something is broken and the cause is not yet proven — a failing test, a production error,
  intermittent behavior, or a symptom that appeared after a change.
- A fix has been attempted and did not work.
- The same bug keeps coming back.

## Procedure

1. **Reproduce it deterministically.** If you cannot make it happen on demand, you cannot know when
   it is fixed. Intermittent means you have not found the variable yet — order, timing, state,
   environment, data.
2. **Narrow the blast radius.** Bisect: which commit, which input, which branch, which layer. Halve
   the search space with each step rather than reading everything.
3. **State a hypothesis that can be wrong.** "The cache returns stale rows after a write" is a
   hypothesis. "Something is wrong with caching" is not.
4. **Test the hypothesis directly** — a log line, a breakpoint, a probe. Prove it, do not infer it.
5. **Explain the whole symptom.** If your cause explains the error but not why it started Tuesday,
   you have found *a* bug, not *the* bug.
6. **Fix, then verify by reverting.** Put the bug back and confirm the test fails again. This is the
   step people skip, and it is the one that proves causation rather than coincidence.

## Pitfalls

- **Shotgun changes** — altering several things at once. Now you cannot attribute the fix.
- **"Probably a flake."** Not a diagnosis. A test that fails intermittently is reporting a real
  race, ordering dependency, or shared-state leak.
- **Fixing the symptom** — catching the exception, adding a retry, widening a timeout — without
  knowing what threw it.
- **Trusting the error message's location.** Where it surfaced is rarely where it originated.
- A cause that explains the error but not the timing. That is a bug, not the bug.

## Verification

State the reproduction, the proven cause, the fix, and the verification that the fix addresses that
cause specifically. Name anything you ruled out and how.

The reverting step is the proof: put the bug back, confirm the failure returns, and re-apply. Without
it you have a correlation.

## Related

- `enterprise/technology/test-driven-development` — the failing test that pins the bug.
- `enterprise/technology/observability-and-reliability` — the instrumentation that makes step 1 possible.
- `enterprise/operations/quality-management` — the same causal discipline outside software.
