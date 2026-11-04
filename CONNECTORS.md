<!-- Modified from anthropics/knowledge-work-plugins (design/CONNECTORS.md): this plugin ships no .mcp.json, so the text about pre-configured servers was changed, and the SEO rows (Search console, Web analytics, SEO tool) were added. -->

# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. For example, `~~design tool` might mean Figma, Sketch, or any other design tool with an MCP server.

Plugins are **tool-agnostic** — they describe workflows in terms of categories (design tool, project tracker, user feedback, etc.) rather than specific products. This plugin does not pre-configure any MCP servers: connect the ones you use (in claude.ai Settings → Connectors, or with `claude mcp add`), and any MCP server in that category works.

## Connectors for this plugin

| Category | Placeholder | Example servers | Other options |
|----------|-------------|-----------------|---------------|
| Chat | `~~chat` | Slack | Microsoft Teams |
| Design tool | `~~design tool` | Figma | Sketch, Adobe XD, Framer |
| Knowledge base | `~~knowledge base` | Notion | Confluence, Guru, Coda |
| Project tracker | `~~project tracker` | Linear, Asana, Atlassian (Jira/Confluence) | Shortcut, ClickUp |
| User feedback | `~~user feedback` | Intercom | Productboard, Canny, UserVoice, Dovetail |
| Product analytics | `~~product analytics` | — | Amplitude, Mixpanel, Heap, FullStory |
| Search console | `~~search console` | Google Search Console | Bing Webmaster Tools |
| Web analytics | `~~web analytics` | Google Analytics | Plausible, Matomo, Adobe Analytics |
| SEO tool | `~~SEO tool` | — | Ahrefs, Semrush, Moz |
