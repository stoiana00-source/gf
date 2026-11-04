# Shipping

This file is the source of truth for which skills ship and at what tier.
`scripts/verify_release.py` reads the table below and fails if it drifts from
`skills/`, the manifests or `README.md`.

**Counts:** 12 skills: 7 Stable · 11 Core, 1 Lite, 0 routing

## Tiers

Each skill has one **tier** (what kind of skill it is) and one **status** (how far it can be trusted).

| Tier | Meaning |
|---|---|
| Core | A full workflow: inputs it needs, a method, and a fixed output template |
| Lite | Reference guidance only: methods and checklists, no output template |
| routing | Picks and hands off to other skills; does no work of its own |

| Status | Meaning |
|---|---|
| Stable | Used on real work; its output format won't change without a release note |
| Beta | New or lightly tested; output may change between versions |

## Skills

| Skill | Tier | Status | Source |
|---|---|---|---|
| accessibility-review | Core | Stable | knowledge-work-plugins |
| design-critique | Core | Stable | knowledge-work-plugins |
| design-handoff | Core | Stable | knowledge-work-plugins |
| design-system | Core | Stable | knowledge-work-plugins |
| research-synthesis | Core | Stable | knowledge-work-plugins |
| user-research | Lite | Stable | knowledge-work-plugins |
| ux-copy | Core | Stable | knowledge-work-plugins |
| seo-audit | Core | Beta | original |
| keyword-research | Core | Beta | original |
| meta-tags | Core | Beta | original |
| schema-markup | Core | Beta | original |
| seo-content | Core | Beta | original |

## Releasing

1. Update the table above when a skill is added, removed, or changes tier or status.
2. Update the **Counts** line here, and the same counts in `.claude-plugin/plugin.json`,
   `.claude-plugin/marketplace.json` and `README.md`.
3. Bump `version` in both manifests and add a `## <version>` entry to `RELEASE-NOTES.md`.
4. Run `python3 scripts/verify_release.py` and fix anything it reports.
