#!/usr/bin/env python3
"""Regenerate README.md from SKILL.md frontmatter. Run from the repo root."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

# security and cloud-devops lead because that is the work this collection is kept for.
LEAD = ("security", "cloud-devops")

BLURBS = {
    "security": "Audits, threat modeling, OWASP, cloud security, and review checklists.",
    "cloud-devops": "Kubernetes, Terraform, CI/CD, observability, and incident response.",
    "azure": "Per-service Azure SDK skills across Python, TypeScript, .NET, Java, and Rust.",
    "ai-ml": "Agents, RAG, prompts, evals, and LLM application workflows.",
    "integrations-automation": "Third-party APIs: Slack, Stripe, Notion, GitHub, and others.",
    "dev-tools": "Debugging, refactoring, code review, and git workflows.",
    "backend": "API and service frameworks, including FastAPI, Nest, and .NET.",
    "frontend": "React, Next.js, Tailwind, accessibility, and UI implementation.",
    "design-uiux": "Interface design, Figma, accessibility, and visual generation.",
    "seo-marketing": "SEO, content, and conversion-oriented writing.",
    "business-product": "Product, finance, and operations workflows.",
    "languages": "Language-specific implementation guidance.",
    "docs-writing": "Docs, changelogs, and technical writing.",
    "testing-qa": "Unit, end-to-end, and review testing.",
    "skills-meta": "Authoring, routing, and checking other skills.",
    "database": "SQL, migrations, and data stores.",
    "payments-fintech": "Billing, Stripe, and payments compliance.",
    "architecture-patterns": "DDD, CQRS, ADRs, and system design.",
    "odoo": "Odoo modules, ORM, and deployment.",
    "health-wellness": "Health and wellness domain helpers.",
    "game-dev": "Game engines and game-development workflows.",
    "context-memory": "Context windows, memory, and session restore.",
    "miscellaneous": "Skills that do not fit another category, including LibreOffice.",
    "functional-programming": "fp-ts and typed functional patterns.",
    "scientific-computing": "Python scientific stack and related libraries.",
    "hig-apple": "Apple Human Interface Guidelines.",
    "makepad": "Makepad UI.",
    "ai-personas": "Persona prompts for design and critique.",
    "three-js": "Three.js scenes, materials, and animation.",
    "apify": "Apify actor workflows.",
    "mobile": "iOS, Android, and React Native.",
    "documents": "Office and PDF document skills. Anthropic's official copies live here.",
    "hugging-face": "Hugging Face datasets, jobs, and training.",
    "expo": "Expo and EAS.",
    "leiloeiro": "Brazilian real-estate auction workflows (upstream author: renat).",
    "n8n-automation": "n8n workflow skills.",
    "conductor": "Multi-track agent orchestration.",
    "robius": "Robius application structure.",
    "wordpress": "WordPress themes, plugins, and WooCommerce.",
}

HIGHLIGHTS = (
    "security-audit",
    "web-security-testing",
    "api-security-testing",
    "aws-security-audit",
    "aws-iam-best-practices",
    "aws-secrets-rotation",
    "aws-compliance-checker",
    "kubernetes-deployment",
    "terraform-infrastructure",
    "linux-troubleshooting",
    "k8s-manifest-generator",
    "production-code-audit",
)


def load_skills() -> list[dict[str, str]]:
    skills = []
    for path in sorted(ROOT.rglob("SKILL.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        match = FRONTMATTER.match(text)
        if match is None:
            continue
        data = yaml.safe_load(match.group(1)) or {}
        rel = path.relative_to(ROOT)
        description = " ".join(str(data.get("description", "")).split())
        if len(description) > 220:
            description = description[:217].rstrip() + "..."
        skills.append(
            {
                "name": str(data.get("name", "")).strip(),
                "description": description.replace("|", "\\|"),
                "category": rel.parts[0],
                "path": str(rel),
            }
        )
    return skills


def category_order(counts: dict[str, int]) -> list[str]:
    rest = [name for name in counts if name not in LEAD]
    rest.sort(key=lambda name: (-counts[name], name))
    return list(LEAD) + rest


def table(rows: list[dict[str, str]], include_category: bool) -> str:
    if include_category:
        header = "| Skill | Category | What it does |\n|---|---|---|\n"
        body = [
            f"| `{row['name']}` | `{row['category']}` | {row['description']} |"
            for row in rows
        ]
    else:
        header = "| Skill | What it does |\n|---|---|\n"
        body = [f"| `{row['name']}` | {row['description']} |" for row in rows]
    return header + "\n".join(body)


def render(skills: list[dict[str, str]]) -> str:
    by_name = {skill["name"]: skill for skill in skills}
    counts: dict[str, int] = {}
    grouped: dict[str, list[dict[str, str]]] = {}
    for skill in skills:
        counts[skill["category"]] = counts.get(skill["category"], 0) + 1
        grouped.setdefault(skill["category"], []).append(skill)
    order = category_order(counts)
    highlights = [by_name[name] for name in HIGHLIGHTS if name in by_name]

    summary_lines = [
        "| Category | Skills | What it covers |",
        "|---|---:|---|",
    ]
    for category in order:
        blurbs = BLURBS.get(category, "Skills in this category.")
        summary_lines.append(f"| `{category}` | {counts[category]} | {blurbs} |")

    sections = []
    for category in order:
        rows = sorted(grouped[category], key=lambda row: row["name"])
        sections.append(
            f"### `{category}` ({counts[category]})\n\n"
            f"{BLURBS.get(category, '')}\n\n"
            f"{table(rows, include_category=False)}\n"
        )

    missing = [name for name in HIGHLIGHTS if name not in by_name]
    if missing:
        raise SystemExit(f"highlight skills missing: {missing}")

    return f"""# Claude Code skills

Skills for [Claude Code](https://code.claude.com/docs/en/skills), collected by [Lesley Oredia](https://github.com/lloredia) (DevSecOps / DevOps / SRE).

A skill is a folder with a `SKILL.md` file. Claude Code reads the YAML frontmatter (`name`, `description`) to decide when the skill applies, then follows the rest of the file. Optional `scripts/`, `references/`, and `examples/` folders sit next to `SKILL.md`.

This repository is a categorized snapshot of a local skills directory (1,292 skills, 39 categories). **Security and cloud/DevOps skills are listed first** because that is the work the collection is kept for. Most of the text was copied from public skill packs. Attribution, licenses, and the files that were removed as duplicates are in [THIRD_PARTY.md](THIRD_PARTY.md).

## Install and use

Clone into its own folder so this set does not mix with skills you write yourself:

```bash
git clone https://github.com/lloredia/My-claudeCode-skills-.git ~/.claude/skills/lloredia
```

Claude Code loads every `SKILL.md` under `~/.claude/skills`. In a session, name the skill (`security-audit`) or describe the task in the words of its `description`. Update with:

```bash
git -C ~/.claude/skills/lloredia pull
```

To install a smaller set, copy one category:

```bash
cp -R ~/.claude/skills/lloredia/security ~/.claude/skills/security
cp -R ~/.claude/skills/lloredia/cloud-devops ~/.claude/skills/cloud-devops
```

`ui-styling` shares font files with `canvas-design` through a relative symlink, so those two skills need to stay inside this clone.

## Layout

```text
<category>/<skill-name>/SKILL.md
<category>/<skill-name>/scripts/       # optional
<category>/<skill-name>/references/    # optional
```

Every skill sits at that depth. Nested skills that used to live under another skill (game-development variants, AWS security checks, LibreOffice apps, and project templates) were moved up with `git mv`.

## Start here

| Skill | Category | What it does |
|---|---|---|
{chr(10).join(f"| `{row['name']}` | `{row['category']}` | {row['description']} |" for row in highlights)}

## Categories

{chr(10).join(summary_lines)}

## All skills

{chr(10).join(sections)}
## Third-party material

Copied skills keep the license file they shipped with. See [THIRD_PARTY.md](THIRD_PARTY.md) before you redistribute a subset, especially the Anthropic document skills under `documents/`.

## Contributing

1. Add one folder: `<category>/<skill-name>/SKILL.md`.
2. Frontmatter needs `name` (lowercase words separated by hyphens, matching the folder, at most 64 characters) and a `description` Claude can match against the user's request.
3. Put helpers in `scripts/` and long reference notes in `references/`. Keep `SKILL.md` to the workflow.
4. Do not commit secrets, `.env` files, virtualenvs, `node_modules`, caches, or large binaries. Copy [`.env.example`](.env.example) and fill it in locally.
5. From the repo root:

```bash
python scripts/check_skill_frontmatter.py
pip install ruff && ruff check .
```

6. If you add or rename a skill, regenerate this file:

```bash
python scripts/render_readme.py
```

Open a pull request. GitHub Actions runs the frontmatter check and Ruff.

## Secrets

Skills that call an API read keys from the environment. Nothing in the tree is a live credential. Placeholder tokens in examples (including Telegram's published sample bot token) are called out in the pull request that introduced this layout.
"""


def main() -> None:
    skills = load_skills()
    text = render(skills)
    destination = ROOT / "README.md"
    destination.write_text(text)
    print(f"wrote {destination} ({len(skills)} skills, {destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
