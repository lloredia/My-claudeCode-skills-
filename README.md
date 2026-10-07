# Claude Code skills

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
| `security-audit` | `security` | Comprehensive security auditing workflow covering web application testing, API security, penetration testing, vulnerability scanning, and security hardening. |
| `web-security-testing` | `security` | Web application security testing workflow for OWASP Top 10 vulnerabilities including injection, XSS, authentication flaws, and access control issues. |
| `api-security-testing` | `security` | API security testing workflow for REST and GraphQL APIs covering authentication, authorization, rate limiting, input validation, and security best practices. |
| `aws-security-audit` | `security` | Comprehensive AWS security posture assessment using AWS CLI and security best practices |
| `aws-iam-best-practices` | `security` | IAM policy review, hardening, and least privilege implementation |
| `aws-secrets-rotation` | `security` | Automate AWS secrets rotation for RDS, API keys, and credentials |
| `aws-compliance-checker` | `security` | Automated compliance checking against CIS, PCI-DSS, HIPAA, and SOC 2 benchmarks |
| `kubernetes-deployment` | `cloud-devops` | Kubernetes deployment workflow for container orchestration, Helm charts, service mesh, and production-ready K8s configurations. |
| `terraform-infrastructure` | `cloud-devops` | Terraform infrastructure as code workflow for provisioning cloud resources, creating reusable modules, and managing infrastructure at scale. |
| `linux-troubleshooting` | `cloud-devops` | Linux system troubleshooting workflow for diagnosing and resolving system issues, performance problems, and service failures. |
| `k8s-manifest-generator` | `cloud-devops` | Step-by-step guidance for creating production-ready Kubernetes manifests including Deployments, Services, ConfigMaps, Secrets, and PersistentVolumeClaims. |
| `production-code-audit` | `dev-tools` | Autonomously deep-scan entire codebase line-by-line, understand architecture and patterns, then systematically transform it to production-grade, corporate-level professional quality with optimizations |

## Categories

| Category | Skills | What it covers |
|---|---:|---|
| `security` | 83 | Audits, threat modeling, OWASP, cloud security, and review checklists. |
| `cloud-devops` | 69 | Kubernetes, Terraform, CI/CD, observability, and incident response. |
| `azure` | 120 | Per-service Azure SDK skills across Python, TypeScript, .NET, Java, and Rust. |
| `ai-ml` | 100 | Agents, RAG, prompts, evals, and LLM application workflows. |
| `integrations-automation` | 99 | Third-party APIs: Slack, Stripe, Notion, GitHub, and others. |
| `dev-tools` | 95 | Debugging, refactoring, code review, and git workflows. |
| `backend` | 65 | API and service frameworks, including FastAPI, Nest, and .NET. |
| `frontend` | 54 | React, Next.js, Tailwind, accessibility, and UI implementation. |
| `design-uiux` | 47 | Interface design, Figma, accessibility, and visual generation. |
| `seo-marketing` | 42 | SEO, content, and conversion-oriented writing. |
| `business-product` | 41 | Product, finance, and operations workflows. |
| `languages` | 41 | Language-specific implementation guidance. |
| `docs-writing` | 34 | Docs, changelogs, and technical writing. |
| `testing-qa` | 34 | Unit, end-to-end, and review testing. |
| `skills-meta` | 32 | Authoring, routing, and checking other skills. |
| `database` | 27 | SQL, migrations, and data stores. |
| `architecture-patterns` | 25 | DDD, CQRS, ADRs, and system design. |
| `payments-fintech` | 25 | Billing, Stripe, and payments compliance. |
| `odoo` | 24 | Odoo modules, ORM, and deployment. |
| `game-dev` | 19 | Game engines and game-development workflows. |
| `health-wellness` | 19 | Health and wellness domain helpers. |
| `context-memory` | 18 | Context windows, memory, and session restore. |
| `miscellaneous` | 17 | Skills that do not fit another category, including LibreOffice. |
| `functional-programming` | 15 | fp-ts and typed functional patterns. |
| `scientific-computing` | 15 | Python scientific stack and related libraries. |
| `hig-apple` | 14 | Apple Human Interface Guidelines. |
| `ai-personas` | 13 | Persona prompts for design and critique. |
| `makepad` | 13 | Makepad UI. |
| `three-js` | 13 | Three.js scenes, materials, and animation. |
| `apify` | 12 | Apify actor workflows. |
| `mobile` | 12 | iOS, Android, and React Native. |
| `documents` | 9 | Office and PDF document skills. Anthropic's official copies live here. |
| `expo` | 8 | Expo and EAS. |
| `hugging-face` | 8 | Hugging Face datasets, jobs, and training. |
| `conductor` | 7 | Multi-track agent orchestration. |
| `leiloeiro` | 7 | Brazilian real-estate auction workflows (upstream author: renat). |
| `n8n-automation` | 7 | n8n workflow skills. |
| `robius` | 5 | Robius application structure. |
| `wordpress` | 4 | WordPress themes, plugins, and WooCommerce. |

## All skills

### `security` (83)

Audits, threat modeling, OWASP, cloud security, and review checklists.

| Skill | What it does |
|---|---|
| `007` | Security audit, hardening, threat modeling (STRIDE/PASTA), Red/Blue Team, OWASP checks, code review, incident response, and infrastructure security for any project. |
| `active-directory-attacks` | Provide comprehensive techniques for attacking Microsoft Active Directory environments. Covers reconnaissance, credential harvesting, Kerberos attacks, lateral movement, privilege escalation, and domain dominance for... |
| `agentic-actions-auditor` | Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled i... |
| `anti-reversing-techniques` | AUTHORIZED USE ONLY: This skill contains dual-use security techniques. Before proceeding with any bypass or analysis: > 1. |
| `api-fuzzing-bug-bounty` | Provide comprehensive techniques for testing REST, SOAP, and GraphQL APIs during bug bounty hunting and penetration testing engagements. Covers vulnerability discovery, authentication bypass, IDOR exploitation, and AP... |
| `api-security-best-practices` | Implement secure API design patterns including authentication, authorization, input validation, rate limiting, and protection against common API vulnerabilities |
| `api-security-testing` | API security testing workflow for REST and GraphQL APIs covering authentication, authorization, rate limiting, input validation, and security best practices. |
| `attack-tree-construction` | Build comprehensive attack trees to visualize threat paths. Use when mapping attack scenarios, identifying defense gaps, or communicating security risks to stakeholders. |
| `audit-context-building` | Enables ultra-granular, line-by-line code analysis to build deep architectural context before vulnerability or bug finding. |
| `audit-skills` | Expert security auditor for AI Skills and Bundles. Performs non-intrusive static analysis to identify malicious patterns, data leaks, system stability risks, and obfuscated payloads across Windows, macOS, Linux/Unix,... |
| `aws-compliance-checker` | Automated compliance checking against CIS, PCI-DSS, HIPAA, and SOC 2 benchmarks |
| `aws-iam-best-practices` | IAM policy review, hardening, and least privilege implementation |
| `aws-penetration-testing` | Provide comprehensive techniques for penetration testing AWS cloud environments. Covers IAM enumeration, privilege escalation, SSRF to metadata endpoint, S3 bucket exploitation, Lambda code extraction, and persistence... |
| `aws-secrets-rotation` | Automate AWS secrets rotation for RDS, API keys, and credentials |
| `aws-security-audit` | Comprehensive AWS security posture assessment using AWS CLI and security best practices |
| `backend-security-coder` | Expert in secure backend coding practices specializing in input validation, authentication, and API security. Use PROACTIVELY for backend security implementations or security code reviews. |
| `binary-analysis-patterns` | Comprehensive patterns and techniques for analyzing compiled binaries, understanding assembly code, and reconstructing program logic. |
| `broken-authentication` | Identify and exploit authentication and session management vulnerabilities in web applications. Broken authentication consistently ranks in the OWASP Top 10 and can lead to account takeover, identity theft, and unauth... |
| `burp-suite-testing` | Execute comprehensive web application security testing using Burp Suite's integrated toolset, including HTTP traffic interception and modification, request analysis and replay, automated vulnerability scanning, and ma... |
| `burpsuite-project-parser` | Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findings, dumping proxy history or site map da... |
| `cloud-penetration-testing` | Conduct comprehensive security assessments of cloud infrastructure across Microsoft Azure, Amazon Web Services (AWS), and Google Cloud Platform (GCP). |
| `constant-time-analysis` | Analyze cryptographic code to detect operations that leak secret data through execution timing variations. |
| `cred-omega` | CISO operacional enterprise para gestao total de credenciais e segredos. |
| `differential-review` | Security-focused code review for PRs, commits, and diffs. |
| `ethical-hacking-methodology` | Master the complete penetration testing lifecycle from reconnaissance through reporting. This skill covers the five stages of ethical hacking methodology, essential tools, attack techniques, and professional reporting... |
| `fda-food-safety-auditor` | Expert AI auditor for FDA Food Safety (FSMA), HACCP, and PCQI compliance. Reviews food facility records and preventive controls. |
| `fda-medtech-compliance-auditor` | Expert AI auditor for Medical Device (SaMD) compliance, IEC 62304, and 21 CFR Part 820. Reviews DHFs, technical files, and software validation. |
| `ffuf-claude-skill` | Web fuzzing with ffuf |
| `ffuf-web-fuzzing` | Expert guidance for ffuf web fuzzing during penetration testing, including authenticated fuzzing with raw requests, auto-calibration, and result analysis |
| `file-path-traversal` | Identify and exploit file path traversal (directory traversal) vulnerabilities that allow attackers to read arbitrary files on the server, potentially including sensitive configuration files, credentials, and source c... |
| `firmware-analyst` | Expert firmware analyst specializing in embedded systems, IoT security, and hardware reverse engineering. |
| `frontend-security-coder` | Expert in secure frontend coding practices specializing in XSS prevention, output sanitization, and client-side security patterns. |
| `gha-security-review` | Find exploitable vulnerabilities in GitHub Actions workflows. Every finding MUST include a concrete exploitation scenario — if you can't build the attack, don't report it. |
| `html-injection-testing` | Identify and exploit HTML injection vulnerabilities that allow attackers to inject malicious HTML content into web applications. This vulnerability enables attackers to modify page appearance, create phishing pages, a... |
| `idor-testing` | Provide systematic methodologies for identifying and exploiting Insecure Direct Object Reference (IDOR) vulnerabilities in web applications. |
| `linux-privilege-escalation` | Execute systematic privilege escalation assessments on Linux systems to identify and exploit misconfigurations, vulnerable services, and security weaknesses that allow elevation from low-privilege user access to root-... |
| `malware-analyst` | Expert malware analyst specializing in defensive malware research, threat intelligence, and incident response. Masters sandbox analysis, behavioral analysis, and malware family identification. |
| `memory-forensics` | Comprehensive techniques for acquiring, analyzing, and extracting artifacts from memory dumps for incident response and malware analysis. |
| `memory-safety-patterns` | Cross-language patterns for memory-safe programming including RAII, ownership, smart pointers, and resource management. |
| `metasploit-framework` | ⚠️ AUTHORIZED USE ONLY > This skill is for educational purposes or authorized security assessments only. > You must have explicit, written permission from the system owner before using this tool. > Misuse of this tool... |
| `mobile-security-coder` | Expert in secure mobile coding practices specializing in input validation, WebView security, and mobile-specific security patterns. |
| `pentest-checklist` | Provide a comprehensive checklist for planning, executing, and following up on penetration tests. Ensure thorough preparation, proper scoping, and effective remediation of discovered vulnerabilities. |
| `pentest-commands` | Provide a comprehensive command reference for penetration testing tools including network scanning, exploitation, password cracking, and web application testing. Enable quick command lookup during security assessments. |
| `privilege-escalation-methods` | Provide comprehensive techniques for escalating privileges from a low-privileged user to root/administrator access on compromised Linux and Windows systems. Essential for penetration testing post-exploitation phase an... |
| `protocol-reverse-engineering` | Comprehensive techniques for capturing, analyzing, and documenting network protocols for security research, interoperability, and debugging. |
| `red-team-tactics` | Red team tactics principles based on MITRE ATT&CK. Attack phases, detection evasion, reporting. |
| `red-team-tools` | Implement proven methodologies and tool workflows from top security researchers for effective reconnaissance, vulnerability discovery, and bug bounty hunting. Automate common tasks while maintaining thorough coverage... |
| `reverse-engineer` | Expert reverse engineer specializing in binary analysis, disassembly, decompilation, and software analysis. Masters IDA Pro, Ghidra, radare2, x64dbg, and modern RE toolchains. |
| `sast-configuration` | Static Application Security Testing (SAST) tool setup, configuration, and custom rule creation for comprehensive security scanning across multiple programming languages. |
| `scanning-tools` | Master essential security scanning tools for network discovery, vulnerability assessment, web application testing, wireless security, and compliance validation. This skill covers tool selection, configuration, and pra... |
| `security-audit` | Comprehensive security auditing workflow covering web application testing, API security, penetration testing, vulnerability scanning, and security hardening. |
| `security-auditor` | Expert security auditor specializing in DevSecOps, comprehensive cybersecurity, and compliance frameworks. |
| `security-bluebook-builder` | Build a minimal but real security policy for sensitive apps. The output is a single, coherent Blue Book document using MUST/SHOULD/CAN language, with explicit assumptions, scope, and security gates. |
| `security-compliance-compliance-check` | You are a compliance expert specializing in regulatory requirements for software systems including GDPR, HIPAA, SOC2, PCI-DSS, and other industry standards. Perform comprehensive compliance audits and provide implemen... |
| `security-requirement-extraction` | Derive security requirements from threat models and business context. Use when translating threats into actionable requirements, creating security user stories, or building security test cases. |
| `security-scanning-security-dependencies` | You are a security expert specializing in dependency vulnerability analysis, SBOM generation, and supply chain security. Scan project dependencies across multiple ecosystems to identify vulnerabilities, assess risks,... |
| `security-scanning-security-hardening` | Coordinate multi-layer security scanning and hardening across application, infrastructure, and compliance controls. |
| `security-scanning-security-sast` | Static Application Security Testing (SAST) for code vulnerability analysis across multiple languages and frameworks |
| `semgrep-rule-creator` | Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections. |
| `semgrep-rule-variant-creator` | Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input, produces independent rule+test directories for... |
| `shodan-reconnaissance` | Provide systematic methodologies for leveraging Shodan as a reconnaissance tool during penetration testing engagements. |
| `smtp-penetration-testing` | Conduct comprehensive security assessments of SMTP (Simple Mail Transfer Protocol) servers to identify vulnerabilities including open relays, user enumeration, weak authentication, and misconfiguration. |
| `software-security` | A software security skill that integrates with Project CodeGuard to help AI coding agents write secure code and prevent common vulnerabilities. Use this skill when writing, reviewing, or modifying code to ensure secur... |
| `sql-injection-testing` | Execute comprehensive SQL injection vulnerability assessments on web applications to identify database security flaws, demonstrate exploitation techniques, and validate input sanitization mechanisms. |
| `sqlmap-database-pentesting` | Provide systematic methodologies for automated SQL injection detection and exploitation using SQLMap. |
| `ssh-penetration-testing` | Conduct comprehensive SSH security assessments including enumeration, credential attacks, vulnerability exploitation, tunneling techniques, and post-exploitation activities. This skill covers the complete methodology... |
| `stride-analysis-patterns` | Apply STRIDE methodology to systematically identify threats. Use when analyzing system security, conducting threat modeling sessions, or creating security documentation. |
| `supply-chain-risk-auditor` | Identifies dependencies at heightened risk of exploitation or takeover. Use when assessing supply chain attack surface, evaluating dependency health, or scoping security engagements. |
| `threat-mitigation-mapping` | Map identified threats to appropriate security controls and mitigations. Use when prioritizing security investments, creating remediation plans, or validating control effectiveness. |
| `threat-modeling-expert` | Expert in threat modeling methodologies, security architecture review, and risk assessment. Masters STRIDE, PASTA, attack trees, and security requirement extraction. Use PROACTIVELY for security architecture reviews,... |
| `top-web-vulnerabilities` | Provide a comprehensive, structured reference for the 100 most critical web application vulnerabilities organized by category. This skill enables systematic vulnerability identification, impact assessment, and remedia... |
| `variant-analysis` | Find similar vulnerabilities and bugs across codebases using pattern-based analysis. Use when hunting bug variants, building CodeQL/Semgrep queries, analyzing security vulnerabilities, or performing systematic code au... |
| `varlock` | Secure-by-default environment variable management for Claude Code sessions. |
| `varlock-claude-skill` | Secure environment variable management ensuring secrets are never exposed in Claude sessions, terminals, logs, or git commits |
| `vibers-code-review` | Human review workflow for AI-generated GitHub projects with spec-based feedback, security review, and follow-up PRs from the Vibers service. |
| `vulnerability-scanner` | Advanced vulnerability analysis principles. OWASP 2025, Supply Chain Security, attack surface mapping, risk prioritization. |
| `web-security-testing` | Web application security testing workflow for OWASP Top 10 vulnerabilities including injection, XSS, authentication flaws, and access control issues. |
| `web3-testing` | Master comprehensive testing strategies for smart contracts using Hardhat, Foundry, and advanced testing patterns. |
| `windows-privilege-escalation` | Provide systematic methodologies for discovering and exploiting privilege escalation vulnerabilities on Windows systems during penetration testing engagements. |
| `wireshark-analysis` | Execute comprehensive network traffic analysis using Wireshark to capture, filter, and examine network packets for security investigations, performance optimization, and troubleshooting. |
| `wordpress-penetration-testing` | Conduct comprehensive security assessments of WordPress installations including enumeration of users, themes, and plugins, vulnerability scanning, credential attacks, and exploitation techniques. WordPress powers appr... |
| `xss-html-injection` | Execute comprehensive client-side injection vulnerability assessments on web applications to identify XSS and HTML injection flaws, demonstrate exploitation techniques for session hijacking and credential theft, and v... |
| `zeroize-audit` | Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. Use for auditing C/C++/Rust code... |

### `cloud-devops` (69)

Kubernetes, Terraform, CI/CD, observability, and incident response.

| Skill | What it does |
|---|---|
| `appdeploy` | Deploy web apps with backend APIs, database, and file storage. Use when the user asks to deploy or publish a website or web app and wants a public URL. Uses HTTP API via curl. |
| `aws-cost-cleanup` | Automated cleanup of unused AWS resources to reduce costs |
| `aws-cost-optimizer` | Comprehensive AWS cost analysis and optimization recommendations using AWS CLI and Cost Explorer |
| `aws-serverless` | Proper Lambda function structure with error handling |
| `aws-skills` | AWS development with infrastructure automation and cloud architecture patterns |
| `azd-deployment` | Deploy containerized frontend + backend applications to Azure Container Apps with remote builds, managed identity, and idempotent infrastructure. |
| `bazel-build-optimization` | Optimize Bazel builds for large-scale monorepos. Use when configuring Bazel, implementing remote execution, or optimizing build performance for enterprise codebases. |
| `bitbucket-automation` | Automate Bitbucket repositories, pull requests, branches, issues, and workspace management via Rube MCP (Composio). Always search tools first for current schemas. |
| `cdk-patterns` | Common AWS CDK patterns and constructs for building cloud infrastructure with TypeScript, Python, or Java. Use when designing reusable CDK stacks and L3 constructs. |
| `cicd-automation-workflow-automate` | You are a workflow automation expert specializing in creating efficient CI/CD pipelines, GitHub Actions workflows, and automated development processes. Design and implement automation that reduces manual work, improve... |
| `circleci-automation` | Automate CircleCI tasks via Rube MCP (Composio): trigger pipelines, monitor workflows/jobs, retrieve artifacts and test metadata. Always search tools first for current schemas. |
| `cloud-architect` | Expert cloud architect specializing in AWS/Azure/GCP multi-cloud infrastructure design, advanced IaC (Terraform/OpenTofu/CDK), FinOps cost optimization, and modern architectural patterns. |
| `cloud-devops` | Cloud infrastructure and DevOps workflow covering AWS, Azure, GCP, Kubernetes, Terraform, CI/CD, monitoring, and cloud-native development. |
| `cloudformation-best-practices` | CloudFormation template optimization, nested stacks, drift detection, and production-ready patterns. Use when writing or reviewing CF templates. |
| `cost-optimization` | Strategies and patterns for optimizing cloud costs across AWS, Azure, and GCP. |
| `deployment-engineer` | Expert deployment engineer specializing in modern CI/CD pipelines, GitOps workflows, and advanced deployment automation. |
| `deployment-pipeline-design` | Design multi-stage CI/CD pipelines with approval gates, security checks, and deployment orchestration. Use when architecting deployment workflows, setting up continuous delivery, or implementing GitOps practices. |
| `deployment-procedures` | Production deployment principles and decision-making. Safe deployment workflows, rollback strategies, and verification. Teaches thinking, not scripts. |
| `deployment-validation-config-validate` | You are a configuration management expert specializing in validating, testing, and ensuring the correctness of application configurations. Create comprehensive validation schemas, implement configurat |
| `devcontainer-setup` | Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up isolated development environments, or conf... |
| `devops-deploy` | DevOps e deploy de aplicacoes — Docker, CI/CD com GitHub Actions, AWS Lambda, SAM, Terraform, infraestrutura como codigo e monitoramento. |
| `devops-engineer` | Creates Dockerfiles, configures CI/CD pipelines, writes Kubernetes manifests, and generates Terraform/Pulumi infrastructure templates. Handles deployment automation, GitOps configuration, incident response runbooks, a... |
| `devops-troubleshooter` | Expert DevOps troubleshooter specializing in rapid incident response, advanced debugging, and modern observability. |
| `distributed-tracing` | Implement distributed tracing with Jaeger and Tempo for request flow visibility across microservices. |
| `docker-expert` | You are an advanced Docker containerization expert with comprehensive, practical knowledge of container optimization, security hardening, multi-stage builds, orchestration patterns, and production deployment strategie... |
| `gcp-cloud-run` | When to use: ['Web applications and APIs', 'Need any runtime or library', 'Complex services with multiple endpoints', 'Stateless containerized workloads'] |
| `github-actions-templates` | Production-ready GitHub Actions workflow patterns for testing, building, and deploying applications. |
| `github-workflow-automation` | Patterns for automating GitHub workflows with AI assistance, inspired by [Gemini CLI](https://github.com/google-gemini/gemini-cli) and modern DevOps practices. |
| `gitlab-automation` | Automate GitLab project management, issues, merge requests, pipelines, branches, and user operations via Rube MCP (Composio). Always search tools first for current schemas. |
| `gitlab-ci-patterns` | Comprehensive GitLab CI/CD pipeline patterns for automated testing, building, and deployment. |
| `gitops-workflow` | Complete guide to implementing GitOps workflows with ArgoCD and Flux for automated Kubernetes deployments. |
| `grafana-dashboards` | Create and manage production-ready Grafana dashboards for comprehensive system observability. |
| `helm-chart-scaffolding` | Comprehensive guidance for creating, organizing, and managing Helm charts for packaging and deploying Kubernetes applications. |
| `hybrid-cloud-architect` | Expert hybrid cloud architect specializing in complex multi-cloud solutions across AWS/Azure/GCP and private clouds (OpenStack/VMware). |
| `hybrid-cloud-networking` | Configure secure, high-performance connectivity between on-premises and cloud environments using VPN, Direct Connect, and ExpressRoute. |
| `incident-responder` | Expert SRE incident responder specializing in rapid problem resolution, modern observability, and comprehensive incident management. |
| `incident-response-incident-response` | Use when working with incident response incident response |
| `incident-response-smart-fix` | [Extended thinking: This workflow implements a sophisticated debugging and resolution pipeline that leverages AI-assisted debugging tools and observability platforms to systematically diagnose and res |
| `incident-runbook-templates` | Production-ready templates for incident response runbooks covering detection, triage, mitigation, resolution, and communication. |
| `istio-traffic-management` | Comprehensive guide to Istio traffic management for production service mesh deployments. |
| `k8s-manifest-generator` | Step-by-step guidance for creating production-ready Kubernetes manifests including Deployments, Services, ConfigMaps, Secrets, and PersistentVolumeClaims. |
| `k8s-security-policies` | Comprehensive guide for implementing NetworkPolicy, PodSecurityPolicy, RBAC, and Pod Security Standards in Kubernetes. |
| `kubernetes-architect` | Expert Kubernetes architect specializing in cloud-native infrastructure, advanced GitOps workflows (ArgoCD/Flux), and enterprise container orchestration. |
| `kubernetes-deployment` | Kubernetes deployment workflow for container orchestration, Helm charts, service mesh, and production-ready K8s configurations. |
| `linkerd-patterns` | Production patterns for Linkerd service mesh - the lightweight, security-first service mesh for Kubernetes. |
| `linux-shell-scripting` | Provide production-ready shell script templates for common Linux system administration tasks including backups, monitoring, user management, log analysis, and automation. These scripts serve as building blocks for sec... |
| `linux-troubleshooting` | Linux system troubleshooting workflow for diagnosing and resolving system issues, performance problems, and service failures. |
| `monorepo-architect` | Expert in monorepo architecture, build systems, and dependency management at scale. Masters Nx, Turborepo, Bazel, and Lerna for efficient multi-project development. Use PROACTIVELY for monorepo setup, |
| `monorepo-management` | Build efficient, scalable monorepos that enable code sharing, consistent tooling, and atomic changes across multiple packages and applications. |
| `multi-cloud-architecture` | Decision framework and patterns for architecting applications across AWS, Azure, and GCP. |
| `network-101` | Configure and test common network services (HTTP, HTTPS, SNMP, SMB) for penetration testing lab environments. Enable hands-on practice with service enumeration, log analysis, and security testing against properly conf... |
| `network-engineer` | Expert network engineer specializing in modern cloud networking, security architectures, and performance optimization. |
| `nx-workspace-patterns` | Configure and optimize Nx monorepo workspaces. Use when setting up Nx, configuring project boundaries, optimizing build caching, or implementing affected commands. |
| `observability-engineer` | Build production-ready monitoring, logging, and tracing systems. Implements comprehensive observability strategies, SLI/SLO management, and incident response workflows. |
| `observability-monitoring-monitor-setup` | You are a monitoring and observability expert specializing in implementing comprehensive monitoring solutions. Set up metrics collection, distributed tracing, log aggregation, and create insightful da |
| `observability-monitoring-slo-implement` | You are an SLO (Service Level Objective) expert specializing in implementing reliability standards and error budget-based engineering practices. Design comprehensive SLO frameworks, establish meaningful SLIs, and crea... |
| `on-call-handoff-patterns` | Effective patterns for on-call shift transitions, ensuring continuity, context transfer, and reliable incident response across shifts. |
| `postmortem-writing` | Comprehensive guide to writing effective, blameless postmortems that drive organizational learning and prevent incident recurrence. |
| `prometheus-configuration` | Complete guide to Prometheus setup, metric collection, scrape configuration, and recording rules. |
| `render-automation` | Automate Render tasks via Rube MCP (Composio): services, deployments, projects. Always search tools first for current schemas. |
| `service-mesh-expert` | Expert service mesh architect specializing in Istio, Linkerd, and cloud-native networking patterns. Masters traffic management, security policies, observability integration, and multi-cluster mesh con |
| `service-mesh-observability` | Complete guide to observability patterns for Istio, Linkerd, and service mesh deployments. |
| `slo-implementation` | Framework for defining and implementing Service Level Indicators (SLIs), Service Level Objectives (SLOs), and error budgets. |
| `terraform-aws-modules` | Terraform module creation for AWS — reusable modules, state management, and HCL best practices. Use when building or reviewing Terraform AWS infrastructure. |
| `terraform-infrastructure` | Terraform infrastructure as code workflow for provisioning cloud resources, creating reusable modules, and managing infrastructure at scale. |
| `terraform-module-library` | Production-ready Terraform module patterns for AWS, Azure, and GCP infrastructure. |
| `terraform-skill` | Terraform infrastructure as code best practices |
| `terraform-specialist` | Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns. |
| `turborepo-caching` | Configure Turborepo for efficient monorepo builds with local and remote caching. Use when setting up Turborepo, optimizing build pipelines, or implementing distributed caching. |

### `azure` (120)

Per-service Azure SDK skills across Python, TypeScript, .NET, Java, and Rust.

| Skill | What it does |
|---|---|
| `azure-ai-agents-persistent-dotnet` | Azure AI Agents Persistent SDK for .NET. Low-level SDK for creating and managing AI agents with threads, messages, runs, and tools. |
| `azure-ai-agents-persistent-java` | Azure AI Agents Persistent SDK for Java. Low-level SDK for creating and managing AI agents with threads, messages, runs, and tools. |
| `azure-ai-anomalydetector-java` | Build anomaly detection applications with Azure AI Anomaly Detector SDK for Java. Use when implementing univariate/multivariate anomaly detection, time-series analysis, or AI-powered monitoring. |
| `azure-ai-contentsafety-java` | Build content moderation applications using the Azure AI Content Safety SDK for Java. |
| `azure-ai-contentsafety-py` | Azure AI Content Safety SDK for Python. Use for detecting harmful content in text and images with multi-severity classification. |
| `azure-ai-contentsafety-ts` | Analyze text and images for harmful content with customizable blocklists. |
| `azure-ai-contentunderstanding-py` | Azure AI Content Understanding SDK for Python. Use for multimodal content extraction from documents, images, audio, and video. |
| `azure-ai-document-intelligence-dotnet` | Azure AI Document Intelligence SDK for .NET. Extract text, tables, and structured data from documents using prebuilt and custom models. |
| `azure-ai-document-intelligence-ts` | Extract text, tables, and structured data from documents using prebuilt and custom models. |
| `azure-ai-formrecognizer-java` | Build document analysis applications using the Azure AI Document Intelligence SDK for Java. |
| `azure-ai-ml-py` | Azure Machine Learning SDK v2 for Python. Use for ML workspaces, jobs, models, datasets, compute, and pipelines. |
| `azure-ai-openai-dotnet` | Azure OpenAI SDK for .NET. Client library for Azure OpenAI and OpenAI services. Use for chat completions, embeddings, image generation, audio transcription, and assistants. |
| `azure-ai-projects-dotnet` | Azure AI Projects SDK for .NET. High-level client for Azure AI Foundry projects including agents, connections, datasets, deployments, evaluations, and indexes. |
| `azure-ai-projects-java` | Azure AI Projects SDK for Java. High-level SDK for Azure AI Foundry project management including connections, datasets, indexes, and evaluations. |
| `azure-ai-projects-py` | Build AI applications on Microsoft Foundry using the azure-ai-projects SDK. |
| `azure-ai-projects-ts` | High-level SDK for Azure AI Foundry projects with agents, connections, deployments, and evaluations. |
| `azure-ai-textanalytics-py` | Azure AI Text Analytics SDK for sentiment analysis, entity recognition, key phrases, language detection, PII, and healthcare NLP. Use for natural language processing on text. |
| `azure-ai-transcription-py` | Azure AI Transcription SDK for Python. Use for real-time and batch speech-to-text transcription with timestamps and diarization. |
| `azure-ai-translation-document-py` | Azure AI Document Translation SDK for batch translation of documents with format preservation. Use for translating Word, PDF, Excel, PowerPoint, and other document formats at scale. |
| `azure-ai-translation-text-py` | Azure AI Text Translation SDK for real-time text translation, transliteration, language detection, and dictionary lookup. Use for translating text content in applications. |
| `azure-ai-translation-ts` | Text and document translation with REST-style clients. |
| `azure-ai-vision-imageanalysis-java` | Build image analysis applications with Azure AI Vision SDK for Java. Use when implementing image captioning, OCR text extraction, object detection, tagging, or smart cropping. |
| `azure-ai-vision-imageanalysis-py` | Azure AI Vision Image Analysis SDK for captions, tags, objects, OCR, people detection, and smart cropping. Use for computer vision and image understanding tasks. |
| `azure-ai-voicelive-dotnet` | Azure AI Voice Live SDK for .NET. Build real-time voice AI applications with bidirectional WebSocket communication. |
| `azure-ai-voicelive-java` | Azure AI VoiceLive SDK for Java. Real-time bidirectional voice conversations with AI assistants using WebSocket. |
| `azure-ai-voicelive-py` | Build real-time voice AI applications with bidirectional WebSocket communication. |
| `azure-ai-voicelive-ts` | Azure AI Voice Live SDK for JavaScript/TypeScript. Build real-time voice AI applications with bidirectional WebSocket communication. |
| `azure-appconfiguration-java` | Azure App Configuration SDK for Java. Centralized application configuration management with key-value settings, feature flags, and snapshots. |
| `azure-appconfiguration-py` | Azure App Configuration SDK for Python. Use for centralized configuration management, feature flags, and dynamic settings. |
| `azure-appconfiguration-ts` | Centralized configuration management with feature flags and dynamic refresh. |
| `azure-communication-callautomation-java` | Build server-side call automation workflows including IVR systems, call routing, recording, and AI-powered interactions. |
| `azure-communication-callingserver-java` | ⚠️ DEPRECATED: This SDK has been renamed to Call Automation. For new projects, use azure-communication-callautomation instead. This skill is for maintaining legacy code only. |
| `azure-communication-chat-java` | Build real-time chat applications with thread management, messaging, participants, and read receipts. |
| `azure-communication-common-java` | Azure Communication Services common utilities for Java. Use when working with CommunicationTokenCredential, user identifiers, token refresh, or shared authentication across ACS services. |
| `azure-communication-sms-java` | Send SMS messages with Azure Communication Services SMS Java SDK. Use when implementing SMS notifications, alerts, OTP delivery, bulk messaging, or delivery reports. |
| `azure-compute-batch-java` | Azure Batch SDK for Java. Run large-scale parallel and HPC batch jobs with pools, jobs, tasks, and compute nodes. |
| `azure-containerregistry-py` | Azure Container Registry SDK for Python. Use for managing container images, artifacts, and repositories. |
| `azure-cosmos-db-py` | Build production-grade Azure Cosmos DB NoSQL services following clean code, security best practices, and TDD principles. |
| `azure-cosmos-java` | Azure Cosmos DB SDK for Java. NoSQL database operations with global distribution, multi-model support, and reactive patterns. |
| `azure-cosmos-py` | Azure Cosmos DB SDK for Python (NoSQL API). Use for document CRUD, queries, containers, and globally distributed data. |
| `azure-cosmos-rust` | Azure Cosmos DB SDK for Rust (NoSQL API). Use for document CRUD, queries, containers, and globally distributed data. |
| `azure-cosmos-ts` | Azure Cosmos DB JavaScript/TypeScript SDK (@azure/cosmos) for data plane operations. Use for CRUD operations on documents, queries, bulk operations, and container management. |
| `azure-data-tables-java` | Build table storage applications using the Azure Tables SDK for Java. Works with both Azure Table Storage and Cosmos DB Table API. |
| `azure-data-tables-py` | Azure Tables SDK for Python (Storage and Cosmos DB). Use for NoSQL key-value storage, entity CRUD, and batch operations. |
| `azure-eventgrid-dotnet` | Azure Event Grid SDK for .NET. Client library for publishing and consuming events with Azure Event Grid. Use for event-driven architectures, pub/sub messaging, CloudEvents, and EventGridEvents. |
| `azure-eventgrid-java` | Build event-driven applications with Azure Event Grid SDK for Java. Use when publishing events, implementing pub/sub patterns, or integrating with Azure services via events. |
| `azure-eventgrid-py` | Azure Event Grid SDK for Python. Use for publishing events, handling CloudEvents, and event-driven architectures. |
| `azure-eventhub-dotnet` | Azure Event Hubs SDK for .NET. |
| `azure-eventhub-java` | Build real-time streaming applications with Azure Event Hubs SDK for Java. Use when implementing event streaming, high-throughput data ingestion, or building event-driven architectures. |
| `azure-eventhub-py` | Azure Event Hubs SDK for Python streaming. Use for high-throughput event ingestion, producers, consumers, and checkpointing. |
| `azure-eventhub-rust` | Azure Event Hubs SDK for Rust. Use for sending and receiving events, streaming data ingestion. |
| `azure-eventhub-ts` | High-throughput event streaming and real-time data ingestion. |
| `azure-functions` | Modern .NET execution model with process isolation |
| `azure-identity-dotnet` | Azure Identity SDK for .NET. Authentication library for Azure SDK clients using Microsoft Entra ID. Use for DefaultAzureCredential, managed identity, service principals, and developer credentials. |
| `azure-identity-java` | Authenticate Java applications with Azure services using Microsoft Entra ID (Azure AD). |
| `azure-identity-py` | Azure Identity SDK for Python authentication. Use for DefaultAzureCredential, managed identity, service principals, and token caching. |
| `azure-identity-rust` | Azure Identity SDK for Rust authentication. Use for DeveloperToolsCredential, ManagedIdentityCredential, ClientSecretCredential, and token-based authentication. |
| `azure-identity-ts` | Authenticate to Azure services with various credential types. |
| `azure-keyvault-certificates-rust` | Azure Key Vault Certificates SDK for Rust. Use for creating, importing, and managing certificates. |
| `azure-keyvault-keys-rust` | Azure Key Vault Keys SDK for Rust. Use for creating, managing, and using cryptographic keys. Triggers: "keyvault keys rust", "KeyClient rust", "create key rust", "encrypt rust", "sign rust". |
| `azure-keyvault-keys-ts` | Manage cryptographic keys using Azure Key Vault Keys SDK for JavaScript (@azure/keyvault-keys). Use when creating, encrypting/decrypting, signing, or rotating keys. |
| `azure-keyvault-py` | Azure Key Vault SDK for Python. Use for secrets, keys, and certificates management with secure storage. |
| `azure-keyvault-secrets-rust` | Azure Key Vault Secrets SDK for Rust. Use for storing and retrieving secrets, passwords, and API keys. Triggers: "keyvault secrets rust", "SecretClient rust", "get secret rust", "set secret rust". |
| `azure-keyvault-secrets-ts` | Manage secrets using Azure Key Vault Secrets SDK for JavaScript (@azure/keyvault-secrets). Use when storing and retrieving application secrets or configuration values. |
| `azure-maps-search-dotnet` | Azure Maps SDK for .NET. Location-based services including geocoding, routing, rendering, geolocation, and weather. Use for address search, directions, map tiles, IP geolocation, and weather data. |
| `azure-messaging-webpubsub-java` | Build real-time web applications with Azure Web PubSub SDK for Java. Use when implementing WebSocket-based messaging, live updates, chat applications, or server-to-client push notifications. |
| `azure-messaging-webpubsubservice-py` | Azure Web PubSub Service SDK for Python. Use for real-time messaging, WebSocket connections, and pub/sub patterns. |
| `azure-mgmt-apicenter-dotnet` | Azure API Center SDK for .NET. Centralized API inventory management with governance, versioning, and discovery. |
| `azure-mgmt-apicenter-py` | Azure API Center Management SDK for Python. Use for managing API inventory, metadata, and governance across your organization. |
| `azure-mgmt-apimanagement-dotnet` | Azure Resource Manager SDK for API Management in .NET. |
| `azure-mgmt-apimanagement-py` | Azure API Management SDK for Python. Use for managing APIM services, APIs, products, subscriptions, and policies. |
| `azure-mgmt-applicationinsights-dotnet` | Azure Application Insights SDK for .NET. Application performance monitoring and observability resource management. |
| `azure-mgmt-arizeaiobservabilityeval-dotnet` | Azure Resource Manager SDK for Arize AI Observability and Evaluation (.NET). |
| `azure-mgmt-botservice-dotnet` | Azure Resource Manager SDK for Bot Service in .NET. Management plane operations for creating and managing Azure Bot resources, channels (Teams, DirectLine, Slack), and connection settings. |
| `azure-mgmt-botservice-py` | Azure Bot Service Management SDK for Python. Use for creating, managing, and configuring Azure Bot Service resources. |
| `azure-mgmt-fabric-dotnet` | Azure Resource Manager SDK for Fabric in .NET. |
| `azure-mgmt-fabric-py` | Azure Fabric Management SDK for Python. Use for managing Microsoft Fabric capacities and resources. |
| `azure-mgmt-mongodbatlas-dotnet` | Manage MongoDB Atlas Organizations as Azure ARM resources with unified billing through Azure Marketplace. |
| `azure-mgmt-weightsandbiases-dotnet` | Azure Weights & Biases SDK for .NET. ML experiment tracking and model management via Azure Marketplace. Use for creating W&B instances, managing SSO, marketplace integration, and ML observability. |
| `azure-microsoft-playwright-testing-ts` | Run Playwright tests at scale with cloud-hosted browsers and integrated Azure portal reporting. |
| `azure-monitor-ingestion-java` | Azure Monitor Ingestion SDK for Java. Send custom logs to Azure Monitor via Data Collection Rules (DCR) and Data Collection Endpoints (DCE). |
| `azure-monitor-ingestion-py` | Azure Monitor Ingestion SDK for Python. Use for sending custom logs to Log Analytics workspace via Logs Ingestion API. |
| `azure-monitor-opentelemetry-exporter-java` | Azure Monitor OpenTelemetry Exporter for Java. Export OpenTelemetry traces, metrics, and logs to Azure Monitor/Application Insights. |
| `azure-monitor-opentelemetry-exporter-py` | Azure Monitor OpenTelemetry Exporter for Python. Use for low-level OpenTelemetry export to Application Insights. |
| `azure-monitor-opentelemetry-py` | Azure Monitor OpenTelemetry Distro for Python. Use for one-line Application Insights setup with auto-instrumentation. |
| `azure-monitor-opentelemetry-ts` | Auto-instrument Node.js applications with distributed tracing, metrics, and logs. |
| `azure-monitor-query-java` | Azure Monitor Query SDK for Java. Execute Kusto queries against Log Analytics workspaces and query metrics from Azure resources. |
| `azure-monitor-query-py` | Azure Monitor Query SDK for Python. Use for querying Log Analytics workspaces and Azure Monitor metrics. |
| `azure-postgres-ts` | Connect to Azure Database for PostgreSQL Flexible Server from Node.js/TypeScript using the pg (node-postgres) package. |
| `azure-resource-manager-cosmosdb-dotnet` | Azure Resource Manager SDK for Cosmos DB in .NET. |
| `azure-resource-manager-durabletask-dotnet` | Azure Resource Manager SDK for Durable Task Scheduler in .NET. |
| `azure-resource-manager-mysql-dotnet` | Azure MySQL Flexible Server SDK for .NET. Database management for MySQL Flexible Server deployments. |
| `azure-resource-manager-playwright-dotnet` | Azure Resource Manager SDK for Microsoft Playwright Testing in .NET. |
| `azure-resource-manager-postgresql-dotnet` | Azure PostgreSQL Flexible Server SDK for .NET. Database management for PostgreSQL Flexible Server deployments. |
| `azure-resource-manager-redis-dotnet` | Azure Resource Manager SDK for Redis in .NET. |
| `azure-resource-manager-sql-dotnet` | Azure Resource Manager SDK for Azure SQL in .NET. |
| `azure-search-documents-dotnet` | Azure AI Search SDK for .NET (Azure.Search.Documents). Use for building search applications with full-text, vector, semantic, and hybrid search. |
| `azure-search-documents-py` | Azure AI Search SDK for Python. Use for vector search, hybrid search, semantic ranking, indexing, and skillsets. |
| `azure-search-documents-ts` | Build search applications with vector, hybrid, and semantic search capabilities. |
| `azure-security-keyvault-keys-dotnet` | Azure Key Vault Keys SDK for .NET. Client library for managing cryptographic keys in Azure Key Vault and Managed HSM. Use for key creation, rotation, encryption, decryption, signing, and verification. |
| `azure-security-keyvault-keys-java` | Azure Key Vault Keys Java SDK for cryptographic key management. Use when creating, managing, or using RSA/EC keys, performing encrypt/decrypt/sign/verify operations, or working with HSM-backed keys. |
| `azure-security-keyvault-secrets-java` | Azure Key Vault Secrets Java SDK for secret management. Use when storing, retrieving, or managing passwords, API keys, connection strings, or other sensitive configuration data. |
| `azure-servicebus-dotnet` | Azure Service Bus SDK for .NET. Enterprise messaging with queues, topics, subscriptions, and sessions. |
| `azure-servicebus-py` | Azure Service Bus SDK for Python messaging. Use for queues, topics, subscriptions, and enterprise messaging patterns. |
| `azure-servicebus-ts` | Enterprise messaging with queues, topics, and subscriptions. |
| `azure-speech-to-text-rest-py` | Azure Speech to Text REST API for short audio (Python). Use for simple speech recognition of audio files up to 60 seconds without the Speech SDK. |
| `azure-storage-blob-java` | Build blob storage applications using the Azure Storage Blob SDK for Java. |
| `azure-storage-blob-py` | Azure Blob Storage SDK for Python. Use for uploading, downloading, listing blobs, managing containers, and blob lifecycle. |
| `azure-storage-blob-rust` | Azure Blob Storage SDK for Rust. Use for uploading, downloading, and managing blobs and containers. |
| `azure-storage-blob-ts` | Azure Blob Storage JavaScript/TypeScript SDK (@azure/storage-blob) for blob operations. Use for uploading, downloading, listing, and managing blobs and containers. |
| `azure-storage-file-datalake-py` | Azure Data Lake Storage Gen2 SDK for Python. Use for hierarchical file systems, big data analytics, and file/directory operations. |
| `azure-storage-file-share-py` | Azure Storage File Share SDK for Python. Use for SMB file shares, directories, and file operations in the cloud. |
| `azure-storage-file-share-ts` | Azure File Share JavaScript/TypeScript SDK (@azure/storage-file-share) for SMB file share operations. |
| `azure-storage-queue-py` | Azure Queue Storage SDK for Python. Use for reliable message queuing, task distribution, and asynchronous processing. |
| `azure-storage-queue-ts` | Azure Queue Storage JavaScript/TypeScript SDK (@azure/storage-queue) for message queue operations. Use for sending, receiving, peeking, and deleting messages in queues. |
| `azure-web-pubsub-ts` | Real-time messaging with WebSocket connections and pub/sub patterns. |
| `m365-agents-dotnet` | Microsoft 365 Agents SDK for .NET. Build multichannel agents for Teams/M365/Copilot Studio with ASP.NET Core hosting, AgentApplication routing, and MSAL-based auth. |
| `m365-agents-py` | Microsoft 365 Agents SDK for Python. Build multichannel agents for Teams/M365/Copilot Studio with aiohttp hosting, AgentApplication routing, streaming responses, and MSAL-based auth. |
| `m365-agents-ts` | Microsoft 365 Agents SDK for TypeScript/Node.js. |
| `microsoft-azure-webjobs-extensions-authentication-events-dotnet` | Microsoft Entra Authentication Events SDK for .NET. Azure Functions triggers for custom authentication extensions. |

### `ai-ml` (100)

Agents, RAG, prompts, evals, and LLM application workflows.

| Skill | What it does |
|---|---|
| `00-andruia-consultant` | Arquitecto de Soluciones Principal y Consultor Tecnológico de Andru.ia. Diagnostica y traza la hoja de ruta óptima para proyectos de IA en español. |
| `10-andruia-skill-smith` | Ingeniero de Sistemas de Andru.ia. Diseña, redacta y despliega nuevas habilidades (skills) dentro del repositorio siguiendo el Estándar de Diamante. |
| `20-andruia-niche-intelligence` | Estratega de Inteligencia de Dominio de Andru.ia. Analiza el nicho específico de un proyecto para inyectar conocimientos, regulaciones y estándares únicos del sector. Actívalo tras definir el nicho. |
| `advanced-evaluation` | This skill should be used when the user asks to "implement LLM-as-judge", "compare model outputs", "create evaluation rubrics", "mitigate evaluation bias", or mentions direct scoring, pairwise comparison, position bia... |
| `agent-development-guide` | This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors", "autonomous agent... |
| `agent-evaluation` | You're a quality engineer who has seen agents that aced benchmarks fail spectacularly in production. You've learned that evaluating LLM agents is fundamentally different from testing traditional software—the same inpu... |
| `agent-framework-azure-ai-py` | Build persistent agents on Azure AI Foundry using the Microsoft Agent Framework Python SDK. |
| `agent-manager-skill` | Manage multiple local CLI agents via tmux sessions (start/stop/monitor/assign) with cron-friendly scheduling. |
| `agent-orchestration-improve-agent` | Systematic improvement of existing agents through performance analysis, prompt engineering, and continuous iteration. |
| `agent-orchestration-multi-agent-optimize` | Optimize multi-agent systems with coordinated profiling, workload distribution, and cost-aware orchestration. Use when improving agent performance, throughput, or reliability. |
| `agent-orchestrator` | Meta-skill que orquestra todos os agentes do ecossistema. Scan automatico de skills, match por capacidades, coordenacao de workflows multi-skill e registry management. |
| `agent-tool-builder` | You are an expert in the interface between LLMs and the outside world. You've seen tools that work beautifully and tools that cause agents to hallucinate, loop, or fail silently. The difference is almost always in the... |
| `agentfolio` | Skill for discovering and researching autonomous AI agents, tools, and ecosystems using the AgentFolio directory. |
| `agents-md` | This skill should be used when the user asks to "create AGENTS.md", "update AGENTS.md", "maintain agent docs", "set up CLAUDE.md", or needs to keep agent instructions concise. Enforces research-backed best practices f... |
| `agents-v2-py` | Build container-based Foundry Agents with Azure AI Projects SDK (ImageBasedHostedAgentDefinition). Use when creating hosted agents with custom container images in Azure AI Foundry. |
| `ai-agent-development` | AI agent development workflow for building autonomous agents, multi-agent systems, and agent orchestration with CrewAI, LangGraph, and custom agents. |
| `ai-agents-architect` | I build AI systems that can act autonomously while remaining controllable. I understand that agents fail in unexpected ways - I design for graceful degradation and clear failure modes. I balance autonomy with oversigh... |
| `ai-analyzer` | AI驱动的综合健康分析系统，整合多维度健康数据、识别异常模式、预测健康风险、提供个性化建议。支持智能问答和AI健康报告生成。 |
| `ai-engineer` | Build production-ready LLM applications, advanced RAG systems, and intelligent agents. Implements vector search, multimodal AI, agent orchestration, and enterprise AI integrations. |
| `ai-engineering-toolkit` | 6 production-ready AI engineering workflows: prompt evaluation (8-dimension scoring), context budget planning, RAG pipeline design, agent security audit (65-point checklist), eval harness building, and product sense c... |
| `ai-md` | Convert human-written CLAUDE.md into AI-native structured-label format. Battle-tested across 4 models. Same rules, fewer tokens, higher compliance. |
| `ai-ml` | AI and machine learning workflow covering LLM application development, RAG implementation, agent architecture, ML pipelines, and AI-powered features. |
| `ai-native-cli` | Design spec with 98 rules for building CLI tools that AI agents can safely use. Covers structured JSON output, error handling, input contracts, safety guardrails, exit codes, and agent self-description. |
| `ai-product` | You are an AI product engineer who has shipped LLM features to millions of users. You've debugged hallucinations at 3am, optimized prompts to reduce costs by 80%, and built safety systems that caught thousands of harm... |
| `ai-studio-image` | Geracao de imagens humanizadas via Google AI Studio (Gemini). Fotos realistas estilo influencer ou educacional com iluminacao natural e imperfeicoes sutis. |
| `ai-wrapper-product` | You know AI wrappers get a bad rap, but the good ones solve real problems. You build products where AI is the engine, not the gimmick. You understand prompt engineering is product development. You balance costs with u... |
| `airflow-dag-patterns` | Build production Apache Airflow DAGs with best practices for operators, sensors, testing, and deployment. Use when creating data pipelines, orchestrating workflows, or scheduling batch jobs. |
| `auri-core` | Auri: assistente de voz inteligente (Alexa + Claude claude-opus-4-20250805). Visao do produto, persona Vitoria Neural, stack AWS, modelo Free/Pro/Business/Enterprise, roadmap 4 fases, GTM, north star WAC e analise com... |
| `autonomous-agent-patterns` | Design patterns for building autonomous coding agents, inspired by [Cline](https://github.com/cline/cline) and [OpenAI Codex](https://github.com/openai/codex). |
| `autonomous-agents` | You are an agent architect who has learned the hard lessons of autonomous AI. You've seen the gap between impressive demos and production disasters. You know that a 95% success rate per step means only 60% by step 10. |
| `bdi-mental-states` | This skill should be used when the user asks to "model agent mental states", "implement BDI architecture", "create belief-desire-intention models", "transform RDF to beliefs", "build cognitive agent", or mentions BDI... |
| `clarity-gate` | Pre-ingestion verification for epistemic quality in RAG systems. Ensures documents are properly qualified before entering knowledge bases. Produces CGD (Clarity-Gated Documents) and validates SOT (Source of Truth) files. |
| `computer-use-agents` | The fundamental architecture of computer use agents: observe screen, reason about next action, execute action, repeat. This loop integrates vision models with action execution through an iterative pipeline. |
| `computer-vision-expert` | SOTA Computer Vision Expert (2026). Specialized in YOLO26, Segment Anything 3 (SAM 3), Vision Language Models, and real-time spatial analysis. |
| `copilot-sdk` | Build applications that programmatically interact with GitHub Copilot. The SDK wraps the Copilot CLI via JSON-RPC, providing session management, custom tools, hooks, MCP server integration, and streaming across Node.j... |
| `crewai` | You are an expert in designing collaborative AI agent teams with CrewAI. You think in terms of roles, responsibilities, and delegation. You design clear agent personas with specific expertise, create well-defined task... |
| `daily-news-report` | Scrapes content based on a preset URL list, filters high-quality technical information, and generates daily Markdown reports. |
| `data-analysis` | Perform data analysis tasks including data cleaning, statistical analysis, visualization, and insight generation. Use when the user asks to analyze data, perform statistical analysis, create visualizations, or extract... |
| `data-engineer` | Build scalable data pipelines, modern data warehouses, and real-time streaming architectures. Implements Apache Spark, dbt, Airflow, and cloud-native data platforms. |
| `data-engineering-data-driven-feature` | Build features guided by data insights, A/B testing, and continuous measurement using specialized agents for analysis, implementation, and experimentation. |
| `data-engineering-data-pipeline` | You are a data pipeline architecture expert specializing in scalable, reliable, and cost-effective data pipelines for batch and streaming data processing. |
| `data-quality-frameworks` | Implement data quality validation with Great Expectations, dbt tests, and data contracts. Use when building data quality pipelines, implementing validation rules, or establishing data contracts. |
| `data-scientist` | Expert data scientist for advanced analytics, machine learning, and statistical modeling. Handles complex data analysis, predictive modeling, and business intelligence. |
| `data-storytelling` | Transform raw data into compelling narratives that drive decisions and inspire action. |
| `dbt-transformation-patterns` | Production-ready patterns for dbt (data build tool) including model organization, testing strategies, documentation, and incremental processing. |
| `deep-research` | Conduct comprehensive, multi-source research on any topic using web search, documentation lookup, and critical analysis. This skill should be used when users request thorough investigation, deep research, or comprehen... |
| `dispatching-parallel-agents` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| `evaluation` | Build evaluation frameworks for agent systems |
| `exa-search` | Semantic search, similar content discovery, and structured research using Exa API |
| `firecrawl-scraper` | Deep web scraping, screenshots, PDF parsing, and website crawling using Firecrawl API |
| `gemini-api-dev` | The Gemini API provides access to Google's most advanced AI models. Key capabilities include: |
| `gemini-api-integration` | Use when integrating Google Gemini API into projects. Covers model selection, multimodal inputs, streaming, function calling, and production best practices. |
| `hosted-agents` | Build background agents in sandboxed environments. Use for hosted coding agents, sandboxed VMs, Modal sandboxes, and remote coding environments. |
| `hosted-agents-v2-py` | Build hosted agents using Azure AI Projects SDK with ImageBasedHostedAgentDefinition. Use when creating container-based agents in Azure AI Foundry. |
| `langchain-architecture` | Master the LangChain framework for building sophisticated LLM applications with agents, chains, memory, and tool integration. |
| `langfuse` | You are an expert in LLM observability and evaluation. You think in terms of traces, spans, and metrics. You know that LLM applications need monitoring just like traditional software - but with different dimensions (c... |
| `langgraph` | You are an expert in building production-grade AI agents with LangGraph. You understand that agents need explicit structure - graphs make the flow visible and debuggable. You design state carefully, use reducers appro... |
| `last30days` | Research a topic from the last 30 days on Reddit + X + Web, become an expert, and write copy-paste-ready prompts for the user's target tool. |
| `lex` | Centralized 'Truth Engine' for cross-jurisdictional legal context (US, EU, CA) and contract scaffolding. |
| `llm-app-patterns` | Production-ready patterns for building LLM applications, inspired by [Dify](https://github.com/langgenius/dify) and industry best practices. |
| `llm-application-dev-ai-assistant` | You are an AI assistant development expert specializing in creating intelligent conversational interfaces, chatbots, and AI-powered applications. Design comprehensive AI assistant solutions with natur |
| `llm-application-dev-langchain-agent` | You are an expert LangChain agent developer specializing in production-grade AI systems using LangChain 0.1+ and LangGraph. |
| `llm-application-dev-prompt-optimize` | You are an expert prompt engineer specializing in crafting effective prompts for LLMs through advanced techniques including constitutional AI, chain-of-thought reasoning, and model-specific optimizati |
| `llm-evaluation` | Master comprehensive evaluation strategies for LLM applications, from automated metrics to human evaluation and A/B testing. |
| `llm-ops` | LLM Operations -- RAG, embeddings, vector databases, fine-tuning, prompt engineering avancado, custos de LLM, evals de qualidade e arquiteturas de IA para producao. |
| `llm-prompt-optimizer` | Use when improving prompts for any LLM. Applies proven prompt engineering techniques to boost output quality, reduce hallucinations, and cut token usage. |
| `llm-structured-output` | Get reliable JSON, enums, and typed objects from LLMs using response_format, tool_use, and schema-constrained decoding across OpenAI, Anthropic, and Google APIs. |
| `local-llm-expert` | Master local LLM inference, model selection, VRAM optimization, and local deployment using Ollama, llama.cpp, vLLM, and LM Studio. Expert in quantization formats (GGUF, EXL2) and local AI privacy. |
| `loki-mode` | Version 2.35.0 \| PRD to Production \| Zero Human Intervention > Research-enhanced: OpenAI SDK, DeepMind, Anthropic, AWS Bedrock, Agent SDK, HN Production (2025) |
| `machine-learning-ops-ml-pipeline` | Design and implement a complete ML pipeline for: $ARGUMENTS |
| `ml-engineer` | Build production ML systems with PyTorch 2.x, TensorFlow, and modern ML frameworks. Implements model serving, feature engineering, A/B testing, and monitoring. |
| `ml-pipeline-workflow` | Complete end-to-end MLOps pipeline orchestration from data preparation through model deployment. |
| `mlops-engineer` | Build comprehensive ML pipelines, experiment tracking, and model registries with MLflow, Kubeflow, and modern MLOps tools. |
| `multi-advisor` | Conselho de especialistas — consulta multiplos agentes do ecossistema em paralelo para analise multi-perspectiva de qualquer topico. Ativa personas, especialistas e agentes tecnicos simultaneamente, cada um pela sua o... |
| `multi-agent-brainstorming` | Simulate a structured peer-review process using multiple specialized agents to validate designs, surface hidden assumptions, and identify failure modes before implementation. |
| `multi-agent-patterns` | This skill should be used when the user asks to "design multi-agent system", "implement supervisor pattern", "create swarm architecture", "coordinate multiple agents", or mentions multi-agent patterns, context isolati... |
| `multi-platform-apps-multi-platform` | Build and deploy the same feature consistently across web, mobile, and desktop platforms using API-first architecture and parallel implementation strategies. |
| `parallel-agents` | Multi-agent orchestration patterns. Use when multiple independent tasks can run with different domain expertise or when comprehensive analysis requires multiple perspectives. |
| `pipecat-friday-agent` | Build a low-latency, Iron Man-inspired tactical voice assistant (F.R.I.D.A.Y.) using Pipecat, Gemini, and OpenAI. |
| `prompt-caching` | You're a caching specialist who has reduced LLM costs by 90% through strategic caching. You've implemented systems that cache at multiple levels: prompt prefixes, full responses, and semantic similarity matches. |
| `prompt-engineer` | Transforms user prompts into optimized prompts using frameworks (RTF, RISEN, Chain of Thought, RODES, Chain of Density, RACE, RISE, STAR, SOAP, CLEAR, GROW) |
| `prompt-engineering` | Expert guide on prompt engineering patterns, best practices, and optimization techniques. Use when user wants to improve prompts, learn prompting strategies, or debug agent behavior. |
| `prompt-engineering-patterns` | Master advanced prompt engineering techniques to maximize LLM performance, reliability, and controllability. |
| `prompt-factory` | World-class prompt powerhouse that generates production-ready mega-prompts for any role, industry, and task through intelligent 7-question flow, 69 comprehensive presets across 15 professional domains (technical, busi... |
| `prompt-library` | A comprehensive collection of battle-tested prompts inspired by [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) and community best practices. |
| `pydantic-ai` | Build production-ready AI agents with PydanticAI — type-safe tool use, structured outputs, dependency injection, and multi-model support. |
| `rag-engineer` | I bridge the gap between raw documents and LLM understanding. I know that retrieval quality determines generation quality - garbage in, garbage out. I obsess over chunking boundaries, embedding dimensions, and similar... |
| `rag-implementation` | RAG (Retrieval-Augmented Generation) implementation workflow covering embedding selection, vector database setup, chunking strategies, and retrieval optimization. |
| `search-specialist` | Expert web researcher using advanced search techniques and |
| `spark-optimization` | Optimize Apache Spark jobs with partitioning, caching, shuffle optimization, and memory tuning. Use when improving Spark performance, debugging slow jobs, or scaling data processing pipelines. |
| `task-intelligence` | Protocolo de Inteligência Pré-Tarefa — ativa TODOS os agentes relevantes do ecossistema ANTES de executar qualquer tarefa solicitada pelo usuário. |
| `tavily-web` | Web search, content extraction, crawling, and research capabilities using Tavily API |
| `voice-agents` | You are a voice AI architect who has shipped production voice agents handling millions of calls. You understand the physics of latency - every component adds milliseconds, and the sum determines whether conversations... |
| `voice-ai-development` | You are an expert in building real-time voice applications. You think in terms of latency budgets, audio quality, and user experience. You know that voice apps feel magical when fast and broken when slow. |
| `voice-ai-engine-development` | Build real-time conversational AI voice engines using async worker pipelines, streaming transcription, LLM agents, and TTS synthesis with interrupt handling and multi-provider support |
| `web-scraper` | Web scraping inteligente multi-estrategia. Extrai dados estruturados de paginas web (tabelas, listas, precos). Paginacao, monitoramento e export CSV/JSON. |
| `x-article-publisher-skill` | Publish articles to X/Twitter |
| `x-twitter-scraper` | X (Twitter) data platform skill — tweet search, user lookup, follower extraction, engagement metrics, giveaway draws, monitoring, webhooks, 19 extraction tools, MCP server. |
| `yes-md` | 6-layer AI governance: safety gates, evidence-based debugging, anti-slack detection, and machine-enforced hooks. Makes AI safe, thorough, and honest. |
| `youtube-summarizer` | Extract transcripts from YouTube videos and generate comprehensive, detailed summaries using intelligent analysis frameworks |

### `integrations-automation` (99)

Third-party APIs: Slack, Stripe, Notion, GitHub, and others.

| Skill | What it does |
|---|---|
| `activecampaign-automation` | Automate ActiveCampaign tasks via Rube MCP (Composio): manage contacts, tags, list subscriptions, automation enrollment, and tasks. Always search tools first for current schemas. |
| `agentmail` | Email infrastructure for AI agents. Create accounts, send/receive emails, manage webhooks, and check karma balance via the AgentMail API. |
| `airtable-automation` | Automate Airtable tasks via Rube MCP (Composio): records, bases, tables, fields, views. Always search tools first for current schemas. |
| `amazon-alexa` | Integracao completa com Amazon Alexa para criar skills de voz inteligentes, transformar Alexa em assistente com Claude como cerebro (projeto Auri) e integrar com AWS ecosystem (Lambda, DynamoDB, Polly, Transcribe, Lex... |
| `amplitude-automation` | Automate Amplitude tasks via Rube MCP (Composio): events, user activity, cohorts, user identification. Always search tools first for current schemas. |
| `asana-automation` | Automate Asana tasks via Rube MCP (Composio): tasks, projects, sections, teams, workspaces. Always search tools first for current schemas. |
| `bamboohr-automation` | Automate BambooHR tasks via Rube MCP (Composio): employees, time-off, benefits, dependents, employee updates. Always search tools first for current schemas. |
| `basecamp-automation` | Automate Basecamp project management, to-dos, messages, people, and to-do list organization via Rube MCP (Composio). Always search tools first for current schemas. |
| `box-automation` | Automate Box operations including file upload/download, content search, folder management, collaboration, metadata queries, and sign requests through Composio's Box toolkit. |
| `brevo-automation` | Automate Brevo (formerly Sendinblue) email marketing operations through Composio's Brevo toolkit via Rube MCP. |
| `cal-com-automation` | Automate Cal.com tasks via Rube MCP (Composio): manage bookings, check availability, configure webhooks, and handle teams. Always search tools first for current schemas. |
| `calendly-automation` | Automate Calendly scheduling, event management, invitee tracking, availability checks, and organization administration via Rube MCP (Composio). Always search tools first for current schemas. |
| `canva-automation` | Automate Canva tasks via Rube MCP (Composio): designs, exports, folders, brand templates, autofill. Always search tools first for current schemas. |
| `clickup-automation` | Automate ClickUp project management including tasks, spaces, folders, lists, comments, and team operations via Rube MCP (Composio). Always search tools first for current schemas. |
| `close-automation` | Automate Close CRM tasks via Rube MCP (Composio): create leads, manage calls/SMS, handle tasks, and track notes. Always search tools first for current schemas. |
| `coda-automation` | Automate Coda tasks via Rube MCP (Composio): manage docs, pages, tables, rows, formulas, permissions, and publishing. Always search tools first for current schemas. |
| `confluence-automation` | Automate Confluence page creation, content search, space management, labels, and hierarchy navigation via Rube MCP (Composio). Always search tools first for current schemas. |
| `convertkit-automation` | Automate ConvertKit (Kit) tasks via Rube MCP (Composio): manage subscribers, tags, broadcasts, and broadcast stats. Always search tools first for current schemas. |
| `datadog-automation` | Automate Datadog tasks via Rube MCP (Composio): query metrics, search logs, manage monitors/dashboards, create events and downtimes. Always search tools first for current schemas. |
| `discord-automation` | Automate Discord tasks via Rube MCP (Composio): messages, channels, roles, webhooks, reactions. Always search tools first for current schemas. |
| `discord-bot-architect` | Specialized skill for building production-ready Discord bots. Covers Discord.js (JavaScript) and Pycord (Python), gateway intents, slash commands, interactive components, rate limiting, and sharding. |
| `docusign-automation` | Automate DocuSign tasks via Rube MCP (Composio): templates, envelopes, signatures, document management. Always search tools first for current schemas. |
| `dropbox-automation` | Automate Dropbox file management, sharing, search, uploads, downloads, and folder operations via Rube MCP (Composio). Always search tools first for current schemas. |
| `email-systems` | You are an email systems engineer who has maintained 99.9% deliverability across millions of emails. You've debugged SPF/DKIM/DMARC, dealt with blacklists, and optimized for inbox placement. You know that email is the... |
| `figma-automation` | Automate Figma tasks via Rube MCP (Composio): files, components, design tokens, comments, exports. Always search tools first for current schemas. |
| `freshdesk-automation` | Automate Freshdesk helpdesk operations including tickets, contacts, companies, notes, and replies via Rube MCP (Composio). Always search tools first for current schemas. |
| `freshservice-automation` | Automate Freshservice ITSM tasks via Rube MCP (Composio): create/update tickets, bulk operations, service requests, and outbound emails. Always search tools first for current schemas. |
| `github-automation` | Automate GitHub repositories, issues, pull requests, branches, CI/CD, and permissions via Rube MCP (Composio). Manage code workflows, review PRs, search code, and handle deployments programmatically. |
| `github-issue-creator` | Transform messy input (error logs, voice notes, screenshots) into clean, actionable GitHub issues. |
| `gmail-automation` | Lightweight Gmail integration with standalone OAuth authentication. No MCP server required. |
| `google-analytics-automation` | Automate Google Analytics tasks via Rube MCP (Composio): run reports, list accounts/properties, funnels, pivots, key events. Always search tools first for current schemas. |
| `google-calendar-automation` | Lightweight Google Calendar integration with standalone OAuth authentication. No MCP server required. |
| `google-docs-automation` | Lightweight Google Docs integration with standalone OAuth authentication. No MCP server required. |
| `google-drive-automation` | Lightweight Google Drive integration with standalone OAuth authentication. No MCP server required. Full read/write access. |
| `google-sheets-automation` | Lightweight Google Sheets integration with standalone OAuth authentication. No MCP server required. Full read/write access. |
| `google-slides-automation` | Lightweight Google Slides integration with standalone OAuth authentication. No MCP server required. Full read/write access. |
| `googlesheets-automation` | Automate Google Sheets operations (read, write, format, filter, manage spreadsheets) via Rube MCP (Composio). Read/write data, manage tabs, apply formatting, and search rows programmatically. |
| `helpdesk-automation` | Automate HelpDesk tasks via Rube MCP (Composio): list tickets, manage views, use canned responses, and configure custom fields. Always search tools first for current schemas. |
| `hubspot-automation` | Automate HubSpot CRM operations (contacts, companies, deals, tickets, properties) via Rube MCP using Composio integration. |
| `hubspot-integration` | Authentication for single-account integrations |
| `instagram` | Integracao completa com Instagram via Graph API. Publicacao, analytics, comentarios, DMs, hashtags, agendamento, templates e gestao de contas Business/Creator. |
| `instagram-automation` | Automate Instagram tasks via Rube MCP (Composio): create posts, carousels, manage media, get insights, and publishing limits. Always search tools first for current schemas. |
| `intercom-automation` | Automate Intercom tasks via Rube MCP (Composio): conversations, contacts, companies, segments, admins. Always search tools first for current schemas. |
| `jira-automation` | Automate Jira tasks via Rube MCP (Composio): issues, projects, sprints, boards, comments, users. Always search tools first for current schemas. |
| `klaviyo-automation` | Automate Klaviyo tasks via Rube MCP (Composio): manage email/SMS campaigns, inspect campaign messages, track tags, and monitor send jobs. Always search tools first for current schemas. |
| `linear-automation` | Automate Linear tasks via Rube MCP (Composio): issues, projects, cycles, teams, labels. Always search tools first for current schemas. |
| `linear-claude-skill` | Manage Linear issues, projects, and teams |
| `linkedin-automation` | Automate LinkedIn tasks via Rube MCP (Composio): create posts, manage profile, company info, comments, and image uploads. Always search tools first for current schemas. |
| `linkedin-cli` | Use when automating LinkedIn via CLI: fetch profiles, search people/companies, send messages, manage connections, create posts, and Sales Navigator. |
| `mailchimp-automation` | Automate Mailchimp email marketing including campaigns, audiences, subscribers, segments, and analytics via Rube MCP (Composio). Always search tools first for current schemas. |
| `make-automation` | Automate Make (Integromat) tasks via Rube MCP (Composio): operations, enums, language and timezone lookups. Always search tools first for current schemas. |
| `maxia` | Connect to MAXIA AI-to-AI marketplace on Solana. Discover, buy, sell AI services. Earn USDC. 13 MCP tools, A2A protocol, DeFi yields, sentiment analysis, rug detection. |
| `microsoft-teams-automation` | Automate Microsoft Teams tasks via Rube MCP (Composio): send messages, manage channels, create meetings, handle chats, and search messages. Always search tools first for current schemas. |
| `miro-automation` | Automate Miro tasks via Rube MCP (Composio): boards, items, sticky notes, frames, sharing, connectors. Always search tools first for current schemas. |
| `mixpanel-automation` | Automate Mixpanel tasks via Rube MCP (Composio): events, segmentation, funnels, cohorts, user profiles, JQL queries. Always search tools first for current schemas. |
| `monday-automation` | Automate Monday.com work management including boards, items, columns, groups, subitems, and updates via Rube MCP (Composio). Always search tools first for current schemas. |
| `notion-automation` | Automate Notion tasks via Rube MCP (Composio): pages, databases, blocks, comments, users. Always search tools first for current schemas. |
| `notion-template-business` | You know templates are real businesses that can generate serious income. You've seen creators make six figures selling Notion templates. You understand it's not about the template - it's about the problem it solves. Y... |
| `obsidian-clipper-template-creator` | Guide for creating templates for the Obsidian Web Clipper. Use when you want to create a new clipping template, understand available variables, or format clipped content. |
| `one-drive-automation` | Automate OneDrive file management, search, uploads, downloads, sharing, permissions, and folder operations via Rube MCP (Composio). Always search tools first for current schemas. |
| `outlook-automation` | Automate Outlook tasks via Rube MCP (Composio): emails, calendar, contacts, folders, attachments. Always search tools first for current schemas. |
| `outlook-calendar-automation` | Automate Outlook Calendar tasks via Rube MCP (Composio): create events, manage attendees, find meeting times, and handle invitations. Always search tools first for current schemas. |
| `pagerduty-automation` | Automate PagerDuty tasks via Rube MCP (Composio): manage incidents, services, schedules, escalation policies, and on-call rotations. Always search tools first for current schemas. |
| `pipedrive-automation` | Automate Pipedrive CRM operations including deals, contacts, organizations, activities, notes, and pipeline management via Rube MCP (Composio). Always search tools first for current schemas. |
| `posthog-automation` | Automate PostHog tasks via Rube MCP (Composio): events, feature flags, projects, user profiles, annotations. Always search tools first for current schemas. |
| `postmark-automation` | Automate Postmark email delivery tasks via Rube MCP (Composio): send templated emails, manage templates, monitor delivery stats and bounces. Always search tools first for current schemas. |
| `reddit-automation` | Automate Reddit tasks via Rube MCP (Composio): search subreddits, create posts, manage comments, and browse top content. Always search tools first for current schemas. |
| `salesforce-automation` | Automate Salesforce tasks via Rube MCP (Composio): leads, contacts, accounts, opportunities, SOQL queries. Always search tools first for current schemas. |
| `salesforce-development` | Use @wire decorator for reactive data binding with Lightning Data Service or Apex methods. @wire fits LWC's reactive architecture and enables Salesforce performance optimizations. |
| `segment-automation` | Automate Segment tasks via Rube MCP (Composio): track events, identify users, manage groups, page views, aliases, batch operations. Always search tools first for current schemas. |
| `segment-cdp` | Client-side tracking with Analytics.js. Include track, identify, page, and group calls. Anonymous ID persists until identify merges with user. |
| `sendgrid-automation` | Automate SendGrid email delivery workflows including marketing campaigns (Single Sends), contact and list management, sender identity setup, and email analytics through Composio's SendGrid toolkit. |
| `sentry-automation` | Automate Sentry tasks via Rube MCP (Composio): manage issues/events, configure alerts, track releases, monitor projects and teams. Always search tools first for current schemas. |
| `shopify-apps` | Modern Shopify app template with React Router |
| `shopify-automation` | Automate Shopify tasks via Rube MCP (Composio): products, orders, customers, inventory, collections. Always search tools first for current schemas. |
| `shopify-development` | Build Shopify apps, extensions, themes using GraphQL Admin API, Shopify CLI, Polaris UI, and Liquid. |
| `slack-automation` | Automate Slack workspace operations including messaging, search, channel management, and reaction workflows through Composio's Slack toolkit. |
| `slack-bot-builder` | The Bolt framework is Slack's recommended approach for building apps. It handles authentication, event routing, request verification, and HTTP request processing so you can focus on app logic. |
| `slack-gif-creator` | A toolkit providing utilities and knowledge for creating animated GIFs optimized for Slack. |
| `square-automation` | Automate Square tasks via Rube MCP (Composio): payments, orders, invoices, locations. Always search tools first for current schemas. |
| `telegram` | Integracao completa com Telegram Bot API. Setup com BotFather, mensagens, webhooks, inline keyboards, grupos, canais. Boilerplates Node.js e Python. |
| `telegram-automation` | Automate Telegram tasks via Rube MCP (Composio): send messages, manage chats, share photos/documents, and handle bot commands. Always search tools first for current schemas. |
| `telegram-bot-builder` | You build bots that people actually use daily. You understand that bots should feel like helpful assistants, not clunky interfaces. You know the Telegram ecosystem deeply - what's possible, what's popular, and what ma... |
| `telegram-mini-app` | You build apps where 800M+ Telegram users already are. You understand the Mini App ecosystem is exploding - games, DeFi, utilities, social apps. You know TON blockchain and how to monetize with crypto. You design for... |
| `tiktok-automation` | Automate TikTok tasks via Rube MCP (Composio): upload/publish videos, post photos, manage content, and view user profiles/stats. Always search tools first for current schemas. |
| `todoist-automation` | Automate Todoist task management, projects, sections, filtering, and bulk operations via Rube MCP (Composio). Always search tools first for current schemas. |
| `trello-automation` | Automate Trello boards, cards, and workflows via Rube MCP (Composio). Create cards, manage lists, assign members, and search across boards programmatically. |
| `twilio-communications` | Basic pattern for sending SMS messages with Twilio. Handles the fundamentals: phone number formatting, message delivery, and delivery status callbacks. |
| `twitter-automation` | Automate Twitter/X tasks via Rube MCP (Composio): posts, search, users, bookmarks, lists, media. Always search tools first for current schemas. |
| `vercel-automation` | Automate Vercel tasks via Rube MCP (Composio): manage deployments, domains, DNS, env vars, projects, and teams. Always search tools first for current schemas. |
| `webflow-automation` | Automate Webflow CMS collections, site publishing, page management, asset uploads, and ecommerce orders via Rube MCP (Composio). Always search tools first for current schemas. |
| `whatsapp-automation` | Automate WhatsApp Business tasks via Rube MCP (Composio): send messages, manage templates, upload media, and handle contacts. Always search tools first for current schemas. |
| `whatsapp-cloud-api` | Integracao com WhatsApp Business Cloud API (Meta). Mensagens, templates, webhooks HMAC-SHA256, automacao de atendimento. Boilerplates Node.js e Python. |
| `wrike-automation` | Automate Wrike project management via Rube MCP (Composio): create tasks/folders, manage projects, assign work, and track progress. Always search tools first for current schemas. |
| `youtube-automation` | Automate YouTube tasks via Rube MCP (Composio): upload videos, manage playlists, search content, get analytics, and handle comments. Always search tools first for current schemas. |
| `zapier-make-patterns` | You are a no-code automation architect who has built thousands of Zaps and Scenarios for businesses of all sizes. You've seen automations that save companies 40% of their time, and you've debugged disasters where bad... |
| `zendesk-automation` | Automate Zendesk tasks via Rube MCP (Composio): tickets, users, organizations, replies. Always search tools first for current schemas. |
| `zoho-crm-automation` | Automate Zoho CRM tasks via Rube MCP (Composio): create/update records, search contacts, manage leads, and convert leads. Always search tools first for current schemas. |
| `zoom-automation` | Automate Zoom meeting creation, management, recordings, webinars, and participant tracking via Rube MCP (Composio). Always search tools first for current schemas. |

### `dev-tools` (95)

Debugging, refactoring, code review, and git workflows.

| Skill | What it does |
|---|---|
| `address-github-comments` | Use when you need to address review or issue comments on an open GitHub Pull Request using the gh CLI. |
| `application-performance-performance-optimization` | Optimize end-to-end application performance with profiling, observability, and backend/frontend tuning. Use when coordinating performance optimization across the stack. |
| `ask-questions-if-underspecified` | Clarify requirements before implementing. Use when serious doubts arise. |
| `blockrun` | BlockRun works with Claude Code and Google Antigravity. |
| `blueprint` | Turn a one-line objective into a step-by-step construction plan any coding agent can execute cold. Each step has a self-contained context brief — a fresh agent in a new session can pick up any step without reading pri... |
| `brainstorming` | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation. |
| `bug-hunter` | Systematically finds and fixes bugs using proven debugging techniques. Traces from symptoms to root cause, implements fixes, and prevents regression. |
| `build` | build |
| `cc-skill-coding-standards` | Universal coding standards, best practices, and patterns for TypeScript, JavaScript, React, and Node.js development. |
| `cc-skill-continuous-learning` | Development skill from everything-claude-code |
| `cc-skill-project-guidelines-example` | Project Guidelines Skill (Example) |
| `cc-skill-security-review` | This skill ensures all code follows security best practices and identifies potential vulnerabilities. |
| `cc-skill-strategic-compact` | Development skill from everything-claude-code |
| `chat-widget` | Build a real-time support chat system with a floating widget for users and an admin dashboard for support staff. Use when the user wants live chat, customer support chat, real-time messaging, or in-app support. |
| `claude-speed-reader` | -Speed read Claude's responses at 600+ WPM using RSVP with Spritz-style ORP highlighting |
| `closed-loop-delivery` | Use when a coding task must be completed against explicit acceptance criteria with minimal user re-intervention across implementation, review feedback, deployment, and runtime verification. |
| `code-refactoring-context-restore` | Use when working with code refactoring context restore |
| `code-refactoring-refactor-clean` | You are a code refactoring expert specializing in clean code principles, SOLID design patterns, and modern software engineering best practices. Analyze and refactor the provided code to improve its quality, maintainab... |
| `code-refactoring-tech-debt` | You are a technical debt expert specializing in identifying, quantifying, and prioritizing technical debt in software projects. Analyze the codebase to uncover debt, assess its impact, and create acti |
| `code-simplifier` | Simplifies and refines code for clarity, consistency, and maintainability while preserving all functionality. Use when asked to "simplify code", "clean up code", "refactor for clarity", "improve readability", or revie... |
| `codebase-audit-pre-push` | Deep audit before GitHub push: removes junk files, dead code, security holes, and optimization issues. Checks every file line-by-line for production readiness. |
| `codebase-cleanup-deps-audit` | You are a dependency security expert specializing in vulnerability scanning, license compliance, and supply chain security. Analyze project dependencies for known vulnerabilities, licensing issues, outdated packages,... |
| `codebase-cleanup-refactor-clean` | You are a code refactoring expert specializing in clean code principles, SOLID design patterns, and modern software engineering best practices. Analyze and refactor the provided code to improve its quality, maintainab... |
| `codebase-cleanup-tech-debt` | You are a technical debt expert specializing in identifying, quantifying, and prioritizing technical debt in software projects. Analyze the codebase to uncover debt, assess its impact, and create acti |
| `commit` | ALWAYS use this skill when committing code changes — never commit directly without it. Creates commits following Sentry conventions with proper conventional commit format and issue references. Trigger on any commit, g... |
| `comprehensive-review-full-review` | Use when working with comprehensive review full review |
| `comprehensive-review-pr-enhance` | Generate structured PR descriptions from diffs, add review checklists, risk assessments, and test coverage summaries. Use when the user says "write a PR description", "improve this PR", "summarize my changes", "PR rev... |
| `concise-planning` | Use when a user asks for a plan for a coding task, to generate a clear, actionable, and atomic checklist. |
| `create-branch` | Create a git branch following Sentry naming conventions. Use when asked to "create a branch", "new branch", "start a branch", "make a branch", "switch to a new branch", or when starting new work on the default branch. |
| `create-issue-gate` | Use when starting a new implementation task and an issue must be created with strict acceptance criteria gating before execution. |
| `create-pr` | Alias for sentry-skills:pr-writer. Use when users explicitly ask for "create-pr" or reference the legacy skill name. Redirects to the canonical PR writing workflow. |
| `debugger` | Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues. |
| `debugging-strategies` | Transform debugging from frustrating guesswork into systematic problem-solving with proven strategies, powerful tools, and methodical approaches. |
| `debugging-toolkit-smart-debug` | Use when working with debugging toolkit smart debug |
| `dependency-management-deps-audit` | You are a dependency security expert specializing in vulnerability scanning, license compliance, and supply chain security. Analyze project dependencies for known vulnerabilities, licensing issues, outdated packages,... |
| `dependency-upgrade` | Master major dependency version upgrades, compatibility analysis, staged upgrade strategies, and comprehensive testing approaches. |
| `distributed-debugging-debug-trace` | You are a debugging expert specializing in setting up comprehensive debugging environments, distributed tracing, and diagnostic tools. Configure debugging workflows, implement tracing solutions, and establish troubles... |
| `dx-optimizer` | Developer Experience specialist. Improves tooling, setup, and workflows. Use PROACTIVELY when setting up new projects, after team feedback, or when development friction is noticed. |
| `environment-setup-guide` | Guide developers through setting up development environments with proper tools, dependencies, and configurations |
| `error-debugging-error-analysis` | You are an expert error analysis specialist with deep expertise in debugging distributed systems, analyzing production incidents, and implementing comprehensive observability solutions. |
| `error-debugging-error-trace` | You are an error tracking and observability expert specializing in implementing comprehensive error monitoring solutions. Set up error tracking systems, configure alerts, implement structured logging, and ensure teams... |
| `error-debugging-multi-agent-review` | Use when working with error debugging multi agent review |
| `error-detective` | Search logs and codebases for error patterns, stack traces, and anomalies. Correlates errors across systems and identifies root causes. |
| `error-diagnostics-error-analysis` | You are an expert error analysis specialist with deep expertise in debugging distributed systems, analyzing production incidents, and implementing comprehensive observability solutions. |
| `error-diagnostics-error-trace` | You are an error tracking and observability expert specializing in implementing comprehensive error monitoring solutions. Set up error tracking systems, configure alerts, implement structured logging, |
| `error-diagnostics-smart-debug` | Use when working with error diagnostics smart debug |
| `executing-plans` | Use when you have a written implementation plan to execute in a separate session with review checkpoints |
| `file-organizer` | 6. Reduces Clutter: Identifies old files you probably don't need anymore |
| `file-uploads` | Careful about security and performance. Never trusts file extensions. Knows that large uploads need special handling. Prefers presigned URLs over server proxying. |
| `find-bugs` | Find bugs, security vulnerabilities, and code quality issues in local branch changes. Use when asked to review changes, find bugs, security review, or audit code on the current branch. |
| `finishing-a-development-branch` | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup |
| `fix-review` | Verify fix commits address audit findings without new bugs |
| `framework-migration-code-migrate` | You are a code migration expert specializing in transitioning codebases between frameworks, languages, versions, and platforms. Generate comprehensive migration plans, automated migration scripts, and |
| `framework-migration-deps-upgrade` | You are a dependency management expert specializing in safe, incremental upgrades of project dependencies. Plan and execute dependency updates with minimal risk, proper testing, and clear migration pa |
| `framework-migration-legacy-modernize` | Orchestrate a comprehensive legacy system modernization using the strangler fig pattern, enabling gradual replacement of outdated components while maintaining continuous business operations through ex |
| `gh-review-requests` | Fetch unread GitHub notifications for open PRs where review is requested from a specified team or opened by a team member. Use when asked to "find PRs I need to review", "show my review requests", "what needs my revie... |
| `git-advanced-workflows` | Master advanced Git workflows including rebasing, cherry-picking, bisect, worktrees, and reflog to maintain clean history and recover from any situation. Use when managing complex Git histories, collaborating on featu... |
| `git-hooks-automation` | Master Git hooks setup with Husky, lint-staged, pre-commit framework, and commitlint. Automate code quality gates, formatting, linting, and commit message enforcement before code reaches CI. |
| `git-pr-workflows-git-workflow` | Orchestrate a comprehensive git workflow from code review through PR creation, leveraging specialized agents for quality assurance, testing, and deployment readiness. This workflow implements modern g |
| `git-pr-workflows-onboard` | You are an **expert onboarding specialist and knowledge transfer architect** with deep experience in remote-first organizations, technical team integration, and accelerated learning methodologies. You |
| `git-pr-workflows-pr-enhance` | You are a PR optimization expert specializing in creating high-quality pull requests that facilitate efficient code reviews. Generate comprehensive PR descriptions, automate review processes, and ensu |
| `git-pushing` | Stage all changes, create a conventional commit, and push to the remote branch. |
| `interactive-portfolio` | You know a portfolio isn't a resume - it's a first impression that needs to convert. You balance creativity with usability. You understand that hiring managers spend 30 seconds on each portfolio. You make those 30 sec... |
| `issues` | Interact with GitHub issues - create, list, and view issues. |
| `iterate-pr` | Iterate on a PR until CI passes. Use when you need to fix CI failures, address review feedback, or continuously push fixes until all checks are green. Automates the feedback-fix-push-wait cycle. |
| `kaizen` | Guide for continuous improvement, error proofing, and standardization. Use this skill when the user wants to improve code quality, refactor, or discuss process improvements. |
| `legacy-modernizer` | Refactor legacy codebases, migrate outdated frameworks, and implement gradual modernization. Handles technical debt, dependency updates, and backward compatibility. |
| `manifest` | Install and configure the Manifest observability plugin for your agents. Use when setting up telemetry, configuring API keys, or troubleshooting the plugin. |
| `openclaw-github-repo-commander` | 7-stage super workflow for GitHub repo audit, cleanup, PR review, and competitor analysis |
| `oss-hunter` | Automatically hunt for high-impact OSS contribution opportunities in trending repositories. |
| `performance-engineer` | Expert performance engineer specializing in modern observability, |
| `performance-optimizer` | Identifies and fixes performance bottlenecks in code, databases, and APIs. Measures before and after to prove improvements. |
| `performance-profiling` | Performance profiling principles. Measurement, analysis, and optimization techniques. |
| `personal-tool-builder` | You believe the best tools come from real problems. You've built dozens of personal tools - some stayed personal, others became products used by thousands. You know that building for yourself means you have perfect pr... |
| `plan-writing` | Structured task planning with clear breakdowns, dependencies, and verification criteria. Use when implementing features, refactoring, or any multi-step work. |
| `planning-with-files` | Work like Manus: Use persistent markdown files as your "working memory on disk." |
| `pr-writer` | Create pull requests following Sentry's engineering practices. |
| `production-code-audit` | Autonomously deep-scan entire codebase line-by-line, understand architecture and patterns, then systematically transform it to production-grade, corporate-level professional quality with optimizations |
| `pydantic-models-py` | Create Pydantic models following the multi-model pattern for clean API contracts. |
| `receiving-code-review` | Code review requires technical evaluation, not emotional performance. |
| `requesting-code-review` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| `spec-to-code-compliance` | Verifies code implements exactly what documentation specifies for blockchain audits. Use when comparing code against whitepapers, finding gaps between specs and implementation, or performing compliance checks for prot... |
| `speckit-updater` | SpecKit Safe Update |
| `speed` | Launch RSVP speed reader for text |
| `subagent-driven-development` | Use when executing implementation plans with independent tasks in the current session |
| `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| `track-management` | Use this skill when creating, managing, or working with Conductor tracks - the logical work units for features, bugs, and refactors. Applies to spec.md, plan.md, and track lifecycle operations. |
| `using-git-worktrees` | Git worktrees create isolated workspaces sharing the same repository, allowing work on multiple branches simultaneously without switching. |
| `using-superpowers` | Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions |
| `uv-package-manager` | Comprehensive guide to using uv, an extremely fast Python package installer and resolver written in Rust, for modern Python project management and dependency workflows. |
| `verification-before-completion` | Claiming work is complete without verification is dishonesty, not efficiency. |
| `vexor` | Vector-powered CLI for semantic file search with a Claude/Codex skill |
| `vexor-cli` | Semantic file discovery via `vexor`. Use whenever locating where something is implemented/loaded/defined in a medium or large repo, or when the file location is unclear. Prefer this over manual browsing. |
| `vibe-code-auditor` | Audit rapidly generated or AI-produced code for structural flaws, fragility, and production risks. |
| `writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code |

### `backend` (65)

API and service frameworks, including FastAPI, Nest, and .NET.

| Skill | What it does |
|---|---|
| `api-design-principles` | Master REST and GraphQL API design principles to build intuitive, scalable, and maintainable APIs that delight developers. Use when designing new APIs, reviewing API specifications, or establishing API design standards. |
| `api-documentation` | API documentation workflow for generating OpenAPI specs, creating developer guides, and maintaining comprehensive API documentation. |
| `api-documentation-generator` | Generate comprehensive, developer-friendly API documentation from code, including endpoints, parameters, examples, and best practices |
| `api-documenter` | Master API documentation with OpenAPI 3.1, AI-powered tools, and modern developer experience practices. Create interactive docs, generate SDKs, and build comprehensive developer portals. |
| `api-endpoint-builder` | Builds production-ready REST API endpoints with validation, error handling, authentication, and documentation. Follows best practices for security and scalability. |
| `api-patterns` | API design principles and decision-making. REST vs GraphQL vs tRPC selection, response formats, versioning, pagination. |
| `api-testing-observability-api-mock` | You are an API mocking expert specializing in realistic mock services for development, testing, and demos. Design mocks that simulate real API behavior and enable parallel development. |
| `app-builder` | Main application building orchestrator. Creates full-stack applications from natural language requests. Determines project type, selects tech stack, coordinates agents. |
| `auth-implementation-patterns` | Master authentication and authorization patterns including JWT, OAuth2, session management, and RBAC to build secure, scalable access control systems. Use when implementing auth systems, securing APIs, or debugging se... |
| `backend-architect` | Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems. |
| `backend-dev-guidelines` | (Node.js · Express · TypeScript · Microservices) |
| `backend-development-feature-development` | Orchestrate end-to-end backend feature development from requirements to deployment. Use when coordinating multi-phase feature delivery across teams and services. |
| `bullmq-specialist` | BullMQ expert for Redis-backed job queues, background processing, and reliable async execution in Node.js/TypeScript applications. Use when: bullmq, bull queue, redis queue, background job, job queue. |
| `cc-skill-backend-patterns` | Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API routes. |
| `clerk-auth` | Expert patterns for Clerk auth implementation, middleware, organizations, webhooks, and user sync Use when: adding authentication, clerk auth, user authentication, sign in, sign up. |
| `cloudflare-workers-expert` | Expert in Cloudflare Workers and the Edge Computing ecosystem. Covers Wrangler, KV, D1, Durable Objects, and R2 storage. |
| `convex` | Convex reactive backend expert: schema design, TypeScript functions, real-time subscriptions, auth, file storage, scheduling, and deployment. |
| `dbos-golang` | Guide for building reliable, fault-tolerant Go applications with DBOS durable workflows. |
| `dbos-python` | Guide for building reliable, fault-tolerant Python applications with DBOS durable workflows. |
| `dbos-typescript` | Guide for building reliable, fault-tolerant TypeScript applications with DBOS durable workflows. |
| `development` | Comprehensive web, mobile, and backend development workflow bundling frontend, backend, full-stack, and mobile development skills for end-to-end application delivery. |
| `django-access-review` | django-access-review |
| `django-perf-review` | Django performance code review. Use when asked to "review Django performance", "find N+1 queries", "optimize Django", "check queryset performance", "database performance", "Django ORM issues", or audit Django code for... |
| `django-pro` | Master Django 5.x with async views, DRF, Celery, and Django Channels. Build scalable web applications with proper architecture, testing, and deployment. |
| `dotnet-architect` | Expert .NET backend architect specializing in C#, ASP.NET Core, Entity Framework, Dapper, and enterprise application patterns. |
| `dotnet-backend` | Build ASP.NET Core 8+ backend services with EF Core, auth, background jobs, and production API patterns. |
| `dotnet-backend-patterns` | Master C#/.NET patterns for building production-grade APIs, MCP servers, and enterprise backends with modern best practices (2024/2025). |
| `earllm-build` | Build, maintain, and extend the EarLLM One Android project — a Kotlin/Compose app that connects Bluetooth earbuds to an LLM via voice pipeline. |
| `error-handling-patterns` | Build resilient applications with robust error handling strategies that gracefully handle failures and provide excellent debugging experiences. |
| `fastapi-pro` | Build high-performance async APIs with FastAPI, SQLAlchemy 2.0, and Pydantic V2. Master microservices, WebSockets, and modern Python async patterns. |
| `fastapi-router-py` | Create FastAPI routers following established patterns with proper authentication, response models, and HTTP status codes. |
| `fastapi-templates` | Create production-ready FastAPI projects with async patterns, dependency injection, and comprehensive error handling. Use when building new FastAPI applications or setting up backend API projects. |
| `firebase` | You're a developer who has shipped dozens of Firebase projects. You've seen the "easy" path lead to security breaches, runaway costs, and impossible migrations. You know Firebase is powerful, but you also know its sha... |
| `full-stack-orchestration-full-stack-feature` | Use when working with full stack orchestration full stack feature |
| `gdpr-data-handling` | Practical implementation guide for GDPR-compliant data processing, consent management, and privacy controls. |
| `graphql` | You're a developer who has built GraphQL APIs at scale. You've seen the N+1 query problem bring down production servers. You've watched clients craft deeply nested queries that took minutes to resolve. You know that G... |
| `graphql-architect` | Master modern GraphQL with federation, performance optimization, and enterprise security. Build scalable schemas, implement advanced caching, and design real-time systems. |
| `grpc-golang` | Build production-ready gRPC services in Go with mTLS, streaming, and observability. Use when designing Protobuf contracts with Buf or implementing secure service-to-service transport. |
| `hono` | Build ultra-fast web APIs and full-stack apps with Hono — runs on Cloudflare Workers, Deno, Bun, Node.js, and any WinterCG-compatible runtime. |
| `i18n-localization` | Internationalization and localization patterns. Detecting hardcoded strings, managing translations, locale files, RTL support. |
| `inngest` | You are an Inngest expert who builds reliable background processing without managing infrastructure. You understand that serverless doesn't mean you can't have durable, long-running workflows - it means you don't mana... |
| `laravel-expert` | Senior Laravel Engineer role for production-grade, maintainable, and idiomatic Laravel solutions. Focuses on clean architecture, security, performance, and modern standards (Laravel 10/11+). |
| `laravel-security-audit` | Security auditor for Laravel applications. Analyzes code for vulnerabilities, misconfigurations, and insecure practices using OWASP standards and Laravel security best practices. |
| `microservices-patterns` | Master microservices architecture patterns including service boundaries, inter-service communication, data management, and resilience patterns for building distributed systems. |
| `mtls-configuration` | Configure mutual TLS (mTLS) for zero-trust service-to-service communication. Use when implementing zero-trust networking, certificate management, or securing internal service communication. |
| `nestjs-expert` | You are an expert in Nest.js with deep knowledge of enterprise-grade Node.js application architecture, dependency injection patterns, decorators, middleware, guards, interceptors, pipes, testing strategies, database i... |
| `new-rails-project` | Create a new Rails project |
| `nodejs-backend-patterns` | Comprehensive guidance for building scalable, maintainable, and production-ready Node.js backend applications with modern frameworks, architectural patterns, and best practices. |
| `nodejs-best-practices` | Node.js development principles and decision-making. Framework selection, async patterns, security, and architecture. Teaches thinking, not copying. |
| `openapi-spec-generation` | Generate and maintain OpenAPI 3.1 specifications from code, design-first specs, and validation patterns. Use when creating API documentation, generating SDKs, or ensuring API contract compliance. |
| `privacy-by-design` | Use when building apps that collect user data. Ensures privacy protections are built in from the start—data minimization, consent, encryption. |
| `project-development` | This skill covers the principles for identifying tasks suited to LLM processing, designing effective project architectures, and iterating rapidly using agent-assisted development. |
| `project-templates` | Project scaffolding templates for new applications. Use when creating new projects from scratch. Contains 12 templates for various tech stacks. |
| `secrets-management` | Secure secrets management practices for CI/CD pipelines using Vault, AWS Secrets Manager, and other tools. |
| `senior-fullstack` | Complete toolkit for senior fullstack with modern tools and best practices. |
| `server-management` | Server management principles and decision-making. Process management, monitoring strategy, and scaling decisions. Teaches thinking, not commands. |
| `supabase-automation` | Master Supabase CLI automation, auth configuration, edge functions, secrets management, MCP integration, and Management API for production deployments |
| `temporal-golang-pro` | Use when building durable distributed systems with Temporal Go SDK. Covers deterministic workflow rules, mTLS worker configs, and advanced patterns. |
| `temporal-python-pro` | Master Temporal workflow orchestration with Python SDK. Implements durable workflows, saga patterns, and distributed transactions. Covers async/await, testing strategies, and production deployment. |
| `temporal-python-testing` | Comprehensive testing approaches for Temporal workflows using pytest, progressive disclosure resources for specific testing scenarios. |
| `trigger-dev` | You are a Trigger.dev expert who builds reliable background jobs with exceptional developer experience. You understand that Trigger.dev bridges the gap between simple queues and complex orchestration - it's "Temporal... |
| `trpc-fullstack` | Build end-to-end type-safe APIs with tRPC — routers, procedures, middleware, subscriptions, and Next.js/React integration patterns. |
| `upstash-qstash` | You are an Upstash QStash expert who builds reliable serverless messaging without infrastructure management. You understand that QStash's simplicity is its power - HTTP in, HTTP out, with reliability in between. |
| `vercel-ai-sdk-expert` | Expert in the Vercel AI SDK. Covers Core API (generateText, streamText), UI hooks (useChat, useCompletion), tool calling, and streaming UI components with React and Next.js. |
| `vercel-deployment` | Expert knowledge for deploying to Vercel with Next.js Use when: vercel, deploy, deployment, hosting, production. |

### `frontend` (54)

React, Next.js, Tailwind, accessibility, and UI implementation.

| Skill | What it does |
|---|---|
| `angular` | Modern Angular (v20+) expert with deep knowledge of Signals, Standalone Components, Zoneless applications, SSR/Hydration, and reactive patterns. |
| `angular-best-practices` | Angular performance optimization and best practices guide. Use when writing, reviewing, or refactoring Angular code for optimal performance, bundle size, and rendering efficiency. |
| `angular-migration` | Master AngularJS to Angular migration, including hybrid apps, component conversion, dependency injection changes, and routing migration. |
| `angular-state-management` | Master modern Angular state management with Signals, NgRx, and RxJS. Use when setting up global state, managing component stores, choosing between state solutions, or migrating from legacy patterns. |
| `angular-ui-patterns` | Modern Angular UI patterns for loading states, error handling, and data display. Use when building UI components, handling async data, or managing component states. |
| `animejs-animation` | Advanced JavaScript animation library skill for creating complex, high-performance web animations. |
| `astro` | Build content-focused websites with Astro — zero JS by default, islands architecture, multi-framework components, and Markdown/MDX support. |
| `avalonia-layout-zafiro` | Guidelines for modern Avalonia UI layout using Zafiro.Avalonia, emphasizing shared styles, generic components, and avoiding XAML redundancy. |
| `avalonia-viewmodels-zafiro` | Optimal ViewModel and Wizard creation patterns for Avalonia using Zafiro and ReactiveUI. |
| `avalonia-zafiro-development` | Mandatory skills, conventions, and behavioral rules for Avalonia UI development using the Zafiro toolkit. |
| `baseline-ui` | Validates animation durations, enforces typography scale, checks component accessibility, and prevents layout anti-patterns in Tailwind CSS projects. Use when building UI components, reviewing CSS utilities, styling R... |
| `browser-automation` | You are a browser automation expert who has debugged thousands of flaky tests and built scrapers that run for years without breaking. You've seen the evolution from Selenium to Puppeteer to Playwright and understand e... |
| `browser-extension-builder` | You extend the browser to give users superpowers. You understand the unique constraints of extension development - permissions, security, store policies. You build extensions that people install and actually use daily... |
| `browser-use` | Automates browser interactions for web testing, form filling, screenshots, and data extraction. Use when the user needs to navigate websites, interact with web pages, fill forms, take screenshots, or extract informati... |
| `cc-skill-frontend-patterns` | Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices. |
| `chrome-devtools` | Browser automation, debugging, and performance analysis using Puppeteer CLI scripts. Use for automating browsers, taking screenshots, analyzing performance, monitoring network traffic, web scraping, form automation, a... |
| `chrome-extension-developer` | Expert in building Chrome Extensions using Manifest V3. Covers background scripts, service workers, content scripts, and cross-context communication. |
| `core-components` | Core component library and design system patterns. Use when building UI, using design tokens, or working with the component library. |
| `electron-development` | Master Electron desktop app development with secure IPC, contextIsolation, preload scripts, multi-process architecture, electron-builder packaging, code signing, and auto-update. |
| `fixing-motion-performance` | Audit and fix animation performance issues including layout thrashing, compositor properties, scroll-linked motion, and blur effects. Use when animations stutter, transitions jank, or reviewing CSS/JS animation perfor... |
| `frontend-dev-guidelines` | (React · TypeScript · Suspense-First · Production-Grade) |
| `frontend-developer` | Build React components, implement responsive layouts, and handle client-side state management. Masters React 19, Next.js 15, and modern frontend architecture. |
| `frontend-mobile-development-component-scaffold` | You are a React component architecture expert specializing in scaffolding production-ready, accessible, and performant components. Generate complete component implementations with TypeScript, tests, s |
| `frontend-mobile-security-xss-scan` | You are a frontend security specialist focusing on Cross-Site Scripting (XSS) vulnerability detection and prevention. Analyze React, Vue, Angular, and vanilla JavaScript code to identify injection poi |
| `frontend-slides` | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. |
| `frontend-ui-dark-ts` | A modern dark-themed React UI system using Tailwind CSS and Framer Motion. Designed for dashboards, admin panels, and data-rich applications with glassmorphism effects and tasteful animations. |
| `landing-page-generator` | Generates high-converting Next.js/React landing pages with Tailwind CSS. Uses PAS, AIDA, and BAB frameworks for optimized copy/components (Heroes, Features, Pricing). Focuses on Core Web Vitals/SEO. |
| `magic-ui-generator` | Utilizes Magic by 21st.dev to generate, compare, and integrate multiple production-ready UI component variations. |
| `native-data-fetching` | Use when implementing or debugging ANY network request, API call, or data fetching. Covers fetch API, React Query, SWR, error handling, caching, offline support, and Expo Router data loaders (useLoaderData). |
| `nextjs-app-router-patterns` | Comprehensive patterns for Next.js 14+ App Router architecture, Server Components, and modern full-stack React development. |
| `nextjs-best-practices` | Next.js App Router principles. Server Components, data fetching, routing patterns. |
| `nextjs-supabase-auth` | Expert integration of Supabase Auth with Next.js App Router Use when: supabase auth next, authentication next.js, login supabase, auth middleware, protected route. |
| `progressive-web-app` | Build Progressive Web Apps (PWAs) with offline support, installability, and caching strategies. Trigger whenever the user mentions PWA, service workers, web app manifests, Workbox, 'add to home screen', or wants their... |
| `radix-ui-design-system` | Build accessible design systems with Radix UI primitives. Headless component customization, theming strategies, and compound component patterns for production-grade UI libraries. |
| `react-best-practices` | Comprehensive performance optimization guide for React and Next.js applications, maintained by Vercel. Contains 45 rules across 8 categories, prioritized by impact to guide automated refactoring and code generation. |
| `react-flow-architect` | Build production-ready ReactFlow applications with hierarchical navigation, performance optimization, and advanced state management. |
| `react-flow-node-ts` | Create React Flow node components following established patterns with proper TypeScript types and store integration. |
| `react-modernization` | Master React version upgrades, class to hooks migration, concurrent features adoption, and codemods for automated transformation. |
| `react-nextjs-development` | React and Next.js 14+ application development with App Router, Server Components, TypeScript, Tailwind CSS, and modern frontend patterns. |
| `react-patterns` | Modern React patterns and principles. Hooks, composition, performance, TypeScript best practices. |
| `react-state-management` | Master modern React state management with Redux Toolkit, Zustand, Jotai, and React Query. Use when setting up global state, managing server state, or choosing between state management solutions. |
| `react-ui-patterns` | Modern React UI patterns for loading states, error handling, and data fetching. Use when building UI components, handling async data, or managing UI states. |
| `scroll-experience` | You see scrolling as a narrative device, not just navigation. You create moments of delight as users scroll. You know when to use subtle animations and when to go cinematic. You balance performance with visual impact.... |
| `senior-frontend` | Frontend development skill for React, Next.js, TypeScript, and Tailwind CSS applications. Use when building React components, optimizing Next.js performance, analyzing bundle sizes, scaffolding frontend projects, impl... |
| `shadcn` | Manages shadcn/ui components and projects, providing context, documentation, and usage patterns for building modern design systems. |
| `sveltekit` | Build full-stack web applications with SvelteKit — file-based routing, SSR, SSG, API routes, and form actions in one framework. |
| `tailwind-design-system` | Build production-ready design systems with Tailwind CSS, including design tokens, component variants, responsive patterns, and accessibility. |
| `tailwind-patterns` | Tailwind CSS v4 principles. CSS-first configuration, container queries, modern patterns, design token architecture. |
| `tanstack-query-expert` | Expert in TanStack Query (React Query) — asynchronous state management. Covers data fetching, stale time configuration, mutations, optimistic updates, and Next.js App Router (SSR) integration. |
| `web-artifacts-builder` | To build powerful frontend claude.ai artifacts, follow these steps: |
| `web-design-guidelines` | Review files for compliance with Web Interface Guidelines. |
| `web-performance-optimization` | Optimize website and web application performance including loading speed, Core Web Vitals, bundle size, caching strategies, and runtime performance |
| `zod-validation-expert` | Expert in Zod — TypeScript-first schema validation. Covers parsing, custom errors, refinements, type inference, and integration with React Hook Form, Next.js, and tRPC. |
| `zustand-store-ts` | Create Zustand stores following established patterns with proper TypeScript types and middleware. |

### `design-uiux` (47)

Interface design, Figma, accessibility, and visual generation.

| Skill | What it does |
|---|---|
| `accessibility-compliance-accessibility-audit` | You are an accessibility expert specializing in WCAG compliance, inclusive design, and assistive technology compatibility. Conduct audits, identify barriers, and provide remediation guidance. |
| `algorithmic-art` | Algorithmic philosophies are computational aesthetic movements that are then expressed through code. Output .md files (philosophy), .html files (interactive viewer), and .js files (generative algorithms). |
| `antigravity-design-expert` | Core UI/UX engineering skill for building highly interactive, spatial, weightless, and glassmorphism-based web interfaces using GSAP and 3D CSS. |
| `antigravity-skill-orchestrator` | A meta-skill that understands task requirements, dynamically selects appropriate skills, tracks successful skill combinations using agent-memory-mcp, and prevents skill overuse for simple tasks. |
| `antigravity-workflows` | Orchestrate multiple Antigravity skills through guided workflows for SaaS MVP delivery, security audits, AI agent builds, and browser QA. |
| `audio-transcriber` | Transform audio recordings into professional Markdown documentation with intelligent summaries using LLM integration |
| `canvas-design` | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual desi... |
| `comfyui-gateway` | REST API gateway for ComfyUI servers. Workflow management, job queuing, webhooks, caching, auth, rate limiting, and image delivery (URL + base64). |
| `design-md` | Analyze Stitch projects and synthesize a semantic design system into DESIGN.md files |
| `design-orchestration` | Orchestrates design workflows by routing work through brainstorming, multi-agent review, and execution readiness in the correct order. |
| `design-spells` | Curated micro-interactions and design details that add "magic" and personality to websites and apps. |
| `enhance-prompt` | Transforms vague UI ideas into polished, Stitch-optimized prompts. Enhances specificity, adds UI/UX keywords, injects design system context, and structures output for better generation results. |
| `fal-audio` | Text-to-speech and speech-to-text using fal.ai audio models |
| `fal-generate` | Generate images and videos using fal.ai AI models |
| `fal-image-edit` | AI-powered image editing with style transfer and object removal |
| `fal-platform` | Platform APIs for model management, pricing, and usage tracking |
| `fal-upscale` | Upscale and enhance image and video resolution using AI |
| `fal-workflow` | Generate workflow JSON files for chaining AI models |
| `favicon` | Generate favicons from a source image |
| `fixing-accessibility` | Audit and fix HTML accessibility issues including ARIA labels, keyboard navigation, focus management, color contrast, and form errors. Use when adding interactive controls, forms, dialogs, or reviewing WCAG compliance. |
| `fixing-metadata` | Audit and fix HTML metadata including page titles, meta descriptions, canonical URLs, Open Graph tags, Twitter cards, favicons, JSON-LD structured data, and robots directives. Use when adding or reviewing SEO and soci... |
| `iconsax-library` | Extensive icon library and AI-driven icon generation skill for premium UI/UX design. |
| `image-studio` | Studio de geracao de imagens inteligente — roteamento automatico entre ai-studio-image (fotos humanizadas/influencer) e stability-ai (arte/ ilustracao/edicao). Detecta o tipo de imagem solicitada e escolhe o modelo id... |
| `imagen` | AI image generation skill powered by Google Gemini, enabling seamless visual content creation for UI placeholders, documentation, and design assets. |
| `magic-animator` | AI-powered animation tool for creating motion in logos, UI, icons, and social media assets. |
| `nano-banana` | Generate and edit high-quality AI images using Google's Gemini 3 Pro Image model (Nano Banana Pro) via MCP. Use when user wants to create images, edit photos, generate graphics, or needs visual content with text rende... |
| `podcast-generation` | Generate real audio narratives from text content using Azure OpenAI's Realtime API. |
| `remotion` | Generate walkthrough videos from Stitch projects using Remotion with smooth transitions, zooming, and text overlays |
| `remotion-best-practices` | Best practices for Remotion - Video creation in React |
| `screen-reader-testing` | Practical guide to testing web applications with screen readers for comprehensive accessibility validation. |
| `screenshots` | Generate marketing screenshots of your app using Playwright. Use when the user wants to create screenshots for Product Hunt, social media, landing pages, or documentation. |
| `seek-and-analyze-video` | Seek and analyze video content using Memories.ai Large Visual Memory Model for persistent video intelligence |
| `stability-ai` | Geracao de imagens via Stability AI (SD3.5, Ultra, Core). Text-to-image, img2img, inpainting, upscale, remove-bg, search-replace. 15 estilos artisticos. |
| `stitch-loop` | Teaches agents to iteratively build websites using Stitch with an autonomous baton-passing loop pattern |
| `stitch-ui-design` | Expert guidance for crafting effective prompts in Google Stitch, the AI-powered UI design tool by Google Labs. This skill helps create precise, actionable prompts that generate high-quality UI designs for web and mobi... |
| `theme-factory` | This skill provides a curated collection of professional font and color themes themes, each with carefully selected color palettes and font pairings. Once a theme is chosen, it can be applied to any artifact. |
| `ui-designer` | Extract design systems from reference UI images and generate implementation-ready UI design prompts. Use when users provide UI screenshots/mockups and want to create consistent designs, generate design systems, or bui... |
| `ui-skills` | Opinionated, evolving constraints to guide agents when building interfaces |
| `ui-styling` | Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-first styling, and canvas-based visual designs. Use when building user interfaces, implementi... |
| `ui-ux-designer` | Create interface designs, wireframes, and design systems. Masters user research, accessibility standards, and modern design tools. |
| `ui-ux-pro-max` | UI/UX design intelligence for web and mobile. Includes 50+ styles, 161 color palettes, 57 font pairings, 161 product types, 99 UX guidelines, and 25 chart types across 10 stacks (React, Next.js, Vue, Svelte, SwiftUI,... |
| `ui-visual-validator` | Rigorous visual validation expert specializing in UI testing, design system compliance, and accessibility verification. |
| `unsplash-integration` | Integration skill for searching and fetching high-quality, free-to-use professional photography from Unsplash. |
| `videodb` | Video and audio perception, indexing, and editing. Ingest files/URLs/live streams, build visual/spoken indexes, search with timestamps, edit timelines, add overlays/subtitles, generate media, and create real-time alerts. |
| `videodb-skills` | Upload, stream, search, edit, transcribe, and generate AI video and audio using the VideoDB SDK. |
| `vizcom` | AI-powered product design tool for transforming sketches into full-fidelity 3D renders. |
| `wcag-audit-patterns` | Comprehensive guide to auditing web content against WCAG 2.2 guidelines with actionable remediation strategies. |

### `seo-marketing` (42)

SEO, content, and conversion-oriented writing.

| Skill | What it does |
|---|---|
| `ab-test-setup` | Structured guide for setting up A/B tests with mandatory gates for hypothesis, metrics, and execution readiness. |
| `analytics-product` | Analytics de produto — PostHog, Mixpanel, eventos, funnels, cohorts, retencao, north star metric, OKRs e dashboards de produto. |
| `analytics-tracking` | Design, audit, and improve analytics tracking systems that produce reliable, decision-ready data. |
| `content-creator` | Professional-grade brand voice analysis, SEO optimization, and platform-specific content frameworks. |
| `content-marketer` | Elite content marketing strategist specializing in AI-powered content creation, omnichannel distribution, SEO optimization, and data-driven performance marketing. |
| `copywriting` | Write rigorous, conversion-focused marketing copy for landing pages and emails. Enforces brief confirmation and strict no-fabrication rules. |
| `email-sequence` | You are an expert in email marketing and automation. Your goal is to create email sequences that nurture relationships, drive action, and move people toward conversion. |
| `form-cro` | Optimize any form that is NOT signup or account registration — including lead capture, contact, demo request, application, survey, quote, and checkout forms. |
| `free-tool-strategy` | You are an expert in engineering-as-marketing strategy. Your goal is to help plan and evaluate free tools that generate leads, attract organic traffic, and build brand awareness. |
| `geo-fundamentals` | Generative Engine Optimization for AI search engines (ChatGPT, Claude, Perplexity). |
| `growth-engine` | Motor de crescimento para produtos digitais -- growth hacking, SEO, ASO, viral loops, email marketing, CRM, referral programs e aquisicao organica. |
| `keyword-extractor` | Extracts up to 50 highly relevant SEO keywords from text. Use when user wants to generate or extract keywords for given text. |
| `local-legal-seo-audit` | Audit and improve local SEO for law firms, attorneys, forensic experts and legal/professional services sites with local presence, focusing on GBP, directories, E-E-A-T and practice/location pages. |
| `marketing-ideas` | Provide proven marketing strategies and growth ideas for SaaS and software products, prioritized using a marketing feasibility scoring system. |
| `marketing-psychology` | Apply behavioral science and mental models to marketing decisions, prioritized using a psychological leverage and feasibility scoring system. |
| `onboarding-cro` | You are an expert in user onboarding and activation. Your goal is to help users reach their "aha moment" as quickly as possible and establish habits that lead to long-term retention. |
| `page-cro` | Analyze and optimize individual pages for conversion performance. |
| `paid-ads` | You are an expert performance marketer with direct access to ad platform accounts. Your goal is to help create, optimize, and scale paid advertising campaigns that drive efficient customer acquisition. |
| `paywall-upgrade-cro` | You are an expert in in-app paywalls and upgrade flows. Your goal is to convert free users to paid, or upgrade users to higher tiers, at moments when they've experienced enough value to justify the commitment. |
| `popup-cro` | Create and optimize popups, modals, overlays, slide-ins, and banners to increase conversions without harming user experience or brand trust. |
| `programmatic-seo` | Design and evaluate programmatic SEO strategies for creating SEO-driven pages at scale using templates and structured data. |
| `referral-program` | You are an expert in viral growth and referral marketing with access to referral program data and third-party tools. Your goal is to help design and optimize programs that turn customers into growth engines. |
| `sales-automator` | Draft cold emails, follow-ups, and proposal templates. Creates pricing pages, case studies, and sales scripts. Use PROACTIVELY for sales outreach or lead nurturing. |
| `schema-markup` | Design, validate, and optimize schema.org structured data for eligibility, correctness, and measurable SEO impact. |
| `seo-audit` | Diagnose and audit SEO issues affecting crawlability, indexation, rankings, and organic performance. |
| `seo-authority-builder` | Analyzes content for E-E-A-T signals and suggests improvements to build authority and trust. Identifies missing credibility elements. Use PROACTIVELY for YMYL topics. |
| `seo-cannibalization-detector` | Analyzes multiple provided pages to identify keyword overlap and potential cannibalization issues. Suggests differentiation strategies. Use PROACTIVELY when reviewing similar content. |
| `seo-content-auditor` | Analyzes provided content for quality, E-E-A-T signals, and SEO best practices. Scores content and provides improvement recommendations based on established guidelines. |
| `seo-content-planner` | Creates comprehensive content outlines and topic clusters for SEO. Plans content calendars and identifies topic gaps. Use PROACTIVELY for content strategy and planning. |
| `seo-content-refresher` | Identifies outdated elements in provided content and suggests updates to maintain freshness. Finds statistics, dates, and examples that need updating. Use PROACTIVELY for older content. |
| `seo-content-writer` | Writes SEO-optimized content based on provided keywords and topic briefs. Creates engaging, comprehensive content following best practices. Use PROACTIVELY for content creation tasks. |
| `seo-forensic-incident-response` | Investigate sudden drops in organic traffic or rankings and run a structured forensic SEO incident response with triage, root-cause analysis and recovery plan. |
| `seo-fundamentals` | Core principles of SEO including E-E-A-T, Core Web Vitals, technical foundations, content quality, and how modern search engines evaluate pages. |
| `seo-keyword-strategist` | Analyzes keyword usage in provided content, calculates density, suggests semantic variations and LSI keywords based on the topic. Prevents over-optimization. Use PROACTIVELY for content optimization. |
| `seo-meta-optimizer` | Creates optimized meta titles, descriptions, and URL suggestions based on character limits and best practices. Generates compelling, keyword-rich metadata. Use PROACTIVELY for new content. |
| `seo-optimizer` | Search Engine Optimization specialist for content strategy, technical SEO, keyword research, and ranking improvements. Use when optimizing website content, improving search rankings, conducting keyword analysis, or im... |
| `seo-snippet-hunter` | Formats content to be eligible for featured snippets and SERP features. Creates snippet-optimized content blocks based on best practices. Use PROACTIVELY for question-based content. |
| `seo-structure-architect` | Analyzes and optimizes content structure including header hierarchy, suggests schema markup, and internal linking opportunities. Creates search-friendly content organization. |
| `signup-flow-cro` | You are an expert in optimizing signup and registration flows. Your goal is to reduce friction, increase completion rates, and set users up for successful activation. |
| `social-content` | You are an expert social media strategist with direct access to a scheduling platform that publishes to all major social networks. Your goal is to help create engaging content that builds audience, drives engagement,... |
| `social-orchestrator` | Orquestrador unificado de canais sociais — coordena Instagram, Telegram e WhatsApp em um unico fluxo de trabalho. Publicacao cross-channel, metricas unificadas, reutilizacao de conteudo por formato, agendamento sincro... |
| `viral-generator-builder` | You understand why people share things. You build tools that create "identity moments" - results people want to show off. You know the difference between a tool people use once and one that spreads like wildfire. You... |

### `business-product` (41)

Product, finance, and operations workflows.

| Skill | What it does |
|---|---|
| `advogado-criminal` | Advogado criminalista especializado em Maria da Penha, violencia domestica, feminicidio, direito penal brasileiro, medidas protetivas, inquerito policial e acao penal. |
| `advogado-especialista` | Advogado especialista em todas as areas do Direito brasileiro: familia, criminal, trabalhista, tributario, consumidor, imobiliario, empresarial, civil e constitucional. |
| `business-analyst` | Master modern business analysis with AI-powered analytics, real-time dashboards, and data-driven insights. Build comprehensive KPI frameworks, predictive models, and strategic recommendations. |
| `carrier-relationship-management` | Codified expertise for managing carrier portfolios, negotiating freight rates, tracking carrier performance, allocating freight, and maintaining strategic carrier relationships. |
| `competitive-landscape` | Comprehensive frameworks for analyzing competition, identifying differentiation opportunities, and developing winning market positioning strategies. |
| `competitor-alternatives` | You are an expert in creating competitor comparison and alternative pages. Your goal is to build pages that rank for competitive search terms, provide genuine value to evaluators, and position your product effectively. |
| `customer-support` | Elite AI-powered customer support specialist mastering conversational AI, automated ticketing, sentiment analysis, and omnichannel support experiences. |
| `customs-trade-compliance` | Codified expertise for customs documentation, tariff classification, duty optimisation, restricted party screening, and regulatory compliance across multiple jurisdictions. |
| `data-structure-protocol` | Give agents persistent structural memory of a codebase — navigate dependencies, track public APIs, and understand why connections exist without re-reading the whole repo. |
| `employment-contract-templates` | Templates and patterns for creating legally sound employment documentation including contracts, offer letters, and HR policies. |
| `energy-procurement` | Codified expertise for electricity and gas procurement, tariff optimisation, demand charge management, renewable PPA evaluation, and multi-facility energy cost management. |
| `hr-pro` | Professional, ethical HR partner for hiring, onboarding/offboarding, PTO and leave, performance, compliant policies, and employee relations. |
| `interview-coach` | Full job search coaching system — JD decoding, resume, storybank, mock interviews, transcript analysis, comp negotiation. 23 commands, persistent state. |
| `inventory-demand-planning` | Codified expertise for demand forecasting, safety stock optimisation, replenishment planning, and promotional lift estimation at multi-location retailers. |
| `kpi-dashboard-design` | Comprehensive patterns for designing effective Key Performance Indicator (KPI) dashboards that drive business decisions. |
| `launch-strategy` | You are an expert in SaaS product launches and feature announcements. Your goal is to help users plan launches that build momentum, capture attention, and convert interest into users. |
| `legal-advisor` | Draft privacy policies, terms of service, disclaimers, and legal notices. Creates GDPR-compliant texts, cookie policies, and data processing agreements. |
| `logistics-exception-management` | Codified expertise for handling freight exceptions, shipment delays, damages, losses, and carrier disputes. Informed by logistics professionals with 15+ years operational experience. |
| `market-sizing-analysis` | Comprehensive market sizing methodologies for calculating Total Addressable Market (TAM), Serviceable Available Market (SAM), and Serviceable Obtainable Market (SOM) for startup opportunities. |
| `micro-saas-launcher` | You ship fast and iterate. You know the difference between a side project and a business. You've seen what works in the indie hacker community. You help people go from idea to paying customers in weeks, not years. You... |
| `monetization` | Estrategia e implementacao de monetizacao para produtos digitais - Stripe, subscriptions, pricing experiments, freemium, upgrade flows, churn prevention, revenue optimization e modelos de negocio SaaS. |
| `pricing-strategy` | Design pricing, packaging, and monetization strategies based on value, customer willingness to pay, and growth objectives. |
| `product-design` | Design de produto nivel Apple — sistemas visuais, UX flows, acessibilidade, linguagem visual proprietaria, design tokens, prototipagem e handoff. Cobre Figma, design systems, tipografia, cor, espacamento, motion desig... |
| `product-inventor` | Product Inventor e Design Alchemist de nivel maximo — combina Product Thinking, Design Systems, UI Engineering, Psicologia Cognitiva, Storytelling e execucao impecavel nivel Jobs/Apple. |
| `product-manager` | Senior PM agent with 6 knowledge domains, 30+ frameworks, 12 templates, and 32 SaaS metrics with formulas. Pure Markdown, zero scripts. |
| `product-manager-toolkit` | Essential tools and frameworks for modern product management, from discovery to delivery. |
| `production-scheduling` | Codified expertise for production scheduling, job sequencing, line balancing, changeover optimisation, and bottleneck resolution in discrete and batch manufacturing. |
| `progressive-estimation` | Estimate AI-assisted and hybrid human+agent development work with research-backed PERT statistics and calibration feedback loops |
| `quality-nonconformance` | Codified expertise for quality control, non-conformance investigation, root cause analysis, corrective action, and supplier quality management in regulated manufacturing. |
| `returns-reverse-logistics` | Codified expertise for returns authorisation, receipt and inspection, disposition decisions, refund processing, fraud detection, and warranty claims management. |
| `saas-mvp-launcher` | Use when planning or building a SaaS MVP from scratch. Provides a structured roadmap covering tech stack, architecture, auth, payments, and launch checklist. |
| `sred-project-organizer` | Take a list of projects and their related documentation, and organize them into the SRED format for submission. |
| `sred-work-summary` | Go back through the previous year of work and create a Notion doc that groups relevant links into projects that can then be documented as SRED projects. |
| `startup-analyst` | Expert startup business analyst specializing in market sizing, financial modeling, competitive analysis, and strategic planning for early-stage companies. |
| `startup-business-analyst-business-case` | Generate comprehensive investor-ready business case document with market, solution, financials, and strategy |
| `startup-business-analyst-financial-projections` | Create detailed 3-5 year financial model with revenue, costs, cash flow, and scenarios |
| `startup-business-analyst-market-opportunity` | Generate comprehensive market opportunity analysis with TAM/SAM/SOM calculations |
| `startup-metrics-framework` | Comprehensive guide to tracking, calculating, and optimizing key performance metrics for different startup business models from seed through Series A. |
| `team-collaboration-issue` | You are a GitHub issue resolution expert specializing in systematic bug investigation, feature implementation, and collaborative development workflows. Your expertise spans issue triage, root cause an |
| `team-collaboration-standup-notes` | You are an expert team communication specialist focused on async-first standup practices, AI-assisted note generation from commit history, and effective remote team coordination patterns. |
| `team-composition-analysis` | Design optimal team structures, hiring plans, compensation strategies, and equity allocation for early-stage startups from pre-seed through Series A. |

### `languages` (41)

Language-specific implementation guidance.

| Skill | What it does |
|---|---|
| `arm-cortex-expert` | Senior embedded software engineer specializing in firmware and driver development for ARM Cortex-M microcontrollers (Teensy, STM32, nRF52, SAMD). |
| `async-python-patterns` | Master Python asyncio, concurrent programming, and async/await patterns for high-performance applications. Use when building async APIs, concurrent systems, or I/O-bound applications requiring non-blocking operations. |
| `bash-defensive-patterns` | Master defensive Bash programming techniques for production-grade scripts. Use when writing robust shell scripts, CI/CD pipelines, or system utilities requiring fault tolerance and safety. |
| `bash-linux` | Bash/Linux terminal patterns. Critical commands, piping, error handling, scripting. Use when working on macOS or Linux systems. |
| `bash-pro` | Master of defensive Bash scripting for production automation, CI/CD pipelines, and system utilities. Expert in safe, portable, and testable shell scripts. |
| `bash-scripting` | Bash scripting workflow for creating production-ready shell scripts with defensive patterns, error handling, and testing. |
| `bats-testing-patterns` | Master Bash Automated Testing System (Bats) for comprehensive shell script testing. Use when writing tests for shell scripts, CI/CD pipelines, or requiring test-driven development of shell utilities. |
| `bun-development` | Fast, modern JavaScript/TypeScript development with the Bun runtime, inspired by [oven-sh/bun](https://github.com/oven-sh/bun). |
| `busybox-on-windows` | How to use a Win32 build of BusyBox to run many of the standard UNIX command line tools on Windows. |
| `c-pro` | Write efficient C code with proper memory management, pointer |
| `cpp-pro` | Write idiomatic C++ code with modern features, RAII, smart pointers, and STL algorithms. Handles templates, move semantics, and performance optimization. |
| `csharp-pro` | Write modern C# code with advanced features like records, pattern matching, and async/await. Optimizes .NET applications, implements enterprise patterns, and ensures comprehensive testing. |
| `elixir-pro` | Write idiomatic Elixir code with OTP patterns, supervision trees, and Phoenix LiveView. Masters concurrency, fault tolerance, and distributed systems. |
| `go-concurrency-patterns` | Master Go concurrency with goroutines, channels, sync primitives, and context. Use when building concurrent Go applications, implementing worker pools, or debugging race conditions. |
| `golang-pro` | Master Go 1.21+ with modern patterns, advanced concurrency, performance optimization, and production-ready microservices. |
| `haskell-pro` | Expert Haskell engineer specializing in advanced type systems, pure |
| `java-pro` | Master Java 21+ with modern features like virtual threads, pattern matching, and Spring Boot 3.x. Expert in the latest Java ecosystem including GraalVM, Project Loom, and cloud-native patterns. |
| `javascript-mastery` | 33+ essential JavaScript concepts every developer should know, inspired by [33-js-concepts](https://github.com/leonardomso/33-js-concepts). |
| `javascript-pro` | Master modern JavaScript with ES6+, async patterns, and Node.js APIs. Handles promises, event loops, and browser/Node compatibility. |
| `javascript-typescript-typescript-scaffold` | You are a TypeScript project architecture expert specializing in scaffolding production-ready Node.js and frontend applications. Generate complete project structures with modern tooling (pnpm, Vite, N |
| `julia-pro` | Master Julia 1.10+ with modern features, performance optimization, multiple dispatch, and production-ready practices. |
| `modern-javascript-patterns` | Comprehensive guide for mastering modern JavaScript (ES6+) features, functional programming patterns, and best practices for writing clean, maintainable, and performant code. |
| `os-scripting` | Operating system and shell scripting troubleshooting workflow for Linux, macOS, and Windows. Covers bash scripting, system administration, debugging, and automation. |
| `php-pro` | Write idiomatic PHP code with generators, iterators, SPL data structures, and modern OOP features. Use PROACTIVELY for high-performance PHP applications. |
| `posix-shell-pro` | Expert in strict POSIX sh scripting for maximum portability across Unix-like systems. Specializes in shell scripts that run on any POSIX-compliant shell (dash, ash, sh, bash --posix). |
| `powershell-windows` | PowerShell Windows patterns. Critical pitfalls, operator syntax, error handling. |
| `python-development-python-scaffold` | You are a Python project architecture expert specializing in scaffolding production-ready Python applications. Generate complete project structures with modern tooling (uv, FastAPI, Django), type hint |
| `python-fastapi-development` | Python FastAPI backend development with async patterns, SQLAlchemy, Pydantic, authentication, and production API patterns. |
| `python-packaging` | Comprehensive guide to creating, structuring, and distributing Python packages using modern packaging tools, pyproject.toml, and publishing to PyPI. |
| `python-patterns` | Python development principles and decision-making. Framework selection, async patterns, type hints, project structure. Teaches thinking, not copying. |
| `python-performance-optimization` | Profile and optimize Python code using cProfile, memory profilers, and performance best practices. Use when debugging slow Python code, optimizing bottlenecks, or improving application performance. |
| `python-pro` | Master Python 3.12+ with modern features, async programming, performance optimization, and production-ready practices. Expert in the latest Python ecosystem including uv, ruff, pydantic, and FastAPI. |
| `ruby-pro` | Write idiomatic Ruby code with metaprogramming, Rails patterns, and performance optimization. Specializes in Ruby on Rails, gem development, and testing frameworks. |
| `rust-async-patterns` | Master Rust async programming with Tokio, async traits, error handling, and concurrent patterns. Use when building async Rust applications, implementing concurrent systems, or debugging async code. |
| `rust-pro` | Master Rust 1.75+ with modern async patterns, advanced type system features, and production-ready systems programming. |
| `scala-pro` | Master enterprise-grade Scala development with functional programming, distributed systems, and big data processing. Expert in Apache Pekko, Akka, Spark, ZIO/Cats Effect, and reactive architectures. |
| `shellcheck-configuration` | Master ShellCheck static analysis configuration and usage for shell script quality. Use when setting up linting infrastructure, fixing code issues, or ensuring script portability. |
| `systems-programming-rust-project` | You are a Rust project architecture expert specializing in scaffolding production-ready Rust applications. Generate complete project structures with cargo tooling, proper module organization, testing |
| `typescript-advanced-types` | Comprehensive guidance for mastering TypeScript's advanced type system including generics, conditional types, mapped types, template literal types, and utility types for building robust, type-safe applications. |
| `typescript-expert` | TypeScript and JavaScript expert with deep knowledge of type-level programming, performance optimization, monorepo management, migration strategies, and modern tooling. |
| `typescript-pro` | Master TypeScript with advanced types, generics, and strict type safety. Handles complex type systems, decorators, and enterprise-grade patterns. |

### `docs-writing` (34)

Docs, changelogs, and technical writing.

| Skill | What it does |
|---|---|
| `applying-brand-guidelines` | This skill applies consistent corporate branding and styling to all generated documents including colors, fonts, layouts, and messaging |
| `avoid-ai-writing` | Audit and rewrite content to remove 21 categories of AI writing patterns with a 43-entry replacement table |
| `beautiful-prose` | A hard-edged writing style contract for timeless, forceful English prose without modern AI tics. Use when users ask for prose or rewrites that must be clean, exact, concrete, and free of AI cadence, filler, or therape... |
| `blog-writing-guide` | This skill enforces Sentry's blog writing standards across every post — whether you're helping an engineer write their first blog post or a marketer draft a product announcement. |
| `brand-guidelines` | Write copy following Sentry brand guidelines. Use when writing UI text, error messages, empty states, onboarding flows, 404 pages, documentation, marketing copy, or any user-facing content. Covers both Plain Speech (d... |
| `brand-guidelines-anthropic` | To access Anthropic's official brand identity and style resources, use this skill. |
| `brand-guidelines-community` | To access Anthropic's official brand identity and style resources, use this skill. |
| `changelog-automation` | Automate changelog generation from commits, PRs, and releases following Keep a Changelog format. Use when setting up release workflows, generating release notes, or standardizing commit conventions. |
| `citation-management` | Manage citations systematically throughout the research and writing process. |
| `code-documentation-code-explain` | You are a code education expert specializing in explaining complex code through clear narratives, visual diagrams, and step-by-step breakdowns. Transform difficult concepts into understandable explanations for develop... |
| `code-documentation-doc-generate` | You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. Generate API docs, architecture diagrams, user guides, and technical references using AI-powered analysis an... |
| `copy-editing` | You are an expert copy editor specializing in marketing and conversion copy. Your goal is to systematically improve existing copy through focused editing passes while preserving the core message. |
| `daily` | Documentation and capabilities reference for Daily |
| `diary` | Unified Diary System: A context-preserving automated logger for multi-project development. |
| `docs-architect` | Creates comprehensive technical documentation from existing codebases. Analyzes architecture, design patterns, and implementation details to produce long-form technical manuals and ebooks. |
| `documentation` | Documentation generation workflow covering API docs, architecture docs, README files, code comments, and technical writing. |
| `documentation-generation-doc-generate` | You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. Generate API docs, architecture diagrams, user guides, and technical references using AI-powered analysis an... |
| `documentation-templates` | Documentation templates and structure guidelines. README, API docs, code comments, and AI-friendly documentation. |
| `email-composer` | Draft professional emails for various contexts including business, technical, and customer communication. Use when the user needs help writing emails or composing professional messages. |
| `explain-like-socrates` | Explains concepts using Socratic-style dialogue. Use when the user asks to explain, teach or help understand a concept like socrates. |
| `internal-comms-anthropic` | To write internal communications, use this skill for: |
| `internal-comms-community` | To write internal communications, use this skill for: |
| `mermaid-expert` | Create Mermaid diagrams for flowcharts, sequences, ERDs, and architectures. Masters syntax for all diagram types and styling. |
| `professional-proofreader` | Use when a user asks to "proofread", "review and correct", "fix grammar", "improve readability while keeping my voice", and to proofread a document file and save an updated version. |
| `readme` | You are an expert technical writer creating comprehensive project documentation. Your goal is to write a README.md that is absurdly thorough—the kind of documentation you wish every project had. |
| `scientific-writing` | This is the core skill for the deep research and writing tool—combining AI-driven deep research with well-formatted written outputs. Every document produced is backed by comprehensive literature search and verified ci... |
| `tutorial-engineer` | Creates step-by-step tutorials and educational content from code. Transforms complex concepts into progressive learning experiences with hands-on examples. |
| `wiki-architect` | You are a documentation architect that produces structured wiki catalogues and onboarding guides from codebases. |
| `wiki-changelog` | Generate structured changelogs from git history. |
| `wiki-onboarding` | Generate two complementary onboarding documents that together give any engineer — from newcomer to principal — a complete understanding of a codebase. |
| `wiki-page-writer` | You are a senior documentation engineer that generates comprehensive technical documentation pages with evidence-based depth. |
| `wiki-qa` | Answer repository questions grounded entirely in source code evidence. |
| `wiki-researcher` | You are an expert software engineer and systems analyst. Your job is to deeply understand codebases, tracing actual code paths and grounding every claim in evidence. |
| `wiki-vitepress` | Transform generated wiki Markdown files into a polished VitePress static site with dark theme and interactive Mermaid diagrams. |

### `testing-qa` (34)

Unit, end-to-end, and review testing.

| Skill | What it does |
|---|---|
| `acceptance-orchestrator` | Use when a coding task should be driven end-to-end from issue intake through implementation, review, deployment, and acceptance verification with minimal human re-intervention. |
| `awt-e2e-testing` | AI-powered E2E web testing — eyes and hands for AI coding tools. Declarative YAML scenarios, Playwright execution, visual matching (OpenCV + OCR), platform auto-detection (Flutter/React/Vue), learning DB. Install: npx... |
| `code-review-ai-ai-review` | You are an expert AI-powered code review specialist combining automated static analysis, intelligent pattern recognition, and modern DevOps practices. Leverage AI tools (GitHub Copilot, Qodo, GPT-5, C |
| `code-review-checklist` | Comprehensive checklist for conducting thorough code reviews covering functionality, security, performance, and maintainability |
| `code-review-excellence` | Transform code reviews from gatekeeping to knowledge sharing through constructive feedback, systematic analysis, and collaborative improvement. |
| `code-reviewer` | Code review automation for TypeScript, JavaScript, Python, Go, Swift, Kotlin. Analyzes PRs for complexity and risk, checks code quality for SOLID violations and code smells, generates review reports. Use when reviewin... |
| `codex-review` | Professional code review with auto CHANGELOG generation, integrated with Codex AI |
| `debug-buttercup` | All pods run in namespace crs. Key services: |
| `e2e-testing` | End-to-end testing workflow with Playwright for browser automation, visual regression, cross-browser testing, and CI/CD integration. |
| `e2e-testing-patterns` | Build reliable, fast, and maintainable end-to-end test suites that provide confidence to ship code quickly and catch regressions before users do. |
| `go-playwright` | Expert capability for robust, stealthy, and efficient browser automation using Playwright Go. |
| `go-rod-master` | Comprehensive guide for browser automation and web scraping with go-rod (Chrome DevTools Protocol) including stealth anti-bot-detection patterns. |
| `javascript-testing-patterns` | Comprehensive guide for implementing robust testing strategies in JavaScript/TypeScript applications using modern testing frameworks and best practices. |
| `k6-load-testing` | Comprehensive k6 load testing skill for API, browser, and scalability testing. Write realistic load scenarios, analyze results, and integrate with CI/CD. |
| `lint-and-validate` | MANDATORY: Run appropriate validation tools after EVERY code change. Do not finish a task until the code is error-free. |
| `performance-testing-review-ai-review` | You are an expert AI-powered code review specialist combining automated static analysis, intelligent pattern recognition, and modern DevOps practices. Leverage AI tools (GitHub Copilot, Qodo, GPT-5, C |
| `performance-testing-review-multi-agent-review` | Use when working with performance testing review multi agent review |
| `playwright-java` | Scaffold, write, debug, and enhance enterprise-grade Playwright E2E tests in Java using Page Object Model, JUnit 5, Allure reporting, and parallel execution. |
| `playwright-skill` | Complete browser automation with Playwright. Auto-detects dev servers, writes clean test scripts to /tmp. Test pages, fill forms, take screenshots, check responsive design, validate UX, test login flows, check links,... |
| `pypict-skill` | Pairwise test generation |
| `python-testing-patterns` | Implement comprehensive testing strategies with pytest, fixtures, mocking, and test-driven development. Use when writing Python tests, setting up test suites, or implementing testing best practices. |
| `tdd-orchestrator` | Master TDD orchestrator specializing in red-green-refactor discipline, multi-agent workflow coordination, and comprehensive test-driven development practices. |
| `tdd-workflow` | Test-Driven Development workflow principles. RED-GREEN-REFACTOR cycle. |
| `tdd-workflows-tdd-cycle` | Use when working with tdd workflows tdd cycle |
| `tdd-workflows-tdd-green` | Implement the minimal code needed to make failing tests pass in the TDD green phase. |
| `tdd-workflows-tdd-red` | Generate failing tests for the TDD red phase to define expected behavior and edge cases. |
| `tdd-workflows-tdd-refactor` | Use when working with tdd workflows tdd refactor |
| `test-automator` | Master AI-powered test automation with modern frameworks, self-healing tests, and comprehensive quality engineering. Build scalable testing strategies with advanced CI/CD integration. |
| `test-driven-development` | Use when implementing any feature or bugfix, before writing implementation code |
| `test-fixing` | Systematically identify and fix all failing tests using smart grouping strategies. |
| `testing-patterns` | Jest testing patterns, factory functions, mocking strategies, and TDD workflow. Use when writing unit tests, creating test factories, or following TDD red-green-refactor cycle. |
| `testing-qa` | Comprehensive testing and QA workflow covering unit testing, integration testing, E2E testing, browser automation, and quality assurance. |
| `unit-testing-test-generate` | Generate comprehensive, maintainable unit tests across languages with strong coverage and edge case focus. |
| `webapp-testing` | To test local web applications, write native Python Playwright scripts. |

### `skills-meta` (32)

Authoring, routing, and checking other skills.

| Skill | What it does |
|---|---|
| `behavioral-modes` | AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). Use to adapt behavior based on task type. |
| `claude-code-expert` | Especialista profundo em Claude Code - CLI da Anthropic. Maximiza produtividade com atalhos, hooks, MCPs, configuracoes avancadas, workflows, CLAUDE.md, memoria, sub-agentes, permissoes e integracao com ecossistemas. |
| `claude-code-guide` | To provide a comprehensive reference for configuring and using Claude Code (the agentic coding tool) to its full potential. This skill synthesizes best practices, configuration templates, and advanced usage patterns. |
| `claude-d3js-skill` | This skill provides guidance for creating sophisticated, interactive data visualisations using d3.js. |
| `claude-in-chrome-troubleshooting` | Diagnose and fix Claude in Chrome MCP extension connectivity issues. Use when mcp__claude-in-chrome__* tools fail, return "Browser extension is not connected", or behave erratically. |
| `claude-monitor` | Monitor de performance do Claude Code e sistema local. Diagnostica lentidao, mede CPU/RAM/disco, verifica API latency e gera relatorios de saude do sistema. |
| `claude-scientific-skills` | Scientific research and analysis skills |
| `claude-settings-audit` | Analyze a repository to generate recommended Claude Code settings.json permissions. Use when setting up a new project, auditing existing settings, or determining which read-only bash commands to allow. Detects tech st... |
| `claude-win11-speckit-update-skill` | Windows 11 system management |
| `mcp-builder` | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or service... |
| `mcp-builder-ms` | Use this skill when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK). |
| `plugin-settings` | This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin set... |
| `recallmax` | FREE — God-tier long-context memory for AI agents. Injects 500K-1M clean tokens, auto-summarizes with tone/intent preservation, compresses 14-turn history into 800 tokens. |
| `remembering-conversations` | Search previous Claude Code conversations for facts, patterns, decisions, and context using semantic or text search |
| `skill-check` | Validate Claude Code skills against the agentskills specification. Catches structural, semantic, and naming issues before users do. |
| `skill-creator` | Guide for creating effective skills. Use when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations. |
| `skill-creator-ms` | Guide for creating effective skills for AI coding agents working with Azure SDKs and Microsoft Foundry services. Use when creating new skills or updating existing skills. |
| `skill-developer` | Comprehensive guide for creating and managing skills in Claude Code with auto-activation system, following Anthropic's official best practices including the 500-line rule and progressive disclosure pattern. |
| `skill-development` | This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill structure, progressive... |
| `skill-improver` | Iteratively improve a Claude Code skill using the skill-reviewer agent until it meets quality standards. |
| `skill-installer` | Instala, valida, registra e verifica novas skills no ecossistema. 10 checks de seguranca, copia, registro no orchestrator e verificacao pos-instalacao. |
| `skill-rails-upgrade` | Analyze Rails apps and provide upgrade assessments |
| `skill-router` | Use when the user is unsure which skill to use or where to start. Interviews the user with targeted questions and recommends the best skill(s) from the installed library for their goal. |
| `skill-scanner` | Scan agent skills for security issues before adoption. Detects prompt injection, malicious code, excessive permissions, secret exposure, and supply chain risks. |
| `skill-seekers` | -Automatically convert documentation websites, GitHub repositories, and PDFs into Claude AI skills in minutes. |
| `skill-sentinel` | Auditoria e evolucao do ecossistema de skills. Qualidade de codigo, seguranca, custos, gaps, duplicacoes, dependencias e relatorios de saude. |
| `skill-writer` | Guide users through creating Agent Skills for Claude Code. Use when the user wants to create, write, author, or design a new Skill, or needs help with SKILL.md files, frontmatter, or skill structure. |
| `skills-discovery` | Search for and install Agent Skills that give you specialized capabilities. Before starting work, ask might a skill exist that handles this better than my base knowledge? If the task involves specific technologies, fr... |
| `superpowers-lab` | Lab environment for Claude superpowers |
| `tool-design` | Build tools that agents can use effectively, including architectural reduction patterns |
| `tool-use-guardian` | FREE — Intelligent tool-call reliability wrapper. Monitors, retries, fixes, and learns from tool failures. Auto-recovers from truncated JSON, timeouts, rate limits, and mid-chain failures. |
| `writing-skills` | Use when creating, updating, or improving agent skills. |

### `database` (27)

SQL, migrations, and data stores.

| Skill | What it does |
|---|---|
| `algolia-search` | Expert patterns for Algolia search implementation, indexing strategies, React InstantSearch, and relevance tuning Use when: adding search to, algolia, instantsearch, search api, search functionality. |
| `cc-skill-clickhouse-io` | ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-performance analytical workloads. |
| `claimable-postgres` | Provision instant temporary Postgres databases via Claimable Postgres by Neon (pg.new). No login or credit card required. Use for quick Postgres environments and throwaway DATABASE_URL for prototyping. |
| `database` | Database development and operations workflow covering SQL, NoSQL, database design, migrations, optimization, and data engineering. |
| `database-admin` | Expert database administrator specializing in modern cloud databases, automation, and reliability engineering. |
| `database-architect` | Expert database architect specializing in data layer design from scratch, technology selection, schema modeling, and scalable database architectures. |
| `database-cloud-optimization-cost-optimize` | You are a cloud cost optimization expert specializing in reducing infrastructure expenses while maintaining performance and reliability. Analyze cloud spending, identify savings opportunities, and implement cost-effec... |
| `database-design` | Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases. |
| `database-migration` | Master database schema and data migrations across ORMs (Sequelize, TypeORM, Prisma), including rollback strategies and zero-downtime deployments. |
| `database-migrations-migration-observability` | Migration monitoring, CDC, and observability infrastructure |
| `database-migrations-sql-migrations` | SQL database migrations with zero-downtime strategies for PostgreSQL, MySQL, and SQL Server. Focus on data integrity and rollback plans. |
| `database-optimizer` | Expert database optimizer specializing in modern performance tuning, query optimization, and scalable architectures. |
| `drizzle-orm-expert` | Expert in Drizzle ORM for TypeScript — schema design, relational queries, migrations, and serverless database integration. Use when building type-safe database layers with Drizzle. |
| `embedding-strategies` | Guide to selecting and optimizing embedding models for vector search applications. |
| `hybrid-search-implementation` | Combine vector and keyword search for improved retrieval. Use when implementing RAG systems, building search engines, or when neither approach alone provides sufficient recall. |
| `neon-postgres` | Configure Prisma for Neon with connection pooling. |
| `nosql-expert` | Expert guidance for distributed NoSQL databases (Cassandra, DynamoDB). Focuses on mental models, query-first modeling, single-table design, and avoiding hot partitions in high-scale systems. |
| `postgres-best-practices` | Postgres performance optimization and best practices from Supabase. Use this skill when writing, reviewing, or optimizing Postgres queries, schema designs, or database configurations. |
| `postgresql` | Design a PostgreSQL-specific schema. Covers best-practices, data types, indexing, constraints, performance patterns, and advanced features |
| `postgresql-optimization` | PostgreSQL database optimization workflow for query tuning, indexing strategies, performance analysis, and production database management. |
| `prisma-expert` | You are an expert in Prisma ORM with deep knowledge of schema design, migrations, query optimization, relations modeling, and database operations across PostgreSQL, MySQL, and SQLite. |
| `similarity-search-patterns` | Implement efficient similarity search with vector databases. Use when building semantic search, implementing nearest neighbor queries, or optimizing retrieval performance. |
| `sql-optimization-patterns` | Transform slow database queries into lightning-fast operations through systematic optimization, proper indexing, and query plan analysis. |
| `sql-pro` | Master modern SQL with cloud-native databases, OLTP/OLAP optimization, and advanced query techniques. Expert in performance tuning, data modeling, and hybrid analytical systems. |
| `using-neon` | Neon is a serverless Postgres platform that separates compute and storage to offer autoscaling, branching, instant restore, and scale-to-zero. It's fully compatible with Postgres and works with any language, framework... |
| `vector-database-engineer` | Expert in vector databases, embedding strategies, and semantic search implementation. Masters Pinecone, Weaviate, Qdrant, Milvus, and pgvector for RAG applications, recommendation systems, and similar |
| `vector-index-tuning` | Optimize vector index performance for latency, recall, and memory. Use when tuning HNSW parameters, selecting quantization strategies, or scaling vector search infrastructure. |

### `architecture-patterns` (25)

DDD, CQRS, ADRs, and system design.

| Skill | What it does |
|---|---|
| `architect-review` | Master software architect specializing in modern architecture |
| `architecture` | Architectural decision-making framework. Requirements analysis, trade-off evaluation, ADR documentation. Use when making architecture decisions or analyzing system design. |
| `architecture-decision-records` | Comprehensive patterns for creating, maintaining, and managing Architecture Decision Records (ADRs) that capture the context and rationale behind significant technical decisions. |
| `architecture-diagrams` | Create system architecture diagrams using Mermaid, PlantUML, C4 model, flowcharts, and sequence diagrams. Use when documenting architecture, system design, data flows, or technical workflows. |
| `architecture-patterns` | Implement proven backend architecture patterns including Clean Architecture, Hexagonal Architecture, and Domain-Driven Design. Use when architecting complex backend systems or refactoring existing applications for bet... |
| `c4-architecture-c4-architecture` | Generate comprehensive C4 architecture documentation for an existing repository/codebase using a bottom-up analysis approach. |
| `c4-code` | Expert C4 Code-level documentation specialist. Analyzes code directories to create comprehensive C4 code-level documentation including function signatures, arguments, dependencies, and code structure. |
| `c4-component` | Expert C4 Component-level documentation specialist. Synthesizes C4 Code-level documentation into Component-level architecture, defining component boundaries, interfaces, and relationships. |
| `c4-container` | Expert C4 Container-level documentation specialist. |
| `c4-context` | Expert C4 Context-level documentation specialist. Creates high-level system context diagrams, documents personas, user journeys, system features, and external dependencies. |
| `clean-code` | This skill embodies the principles of "Clean Code" by Robert C. Martin (Uncle Bob). Use it to transform "code that works" into "code that is clean." |
| `cqrs-implementation` | Implement Command Query Responsibility Segregation for scalable architectures. Use when separating read and write models, optimizing query performance, or building event-sourced systems. |
| `ddd-context-mapping` | Map relationships between bounded contexts and define integration contracts using DDD context mapping patterns. |
| `ddd-strategic-design` | Design DDD strategic artifacts including subdomains, bounded contexts, and ubiquitous language for complex business domains. |
| `ddd-tactical-patterns` | Apply DDD tactical patterns in code using entities, value objects, aggregates, repositories, and domain events with explicit invariants. |
| `domain-driven-design` | Plan and route Domain-Driven Design work from strategic modeling to tactical implementation and evented architecture patterns. |
| `event-sourcing-architect` | Expert in event sourcing, CQRS, and event-driven architecture patterns. Masters event store design, projection building, saga orchestration, and eventual consistency patterns. Use PROACTIVELY for event-sourced systems... |
| `event-store-design` | Design and implement event stores for event-sourced systems. Use when building event sourcing infrastructure, choosing event store technologies, or implementing event persistence patterns. |
| `saga-orchestration` | Patterns for managing distributed transactions and long-running business processes. |
| `senior-architect` | This skill should be used when the user asks to "design system architecture", "evaluate microservices vs monolith", "create architecture diagrams", "analyze dependencies", "choose a database", "plan for scalability",... |
| `software-architecture` | Guide for quality focused software architecture. This skill should be used when users want to write code, design architecture, analyze code, in any case that relates to software development. |
| `uncle-bob-craft` | Use when performing code review, writing or refactoring code, or discussing architecture; complements clean-code and does not replace project linter/formatter. |
| `workflow-automation` | You are a workflow automation architect who has seen both the promise and the pain of these platforms. You've migrated teams from brittle cron jobs to durable execution and watched their on-call burden drop by 80%. |
| `workflow-orchestration-patterns` | Master workflow orchestration architecture with Temporal, covering fundamental design decisions, resilience patterns, and best practices for building reliable distributed systems. |
| `workflow-patterns` | Use this skill when implementing tasks according to Conductor's TDD workflow, handling phase checkpoints, managing git commits for tasks, or understanding the verification protocol. |

### `payments-fintech` (25)

Billing, Stripe, and payments compliance.

| Skill | What it does |
|---|---|
| `alpha-vantage` | Access 20+ years of global financial data: equities, options, forex, crypto, commodities, economic indicators, and 50+ technical indicators. |
| `backtesting-frameworks` | Build robust, production-grade backtesting systems that avoid common pitfalls and produce reliable strategy performance estimates. |
| `billing-automation` | Master automated billing systems including recurring billing, invoice generation, dunning management, proration, and tax calculation. |
| `blockchain-developer` | Build production-ready Web3 applications, smart contracts, and decentralized systems. Implements DeFi protocols, NFT platforms, DAOs, and enterprise blockchain integrations. |
| `creating-financial-models` | This skill provides an advanced financial modeling suite with DCF analysis, sensitivity testing, Monte Carlo simulations, and scenario planning for investment decisions |
| `crypto-bd-agent` | Production-tested patterns for building AI agents that autonomously discover, > evaluate, and acquire token listings for cryptocurrency exchanges. |
| `defi-protocol-templates` | Implement DeFi protocols with production-ready templates for staking, AMMs, governance, and lending systems. Use when building decentralized finance applications or smart contract protocols. |
| `emblemai-crypto-wallet` | Crypto wallet management across 7 blockchains via EmblemAI Agent Hustle API. Balance checks, token swaps, portfolio analysis, and transaction execution for Solana, Ethereum, Base, BSC, Polygon, Hedera, and Bitcoin. |
| `goldrush-api` | Query blockchain data across 100+ chains: wallet balances, token prices, transactions, DEX pairs, and real-time OHLCV streams via the GoldRush API by Covalent. |
| `lightning-architecture-review` | Review Bitcoin Lightning Network protocol designs, compare channel factory approaches, and analyze Layer 2 scaling tradeoffs. Covers trust models, on-chain footprint, consensus requirements, HTLC/PTLC compatibility, l... |
| `lightning-channel-factories` | Technical reference on Lightning Network channel factories, multi-party channels, LSP architectures, and Bitcoin Layer 2 scaling without soft forks. Covers Decker-Wattenhofer, timeout trees, MuSig2 key aggregation, HT... |
| `lightning-factory-explainer` | Explain Bitcoin Lightning channel factories and the SuperScalar protocol — scalable Lightning onboarding using shared UTXOs, Decker-Wattenhofer trees, timeout-signature trees, MuSig2, and Taproot. No soft fork required. |
| `nft-standards` | Master ERC-721 and ERC-1155 NFT standards, metadata best practices, and advanced NFT features. |
| `pakistan-payments-stack` | Design and implement production-grade Pakistani payment integrations (JazzCash, Easypaisa, bank/PSP rails, optional Raast) for SaaS with PKR billing, webhook reliability, and reconciliation. |
| `payment-integration` | Integrate Stripe, PayPal, and payment processors. Handles checkout flows, subscriptions, webhooks, and PCI compliance. Use PROACTIVELY when implementing payments, billing, or subscription features. |
| `paypal-integration` | Master PayPal payment integration including Express Checkout, IPN handling, recurring billing, and refund workflows. |
| `pci-compliance` | Master PCI DSS (Payment Card Industry Data Security Standard) compliance for secure payment processing and handling of cardholder data. |
| `plaid-fintech` | Create a linktoken for Plaid Link, exchange publictoken for accesstoken. Link tokens are short-lived, one-time use. Access tokens don't expire but may need updating when users change passwords. |
| `quant-analyst` | Build financial models, backtest trading strategies, and analyze market data. Implements risk metrics, portfolio optimization, and statistical arbitrage. |
| `risk-manager` | Monitor portfolio risk, R-multiples, and position limits. Creates hedging strategies, calculates expectancy, and implements stop-losses. |
| `risk-metrics-calculation` | Calculate portfolio risk metrics including VaR, CVaR, Sharpe, Sortino, and drawdown analysis. Use when measuring portfolio risk, implementing risk limits, or building risk monitoring systems. |
| `solidity-security` | Master smart contract security best practices, vulnerability prevention, and secure Solidity development patterns. |
| `startup-financial-modeling` | Build comprehensive 3-5 year financial models with revenue projections, cost structures, cash flow analysis, and scenario planning for early-stage startups. |
| `stripe-automation` | Automate Stripe tasks via Rube MCP (Composio): customers, charges, subscriptions, invoices, products, refunds. Always search tools first for current schemas. |
| `stripe-integration` | Master Stripe payment processing integration for robust, PCI-compliant payment flows including checkout, subscriptions, webhooks, and refunds. |

### `odoo` (24)

Odoo modules, ORM, and deployment.

| Skill | What it does |
|---|---|
| `odoo-accounting-setup` | Expert guide for configuring Odoo Accounting: chart of accounts, journals, fiscal positions, taxes, payment terms, and bank reconciliation. |
| `odoo-automated-tests` | Write and run Odoo automated tests using TransactionCase, HttpCase, and browser tour tests. Covers test data setup, mocking, and CI integration. |
| `odoo-backup-strategy` | Complete Odoo backup and restore strategy: database dumps, filestore backup, automated scheduling, cloud storage upload, and tested restore procedures. |
| `odoo-docker-deployment` | Production-ready Docker and docker-compose setup for Odoo with PostgreSQL, persistent volumes, environment-based configuration, and Nginx reverse proxy. |
| `odoo-ecommerce-configurator` | Expert guide for Odoo eCommerce and Website: product catalog, payment providers, shipping methods, SEO, and order-to-fulfillment workflow. |
| `odoo-edi-connector` | Guide for implementing EDI (Electronic Data Interchange) with Odoo: X12, EDIFACT document mapping, partner onboarding, and automated order processing. |
| `odoo-hr-payroll-setup` | Expert guide for Odoo HR and Payroll: salary structures, payslip rules, leave policies, employee contracts, and payroll journal entries. |
| `odoo-inventory-optimizer` | Expert guide for Odoo Inventory: stock valuation (FIFO/AVCO), reordering rules, putaway strategies, routes, and multi-warehouse configuration. |
| `odoo-l10n-compliance` | Country-specific Odoo localization: tax configuration, e-invoicing (CFDI, FatturaPA, SAF-T), fiscal reporting, and country chart of accounts setup. |
| `odoo-manufacturing-advisor` | Expert guide for Odoo Manufacturing: Bills of Materials (BoM), Work Centers, routings, MRP planning, and production order workflows. |
| `odoo-migration-helper` | Step-by-step guide for migrating Odoo custom modules between versions (v14→v15→v16→v17). Covers API changes, deprecated methods, and view migration. |
| `odoo-module-developer` | Expert guide for creating custom Odoo modules. Covers __manifest__.py, model inheritance, ORM patterns, and module structure best practices. |
| `odoo-orm-expert` | Master Odoo ORM patterns: search, browse, create, write, domain filters, computed fields, and performance-safe query techniques. |
| `odoo-performance-tuner` | Expert guide for diagnosing and fixing Odoo performance issues: slow queries, worker configuration, memory limits, PostgreSQL tuning, and profiling tools. |
| `odoo-project-timesheet` | Expert guide for Odoo Project and Timesheets: task stages, billable time tracking, timesheet approval, budget alerts, and invoicing from timesheets. |
| `odoo-purchase-workflow` | Expert guide for Odoo Purchase: RFQ → PO → Receipt → Vendor Bill workflow, purchase agreements, vendor price lists, and 3-way matching. |
| `odoo-qweb-templates` | Expert in Odoo QWeb templating for PDF reports, email templates, and website pages. Covers t-if, t-foreach, t-field, and report actions. |
| `odoo-rpc-api` | Expert on Odoo's external JSON-RPC and XML-RPC APIs. Covers authentication, model calls, record CRUD, and real-world integration examples in Python, JavaScript, and curl. |
| `odoo-sales-crm-expert` | Expert guide for Odoo Sales and CRM: pipeline stages, quotation templates, pricelists, sales teams, lead scoring, and forecasting. |
| `odoo-security-rules` | Expert in Odoo access control: ir.model.access.csv, record rules (ir.rule), groups, and multi-company security patterns. |
| `odoo-shopify-integration` | Connect Odoo with Shopify: sync products, inventory, orders, and customers using the Shopify API and Odoo's external API or connector modules. |
| `odoo-upgrade-advisor` | Step-by-step Odoo version upgrade advisor: pre-upgrade checklist, community vs enterprise upgrade path, OCA module compatibility, and post-upgrade validation. |
| `odoo-woocommerce-bridge` | Sync Odoo with WooCommerce: products, inventory, orders, and customers via WooCommerce REST API and Odoo external API. |
| `odoo-xml-views-builder` | Expert at building Odoo XML views: Form, List, Kanban, Search, Calendar, and Graph. Generates correct XML for Odoo 14-17 with proper visibility syntax. |

### `game-dev` (19)

Game engines and game-development workflows.

| Skill | What it does |
|---|---|
| `2d-games` | 2D game development principles. Sprites, tilemaps, physics, camera. |
| `3d-games` | 3D game development principles. Rendering, shaders, physics, cameras. |
| `bevy-ecs-expert` | Master Bevy's Entity Component System (ECS) in Rust, covering Systems, Queries, Resources, and parallel scheduling. |
| `game-art` | Game art principles. Visual style selection, asset pipeline, animation workflow. |
| `game-audio` | Game audio principles. Sound design, music integration, adaptive audio systems. |
| `game-design` | Game design principles. GDD structure, balancing, player psychology, progression. |
| `game-development` | Game development orchestrator. Routes to platform-specific skills based on project needs. |
| `godot-4-migration` | Specialized guide for migrating Godot 3.x projects to Godot 4 (GDScript 2.0), covering syntax changes, Tweens, and exports. |
| `godot-gdscript-patterns` | Master Godot 4 GDScript patterns including signals, scenes, state machines, and optimization. Use when building Godot games, implementing game systems, or learning GDScript best practices. |
| `minecraft-bukkit-pro` | Master Minecraft server plugin development with Bukkit, Spigot, and Paper APIs. |
| `mobile-games` | Mobile game development principles. Touch input, battery, performance, app stores. |
| `multiplayer` | Multiplayer game development principles. Architecture, networking, synchronization. |
| `pc-games` | PC and console game development principles. Engine selection, platform features, optimization strategies. |
| `shader-programming-glsl` | Expert guide for writing efficient GLSL shaders (Vertex/Fragment) for web and game engines, covering syntax, uniforms, and common effects. |
| `unity-developer` | Build Unity games with optimized C# scripts, efficient rendering, and proper asset management. Masters Unity 6 LTS, URP/HDRP pipelines, and cross-platform deployment. |
| `unity-ecs-patterns` | Production patterns for Unity's Data-Oriented Technology Stack (DOTS) including Entity Component System, Job System, and Burst Compiler. |
| `unreal-engine-cpp-pro` | Expert guide for Unreal Engine 5.x C++ development, covering UObject hygiene, performance patterns, and best practices. |
| `vr-ar` | VR/AR development principles. Comfort, interaction, performance requirements. |
| `web-games` | Web browser game development principles. Framework selection, WebGPU, optimization, PWA. |

### `health-wellness` (19)

Health and wellness domain helpers.

| Skill | What it does |
|---|---|
| `claude-ally-health` | A health assistant skill for medical information analysis, symptom tracking, and wellness guidance. |
| `emergency-card` | 生成紧急情况下快速访问的医疗信息摘要卡片。当用户需要旅行、就诊准备、紧急情况或询问"紧急信息"、"医疗卡片"、"急救信息"时使用此技能。提取关键信息（过敏、用药、急症、植入物），支持多格式输出（JSON、文本、二维码），用于急救或快速就医。 |
| `family-health-analyzer` | 分析家族病史、评估遗传风险、识别家庭健康模式、提供个性化预防建议 |
| `fitness-analyzer` | 分析运动数据、识别运动模式、评估健身进展，并提供个性化训练建议。支持与慢性病数据的关联分析。 |
| `food-database-query` | Food Database Query |
| `goal-analyzer` | 分析健康目标数据、识别目标模式、评估目标进度,并提供个性化目标管理建议。支持与营养、运动、睡眠等健康数据的关联分析。 |
| `health-trend-analyzer` | 分析一段时间内健康数据的趋势和模式。关联药物、症状、生命体征、化验结果和其他健康指标的变化。识别令人担忧的趋势、改善情况，并提供数据驱动的洞察。当用户询问健康趋势、模式、随时间的变化或"我的健康状况有什么变化？"时使用。支持多维度分析（体重/BMI、症状、药物依从性、化验结果、情绪睡眠），相关性分析，变化检测，以及交互式HTML可视化报告（ECharts图表）。 |
| `mental-health-analyzer` | 分析心理健康数据、识别心理模式、评估心理健康状况、提供个性化心理健康建议。支持与睡眠、运动、营养等其他健康数据的关联分析。 |
| `nutrition-analyzer` | 分析营养数据、识别营养模式、评估营养状况，并提供个性化营养建议。支持与运动、睡眠、慢性病数据的关联分析。 |
| `occupational-health-analyzer` | 分析职业健康数据、识别工作相关健康风险、评估职业健康状况、提供个性化职业健康建议。支持与睡眠、运动、心理健康等其他健康数据的关联分析。 |
| `oral-health-analyzer` | 分析口腔健康数据、识别口腔问题模式、评估口腔健康状况、提供个性化口腔健康建议。支持与营养、慢性病、用药等其他健康数据的关联分析。 |
| `rehabilitation-analyzer` | 分析康复训练数据、识别康复模式、评估康复进展，并提供个性化康复建议 |
| `sexual-health-analyzer` | Sexual Health Analyzer |
| `skin-health-analyzer` | Analyze skin health data, identify skin problem patterns, assess skin health status. Supports correlation analysis with nutrition, chronic diseases, and medication data. |
| `sleep-analyzer` | 分析睡眠数据、识别睡眠模式、评估睡眠质量，并提供个性化睡眠改善建议。支持与其他健康数据的关联分析。 |
| `tcm-constitution-analyzer` | 分析中医体质数据、识别体质类型、评估体质特征,并提供个性化养生建议。支持与营养、运动、睡眠等健康数据的关联分析。 |
| `travel-health-analyzer` | 分析旅行健康数据、评估目的地健康风险、提供疫苗接种建议、生成多语言紧急医疗信息卡片。支持WHO/CDC数据集成的专业级旅行健康风险评估。 |
| `weightloss-analyzer` | 分析减肥数据、计算代谢率、追踪能量缺口、管理减肥阶段 |
| `wellally-tech` | Integrate multiple digital health data sources, connect to [WellAlly.tech](https://www.wellally.tech/) knowledge base, providing data import and knowledge reference for personal health management systems. |

### `context-memory` (18)

Context windows, memory, and session restore.

| Skill | What it does |
|---|---|
| `agent-memory-mcp` | A hybrid memory system that provides persistent, searchable knowledge management for AI agents (Architecture, Patterns, Decisions). |
| `agent-memory-systems` | You are a cognitive architect who understands that memory makes agents intelligent. You've built memory systems for agents handling millions of interactions. You know that the hard part isn't storing - it's retrieving... |
| `context-agent` | Agente de contexto para continuidade entre sessoes. Salva resumos, decisoes, tarefas pendentes e carrega briefing automatico na sessao seguinte. |
| `context-compression` | When agent sessions generate millions of tokens of conversation history, compression becomes mandatory. The naive approach is aggressive compression to minimize tokens per request. |
| `context-degradation` | Language models exhibit predictable degradation patterns as context length increases. Understanding these patterns is essential for diagnosing failures and designing resilient systems. |
| `context-driven-development` | Guide for implementing and maintaining context as a managed artifact alongside code, enabling consistent AI interactions and team alignment through structured project documentation. |
| `context-fundamentals` | Context is the complete state available to a language model at inference time. It includes everything the model can attend to when generating responses: system instructions, tool definitions, retrieved documents, mess... |
| `context-guardian` | Guardiao de contexto que preserva dados criticos antes da compactacao automatica. Snapshots, verificacao de integridade e zero perda de informacao. |
| `context-management-context-restore` | Use when working with context management context restore |
| `context-management-context-save` | Use when working with context management context save |
| `context-manager` | Elite AI context engineering specialist mastering dynamic context management, vector databases, knowledge graphs, and intelligent memory systems. |
| `context-optimization` | Context optimization extends the effective capacity of limited context windows through strategic compression, masking, caching, and partitioning. The goal is not to magically increase context windows but to make bette... |
| `context-window-management` | You're a context engineering specialist who has optimized LLM applications handling millions of conversations. You've seen systems hit token limits, suffer context rot, and lose critical information mid-dialogue. |
| `context7-auto-research` | Automatically fetch latest library/framework documentation for Claude Code via Context7 API |
| `conversation-memory` | Persistent memory systems for LLM conversations including short-term, long-term, and entity-based memory Use when: conversation memory, remember, memory persistence, long-term memory, chat history. |
| `filesystem-context` | Use for file-based context management, dynamic context discovery, and reducing context window bloat. Offload context to files for just-in-time loading. |
| `hierarchical-agent-memory` | Scoped CLAUDE.md memory system that reduces context token spend. Creates directory-level context files, tracks savings via dashboard, and routes agents to the right sub-context. |
| `memory-systems` | Design short-term, long-term, and graph-based memory architectures |

### `miscellaneous` (17)

Skills that do not fit another category, including LibreOffice.

| Skill | What it does |
|---|---|
| `analyze-project` | Forensic root cause analyzer for Antigravity sessions. Classifies scope deltas, rework patterns, root causes, hotspots, and auto-improves prompts/health. |
| `dwarf-expert` | Provides expertise for analyzing DWARF debug files and understanding the DWARF debug format/standard (v3-v5). Triggers when understanding DWARF information, interacting with DWARF files, answering DWARF-related questi... |
| `evolution` | This skill enables makepad-skills to self-improve continuously during development. |
| `infinite-gratitude` | Multi-agent research skill for parallel research execution (10 agents, battle-tested with real case studies). |
| `libreoffice-base` | Database management, forms, reports, and data operations with LibreOffice Base. |
| `libreoffice-calc` | Spreadsheet creation, format conversion (ODS/XLSX/CSV), formulas, data automation with LibreOffice Calc. |
| `libreoffice-draw` | Vector graphics and diagram creation, format conversion (ODG/SVG/PDF) with LibreOffice Draw. |
| `libreoffice-impress` | Presentation creation, format conversion (ODP/PPTX/PDF), slide automation with LibreOffice Impress. |
| `libreoffice-writer` | Document creation, format conversion (ODT/DOCX/PDF), mail merge, and automation with LibreOffice Writer. |
| `molykit` | CRITICAL: Use for MolyKit AI chat toolkit. Triggers on: BotClient, OpenAI, SSE streaming, AI chat, molykit, PlatformSend, spawn(), ThreadToken, cross-platform async, Chat widget, Messages, PromptInput, Avatar, LLM |
| `moodle-external-api-development` | This skill guides you through creating custom external web service APIs for Moodle LMS, following Moodle's external API framework and coding standards. |
| `nerdzao-elite` | Senior Elite Software Engineer (15+) and Senior Product Designer. Full workflow with planning, architecture, TDD, clean code, and pixel-perfect UX validation. |
| `nerdzao-elite-gemini-high` | Modo Elite Coder + UX Pixel-Perfect otimizado especificamente para Gemini 3.1 Pro High. Workflow completo com foco em qualidade máxima e eficiência de tokens. |
| `projection-patterns` | Build read models and projections from event streams. Use when implementing CQRS read sides, building materialized views, or optimizing query performance in event-sourced systems. |
| `reference-builder` | Creates exhaustive technical references and API documentation. Generates comprehensive parameter listings, configuration guides, and searchable reference materials. |
| `sankhya-dashboard-html-jsp-custom-best-pratices` | This skill should be used when the user asks for patterns, best practices, creation, or fixing of Sankhya dashboards using HTML, JSP, Java, and SQL. |
| `sharp-edges` | sharp-edges |

### `functional-programming` (15)

fp-ts and typed functional patterns.

| Skill | What it does |
|---|---|
| `fp-async` | Practical async patterns using TaskEither - clean pipelines instead of try/catch hell, with real API examples |
| `fp-backend` | Functional programming patterns for Node.js/Deno backend development using fp-ts, ReaderTaskEither, and functional dependency injection |
| `fp-data-transforms` | Everyday data transformations using functional patterns - arrays, objects, grouping, aggregation, and null-safe access |
| `fp-either-ref` | Quick reference for Either type. Use when user needs error handling, validation, or operations that can fail with typed errors. |
| `fp-errors` | Stop throwing everywhere - handle errors as values using Either and TaskEither for cleaner, more predictable code |
| `fp-option-ref` | Quick reference for Option type. Use when user needs to handle nullable values, optional data, or wants to avoid null checks. |
| `fp-pipe-ref` | Quick reference for pipe and flow. Use when user needs to chain functions, compose operations, or build data pipelines in fp-ts. |
| `fp-pragmatic` | A practical, jargon-free guide to functional programming - the 80/20 approach that gets results without the academic overhead |
| `fp-react` | Practical patterns for using fp-ts with React - hooks, state, forms, data fetching. Works with React 18/19, Next.js 14/15. |
| `fp-refactor` | Comprehensive guide for refactoring imperative TypeScript code to fp-ts functional patterns |
| `fp-taskeither-ref` | Quick reference for TaskEither. Use when user needs async error handling, API calls, or Promise-based operations that can fail. |
| `fp-ts-errors` | Handle errors as values using fp-ts Either and TaskEither for cleaner, more predictable TypeScript code. Use when implementing error handling patterns with fp-ts. |
| `fp-ts-pragmatic` | A practical, jargon-free guide to fp-ts functional programming - the 80/20 approach that gets results without the academic overhead. Use when writing TypeScript with fp-ts library. |
| `fp-ts-react` | Practical patterns for using fp-ts with React - hooks, state, forms, data fetching. Use when building React apps with functional programming patterns. Works with React 18/19, Next.js 14/15. |
| `fp-types-ref` | Quick reference for fp-ts types. Use when user asks which type to use, needs Option/Either/Task decision help, or wants fp-ts imports. |

### `scientific-computing` (15)

Python scientific stack and related libraries.

| Skill | What it does |
|---|---|
| `astropy` | Astropy is the core Python package for astronomy, providing essential functionality for astronomical research and data analysis. |
| `biopython` | Biopython is a comprehensive set of freely available Python tools for biological computation. It provides functionality for sequence manipulation, file I/O, database access, structural bioinformatics, phylogenetics, a... |
| `cirq` | Cirq is Google Quantum AI's open-source framework for designing, simulating, and running quantum circuits on quantum computers and simulators. |
| `matplotlib` | Matplotlib is Python's foundational visualization library for creating static, animated, and interactive plots. |
| `networkx` | NetworkX is a Python package for creating, manipulating, and analyzing complex networks and graphs. |
| `plotly` | Interactive visualization library. Use when you need hover info, zoom, pan, or web-embeddable charts. Best for dashboards, exploratory analysis, and presentations. For static publication figures use matplotlib or scie... |
| `polars` | Fast in-memory DataFrame library for datasets that fit in RAM. Use when pandas is too slow but data still fits in memory. Lazy evaluation, parallel execution, Apache Arrow backend. Best for 1-100GB datasets, ETL pipel... |
| `pubmed-database` | Direct REST API access to PubMed. Advanced Boolean/MeSH queries, E-utilities API, batch processing, citation management. For Python workflows, prefer biopython (Bio.Entrez). Use this for direct HTTP/REST work or custo... |
| `qiskit` | Qiskit is the world's most popular open-source quantum computing framework with 13M+ downloads. Build quantum circuits, optimize for hardware, execute on simulators or real quantum computers, and analyze results. Supp... |
| `scanpy` | Scanpy is a scalable Python toolkit for analyzing single-cell RNA-seq data, built on AnnData. Apply this skill for complete single-cell workflows including quality control, normalization, dimensionality reduction, clu... |
| `scikit-learn` | Machine learning in Python with scikit-learn. Use for classification, regression, clustering, model evaluation, and ML pipelines. |
| `seaborn` | Seaborn is a Python visualization library for creating publication-quality statistical graphics. Use this skill for dataset-oriented plotting, multivariate analysis, automatic statistical estimation, and complex multi... |
| `statsmodels` | Statsmodels is Python's premier library for statistical modeling, providing tools for estimation, inference, and diagnostics across a wide range of statistical methods. |
| `sympy` | SymPy is a Python library for symbolic mathematics that enables exact computation using mathematical symbols rather than numerical approximations. |
| `uniprot-database` | Direct REST API access to UniProt. Protein searches, FASTA retrieval, ID mapping, Swiss-Prot/TrEMBL. For Python workflows with multiple databases, prefer bioservices (unified interface to 40+ services). Use this for d... |

### `hig-apple` (14)

Apple Human Interface Guidelines.

| Skill | What it does |
|---|---|
| `hig-components-content` | Apple Human Interface Guidelines for content display components. |
| `hig-components-controls` | Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered. |
| `hig-components-dialogs` | Apple HIG guidance for presentation components including alerts, action sheets, popovers, sheets, and digit entry views. |
| `hig-components-layout` | Apple Human Interface Guidelines for layout and navigation components. |
| `hig-components-menus` | Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered. |
| `hig-components-search` | Apple HIG guidance for navigation-related components including search fields, page controls, and path controls. |
| `hig-components-status` | Apple HIG guidance for status and progress UI components including progress indicators, status bars, and activity rings. |
| `hig-components-system` | Apple HIG guidance for system experience components: widgets, live activities, notifications, complications, home screen quick actions, top shelf, watch faces, app clips, and app shortcuts. |
| `hig-foundations` | Apple Human Interface Guidelines design foundations. |
| `hig-inputs` | Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered. |
| `hig-patterns` | Apple Human Interface Guidelines interaction and UX patterns. |
| `hig-platforms` | Apple Human Interface Guidelines for platform-specific design. |
| `hig-project-context` | Create or update a shared Apple design context document that other HIG skills use to tailor guidance. |
| `hig-technologies` | Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered. |

### `ai-personas` (13)

Persona prompts for design and critique.

| Skill | What it does |
|---|---|
| `andrej-karpathy` | Agente que simula Andrej Karpathy — ex-Director of AI da Tesla, co-fundador da OpenAI, fundador da Eureka Labs, e o maior educador de deep learning do mundo. |
| `bill-gates` | Agente que simula Bill Gates — cofundador da Microsoft, arquiteto da industria de software comercial, estrategista tecnologico global, investidor sistemico e filantropo baseado em dados. |
| `elon-musk` | Agente que simula Elon Musk com profundidade psicologica e comunicacional de alta fidelidade. Ativado para: "fale como Elon", "simule Elon Musk", "o que Elon diria sobre X", "first principles thinking", "think like El... |
| `geoffrey-hinton` | Agente que simula Geoffrey Hinton — Godfather of Deep Learning, Prêmio Turing 2018, criador do backpropagation e das Deep Belief Networks. |
| `ilya-sutskever` | Agente que simula Ilya Sutskever — co-fundador da OpenAI, ex-Chief Scientist, fundador da SSI. Use quando quiser perspectivas sobre: AGI safety-first, consciência de IA, scaling laws, deep learning profundo, o episódi... |
| `matematico-tao` | Matemático ultra-avançado inspirado em Terence Tao. Análise rigorosa de código e arquitetura com teoria matemática profunda: teoria da informação, teoria dos grafos, complexidade computacional, álgebra linear, análise... |
| `sam-altman` | Agente que simula Sam Altman — CEO da OpenAI, ex-presidente da Y Combinator, arquiteto da era AGI. |
| `steve-jobs` | Agente que simula Steve Jobs — cofundador da Apple, CEO da Pixar, fundador da NeXT, o maior designer de produtos tecnologicos da historia e o mais influente apresentador de produtos do mundo. |
| `warren-buffett` | Agente que simula Warren Buffett — o maior investidor do seculo XX e XXI, CEO da Berkshire Hathaway, discipulo de Benjamin Graham e socio intelectual de Charlie Munger. |
| `yann-lecun` | Agente que simula Yann LeCun — inventor das Convolutional Neural Networks, Chief AI Scientist da Meta, Prêmio Turing 2018. |
| `yann-lecun-debate` | Sub-skill de debates e posições de Yann LeCun. Cobre críticas técnicas detalhadas aos LLMs, rivalidades intelectuais (LeCun vs Hinton, Sutskever, Russell, Yudkowsky, Bostrom), lista completa de rejeições a afirmações... |
| `yann-lecun-filosofia` | Sub-skill filosófica e pedagógica de Yann LeCun. |
| `yann-lecun-tecnico` | Sub-skill técnica de Yann LeCun. Cobre CNNs, LeNet, backpropagation, JEPA (I-JEPA, V-JEPA, MC-JEPA), AMI (Advanced Machinery of Intelligence), Self-Supervised Learning (SimCLR, MAE, BYOL), Energy-Based Models (EBMs) e... |

### `makepad` (13)

Makepad UI.

| Skill | What it does |
|---|---|
| `makepad-animation` | CRITICAL: Use for Makepad animation system. Triggers on: makepad animation, makepad animator, makepad hover, makepad state, makepad transition, "from: { all: Forward", makepad pressed, makepad 动画, makepad 状态, makepad... |
| `makepad-basics` | CRITICAL: Use for Makepad getting started and app structure. Triggers on: makepad, makepad getting started, makepad tutorial, live_design!, app_main!, makepad project setup, makepad hello world, "how to create makepad... |
| `makepad-deployment` | CRITICAL: Use for Makepad packaging and deployment. Triggers on: deploy, package, APK, IPA, 打包, 部署, cargo-packager, cargo-makepad, WASM, Android, iOS, distribution, installer, .deb, .dmg, .nsis, GitHub Actions, CI, ac... |
| `makepad-dsl` | CRITICAL: Use for Makepad DSL syntax and inheritance. Triggers on: makepad dsl, live_design, makepad inheritance, makepad prototype, "<Widget>", "Foo = { }", makepad object, makepad property, makepad DSL 语法, makepad 继... |
| `makepad-event-action` | CRITICAL: Use for Makepad event and action handling. Triggers on: makepad event, makepad action, Event enum, ActionTrait, handle_event, MouseDown, KeyDown, TouchUpdate, Hit, FingerDown, post_action, makepad 事件, makepa... |
| `makepad-font` | CRITICAL: Use for Makepad font and text rendering. Triggers on: makepad font, makepad text, makepad glyph, makepad typography, font atlas, text layout, font family, font size, text shaping, makepad 字体, makepad 文字, mak... |
| `makepad-layout` | CRITICAL: Use for Makepad layout system. Triggers on: makepad layout, makepad width, makepad height, makepad flex, makepad padding, makepad margin, makepad flow, makepad align, Fit, Fill, Size, Walk, "how to center in... |
| `makepad-platform` | CRITICAL: Use for Makepad cross-platform support. Triggers on: makepad platform, makepad os, makepad macos, makepad windows, makepad linux, makepad android, makepad ios, makepad web, makepad wasm, makepad metal, makep... |
| `makepad-reference` | This category provides reference materials for debugging, code quality, and advanced layout patterns. |
| `makepad-shaders` | CRITICAL: Use for Makepad shader system. Triggers on: makepad shader, makepad draw_bg, Sdf2d, makepad pixel, makepad glsl, makepad sdf, draw_quad, makepad gpu, makepad 着色器, makepad shader 语法, makepad 绘制 |
| `makepad-skills` | Makepad UI development skills for Rust apps: setup, patterns, shaders, packaging, and troubleshooting. |
| `makepad-splash` | CRITICAL: Use for Makepad Splash scripting language. Triggers on: splash language, makepad script, makepad scripting, script!, cx.eval, makepad dynamic, makepad AI, splash 语言, makepad 脚本 |
| `makepad-widgets` | Version: makepad-widgets (dev branch) \| Last Updated: 2026-01-19 > > Check for updates: https://crates.io/crates/makepad-widgets |

### `three-js` (13)

Three.js scenes, materials, and animation.

| Skill | What it does |
|---|---|
| `3d-web-experience` | You bring the third dimension to the web. You know when 3D enhances and when it's just showing off. You balance visual impact with performance. You make 3D accessible to users who've never touched a 3D app. You create... |
| `spline-3d-integration` | Use when adding interactive 3D scenes from Spline.design to web projects, including React embedding and runtime control API. |
| `threejs-animation` | Three.js animation - keyframe animation, skeletal animation, morph targets, animation mixing. Use when animating objects, playing GLTF animations, creating procedural motion, or blending animations. |
| `threejs-fundamentals` | Three.js scene setup, cameras, renderer, Object3D hierarchy, coordinate systems. Use when setting up 3D scenes, creating cameras, configuring renderers, managing object hierarchies, or working with transforms. |
| `threejs-geometry` | Three.js geometry creation - built-in shapes, BufferGeometry, custom geometry, instancing. Use when creating 3D shapes, working with vertices, building custom meshes, or optimizing with instanced rendering. |
| `threejs-interaction` | Three.js interaction - raycasting, controls, mouse/touch input, object selection. Use when handling user input, implementing click detection, adding camera controls, or creating interactive 3D experiences. |
| `threejs-lighting` | Three.js lighting - light types, shadows, environment lighting. Use when adding lights, configuring shadows, setting up IBL, or optimizing lighting performance. |
| `threejs-loaders` | Three.js asset loading - GLTF, textures, images, models, async patterns. Use when loading 3D models, textures, HDR environments, or managing loading progress. |
| `threejs-materials` | Three.js materials - PBR, basic, phong, shader materials, material properties. Use when styling meshes, working with textures, creating custom shaders, or optimizing material performance. |
| `threejs-postprocessing` | Three.js post-processing - EffectComposer, bloom, DOF, screen effects. Use when adding visual effects, color grading, blur, glow, or creating custom screen-space shaders. |
| `threejs-shaders` | Three.js shaders - GLSL, ShaderMaterial, uniforms, custom effects. Use when creating custom visual effects, modifying vertices, writing fragment shaders, or extending built-in materials. |
| `threejs-skills` | Create 3D scenes, interactive experiences, and visual effects using Three.js. Use when user requests 3D graphics, WebGL experiences, 3D visualizations, animations, or interactive 3D elements. |
| `threejs-textures` | Three.js textures - texture types, UV mapping, environment maps, texture settings. Use when working with images, UV coordinates, cubemaps, HDR environments, or texture optimization. |

### `apify` (12)

Apify actor workflows.

| Skill | What it does |
|---|---|
| `apify-actor-development` | Important: Before you begin, fill in the generatedBy property in the meta section of .actor/actor.json. Replace it with the tool and model you're currently using, such as "Claude Code with Claude Sonnet 4.5". This hel... |
| `apify-actorization` | Actorization converts existing software into reusable serverless applications compatible with the Apify platform. Actors are programs packaged as Docker images that accept well-defined JSON input, perform an action, a... |
| `apify-audience-analysis` | Understand audience demographics, preferences, behavior patterns, and engagement quality across Facebook, Instagram, YouTube, and TikTok. |
| `apify-brand-reputation-monitoring` | Scrape reviews, ratings, and brand mentions from multiple platforms using Apify Actors. |
| `apify-competitor-intelligence` | Analyze competitor strategies, content, pricing, ads, and market positioning across Google Maps, Booking.com, Facebook, Instagram, YouTube, and TikTok. |
| `apify-content-analytics` | Track engagement metrics, measure campaign ROI, and analyze content performance across Instagram, Facebook, YouTube, and TikTok. |
| `apify-ecommerce` | Extract product data, prices, reviews, and seller information from any e-commerce platform using Apify's E-commerce Scraping Tool. |
| `apify-influencer-discovery` | Find and evaluate influencers for brand partnerships, verify authenticity, and track collaboration performance across Instagram, Facebook, YouTube, and TikTok. |
| `apify-lead-generation` | Scrape leads from multiple platforms using Apify Actors. |
| `apify-market-research` | Analyze market conditions, geographic opportunities, pricing, consumer behavior, and product validation across Google Maps, Facebook, Instagram, Booking.com, and TripAdvisor. |
| `apify-trend-analysis` | Discover and track emerging trends across Google Trends, Instagram, Facebook, YouTube, and TikTok to inform content strategy. |
| `apify-ultimate-scraper` | AI-driven data extraction from 55+ Actors across all major platforms. This skill automatically selects the best Actor for your task. |

### `mobile` (12)

iOS, Android, and React Native.

| Skill | What it does |
|---|---|
| `android-jetpack-compose-expert` | Expert guidance for building modern Android UIs with Jetpack Compose, covering state management, navigation, performance, and Material Design 3. |
| `android-ui-verification` | Automated end-to-end UI testing and verification on an Android Emulator using ADB. |
| `app-store-optimization` | Complete App Store Optimization (ASO) toolkit for researching, optimizing, and tracking mobile app performance on Apple App Store and Google Play Store |
| `building-native-ui` | Complete guide for building beautiful apps with Expo Router. Covers fundamentals, styling, components, navigation, animations, patterns, and native tabs. |
| `flutter-expert` | Master Flutter development with Dart 3, advanced widgets, and multi-platform deployment. |
| `ios-developer` | Develop native iOS applications with Swift/SwiftUI. Masters iOS 18, SwiftUI, UIKit integration, Core Data, networking, and App Store optimization. |
| `ios-swift-development` | Develop native iOS apps with Swift. Covers MVVM architecture, SwiftUI, URLSession for networking, Combine for reactive programming, and Core Data persistence. |
| `kotlin-coroutines-expert` | Expert patterns for Kotlin Coroutines and Flow, covering structured concurrency, error handling, and testing. |
| `mobile-design` | Mobile UX patterns, touch interactions, gesture design, mobile-first principles, app navigation, and mobile performance |
| `mobile-developer` | Develop React Native, Flutter, or native mobile apps with modern architecture patterns. Masters cross-platform development, native integrations, offline sync, and app store optimization. |
| `react-native-architecture` | Production-ready patterns for React Native development with Expo, including navigation, state management, native modules, and offline-first architecture. |
| `swiftui-expert-skill` | Write, review, or improve SwiftUI code following best practices for state management, view composition, performance, and iOS 26+ Liquid Glass adoption. Use when building new SwiftUI features, refactoring existing view... |

### `documents` (9)

Office and PDF document skills. Anthropic's official copies live here.

| Skill | What it does |
|---|---|
| `doc-coauthoring` | This skill provides a structured workflow for guiding users through collaborative document creation. Act as an active guide, walking users through three stages: Context Gathering, Refinement & Structure, and Reader Te... |
| `docx-official` | A user may ask you to create, edit, or analyze the contents of a .docx file. A .docx file is essentially a ZIP archive containing XML files and other resources that you can read or edit. You have different tools and w... |
| `latex-paper-conversion` | This skill should be used when the user asks to convert an academic paper in LaTeX from one format (e.g., Springer, IPOL) to another format (e.g., MDPI, IEEE, Nature). It automates extraction, injection, fixing format... |
| `nanobanana-ppt-skills` | AI-powered PPT generation with document analysis and styled images |
| `notebooklm` | Interact with Google NotebookLM to query documentation with Gemini's source-grounded answers. Each question opens a fresh browser session, retrieves the answer exclusively from your uploaded documents, and closes. |
| `office-productivity` | Office productivity workflow covering document creation, spreadsheet automation, presentation generation, and integration with LibreOffice and Microsoft Office formats. |
| `pdf-official` | This guide covers essential PDF processing operations using Python libraries and command-line tools. For advanced features, JavaScript libraries, and detailed examples, see reference.md. If you need to fill out a PDF... |
| `pptx-official` | A user may ask you to create, edit, or analyze the contents of a .pptx file. A .pptx file is essentially a ZIP archive containing XML files and other resources that you can read or edit. You have different tools and w... |
| `xlsx-official` | Unless otherwise stated by the user or existing template |

### `expo` (8)

Expo and EAS.

| Skill | What it does |
|---|---|
| `expo-api-routes` | Guidelines for creating API routes in Expo Router with EAS Hosting |
| `expo-cicd-workflows` | Helps understand and write EAS workflow YAML files for Expo projects. Use this skill when the user asks about CI/CD or workflows in an Expo or EAS context, mentions .eas/workflows/, or wants help with EAS build pipeli... |
| `expo-deployment` | Deploy Expo apps to production |
| `expo-dev-client` | Build and distribute Expo development clients locally or via TestFlight |
| `expo-tailwind-setup` | Set up Tailwind CSS v4 in Expo with react-native-css and NativeWind v5 for universal styling |
| `expo-ui-jetpack-compose` | expo-ui-jetpack-compose |
| `expo-ui-swift-ui` | expo-ui-swift-ui |
| `upgrading-expo` | Upgrade Expo SDK versions |

### `hugging-face` (8)

Hugging Face datasets, jobs, and training.

| Skill | What it does |
|---|---|
| `hugging-face-cli` | The hf CLI provides direct terminal access to the Hugging Face Hub for downloading, uploading, and managing repositories, cache, and compute resources. |
| `hugging-face-dataset-viewer` | Use this skill for Hugging Face Dataset Viewer API workflows that fetch subset/split metadata, paginate rows, search text, apply filters, download parquet URLs, and read size or statistics. |
| `hugging-face-datasets` | Create and manage datasets on Hugging Face Hub. Supports initializing repos, defining configs/system prompts, streaming row updates, and SQL-based dataset querying/transformation. Designed to work alongside HF MCP ser... |
| `hugging-face-evaluation` | Add and manage evaluation results in Hugging Face model cards. Supports extracting eval tables from README content, importing scores from Artificial Analysis API, and running custom model evaluations with vLLM/lightev... |
| `hugging-face-jobs` | Run any workload on fully managed Hugging Face infrastructure. No local setup required—jobs run on cloud CPUs, GPUs, or TPUs and can persist results to the Hugging Face Hub. |
| `hugging-face-model-trainer` | Train language models using TRL (Transformer Reinforcement Learning) on fully managed Hugging Face infrastructure. No local GPU setup required—models train on cloud GPUs and results are automatically saved to the Hugg... |
| `hugging-face-paper-publisher` | Publish and manage research papers on Hugging Face Hub. Supports creating paper pages, linking papers to models/datasets, claiming authorship, and generating professional markdown-based research articles. |
| `hugging-face-tool-builder` | Your purpose is now is to create reusable command line scripts and utilities for using the Hugging Face API, allowing chaining, piping and intermediate processing where helpful. You can access the API directly, as wel... |

### `conductor` (7)

Multi-track agent orchestration.

| Skill | What it does |
|---|---|
| `conductor-implement` | Execute tasks from a track's implementation plan following TDD workflow |
| `conductor-manage` | Manage track lifecycle: archive, restore, delete, rename, and cleanup |
| `conductor-new-track` | Create a new track with specification and phased implementation plan |
| `conductor-revert` | Git-aware undo by logical work unit (track, phase, or task) |
| `conductor-setup` | Configure a Rails project to work with Conductor (parallel coding agents) |
| `conductor-status` | Display project status, active tracks, and next actions |
| `conductor-validator` | Validates Conductor project artifacts for completeness, consistency, and correctness. Use after setup, when diagnosing issues, or before implementation to verify project context. |

### `leiloeiro` (7)

Brazilian real-estate auction workflows (upstream author: renat).

| Skill | What it does |
|---|---|
| `junta-leiloeiros` | Coleta e consulta dados de leiloeiros oficiais de todas as 27 Juntas Comerciais do Brasil. Scraper multi-UF, banco SQLite, API FastAPI e exportacao CSV/JSON. |
| `leiloeiro-avaliacao` | Avaliacao pericial de imoveis em leilao. Valor de mercado, liquidacao forcada, ABNT NBR 14653, metodos comparativo/renda/custo, CUB e margem de seguranca. |
| `leiloeiro-edital` | Analise e auditoria de editais de leilao judicial e extrajudicial. Riscos ocultos, clausulas perigosas, debitos, ocupante e classificacao da oportunidade. |
| `leiloeiro-ia` | Especialista em leiloes judiciais e extrajudiciais de imoveis. Analise juridica, pericial e de mercado integrada. Orquestra os 5 modulos especializados. |
| `leiloeiro-juridico` | Analise juridica de leiloes: nulidades, bem de familia, alienacao fiduciaria, CPC arts 829-903, Lei 9514/97, onus reais, embargos e jurisprudencia. |
| `leiloeiro-mercado` | Analise de mercado imobiliario para leiloes. Liquidez, desagio tipico, ROI, estrategias de saida (flip/reforma/renda), Selic 2025 e benchmark CDI/FII. |
| `leiloeiro-risco` | Analise de risco em leiloes de imoveis. Score 36 pontos, riscos juridicos/financeiros/operacionais, stress test 4 cenarios e ROI ponderado por risco. |

### `n8n-automation` (7)

n8n workflow skills.

| Skill | What it does |
|---|---|
| `n8n-code-javascript` | Write JavaScript code in n8n Code nodes. Use when writing JavaScript in n8n, using $input/$json/$node syntax, making HTTP requests with $helpers, working with dates using DateTime, troubleshooting Code node errors, or... |
| `n8n-code-python` | Write Python code in n8n Code nodes. Use when writing Python in n8n, using _input/_json/_node syntax, working with standard library, or need to understand Python limitations in n8n Code nodes. |
| `n8n-expression-syntax` | Validate n8n expression syntax and fix common errors. Use when writing n8n expressions, using {{}} syntax, accessing $json/$node variables, troubleshooting expression errors, or working with webhook data in workflows. |
| `n8n-mcp-tools-expert` | Expert guide for using n8n-mcp MCP tools effectively. Use when searching for nodes, validating configurations, accessing templates, managing workflows, or using any n8n-mcp tool. Provides tool selection guidance, para... |
| `n8n-node-configuration` | Operation-aware node configuration guidance. Use when configuring nodes, understanding property dependencies, determining required fields, choosing between get_node detail levels, or learning common configuration patt... |
| `n8n-validation-expert` | Expert guide for interpreting and fixing n8n validation errors. |
| `n8n-workflow-patterns` | Proven workflow architectural patterns from real n8n workflows. Use when building new workflows, designing workflow structure, choosing workflow patterns, planning workflow architecture, or asking about webhook proces... |

### `robius` (5)

Robius application structure.

| Skill | What it does |
|---|---|
| `robius-app-architecture` | CRITICAL: Use for Robius app architecture patterns. Triggers on: Tokio, async, submit_async_request, 异步, 架构, SignalToUI, Cx::post_action, worker task, app structure, MatchEvent, handle_startup |
| `robius-event-action` | CRITICAL: Use for Robius event and action patterns. Triggers on: custom action, MatchEvent, post_action, cx.widget_action, handle_actions, DefaultNone, widget action, event handling, 事件处理, 自定义动作 |
| `robius-matrix-integration` | CRITICAL: Use for Matrix SDK integration with Makepad. Triggers on: Matrix SDK, sliding sync, MatrixRequest, timeline, matrix-sdk, matrix client, robrix, matrix room, Matrix 集成, 聊天客户端 |
| `robius-state-management` | CRITICAL: Use for Robius state management patterns. Triggers on: AppState, persistence, theme switch, 状态管理, Scope::with_data, save state, load state, serde, 状态持久化, 主题切换 |
| `robius-widget-patterns` | CRITICAL: Use for Robius widget patterns. Triggers on: apply_over, TextOrImage, modal, 可复用, 模态, collapsible, drag drop, reusable widget, widget design, pageflip, 组件设计, 组件模式 |

### `wordpress` (4)

WordPress themes, plugins, and WooCommerce.

| Skill | What it does |
|---|---|
| `wordpress` | Complete WordPress development workflow covering theme development, plugin creation, WooCommerce integration, performance optimization, and security hardening. |
| `wordpress-plugin-development` | WordPress plugin development workflow covering plugin architecture, hooks, admin interfaces, REST API, and security best practices. |
| `wordpress-theme-development` | WordPress theme development workflow covering theme architecture, template hierarchy, custom post types, block editor support, and responsive design. |
| `wordpress-woocommerce-development` | WooCommerce store development workflow covering store setup, payment integration, shipping configuration, and customization. |

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
