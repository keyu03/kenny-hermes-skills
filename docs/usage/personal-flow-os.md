# personal-flow-os 使用說明

## 一句話

把自己當公司經營，Hermes 當幕僚長：幫你收斂 90 天主線、每日 Boss、週回顧與個人/事業節奏。

## 解決什麼問題

`personal-flow-os` 用來處理「方向太多、任務太散、每天不知道先做什麼」的問題。

它不是單純 todo list，也不是心靈雞湯。它的重點是：

- 把 90 天方向變成一條主線。
- 把每天的焦點變成一隻 Daily Boss。
- 把其他有趣但不急的東西放進 Side Quests 停車場。
- 透過週回顧確認你真的有前進，而不是只是在換工具。

## 適合情境

- 今天不知道先做哪件事。
- AI 工具、專案、Obsidian、公司事情全部混在一起。
- 想設定接下來 90 天的主線。
- 想做每週回顧，確認什麼有推進、什麼卡住。
- 想把人生、事業、學習、AI Lab 變成一套週期節奏。
- 想讓 Hermes 幫你做「幕僚長式」優先順序判斷。

## 不適合情境

- 不適合取代正式公司專案管理。
- 不適合做台股分析。
- 不適合拿來硬排滿每天所有時間。
- 不適合把所有 side quests 都升級成正式任務。
- 不適合複製任何 proprietary course 的 prompt/template/workflow。

## Telegram 使用方式

```text
/skill personal-flow-os
幫我做今天的 Daily Boss。我今天有 2 小時，想推進 AI Lab，但也有公司專案和 Obsidian 要整理。
```

```text
/skill personal-flow-os
幫我做本週 Flow Review：完成什麼、卡在哪、下週主線是什麼。
```

## CLI 使用方式

```bash
hermes -p lab -s personal-flow-os
```

單次 query：

```bash
hermes -p lab -s personal-flow-os chat -q "幫我設定接下來 90 天的 AI Lab 主線。"
```

## 常用 Prompt 範例

### 每日 Boss

```text
/skill personal-flow-os
幫我選今天的 Daily Boss。我今天只有 2 小時，候選任務有：A、B、C。請選一個，列成功條件、時間盒、不做清單。
```

### 任務收斂

```text
/skill personal-flow-os
我現在事情太散：AI 工具研究、Obsidian 整理、公司專案、學習 MCP。幫我分成主線、side quests、停車場、要殺掉的項目。
```

### 90 天主線

```text
/skill personal-flow-os
幫我設定接下來 90 天主線。目標是讓 AI Lab 產出 3 個可長期使用的 workflow 或 skill。
```

### 週回顧

```text
/skill personal-flow-os
幫我做本週回顧：我做了哪些事、哪些有證據、哪些只是忙、下週只該推進哪一條主線？
```

## 典型輸出

```markdown
## 今日 Boss

任務：
成功條件：
時間盒：
需要工具：
完成後輸出：

## 不做清單

## Side Quests 停車場

## 下一步
```

或：

```markdown
## 90 天主線

## 成功條件

## 每週節奏

## Daily Boss 規則

## 不做清單

## 90 天結束要留下的資產
```

## 安全與邊界

- 如果任務涉及公司正式資料，應切到 `work-ai` 的正式治理流程。
- 如果任務涉及投資或持股，應切到 `stocks-tw`。
- 不要讓這個 skill 幫你做所有事情；它的價值是收斂，不是塞滿。
- 如果輸出沒有「一個明確下一步」，就還沒完成。

## 維護備註

如果未來每天只想快速問「今天打哪隻 Boss」，而 `personal-flow-os` 太重，可以把那一段拆成候選 skill：`daily-boss-review`。
