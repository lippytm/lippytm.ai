---
name: chatgpt-business-import-automation
description: Use when importing, unpacking, normalizing, indexing, classifying, or summarizing ChatGPT Business export ZIPs, copied ChatGPT conversations, or ChatGPT-generated files into the LippytmAI Zo Computer workspace and GitHub-ready markdown structure.
compatibility: Created for Zo Computer
metadata:
  author: lippytmai.zo.computer
---
# ChatGPT Business Import Automation

## Purpose

Automate the import side of the ChatGPT Business → Zo Computer workflow.

## Inputs

Use this skill when the user provides:

- a ChatGPT Business export ZIP
- copied ChatGPT conversations
- markdown/text files from ChatGPT Business
- ChatGPT-generated specs, campaigns, eBooks, prompts, or code plans

## Standard workflow

1. Place raw source material under `/home/workspace/Records/Imports/ChatGPT Business/Raw/`.
2. Run `scripts/import_chatgpt_export.py` against the ZIP, directory, or file.
3. Store processed markdown under `/home/workspace/Records/Imports/ChatGPT Business/Processed/`.
4. Review `processed-index.md` for classification and next actions.
5. Promote high-value material into the right durable location:
   - `Records/Plans/`
   - `Records/Workflows/`
   - `Campaigns/`
   - `Ebooks/`
   - `Records/Templates/`
   - `Skills/`
6. Use GitHub sync automation after approval.

## Classification categories

- strategy
- campaign
- ebook
- code-spec
- automation
- prompt
- canva-brief
- agent-swarm
- web3-affiliate
- getbizfunds
- payment-wallet
- general

## Safeguards

- Do not promote secrets, API keys, passwords, or private credentials.
- Keep raw exports separate from processed summaries.
- Condense long transcripts into reusable assets instead of duplicating everything everywhere.
- Mark funding, legal, tax, investment, or crypto content as educational unless professionally verified.

## Output

Return:

- raw input path
- processed output path
- index path
- high-value candidates
- suggested GitHub repo target
- recommended next action
