# designer-pro-and-seo

A Claude Code plugin with design and SEO skills: accessibility audits, design
critique, developer handoff specs, design-system work, user research, UX copy,
SEO audits, keyword research, meta tags, structured data and search content.

## Install

```text
/plugin marketplace add stoiana00-source/gf
/plugin install designer-pro-and-seo@designer-pro-and-seo
```

**12 skills: 7 Stable · 11 Core, 1 Lite, 0 routing.** Tiers and status are defined in
[SHIPPING.md](SHIPPING.md): the design skills are Stable, the SEO skills are Beta.

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

## Layout

- `.claude-plugin/`: plugin and marketplace manifests (see its README)
- `skills/`: one folder per skill, each with a `SKILL.md`
- `SHIPPING.md`: each skill's tier and status, and the release checklist
- `scripts/verify_release.py`: fails if versions, release notes, skills or counts drift
- `RELEASE-NOTES.md`: changes per version

## License

Apache License 2.0. The design skills come from
[anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins);
see [NOTICE](NOTICE). The SEO skills are original to this repo.
