---
name: seo-content
description: Write content briefs for search, or optimize an existing page so it ranks for its target keyword. Trigger with "content brief for", "optimize this article for SEO", "why does this competitor outrank us?", "refresh this post", or when outlining a new page, closing topic gaps against ranking pages, or improving E-E-A-T signals.
argument-hint: "[brief | optimize] <keyword, URL, or draft>"
---

# /seo-content

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Plan or improve content so it is the most useful result for a search query.

## Usage

```
/seo-content brief <keyword>            # Brief a new page
/seo-content optimize <URL or draft>    # Improve an existing page
```

If a URL is given, fetch it. When possible, also look at the pages that currently rank for the keyword to understand what searchers expect.

## What I Need From You

- **Target keyword**: And secondary keywords if you have them (see **keyword-research**)
- **Audience**: Who's searching and what they already know
- **Your angle**: First-hand experience, data, or expertise you can add that others can't
- **The draft or URL**: For optimize mode

## Principles

1. **Match intent first** — Format follows what ranks: a guide, a list, a comparison, a tool
2. **Answer early** — Give the direct answer in the first paragraph, then go deeper
3. **Cover the topic, not the keyword** — Answer the follow-up questions searchers have; don't repeat the phrase
4. **Show experience** (E-E-A-T) — Original examples, screenshots, data, a named author with credentials
5. **Make it scannable** — Descriptive subheadings, short paragraphs, lists and tables where they help
6. **Link with purpose** — To the pillar page, related pages, and credible sources
7. **Write for people** — Content made mainly to rank, at scale or rewritten from others, is what Google's updates demote

## Brief Checklist

- Search intent and the format that wins
- Working title, H1 and meta description (see **meta-tags**)
- Outline (H2/H3) covering the subtopics ranking pages share, plus the gap they miss
- Questions to answer
- Unique value: what only you can include
- Internal links in and out
- Suggested structured data (see **schema-markup**)
- Length: whatever the topic needs; use competitor length as a range, not a target

## Optimize Checklist

- Does the page match the intent of what ranks now?
- Is the answer in the first 100 words?
- Which subtopics and questions do ranking pages cover that this one doesn't?
- Is anything outdated: stats, screenshots, prices, years?
- Do the title, H1 and intro use the target keyword naturally?
- Are there internal links to and from related pages?
- Is the author and their experience visible?
- What can be cut — filler, repetition, off-topic sections?

## Output — Brief

```markdown
## Content Brief: [Working Title]
**Primary keyword:** [keyword] | **Secondary:** [list] | **Intent:** [intent]
**Format:** [Guide / Comparison / List / Landing page] | **Suggested length:** [range]

### Title and Meta
**Title:** [Title] ([X] chars)
**H1:** [H1]
**Meta description:** [Description] ([X] chars)
**Slug:** /[slug]

### What Searchers Need
[2-3 sentences on the problem behind the query and what a great answer looks like]

### Outline
- H2: [Section] — [What to cover]
  - H3: [Subsection]
- H2: [Section] — [What to cover]

### Questions to Answer
- [Question]

### Our Unique Angle
[Experience, data or examples to include that ranking pages lack]

### Links
**Link to:** [Pillar and related pages] | **Link from:** [Existing pages that should link here]

### Structured Data
[Suggested types]
```

## Output — Optimize

```markdown
## Content Optimization: [Page Title]
**URL:** [URL] | **Target keyword:** [keyword]

### Summary
[What's holding the page back, in 1-2 sentences]

### Recommendations
| # | Change | Why | Impact |
|---|--------|-----|--------|
| 1 | [Add a section on X] | [Ranking pages cover it; searchers ask it] | High |
| 2 | [Rewrite intro to answer first] | [Answer is buried in paragraph 4] | Medium |

### Topic Gaps
| Subtopic / Question | Covered by ranking pages | On this page? |
|---------------------|--------------------------|---------------|
| [Subtopic] | [X of Y] | ❌ |

### Rewrites
**Title:** [Before] → [After]
**Intro:** [Rewritten opening paragraph]

### Cut or Update
- [Outdated or off-topic content]
```

## If Connectors Available

If **~~search console** is connected:
- See which queries the page already ranks for and their positions
- Find queries with impressions the page doesn't answer yet

If **~~SEO tool** is connected:
- Pull the current top-ranking URLs and their headings for gap analysis

If **~~knowledge base** is connected:
- Pull the brand voice guide and product facts to keep content accurate

## Tips

1. **Read what ranks before writing** — The search results show what Google thinks the intent is.
2. **Refresh before you create** — Updating a page that's already on page 2 is often faster than a new page.
3. **Bring something new** — If your page says what the top ten already say, it has no reason to outrank them.
