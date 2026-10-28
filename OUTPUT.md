# Migration report — `headcount` → Hermes Agent enterprise organization

Migration of [`cbrock84/headcount`](https://github.com/cbrock84/headcount) — an agent organization
built for Claude Code — into a virtual agentic organization for
[Hermes Agent](https://hermes-agent.nousresearch.com), at
`hermes/skills/enterprise/`.

**Result:** 16 departments, 143 skills, 16 souls, 16 department READMEs, 4 support files carried
verbatim, and a validator. `python3 scripts/validate_hermes_skills.py` reports **0 errors**.

Source is MIT licensed, © 2026 Chris Brock; every migrated skill preserves that attribution in its
frontmatter.

---

## 1. Final structure

```
hermes/skills/enterprise/
├── README.md                          org overview and installation
├── OUTPUT.md                          this report
├── scripts/validate_hermes_skills.py  spec validator + index preview
└── <department>/                      × 16
    ├── SOUL.md                        department persona (Hermes profile slot #1)
    ├── README.md                      coverage, skill table, install commands
    └── <skill>/SKILL.md               × 143 total
        ├── references/                (executive/agent-hierarchy only)
        └── scripts/                   (executive/agent-hierarchy only)
```

### Departments and counts

| Source plugin | Target directory | Skills | Soul persona |
|---|---|---:|---|
| `plugins/executive` | `executive/` | 6 | Chief Executive — escalation endpoint |
| `plugins/corporate-strategy` | `corporate-strategy/` | 5 | Chief Strategy Officer |
| `plugins/finance` | `finance/` | 10 | Chief Financial Officer |
| `plugins/revenue` | `revenue/` | 8 | Chief Revenue Officer |
| `plugins/marketing` | `marketing/` | 18 | Chief Marketing Officer |
| `plugins/demand-generation` | `demand-generation/` | 11 | Head of Demand Generation |
| `plugins/product` | `product/` | 9 | Chief Product Officer |
| `plugins/technology` | `technology/` | 18 | Chief Technology Officer |
| `plugins/it-operations` | `it-operations/` | 8 | Chief Information Officer |
| `plugins/security` | `security/` | 6 | CISO — **reviewer-class** |
| `plugins/legal-risk` | `legal-risk/` | 6 | Chief Legal & Risk Officer — **reviewer-class** |
| `plugins/data-analytics` | `data-analytics/` | 6 | Chief Data Officer |
| `plugins/people` | `people/` | 10 | Chief Human Resources Officer |
| `plugins/operations` | `operations/` | 10 | Chief Operating Officer |
| `plugins/pmo` | `pmo/` | 7 | Head of the Enterprise PMO |
| `plugins/customer-experience` | `customer-experience/` | 5 | Chief Customer Officer |
| | **16** | **143** | |

Every skill directory name is unchanged from the source, and all 143 are unique across departments —
so a skill resolves unambiguously as `enterprise/<department>/<skill>`.

---

## 2. Spec conformance: what changed and why

Verified against the Hermes source and docs rather than assumed:

| Constraint | Source of truth |
|---|---|
| Discovery walks for `SKILL.md` at any depth | `agent/skill_utils.py::iter_skill_index_files` |
| `references/ templates/ assets/ scripts/` are progressive-disclosure areas, never scanned as skills | `skill_utils.py::SKILL_SUPPORT_DIRS` |
| System-prompt index truncates descriptions at 60 chars (`desc[:57] + "..."`) | `skill_utils.py::SKILL_PROMPT_DESC_LIMIT` |
| `skills_list` carries descriptions up to 1024 chars | `tools/skills_tool.py` |
| Frontmatter at byte 0, closes `\n---\n`, YAML mapping; `name` matches `^[a-z][a-z0-9_-]*$`, ≤64 chars; body ≤100,000 chars | `skills/software-development/hermes-agent-skill-authoring/SKILL.md` |
| House body order: intro → When to Use → Prerequisites → Procedure → Pitfalls → Verification | same |
| `SOUL.md` loads from `HERMES_HOME` only | `docs/user-guide/features/personality` |

### 2.1 Frontmatter

Headcount skills carried two fields — `name` and `description`. Each migrated skill now carries the
full Hermes contract:

```yaml
---
name: chief-strategy-officer
description: "Owns where the business plays and how it wins. Multi-year portfolio choices, …"
version: 1.0.0
author: Chris Brock (cbrock84), ported to Hermes Agent
license: MIT
platforms: [linux, macos, windows]
category: corporate-strategy
metadata:
  hermes:
    category: corporate-strategy
    tags: [corporate-strategy, strategy, portfolio, corp-dev, executive]
    related_skills: [portfolio-strategy, mergers-and-acquisitions, scenario-planning, strategic-alliances]
---
```

- `platforms` is all three everywhere: the bodies are prose, and the one script (`agent-guard.mjs`)
  is Node.
- `category` is emitted both top-level (as the shipped
  `optional-skills/communication/one-three-one-rule` does) and under `metadata.hermes` (as
  `skill_utils.py` documents).
- `tags` derive from the source plugin's `keywords` plus the skill's own subject.
- `related_skills` are bare skill names, valid because all 143 are unique. Every entry resolves —
  the validator enforces it.
- Descriptions are double-quoted YAML scalars, so a colon or comma inside one cannot break parsing.

### 2.2 Body structure

Original prose is preserved; the sections were remapped to the Hermes house style.

| headcount section | Hermes section |
|---|---|
| *(the "Use this when…" trigger text in the description)* | **When to Use**, as bullets |
| H1 + opening prose, or "Why this role exists" | intro, 2–3 sentences |
| Remit / What this role owns / the skill's own method sections | **Procedure**, with the original subheads kept as `###` |
| Never / anti-patterns / "what does not work" | **Pitfalls** |
| Return contract / measurement / testing sections | **Verification** |
| Works with / Escalation | **Related**, with cross-references rewritten |

Where a skill had genuine preconditions, they were lifted into a **Prerequisites** section —
`programmatic-seo`, `referral-programs`, `parallel-agent-delivery`, `visual-reference-generation`,
`implementation-planning`, `agent-hierarchy`.

Every skill now ends with a **Related** section. Headcount's inline `department:skill` references
were rewritten to `enterprise/<department>/<skill>`, which is a `skill_view()`-loadable relative path
under the Hermes skills root. The validator rejects both a dangling path and any leftover
`department:skill` syntax.

### 2.3 What was carried verbatim

`executive/agent-hierarchy/references/{playbook.md,starter-rosters.md,bootstrap-prompt.md}` and
`executive/agent-hierarchy/scripts/agent-guard.mjs` — byte-identical to the source, confirmed with
`diff -r`. They are support files, loaded on demand via `skill_view(..., file_path=…)`, and Hermes
never scans them as skills.

---

## 3. Deliberate deviations

Two, both decided explicitly rather than by accident.

### 3.1 Descriptions exceed the authoring skill's 60-character rule

The Hermes skill-authoring spec says a description is "≤ 60 characters. One sentence." Headcount's
descriptions are 300–500 characters and carry the `Use this when…` trigger text that makes skills
auto-select correctly. Strict conformance would have moved all of that into the body, where the
system prompt cannot see it — weakening exactly the behavior the organization depends on.

**What was done instead:** a lead sentence of ≤57 characters ending in a period, followed by the
original trigger text.

- The system-prompt index truncates at 57 characters + `...`, so it lands cleanly at the end of the
  lead sentence.
- `skills_list` and `skill_view` return the full description (1024-char limit; the longest here is
  584, mean 360), so the trigger language survives where it is read.

The validator enforces the half that matters mechanically — lead sentence ≤57 chars and
period-terminated, total ≤1024 — and emits a `warn` for each of the 143 skills whose description
exceeds 60 characters. **Those 143 warnings are this deviation, and they are expected.** The run
reports 0 errors.

### 3.2 `SOUL.md` files are staged, not auto-loaded

Hermes loads `SOUL.md` exclusively from `HERMES_HOME` (or `~/.hermes/profiles/<name>/`), never from a
skills subdirectory. The 16 `SOUL.md` files here are therefore **personas staged for installation**,
not files Hermes picks up in place. Each department README says so and gives the copy command; the
top-level README covers both the one-profile-per-department and the single-profile-for-everything
configurations.

No `config.yaml` templates were generated: they would encode machine-local paths, which the authoring
spec forbids. The READMEs show the `skills.external_dirs` snippet with a `<path-to>` placeholder
instead.

---

## 4. Souls

Each `SOUL.md` follows the documented shape — Core Identity → Style → What to avoid → Domain posture
→ Escalation — at roughly 40–60 lines, written in the register of the function rather than filled
from a template. Source material was the department's own `chief-*` skill (remit, owned artifacts,
"Never" rules, escalation path) plus the corresponding charter in the source repo's `.claude/agents/`.

Two carry the reviewer-class stance explicitly in the soul itself, because it changes how the agent
must behave rather than merely what it knows:

- **security** — blocking findings are not overrulable by the department under review; the CISO
  reports independently of the CTO precisely because a security function inside delivery is measured
  on delivery.
- **legal-risk** — a producing department cannot approve its own contract terms, accept its own risk
  above threshold, or close its own compliance finding.

**executive** is the escalation endpoint: its soul states that nothing goes above it, and that where
a decision is genuinely the owner's it says so rather than deciding for them.

---

## 5. Verification

`scripts/validate_hermes_skills.py` reproduces Hermes' own discovery walk (including the
support-directory and metadata-directory prune rules) and then checks each skill against the spec:

- frontmatter starts at byte 0, closes with `\n---\n`, parses as a YAML mapping, no BOM
- `name` matches `^[a-z][a-z0-9_-]*$`, ≤64 chars, and equals its directory name
- required keys present: `name description version author license platforms metadata`
- `platforms` values valid; `metadata.hermes.tags` and `.category` non-empty
- every `related_skills` entry resolves to a real migrated skill
- description ≤1024 chars; lead sentence ≤57 chars and period-terminated
- body ≤100,000 chars, and contains both `## When to Use` and `## Verification`
- every `enterprise/<dept>/<skill>` path referenced in a body exists on disk
- no leftover Claude-plugin `department:skill` syntax
- subdirectories limited to `references|templates|assets|scripts`
- each department has both `SOUL.md` and `README.md`

### Results

```
143 skills in 16 departments (all departments): 0 errors, 143 warnings
```

The 143 warnings are the description-length deviation in §3.1, one per skill.

Independent count checks:

| Check | Expected | Actual |
|---|---:|---:|
| `find . -name SKILL.md \| wc -l` | 143 | 143 |
| department directories | 16 | 16 |
| `SOUL.md` files | 16 | 16 |
| department `README.md` files | 16 | 16 |
| support files carried verbatim | 4 | 4 |

`diff -r` against the source confirms `agent-hierarchy`'s `references/` and `agent-guard.mjs` are
byte-identical. Longest skill body is 6,068 characters (`executive/agent-hierarchy`), well inside the
100,000 limit.

### Prompt-index preview

`python3 scripts/validate_hermes_skills.py --index` prints the skill index Hermes would build, with
each description truncated exactly as the system prompt renders it, so the truncation is inspected
rather than assumed:

```
executive/
  agent-hierarchy      Designs orchestrator-and-subagent hierarchies. Splits age...
  ceo-advisor          Pressure-tests a decision before it is committed to. Surf...
  chief-executive      Sets direction and makes the calls no one else can. Alloc...
```

The cut lands after the lead sentence in every case, which is what §3.1 was designed for.

### Not verified here

No `hermes` CLI is installed on this machine and `~/.hermes` does not exist, so the tree has not been
loaded by a running Hermes agent. The validator reproduces the discovery and frontmatter rules from
the Hermes source, but a live `hermes skills list` against an installed profile is the remaining
confirmation step.

---

## 6. Notes and follow-ups

- **Four cross-references had no target.** Headcount skills referenced `technology:documentation`,
  `marketing:competitive-brief`, and `technology:testing-strategy`, none of which exist in the source
  repository. They were repointed to the nearest real skill —
  `enterprise/marketing/marketing-copywriting`, `enterprise/executive/ai-research-analyst`,
  `enterprise/technology/code-review`, and `enterprise/technology/test-driven-development` — and the
  validator now prevents the class of error recurring.
- **One repo-specific reference was generalized.** `agent-hierarchy` pointed at the source
  repository's own `docs/DECISION-LOG.md`; the migrated skill describes the decision-log format from
  `references/playbook.md` and cites the source repo as the worked example.
  `legal-risk/regulatory-compliance`'s pointer to `docs/USE-CASES.md` was replaced with the situation
  it described.
- **Three source agent charters have no plugin** — `.claude/agents/{legal-risk-review,
  security-review,repo-meta}.md` — and were out of scope. The reviewer-class stance they encode is
  preserved in the `security` and `legal-risk` souls and READMEs.
- **Nothing was committed.** The target is not a git repository, and committing was not part of the
  request.
