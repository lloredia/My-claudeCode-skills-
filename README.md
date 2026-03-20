<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Claude_AI_logo.svg/1200px-Claude_AI_logo.svg.png" alt="Claude Code Skills" width="100" />
</p>

<h1 align="center">Claude Code Skills Collection</h1>

<p align="center">
  <strong>1,282 curated skills across 39 categories — the largest open collection for Claude Code.</strong>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> &bull;
  <a href="#-category-breakdown">Categories</a> &bull;
  <a href="#-skill-highlights">Highlights</a> &bull;
  <a href="#-usage">Usage</a> &bull;
  <a href="#-contributing">Contributing</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/total_skills-1,282-0066FF?style=for-the-badge&labelColor=000" />
  <img src="https://img.shields.io/badge/categories-39-8B5CF6?style=for-the-badge&labelColor=000" />
  <img src="https://img.shields.io/badge/claude_code-compatible-10B981?style=for-the-badge&labelColor=000" />
  <img src="https://img.shields.io/badge/license-open-F59E0B?style=for-the-badge&labelColor=000" />
</p>

---

## What Are Skills?

Skills are **plug-and-play expertise modules** for Claude Code. Each skill transforms Claude into a domain specialist with production-ready patterns, security best practices, and framework-specific knowledge.

```
You:    /react-patterns        →  Claude becomes a React architecture expert
You:    /docker-expert         →  Claude optimizes containers & hardens security
You:    /stripe-integration    →  Claude builds PCI-compliant payment flows
You:    /ethical-hacking       →  Claude runs full penetration test assessments
You:    /kubernetes-architect  →  Claude designs production K8s clusters
```

---

## Quick Start

```bash
# One command to install all 1,282 skills
git clone https://github.com/lloredia/My-claudeCode-skills-.git ~/.claude/skills
```

Then in Claude Code, invoke any skill:
```
/skill-name
```

---

## Distribution Overview

```
AI & Machine Learning    ████████████████████████████████████████████  100
Integrations & Automation████████████████████████████████████████████  100
Azure SDK Collection     ██████████████████████████████████████████████████  120
Developer Tools          ██████████████████████████████████████████  95
Security & Pentesting    █████████████████████████████████████  80
Cloud & DevOps           ████████████████████████████████  69
Backend Development      █████████████████████████████  64
Frontend Development     ████████████████████████  55
Design & UI/UX           █████████████████████  47
SEO & Marketing          ███████████████████  42
Languages                ██████████████████  41
Business & Product       ██████████████████  41
Documentation            ███████████████  35
Testing & QA             ██████████████  34
Skills & Meta Tools      █████████████  32
Database                 ████████████  27
Payments & Fintech       ███████████  25
Architecture             ███████████  25
Odoo ERP                 ██████████  24
Health & Wellness        █████████  19
Other (13 categories)    ██████████████████████████  ~130
```

---

## Category Breakdown

<!-- ═══════════════════════════════════════════ -->

### <img src="https://img.shields.io/badge/-AI%20%26%20ML-FF6B6B?style=flat-square" /> AI & Machine Learning `100 skills`

> LLM applications, multi-agent systems, RAG, embeddings, ML pipelines, prompt engineering

<p>
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" />
  <img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat-square&logo=huggingface&logoColor=000" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" />
</p>

| Top Skills | What It Does |
|-----------|-------------|
| `ai-engineer` | Production LLM apps, RAG systems, and intelligent agents |
| `ai-agents-architect` | Multi-agent orchestration and swarm design |
| `langgraph` | LangGraph stateful agent workflows |
| `crewai` | Multi-agent collaboration with CrewAI |
| `pydantic-ai` | Type-safe AI agents with Pydantic |
| `rag-implementation` | Retrieval-Augmented Generation architecture |
| `prompt-engineering` | Advanced prompt design and optimization |
| `llm-evaluation` | LLM output quality evaluation frameworks |
| `computer-vision-expert` | SOTA computer vision techniques |
| `voice-ai-development` | Real-time conversational voice AI |

<!-- ═══════════════════════════════════════════ -->

### <img src="https://img.shields.io/badge/-Security-DC2626?style=flat-square" /> Security & Penetration Testing `80 skills`

> Offensive security, OWASP, threat modeling, vulnerability scanning, compliance, hardening

<p>
  <img src="https://img.shields.io/badge/Burp_Suite-FF6633?style=flat-square&logo=burpsuite&logoColor=white" />
  <img src="https://img.shields.io/badge/Metasploit-2596CD?style=flat-square&logo=metasploit&logoColor=white" />
  <img src="https://img.shields.io/badge/OWASP-000000?style=flat-square&logo=owasp&logoColor=white" />
  <img src="https://img.shields.io/badge/Nmap-4682B4?style=flat-square" />
  <img src="https://img.shields.io/badge/Wireshark-1679A7?style=flat-square&logo=wireshark&logoColor=white" />
  <img src="https://img.shields.io/badge/Semgrep-22A47F?style=flat-square" />
</p>

| Top Skills | What It Does |
|-----------|-------------|
| `007` | Full security audit — STRIDE/PASTA, OWASP, Red/Blue Team |
| `ethical-hacking-methodology` | Complete penetration testing lifecycle |
| `burp-suite-testing` | Web application security testing |
| `sql-injection-testing` | SQL injection detection and exploitation |
| `xss-html-injection` | Cross-site scripting attacks and defense |
| `cloud-penetration-testing` | AWS/Azure/GCP security assessments |
| `threat-modeling-expert` | STRIDE methodology and risk mapping |
| `vulnerability-scanner` | Automated vulnerability analysis |
| `malware-analyst` | Malware reverse engineering |
| `red-team-tactics` | Red team engagement strategies |

<!-- ═══════════════════════════════════════════ -->

### <img src="https://img.shields.io/badge/-Frontend-3B82F6?style=flat-square" /> Frontend Development `55 skills`

> React, Next.js, Angular, Svelte, Astro, Tailwind, design systems, component architecture

<p>
  <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=000" />
  <img src="https://img.shields.io/badge/Next.js-000?style=flat-square&logo=nextdotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/Angular-DD0031?style=flat-square&logo=angular&logoColor=white" />
  <img src="https://img.shields.io/badge/Svelte-FF3E00?style=flat-square&logo=svelte&logoColor=white" />
  <img src="https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" />
</p>

| Top Skills | What It Does |
|-----------|-------------|
| `react-patterns` | Hooks, composition, and TypeScript patterns |
| `nextjs-best-practices` | App Router, SSR, ISR, and RSC patterns |
| `angular` | Angular 20+ with signals and standalone components |
| `sveltekit` | Full-stack SvelteKit applications |
| `tailwind-design-system` | Production design systems with Tailwind |
| `shadcn` | shadcn/ui component management |
| `react-state-management` | Zustand, Jotai, Redux patterns |
| `astro` | Content-focused static site generation |
| `electron-development` | Desktop apps with Electron |
| `progressive-web-app` | PWA architecture and service workers |

<!-- ═══════════════════════════════════════════ -->

### <img src="https://img.shields.io/badge/-Backend-10B981?style=flat-square" /> Backend Development `64 skills`

> REST/GraphQL/gRPC APIs, microservices, serverless, auth, real-time systems

<p>
  <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/NestJS-E0234E?style=flat-square&logo=nestjs&logoColor=white" />
  <img src="https://img.shields.io/badge/GraphQL-E10098?style=flat-square&logo=graphql&logoColor=white" />
  <img src="https://img.shields.io/badge/gRPC-244C5A?style=flat-square" />
</p>

| Top Skills | What It Does |
|-----------|-------------|
| `backend-architect` | Scalable API design and distributed systems |
| `nestjs-expert` | Nest.js with DI, decorators, and middleware |
| `fastapi-pro` | High-performance async Python APIs |
| `django-pro` | Django 5.x with async views |
| `laravel-expert` | Production Laravel engineering |
| `graphql-architect` | GraphQL federation and schema design |
| `hono` | Ultra-fast edge-ready web APIs |
| `trpc-fullstack` | End-to-end type-safe APIs |
| `firebase` | Firebase backend-as-a-service |
| `supabase-automation` | Supabase CLI, auth, and edge functions |

<!-- ═══════════════════════════════════════════ -->

### <img src="https://img.shields.io/badge/-Cloud%20%26%20DevOps-F59E0B?style=flat-square" /> Cloud & DevOps `69 skills`

> AWS, GCP, Docker, Kubernetes, Terraform, CI/CD, monitoring, incident response

<p>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" />
  <img src="https://img.shields.io/badge/Terraform-844FBA?style=flat-square&logo=terraform&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" />
  <img src="https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white" />
</p>

| Top Skills | What It Does |
|-----------|-------------|
| `docker-expert` | Container optimization and security hardening |
| `kubernetes-architect` | K8s cluster design and GitOps |
| `terraform-specialist` | Terraform/OpenTofu IaC patterns |
| `aws-skills` | AWS infrastructure and services |
| `github-actions-templates` | Production CI/CD workflows |
| `grafana-dashboards` | Monitoring dashboard creation |
| `helm-chart-scaffolding` | K8s Helm chart development |
| `gitops-workflow` | GitOps with ArgoCD/Flux |
| `incident-responder` | SRE incident response |
| `cloud-architect` | Multi-cloud architecture design |

<!-- ═══════════════════════════════════════════ -->

### <img src="https://img.shields.io/badge/-Azure-0078D4?style=flat-square" /> Azure SDK Collection `120 skills`

> Complete Azure service SDKs across .NET, Java, Python, TypeScript, and Rust

<p>
  <img src="https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white" />
  <img src="https://img.shields.io/badge/.NET-512BD4?style=flat-square&logo=dotnet&logoColor=white" />
  <img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/Rust-000?style=flat-square&logo=rust&logoColor=white" />
</p>

| Service Area | Skills |
|-------------|--------|
| **AI & Cognitive** | `azure-ai-openai-dotnet`, `azure-ai-projects-*`, `azure-ai-vision-*`, `azure-ai-voicelive-*` |
| **Storage** | `azure-storage-blob-*`, `azure-storage-queue-*`, `azure-cosmos-*` |
| **Messaging** | `azure-servicebus-*`, `azure-eventhub-*`, `azure-eventgrid-*` |
| **Identity & Security** | `azure-identity-*`, `azure-keyvault-*`, `azure-security-*` |
| **Monitoring** | `azure-monitor-*`, `azure-appconfiguration-*` |
| **Management** | `azure-mgmt-*`, `azure-resource-manager-*` |

<!-- ═══════════════════════════════════════════ -->

### <img src="https://img.shields.io/badge/-Database-8B5CF6?style=flat-square" /> Database `27 skills`

> PostgreSQL, NoSQL, vector databases, migrations, query optimization, ORMs

<p>
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Prisma-2D3748?style=flat-square&logo=prisma&logoColor=white" />
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white" />
  <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" />
  <img src="https://img.shields.io/badge/Pinecone-000?style=flat-square" />
  <img src="https://img.shields.io/badge/Neon-00E699?style=flat-square" />
</p>

| Top Skills | What It Does |
|-----------|-------------|
| `postgresql-optimization` | PostgreSQL performance tuning |
| `database-architect` | Database architecture and design |
| `prisma-expert` | Prisma ORM advanced patterns |
| `drizzle-orm-expert` | Drizzle ORM for TypeScript |
| `vector-database-engineer` | Vector DBs for AI/RAG |
| `sql-optimization-patterns` | Slow query transformation |
| `database-migration` | Zero-downtime schema migrations |
| `neon-postgres` | Serverless Postgres with Neon |

<!-- ═══════════════════════════════════════════ -->

### <img src="https://img.shields.io/badge/-Mobile-EC4899?style=flat-square" /> Mobile Development `12 skills` + Expo `8 skills`

> iOS (Swift/SwiftUI), Android (Kotlin/Compose), React Native, Flutter

<p>
  <img src="https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white" />
  <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white" />
  <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white" />
  <img src="https://img.shields.io/badge/React_Native-61DAFB?style=flat-square&logo=react&logoColor=000" />
  <img src="https://img.shields.io/badge/Expo-000020?style=flat-square&logo=expo&logoColor=white" />
</p>

| Top Skills | What It Does |
|-----------|-------------|
| `ios-developer` | Native iOS with Swift/SwiftUI |
| `android-jetpack-compose-expert` | Modern Android with Compose |
| `flutter-expert` | Cross-platform Flutter with Dart 3 |
| `react-native-architecture` | Production React Native patterns |
| `expo-deployment` | Expo production deployment |
| `app-store-optimization` | ASO for iOS and Android |

<!-- ═══════════════════════════════════════════ -->

### <img src="https://img.shields.io/badge/-Testing-14B8A6?style=flat-square" /> Testing & Quality `34 skills`

> TDD, E2E testing, Playwright, Jest, Pytest, code review, load testing

<p>
  <img src="https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white" />
  <img src="https://img.shields.io/badge/Jest-C21325?style=flat-square&logo=jest&logoColor=white" />
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white" />
  <img src="https://img.shields.io/badge/k6-7D64FF?style=flat-square&logo=k6&logoColor=white" />
  <img src="https://img.shields.io/badge/Vitest-6E9F18?style=flat-square&logo=vitest&logoColor=white" />
</p>

| Top Skills | What It Does |
|-----------|-------------|
| `test-driven-development` | TDD red-green-refactor workflow |
| `playwright-skill` | Browser automation and E2E testing |
| `javascript-testing-patterns` | Jest/Vitest testing guide |
| `python-testing-patterns` | Pytest patterns and strategies |
| `code-review-excellence` | High-quality code review practices |
| `k6-load-testing` | Performance and load testing |
| `tdd-orchestrator` | Full TDD workflow orchestration |

<!-- ═══════════════════════════════════════════ -->

### <img src="https://img.shields.io/badge/-Integrations-6366F1?style=flat-square" /> Integrations & Automation `100 skills`

> 50+ SaaS platforms — Slack, GitHub, Jira, Notion, HubSpot, Stripe, and more

<p>
  <img src="https://img.shields.io/badge/Slack-4A154B?style=flat-square&logo=slack&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/Jira-0052CC?style=flat-square&logo=jira&logoColor=white" />
  <img src="https://img.shields.io/badge/Notion-000?style=flat-square&logo=notion&logoColor=white" />
  <img src="https://img.shields.io/badge/Zapier-FF4A00?style=flat-square&logo=zapier&logoColor=white" />
  <img src="https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white" />
</p>

| Top Skills | What It Does |
|-----------|-------------|
| `slack-bot-builder` | Slack Bolt bot framework |
| `github-automation` | GitHub repos, issues, and PRs |
| `jira-automation` | Jira task automation |
| `notion-automation` | Notion workspace automation |
| `discord-bot-architect` | Production Discord bots |
| `telegram-bot-builder` | Telegram bot development |
| `shopify-development` | Shopify apps and themes |
| `zapier-make-patterns` | No-code automation architecture |
| `hubspot-automation` | HubSpot CRM operations |

<!-- ═══════════════════════════════════════════ -->

### <img src="https://img.shields.io/badge/-Payments-059669?style=flat-square" /> Payments & Fintech `25 skills`

> Stripe, PayPal, crypto, DeFi, billing, PCI compliance, financial modeling

<p>
  <img src="https://img.shields.io/badge/Stripe-635BFF?style=flat-square&logo=stripe&logoColor=white" />
  <img src="https://img.shields.io/badge/PayPal-003087?style=flat-square&logo=paypal&logoColor=white" />
  <img src="https://img.shields.io/badge/Ethereum-3C3C3D?style=flat-square&logo=ethereum&logoColor=white" />
  <img src="https://img.shields.io/badge/Solidity-363636?style=flat-square&logo=solidity&logoColor=white" />
  <img src="https://img.shields.io/badge/Plaid-000?style=flat-square" />
</p>

| Top Skills | What It Does |
|-----------|-------------|
| `stripe-integration` | Checkout, subscriptions, and webhooks |
| `paypal-integration` | PayPal payment processing |
| `pci-compliance` | PCI DSS compliance implementation |
| `blockchain-developer` | Web3 and smart contract development |
| `solidity-security` | Smart contract security auditing |
| `defi-protocol-templates` | DeFi protocol implementation |

<!-- ═══════════════════════════════════════════ -->

### <img src="https://img.shields.io/badge/-Architecture-7C3AED?style=flat-square" /> Architecture & Patterns `25 skills`

> DDD, microservices, event sourcing, CQRS, clean architecture, ADRs

<p>
  <img src="https://img.shields.io/badge/DDD-000?style=flat-square" />
  <img src="https://img.shields.io/badge/CQRS-444?style=flat-square" />
  <img src="https://img.shields.io/badge/Event_Sourcing-666?style=flat-square" />
  <img src="https://img.shields.io/badge/C4_Model-004488?style=flat-square" />
  <img src="https://img.shields.io/badge/Clean_Architecture-888?style=flat-square" />
</p>

| Top Skills | What It Does |
|-----------|-------------|
| `domain-driven-design` | DDD strategic and tactical design |
| `microservices-patterns` | Microservices architecture mastery |
| `event-sourcing-architect` | Event sourcing and CQRS |
| `architecture-decision-records` | ADR creation and management |
| `saga-orchestration` | Distributed transaction patterns |
| `clean-code` | Clean code principles (Uncle Bob) |

<!-- ═══════════════════════════════════════════ -->

### <img src="https://img.shields.io/badge/-Languages-F97316?style=flat-square" /> Programming Languages `41 skills`

> Deep expertise for 15+ languages including Python, TypeScript, Go, Rust, Java, C++

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white" />
  <img src="https://img.shields.io/badge/Rust-000?style=flat-square&logo=rust&logoColor=white" />
  <img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white" />
  <img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white" />
  <img src="https://img.shields.io/badge/Elixir-4B275F?style=flat-square&logo=elixir&logoColor=white" />
  <img src="https://img.shields.io/badge/Ruby-CC342D?style=flat-square&logo=ruby&logoColor=white" />
</p>

| Language | Skills |
|----------|--------|
| **Python** | `python-pro`, `python-patterns`, `python-testing-patterns`, `python-packaging`, `async-python-patterns` |
| **TypeScript/JS** | `typescript-pro`, `typescript-expert`, `typescript-advanced-types`, `javascript-mastery`, `javascript-pro` |
| **Go** | `golang-pro`, `go-concurrency-patterns` |
| **Rust** | `rust-pro`, `rust-async-patterns`, `systems-programming-rust-project` |
| **C/C++** | `c-pro`, `cpp-pro`, `arm-cortex-expert` |
| **JVM** | `java-pro`, `kotlin-coroutines-expert`, `scala-pro` |
| **Shell** | `bash-pro`, `bash-scripting`, `posix-shell-pro`, `powershell-windows` |
| **Other** | `ruby-pro`, `php-pro`, `elixir-pro`, `haskell-pro`, `julia-pro`, `csharp-pro` |

<!-- ═══════════════════════════════════════════ -->

### <img src="https://img.shields.io/badge/-Design-D946EF?style=flat-square" /> Design & UI/UX `47 skills`

> Interface design, design systems, accessibility, media generation, 3D graphics

<p>
  <img src="https://img.shields.io/badge/Figma-F24E1E?style=flat-square&logo=figma&logoColor=white" />
  <img src="https://img.shields.io/badge/Three.js-000?style=flat-square&logo=threedotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/WCAG-005A9C?style=flat-square" />
  <img src="https://img.shields.io/badge/Framer_Motion-0055FF?style=flat-square&logo=framer&logoColor=white" />
  <img src="https://img.shields.io/badge/Remotion-000?style=flat-square" />
</p>

| Top Skills | What It Does |
|-----------|-------------|
| `ui-ux-pro-max` | Advanced UI/UX design intelligence |
| `ui-designer` | Design system extraction from references |
| `accessibility-compliance-*` | WCAG accessibility auditing |
| `threejs-skills` | 3D graphics with Three.js (13 skills) |
| `remotion` | Programmatic video generation |
| `canvas-design` | Visual art in PNG/PDF |
| `favicon` | Favicon generation from source images |

<!-- ═══════════════════════════════════════════ -->

### <img src="https://img.shields.io/badge/-SEO%20%26%20Marketing-EF4444?style=flat-square" /> SEO & Marketing `42 skills`

> Technical SEO, content strategy, CRO, paid ads, analytics, growth engineering

<p>
  <img src="https://img.shields.io/badge/Google_Analytics-E37400?style=flat-square&logo=googleanalytics&logoColor=white" />
  <img src="https://img.shields.io/badge/Ahrefs-FF8C00?style=flat-square" />
  <img src="https://img.shields.io/badge/Schema.org-006DB0?style=flat-square" />
  <img src="https://img.shields.io/badge/PostHog-000?style=flat-square&logo=posthog&logoColor=white" />
  <img src="https://img.shields.io/badge/Mixpanel-7856FF?style=flat-square&logo=mixpanel&logoColor=white" />
</p>

| Top Skills | What It Does |
|-----------|-------------|
| `seo-audit` | Technical SEO auditing |
| `seo-content-writer` | SEO-optimized content creation |
| `seo-keyword-strategist` | Keyword analysis and strategy |
| `marketing-psychology` | Behavioral science for marketing |
| `paid-ads` | PPC and performance marketing |
| `growth-engine` | Product growth engineering |
| `analytics-tracking` | Analytics implementation and auditing |

<!-- ═══════════════════════════════════════════ -->

### <img src="https://img.shields.io/badge/-Dev%20Tools-374151?style=flat-square" /> Developer Tools & Workflows `95 skills`

> Git workflows, debugging, refactoring, code quality, performance profiling, CLI tools

<p>
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" />
  <img src="https://img.shields.io/badge/ESLint-4B32C3?style=flat-square&logo=eslint&logoColor=white" />
  <img src="https://img.shields.io/badge/Prettier-F7B93E?style=flat-square&logo=prettier&logoColor=000" />
  <img src="https://img.shields.io/badge/ShellCheck-555?style=flat-square" />
</p>

| Top Skills | What It Does |
|-----------|-------------|
| `commit` | Smart git commit workflow |
| `systematic-debugging` | Root cause analysis methodology |
| `production-code-audit` | Deep codebase security + quality scan |
| `vibe-code-auditor` | AI-generated code auditing |
| `performance-optimizer` | Performance bottleneck identification |
| `dx-optimizer` | Developer experience improvement |
| `legacy-modernizer` | Legacy codebase refactoring |

<!-- ═══════════════════════════════════════════ -->

### <img src="https://img.shields.io/badge/-Business-0EA5E9?style=flat-square" /> Business & Product `41 skills`

> Product management, startup strategy, financial modeling, competitive analysis, legal

| Top Skills | What It Does |
|-----------|-------------|
| `product-manager` | Senior PM with 6 knowledge domains |
| `startup-financial-modeling` | 3-5 year financial projections |
| `pricing-strategy` | Pricing and packaging design |
| `competitive-landscape` | Competitive analysis frameworks |
| `market-sizing-analysis` | TAM/SAM/SOM sizing |
| `launch-strategy` | SaaS product launch planning |

<!-- ═══════════════════════════════════════════ -->

### More Categories

| Category | Skills | Highlights |
|----------|--------|------------|
| <img src="https://img.shields.io/badge/-Docs-64748B?style=flat-square" /> **Documentation** | 35 | `docs-architect`, `api-documentation`, `wiki-architect`, `tutorial-engineer` |
| <img src="https://img.shields.io/badge/-Health-22C55E?style=flat-square" /> **Health & Wellness** | 19 | `fitness-analyzer`, `nutrition-analyzer`, `sleep-analyzer`, `mental-health-analyzer` |
| <img src="https://img.shields.io/badge/-FP-A855F7?style=flat-square" /> **Functional Programming** | 15 | `fp-pragmatic`, `fp-async`, `fp-backend`, `fp-react`, `fp-refactor` |
| <img src="https://img.shields.io/badge/-Science-06B6D4?style=flat-square" /> **Scientific Computing** | 15 | `qiskit`, `biopython`, `scikit-learn`, `matplotlib`, `astropy` |
| <img src="https://img.shields.io/badge/-Odoo-714B67?style=flat-square" /> **Odoo ERP** | 24 | `odoo-module-developer`, `odoo-orm-expert`, `odoo-accounting-setup` |
| <img src="https://img.shields.io/badge/-Apple-000?style=flat-square" /> **Apple HIG** | 14 | `hig-foundations`, `hig-patterns`, `hig-components-*` |
| <img src="https://img.shields.io/badge/-Game-EAB308?style=flat-square" /> **Game Development** | 9 | `unity-developer`, `unreal-engine-cpp-pro`, `godot-gdscript-patterns`, `bevy-ecs-expert` |
| <img src="https://img.shields.io/badge/-AI%20Personas-F472B6?style=flat-square" /> **AI Personas** | 13 | `steve-jobs`, `elon-musk`, `yann-lecun`, `andrej-karpathy`, `sam-altman` |
| <img src="https://img.shields.io/badge/-Documents-78716C?style=flat-square" /> **Document Generation** | 13 | `pdf`, `docx`, `pptx`, `xlsx`, `latex-paper-conversion` |
| <img src="https://img.shields.io/badge/-3D-000?style=flat-square" /> **Three.js** | 13 | `threejs-fundamentals`, `threejs-shaders`, `threejs-animation`, `threejs-materials` |
| <img src="https://img.shields.io/badge/-Makepad-E44D26?style=flat-square" /> **Makepad** | 13 | `makepad-basics`, `makepad-widgets`, `makepad-shaders`, `makepad-layout` |
| <img src="https://img.shields.io/badge/-HF-FFD21E?style=flat-square" /> **Hugging Face** | 8 | `hugging-face-model-trainer`, `hugging-face-datasets`, `hugging-face-cli` |
| <img src="https://img.shields.io/badge/-WordPress-21759B?style=flat-square" /> **WordPress** | 4 | `wordpress`, `wordpress-plugin-development`, `wordpress-theme-development` |

---

## Skill Highlights

### Most Powerful Skills

| Skill | Category | Why It Stands Out |
|-------|----------|------------------|
| `007` | Security | Full-spectrum security audit in one command |
| `ai-engineer` | AI/ML | Production LLM apps, RAG, agents, vector search |
| `senior-fullstack` | Backend | Complete full-stack development toolkit |
| `kubernetes-architect` | DevOps | Enterprise K8s with GitOps and multi-cluster |
| `production-code-audit` | Dev Tools | Deep codebase scan with security + quality |
| `loki-mode` | Dev Tools | PRD to production in one session |
| `prompt-factory` | AI/ML | Mega-prompt generation across 15 domains |
| `10x-fullstack-engineer` | Backend | Architecture, implement, debug, optimize, review |

### Unique Skills You Didn't Know Existed

| Skill | What It Does |
|-------|-------------|
| `steve-jobs` | Brainstorm with a simulated Steve Jobs persona |
| `tcm-constitution-analyzer` | Traditional Chinese Medicine body constitution analysis |
| `qiskit` | Quantum computing circuit design |
| `algorithmic-art` | Generative art with p5.js and creative coding |
| `speed` | RSVP speed reader for long text |
| `pipecat-friday-agent` | Iron Man FRIDAY-style voice AI assistant |
| `explain-like-socrates` | Learn concepts through Socratic questioning |

---

## Usage

### Invoke a skill
```bash
/skill-name          # Activates the skill for your session
```

### Find the right skill
```bash
/skill-router        # Describe your need, get routed to the best skill
```

### Install on a new machine
```bash
git clone https://github.com/lloredia/My-claudeCode-skills-.git ~/.claude/skills
```

### Keep in sync
```bash
cd ~/.claude/skills && git pull
```

---

## Folder Structure

```
~/.claude/skills/
├── category-name/                # 39 category folders
│   ├── skill-name/
│   │   ├── SKILL.md              # Skill definition (required)
│   │   ├── references/           # Reference docs (optional)
│   │   ├── scripts/              # Helper scripts (optional)
│   │   └── examples/             # Usage examples (optional)
│   └── ...
├── .gitignore
└── README.md
```

---

## Stats

```
Total Skills         1,282       Languages Covered    15+
Categories              39       SaaS Integrations    50+
Azure SDKs             120       Frameworks           40+
Security Skills         80       AI/ML Skills         100
```

---

## Contributing

1. Fork this repository
2. Create a skill folder inside the appropriate category:
```
category-name/your-skill-name/SKILL.md
```
3. Use this frontmatter template:
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
