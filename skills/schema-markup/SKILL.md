---
name: schema-markup
description: Write, review, or fix structured data (JSON-LD schema.org markup) for rich results. Trigger with "add schema", "structured data for", "JSON-LD", "why don't we get rich results?", or when marking up products, articles, organizations, breadcrumbs, events, recipes, reviews, local businesses, or videos.
argument-hint: "<URL, page content, or page type>"
---

# /schema-markup

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Generate valid JSON-LD that describes a page's content to search engines.

## Usage

```
/schema-markup $ARGUMENTS
```

If a URL is given, fetch the page, read any existing `application/ld+json` blocks, and base the markup on what is visible on the page. Otherwise, work from the content provided.

## What I Need From You

- **The page**: URL, content, or page type (product, article, event…)
- **The facts**: Prices, dates, ratings, addresses — I'll only mark up what you give me or what's on the page
- **Stack** (optional): Where the markup goes (template, CMS field, Next.js head) so I can format it

## Rules

1. **Use JSON-LD** in a `<script type="application/ld+json">` block — Google's recommended format
2. **Mark up only visible content** — Ratings, prices and FAQs must appear on the page
3. **Never invent values** — Use `[placeholder]` for anything unknown and list it under Missing Data
4. **Fill required properties first**, then recommended ones; missing required properties disqualify rich results
5. **Use absolute URLs and ISO 8601 dates** (`2026-03-15`, `2026-03-15T19:00:00+01:00`)
6. **Link entities with `@id`** so the Organization, WebSite and page reference each other instead of repeating
7. **Valid markup doesn't guarantee rich results** — Google decides; eligibility rules change, so check Google's current structured data docs for the type

## Common Types

| Page | Type | Key properties |
|------|------|----------------|
| Home page | `Organization` + `WebSite` | name, url, logo, sameAs |
| Product page | `Product` with `Offer` | name, image, offers (price, priceCurrency, availability), aggregateRating, review |
| Blog post | `Article` / `BlogPosting` | headline, image, datePublished, dateModified, author |
| Any deep page | `BreadcrumbList` | itemListElement with position, name, item |
| Local business | `LocalBusiness` (or a subtype) | name, address, telephone, openingHoursSpecification, geo |
| Event | `Event` | name, startDate, location, eventStatus, offers |
| Video | `VideoObject` | name, thumbnailUrl, uploadDate, description, contentUrl or embedUrl |
| Recipe | `Recipe` | name, image, recipeIngredient, recipeInstructions |
| Job posting | `JobPosting` | title, description, datePosted, hiringOrganization, jobLocation |

Google limits some types: FAQ rich results show only for well-known government and health sites, and How-to rich results are no longer shown. The markup is still valid schema.org, but don't promise those results.

## Output

```markdown
## Structured Data: [Page Name]
**Types:** [Product, BreadcrumbList] | **Rich result eligible:** [Product snippets / Breadcrumbs / None]

### JSON-LD
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "...", "@id": "[URL]#...", ... }
  ]
}
</script>

### Property Check
| Property | Required? | Status | Value source |
|----------|-----------|--------|--------------|
| [name] | Required | ✅ Set | [Page H1] |
| [aggregateRating] | Recommended | ⚠️ Placeholder | [Needs review data] |

### Missing Data
- [Value the markup needs that isn't on the page or wasn't provided]

### Validate
1. Google Rich Results Test: https://search.google.com/test/rich-results
2. Schema Markup Validator: https://validator.schema.org
```

When reviewing existing markup, list each error (invalid type, missing required property, mismatch with visible content), then give the corrected JSON-LD.

## If Connectors Available

If **~~search console** is connected:
- Check the rich result reports for errors and warnings on existing markup
- Confirm which pages currently earn rich results

## Tips

1. **Use `@graph`** — One script block with linked entities is easier to maintain than several.
2. **Template it** — Generate markup from the same data that renders the page, so the two never drift.
3. **Keep `dateModified` honest** — Update it only when the content meaningfully changes.
