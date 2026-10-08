---
name: access-and-identity
description: "Designs and audits who can reach what. Authentication, authorization models, privileged access, service credentials, and joiner-mover-leaver policy. Use this to design a permissions model, run an access review, reduce standing privilege, handle offboarding, set up SSO or MFA, manage service and machine credentials, or diagnose why permissions have sprawled."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: security
metadata:
  hermes:
    category: security
    tags: [security, identity, least-privilege, sso, access-reviews]
    related_skills: [chief-information-security-officer, identity-lifecycle-administration, security-architecture-review, onboarding-and-offboarding]
---

# Access and identity

Access accumulates. People change roles and keep the old permissions, services get broad credentials
because narrow ones were inconvenient, and contractors' accounts outlive their contracts. Left alone,
entitlement always grows and never shrinks.

This owns **policy** — what a role should be entitled to. Execution belongs to
`enterprise/it-operations/identity-lifecycle-administration`.

## When to Use

- Designing a permissions model.
- Running an access review.
- Reducing standing privilege.
- Handling offboarding, or setting up SSO or MFA.
- Managing service and machine credentials.
- Diagnosing why permissions have sprawled.

## Procedure

### Principles that actually hold

- **Least privilege, and it must be practical.** A model so restrictive that people share accounts
  to get work done is worse than a looser one they follow.
- **Role-based, not person-based.** Grants attached to individuals are ungovernable at any scale.
- **Time-bound elevation over standing privilege.** Nobody should hold administrative access
  continuously because they occasionally need it. Elevation on request, with a reason, expiring
  automatically.
- **Separate duties where the consequence is severe.** The person who requests a payment does not
  approve it; the person who writes the deploy does not solely authorize the production change.

### Authentication

Single sign-on wherever possible — the value is not convenience, it is that offboarding becomes one
action rather than forty. Every system outside SSO is a system someone will still have access to
after they leave.

Multi-factor everywhere it is available, and phishing-resistant factors for administrative access.
SMS is better than nothing and is the weakest option worth deploying.

### Joiner, mover, leaver

**Mover is the one everyone gets wrong.** Joining and leaving are events with a process; changing
role usually adds permissions and removes none, which is how a long-tenured employee ends up with
access to everything.

Make role change a revoke-and-regrant rather than an addition. It is the single highest-value change
most organizations can make to their access posture.

Offboarding needs to be same-day, cover everything including systems outside SSO, and be verified
rather than assumed. Keep a list of what exists to be revoked — the fastest way to find the shadow
systems is to try to offboard someone thoroughly.

### Service and machine credentials

Usually more numerous and less governed than human ones. Each needs a named human owner, a scope
limited to its actual use, a rotation path, and an expiry.

Prefer short-lived, automatically issued credentials over long-lived keys. A key that never expires
will eventually appear in a repository, a log, or a support ticket.

## Pitfalls

- A model so restrictive that people share accounts to get work done.
- Grants attached to individuals rather than roles.
- Standing administrative access held because it is occasionally needed.
- Treating a role change as an addition rather than a revoke-and-regrant.
- Long-lived keys, which eventually appear in a repository, a log, or a support ticket.
- Assuming offboarding completed rather than verifying it.

## Verification

Access reviews: periodic, by system, with the reviewer being the person accountable for the data
rather than IT. Reviewers who cannot say why someone needs access should remove it — the burden
belongs on retention, not removal. Review dormant accounts as a separate pass.

Diagnose sprawl against a fixed list, because it is nearly always the same list: permissions granted
to individuals rather than roles, roles nobody can define, standing administrative access, accounts
whose owner has left, service credentials with no owner, and systems outside SSO.

## Related

- `enterprise/it-operations/identity-lifecycle-administration` — executes this policy.
- `enterprise/security/security-architecture-review` — authorization in a specific design.
- `enterprise/people/onboarding-and-offboarding` — the joiner and leaver events.
