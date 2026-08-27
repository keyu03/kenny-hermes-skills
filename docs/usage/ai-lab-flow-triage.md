# ai-lab-flow-triage 使用說明

## 一句話

把 AI 新東西分流成可學、可測、可追蹤、可孵化，或安詳送走。

## 解決什麼問題

`ai-lab-flow-triage` 用來避免 AI 工具焦慮與 repo 收藏癖。

它會用 Lab 的流程：

```text
Discover → Triage → Deep Dive → Experiment → Verdict → Incubate
```

幫你判斷一個 AI 工具、GitHub repo、Agent workflow、MCP server、plugin 或 skill：

- 解決什麼問題？
- 是否真的比現有做法好？
- 架構、tool interface、權限與資料流是什麼？
- 安裝與維運成本高不高？
- 授權、安全、企業使用風險是什麼？
- 最小可行實驗怎麼設計？
- 要不要歸檔到 Obsidian？
- 值不值得孵化成 skill / plugin / MCP server / GitHub project？

## 適合情境

- 看到一個 AI 工具，不知道值不值得研究。
- 看到一個 GitHub repo，想知道要不要 clone 實測。
- 想確認專案是否有 MCP、OpenAPI、llms.txt、skills、plugins 或 tool discovery。
- 想把 AI link/repo 變成 Obsidian AI資訊筆記。
- 想設計 60–120 分鐘內可完成的最小可行實驗。
- 想判斷一個 idea 是否值得做成 Hermes skill、plugin、MCP server 或專案。

## 不適合情境

- 不適合直接做正式公司 production rollout。
- 不適合只存連結不分析；那是收集箱，不是 triage。
- 不適合只看 README 就下結論。
- 不適合把 star 數、漂亮 UI、demo 影片當能力證明。
- 不適合執行需要敏感權限或付費 API 的工具，除非使用者明確同意。

## Telegram 使用方式

```text
/skill ai-lab-flow-triage
分析這個工具的用途、風險、值不值得測：https://example.com/tool
```

```text
/skill ai-lab-flow-triage
分析這個 repo 值不值得測，並判斷能不能變成 Hermes skill 或 MCP server：https://github.com/owner/repo
```

## CLI 使用方式

```bash
hermes -p lab -s ai-lab-flow-triage
```

單次 query：

```bash
hermes -p lab -s ai-lab-flow-triage chat -q "分析這個 repo 是否值得測：https://github.com/owner/repo"
```

## 常用 Prompt 範例

### AI 工具分析

```text
/skill ai-lab-flow-triage
這個 AI 工具看起來很紅，幫我判斷是值得測、值得追蹤，還是漂亮玩具：https://example.com/tool
```

### GitHub repo triage

```text
/skill ai-lab-flow-triage
這個 GitHub repo 值不值得 clone 實測？請檢查 README、license、維護狀況、tests、agent-facing surfaces，最後給 Verdict：https://github.com/owner/repo
```

### MCP / Plugin / Skill 檢查

```text
/skill ai-lab-flow-triage
幫我看這個專案有沒有 MCP、OpenAPI、llms.txt、skills、plugins、tool discovery 或可被 agent 使用的介面。
```

### 最小可行實驗

```text
/skill ai-lab-flow-triage
如果這個工具值得測，請設計 60 分鐘內可完成的最小實驗，包含成功條件、退出條件、風險控制。
```

### 專案孵化

```text
/skill ai-lab-flow-triage
這個 idea 有沒有值得做成 Hermes skill / MCP server / plugin / GitHub project？請給 MVP、成功條件與退出條件。
```

## 典型輸出

```markdown
## 一句話

## 它解決什麼問題？

## 對我的實際幫助

## 架構 / Tool Interface / 權限 / 資料流

## 安裝與維運成本

## 安全 / 隱私 / 授權風險

## 最小可行實驗

## Verdict

判定：🟡 值得測
值不值得看：
值不值得測：
建議投入時間：
可能產生價值：
主要風險：
下一步：

## Incubation Decision
```

## Verdict 標籤

| 標籤 | 意義 |
|---|---|
| 🟢 可用 | 已足夠在明確範圍內使用 |
| 🟡 值得測 | 有潛力，但需要小實驗驗證 |
| 🔵 值得追蹤 | 有趣但還不急或還不成熟 |
| 🟠 值得學 | 架構 / 模式值得學，不一定要用 |
| 🔴 不建議 | 風險、成本、品質或需求不匹配 |
| 🧸 漂亮玩具 | Demo/UI 漂亮，但缺乏耐用價值證據 |

## 安全與邊界

- 優先用免費、公開、可重現來源查證。
- 執行陌生 repo 前，先看安裝腳本與權限需求。
- 不要把未驗證工具接到正式公司資料或 production credentials。
- 會產生費用、對外發布、寫入外部服務、需要敏感權限時，必須先確認。
- 課程、付費模板、proprietary prompts/workflows 只能做高層次分析，不可複製進 repo。

## 維護備註

如果未來 triage 後經常要進入 MVP / repo / skill / MCP server 設計，可以把「孵化」部分拆成候選 skill：`ai-project-incubator`。
