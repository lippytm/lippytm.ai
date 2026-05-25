---
name: chatgpt-zo-full-workspace-exporter
description: Use when creating comprehensive ChatGPT Business-ready exports of lippytmai.zo.computer covering workspace files, Skills, workflows, campaigns, eBooks, templates, GitHub state, public pages, Web3 affiliate systems, GetBizFunds, and AgentBot swarm systems.
compatibility: Created for Zo Computer
metadata:
  author: lippytmai.zo.computer
---
# ChatGPT Zo Full Workspace Exporter

## Purpose

Create a deeper Zo → ChatGPT Business package than the standard export when ChatGPT Business needs to understand the whole LippytmAI build ecosystem.

## Standard workflow

1. Run `scripts/export_full_workspace_for_chatgpt.py`.
2. Review the export manifest.
3. Give the ZIP to the user for ChatGPT Business upload.
4. Use `Records/Templates/ChatGPTZoBridge/full-workspace-chatgpt-prompt.md` inside ChatGPT Business.
5. Import returned outputs with `chatgpt-business-import-automation`.

## Included areas

- AGENTS.md
- Records/Plans
- Records/Workflows
- Records/Templates
- Campaigns
- Ebooks
- Skills list and selected SKILL.md files
- public route map
- GitHub repo state summary
- ChatGPT return prompts

## Safeguards

- Exclude Trash, node_modules, .git, secrets, credentials, raw large exports, and unnecessary media.
- Prefer summaries for bulky generated assets.
- Keep packages timestamped.

## Output

Return:

- export folder
- export ZIP
- manifest path
- included areas
- excluded areas
- recommended ChatGPT Business prompt
