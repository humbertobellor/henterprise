# Henterprise — a virtual agentic organization for Hermes Agent

Sixteen departments, 143 skills, and a soul for each department. A chief executive over the
functions a company actually has: strategy, finance, product, technology, security, legal and risk,
people, operations, and the revenue and demand engine.

Migrated from [`cbrock84/headcount`](https://github.com/cbrock84/headcount) — an agent organization
built for Claude Code — and brought to the [Hermes Agent](https://hermes-agent.nousresearch.com)
skill specification. MIT licensed, © 2026 Chris Brock. See [OUTPUT.md](OUTPUT.md) for exactly what
the migration changed.

## Structure

```
enterprise/
├── <department>/
│   ├── SOUL.md          persona for running this department as a Hermes profile
│   ├── README.md        what it covers, and how to install it
│   └── <skill>/SKILL.md
└── scripts/validate-hermes-skills.py
```

Hermes discovers skills by walking for `SKILL.md`, so the extra nesting level is fine: a skill
resolves as `enterprise/<department>/<skill>`.

## Departments

| Department | Skills | Chief |
|---|---:|---|
| [executive](executive/) | 6 | Chief Executive |
| [corporate-strategy](corporate-strategy/) | 5 | Chief Strategy Officer |
| [finance](finance/) | 10 | Chief Financial Officer |
| [revenue](revenue/) | 8 | Chief Revenue Officer |
| [marketing](marketing/) | 18 | Chief Marketing Officer |
| [demand-generation](demand-generation/) | 11 | Head of Demand Generation |
| [product](product/) | 9 | Chief Product Officer |
| [technology](technology/) | 18 | Chief Technology Officer |
| [it-operations](it-operations/) | 8 | Chief Information Officer |
| [security](security/) | 6 | Chief Information Security Officer |
| [legal-risk](legal-risk/) | 6 | Chief Legal & Risk Officer |
| [data-analytics](data-analytics/) | 6 | Chief Data Officer |
| [people](people/) | 10 | Chief Human Resources Officer |
| [operations](operations/) | 10 | Chief Operating Officer |
| [pmo](pmo/) | 7 | Head of the Enterprise PMO |
| [customer-experience](customer-experience/) | 5 | Chief Customer Officer |

**Two departments are reviewer-class.** `security` and `legal-risk` review what the others build,
and their blocking findings are not overrulable by the department under review. Disagreement
escalates to `enterprise/executive/chief-executive`, where accepted risk is recorded with a name
against it. This is why the CISO reports independently of the CTO.

## Installing

### One agent for the whole organization

Point a single Hermes profile at this tree. All sixteen departments resolve from it, and skills load
themselves when a request matches.

```yaml
skills:
  external_dirs:
    - <path-to>/hermes/skills
```

The executive persona is the natural soul for this configuration — every other chief escalates there:

```bash
cp executive/SOUL.md ~/.hermes/SOUL.md
```

When one executive session needs genuinely separate departmental workers, use Hermes' native
`delegate_task` path rather than simulating several departments in the main conversation. Give each
child an actual departmental remit and the relevant Henterprise skill. The executive session remains
the shared coordination surface for that task.

For a cross-department dependency, load `enterprise/pmo/dependency-and-risk-management` in the
executive session and keep the task-scoped commitment ledger described by
`enterprise/technology/parallel-agent-delivery`. The providing department must explicitly accept,
revise, or reject the commitment; the accepted or revised result is then returned to every affected
consumer before its work continues.

For independent review, `enterprise/executive/agent-hierarchy` defines the producer/reviewer split:
spawn a fresh reviewer child, have it inspect the underlying artifact rather than the producer's
summary, and return blocking findings for correction and fresh independent re-review.

This is a task-scoped delegated mode. It does not turn a delegated child into one of the persistent
profiles below and does not claim persistent cross-profile transport. Use separate profiles when a
department needs long-lived isolated Hermes state.

### One profile per department

Each department folder is a staged Hermes profile. Its `README.md` carries the exact commands; the
shape is:

```bash
hermes profile create security
```

```bash
cp security/SOUL.md ~/.hermes/profiles/security/SOUL.md
```

Running the reviewer-class departments as their own profiles is the point of the split: a separate
agent, with its own soul, reviewing what the building profiles produced.

**`SOUL.md` is loaded from `HERMES_HOME` only** — never from a skills directory. The files here are
personas staged for installation, not files Hermes picks up in place.

## Validating

```bash
python3 scripts/validate-hermes-skills.py
```

Checks every skill against the Hermes frontmatter contract, confirms `name` matches its directory,
resolves every `related_skills` entry and every `enterprise/<dept>/<skill>` cross-reference, and
enforces the layout. Pass department names to check a subset.

```bash
python3 scripts/validate-hermes-skills.py --index
```

Prints the skill index Hermes would build, with each description truncated at 60 characters exactly
as the system prompt renders it — so the truncation can be inspected rather than assumed.
