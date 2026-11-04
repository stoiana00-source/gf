---
name: keyword-research
description: Find and prioritize the search keywords a page or site should target. Trigger with "keyword research", "what should we rank for?", "find keywords for", or when planning a new page, mapping keywords to existing pages, grouping topics into clusters, or judging search intent and difficulty.
argument-hint: "<topic, product, URL, or seed keywords>"
---

# /keyword-research

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Turn a topic into a prioritized keyword plan, with each keyword mapped to one page.

## Usage

```
/keyword-research $ARGUMENTS
```

## What I Need From You

- **Topic or product**: What you offer and the problem it solves
- **Audience**: Who searches, in which country and language
- **Site** (optional): Your domain and existing pages, so I can map keywords to them
- **Competitors** (optional): Sites that rank where you want to rank

## Process

### 1. Seed and Expand
- Start from how customers describe the problem, not your product's internal name
- Expand with modifiers: best, vs, alternative, how to, for [audience], near me, price, template
- Mine questions people ask (who, what, why, how, can, does)
- Note the language competitors' top pages use in their titles and headings

### 2. Classify Search Intent
| Intent | The searcher wants to | Typical words | Page type that wins |
|--------|----------------------|---------------|---------------------|
| Informational | Learn or solve a problem | how, what, why, guide, ideas | Article, guide, tutorial |
| Commercial | Compare before buying | best, vs, review, alternative | Comparison, listicle, review |
| Transactional | Buy or sign up now | buy, price, pricing, discount, trial | Product, pricing, sign-up page |
| Navigational | Reach a specific site | brand names, login | Home page, login page |

Check intent against what currently ranks: if the top results are all guides, a product page won't rank for that query.

### 3. Assess Each Keyword
- **Volume**: Monthly searches (from a keyword tool; mark as unknown if none is connected)
- **Difficulty**: How strong the ranking pages are; a forum or thin page in the top results means an opening
- **Business value**: How close the searcher is to needing what you sell (High / Medium / Low)
- **Fit**: Can you credibly write the best result for this?

### 4. Cluster and Map
- Group keywords that the same page could satisfy (same intent, results overlap)
- One primary keyword per page; close variants become secondary keywords
- Each cluster gets a pillar page with supporting pages linking to it
- Flag cannibalization: two of your pages targeting the same cluster

## Prioritization

Score = business value × fit, then break ties by easier difficulty. Quick wins are high-value keywords where you already rank on page 2 (positions 11–20).

## Output

```markdown
## Keyword Plan: [Topic]
**Market:** [Country / Language] | **Data source:** [Tool name / Estimates only]

### Summary
[2-3 sentences: the main opportunity and where to start]

### Keyword Clusters

#### Cluster 1: [Name] — [Intent]
**Target page:** [Existing URL / New page: suggested slug]
| Keyword | Role | Intent | Volume | Difficulty | Value |
|---------|------|--------|--------|------------|-------|
| [keyword] | Primary | [Intent] | [X / Unknown] | [Low/Med/High] | [High/Med/Low] |
| [keyword] | Secondary | [Intent] | [X] | [Diff] | [Value] |

#### Cluster 2: [Name]
[Same format]

### Priority List
| # | Keyword / Cluster | Action | Why |
|---|-------------------|--------|-----|
| 1 | [Cluster] | [Create / Optimize / Merge page] | [Reason] |

### Cannibalization and Gaps
- [Pages competing for the same cluster, and which one should own it]
- [Clusters competitors cover that you don't]

### Questions to Answer in Content
- [Question searchers ask]
```

## If Connectors Available

If **~~SEO tool** is connected:
- Pull real search volume, keyword difficulty and the current top-ranking URLs
- Find keywords competitors rank for that you don't

If **~~search console** is connected:
- Find queries you already get impressions for, especially positions 11–20
- Spot pages that rank for clusters they weren't built for

## Tips

1. **Never invent volumes** — Without a connected tool, give relative estimates and say so.
2. **Intent beats volume** — A 50-search keyword from buyers is worth more than 5,000 from students.
3. **Map before you write** — Deciding which page owns each cluster prevents cannibalization later.
