#!/usr/bin/env python3
"""Validate the enterprise skill tree against the Hermes Agent skill spec.

Reproduces the discovery rules Hermes itself applies (``os.walk`` for
``SKILL.md``, with support directories and metadata directories pruned) and then
checks every discovered skill against the frontmatter contract documented in
``NousResearch/hermes-agent`` (``skills/software-development/
hermes-agent-skill-authoring/SKILL.md`` and ``agent/skill_utils.py``).

Run with no arguments to check the whole tree, or pass one or more department
directory names to check only those. Pass ``--index`` to print the skill index
Hermes would build instead, so the 60-character prompt truncation can be
inspected rather than assumed.

Exit status is 0 when no errors were found, 1 otherwise. Warnings never fail the
run: they flag deliberate, documented deviations (see OUTPUT.md).
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import yaml

# ── Spec constants, mirrored from the Hermes source ────────────────────────

#: ``agent/skill_utils.py::SKILL_PROMPT_DESC_LIMIT`` — descriptions longer than
#: this are rendered as ``desc[:57] + "..."`` in the system-prompt skill index.
SKILL_PROMPT_DESC_LIMIT = 60

#: ``tools/skills_tool.py`` header — the limit ``skills_list`` carries.
SKILL_LIST_DESC_LIMIT = 1024

#: ``hermes-agent-skill-authoring`` — hard body ceiling.
BODY_LIMIT = 100_000

#: ``agent/skill_utils.py::SKILL_SUPPORT_DIRS`` — progressive-disclosure areas
#: loaded through ``skill_view(..., file_path=...)``, never scanned as skills.
SUPPORT_DIRS = frozenset(("references", "templates", "assets", "scripts"))

#: ``agent/skill_utils.py::EXCLUDED_SKILL_DIRS`` (the subset that can occur here).
EXCLUDED_DIRS = frozenset((".git", ".github", ".hub", ".archive", "__pycache__"))

NAME_RE = re.compile(r"^[a-z][a-z0-9_-]*$")
NAME_MAX = 64

REQUIRED_KEYS = ("name", "description", "version", "author", "license", "platforms", "metadata")
VALID_PLATFORMS = frozenset(("linux", "macos", "windows"))

#: Cross-references rewritten during migration, e.g. ``enterprise/finance/tax``.
XREF_RE = re.compile(r"\benterprise/([a-z][a-z0-9-]*)/([a-z][a-z0-9-]*)\b")

#: A leftover Claude-plugin reference (``department:skill``) that migration missed.
LEGACY_XREF_RE = re.compile(r"`([a-z][a-z0-9-]*):([a-z][a-z0-9-]*)`")

ROOT = Path(__file__).resolve().parent.parent


# ── Discovery (mirrors skill_utils.iter_skill_index_files) ─────────────────

def iter_skill_files(root: Path):
    """Yield every ``SKILL.md`` Hermes would treat as an active skill root."""
    root_str = str(root)
    matches: List[str] = []
    for dirpath, dirnames, filenames in os.walk(root_str):
        has_skill_md = "SKILL.md" in filenames
        dirnames[:] = [
            d for d in dirnames
            if d not in EXCLUDED_DIRS and not (has_skill_md and d in SUPPORT_DIRS)
        ]
        if has_skill_md:
            matches.append(os.path.join(dirpath, "SKILL.md"))
    for path in sorted(matches):
        yield Path(path)


def parse_frontmatter(text: str) -> Tuple[Dict[str, Any], str, List[str]]:
    """Split a SKILL.md into (frontmatter, body, structural errors)."""
    errors: List[str] = []
    if text.startswith("﻿"):
        return {}, text, ["frontmatter: file begins with a UTF-8 BOM"]
    if not text.startswith("---"):
        return {}, text, ["frontmatter: must start at byte 0 with '---'"]
    end = text.find("\n---\n", 3)
    if end == -1:
        return {}, text, ["frontmatter: no closing '\\n---\\n' fence"]
    raw = text[4:end]
    body = text[end + 5:]
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        return {}, body, [f"frontmatter: invalid YAML ({exc.__class__.__name__})"]
    if not isinstance(data, dict):
        return {}, body, ["frontmatter: does not parse as a YAML mapping"]
    return data, body, errors


def lead_sentence(description: str) -> str:
    """The first sentence — what the system-prompt index shows before truncating."""
    match = re.match(r"^(.*?[.!?])(\s|$)", description.strip())
    return match.group(1) if match else description.strip()


# ── Checks ─────────────────────────────────────────────────────────────────

def _check_name(fm: Dict[str, Any], dir_name: str) -> List[str]:
    """Validate the ``name`` key against the spec and its directory."""
    errors: List[str] = []
    name = str(fm.get("name", ""))
    if not NAME_RE.match(name):
        errors.append(f"name: {name!r} does not match ^[a-z][a-z0-9_-]*$")
    if len(name) > NAME_MAX:
        errors.append(f"name: {len(name)} chars exceeds the {NAME_MAX}-char limit")
    if name != dir_name:
        errors.append(f"name: {name!r} does not equal its directory name {dir_name!r}")
    return errors


def _check_description(fm: Dict[str, Any]) -> Tuple[List[str], List[str]]:
    """Validate ``description``; return (errors, warnings)."""
    errors: List[str] = []
    warnings: List[str] = []
    description = str(fm.get("description", "")).strip()
    if not description:
        return ["description: empty"], warnings
    if len(description) > SKILL_LIST_DESC_LIMIT:
        errors.append(
            f"description: {len(description)} chars exceeds the "
            f"{SKILL_LIST_DESC_LIMIT}-char skills_list limit"
        )
    lead = lead_sentence(description)
    if not lead.endswith((".", "!", "?")):
        errors.append("description: lead sentence is not period-terminated")
    if len(lead) > SKILL_PROMPT_DESC_LIMIT - 3:
        errors.append(
            f"description: lead sentence is {len(lead)} chars; must be "
            f"<= {SKILL_PROMPT_DESC_LIMIT - 3} so prompt-index truncation "
            f"falls on a sentence boundary"
        )
    if len(description) > SKILL_PROMPT_DESC_LIMIT:
        warnings.append(
            f"description: {len(description)} chars — truncated to "
            f"{SKILL_PROMPT_DESC_LIMIT} in the system-prompt index "
            f"(deliberate; see OUTPUT.md)"
        )
    return errors, warnings


def _check_platforms(fm: Dict[str, Any]) -> List[str]:
    """Validate the optional ``platforms`` list."""
    platforms = fm.get("platforms")
    if platforms is None:
        return []
    if not isinstance(platforms, list) or not platforms:
        return ["platforms: must be a non-empty list"]
    bad = [p for p in platforms if p not in VALID_PLATFORMS]
    return [f"platforms: unknown value(s) {bad}"] if bad else []


def _check_metadata(fm: Dict[str, Any], known: Dict[str, Path]) -> List[str]:
    """Validate the ``metadata.hermes`` mapping."""
    errors: List[str] = []
    metadata = fm.get("metadata")
    hermes = metadata.get("hermes") if isinstance(metadata, dict) else None
    if not isinstance(hermes, dict):
        return ["metadata: missing the 'hermes' mapping"]
    tags = hermes.get("tags")
    if not isinstance(tags, list) or not tags:
        errors.append("metadata.hermes.tags: missing or empty")
    if not str(hermes.get("category", "")).strip():
        errors.append("metadata.hermes.category: missing")
    for related in hermes.get("related_skills") or []:
        if related not in known:
            errors.append(f"metadata.hermes.related_skills: {related!r} does not exist")
    return errors


def _check_body(body: str) -> List[str]:
    """Validate body size and required sections."""
    errors: List[str] = []
    if len(body) > BODY_LIMIT:
        errors.append(f"body: {len(body)} chars exceeds the {BODY_LIMIT}-char limit")
    if "## When to Use" not in body:
        errors.append("body: missing the 'When to Use' section")
    if "## Verification" not in body:
        errors.append("body: missing the 'Verification' section")
    return errors


def _check_xrefs(text: str, body: str) -> List[str]:
    """Validate ``enterprise/<dept>/<skill>`` links and flag legacy syntax."""
    errors: List[str] = []
    for dept, skill in XREF_RE.findall(text):
        if not (ROOT / dept / skill / "SKILL.md").exists():
            errors.append(f"cross-reference: enterprise/{dept}/{skill} does not exist")
    for dept, skill in LEGACY_XREF_RE.findall(body):
        if (ROOT / dept / skill / "SKILL.md").exists():
            errors.append(
                f"cross-reference: `{dept}:{skill}` is Claude-plugin syntax; "
                f"rewrite as enterprise/{dept}/{skill}"
            )
    return errors


def _check_layout(skill_dir: Path) -> List[str]:
    """Reject subdirectories that are not Hermes support directories."""
    return [
        f"layout: unexpected subdirectory {child.name!r} "
        f"(support dirs are {sorted(SUPPORT_DIRS)})"
        for child in skill_dir.iterdir()
        if child.is_dir() and child.name not in SUPPORT_DIRS
    ]


def check_skill(path: Path, known: Dict[str, Path]) -> Tuple[List[str], List[str]]:
    """Return (errors, warnings) for one SKILL.md."""
    text = path.read_text(encoding="utf-8")
    fm, body, errors = parse_frontmatter(text)
    if not fm:
        return errors, []

    errors.extend(f"frontmatter: missing required key '{key}'"
                  for key in REQUIRED_KEYS if key not in fm)
    errors.extend(_check_name(fm, path.parent.name))
    desc_errors, warnings = _check_description(fm)
    errors.extend(desc_errors)
    errors.extend(_check_platforms(fm))
    errors.extend(_check_metadata(fm, known))
    errors.extend(_check_body(body))
    errors.extend(_check_xrefs(text, body))
    errors.extend(_check_layout(path.parent))
    return errors, warnings


def check_department(dept: Path) -> List[str]:
    """Return errors for a department directory's own required files."""
    errors = []
    for required in ("SOUL.md", "README.md"):
        if not (dept / required).is_file():
            errors.append(f"{dept.name}: missing {required}")
    return errors


def print_index(departments: List[Path]) -> int:
    """Print each skill as the system-prompt index would render it."""
    count = 0
    for dept in departments:
        print(f"\n{dept.name}/")
        for path in iter_skill_files(dept):
            fm, _, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
            description = str(fm.get("description", "")).strip()
            if len(description) > SKILL_PROMPT_DESC_LIMIT:
                shown = description[:SKILL_PROMPT_DESC_LIMIT - 3] + "..."
            else:
                shown = description
            print(f"  {path.parent.name:<42} {shown}")
            count += 1
    print(f"\n{count} skills indexed")
    return 0


def main(argv: List[str]) -> int:
    """Validate the requested departments (or all) and return the exit status."""
    index_only = "--index" in argv
    argv = [a for a in argv if a != "--index"]
    departments = (
        [ROOT / a for a in argv]
        if argv
        else sorted(
            d for d in ROOT.iterdir()
            if d.is_dir() and d.name not in {"scripts"} and not d.name.startswith(".")
        )
    )

    for dept in departments:
        if not dept.is_dir():
            print(f"ERROR  {dept.name}: no such department directory")
            return 1

    if index_only:
        return print_index(departments)

    skill_files: List[Path] = []
    for dept in departments:
        skill_files.extend(iter_skill_files(dept))

    # Names must be resolvable tree-wide, not just within the departments asked
    # for, so related_skills across departments validate on a partial run.
    known = {p.parent.name: p for p in iter_skill_files(ROOT)}

    total_errors = 0
    total_warnings = 0
    for dept in departments:
        for message in check_department(dept):
            print(f"ERROR  {message}")
            total_errors += 1

    for path in skill_files:
        rel = path.relative_to(ROOT)
        errors, warnings = check_skill(path, known)
        for message in errors:
            print(f"ERROR  {rel}: {message}")
        for message in warnings:
            print(f"warn   {rel}: {message}")
        total_errors += len(errors)
        total_warnings += len(warnings)

    scope = ", ".join(d.name for d in departments) if argv else "all departments"
    print(
        f"\n{len(skill_files)} skills in {len(departments)} departments "
        f"({scope}): {total_errors} errors, {total_warnings} warnings"
    )
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
