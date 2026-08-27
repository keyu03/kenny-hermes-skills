# Skill Documentation Standard

本文件定義 `kenny-hermes-skills` repo 的文件規範：**每新增一個 skill，就必須同步新增一份使用說明文件**。

這份規範的目的不是把文件寫得很華麗，而是讓未來的自己可以快速回答三個問題：

1. 這個 skill 解決什麼問題？
2. 什麼情境該用它、不該用它？
3. 在 Telegram / CLI 裡到底要怎麼叫它？

如果一個 skill 沒有使用說明，它就像沒有標籤的藥罐：可能有效，但誰敢吞。

## 必填規則

每個 skill 都必須同時有：

```text
skills/<skill-name>/SKILL.md
docs/usage/<skill-name>.md
```

例如：

```text
skills/personal-flow-os/SKILL.md
docs/usage/personal-flow-os.md
```

## 新增 Skill Checklist

新增 skill 時，請完成：

- [ ] 建立 `skills/<skill-name>/SKILL.md`。
- [ ] 建立 `docs/usage/<skill-name>.md`。
- [ ] 在 `README.md` 的 `Implemented skills` 表格加入 skill。
- [ ] 在 `README.md` 的「Skill 使用說明文件」區塊加入 usage doc 連結。
- [ ] 若是未來候選方向，更新 `docs/skill-options-roadmap.md`。
- [ ] 執行 `python scripts/check-skill-docs.py`。
- [ ] 確認輸出為 `OK` 後再 commit。

## Usage Doc 必填內容

每份 `docs/usage/<skill-name>.md` 至少要包含：

```markdown
# <skill-name> 使用說明

## 一句話

## 解決什麼問題

## 適合情境

## 不適合情境

## Telegram 使用方式

## CLI 使用方式

## 常用 Prompt 範例

## 典型輸出

## 安全與邊界

## 維護備註
```

## 建議寫法

### 一句話

用一句人話說明這個 skill 的價值。

好的例子：

> 把 AI 新工具分流成可學、可測、可追蹤、可孵化，或安詳送走。

不好的例子：

> This is a comprehensive powerful next-generation workflow optimization skill.

看到 `comprehensive powerful next-generation` 可以先泡杯咖啡，然後刪掉。

### 適合情境

寫實際會發生的使用情境，不要只寫抽象概念。

好的例子：

- 看到一個 GitHub repo，想知道值不值得 clone 實測。
- 今天任務太多，需要選一個 Daily Boss。

### 不適合情境

明確寫出邊界，避免 skill 被亂用。

例如：

- 不要用個人 workflow skill 取代正式公司專案治理。
- 不要把未驗證 AI 工具接上正式資料。
- 不要複製 proprietary course prompt/template/workflow。

### 使用方式

至少提供 Telegram 與 CLI 範例：

```text
/skill <skill-name>
你的任務描述
```

```bash
hermes -p lab -s <skill-name>
hermes -p lab -s <skill-name> chat -q "你的任務描述"
```

### 常用 Prompt 範例

每個 skill 至少放 3 個可直接複製的 prompt。

## 驗證方式

執行：

```bash
python scripts/check-skill-docs.py
```

成功時應看到類似：

```text
OK skill docs complete: 2 skills checked
```

如果缺文件，腳本會列出缺少的 `docs/usage/<skill-name>.md`。

## 維護原則

- `SKILL.md` 寫給 Hermes agent 看：偏程序、規則、觸發條件。
- `docs/usage/*.md` 寫給人看：偏情境、範例、怎麼用。
- README 只放快速入口，不要塞完整長文。
- 每次改 skill 行為，如果會影響使用方式，也要同步更新 usage doc。
- 候選 skill 可以先放在 roadmap；真正建立 `skills/<name>/SKILL.md` 時，就必須補 usage doc。
