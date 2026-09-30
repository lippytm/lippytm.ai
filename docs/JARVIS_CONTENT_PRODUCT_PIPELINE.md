# Jarvis Content Product Pipeline

**Scope:** Editorial and production lifecycle for ebooks, audiobooks, and videobooks. Existing repository ebook/campaign files are source assets at varying stages, not evidence of a finished, distributed product or active checkout.

## Lifecycle and release gates

| Stage | Work | Acceptance criteria / evidence |
|---|---|---|
| 1. Idea | Record audience, problem, intended format, business goal, and owner | One-page brief; audience and value proposition are specific |
| 2. Source inventory | Link source files and record author, version, rights, permissions, third-party material, and sensitive information | Rights/permission status is `verified`, `permission required`, or `blocked`; blocked content cannot proceed |
| 3. Outline | Organize chapters/episodes around learner outcomes | Every section has an objective, source reference, and proposed CTA |
| 4. Draft | Write/adapt the ebook master manuscript; separate established facts from opinion and dated claims | Editorial owner review; fact-sensitive claims have sources and as-of date |
| 5. Editorial and safety QA | Check accuracy, originality/permissions, claims, privacy, affiliate disclosures, accessibility, spelling, and consistency | Issues resolved or explicitly accepted by human owner; no unsupported guarantee |
| 6. Ebook production | Export accessible HTML/PDF/other intended formats from approved master | Contents, links, metadata, rendering, mobile readability, and CTA tested |
| 7. Audiobook adaptation | Prepare narration script, pronunciation guide, credits, licensed music/voices, recording, and mastering | Complete listen-through; transcript/script matches; rights and audio quality approved |
| 8. Videobook adaptation | Prepare storyboard, captions, visual permissions, audio mix, edit, and transcript | Full playback on target device; captions/transcript and all visual/audio rights checked |
| 9. Product and publishing setup | Define edition, version, metadata, price placeholder, delivery platform, refund/support policy, and publication date | Test purchase/delivery/refund path before claiming availability; human release approval |
| 10. Promotion | Prepare excerpt, landing copy, campaign variants, and channel-specific disclosure | Claims match product; affiliate relationship disclosed beside relevant links; every send approved |
| 11. Measure and maintain | Track opt-in, qualified CTA action, refunds/feedback, defects, and source changes | Monthly review; versioned corrections and takedown path documented |

## Content record

Track at minimum: `content_id`, title, audience, source path and commit/version, format, owner, rights state, factual review date, editorial reviewer, edition version, production status, accessibility checks, publication URL/status, price placeholder/approved price, CTA target, affiliate disclosure state, and next review date. Do not put private customer details or credentials in a content record.

## CTA mapping

| Asset / audience intent | Primary CTA | Secondary CTA | Guardrail |
|---|---|---|---|
| Free excerpt or checklist | Opt in for the related resource | Book a discovery conversation | State what follow-up will occur; honor opt-out |
| Ebook about business workflows | Purchase the ebook once checkout is tested | Request the lead-workflow pilot | Describe only the narrow, currently supportable scope |
| Audiobook | Visit the transcript/edition page | Explore the related ebook or pilot | Put affiliate disclosure in show notes and spoken/scripted context where required |
| Videobook tutorial | Download/check the relevant exercise | Request a workflow review | Show only tested product behavior; caption and disclose sponsored/affiliate content |
| Hosting/site-building content | Visit Hostinger through a clearly disclosed referral if active | Ask about a separate Jarvis setup pilot | Affiliate purchase does not guarantee business outcomes or Jarvis eligibility |

Use one primary CTA per asset and record a tagged destination or campaign ID. A click, opt-in, purchase, or referral must not be described as proof of a customer outcome.

## Existing source examples

This repository currently includes ebook and campaign materials under [`ebooks/`](../ebooks/) and [`campaigns/`](../campaigns/), along with a publishing checklist at [`operations/weekly-publishing-checklist.md`](../operations/weekly-publishing-checklist.md). Inventory each asset's edition and rights state before treating it as publish-ready.
