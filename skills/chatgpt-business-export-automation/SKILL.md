---
name: chatgpt-business-export-automation
description: Use when exporting LippytmAI Zo Computer workspace files, GitHub state, public page maps, campaigns, eBooks, workflows, templates, skills, and AgentBots swarm systems into a ChatGPT Business-ready ZIP package.
compatibility: Created for Zo Computer
metadata:
  author: lippytmai.zo.computer
---
# ChatGPT Business Export Automation

## Purpose

Automate the Zo Computer → ChatGPT Business export side of the workflow.

## Standard workflow

1. Run `scripts/export_zo_workspace_for_chatgpt.py`.
2. Create a timestamped package under `/home/workspace/Exports/LippytmAI-Zo-Workspace-Export/`.
3. Include:
   - AGENTS.md
   - core plans
   - core workflows
   - current campaign/eBook files
   - skill map
   - public URL map
   - GitHub repo map
   - ChatGPT return prompt
4. Give the ZIP to the user for upload into ChatGPT Business.
5. Ask ChatGPT Business to return improved files, plans, prompts, or campaign material.
6. Import the returned material with `chatgpt-business-import-automation`.

## When to use

Use before major ChatGPT Business work sessions, after major Zo/GitHub changes, or when the user asks to export all current Zo Computer work.

## Safeguards

- Do not include secrets, tokens, or credentials.
- Prefer source markdown and summaries over bulky generated media unless needed.
- Include GitHub/public URL maps so ChatGPT Business can reason from current state.
- Keep exports timestamped for traceability.

## Output

Return:

- export folder path
- export ZIP path
- important included files
- recommended ChatGPT Business prompt
- next import step
