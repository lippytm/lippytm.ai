# Cross-Platform Infrastructure Hub

This document is the operating map for the lippytm cross-platform infrastructure network. It connects GitHub, Slack, Viktor, HuggingFace, bots, Web3, creative/business assets, and future OAuth tools into one practical control system.

## Current live connections

| Platform | Status | What Viktor can do now |
| --- | --- | --- |
| GitHub | Live | Read/write repos, branches, PRs, issues, releases, Actions, repo inventory |
| Slack | Live | DM updates, channel posts, bookmarks, canvases, file sharing |
| Web browser | Live | Browse sites, research, inspect HuggingFace pages, gather public data |
| Email | Live | Send and receive email with attachments |
| Media generation | Live | Images, video, audio, transcription |
| Viktor Spaces | Live | Build hosted apps with database, auth, and dashboards |

## Dashboard app

A Viktor Space app named `lippytm-infra-hub` has been created as the central infrastructure dashboard.

The dashboard tracks:

- Repository count and categories
- GitHub Actions workflow coverage
- Open issue counts
- Live platform connections
- OAuth integrations to connect next
- The five major build tracks:
  1. Central dashboard app
  2. GitHub Actions cross-repo setup
  3. HuggingFace browsing/integration
  4. Automated repo management
  5. More tool connections

## GitHub automation runway

Recommended automation layers:

1. **Weekly repo inventory** — scheduled report of repos, workflows, open issues, and updated dates.
2. **Security hygiene** — CodeQL, dependency review, Dependabot, protected-path awareness.
3. **Issue triage** — label issues by business lane: security, monetization, bots, Web3, creative, docs.
4. **Repo role map** — keep every repo assigned to a lane and mission.
5. **PR quality gate** — require summaries, test notes, rollback notes, and risk level.

The workflow `.github/workflows/lippytm-cross-platform-inventory.yml` implements the first layer.

## HuggingFace integration path

Current status: browser-ready.

Viktor can browse the HuggingFace profile at:

- https://huggingface.co/lippytm

Possible next steps:

- Inventory models, datasets, and Spaces.
- Add links from GitHub repos to related HuggingFace assets.
- Create model cards and dataset cards from repo documentation.
- If an API token or OAuth connection is added later, automate uploads, metadata edits, and release notes.

## OAuth tools to connect next

Connect these at https://app.getviktor.com/integrations when ready:

| Priority | Tool | Why it matters |
| --- | --- | --- |
| 1 | Google Drive | Shared docs, PDFs, exported reports, business assets |
| 2 | Notion | Knowledge base and operating manuals |
| 3 | Linear | Structured engineering and automation work queue |
| 4 | Stripe | Money path, offers, billing, revenue reporting |
| 5 | Google Calendar | Scheduling and recurring operating cadence |
| 6 | HubSpot/Salesforce | CRM and partner/customer tracking |
| 7 | PostHog/Google Analytics | Product and web analytics |
| 8 | Google Ads/Meta Ads | Growth campaign management |

## Operating cadence

- **Daily:** issue triage and urgent blocker detection.
- **Weekly:** repo inventory, security summary, open issue ranking.
- **Monthly:** business asset map, revenue path review, integration expansion plan.

## Safety rules

- Use PRs for repo changes instead of direct pushes to `main`.
- Keep secrets out of repos; use GitHub Actions secrets or connected OAuth tools.
- Avoid automated destructive changes without explicit approval.
- Label high-risk changes before merging.
