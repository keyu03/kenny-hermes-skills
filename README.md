# Kenny Hermes Skills

Personal Hermes skills maintained by Yaohsiang Ko (`keyu03`) with Hermes Agent assistance.

This repo is the source-of-truth for custom skills before syncing them into one or more local Hermes profiles.

## Implemented skills

| Skill | Purpose | Suggested profiles |
|---|---|---|
| `personal-flow-os` | 90-day focus, Daily Boss, weekly review, project incubation | `lab`, `life`, `learning` |
| `ai-lab-flow-triage` | AI tool/repo/agent/MCP/plugin triage, experiments, Obsidian archive | `lab`, `learning`, `work-ai` |

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
  skill-options-roadmap.md
scripts/
  sync-to-profiles.py
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

## Usage examples

```text
/skill personal-flow-os
幫我做今天的 Daily Boss。我今天有 2 小時，想推進 AI Lab。
```

```text
/skill ai-lab-flow-triage
分析這個 repo 值不值得測：https://github.com/owner/repo
```

## Safety notes

- These are personal workflow skills, not official Hermes bundled skills.
- Keep experiments away from production data.
- Ask before paid tools, external publishing, broad permissions, or sensitive credentials.
- Do not copy proprietary course prompts/templates/workflows into these skills.
