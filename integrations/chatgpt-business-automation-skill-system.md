# ChatGPT Business Automation Skill System

## Purpose

Automate the recurring LippytmAI flow between ChatGPT Business, Zo Computer, GitHub, Zapier, Canva, Claude, Web3 affiliate websites, GetBizFunds, eBooks, and AI Agentic Super Synthetic Intelligence Engines AgentsBots Swarms.

## Skill stack

### 1. Import automation

Use `Skills/chatgpt-business-import-automation/SKILL.md` when the user provides ChatGPT Business exports or copied conversations.

Capabilities:

- stores raw files separately
- extracts ZIPs
- converts supported files into markdown
- classifies content by category
- creates a processed index
- prepares promotion into workspace/GitHub

### 2. Export automation

Use `Skills/chatgpt-business-export-automation/SKILL.md` when sending Zo Computer work back to ChatGPT Business.

Capabilities:

- creates timestamped export package
- includes core workflows, skills, campaign files, eBooks, public URL maps, and GitHub maps
- creates ZIP package for upload into ChatGPT Business
- includes a return prompt

### 3. GitHub sync automation

Use `Skills/chatgpt-github-sync-automation/SKILL.md` when promoting ChatGPT/Zo material into GitHub.

Capabilities:

- copies source material into repo paths
- commits and pushes changes
- keeps small traceable commits
- supports the main LippytmAI repo lanes

## Recommended recurring cadence

### Before a ChatGPT Business work session

1. Run export automation.
2. Upload ZIP into ChatGPT Business.
3. Use the return package prompt.
4. Ask ChatGPT Business for improved campaign, eBook, code, Zapier, Canva, Web3, or swarm assets.

### After a ChatGPT Business work session

1. Save returned material as files or export ZIP.
2. Run import automation.
3. Review `processed-index.md`.
4. Promote best content into durable workspace locations.
5. Run GitHub sync automation.
6. Re-export if ChatGPT Business should continue the loop.

## Promotion rules

- Strategy and roadmaps → `Records/Plans/`
- Workflows and operating systems → `Records/Workflows/`
- Campaigns and ads → `Campaigns/`
- eBooks and sales copy → `Ebooks/`
- Prompts and templates → `Records/Templates/`
- Skills → `Skills/`
- GetBizFunds-specific systems → mirror into `lippytmai.getbizfunds.com-`
- Platform-wide systems → mirror into `lippytm.ai`

## Safety rules

- Never import or commit secrets.
- Keep raw ChatGPT exports in the Raw folder.
- Prefer processed summaries and reusable assets over full transcript sprawl.
- Review funding, affiliate, crypto, legal, tax, and investment claims before publishing.
- Use human approval before sending external messages, taking payments, or changing public financial claims.

## Immediate next step

When Charles provides a ChatGPT Business export ZIP, run:

```bash
python3 /home/workspace/Skills/chatgpt-business-import-automation/scripts/import_chatgpt_export.py '/path/to/export.zip'
```

To export current Zo work for ChatGPT Business, run:

```bash
python3 /home/workspace/Skills/chatgpt-business-export-automation/scripts/export_zo_workspace_for_chatgpt.py
```
