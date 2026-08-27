---
name: ai-lab-flow-triage
description: Triage AI tools, repos, agents, and workflows.
version: 0.1.0
author: Yaohsiang Ko (keyu03), Hermes Agent
license: MIT
platforms: [windows]
metadata:
  hermes:
    tags: [AIResearch, GitHub, Agents, MCP, Obsidian, Triage]
    related_skills: [grounded-citations, ai-info-obsidian-archive]
  created_by: agent
---

# AI Lab Flow Triage Skill

Use this skill to evaluate AI tools, GitHub repos, MCP servers, plugins, agent skills, and developer workflows through a skeptical lab process. The goal is not to chase every new thing; the goal is to find the few tools worth learning, testing, adopting, archiving, or incubating into projects.

This skill uses the flow: **Discover → Triage → Deep Dive → Experiment → Verdict → Incubate**.

## When to Use

Use when the user asks to:

- Analyze an AI product, course, agent platform, coding tool, MCP server, plugin, or skill.
- Decide whether a GitHub repo is worth reading, cloning, testing, or archiving.
- Turn a link into an Obsidian AI info note.
- Compare a tool's claims against real architecture, source code, docs, maintenance, and risks.
- Design a minimum viable experiment before adopting a new AI workflow.
- Decide whether something should become a Hermes skill, plugin, MCP server, GitHub project, or company-side experiment.

Don't use for:

- Full implementation of a coding project; use coding/project skills after the verdict.
- Formal company production rollout; route to `work-ai` and add governance checks.
- Taiwan stock analysis.
- Pure note-taking without analysis; use Obsidian skills.
- Copying proprietary course content, prompts, templates, or workflows.

## Prerequisites

- Preferred language: Traditional Chinese.
- Default Obsidian vault: `D:/program/obsidian/claude`.
- Default archive folder: `D:/program/obsidian/claude/AI資訊/`.
- Use free/public sources first: official docs, GitHub API, README, repo tree, license, issues, releases, examples, and local tests.
- Ask before paid tools, paid APIs, external publishing, or sensitive permissions.
- Do not connect unverified tools to production data.
- For fetched claims, use citations or preserve source URLs in saved notes.

## How to Run

In Telegram / gateway:

```text
/skill ai-lab-flow-triage
分析這個工具的用途、風險、值不值得測：https://example.com/tool
```

In CLI:

```bash
hermes -p lab -s ai-lab-flow-triage
hermes -p lab -s ai-lab-flow-triage chat -q "分析這個 repo 是否值得測：https://github.com/owner/repo"
```

After creating or syncing the skill, use `/reload-skills` and usually `/reset` so the running session sees it.

## Quick Reference

| Need | User prompt |
|---|---|
| AI tool review | `用 ai-lab-flow-triage 分析這個工具。` |
| Repo triage | `這個 GitHub repo 值不值得 clone 實測？` |
| MCP/plugin check | `它有沒有 MCP / OpenAPI / plugin / skill 介面？` |
| Minimum experiment | `幫我設計 60 分鐘內可完成的最小實驗。` |
| Archive | `如果值得，整理到 Obsidian AI資訊。` |
| Incubate | `判斷能不能變成 Hermes skill / plugin / MCP server。` |

## Triage Flow

### 1. Discover

Collect basic facts from public sources.

For websites/products:

- Official page.
- Docs.
- Pricing.
- Terms/privacy/license.
- Integration surfaces.
- Evidence of real product vs landing page.

For GitHub repos:

- README.
- License.
- Default branch and latest commits.
- Repo tree.
- Package files.
- Tests/examples.
- Issues/releases.
- Security notes.
- Agent-facing files: MCP, OpenAPI, `llms.txt`, skills, plugins, tool discovery, manifests.

Completion criteria:

- Source URLs are preserved.
- Claims are separated from inference.

### 2. Triage

Classify the item:

| Status | Meaning |
|---|---|
| 🟢 可用 | Strong enough to use now in a bounded context |
| 🟡 值得測 | Promising, needs a small experiment |
| 🔵 值得追蹤 | Interesting, not ready or not urgent |
| 🟠 值得學 | Valuable architecture/pattern, not necessarily usable |
| 🔴 不建議 | Risk, low value, dead, or mismatch |
| 🧸 漂亮玩具 | Nice demo/UI, weak evidence of durable value |

Ask:

- What problem does it solve?
- Is the problem important to the user?
- Is it better than current tools?
- What evidence supports its claims?
- What would make us stop caring?

Completion criteria:

- One provisional verdict exists.
- The next step is either deep dive, experiment, archive, or kill.

### 3. Deep Dive

Inspect the hard parts.

Minimum checklist:

- **Problem fit** — what pain does it reduce?
- **Architecture** — runtime, storage, deployment, extensibility.
- **Tool interface** — CLI, API, SDK, MCP, OpenAPI, webhooks, plugins, skills.
- **Permissions** — filesystem, browser, cloud accounts, tokens, production data.
- **Data flow** — what leaves the machine, where it is stored, how it is deleted.
- **Install cost** — dependencies, OS support, Docker/WSL/cloud needs.
- **Maintenance** — recent commits, releases, issues, tests, bus factor.
- **License/commercial use** — OSS license, proprietary terms, AI training restrictions.
- **Enterprise fit** — audit, access control, observability, rollback, governance.

Completion criteria:

- The analysis includes both value and constraints.
- Marketing language is not treated as proof.

### 4. Experiment

Design the smallest safe test.

Use this format:

```markdown
## 最小可行實驗

假設：
測試範圍：
測試資料：
安裝步驟：
執行步驟：
成功條件：
退出條件：
時間盒：
風險控制：
```

Rules:

- Prefer local/sandboxed tests.
- Avoid production credentials and real customer data.
- Define success and exit criteria before installing heavy dependencies.
- If it cannot be tested safely in under 1–2 hours, explain why.

Completion criteria:

- The test can be run without guessing what success means.
- The user knows when to stop.

### 5. Verdict

Every answer must end with a clear verdict.

Use this format:

```markdown
## Verdict

判定：
值不值得看：
值不值得測：
建議投入時間：
可能產生價值：
主要風險：
下一步：
```

Completion criteria:

- The verdict uses exactly one of the six labels.
- The next step is concrete.

### 6. Incubate

If the item is worth keeping, decide its destination:

- Obsidian note.
- Lab experiment.
- Hermes skill.
- MCP server.
- Plugin.
- GitHub repo.
- Work project.
- Watchlist.
- Kill list.

Use this format:

```markdown
## Incubation Decision

目的地：
原因：
MVP：
成功條件：
退出條件：
需要保存到 Obsidian：是 / 否
```

Completion criteria:

- The item has a destination or is explicitly killed.
- Durable findings are archived when useful.

## Output Templates

### Tool/Product Review

```markdown
# 工具名稱

## 一句話

## 它解決什麼問題？

## 對我的實際幫助

## 架構 / 介面 / 資料流

## 安裝與維運成本

## 安全 / 隱私 / 授權風險

## 最小可行實驗

## Verdict

## 下一步

## Sources
```

### GitHub Repo Review

```markdown
# owner/repo

## 一句話

## Repo 現況

- License：
- Language：
- 最近維護：
- Tests：
- Releases：
- Docs：

## 它實際做什麼？

## Agent-facing surfaces

- MCP：
- OpenAPI：
- llms.txt：
- Skills：
- Plugins：
- Tool discovery：

## 風險與限制

## 最小可行實驗

## Verdict

## 是否值得歸檔 / 孵化
```

## Obsidian Archiving

When saving durable research, write under:

```text
D:/program/obsidian/claude/AI資訊/
```

Common destinations:

```text
AI資訊/AI工具/
AI資訊/AI開發工作流/
AI資訊/平台比較/
AI資訊/AI新資訊收集箱.md
```

A good note includes:

- YAML frontmatter with tags and source URLs.
- Original links.
- Date.
- One-line conclusion.
- Source-grounded facts.
- Inference/opinion clearly separated.
- Strengths, gaps, risks.
- Verdict and next step.

After writing:

- Verify file exists with `read_file`.
- Patch `AI資訊/AI資訊總覽.md` when the item is index-worthy.

## Pitfalls

- Do not confuse README claims with working capability.
- Do not treat stars, launch hype, or UI polish as proof.
- Do not over-invest before a minimum experiment.
- Do not clone or run unknown code against sensitive folders or credentials.
- Do not install tools that require broad permissions without asking.
- Do not archive raw links without practical analysis.
- Do not present a paid course as an agent platform unless architecture evidence supports it.
- Do not copy proprietary prompts, workflows, templates, or course content.

## Verification

Before finalizing, check:

- Are source links preserved?
- Is the problem/value stated in plain language?
- Are architecture, permissions, and data flow addressed when relevant?
- Are install/maintenance/security costs named?
- Is there a minimum viable experiment with success and exit criteria?
- Is the verdict explicit?
- Was useful durable research saved to Obsidian when appropriate?
