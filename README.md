<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Claude_AI_logo.svg/1200px-Claude_AI_logo.svg.png" alt="Claude Code Skills" width="120" />
</p>

<h1 align="center">Claude Code Skills Collection</h1>

<p align="center">
  <strong>1,282 curated skills for Claude Code — the largest open collection available.</strong>
</p>

<p align="center">
  <a href="#installation">Installation</a> &bull;
  <a href="#categories">Categories</a> &bull;
  <a href="#usage">Usage</a> &bull;
  <a href="#contributing">Contributing</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/skills-1282-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/categories-39-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/claude--code-compatible-green?style=for-the-badge" />
</p>

---

## What Are Skills?

Skills are markdown-based instruction sets that give Claude Code specialized expertise on demand. Instead of generic responses, skills provide **domain-specific patterns, best practices, and production-ready templates** for any technology or workflow.

```
/react-patterns       → Claude becomes a React architecture expert
/docker-expert        → Claude becomes a containerization specialist
/stripe-integration   → Claude builds PCI-compliant payment flows
/ethical-hacking      → Claude runs security assessments
```

---

## Installation

```bash
# Clone directly into your Claude Code skills directory
git clone git@github.com:lloredia/My-claudeCode-skills-.git ~/.claude/skills

# Or via HTTPS
git clone https://github.com/lloredia/My-claudeCode-skills-.git ~/.claude/skills
```

Skills are automatically available in Claude Code after cloning. Use them with `/skill-name` in any conversation.

---

## Directory Map

All 1,282 skills are organized into **39 category folders**:

```
~/.claude/skills/
├── ai-ml/                    (100)  LLMs, agents, RAG, ML pipelines, data science
├── ai-personas/               (13)  Steve Jobs, Elon Musk, Yann LeCun, etc.
├── apify/                     (12)  Web scraping & data extraction platform
├── architecture-patterns/     (25)  DDD, microservices, event sourcing, CQRS
├── azure/                    (120)  Azure SDKs across .NET, Java, Python, TS, Rust
├── backend/                   (64)  APIs, Node.js, Python, Go, Rust, Java frameworks
├── business-product/          (41)  Product management, startups, analytics, legal
├── cloud-devops/              (69)  Docker, K8s, Terraform, AWS, CI/CD, monitoring
├── conductor/                  (7)  Conductor workflow management
├── context-memory/            (18)  Context management & agent memory systems
├── database/                  (27)  SQL, NoSQL, migrations, vector DBs, optimization
├── design-uiux/               (47)  UI/UX, design systems, media, accessibility
├── dev-tools/                 (95)  Git, debugging, refactoring, code quality, CLI
├── docs-writing/              (35)  Technical writing, wikis, documentation
├── documents/                 (13)  PDF, DOCX, PPTX, XLSX generation
├── expo/                       (8)  Expo/React Native deployment & tooling
├── frontend/                  (55)  React, Angular, Svelte, Next.js, Tailwind
├── functional-programming/    (15)  fp-ts, Either, TaskEither, pipe/flow
├── game-dev/                   (9)  Unity, Unreal, Godot, Bevy
├── health-wellness/           (19)  Fitness, nutrition, sleep, mental health analysis
├── hig-apple/                 (14)  Apple Human Interface Guidelines
├── hugging-face/               (8)  Model training, datasets, evaluation
├── integrations-automation/  (100)  Slack, GitHub, Jira, Notion, 50+ SaaS platforms
├── languages/                 (41)  Python, TypeScript, Go, Rust, C++, Bash, etc.
├── leiloeiro/                  (7)  Brazilian auction analysis (Portuguese)
├── makepad/                   (13)  Makepad UI framework for Rust
├── miscellaneous/             (14)  Uncategorized / niche skills
├── mobile/                    (12)  iOS, Android, Flutter, React Native
├── n8n-automation/             (7)  n8n workflow automation
├── odoo/                      (24)  Odoo ERP modules & configuration
├── payments-fintech/          (25)  Stripe, PayPal, crypto, DeFi, billing
├── robius/                     (5)  Robius cross-platform framework
├── scientific-computing/      (15)  Qiskit, SciPy, BioPython, Matplotlib
├── security/                  (80)  Pentesting, OWASP, threat modeling, hardening
├── seo-marketing/             (42)  SEO, content marketing, CRO, paid ads
├── skills-meta/               (32)  Skill creation, Claude Code tools, MCP
├── testing-qa/                (34)  TDD, E2E, Playwright, code review, load testing
├── three-js/                  (13)  Three.js 3D graphics & WebGL
└── wordpress/                  (4)  WordPress dev, themes, plugins, WooCommerce
```

---

## Categories

### Security & Penetration Testing
> Offensive security, vulnerability scanning, compliance, and hardening

| Skill | Description |
|-------|-------------|
| `007` | Full security audit — STRIDE/PASTA threat modeling, OWASP, Red/Blue Team |
| `active-directory-attacks` | Active Directory exploitation techniques |
| `api-security-testing` | REST/GraphQL API security testing workflows |
| `broken-authentication` | Auth bypass and session management testing |
| `burp-suite-testing` | Web app security testing with Burp Suite |
| `cloud-penetration-testing` | AWS/Azure/GCP security assessments |
| `ethical-hacking-methodology` | Full penetration testing lifecycle |
| `file-path-traversal` | Path traversal vulnerability identification |
| `gha-security-review` | GitHub Actions workflow security audit |
| `idor-testing` | Insecure direct object reference testing |
| `linux-privilege-escalation` | Linux privesc enumeration and exploitation |
| `malware-analyst` | Malware reverse engineering and analysis |
| `metasploit-framework` | Metasploit exploitation framework |
| `pentest-checklist` | Comprehensive pentest checklists |
| `red-team-tactics` | Red team engagement methodologies |
| `scanning-tools` | Nmap, Nikto, and security scanner mastery |
| `shodan-reconnaissance` | Internet-facing asset reconnaissance |
| `sql-injection-testing` | SQL injection detection and exploitation |
| `ssh-penetration-testing` | SSH service security assessment |
| `vulnerability-scanner` | Automated vulnerability analysis |
| `web-security-testing` | Full web application security testing |
| `windows-privilege-escalation` | Windows privesc techniques |
| `xss-html-injection` | Cross-site scripting and HTML injection |
| `zeroize-audit` | Sensitive data memory zeroization audit |

### Frontend Development
> React, Angular, Vue, Next.js, UI components, and design systems

| Skill | Description |
|-------|-------------|
| `react-patterns` | Modern React hooks, composition, and TypeScript patterns |
| `react-best-practices` | Performance optimization for React apps |
| `react-state-management` | Redux, Zustand, Jotai, and state patterns |
| `react-modernization` | Class-to-hooks migration and version upgrades |
| `nextjs-best-practices` | Next.js App Router, SSR, and ISR patterns |
| `nextjs-app-router-patterns` | Advanced App Router patterns |
| `angular` | Angular 20+ with signals and modern patterns |
| `angular-best-practices` | Angular performance and architecture |
| `sveltekit` | Full-stack SvelteKit applications |
| `astro` | Content-focused static site generation |
| `senior-frontend` | Senior-level frontend architecture |
| `frontend-dev-guidelines` | React + TypeScript + Suspense-first guidelines |
| `shadcn` | shadcn/ui component management |
| `radix-ui-design-system` | Accessible design systems with Radix |
| `tailwind-patterns` | Tailwind CSS v4 patterns |
| `tailwind-design-system` | Production design systems with Tailwind |
| `tanstack-query-expert` | TanStack Query data fetching patterns |
| `zustand-store-ts` | Zustand state management stores |

### Backend Development
> APIs, microservices, databases, and server architecture

| Skill | Description |
|-------|-------------|
| `backend-architect` | Scalable API design and distributed systems |
| `nestjs-expert` | Nest.js with decorators and dependency injection |
| `fastapi-pro` | High-performance async Python APIs |
| `django-pro` | Django 5.x with async views and modern patterns |
| `laravel-expert` | Production Laravel engineering |
| `hono` | Ultra-fast web APIs with Hono |
| `golang-pro` | Go 1.21+ with modern concurrency patterns |
| `rust-pro` | Rust 1.75+ with async and systems programming |
| `java-pro` | Java 21+ with virtual threads and records |
| `python-pro` | Python 3.12+ with modern features |
| `typescript-pro` | Advanced TypeScript patterns |
| `elixir-pro` | Elixir with OTP and Phoenix |
| `ruby-pro` | Idiomatic Ruby with metaprogramming |
| `graphql-architect` | GraphQL federation and schema design |
| `grpc-golang` | Production gRPC services in Go |
| `trpc-fullstack` | End-to-end type-safe APIs |

### Mobile Development
> iOS, Android, React Native, Flutter, and Expo

| Skill | Description |
|-------|-------------|
| `ios-developer` | Native iOS with Swift/SwiftUI |
| `ios-swift-development` | Swift app architecture patterns |
| `swiftui-expert-skill` | SwiftUI component design |
| `android-jetpack-compose-expert` | Modern Android with Compose |
| `flutter-expert` | Cross-platform Flutter with Dart 3 |
| `react-native-architecture` | Production React Native patterns |
| `mobile-developer` | Cross-platform mobile development |
| `mobile-design` | Mobile UX patterns and touch interactions |
| `expo-deployment` | Expo production deployment |
| `expo-dev-client` | Expo development client builds |
| `expo-tailwind-setup` | Tailwind CSS in Expo apps |
| `app-store-optimization` | ASO for iOS and Android |
| `building-native-ui` | Native UI component development |

### Cloud & DevOps
> AWS, Azure, GCP, Docker, Kubernetes, CI/CD, and infrastructure

| Skill | Description |
|-------|-------------|
| `docker-expert` | Container optimization and security hardening |
| `kubernetes-architect` | K8s architecture and cluster design |
| `kubernetes-deployment` | K8s deployment workflows |
| `terraform-specialist` | Terraform/OpenTofu IaC patterns |
| `aws-skills` | AWS development and infrastructure |
| `aws-serverless` | Lambda, API Gateway, DynamoDB |
| `cloud-architect` | Multi-cloud architecture design |
| `gcp-cloud-run` | Google Cloud Run deployments |
| `devops-engineer` | Dockerfiles, CI/CD, and automation |
| `github-actions-templates` | Production GitHub Actions workflows |
| `gitlab-ci-patterns` | GitLab CI/CD pipeline patterns |
| `helm-chart-scaffolding` | Kubernetes Helm charts |
| `cloudformation-best-practices` | AWS CloudFormation templates |
| `cdk-patterns` | AWS CDK infrastructure patterns |
| `gitops-workflow` | GitOps with ArgoCD/Flux |
| `istio-traffic-management` | Istio service mesh traffic control |
| `prometheus-configuration` | Prometheus monitoring setup |
| `grafana-dashboards` | Production Grafana dashboards |

### Database
> SQL, NoSQL, migrations, optimization, and architecture

| Skill | Description |
|-------|-------------|
| `database-architect` | Database architecture and design |
| `database-optimizer` | Query and index optimization |
| `postgresql` | PostgreSQL-specific schema design |
| `postgresql-optimization` | PostgreSQL performance tuning |
| `prisma-expert` | Prisma ORM patterns |
| `drizzle-orm-expert` | Drizzle ORM for TypeScript |
| `nosql-expert` | Distributed NoSQL guidance |
| `database-migration` | Schema and data migration patterns |
| `sql-optimization-patterns` | Slow query transformation |
| `sql-pro` | Modern SQL with cloud-native patterns |
| `vector-database-engineer` | Vector DBs and embedding strategies |
| `neon-postgres` | Serverless Postgres with Neon |
| `convex` | Convex reactive backend |

### AI & Machine Learning
> LLMs, agents, RAG, embeddings, ML pipelines, and AI engineering

| Skill | Description |
|-------|-------------|
| `ai-engineer` | Production LLM applications and RAG systems |
| `ai-agent-development` | AI agent architecture and tools |
| `ai-agents-architect` | Multi-agent system design |
| `langgraph` | LangGraph agent orchestration |
| `langchain-architecture` | LangChain framework mastery |
| `pydantic-ai` | Production AI agents with Pydantic |
| `crewai` | Multi-agent collaboration with CrewAI |
| `ml-engineer` | Production ML systems with Python |
| `mlops-engineer` | ML pipelines and deployment |
| `rag-implementation` | RAG architecture and retrieval |
| `embedding-strategies` | Embedding selection and optimization |
| `llm-evaluation` | LLM evaluation frameworks |
| `llm-structured-output` | Reliable JSON/typed output from LLMs |
| `prompt-engineering` | Advanced prompt design patterns |
| `computer-vision-expert` | SOTA computer vision (2026) |
| `voice-ai-development` | Real-time voice AI systems |
| `local-llm-expert` | Local LLM inference and optimization |

### Payments & Fintech
> Stripe, PayPal, billing, PCI compliance, and crypto

| Skill | Description |
|-------|-------------|
| `stripe-integration` | Stripe checkout, subscriptions, webhooks |
| `paypal-integration` | PayPal payment processing |
| `payment-integration` | Multi-processor payment flows |
| `billing-automation` | Automated billing systems |
| `pci-compliance` | PCI DSS implementation |
| `plaid-fintech` | Plaid Link financial data |
| `crypto-bd-agent` | Crypto business development patterns |
| `defi-protocol-templates` | DeFi protocol implementation |
| `blockchain-developer` | Web3 and smart contract development |
| `solidity-security` | Smart contract security |

### Testing & Quality
> Unit testing, E2E, TDD, code review, and quality assurance

| Skill | Description |
|-------|-------------|
| `test-driven-development` | TDD workflow and patterns |
| `tdd-orchestrator` | TDD red-green-refactor orchestration |
| `e2e-testing` | End-to-end testing with Playwright |
| `playwright-skill` | Complete browser automation |
| `javascript-testing-patterns` | Jest/Vitest testing guide |
| `python-testing-patterns` | Pytest patterns and strategies |
| `code-review-excellence` | High-quality code review practices |
| `code-reviewer` | Automated code review |
| `unit-testing-test-generate` | Comprehensive test generation |
| `k6-load-testing` | Load testing with k6 |
| `webapp-testing` | Local web app testing |
| `test-fixing` | Systematic test failure resolution |

### SEO & Marketing
> Search optimization, content strategy, and growth

| Skill | Description |
|-------|-------------|
| `seo-fundamentals` | Core SEO principles and E-E-A-T |
| `seo-audit` | Technical SEO auditing |
| `seo-content-writer` | SEO-optimized content creation |
| `seo-keyword-strategist` | Keyword analysis and strategy |
| `seo-meta-optimizer` | Meta title and description optimization |
| `programmatic-seo` | Programmatic SEO at scale |
| `marketing-psychology` | Behavioral science for marketing |
| `content-marketer` | Content marketing strategy |
| `paid-ads` | Performance marketing and PPC |
| `copywriting` | Conversion-focused copywriting |
| `growth-engine` | Product growth engineering |
| `analytics-tracking` | Analytics implementation and auditing |

### Third-Party Integrations & Automation
> SaaS APIs, workflow automation, and platform integrations

| Skill | Description |
|-------|-------------|
| `slack-automation` | Slack workspace automation |
| `slack-bot-builder` | Slack Bolt bot framework |
| `github-automation` | GitHub repos, issues, and PRs |
| `jira-automation` | Jira task automation |
| `notion-automation` | Notion workspace automation |
| `hubspot-automation` | HubSpot CRM operations |
| `salesforce-automation` | Salesforce task automation |
| `discord-automation` | Discord server automation |
| `telegram-automation` | Telegram messaging automation |
| `zapier-make-patterns` | No-code automation architecture |
| `n8n-workflow-patterns` | n8n workflow design |
| `linear-automation` | Linear issue management |
| `shopify-automation` | Shopify store automation |
| `mailchimp-automation` | Email marketing automation |
| `sendgrid-automation` | Email delivery automation |
| `figma-automation` | Figma design automation |
| `vercel-automation` | Vercel deployment automation |

### Architecture & Patterns
> System design, DDD, microservices, event sourcing, and architecture decisions

| Skill | Description |
|-------|-------------|
| `architecture` | Architectural decision-making frameworks |
| `architecture-decision-records` | ADR creation patterns |
| `microservices-patterns` | Microservices architecture mastery |
| `domain-driven-design` | DDD strategic and tactical design |
| `event-sourcing-architect` | Event sourcing and CQRS |
| `saga-orchestration` | Distributed transaction patterns |
| `cqrs-implementation` | Command Query Responsibility Segregation |
| `api-design-principles` | REST and GraphQL API design |
| `monorepo-management` | Monorepo architecture with Nx/Turborepo |
| `clean-code` | Clean code principles |
| `software-architecture` | Quality-focused software design |
| `senior-architect` | Senior architecture patterns |

### Azure SDK Collection (70+)
> Complete Azure service SDKs across .NET, Java, Python, TypeScript, and Rust

| Category | Skills |
|----------|--------|
| **AI & Cognitive** | `azure-ai-openai-dotnet`, `azure-ai-projects-*`, `azure-ai-vision-*`, `azure-ai-voicelive-*`, `azure-ai-contentsafety-*` |
| **Storage** | `azure-storage-blob-*`, `azure-storage-queue-*`, `azure-storage-file-*`, `azure-cosmos-*` |
| **Messaging** | `azure-servicebus-*`, `azure-eventhub-*`, `azure-eventgrid-*`, `azure-web-pubsub-*` |
| **Security** | `azure-identity-*`, `azure-keyvault-*`, `azure-security-*` |
| **Monitoring** | `azure-monitor-*`, `azure-appconfiguration-*` |
| **Management** | `azure-mgmt-*`, `azure-resource-manager-*` |

### Game Development
> Unity, Unreal, Godot, Bevy, and Makepad

| Skill | Description |
|-------|-------------|
| `unity-developer` | Unity C# game development |
| `unity-ecs-patterns` | Unity DOTS/ECS patterns |
| `unreal-engine-cpp-pro` | Unreal Engine 5 C++ |
| `godot-gdscript-patterns` | Godot 4 GDScript |
| `godot-4-migration` | Godot version migration |
| `bevy-ecs-expert` | Bevy ECS game engine (Rust) |
| `makepad-*` | Makepad UI framework (11 skills) |
| `game-development` | Game dev orchestrator |

### Documentation & Writing
> Technical writing, API docs, content creation, and wikis

| Skill | Description |
|-------|-------------|
| `documentation` | Documentation generation workflows |
| `docs-architect` | Technical documentation architecture |
| `api-documentation` | API documentation generation |
| `readme` | README file creation |
| `wiki-architect` | Wiki structure design |
| `wiki-page-writer` | Wiki content creation |
| `blog-writing-guide` | Technical blog writing |
| `scientific-writing` | Research paper writing |
| `beautiful-prose` | High-quality prose writing |
| `copy-editing` | Professional copy editing |
| `tutorial-engineer` | Step-by-step tutorial creation |

### Business & Product
> Product management, startups, pricing, analytics, and strategy

| Skill | Description |
|-------|-------------|
| `product-manager` | Senior PM with 6 knowledge domains |
| `product-manager-toolkit` | PM tools and frameworks |
| `startup-analyst` | Startup business analysis |
| `startup-financial-modeling` | 3-5 year financial models |
| `pricing-strategy` | Pricing and packaging design |
| `competitive-landscape` | Competitive analysis frameworks |
| `market-sizing-analysis` | TAM/SAM/SOM market sizing |
| `business-analyst` | Modern business analysis |
| `launch-strategy` | SaaS product launch planning |
| `creating-financial-models` | Advanced financial modeling |

### Health & Wellness
> Health data analysis, nutrition, fitness, and medical information

| Skill | Description |
|-------|-------------|
| `ai-analyzer` | AI-driven comprehensive health analysis |
| `fitness-analyzer` | Exercise data analysis and training plans |
| `nutrition-analyzer` | Nutrition pattern analysis |
| `sleep-analyzer` | Sleep quality analysis |
| `health-trend-analyzer` | Health data trend analysis |
| `mental-health-analyzer` | Mental health pattern analysis |
| `weightloss-analyzer` | Weight loss data and metabolic analysis |
| `family-health-analyzer` | Family health history analysis |
| `tcm-constitution-analyzer` | Traditional Chinese Medicine analysis |
| `rehabilitation-analyzer` | Rehabilitation progress analysis |
| `claude-ally-health` | Medical health assistant |

### Design & UI/UX
> Interface design, design systems, accessibility, and Apple HIG

| Skill | Description |
|-------|-------------|
| `ui-ux-designer` | Interface design and wireframes |
| `ui-ux-pro-max` | Advanced UI/UX intelligence |
| `ui-designer` | Design system extraction |
| `ui-styling` | Beautiful, accessible interfaces |
| `hig-foundations` | Apple Human Interface Guidelines |
| `hig-patterns` | Apple HIG interaction patterns |
| `accessibility-compliance-accessibility-audit` | WCAG accessibility auditing |
| `wcag-audit-patterns` | Web accessibility audit guide |
| `mobile-design` | Mobile UX and touch patterns |
| `frontend-design` | Production-grade visual design |
| `design-orchestration` | Design workflow orchestration |

### Developer Tools & Workflows
> Git, CLI tools, debugging, refactoring, and developer experience

| Skill | Description |
|-------|-------------|
| `commit` | Smart git commit workflow |
| `git-advanced-workflows` | Advanced Git operations |
| `git-pushing` | Stage, commit, and push workflow |
| `create-branch` | Branch creation conventions |
| `create-pr` | Pull request creation |
| `pr-writer` | PR description writing |
| `debugger` | Error and test debugging |
| `systematic-debugging` | Root cause analysis methodology |
| `code-simplifier` | Code simplification |
| `dx-optimizer` | Developer experience improvement |
| `environment-setup-guide` | Dev environment setup |
| `vibe-code-auditor` | AI-generated code auditing |

### Language-Specific Deep Dives
> Expert-level guidance for individual programming languages

| Language | Skills |
|----------|--------|
| **Python** | `python-pro`, `python-patterns`, `python-testing-patterns`, `python-packaging`, `python-performance-optimization`, `async-python-patterns` |
| **TypeScript** | `typescript-pro`, `typescript-expert`, `typescript-advanced-types`, `javascript-mastery`, `javascript-pro` |
| **Go** | `golang-pro`, `go-concurrency-patterns`, `grpc-golang`, `temporal-golang-pro` |
| **Rust** | `rust-pro`, `rust-async-patterns`, `systems-programming-rust-project` |
| **C/C++** | `c-pro`, `cpp-pro`, `arm-cortex-expert` |
| **Java** | `java-pro`, `kotlin-coroutines-expert`, `scala-pro` |
| **Other** | `ruby-pro`, `php-pro`, `elixir-pro`, `haskell-pro`, `julia-pro`, `csharp-pro` |

### Odoo ERP (20+)
> Complete Odoo ecosystem covering every module

| Skill | Description |
|-------|-------------|
| `odoo-module-developer` | Custom module creation |
| `odoo-orm-expert` | ORM patterns and queries |
| `odoo-xml-views-builder` | XML view construction |
| `odoo-qweb-templates` | QWeb template engine |
| `odoo-security-rules` | Access control and security |
| `odoo-accounting-setup` | Accounting configuration |
| `odoo-inventory-optimizer` | Inventory management |
| `odoo-ecommerce-configurator` | eCommerce setup |
| `odoo-hr-payroll-setup` | HR and payroll |
| `odoo-manufacturing-advisor` | Manufacturing module |
| `odoo-migration-helper` | Version migration guide |
| `odoo-docker-deployment` | Docker deployment |

### AI Personas
> Simulated thought leaders for brainstorming and debate

| Skill | Description |
|-------|-------------|
| `steve-jobs` | Product vision and design thinking |
| `elon-musk` | First-principles engineering |
| `bill-gates` | Technology strategy |
| `warren-buffett` | Investment and business analysis |
| `sam-altman` | AI and startup strategy |
| `geoffrey-hinton` | Deep learning research |
| `yann-lecun` | AI research and philosophy |
| `andrej-karpathy` | Neural networks and AI engineering |
| `ilya-sutskever` | AI safety and scaling |

### Document Generation
> PDF, DOCX, PPTX, XLSX, and office document creation

| Skill | Description |
|-------|-------------|
| `pdf` / `pdf-official` | PDF creation and manipulation |
| `docx` / `docx-official` | Word document generation |
| `pptx` / `pptx-official` | PowerPoint presentation creation |
| `xlsx` / `xlsx-official` | Excel spreadsheet generation |
| `latex-paper-conversion` | LaTeX paper conversion |
| `nanobanana-ppt-skills` | AI-powered PPT generation |

### Functional Programming
> fp-ts, Effect, and functional patterns for TypeScript

| Skill | Description |
|-------|-------------|
| `fp-pragmatic` | Practical, jargon-free FP guide |
| `fp-ts-pragmatic` | fp-ts practical patterns |
| `fp-async` | Async patterns using TaskEither |
| `fp-backend` | FP patterns for backend services |
| `fp-react` | fp-ts patterns in React |
| `fp-errors` | Error handling as values |
| `fp-refactor` | Refactoring to functional style |
| `fp-pipe-ref` | Pipe and flow quick reference |
| `fp-either-ref` | Either type quick reference |
| `fp-option-ref` | Option type quick reference |

---

## Usage

### Invoke a skill
```
/skill-name
```
Example: `/docker-expert` activates Docker expertise for your session.

### Find the right skill
```
/skill-router
```
Describe your need and get routed to the best matching skill.

### Install on a new machine
```bash
git clone git@github.com:lloredia/My-claudeCode-skills-.git ~/.claude/skills
```

### Keep skills synced
```bash
cd ~/.claude/skills && git pull
```

### Add new skills
```bash
cd ~/.claude/skills
# Add your skill folder with SKILL.md
git add -A && git commit -m "Add new skill" && git push
```

---

## Folder Structure

```
~/.claude/skills/
├── category-name/             # Category folder (e.g., security/, frontend/)
│   ├── skill-name/
│   │   ├── SKILL.md           # Main skill definition (required)
│   │   ├── references/        # Reference docs (optional)
│   │   ├── scripts/           # Helper scripts (optional)
│   │   └── examples/          # Usage examples (optional)
│   └── another-skill/
│       └── SKILL.md
└── README.md
```

---

## Stats

| Metric | Count |
|--------|-------|
| **Total Skills** | 1,282 |
| **Category Folders** | 39 |
| **Azure SDK Skills** | 120 |
| **AI & ML Skills** | 100 |
| **Integrations** | 100 |
| **Dev Tools** | 95 |
| **Security Skills** | 80 |
| **Cloud & DevOps** | 69 |
| **Backend** | 64 |
| **Frontend** | 55 |
| **Languages** | 41 |

---

## Contributing

1. Fork this repository
2. Create a new folder with your skill name
3. Add a `SKILL.md` with proper frontmatter:
```yaml
---
name: your-skill-name
description: "One-line description of what this skill does"
risk: unknown
source: community
---
```
4. Submit a pull request

---

<p align="center">
  <sub>Maintained by <a href="https://github.com/lloredia">@lloredia</a> &mdash; Powered by Claude Code</sub>
</p>
