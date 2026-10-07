# Third-party material

This repository is [Lesley Oredia](https://github.com/lloredia)'s categorized snapshot of Claude Code skills. The first commit (`ac75ada`, "Backup all Claude Code skills", 2026-03-20) imported a local skills directory. Category folders were added later in this repo. The skill text itself is almost entirely copied from public projects. Lesley's own work in the repository is the organization, the README, and this cleanup — not authorship of the upstream skills.

Security and cloud/DevOps skills are listed first in the README because they match the work the collection is used for. They are still upstream skills unless a file says otherwise.

## Where copies came from

| Source | What landed here |
|---|---|
| [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | The bulk of the catalog. Skills tagged `source: community`, `source: personal`, `source: self`, or `source: original` in that project were copied with those tags intact. That includes the Andru.ia skills and `vibe-code-auditor`. It is an upstream tag, not a claim that Lesley wrote the skill. |
| [microsoft/skills](https://github.com/microsoft/skills) | Most of `azure/` (per-SDK, per-language Azure skills). |
| [anthropics/skills](https://github.com/anthropics/skills) | Official document, design, and MCP skills that ship with an Anthropic `LICENSE.txt`. |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | `ai-ml/loki-mode` (MIT). Generated benchmark dumps and `demo/loki-demo.gif` were removed. |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | `ai-ml/last30days`. Example images and the sample MP3 were removed. |
| [op7418/NanoBanana-PPT-Skills](https://github.com/op7418/NanoBanana-PPT-Skills) | `design-uiux/nano-banana`. PNG logos over 100 KB were removed. |
| Hugging Face, Expo, and other repos | Named in the skill's `source:` field when the upstream author set one. |

Individual `source:` values that are URLs:

- https://github.com/CloudAI-X/threejs-skills
- https://github.com/ChaosRealmsAI/agent-cli-spec
- https://github.com/K-Dense-AI/claude-scientific-skills
- https://github.com/NotMyself/claude-win11-speckit-update-skill
- https://github.com/SeanZoR/claude-speed-reader
- https://github.com/Shpigford/skills
- https://github.com/ZhangHanDong/makepad-skills
- https://github.com/ai-evos/agent-skills
- https://github.com/antonbabenko/terraform-skill
- https://github.com/astropy/astropy
- https://github.com/biopython/biopython
- https://github.com/conorbronsdon/avoid-ai-writing
- https://github.com/dmno-dev/varlock
- https://github.com/expo/skills
- https://github.com/fal-ai-community/skills
- https://github.com/go-rod/rod
- https://github.com/google-labs-code/stitch-skills
- https://github.com/huifer/Claude-Ally-Health
- https://github.com/huggingface/skills
- https://github.com/ibelick/ui-skills
- https://github.com/jackjin1997/ClawForge
- https://github.com/jthack/ffuf_claude_skill
- https://github.com/k-kolomeitsev/data-structure-protocol
- https://github.com/kennyzheng-builds/seek-and-analyze-video
- https://github.com/kromahlusenii-ops/ham
- https://github.com/ksgisang/awt-skill
- https://github.com/makepad/makepad
- https://github.com/marsiandeployer/vibers-action
- https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering
- https://github.com/neondatabase/agent-skills
- https://github.com/networkx/networkx
- https://github.com/obra/superpowers-lab
- https://github.com/olgasafonova/SkillCheck-Free
- https://github.com/omkamal/pypict-claude-skill
- https://github.com/playwright-community/playwright-go
- https://github.com/robzolkos/skill-rails-upgrade
- https://github.com/sanjay3290/ai-skills
- https://github.com/scarletkc/vexor
- https://github.com/shadcn-ui/ui
- https://github.com/sstklen/infinite-gratitude
- https://github.com/sympy/sympy
- https://github.com/trailofbits/skills
- https://github.com/whatiskadudoing/fp-ts-skills
- https://github.com/wrsmith108/linear-claude-skill
- https://github.com/wrsmith108/varlock-claude-skill
- https://github.com/wshuyi/x-article-publisher-skill
- https://github.com/yusufkaraaslan/Skill_Seekers
- https://github.com/zarazhangrui/frontend-slides
- https://github.com/zxkane/aws-skills
- https://docs.convex.dev
- https://docs.dbos.dev/

`leiloeiro/` is community work by the author named `renat` in the skill frontmatter, also published in antigravity-awesome-skills.

## Licenses kept beside the skills

These files are the upstream licenses. They were not rewritten.

- `ai-ml/loki-mode/LICENSE` (MIT)
- `design-uiux/algorithmic-art/LICENSE.txt`
- `design-uiux/canvas-design/LICENSE.txt`
- `design-uiux/theme-factory/LICENSE.txt`
- `design-uiux/ui-styling/LICENSE.txt`
- `docs-writing/brand-guidelines-anthropic/LICENSE.txt`
- `docs-writing/brand-guidelines-community/LICENSE.txt`
- `docs-writing/diary/LICENSE`
- `docs-writing/docs/sources/LICENSE-MICROSOFT`
- `docs-writing/internal-comms-anthropic/LICENSE.txt`
- `docs-writing/internal-comms-community/LICENSE.txt`
- `documents/docx-official/LICENSE.txt`
- `documents/notebooklm/LICENSE`
- `documents/pdf-official/LICENSE.txt`
- `documents/pptx-official/LICENSE.txt`
- `documents/xlsx-official/LICENSE.txt`
- `frontend/web-artifacts-builder/LICENSE.txt`
- `integrations-automation/slack-gif-creator/LICENSE.txt`
- `skills-meta/mcp-builder/LICENSE.txt`
- `skills-meta/skill-creator/LICENSE.txt`
- `testing-qa/webapp-testing/LICENSE.txt`

Anthropic's `LICENSE.txt` (for example `documents/docx-official/LICENSE.txt`) says those materials may not be extracted from Anthropic's services or redistributed. They were already in this public repository when this cleanup started. The license file stays with the skill so the restriction is visible. Whether those folders should remain public is the owner's call.

## Duplicates removed

These directories were byte-for-byte copies of another skill and were deleted:

| Removed | Kept |
|---|---|
| `documents/docx` | `documents/docx-official` |
| `documents/pptx` | `documents/pptx-official` |
| `documents/xlsx` | `documents/xlsx-official` |
| `documents/pdf` | `documents/pdf-official` |

`design-uiux/ui-styling/canvas-fonts` is a symlink to `../canvas-design/canvas-fonts`. The font files are stored once.

`frontend/web-artifacts-builder/scripts/shadcn-components.tar.gz` is still here. It is the component payload that skill's script unpacks (about 20 KB), not a second copy of source files already in the tree.

## Broken links removed

Two symlinks pointed at paths that only existed on the machine that made the backup:

- `frontend/frontend-design` → `../../.agents/skills/frontend-design`
- `backend/supabase-automation/supabase-automation` → `../../docs/claude-code-skills/community/supabase-automation`
