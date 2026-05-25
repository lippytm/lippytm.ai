---
name: chatgpt-github-sync-automation
description: Use when syncing ChatGPT Business-originated or Zo Computer-refined work into GitHub repositories, creating commits, organizing repo paths, generating mirror notes, or preparing pull/commit summaries for LippytmAI and Business of Businesses.
compatibility: Created for Zo Computer
metadata:
  author: lippytmai.zo.computer
---
# ChatGPT GitHub Sync Automation

## Purpose

Automate the flow from ChatGPT Business and Zo Computer into GitHub source-of-truth repositories.

## Default repo targets

- `lippytm/lippytm.ai` — central ecosystem, campaigns, skills, workflows, eBooks, swarm systems.
- `lippytm/lippytmai.getbizfunds.com-` — GetBizFunds lead, funding, payment, wallet, Web3 business systems.
- `lippytm/lippytmai.zo.computer-` — Zo Computer connection and platform attachments.
- `lippytm/lippytm-lippytm.ai-tower-control-ai` — control tower, AI coding, automation, orchestration, and swarm control systems.

## Standard workflow

1. Identify the source file or processed ChatGPT folder.
2. Select the right GitHub repo and target path.
3. Copy or transform content into a durable markdown/spec/template path.
4. Run `scripts/sync_to_github_repo.py` or perform equivalent Git commands.
5. Commit with a clear message.
6. Push.
7. Record the commit in the relevant workflow or plan.

## Recommended repo paths

- `integrations/` — integration workflows
- `workflows/` — operating systems and process maps
- `campaigns/` — advertising and campaign assets
- `ebooks/` — eBook drafts and sales copy
- `templates/` — reusable prompts, CSVs, schemas, checklists
- `skills/` — portable skill packages
- `docs/` — public or internal documentation

## Safeguards

- Do not commit secrets or private credentials.
- Use small focused commits.
- Prefer markdown and structured templates over raw transcript dumps.
- If the content affects public claims, funding, crypto, legal, tax, or financial advice, run safety review first.

## Output

Return:

- repo
- files changed
- commit hash
- push status
- next GitHub/ChatGPT/Zo action
