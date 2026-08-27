# Kenny Hermes Skills

Personal Hermes skills maintained by Yaohsiang Ko (`keyu03`) with Hermes Agent assistance.

This repo is the source-of-truth for custom skills before syncing them into one or more local Hermes profiles.

## Implemented skills

| Skill | Purpose | Suggested profiles | Usage doc |
|---|---|---|---|
| `personal-flow-os` | 90-day focus, Daily Boss, weekly review, project incubation | `lab`, `life`, `learning` | [`docs/usage/personal-flow-os.md`](docs/usage/personal-flow-os.md) |
| `ai-lab-flow-triage` | AI tool/repo/agent/MCP/plugin triage, experiments, Obsidian archive | `lab`, `learning`, `work-ai` | [`docs/usage/ai-lab-flow-triage.md`](docs/usage/ai-lab-flow-triage.md) |

## Documentation rule

Every implemented skill must include a human usage doc:

```text
skills/<skill-name>/SKILL.md
docs/usage/<skill-name>.md
```

See [`docs/skill-documentation-standard.md`](docs/skill-documentation-standard.md).

Before committing a new skill, run:

```bash
python scripts/check-skill-docs.py
```

## Skill roadmap

See [`docs/skill-options-roadmap.md`](docs/skill-options-roadmap.md) for the organized skill map.

Current and candidate skills:

| Skill | Status | One-line purpose |
|---|---|---|
| `personal-flow-os` | Implemented | Treat yourself like a company; Hermes acts as chief of staff. |
| `ai-lab-flow-triage` | Implemented | Sort AI discoveries into learn, test, track, incubate, or kill. |
| `daily-boss-review` | Candidate | Pick one Daily Boss; do not open ten dungeons at once. |
| `ai-project-incubator` | Candidate | Turn inspiration into experiments, projects, or clean exits. |

## Layout

```text
skills/
  personal-flow-os/
    SKILL.md
  ai-lab-flow-triage/
    SKILL.md
docs/
  skill-documentation-standard.md
  skill-options-roadmap.md
  usage/
    personal-flow-os.md
    ai-lab-flow-triage.md
scripts/
  sync-to-profiles.py
  check-skill-docs.py
```

## Sync to a Hermes profile

From this repo:

```bash
python scripts/sync-to-profiles.py --profiles lab
```

Sync to several profiles:

```bash
python scripts/sync-to-profiles.py --profiles lab learning life
python scripts/sync-to-profiles.py --profiles lab work-ai --skills ai-lab-flow-triage
```

The script handles the default profile specially:

- `default` → `%LOCALAPPDATA%/hermes/skills/`
- named profile → `%LOCALAPPDATA%/hermes/profiles/<name>/skills/`

After syncing, restart or reload Hermes:

```text
/reload-skills
/reset
```

In Telegram, you can then load a skill with:

```text
/skill personal-flow-os
/skill ai-lab-flow-triage
```

## 什麼情境可以怎麼使用 Skill

### 1. `personal-flow-os`：個人 / 事業經營 OS

一句話：**把自己當公司經營，Hermes 當幕僚長。**

適合用在「方向、節奏、優先順序」這類問題：

| 情境 | 你可以這樣問 |
|---|---|
| 今天不知道先做什麼 | `/skill personal-flow-os`<br>`幫我選今天的 Daily Boss，我今天只有 2 小時。` |
| 任務太多、注意力很散 | `/skill personal-flow-os`<br>`我現在有這些事情：A、B、C，幫我收斂成一條主線和 side quests。` |
| 想規劃 90 天方向 | `/skill personal-flow-os`<br>`幫我設定接下來 90 天的 AI Lab 主線，並定義成功條件。` |
| 做每週回顧 | `/skill personal-flow-os`<br>`幫我做本週 Flow Review：完成什麼、卡在哪、下週主線是什麼。` |
| 想把人生 / 事業 / 學習變成週期系統 | `/skill personal-flow-os`<br>`幫我設計每週節奏：學習、AI Lab、公司專案、Obsidian 整理怎麼安排。` |

典型輸出會包含：

```text
今日 Boss
成功條件
時間盒
不做清單
Side Quests 停車場
下一步
```

使用範例：

```text
/skill personal-flow-os
幫我做今天的 Daily Boss。我今天有 2 小時，想推進 AI Lab，但也有公司專案和 Obsidian 要整理。
```

```text
/skill personal-flow-os
幫我設定接下來 90 天的 AI Lab 主線。目標是找出 3 個值得長期使用或做成專案的 AI workflow。
```

---

### 2. `ai-lab-flow-triage`：AI 工具 / Repo / Agent workflow 評估

一句話：**把 AI 新東西分流成可學、可測、可追蹤、可孵化，或安詳送走。**

適合用在「AI 技術雷達、工具評估、repo 分析、實驗設計」這類問題：

| 情境 | 你可以這樣問 |
|---|---|
| 看到一個 AI 工具，不知道值不值得研究 | `/skill ai-lab-flow-triage`<br>`分析這個工具的用途、風險、值不值得測：https://example.com/tool` |
| 看到 GitHub repo，想判斷是否值得 clone | `/skill ai-lab-flow-triage`<br>`這個 repo 值不值得測？請看 README、license、維護狀況和最小實驗：https://github.com/owner/repo` |
| 想檢查 MCP / plugin / skill / agent-facing 介面 | `/skill ai-lab-flow-triage`<br>`幫我看這個專案有沒有 MCP、OpenAPI、llms.txt、skills、plugins 或 tool discovery。` |
| 想設計最小可行實驗 | `/skill ai-lab-flow-triage`<br>`如果值得測，幫我設計 60 分鐘內可完成的最小實驗、成功條件和退出條件。` |
| 想歸檔到 Obsidian AI資訊 | `/skill ai-lab-flow-triage`<br>`如果這個工具值得追蹤，整理成 Obsidian AI資訊筆記。` |
| 想判斷能不能孵化成專案 | `/skill ai-lab-flow-triage`<br>`判斷這個 idea 能不能變成 Hermes skill、plugin、MCP server 或 GitHub project。` |

它會使用這個流程：

```text
Discover → Triage → Deep Dive → Experiment → Verdict → Incubate
```

Verdict 標籤：

| 標籤 | 意義 |
|---|---|
| 🟢 可用 | 已足夠在明確範圍內使用 |
| 🟡 值得測 | 有潛力，但需要小實驗驗證 |
| 🔵 值得追蹤 | 有趣但還不急或還不成熟 |
| 🟠 值得學 | 架構 / 模式值得學，不一定要用 |
| 🔴 不建議 | 風險、成本、品質或需求不匹配 |
| 🧸 漂亮玩具 | Demo/UI 漂亮，但缺乏耐用價值證據 |

使用範例：

```text
/skill ai-lab-flow-triage
分析這個 repo 值不值得測，並判斷能不能變成 Hermes skill 或 MCP server：https://github.com/owner/repo
```

```text
/skill ai-lab-flow-triage
這個 AI 工具看起來很紅，幫我判斷是值得測、值得追蹤，還是漂亮玩具。
```

---

### 3. 候選 Skill：`daily-boss-review`

一句話：**每天只抓一隻 Boss 打，不要同時開十條副本。**

目前尚未獨立實作，功能先包含在 `personal-flow-os` 裡。若每天常用，可以之後拆成輕量 skill。

適合情境：

- 每天早上快速決定今天最重要的一件事。
- 每週整理實際完成了什麼。
- 不想啟動完整 90 天規劃，只想要「今天做什麼」。

可先這樣使用：

```text
/skill personal-flow-os
只做輕量 Daily Boss Review：幫我選今天一件最重要的事，列成功條件和不做清單。
```

---

### 4. 候選 Skill：`ai-project-incubator`

一句話：**把靈感變成實驗，把實驗變成專案，把爛點子安詳送走。**

目前尚未獨立實作，功能先包含在 `ai-lab-flow-triage` 裡。若 AI idea 經常要變成 MVP / repo / skill / MCP server，可以之後拆出來。

適合情境：

- 想判斷一個 AI idea 值不值得做。
- 想把工具或 repo 變成 Hermes skill、plugin、MCP server 或 Obsidian workflow。
- 想設計 MVP、成功條件、退出條件。
- 想避免「看起來很酷但做了三天才發現沒用」。

可先這樣使用：

```text
/skill ai-lab-flow-triage
這個 idea 有沒有值得做成 Hermes skill / MCP server / GitHub project？請給 MVP、成功條件與退出條件。
```

## Safety notes

- These are personal workflow skills, not official Hermes bundled skills.
- Keep experiments away from production data.
- Ask before paid tools, external publishing, broad permissions, or sensitive credentials.
- Do not copy proprietary course prompts/templates/workflows into these skills.
