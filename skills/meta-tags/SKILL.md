---
name: meta-tags
description: Write or review a page's title tag, meta description, and social sharing tags. Trigger with "write a title tag", "meta description for", "improve our CTR", "fix our link previews", or when naming a new page for search, rewriting titles that get impressions but few clicks, or setting Open Graph and Twitter card tags.
argument-hint: "<URL, page content, or target keyword>"
---

# /meta-tags

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Write the tags that control how a page appears in search results and link previews.

## Usage

```
/meta-tags $ARGUMENTS
```

If a URL is given, fetch the page and read its current tags and content. If the page isn't live, work from the content or brief provided.

## What I Need From You

- **The page**: URL, content, or a summary of what it offers
- **Target keyword**: The main query this page should rank for (see **keyword-research**)
- **Brand name**: And whether to include it in titles
- **Constraints** (optional): CMS templates, existing title pattern, character limits

## Title Tag

- Aim for about 50–60 characters; Google truncates by pixel width (about 600 px), so check long words
- Put the main keyword near the start
- Make it unique across the site
- Match the intent: "Pricing", "vs", "How to" and years signal what the page delivers
- Add the brand at the end with a separator (`|` or `–`) when space allows
- Google may rewrite titles that are vague, stuffed, or don't match the H1, so keep them aligned

## Meta Description

- Aim for about 140–160 characters; mobile shows less, so put the hook first
- Not a ranking factor, but it shapes click-through rate
- Summarize what the searcher gets, include the keyword naturally (Google bolds it), end with a reason to click
- Unique per page; Google often writes its own snippet if the description doesn't fit the query

## Social Tags

| Tag | Purpose | Guidance |
|-----|---------|----------|
| `og:title` | Preview headline | Can be punchier than the title tag; no brand suffix needed |
| `og:description` | Preview text | 1–2 sentences |
| `og:image` | Preview image | 1200×630 px, absolute URL, key text away from edges |
| `og:url` | Canonical URL | Same as `rel="canonical"` |
| `og:type` | Content type | `website` or `article` |
| `twitter:card` | Card layout | `summary_large_image` for most pages |

## Output

```markdown
## Meta Tags: [Page Name]
**Target keyword:** [keyword] | **Intent:** [intent]

### Recommended
**Title** ([X] chars): [Title]
**Meta description** ([X] chars): [Description]

### Alternatives
| Option | Title | Chars | Angle |
|--------|-------|-------|-------|
| A | [Title] | [X] | [e.g. benefit-led] |
| B | [Title] | [X] | [e.g. question] |
| C | [Title] | [X] | [e.g. number / year] |

### Search Preview
[Title]
[example.com › path]
[Meta description]

### HTML
<title>[Title]</title>
<meta name="description" content="[Description]">
<link rel="canonical" href="[URL]">
<meta property="og:title" content="[OG title]">
<meta property="og:description" content="[OG description]">
<meta property="og:image" content="[Image URL]">
<meta property="og:url" content="[URL]">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">

### Rationale
[Why this wording: keyword placement, intent, differentiation from competitors]
```

For many pages at once (a template or a site), return a table: URL, current title, new title, current description, new description, character counts.

## If Connectors Available

If **~~search console** is connected:
- Find pages with high impressions and low click-through rate; rewrite those first
- Check which queries each page actually appears for before choosing the keyword

If **~~SEO tool** is connected:
- See the titles competitors use for the same query, and differentiate

## Tips

1. **Count characters** — Always show the count next to each title and description.
2. **Promise only what the page delivers** — A misleading title raises clicks and bounces.
3. **Test the weak pages first** — Rewriting titles on pages with impressions but no clicks is the fastest SEO win.
