# designer-pro-and-seo

A Claude Code plugin with design skills: accessibility audits, design critique,
developer handoff specs, design-system work, user research planning, research
synthesis and UX copy.

## Install

```text
/plugin marketplace add stoiana00-source/gf
/plugin install designer-pro-and-seo@designer-pro-and-seo
```

## Skills

| Skill | Use it to |
|---|---|
| `accessibility-review` | Run a WCAG 2.1 AA audit: contrast, keyboard, touch targets, screen readers |
| `design-critique` | Get structured feedback on usability, hierarchy and consistency |
| `design-handoff` | Write developer handoff specs: layout, tokens, states, breakpoints, edge cases |
| `design-system` | Audit, document or extend a design system |
| `user-research` | Plan studies, write interview guides, choose methods |
| `research-synthesis` | Turn transcripts, surveys and tickets into themes and recommendations |
| `ux-copy` | Write or review microcopy, error messages, empty states and CTAs |

Each skill works from a description, screenshot or file. Skills get more out of
connected tools (a design tool such as Figma, a project tracker, a knowledge base);
see [CONNECTORS.md](CONNECTORS.md). The plugin itself installs no MCP servers.

## Layout

- `.claude-plugin/`: plugin and marketplace manifests (see its README)
- `skills/`: one folder per skill, each with a `SKILL.md`
- `RELEASE-NOTES.md`: changes per version

## License

Apache License 2.0. The skills come from
[anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins);
see [NOTICE](NOTICE).
