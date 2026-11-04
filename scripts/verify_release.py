#!/usr/bin/env python3
"""Fail the release if the plugin's metadata has drifted.

Checks:
  1. `version` matches in .claude-plugin/plugin.json and this plugin's entry in
     .claude-plugin/marketplace.json, and is a MAJOR.MINOR.PATCH version.
  2. RELEASE-NOTES.md has a `## <version>` entry.
  3. The skills table in SHIPPING.md lists exactly the folders in skills/, each
     with a valid tier and status, and each SKILL.md has a matching `name` and
     a `description` in its frontmatter.
  4. The skill counts (total, Stable, Core, Lite, routing) computed from that
     table appear in SHIPPING.md's Counts line, both manifest descriptions and
     README.md.

Usage: python3 scripts/verify_release.py [repo_root]
Exits 0 when everything matches, 1 otherwise. Standard library only.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

TIERS = ("Core", "Lite", "routing")
STATUSES = ("Stable", "Beta")
COUNT_LABELS = ("skills", "Stable") + TIERS
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")


def read_json(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"{path}: file missing")
    except json.JSONDecodeError as exc:
        errors.append(f"{path}: invalid JSON ({exc})")
    return {}


def read_text(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append(f"{path}: file missing")
        return ""


def frontmatter(text: str) -> dict[str, str]:
    """Top-level `key: value` pairs from a leading --- block."""
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep and not line.startswith((" ", "\t")):
            fields[key.strip()] = value.strip().strip("\"'")
    return fields


def shipping_table(text: str) -> list[tuple[str, str, str]]:
    """(skill, tier, status) rows from the table under `## Skills`."""
    section = re.search(r"^## Skills\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not section:
        return []
    rows = []
    for line in section.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or not line.strip().startswith("|"):
            continue
        if cells[0].lower() == "skill" or set(cells[0]) <= set("-: "):
            continue
        rows.append((cells[0].strip("`"), cells[1], cells[2]))
    return rows


def find_counts(text: str) -> dict[str, int]:
    """Numbers written before each count label, e.g. `7 Stable`."""
    found = {}
    for label in COUNT_LABELS:
        match = re.search(rf"\b(\d+)\s+{label}\b", text, re.I)
        if match:
            found[label] = int(match.group(1))
    return found


def main(root: Path) -> int:
    errors: list[str] = []
    plugin_path = root / ".claude-plugin" / "plugin.json"
    market_path = root / ".claude-plugin" / "marketplace.json"
    plugin = read_json(plugin_path, errors)
    market = read_json(market_path, errors)

    # 1. Versions
    name = plugin.get("name")
    version = plugin.get("version")
    entries = [p for p in market.get("plugins", []) if p.get("name") == name]
    if not version:
        errors.append(f"{plugin_path}: no version")
    elif not SEMVER.match(version):
        errors.append(f"{plugin_path}: version {version!r} is not MAJOR.MINOR.PATCH")
    if len(entries) != 1:
        errors.append(f"{market_path}: expected one plugin entry named {name!r}, found {len(entries)}")
        entry = {}
    else:
        entry = entries[0]
        if entry.get("version") != version:
            errors.append(
                f"version mismatch: plugin.json has {version!r}, "
                f"marketplace.json has {entry.get('version')!r}"
            )

    # 2. Release notes
    notes = read_text(root / "RELEASE-NOTES.md", errors)
    if version and notes and not re.search(rf"^##\s+v?{re.escape(version)}\b", notes, re.M):
        errors.append(f"RELEASE-NOTES.md: no '## {version}' entry")

    # 3. Skills vs SHIPPING.md
    shipping = read_text(root / "SHIPPING.md", errors)
    rows = shipping_table(shipping)
    if shipping and not rows:
        errors.append("SHIPPING.md: no rows found in the table under '## Skills'")
    listed = [r[0] for r in rows]
    for dup in sorted({s for s in listed if listed.count(s) > 1}):
        errors.append(f"SHIPPING.md: {dup} is listed more than once")

    skills_dir = root / "skills"
    on_disk = sorted(p.parent.name for p in skills_dir.glob("*/SKILL.md"))
    for missing in sorted(set(on_disk) - set(listed)):
        errors.append(f"SHIPPING.md: skills/{missing} is not listed")
    for extra in sorted(set(listed) - set(on_disk)):
        errors.append(f"SHIPPING.md: {extra} is listed but skills/{extra}/SKILL.md does not exist")

    for skill, tier, status in rows:
        if tier not in TIERS:
            errors.append(f"SHIPPING.md: {skill} has tier {tier!r}; use one of {', '.join(TIERS)}")
        if status not in STATUSES:
            errors.append(f"SHIPPING.md: {skill} has status {status!r}; use one of {', '.join(STATUSES)}")

    for skill in on_disk:
        path = skills_dir / skill / "SKILL.md"
        meta = frontmatter(path.read_text(encoding="utf-8"))
        if not meta:
            errors.append(f"{path}: no frontmatter")
            continue
        if meta.get("name") != skill:
            errors.append(f"{path}: frontmatter name {meta.get('name')!r} does not match folder {skill!r}")
        if not meta.get("description"):
            errors.append(f"{path}: frontmatter has no description")

    # 4. Counts
    expected = {
        "skills": len(rows),
        "Stable": sum(1 for r in rows if r[2] == "Stable"),
        **{t: sum(1 for r in rows if r[1] == t) for t in TIERS},
    }
    counts_line = next((l for l in shipping.splitlines() if l.startswith("**Counts:**")), "")
    if shipping and not counts_line:
        errors.append("SHIPPING.md: no '**Counts:**' line")
    sources = {
        "SHIPPING.md Counts line": counts_line,
        "plugin.json description": plugin.get("description", ""),
        "marketplace.json description": entry.get("description", ""),
        "README.md": read_text(root / "README.md", errors),
    }
    for where, text in sources.items():
        if not text:
            continue
        found = find_counts(text)
        for label, want in expected.items():
            got = found.get(label)
            if got is None:
                errors.append(f"{where}: no '{want} {label}' count")
            elif got != want:
                errors.append(f"{where}: says {got} {label}, SHIPPING.md table has {want}")

    summary = ", ".join(f"{expected[l]} {l}" for l in COUNT_LABELS)
    if errors:
        print(f"verify_release: {len(errors)} problem(s) for version {version}:")
        for err in errors:
            print(f"  - {err}")
        return 1
    print(f"verify_release: OK — version {version}, {summary}")
    return 0


if __name__ == "__main__":
    repo = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    sys.exit(main(repo))
