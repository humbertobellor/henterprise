# AGENTS.md

Standards for anyone, human or agent, changing this repository. Each rule is tagged:

- **[enforced]** `scripts/validate_hermes_skills.py` or CI fails on it.
- **[convention]** observed throughout the tree but not checked. Follow it anyway.

If a rule here and the validator disagree, the validator wins; fix this file in the same change.

## 1. What this repo is

A virtual agentic organization for [Hermes Agent](https://hermes-agent.nousresearch.com): 16
departments, each with a persona (`SOUL.md`) and a set of skills (`<skill>/SKILL.md`). The repo root
is the `enterprise/` tree, so a skill resolves as `enterprise/<department>/<skill>`. Derived from
`cbrock84/headcount` (MIT); see `OUTPUT.md` for what the migration changed.

## 2. Ground rules

1. Run `python scripts/validate_hermes_skills.py` before every commit. It must exit 0.
   Warnings do not fail the run; errors do.
2. Work on a feature branch and open a pull request into `master`. Do not push to `master`.
3. One logical change per pull request. Imperative commit subjects ("Add tax-treaty skill").
4. Never commit secrets or credentials.
5. Do not hand-edit generated output. `--index` prints the system-prompt skill index; do not paste it
   into files.

## 3. Project structure

```
<department>/
├── SOUL.md              department persona
├── README.md            coverage and skill table
└── <skill>/
    ├── SKILL.md
    └── references/ templates/ assets/ scripts/    (optional support dirs)
scripts/validate_hermes_skills.py                  spec validator
.github/workflows/                                 CI
README.md  OUTPUT.md  AGENTS.md  SECURITY.md  LICENSE
```

- **[enforced]** Every top-level directory except `scripts/` and dot-directories is treated as a
  department. A stray directory at the root fails validation (missing `SOUL.md`/`README.md`).
- **[enforced]** Every department has `SOUL.md` and `README.md`.
- **[enforced]** A skill directory may contain only the support dirs `references/`, `templates/`,
  `assets/`, `scripts/`. Any other subdirectory is an error. Support dirs are never scanned for
  skills.
- **[convention]** Skills sit one level below their department. No nested skills.
- **[convention]** Validator and tooling live in `scripts/`; workflows in `.github/workflows/`.

## 4. Skills standards

### Frontmatter

The file must start at byte 0 with `---` (no BOM) and close with `\n---\n`. **[enforced]**

| Key | Rule |
|---|---|
| `name` | **[enforced]** matches `^[a-z][a-z0-9_-]*$`, at most 64 chars, **equals the directory name** |
| `description` | **[enforced]** see below |
| `version` | **[enforced]** present (current skills use `1.0.0`) |
| `author` | **[enforced]** present |
| `license` | **[enforced]** present (`MIT`) |
| `platforms` | **[enforced]** non-empty list drawn from `linux`, `macos`, `windows` |
| `metadata.hermes.tags` | **[enforced]** non-empty list |
| `metadata.hermes.category` | **[enforced]** non-empty; **[convention]** equals the department name |
| `metadata.hermes.related_skills` | **[enforced]** every entry is the name of an existing skill |

**[convention]** Keep the top-level `category:` key alongside `metadata.hermes.category`, as existing
skills do. **[convention]** Preserve the upstream attribution in `author` when migrating a skill.

### Description

- **[enforced]** At most 1024 characters.
- **[enforced]** The first sentence ends in `.`, `!` or `?` and is at most 57 characters. The
  system-prompt index truncates descriptions to 60 characters (`desc[:57] + "..."`), so this keeps the
  cut on a sentence boundary.
- **[convention]** After the lead sentence, say what the skill covers, then a "Use this to ..."
  sentence listing the situations that should trigger it.
- Longer-than-60 descriptions produce a `warn` line. That is expected and deliberate.

### Body

- **[enforced]** At most 100,000 characters.
- **[enforced]** Contains the headings `## When to Use` and `## Verification` (exact text).
- **[convention]** Order: title, one-line summary, `## When to Use` (bullets), `## Procedure`
  (`###` subsections), `## Verification`.

### Cross-references

- **[enforced]** Link other skills as `enterprise/<department>/<skill>`. The target
  `<department>/<skill>/SKILL.md` must exist.
- **[enforced]** Claude-plugin syntax such as `` `finance:tax` `` is rejected when it points at an
  existing skill. Rewrite it as `enterprise/finance/tax`.

### Template

```markdown
---
name: example-skill
description: "Does one thing in a short lead sentence. What it covers in more detail. Use this to handle situation A, situation B, or situation C."
version: 1.0.0
author: Your Name
license: MIT
platforms: [linux, macos, windows]
category: example-department
metadata:
  hermes:
    category: example-department
    tags: [example, tag]
    related_skills: [another-existing-skill]
---

# Example skill

One-line summary of what this skill is for.

## When to Use

- The situations that should load this skill.

## Procedure

### First step

What to do and why.

## Verification

- How to tell the work was done correctly.
```

## 5. Department standards

- **`SOUL.md`** **[convention]**: first line `# <Department> — <Chief title>`, then a paragraph on what
  the role owns and where its word is final, then `## Style` and `## What to avoid`. Write in second
  person ("You are the ...").
- **`README.md`** **[convention]**: one-paragraph scope, then a `## Skills` table
  (`| Skill | What it does |`) listing every skill in the department, alphabetically.
- **[convention]** Adding or removing a skill also updates its department `README.md` table and the
  skill and department counts in the root `README.md` and `OUTPUT.md`.
- **[convention]** `security` and `legal-risk` are reviewer-class: their blocking findings are not
  overrulable by the department under review. Disagreement escalates to
  `enterprise/executive/chief-executive`. Do not weaken this when editing their skills or souls.
- **[convention]** Skills that touch tax, accounting, legal or security conclusions structure the
  question and route material positions to qualified advisers. Keep that boundary.

## 6. Development standards

- **[enforced]** Python must pass pylint (`.github/workflows/pylint.yml` runs
  `pylint $(git ls-files '*.py')`) on Python 3.8, 3.9 and 3.10. Keep syntax 3.8-compatible and keep
  `from __future__ import annotations`.
- **[convention]** The only third-party dependency is `pyyaml`. Do not add others without a reason
  stated in the pull request.
- **[convention]** Match the validator's style: type hints, a docstring on every function, spec
  constants commented with the Hermes source they mirror.
- **[convention]** A rule change touches the validator, this file, and (if it alters the migration
  story) `OUTPUT.md` together.
- **[enforced]** `validate-skills.yml` runs the validator on pull requests and on pushes to `master`
  that touch `**/SKILL.md`, `**/SOUL.md`, `**/README.md`, the validator or the workflow. Changes
  outside those paths, including this file, do not trigger it; run the validator locally.

Useful commands:

```bash
python scripts/validate_hermes_skills.py              # whole tree
python scripts/validate_hermes_skills.py finance      # one department
python scripts/validate_hermes_skills.py --index      # prompt index preview
```

## 7. Checklists

**Adding a skill**

1. Create `<department>/<skill-name>/SKILL.md` from the template; directory name = `name`.
2. Write a lead sentence of 57 characters or fewer, ending in a period.
3. Include `## When to Use` and `## Verification`.
4. Use `enterprise/<dept>/<skill>` for links; add only existing skills to `related_skills`.
5. Add a row to the department `README.md`; update the counts in the root `README.md`/`OUTPUT.md`.
6. Run the validator; it must exit 0.

**Adding a department**

1. Create `<department>/` with `SOUL.md` and `README.md` (section 5).
2. Add at least one skill (section 4).
3. Add the department to the table in the root `README.md` and update the counts.
4. Run the validator; it must exit 0.
