---
name: personal-flow-os
description: Run 90-day focus, daily boss, and reviews.
version: 0.1.0
author: Yaohsiang Ko (keyu03), Hermes Agent
license: MIT
platforms: [windows]
metadata:
  hermes:
    tags: [PersonalOS, Planning, Review, Obsidian, Focus]
    related_skills: [ai-info-obsidian-archive]
  created_by: agent
---

# Personal Flow OS Skill

Use this skill to turn scattered goals, AI-tool ideas, project threads, and daily work into a focused operating rhythm. It is inspired by generic planning patterns: 90-day focus, weekly review, daily priority, project incubation, and AI-assisted reflection.

This skill is **not** a clone of FlowCEO, FlowGPS, or any paid course/template. Do not copy proprietary course content, prompts, workflows, or templates; use only the user's own context and original outputs.

## When to Use

Use when the user asks to:

- Set or review a 90-day personal, business, or AI-lab direction.
- Decide today's most important task.
- Convert scattered goals into one mainline and a few side quests.
- Run a daily check-in, weekly review, monthly triage, or 90-day reset.
- Reduce AI-tool anxiety by choosing fewer, higher-value actions.
- Decide whether an idea should become a note, recurring workflow, skill, plugin, repo, or dead idea.

Don't use for:

- Formal company AI / BI / API / Agent delivery; route to `work-ai` or a formal project workflow.
- Taiwan stock analysis; route to `stocks-tw` / finance skills.
- Deep GitHub repo verification; use GitHub research skills first, then return here for prioritization.
- Recreating paid-course material from FlowCEO or any other proprietary source.

## Prerequisites

- Preferred language: Traditional Chinese.
- Preferred operating style: direct, practical, lightly humorous, evidence-based.
- Default Obsidian vault for durable notes: `D:/program/obsidian/claude`.
- Default AI information folder: `D:/program/obsidian/claude/AI資訊/`.
- Use local-first, free, open-source, and self-hostable workflows where possible.
- Ask before paid tools, paid APIs, external publishing, or sensitive permissions.
- Do not connect experimental workflows to production data.

## How to Run

In Telegram / gateway:

```text
/skill personal-flow-os
幫我做今天的 Daily Boss。我今天有 2 小時，想推進 AI Lab，但也有公司專案和 Obsidian 要整理。
```

In CLI:

```bash
hermes -p lab -s personal-flow-os
hermes -p lab -s personal-flow-os chat -q "幫我設定接下來 90 天的 AI Lab 主線。"
```

After creating or syncing the skill, use `/reload-skills` and usually `/reset` so the running session sees it.

## Quick Reference

| Need | User prompt |
|---|---|
| Daily focus | `用 personal-flow-os 幫我選今天的 Daily Boss。` |
| Weekly review | `幫我做本週 Flow Review，決定下週主線。` |
| 90-day plan | `幫我設定接下來 90 天的主線與成功條件。` |
| Stuck state | `我現在事情太散，幫我收斂成一條主線。` |
| Project incubation | `這個想法值得孵化成 skill/plugin/MCP 嗎？` |

## Core Model

Use five layers:

1. **North Star** — what outcome makes the next 90 days worthwhile?
2. **Mainline** — the one direction that must keep moving.
3. **Side Quests** — useful but secondary experiments that cannot steal the mainline.
4. **Daily Boss** — one concrete task that makes today successful.
5. **Review Loop** — daily check-in, weekly review, monthly triage, 90-day reset.

## AI Roles

Activate these roles explicitly when useful:

### Radar Scout

Finds relevant AI tools, repos, models, agents, skills, plugins, MCP servers, or workflows.

Output:

- What it is.
- Why it matters.
- Whether it is hype, useful, risky, or worth testing.
- Source links when fetched.

### Skeptical Engineer

Pushes back against marketing claims.

Check:

- Is there source code?
- Is there a working demo?
- Is it maintained?
- Are there tests?
- What permissions does it need?
- Can it run locally?
- What breaks in real usage?

### Experiment Designer

Turns ideas into small tests.

Each experiment needs:

- Hypothesis.
- Setup.
- Minimum viable test.
- Success criteria.
- Exit criteria.
- Time box.

### Obsidian Archivist

Saves durable findings into the Obsidian vault when useful.

Each saved note should include:

- Source.
- Date.
- Summary.
- Practical value.
- Limits.
- Verdict.
- Next step.

### Incubator

Decides whether something should become:

- One-off note.
- Recurring workflow.
- Hermes skill.
- Plugin.
- MCP server.
- GitHub project.
- Company-side project.
- Dead idea.

## Procedure

### 1. Identify the session type

Classify the request as one of:

- Daily check-in.
- Weekly review.
- 90-day planning.
- AI tool triage.
- Project incubation.
- Stuck-state debugging.

If the task is obvious, proceed without asking.

Completion criteria:

- Session type is identified.
- The user has one concrete output target.

### 2. Take a current-state snapshot

Collect only the minimum needed context. Ask, search past sessions, or read Obsidian only when it materially improves the result.

Separate:

- Mainline.
- Side quests.
- Blockers.
- Commitments.
- Parking lot.

Completion criteria:

- No more than 3 active priorities remain.
- The mainline is separate from side quests.

### 3. Triage commitments

Classify each item:

| Status | Meaning |
|---|---|
| Mainline | Directly advances the current 90-day goal |
| Side Quest | Interesting but not urgent |
| Incubate | Could become a project or skill |
| Archive | Worth saving, not acting now |
| Kill | Not worth more attention |

Rules:

- New does not mean important.
- If there is no next action, it is not a priority.
- If there are more than 3 priorities, anxiety is wearing a fake moustache.

Completion criteria:

- Every item has one status.
- The user has one recommended next action.

### 4. Define Today's Boss

Pick exactly one Daily Boss.

A good Daily Boss is:

- Specific.
- Finishable today.
- Evidence-based.
- Connected to the mainline.
- Not merely `research more`.

Use this format:

```markdown
## 今日 Boss

任務：
成功條件：
時間盒：
需要工具：
完成後輸出：

## 不做清單

## Side Quests 停車場
```

Completion criteria:

- One task only.
- Success condition is verifiable.

### 5. Design experiments when needed

For AI tools, repos, MCP servers, skills, plugins, or agent workflows, use:

```markdown
## 最小可行實驗

假設：
為什麼值得測：
安裝 / 前置需求：
測試步驟：
成功條件：
退出條件：
預估時間：
風險：
```

Completion criteria:

- The experiment avoids production data.
- The user knows when to stop.

### 6. Give a verdict

Use one of:

- 🟢 可用
- 🟡 值得測
- 🔵 值得追蹤
- 🟠 值得學
- 🔴 不建議
- 🧸 漂亮玩具

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

- Recommendation is explicit.
- Next step is actionable.

### 7. Archive durable outputs

If useful beyond the current chat, save to Obsidian.

Default folders:

```text
AI資訊/AI工具/
AI資訊/AI開發工作流/
AI資訊/平台比較/
AI資訊/AI新資訊收集箱.md
```

Use `write_file` for new notes and `patch` for index updates.

Completion criteria:

- Note exists.
- Source links are preserved.
- The note is linked from `AI資訊/AI資訊總覽.md` when index-worthy.

## Templates

### Daily Check-in

```markdown
# Daily Flow Check-in

日期：

## 今日狀態

能量：
注意力：
目前卡點：

## 90 天主線

目前主線：

## 今日 Boss

任務：
成功條件：
時間盒：

## Side Quests 停車場

- 

## 今日結束前要留下的證據

- 
```

### Weekly Review

```markdown
# Weekly Flow Review

週期：

## 本週主線

原本想推進：
實際推進：

## 完成的證據

- 

## 卡住的地方

- 

## AI / Tool / Repo 發現

| 名稱 | 類型 | Verdict | 下一步 |
|---|---|---|---|

## 下週主線

只選一個：

## 下週不要做

- 
```

### Project Incubation Brief

```markdown
# Project Incubation Brief

專案名稱：

## 問題

這解決誰的什麼問題？

## 現有替代方案

目前怎麼解？

## 為什麼現在值得做？

## 最小可行版本

第一版只做什麼？

## 不做什麼

- 

## 成功條件

- 

## 退出條件

- 

## 可能變成

- [ ] Obsidian note
- [ ] Hermes skill
- [ ] MCP server
- [ ] plugin
- [ ] GitHub repo
- [ ] 公司專案
- [ ] 放棄
```

## Pitfalls

- Do not turn every interesting link into a project.
- Do not turn every repeated thought into a skill.
- Do not optimize the system instead of doing the work.
- Do not connect experimental workflows to production data.
- Do not copy proprietary course content, prompts, templates, or workflows.
- Do not let side quests steal the Daily Boss.
- Do not use this skill to make formal work commitments without a separate work-project workflow.

## Verification

A session using this skill is successful only if it produces at least one of:

- Clear Daily Boss.
- 90-day mainline.
- Weekly review.
- Saved Obsidian note.
- Minimum viable experiment.
- Kill / archive / incubate decision.
- Concrete next action with success criteria.

Before finalizing, check:

- Is there exactly one recommended next action?
- Is the action small enough to execute?
- Is the output grounded in sources or user-provided context?
- Did we avoid copying proprietary external content?
- Did we save durable findings when appropriate?
