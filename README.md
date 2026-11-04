# designer-pro-and-seo

A Claude Code plugin with design and SEO skills: accessibility audits, design
critique, developer handoff specs, design-system work, user research, UX copy,
SEO audits, keyword research, meta tags, structured data and search content,
plus 67 ready-made visual styles.

## Install

```text
/plugin marketplace add stoiana00-source/gf
/plugin install designer-pro-and-seo@designer-pro-and-seo
```

**79 skills: 7 Stable · 11 Core, 68 Lite, 0 routing.** Tiers and status are defined in
[SHIPPING.md](SHIPPING.md): the design skills are Stable; the SEO and style skills are Beta.

## Design skills

| Skill | Use it to |
|---|---|
| `accessibility-review` | Run a WCAG 2.1 AA audit: contrast, keyboard, touch targets, screen readers |
| `design-critique` | Get structured feedback on usability, hierarchy and consistency |
| `design-handoff` | Write developer handoff specs: layout, tokens, states, breakpoints, edge cases |
| `design-system` | Audit, document or extend a design system |
| `user-research` | Plan studies, write interview guides, choose methods |
| `research-synthesis` | Turn transcripts, surveys and tickets into themes and recommendations |
| `ux-copy` | Write or review microcopy, error messages, empty states and CTAs |

## SEO skills

| Skill | Use it to |
|---|---|
| `seo-audit` | Audit crawling, indexing, on-page tags, links, Core Web Vitals and mobile |
| `keyword-research` | Find keywords, classify intent, cluster them and map each to a page |
| `meta-tags` | Write title tags, meta descriptions and Open Graph / Twitter tags |
| `schema-markup` | Write or fix JSON-LD structured data for rich results |
| `seo-content` | Brief new pages or optimize existing ones against what ranks |

Each skill works from a description, screenshot or file. Skills get more out of
connected tools (a design tool such as Figma, a project tracker, Search Console, an SEO tool);
see [CONNECTORS.md](CONNECTORS.md). The plugin itself installs no MCP servers.

## Style skills

67 visual styles, each a skill with design tokens (colors, type, spacing, radii),
component rules, accessibility requirements and a QA checklist, plus a `DESIGN.md`
explaining the intent. Ask for one by name ("build this page in the brutalism style")
or describe the look you want.

`style-agentic`, `style-arcade`, `style-artistic`, `style-basic`, `style-bento`, `style-blank-canvas`, `style-blocks`, `style-bold`, `style-brutalism`, `style-cafe`, `style-claymorphism`, `style-clean`, `style-colorful`, `style-contemporary`, `style-corporate`, `style-cosmic`, `style-creative`, `style-dithered`, `style-doodle`, `style-dramatic`, `style-editorial`, `style-eight-bit`, `style-enterprise`, `style-expressive`, `style-fantasy`, `style-fiction`, `style-flat`, `style-friendly`, `style-futuristic`, `style-geometric`, `style-glassmorphism`, `style-gradient`, `style-immersive`, `style-impeccable`, `style-layered`, `style-levels`, `style-matrix`, `style-minimal`, `style-modern`, `style-mono`, `style-neobrutalism`, `style-neon`, `style-neumorphism`, `style-paper`, `style-perspective`, `style-playful-rounded`, `style-power`, `style-premium`, `style-professional`, `style-pulse`, `style-purple-dashboard`, `style-refined`, `style-research-journal`, `style-retro`, `style-riso`, `style-sketch`, `style-skeumorphism`, `style-sleek`, `style-spacious`, `style-square`, `style-stitch`, `style-storytelling`, `style-structured`, `style-terracotta`, `style-utility-mono`, `style-vibrant`, `style-vintage`

## Layout

- `.claude-plugin/`: plugin and marketplace manifests (see its README)
- `skills/`: one folder per skill, each with a `SKILL.md`
- `SHIPPING.md`: each skill's tier and status, and the release checklist
- `scripts/verify_release.py`: fails if versions, release notes, skills or counts drift
- `RELEASE-NOTES.md`: changes per version

## License

Apache License 2.0. The design skills come from
[anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins);
see [NOTICE](NOTICE). The style skills come from
[bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) (MIT).
The SEO skills are original to this repo.
