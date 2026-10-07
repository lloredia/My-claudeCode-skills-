#!/usr/bin/env python3
"""Check that every SKILL.md has closed YAML frontmatter with name and description."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def skill_paths() -> list[Path]:
    paths = []
    for path in ROOT.rglob("SKILL.md"):
        if ".git" in path.parts:
            continue
        paths.append(path)
    return sorted(paths)


def check(path: Path, names: dict[str, Path]) -> list[str]:
    rel = path.relative_to(ROOT)
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return [f"{rel}: frontmatter must start at the first line with '---'"]
    match = FRONTMATTER.match(text)
    if match is None:
        return [f"{rel}: frontmatter is not closed with '---'"]
    if len(rel.parts) != 3:
        errors.append(f"{rel}: expected <category>/<skill>/SKILL.md")
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return errors + [f"{rel}: invalid YAML ({exc})"]
    if not isinstance(data, dict):
        return errors + [f"{rel}: frontmatter must be a mapping"]

    name = data.get("name")
    description = data.get("description")
    if not isinstance(name, str) or not name.strip():
        errors.append(f"{rel}: missing name")
    else:
        slug = name.strip()
        if len(slug) > 64 or SLUG.fullmatch(slug) is None:
            errors.append(
                f"{rel}: name {slug!r} must be a lowercase slug of at most 64 characters"
            )
        previous = names.get(slug)
        if previous is not None:
            errors.append(f"{rel}: duplicate name {slug!r} (also {previous.relative_to(ROOT)})")
        else:
            names[slug] = path
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{rel}: missing description")
    return errors


def main() -> int:
    names: dict[str, Path] = {}
    errors: list[str] = []
    paths = skill_paths()
    for path in paths:
        errors.extend(check(path, names))
    if errors:
        print(f"{len(errors)} frontmatter error(s):", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"OK: {len(paths)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
