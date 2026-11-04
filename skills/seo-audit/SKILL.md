---
name: seo-audit
description: Run a technical and on-page SEO audit of a page or site. Trigger with "audit SEO", "why isn't this page ranking?", "check my site's SEO", or when reviewing crawlability, indexing, titles and headings, internal links, page speed (Core Web Vitals), mobile rendering, or structured data before or after a launch.
argument-hint: "<URL, HTML file, or description of the site>"
---

# /seo-audit

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Audit a page or site for technical and on-page SEO problems, ranked by impact.

## Usage

```
/seo-audit $ARGUMENTS
```

Audit for SEO: @$1

If a URL is given, fetch the page and read its HTML, `robots.txt` and sitemap. If a file or repo is given, read the templates that produce the `<head>` and page markup. Otherwise, ask the user for a URL or the page source.

## What I Need From You

- **The page or site**: URL, HTML, or the code that renders it
- **Goal**: What should this page rank for, and who is searching?
- **Scope** (optional): One page, a template (all product pages), or the whole site
- **Known symptoms** (optional): Traffic drop, page not indexed, wrong page ranking

## Audit Checklist

### 1. Crawling and Indexing
- `robots.txt` doesn't block the page, or the CSS/JS it needs to render
- No accidental `noindex` in `<meta name="robots">` or the `X-Robots-Tag` header
- Returns HTTP 200; redirects are single-hop 301s, not chains or 302s
- `<link rel="canonical">` is present, absolute, and points to itself (or the true original)
- Page is in the XML sitemap; sitemap lists only canonical, indexable, 200 URLs
- Important content is in the rendered HTML, not only behind clicks or client-side fetches
- Pagination, faceted filters and URL parameters don't create endless duplicate URLs

### 2. On-Page
- One unique `<title>` that leads with the main topic (see **meta-tags**)
- A `<meta name="description">` that matches the page and invites the click
- Exactly one `<h1>` that matches search intent; `<h2>`/`<h3>` follow a logical outline
- Main keyword and close variants appear naturally in the title, H1, intro and subheadings
- Descriptive, lowercase, hyphenated URL slug
- Images have meaningful `alt` text, sensible file names, and explicit width/height
- Content answers the query better than the pages currently ranking (see **seo-content**)

### 3. Links
- Page is reachable within a few clicks from the home page
- Internal links use descriptive anchor text, not "click here"
- No broken internal or external links (4xx/5xx)
- Orphan pages (no internal links in) are found and linked

### 4. Performance and Mobile
Core Web Vitals, measured at the 75th percentile of real users:

| Metric | Good | Needs improvement | Poor |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | ≤ 2.5 s | ≤ 4.0 s | > 4.0 s |
| INP (Interaction to Next Paint) | ≤ 200 ms | ≤ 500 ms | > 500 ms |
| CLS (Cumulative Layout Shift) | ≤ 0.1 | ≤ 0.25 | > 0.25 |

- `<meta name="viewport" content="width=device-width, initial-scale=1">` is set
- Text is readable and tap targets are usable on a phone without zooming
- Same content on mobile and desktop (Google indexes the mobile version)
- Images are compressed, sized to their display size, and lazy-loaded below the fold
- HTTPS everywhere; no mixed content

### 5. Structured Data and Sharing
- JSON-LD matches visible content and validates (see **schema-markup**)
- Open Graph and Twitter card tags are set for shareable pages
- `hreflang` tags are reciprocal and use valid language-region codes on multilingual sites

## Severity

- 🔴 **Critical**: Stops the page from being crawled, indexed or ranked (noindex, blocked, 404, wrong canonical)
- 🟡 **Major**: Clearly limits ranking or clicks (missing title, duplicate content, poor Core Web Vitals)
- 🟢 **Minor**: Polish (alt text gaps, slightly long titles, a missing OG image)

## Output

```markdown
## SEO Audit: [Page/Site Name]
**URL:** [URL] | **Scope:** [Page / Template / Site] | **Date:** [Date]

### Summary
**Issues found:** [X] | **Critical:** [X] | **Major:** [X] | **Minor:** [X]
[1-2 sentences: the biggest thing holding this page back]

### Findings
| # | Area | Issue | Evidence | Severity | Fix |
|---|------|-------|----------|----------|-----|
| 1 | Indexing | [Issue] | [Tag, header or URL that shows it] | 🔴 Critical | [Fix] |
| 2 | On-page | [Issue] | [Evidence] | 🟡 Major | [Fix] |

### On-Page Snapshot
| Element | Current | Recommended |
|---------|---------|-------------|
| Title ([X] chars) | [Current] | [Suggestion] |
| Meta description ([X] chars) | [Current] | [Suggestion] |
| H1 | [Current] | [Suggestion] |
| Canonical | [Current] | [OK / Suggestion] |

### Core Web Vitals
| Metric | Value | Source | Status |
|--------|-------|--------|--------|
| LCP | [X] s | [Field data / Lab estimate / Not measured] | ✅/⚠️/❌ |
| INP | [X] ms | [Source] | ✅/⚠️/❌ |
| CLS | [X] | [Source] | ✅/⚠️/❌ |

### Priority Fixes
1. **[Critical fix]** — [Why it matters, how to fix]
2. **[Major fix]** — [Why, how]
3. **[Minor fix]** — [Why, how]

### Not Checked
[What this audit couldn't verify without more access, e.g. field data, backlinks, server logs]
```

## If Connectors Available

If **~~search console** is connected:
- Check index coverage, the page's indexed status and canonical Google chose
- Pull the queries and pages with high impressions but low click-through rate

If **~~web analytics** is connected:
- Compare organic traffic before and after a drop to date the problem
- Find high-traffic pages to prioritize

If **~~project tracker** is connected:
- Create a ticket per finding with severity, evidence and the fix

## Tips

1. **Fix indexing first** — Nothing else matters if the page can't be crawled or indexed.
2. **Say what you measured** — Label Core Web Vitals as field data or a lab estimate; never invent numbers.
3. **Audit templates, not just pages** — A fix to the product template fixes every product page.
