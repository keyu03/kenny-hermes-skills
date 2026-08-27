#!/usr/bin/env python
"""Check that every skill has a matching human usage doc.

Required mapping:
    skills/<skill-name>/SKILL.md -> docs/usage/<skill-name>.md
"""
from __future__ import annotations

import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "# {skill} 使用說明",
    "## 一句話",
    "## 解決什麼問題",
    "## 適合情境",
    "## 不適合情境",
    "## Telegram 使用方式",
    "## CLI 使用方式",
    "## 常用 Prompt 範例",
    "## 典型輸出",
    "## 安全與邊界",
    "## 維護備註",
]


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    skills_dir = repo_root / "skills"
    usage_dir = repo_root / "docs" / "usage"

    if not skills_dir.is_dir():
        print(f"ERROR: missing skills dir: {skills_dir}")
        return 2

    skill_names = sorted(p.name for p in skills_dir.iterdir() if (p / "SKILL.md").is_file())
    if not skill_names:
        print("ERROR: no skills found under ./skills")
        return 2

    errors: list[str] = []
    for skill in skill_names:
        doc = usage_dir / f"{skill}.md"
        if not doc.is_file():
            errors.append(f"missing usage doc for {skill}: {doc.relative_to(repo_root)}")
            continue

        text = doc.read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            expected = section.format(skill=skill)
            if expected not in text:
                errors.append(f"{doc.relative_to(repo_root)} missing section: {expected}")

    if errors:
        print("ERROR: skill documentation incomplete")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"OK skill docs complete: {len(skill_names)} skills checked")
    for skill in skill_names:
        print(f"- {skill} -> docs/usage/{skill}.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
