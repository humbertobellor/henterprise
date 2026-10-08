---
name: api-design
description: "Designs interfaces that survive their consumers. Resource modeling, errors, versioning, pagination, and compatibility. Use this to design a new API, review one before it ships, decide how to version or deprecate, fix an interface consumers keep misusing, or work out whether a change is breaking."
version: 1.0.0
author: Chris Brock (cbrock84), migrated for Hermes Agent by Humberto Bello
license: MIT
platforms: [linux, macos, windows]
category: technology
metadata:
  hermes:
    category: technology
    tags: [technology, api, versioning, compatibility, pagination]
    related_skills: [solution-architecture, code-review, security-architecture-review, completion-verification]
---

# API design

An API is a promise you cannot withdraw once someone depends on it. Design accordingly: the cost of
getting it wrong is paid continuously by everyone who integrates.

## When to Use

- Designing a new API, or reviewing one before it ships.
- Deciding how to version or deprecate.
- Fixing an interface consumers keep misusing.
- Working out whether a change is breaking.

## Procedure

### Model the domain, not the database

Expose concepts the consumer thinks in. An interface that mirrors internal table structure leaks
implementation, breaks whenever storage changes, and forces consumers to reconstruct meaning you
already had.

Name things as the domain names them. Consistency in naming, casing, date formats and identifier
style matters more than any individual choice being optimal — an interface that is uniformly
imperfect is learnable, and one that is inconsistently excellent is not.

### Errors are part of the contract

Most integrations spend most of their code on failure. Give it the same care as the success path:

- **Distinguish machine-readable code from human-readable message.** Consumers branch on the code;
  the message is for the developer reading logs.
- **Say what to do about it.** Retryable or not, and after how long.
- **Never leak internals** — stack traces and SQL in error bodies are a security finding as well as
  bad design.
- **Be consistent about which failures are which status.** Validation, authorization, and conflict
  are different situations and should never share a shape.

### Compatibility

Adding an optional field is safe. Removing a field, renaming one, tightening validation, changing a
default, or adding a required parameter are all breaking, and the last three break consumers who are
doing nothing wrong.

Version when you must break, and be explicit about how long the previous version lives. A
deprecation without a date is a deprecation nobody acts on.

Prefer expansion over versioning where possible: a new optional field costs a consumer nothing, a new
version costs them a migration.

### Pagination, filtering and limits

Any collection that can grow needs pagination from the first release — retrofitting it is a breaking
change to every consumer. Prefer cursors over offsets for anything that changes while being read;
offset pagination silently skips and duplicates records under concurrent writes.

State rate limits in the contract and communicate them in responses. An undocumented limit is
discovered in the consumer's production incident.

## Pitfalls

- Exposing internal identifiers or storage structure through the interface.
- Returning errors whose meaning must be inferred from the message text.
- Tightening validation on an existing endpoint and calling it non-breaking.
- Shipping a collection endpoint without pagination.
- Offset pagination on a collection that changes while being read.
- A deprecation with no date, which nobody acts on.

## Verification

Test every change against the breaking-change list before calling it additive: removed field, renamed
field, tightened validation, changed default, new required parameter. The last three break consumers
who are doing nothing wrong, and they are the ones most often shipped as minor.

Confirm the error contract by exercising the failure paths, not the success path: each failure class
returns its own status and machine-readable code, says whether it is retryable, and leaks nothing.

## Related

- `enterprise/technology/solution-architecture` — the boundaries the API expresses.
- `enterprise/security/security-architecture-review` — authorization on every endpoint and object.
- `enterprise/technology/code-review` — where a breaking change gets caught before release.
