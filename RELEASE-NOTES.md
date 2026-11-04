# Release notes

## 0.4.0

- Add `SHIPPING.md`: every skill gets a tier (Core / Lite / routing) and a status (Stable / Beta).
- Add `scripts/verify_release.py`, run in CI by `.github/workflows/verify-release.yml`.
- Manifest descriptions and `README.md` now state the skill counts.

## 0.3.0

- Add 5 SEO skills: seo-audit, keyword-research, meta-tags, schema-markup, seo-content.
- Add Search console, Web analytics and SEO tool connector categories to `CONNECTORS.md`.

## 0.2.0

- Add 7 design skills from anthropics/knowledge-work-plugins (`design/`): accessibility-review,
  design-critique, design-handoff, design-system, research-synthesis, user-research, ux-copy.
- Add `CONNECTORS.md`, root `README.md`, `LICENSE` and `NOTICE`.
- License changed from MIT to Apache-2.0 to match the imported skills.

## 0.1.0

- Initial plugin scaffold: `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.
