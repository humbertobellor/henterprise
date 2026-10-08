---
name: security-architecture-review
description: "Reviews a design or change for security. Authentication and authorization, data handling, secrets, dependencies, and the secure-development practices around it. Use this to review an architecture or pull request for security, set secure coding standards, choose or tune SAST and DAST tooling, assess a third-party integration, or decide whether a design is safe to build."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: security
metadata:
  hermes:
    category: security
    tags: [security, code-review, authorization, secrets, supply-chain]
    related_skills: [threat-modeling, chief-information-security-officer, access-and-identity, vulnerability-management, code-review]
---

# Security architecture review

Reviewing a design or a change for the things that actually cause incidents, in the order that finds
them fastest.

## When to Use

- Reviewing an architecture or a pull request for security.
- Setting secure coding standards.
- Choosing or tuning SAST and DAST tooling.
- Assessing a third-party integration.
- Deciding whether a design is safe to build.

## Procedure

Attention spent in this order finds the most consequential problems first.

**1. Authentication.** How identity is established, how sessions are represented, how they expire,
what happens on password reset and account recovery. Recovery flows are the most commonly weakest
path into an account and the least reviewed.

**2. Authorization.** The one that matters most and gets least attention. For every endpoint and
every object: who is allowed, and where is that checked? The characteristic failure is checking on
the way in but not on the object itself, so any authenticated user can reach any record by changing
an identifier.

Check multi-tenant isolation explicitly and by test, not by reading. Assume every identifier in a
request is attacker-controlled, because it is.

**3. Data.** What is collected, where it goes, where it rests, and who can read it. Sensitive data
in logs, in error responses, in analytics payloads, and in client bundles — all four are routine
findings.

**4. Input and output.** Untrusted input reaching a query, a template, a command, a deserializer, or
a URL the server fetches. Parameterize rather than escape. Validate against an allowlist rather than
a denylist.

**5. Secrets.** Never in source, never in client bundles, never in build logs. Rotatable, scoped to
what needs them, and with a documented rotation path that someone has actually walked.

**6. Dependencies and supply chain.** What is pulled in, how it is pinned, how updates are reviewed,
and what would happen if a maintainer account were compromised. Lockfiles committed, builds
reproducible.

### Reviewing a change rather than a design

Look for: new endpoints without an authorization check, new external input, changed authentication
or session logic, new dependencies, anything touching cryptography, and anything that widens what a
role can do. Everything else is usually lower yield.

### Third-party integrations

What data leaves, under what agreement, with what access, and what happens if they are breached.
Scope credentials to the minimum, prefer short-lived tokens, and know how to revoke without an
outage.

## Pitfalls

- Writing your own cryptography. Use the vetted primitives, and be suspicious of any diff that
  implements a comparison, a token, or a signature by hand.
- Checking authorization on the way in but not on the object itself.
- Verifying multi-tenant isolation by reading rather than by test.
- Treating automation as a review. It finds known patterns, not design flaws — and design flaws are
  what cause the expensive incidents.
- Untuned SAST, which produces false positives at volume until the team learns to ignore all of it.
- Escaping where parameterizing was available; denylists where allowlists were.

## Verification

Report findings by severity, each with: the concrete attack, what the attacker gains, whether it
blocks release, and the specific fix. A finding with no attack path stated is a preference.

Tooling is the floor beneath that, not a substitute: SAST tuned rather than merely enabled, DAST and
dependency scanning both running because they find different things, and secret scanning in CI and
pre-commit — the highest-value automation per unit of effort.

## Related

- `enterprise/security/threat-modeling` — done earlier, at design time, and cheaper.
- `enterprise/technology/code-review` — the general review this specializes.
- `enterprise/security/vulnerability-management` — where the findings are tracked to closure.
