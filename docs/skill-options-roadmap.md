# Skill Options & Roadmap

This document organizes the personal Hermes skill ideas derived from the Flow-style planning discussion. It is a roadmap, not a promise to implement every idea immediately.

Core principle:

> Build skills only when they make repeated Hermes behavior more predictable. Do not turn every interesting idea into a skill.

## Overview

| Skill | Status | Scope | One-line purpose |
|---|---|---|---|
| `personal-flow-os` | Implemented | Personal / business operating rhythm | Treat yourself like a company; Hermes acts as chief of staff. |
| `ai-lab-flow-triage` | Implemented | AI tool / repo / agent workflow evaluation | Sort AI discoveries into learn, test, track, incubate, or kill. |
| `daily-boss-review` | Candidate | Lightweight daily/weekly execution | Pick one daily boss and review weekly progress. |
| `ai-project-incubator` | Candidate | AI project validation and MVP design | Turn ideas into experiments, then projects, or kill them cleanly. |

## 1. `personal-flow-os`

**Type:** Personal / business operating system  
**Status:** Implemented  
**Recommended profiles:** `lab`, `life`, `learning`

### Purpose

Help define and maintain:

- 90-day mainline.
- Daily Boss.
- Weekly review.
- Life / business / learning rhythm.
- Personal and project focus across Telegram + Hermes + Obsidian.

### Good fit

Use when:

- You do not know what to prioritize today.
- AI tools and ideas are scattered everywhere.
- You want to turn life, business, learning, and projects into a recurring cycle.
- You want Hermes to act as a chief-of-staff style assistant.

### One-liner

> Treat yourself like a company; Hermes acts as chief of staff.

### Boundary

This skill should not replace formal company project management or Taiwan stock analysis. It is for personal operating rhythm and high-level focus.

## 2. `ai-lab-flow-triage`

**Type:** AI tool / GitHub repo / agent workflow evaluation  
**Status:** Implemented  
**Recommended profiles:** `lab`, `learning`, `work-ai` with work-safe boundaries

### Purpose

Use the Lab flow:

```text
Discover → Triage → Deep Dive → Experiment → Verdict → Incubate
```

To evaluate:

- AI tools.
- GitHub repos.
- MCP servers.
- Plugins.
- Agent skills.
- Developer workflows.
- AI product/course claims.

### Good fit

Use when:

- A new AI tool or repo looks interesting.
- You need to decide whether it is worth research or testing.
- You need a minimum viable experiment.
- You want useful findings archived into `D:/program/obsidian/claude/AI資訊/`.
- You need a clear verdict instead of another shiny bookmark.

### Verdict labels

- 🟢 可用
- 🟡 值得測
- 🔵 值得追蹤
- 🟠 值得學
- 🔴 不建議
- 🧸 漂亮玩具

### One-liner

> Sort AI discoveries into learn, test, track, incubate, or kill.

### Boundary

Do not confuse README claims, star count, demos, or UI polish with real capability. Check source, maintenance, license, permissions, data flow, and reproducible tests.

## 3. `daily-boss-review`

**Type:** Lightweight daily / weekly execution skill  
**Status:** Candidate  
**Recommended profiles:** `life`, `learning`, maybe `lab`

### Purpose

A smaller version of `personal-flow-os`, focused only on:

- Today's single highest-priority task.
- Weekly review.
- Avoiding priority sprawl.

### Good fit

Use when:

- You want a lightweight morning check-in.
- You ask: `今天要打哪隻 Boss？`
- You want weekly evidence of what actually moved.
- You do not want a full personal operating system.

### One-liner

> Pick one Daily Boss; do not open ten dungeons at once.

### Candidate implementation notes

This may remain as a template inside `personal-flow-os` unless repeated usage proves it deserves its own standalone skill.

Create it only if:

- `personal-flow-os` feels too heavy for daily use.
- Daily/weekly execution becomes a frequent standalone request.
- The smaller trigger improves skill selection.

## 4. `ai-project-incubator`

**Type:** AI project incubation skill  
**Status:** Candidate  
**Recommended profiles:** `lab`, `work-ai` with strict safety boundaries

### Purpose

Turn ideas, tools, repos, or workflows into safe, testable projects.

It should define:

- Problem.
- Existing alternatives.
- Why now.
- MVP.
- Non-goals.
- Success criteria.
- Exit criteria.
- Whether the idea should become a Hermes skill, plugin, MCP server, Obsidian workflow, GitHub repo, company project, or abandoned idea.

### Good fit

Use when:

- An AI idea seems promising but fuzzy.
- A repo/tool might become a Hermes skill, plugin, or MCP server.
- You need a small experiment before committing time.
- You want to avoid spending three days proving a cool demo has no durable value.

### One-liner

> Turn inspiration into experiments, experiments into projects, and weak ideas into clean exits.

### Candidate implementation notes

This may stay inside `ai-lab-flow-triage` until project incubation becomes frequent enough to justify a dedicated skill.

Create it only if:

- Many triage results become MVPs or repos.
- You need a separate project brief format.
- The skill can produce real artifacts, not just brainstorms.

## Recommended Evolution

### Current structure

Keep two implemented skills:

```text
personal-flow-os
ai-lab-flow-triage
```

Reason:

- Clear separation: personal rhythm vs AI research triage.
- Low maintenance cost.
- Fits the `lab` profile immediately.

### Future split conditions

Create `daily-boss-review` if:

- Daily focus prompts happen often.
- `personal-flow-os` is too broad for quick use.
- The desired output is usually only `今日 Boss` + `本週回顧`.

Create `ai-project-incubator` if:

- Many AI discoveries become actual MVPs.
- You need consistent project briefs and exit criteria.
- It starts to overlap too much with coding/project skills.

## Suggested Prompt Examples

### `personal-flow-os`

```text
/skill personal-flow-os
幫我做今天的 Daily Boss。我今天只有 2 小時，要從 AI Lab、Obsidian、公司專案裡選一個主線。
```

```text
/skill personal-flow-os
幫我設定接下來 90 天的 AI Lab 主線，目標是留下 3 個值得長期使用的 workflow。
```

### `ai-lab-flow-triage`

```text
/skill ai-lab-flow-triage
分析這個 GitHub repo 值不值得測，並設計 60 分鐘內可完成的最小實驗：https://github.com/owner/repo
```

```text
/skill ai-lab-flow-triage
這個 AI 工具看起來很紅，幫我判斷是值得測、值得追蹤，還是漂亮玩具。
```

### `daily-boss-review` candidate

```text
幫我選今天的 Daily Boss，並列出今天不做清單。
```

### `ai-project-incubator` candidate

```text
這個 idea 有沒有值得做成 Hermes skill / MCP server / GitHub project？請給 MVP、成功條件與退出條件。
```

## Safety Rules

- Do not copy proprietary course content, prompts, templates, or workflows.
- Do not connect unverified tools to production data.
- Ask before paid tools, external publishing, broad permissions, or sensitive credentials.
- Archive useful AI research into Obsidian only when it has practical value.
- Prefer small experiments over giant plans.
