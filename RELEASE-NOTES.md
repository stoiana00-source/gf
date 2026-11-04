# Release notes

## 0.5.0

- Add 67 visual-style skills (`style-*`, tier Lite, status Beta) from bergside/awesome-design-skills (MIT),
  each with a `SKILL.md` and a `DESIGN.md`.
- Ten brand-named styles were renamed: ant → style-structured, claude → style-research-journal, codex → style-blank-canvas, lingo → style-playful-rounded, material → style-layered, pacman → style-eight-bit, roku → style-purple-dashboard, sega → style-arcade, shadcn → style-utility-mono, tetris → style-blocks.
- Broaden the Lite tier definition in `SHIPPING.md` to cover style skills.

## 0.4.1

- Add the plugin icon: `.claude-plugin/icon.png` (1024×1024), drawn from `.claude-plugin/icon.svg`.
- Add a marketplace description to `marketplace.json`.

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
