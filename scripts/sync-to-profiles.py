#!/usr/bin/env python
"""Sync Kenny Hermes skills into local Hermes profiles.

Usage:
    python scripts/sync-to-profiles.py --profiles lab
    python scripts/sync-to-profiles.py --profiles lab learning life
    python scripts/sync-to-profiles.py --profiles lab work-ai --skills ai-lab-flow-triage
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

DEFAULT_SKILLS = ["personal-flow-os", "ai-lab-flow-triage"]


def default_hermes_home() -> Path:
    local = os.environ.get("LOCALAPPDATA")
    if local:
        return Path(local) / "hermes"
    return Path.home() / "AppData" / "Local" / "hermes"


def profile_skills_dir(hermes_home: Path, profile: str) -> Path:
    if profile == "default":
        return hermes_home / "skills"
    return hermes_home / "profiles" / profile / "skills"


def sync_skill(repo_root: Path, hermes_home: Path, profile: str, skill: str, category: str) -> Path:
    src = repo_root / "skills" / skill
    if not (src / "SKILL.md").is_file():
        raise FileNotFoundError(f"Missing skill source: {src / 'SKILL.md'}")

    dst = profile_skills_dir(hermes_home, profile) / category / skill
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    return dst


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync personal Hermes skills to profiles.")
    parser.add_argument("--profiles", nargs="+", default=["lab"], help="Profiles to sync into. Use 'default' for root profile.")
    parser.add_argument("--skills", nargs="+", default=DEFAULT_SKILLS, help="Skill names under ./skills to sync.")
    parser.add_argument("--category", default="kenny", help="Destination category folder under each profile's skills directory.")
    parser.add_argument("--hermes-home", default=None, help="Hermes home path. Defaults to LOCALAPPDATA/hermes.")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    hermes_home = Path(args.hermes_home) if args.hermes_home else default_hermes_home()

    print(f"repo_root={repo_root}")
    print(f"hermes_home={hermes_home}")

    copied: list[Path] = []
    for profile in args.profiles:
        for skill in args.skills:
            dst = sync_skill(repo_root, hermes_home, profile, skill, args.category)
            copied.append(dst)
            print(f"synced {skill} -> profile={profile}: {dst}")

    print(f"done: {len(copied)} skill copies")
    print("next: /reload-skills then /reset in Hermes gateway/CLI sessions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
