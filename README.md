<!-- ──────────────────────────────────────────────────────────────────────── -->
<!--  My Claude Code Skills · 1,296 plug-and-play expertise modules         -->
<!--  Drop in ~/.claude/skills · invoke via /skill-name                     -->
<!-- ──────────────────────────────────────────────────────────────────────── -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,40:1a1f2e,100:D97757&height=180&section=header&text=Claude%20Code%20Skills&fontColor=ffffff&fontSize=46&fontAlignY=38&desc=1%2C296%20expertise%20modules%20%C2%B7%2039%20categories&descSize=14&descAlignY=62&descAlign=50" alt="Claude Code Skills" />
</p>

<p align="center">
  <img alt="skills" src="https://img.shields.io/badge/skills-1%2C296-D97757" />
  <img alt="categories" src="https://img.shields.io/badge/categories-39-1f6feb" />
  <img alt="install" src="https://img.shields.io/badge/install-~/.claude/skills-22c55e" />
  <img alt="format" src="https://img.shields.io/badge/format-SKILL.md%20%2B%20YAML%20frontmatter-8b949e" />
  <img alt="claude code" src="https://img.shields.io/badge/claude%20code-compatible-D97757?logo=anthropic&logoColor=white" />
  <img alt="last update" src="https://img.shields.io/github/last-commit/lloredia/My-claudeCode-skills-?label=last%20update" />
  <img alt="license" src="https://img.shields.io/badge/license-unlicensed-8b949e" />
</p>

<p align="center">
  <b>The default Claude Code session knows everything in general and nothing in particular.</b><br/>
  Ask it to harden a Postgres schema, audit a Solidity contract, build a Stripe webhook, or design a K8s topology, and you're prompting from scratch each time. This repo is a 1,296-deep curated index of domain experts — every <code>/skill-name</code> swaps a generalist session into a specialist one with a battle-tested checklist already loaded.
</p>

<p align="center">
  <a href="#-quickstart">install →</a> ·
  <a href="#-categories">39 categories</a> ·
  <a href="#-skill-anatomy">skill format</a> ·
  <a href="docs/architecture.svg">architecture</a>
</p>

---

```text
$ claude --tail "audit the staging cluster's network policies"
[10:14:02] router      no skill loaded · session=generalist
[10:14:02] /skill-router "k8s network policy audit security"
[10:14:03] discover    candidates=[k8s-security-policies, security-audit, kubernetes-architect]
[10:14:03] match       k8s-security-policies score=0.94  category=cloud-devops/
[10:14:03] load        cloud-devops/k8s-security-policies/SKILL.md
[10:14:03] frontmatter risk=safe  source=community  date_added=2026-02-27
[10:14:03] activate    role=K8s NetworkPolicy auditor  refs=NIST 800-190 · CIS 5.x
[10:14:03] checklist   ingress default-deny? egress default-deny? ns-isolation?
[10:14:04] session     specialist mode active · prompt budget −470 tokens
[10:15:11] /skill-router "wait actually — also check pod security standards"
[10:15:11] suggest     k8s-manifest-generator + security-scanning-security-hardening
[10:15:11] stack       2 skills active concurrently · context preserved
[10:18:33] output      cluster audit · 14 findings · 3 critical · runbook attached
[10:18:33] done        skills used: 3  ·  invocations: 1 router + 2 named
```

---

## architecture

```mermaid
%%{init: {'theme':'base','themeVariables':{
  'primaryColor':'#0d1117','primaryTextColor':'#c9d1d9','primaryBorderColor':'#30363d',
  'lineColor':'#D97757','secondaryColor':'#161b22','tertiaryColor':'#1f6feb'
}}}%%
flowchart LR
  subgraph User["user"]
    CMD["/skill-name<br/>or /skill-router"]
  end
  subgraph CC["Claude Code"]
    LDR["skill loader"]
    SES["session context"]
  end
  subgraph Repo["~/.claude/skills/"]
    CAT["39 categories"]
    SK[("1,296 SKILL.md")]
    REF["references/<br/>scripts/<br/>examples/"]
  end
  subgraph FM["each SKILL.md"]
    NM["name"]
    DESC["description"]
    RSK["risk"]
    SRC["source"]
    DT["date_added"]
  end
  CMD --> LDR
  LDR --> CAT
  CAT --> SK
  SK --> REF
  SK --> FM
  LDR --> SES
  SES -. "domain expert mode" .- CMD
```

<!-- mobile fallback (GitHub mobile app does not render mermaid) -->
<p align="center"><img src="docs/architecture.svg" alt="architecture diagram" width="780" /></p>

> **Skills are filesystem.** Each `<category>/<skill-name>/SKILL.md` is a YAML-fronted markdown file Claude Code reads and uses to specialize the session. No registry, no plugin manager, no API — drop the directory at `~/.claude/skills/` and `git pull` updates everything.

---

## 📊 by the numbers

| | |
|---|---|
| **Total skills** | 1,296 (`find . -name SKILL.md \| wc -l`) |
| **Categories** | 39 |
| **Largest category** | `azure/` — 120 SKILL.md (per-SDK + per-language coverage) |
| **AI/ML** | 100 (agents · RAG · prompt engineering · voice · evals) |
| **Integrations / SaaS** | 99 (50+ third-party providers — Slack, Stripe, Salesforce, Notion, …) |
| **Dev tooling** | 95 (debugging, refactoring, code review, git workflows) |
| **Security** | 83 (pentest, SAST, threat modeling, OWASP top-10, cloud audit) |
| **Cloud / DevOps** | 69 (K8s, Terraform, observability, multi-cloud, GitOps) |
| **Frontend / Backend** | 54 / 65 |
| **Frontmatter format** | `name` · `description` · `risk` · `source` · `date_added` (YAML) |
| **Skill spawn rate** | 1,282 → 1,296 between commits `a2f4210` and `358f478` |

<sub><!-- TODO: measure --> Per-skill activation latency, average tokens-per-skill, and skill-router top-K accuracy aren't measured — add once a benchmark harness lands. The `risk` field is also `unknown` on most skills; backfilling that taxonomy is on the roadmap.</sub>

---

## 🚀 quickstart

```bash
# clone into Claude Code's skills directory
git clone https://github.com/lloredia/My-claudeCode-skills-.git ~/.claude/skills

# verify
ls ~/.claude/skills | head            # 39 category folders
find ~/.claude/skills -name SKILL.md | wc -l   # 1,296
```

then in any Claude Code session:

```text
/skill-router        # describe what you need; get routed to the best match
/<skill-name>        # invoke a specific skill directly
```

keep in sync:

```bash
cd ~/.claude/skills && git pull
```

---

## 🗂 categories

<details open>
<summary><b>top 12 by skill count</b></summary>

| # | Category | Skills | What's in it |
|---|---|---|---|
| 1 | `azure/` | 120 | Per-SDK + per-language modules (TS / Python / Java / .NET / Rust) covering Azure AI, Storage, Service Bus, Cosmos DB, Key Vault, App Config, Monitor, Identity, etc. |
| 2 | `ai-ml/` | 100 | Agents · RAG · prompt engineering · voice agents · evals · LangChain/LangGraph · Pydantic AI · multi-agent · LLM ops |
| 3 | `integrations-automation/` | 99 | 50+ third-party providers — Slack, Stripe, Salesforce, Notion, Jira, Linear, GitHub, Hubspot, Zendesk, Twilio, Sendgrid, … |
| 4 | `dev-tools/` | 95 | Debugging, refactoring, code review, git workflows, plan-writing, dependency upgrade, codebase audit |
| 5 | `security/` | 83 | Pentest playbooks, SAST, threat modeling, OWASP top-10, cloud audit, red-team tactics, malware analysis, web3 testing |
| 6 | `cloud-devops/` | 69 | K8s, Terraform, observability, multi-cloud, GitOps, incident response, CI/CD, distributed tracing, service mesh |
| 7 | `backend/` | 65 | FastAPI, NestJS, Hono, Convex, Trigger.dev, Cloudflare Workers, gRPC Go, Rails, Spring Boot, microservices patterns |
| 8 | `frontend/` | 54 | React (Next.js + state mgmt + patterns), Tailwind, shadcn, Astro, SvelteKit, Angular, Avalonia, Vue, animations |
| 9 | `design-uiux/` | 47 | UI Bot, accessibility audits, Figma, Imagen / Stable Diffusion, fal.ai, Remotion, podcasts, brand systems |
| 10 | `seo-marketing/` | 42 | SEO content, schema markup, CRO, paid ads, programmatic SEO, viral generators, social orchestration |
| 11 | `languages/` | 41 | Per-language pros (TypeScript, Python, Go, Rust, C++, Bash, Ruby, Elixir, Scala, …) plus framework guides |
| 12 | `business-product/` | 41 | Startup analyst, financial modeling, KPIs, market sizing, product manager toolkit, hr, contracts |

</details>

<details>
<summary><b>all 39 categories</b></summary>

| Category | Skills |
|---|---|
| `azure/` | 120 |
| `ai-ml/` | 100 |
| `integrations-automation/` | 99 |
| `dev-tools/` | 95 |
| `security/` | 83 |
| `cloud-devops/` | 69 |
| `backend/` | 65 |
| `frontend/` | 54 |
| `design-uiux/` | 47 |
| `seo-marketing/` | 42 |
| `languages/` | 41 |
| `business-product/` | 41 |
| `testing-qa/` | 34 |
| `docs-writing/` | 34 |
| `skills-meta/` | 32 |
| `database/` | 27 |
| `payments-fintech/` | 25 |
| `architecture-patterns/` | 25 |
| `odoo/` | 24 |
| `health-wellness/` | 19 |
| `game-dev/` | 19 |
| `context-memory/` | 18 |
| `miscellaneous/` | 17 |
| `scientific-computing/` | 15 |
| `functional-programming/` | 15 |
| `hig-apple/` | 14 |
| `three-js/` | 13 |
| `makepad/` | 13 |
| `documents/` | 13 |
| `ai-personas/` | 13 |
| `mobile/` | 12 |
| `apify/` | 12 |
| `hugging-face/` | 8 |
| `expo/` | 8 |
| `n8n-automation/` | 7 |
| `leiloeiro/` | 7 |
| `conductor/` | 7 |
| `robius/` | 5 |
| `wordpress/` | 4 |

(verified via `for d in */; do find "$d" -name SKILL.md \| wc -l; done`)

</details>

---

## 🧬 skill anatomy

every skill is a single `SKILL.md` with YAML frontmatter:

```yaml
---
name: ai-engineer
description: Build production-ready LLM applications, advanced RAG systems, and intelligent agents. Implements vector search, multimodal AI, agent orchestration, and enterprise AI integrations.
risk: unknown
source: community
date_added: '2026-02-27'
---
```

followed by markdown sections that Claude Code consumes to specialize the session:

- **Use this skill when** — trigger conditions
- **Do not use this skill when** — explicit non-goals
- **Instructions** — step-by-step workflow
- **Role Statement** — the persona Claude adopts
- *(optional)* `references/`, `scripts/`, `examples/` siblings — deep-dive material loaded on demand

```text
~/.claude/skills/
├── <category>/                     39 of these
│   └── <skill-name>/
│       ├── SKILL.md                ←— the only required file
│       ├── references/             ←— optional, loaded on demand
│       ├── scripts/                ←— optional, helper utilities
│       └── examples/               ←— optional, usage samples
└── docs/architecture.{mmd,svg}     this README's diagram
```

---

## ✨ highlights

a few skills that exemplify the breadth:

| Skill | Category | Why it stands out |
|---|---|---|
| `007` | security/ | full-spectrum security audit in one invocation |
| `ai-engineer` | ai-ml/ | production LLM apps, RAG, agents, vector search |
| `kubernetes-architect` | cloud-devops/ | enterprise K8s with GitOps + multi-cluster |
| `production-code-audit` | dev-tools/ | deep codebase scan with security + quality gates |
| `prompt-factory` | ai-ml/ | mega-prompt generation across 15 domains |
| `senior-fullstack` | backend/ | architect → implement → debug → optimize |
| `loki-mode` | dev-tools/ | PRD → production in a single session |
| `skill-router` | skills-meta/ | describe what you need; get the best skill |
| `skill-creator` | skills-meta/ | bootstrap a new skill with the canonical layout |

and a few you didn't know existed:

| Skill | What it does |
|---|---|
| `steve-jobs` | brainstorm with a simulated Steve Jobs persona |
| `tcm-constitution-analyzer` | Traditional Chinese Medicine body-constitution analysis |
| `qiskit` | quantum-computing circuit design |
| `algorithmic-art` | generative art with p5.js + creative coding |
| `speed` | RSVP speed-reader for long text |
| `pipecat-friday-agent` | Iron-Man-FRIDAY-style voice AI assistant |
| `explain-like-socrates` | learn concepts through Socratic questioning |
| `infinite-gratitude` | gratitude-journaling skill (yes, really) |

---

## 🎯 picking the right skill

three approaches, in order of laziness:

1. **`/skill-router`** — describe your task; the router skill scans the index and returns the best match. Default move when unsure.
2. **`/<exact-name>`** — if you know the skill, invoke it directly. Fastest.
3. **browse `<category>/`** — scan a category folder when you want to see what's available before committing.

multiple skills can stack inside one session — they layer rather than replace.

---

## 🛠 contributing

```bash
# 1. add a new skill
mkdir -p <category>/<skill-name>
cat > <category>/<skill-name>/SKILL.md <<'EOF'
---
name: <skill-name>
description: <one sentence — Claude reads this to decide if the skill matches>
risk: safe        # safe | unknown | critical
source: community  # community | personal | upstream
date_added: '2026-04-30'
---

# <Title>

## Use this skill when
- ...

## Do not use this skill when
- ...

## Instructions
- ...
EOF

# 2. update the README count
find . -name SKILL.md | wc -l    # bump the badge / by-the-numbers row

# 3. PR
```

guidance:

- **one skill per PR** — keep diffs small enough to review the description carefully
- **the description is the API** — Claude routes off it; vague descriptions don't get matched
- **prefer `safe` risk** explicitly when applicable; leaving `unknown` is fine if the skill could touch destructive ops
- **deep material goes in `references/`** — keep `SKILL.md` focused on the workflow, not the encyclopedia

the `skills-meta/skill-creator` and `skills-meta/skill-writer` skills can scaffold a compliant skill from a one-line description.

---

## 🗺 roadmap

### now
- **count drift fixes** — last two commits (`a2f4210`, `358f478`) reconciled 1,282 → 1,296; periodic re-counts to keep the badge honest.
- **risk taxonomy backfill** — most skills carry `risk: unknown`; sweeping toward `safe` / `critical` based on whether the skill triggers destructive ops.

### next
- **skill-router top-K eval** — measure routing accuracy on a labeled task set so the index quality is observable.
- **per-skill `examples/` adoption** — the layout supports `examples/` and `scripts/` siblings; most skills haven't filled them in yet.
- **deduplicate near-twins** — some categories have multiple skills covering the same ground (e.g., several `prompt-engineering` variants); merge or differentiate.

### later
- **plugin-style packaging** — turn cohesive subsets into installable plugin manifests rather than a flat folder pull.
- **skill telemetry hooks** — opt-in usage counts so the README can sort by "most invoked," not just "most files."

---

<p align="center"><sub>collected by <a href="https://github.com/lloredia">@lloredia</a> · <kbd>1,296</kbd> ways to specialize a session · drop in <code>~/.claude/skills</code> and go</sub></p>
