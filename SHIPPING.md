# Shipping

This file is the source of truth for which skills ship and at what tier.
`scripts/verify_release.py` reads the table below and fails if it drifts from
`skills/`, the manifests or `README.md`.

**Counts:** 79 skills: 7 Stable · 11 Core, 68 Lite, 0 routing

## Tiers

Each skill has one **tier** (what kind of skill it is) and one **status** (how far it can be trusted).

| Tier | Meaning |
|---|---|
| Core | A full workflow: inputs it needs, a method, and a fixed output template |
| Lite | Reference guidance only: methods, checklists, or one visual style's tokens and rules; no step-by-step workflow |
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
| style-agentic | Lite | Beta | awesome-design-skills |
| style-arcade | Lite | Beta | awesome-design-skills |
| style-artistic | Lite | Beta | awesome-design-skills |
| style-basic | Lite | Beta | awesome-design-skills |
| style-bento | Lite | Beta | awesome-design-skills |
| style-blank-canvas | Lite | Beta | awesome-design-skills |
| style-blocks | Lite | Beta | awesome-design-skills |
| style-bold | Lite | Beta | awesome-design-skills |
| style-brutalism | Lite | Beta | awesome-design-skills |
| style-cafe | Lite | Beta | awesome-design-skills |
| style-claymorphism | Lite | Beta | awesome-design-skills |
| style-clean | Lite | Beta | awesome-design-skills |
| style-colorful | Lite | Beta | awesome-design-skills |
| style-contemporary | Lite | Beta | awesome-design-skills |
| style-corporate | Lite | Beta | awesome-design-skills |
| style-cosmic | Lite | Beta | awesome-design-skills |
| style-creative | Lite | Beta | awesome-design-skills |
| style-dithered | Lite | Beta | awesome-design-skills |
| style-doodle | Lite | Beta | awesome-design-skills |
| style-dramatic | Lite | Beta | awesome-design-skills |
| style-editorial | Lite | Beta | awesome-design-skills |
| style-eight-bit | Lite | Beta | awesome-design-skills |
| style-enterprise | Lite | Beta | awesome-design-skills |
| style-expressive | Lite | Beta | awesome-design-skills |
| style-fantasy | Lite | Beta | awesome-design-skills |
| style-fiction | Lite | Beta | awesome-design-skills |
| style-flat | Lite | Beta | awesome-design-skills |
| style-friendly | Lite | Beta | awesome-design-skills |
| style-futuristic | Lite | Beta | awesome-design-skills |
| style-geometric | Lite | Beta | awesome-design-skills |
| style-glassmorphism | Lite | Beta | awesome-design-skills |
| style-gradient | Lite | Beta | awesome-design-skills |
| style-immersive | Lite | Beta | awesome-design-skills |
| style-impeccable | Lite | Beta | awesome-design-skills |
| style-layered | Lite | Beta | awesome-design-skills |
| style-levels | Lite | Beta | awesome-design-skills |
| style-matrix | Lite | Beta | awesome-design-skills |
| style-minimal | Lite | Beta | awesome-design-skills |
| style-modern | Lite | Beta | awesome-design-skills |
| style-mono | Lite | Beta | awesome-design-skills |
| style-neobrutalism | Lite | Beta | awesome-design-skills |
| style-neon | Lite | Beta | awesome-design-skills |
| style-neumorphism | Lite | Beta | awesome-design-skills |
| style-paper | Lite | Beta | awesome-design-skills |
| style-perspective | Lite | Beta | awesome-design-skills |
| style-playful-rounded | Lite | Beta | awesome-design-skills |
| style-power | Lite | Beta | awesome-design-skills |
| style-premium | Lite | Beta | awesome-design-skills |
| style-professional | Lite | Beta | awesome-design-skills |
| style-pulse | Lite | Beta | awesome-design-skills |
| style-purple-dashboard | Lite | Beta | awesome-design-skills |
| style-refined | Lite | Beta | awesome-design-skills |
| style-research-journal | Lite | Beta | awesome-design-skills |
| style-retro | Lite | Beta | awesome-design-skills |
| style-riso | Lite | Beta | awesome-design-skills |
| style-sketch | Lite | Beta | awesome-design-skills |
| style-skeumorphism | Lite | Beta | awesome-design-skills |
| style-sleek | Lite | Beta | awesome-design-skills |
| style-spacious | Lite | Beta | awesome-design-skills |
| style-square | Lite | Beta | awesome-design-skills |
| style-stitch | Lite | Beta | awesome-design-skills |
| style-storytelling | Lite | Beta | awesome-design-skills |
| style-structured | Lite | Beta | awesome-design-skills |
| style-terracotta | Lite | Beta | awesome-design-skills |
| style-utility-mono | Lite | Beta | awesome-design-skills |
| style-vibrant | Lite | Beta | awesome-design-skills |
| style-vintage | Lite | Beta | awesome-design-skills |

## Releasing

1. Update the table above when a skill is added, removed, or changes tier or status.
2. Update the **Counts** line here, and the same counts in `.claude-plugin/plugin.json`,
   `.claude-plugin/marketplace.json` and `README.md`.
3. Bump `version` in both manifests and add a `## <version>` entry to `RELEASE-NOTES.md`.
4. Run `python3 scripts/verify_release.py` and fix anything it reports.
