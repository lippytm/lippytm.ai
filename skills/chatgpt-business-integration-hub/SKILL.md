---
name: chatgpt-business-integration-hub
description: Use when integrating ChatGPT Business into the LippytmAI Zo Computer building process, importing ChatGPT exports, cloning ChatGPT-originated work into workspace/GitHub, or exporting Zo work back into ChatGPT Business-ready packages.
compatibility: Created for Zo Computer
metadata:
  author: lippytmai.zo.computer
---
# ChatGPT Business Integration Hub

## Purpose

Make ChatGPT Business a first-class creative and planning source for LippytmAI, while keeping Zo Computer and GitHub as durable build systems.

## Important limitation

ChatGPT Business does not provide a standard direct workspace-to-workspace clone tool here. To import prior ChatGPT Business work, use one of these inputs:

- ChatGPT export ZIP from ChatGPT settings.
- Copied conversation text pasted into a markdown file.
- Individual files generated from ChatGPT Business.
- GitHub commits created from ChatGPT-originated work.

## Integration workflow

1. Ask the user for the ChatGPT Business export ZIP or copied conversation files.
2. Store raw imports under `/home/workspace/Records/Imports/ChatGPT Business/Raw/`.
3. Extract and normalize useful conversations into markdown under `/home/workspace/Records/Imports/ChatGPT Business/Processed/`.
4. Classify each asset into: strategy, campaign, eBook, code spec, automation, prompt, Canva brief, agent/swarm spec, or website plan.
5. Convert high-value content into durable workspace files.
6. Mirror the approved materials into the relevant GitHub repo.
7. Create a ChatGPT Business return package under `/home/workspace/Exports/` so ChatGPT Business can continue from the newest Zo/GitHub state.

## Required safeguards

- Do not store secrets, API keys, personal credentials, or unnecessary private data.
- Mark income, funding, crypto, tax, legal, or investment material as educational unless professionally verified.
- Keep raw exports separate from processed summaries.
- Prefer condensed reusable assets over full transcript duplication.

## Output format

Return:

- Import status
- Files processed
- Durable files created
- GitHub mirror targets
- ChatGPT Business return package
- Blockers or needed user input
