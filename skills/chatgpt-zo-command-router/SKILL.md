---
name: chatgpt-zo-command-router
description: Use when converting ChatGPT Business outputs into structured Zo Computer command packets, routing tasks to workspace areas, GitHub repos, Zo Space pages, Zapier automations, Canva briefs, Skills, or AgentBot swarms.
compatibility: Created for Zo Computer
metadata:
  author: lippytmai.zo.computer
---
# ChatGPT → Zo Command Router

## Purpose

Convert ChatGPT Business output into actionable Zo Computer packets so ideas become files, GitHub commits, public pages, automations, campaigns, eBooks, or AgentBot swarm tasks.

## Standard workflow

1. Receive ChatGPT output or import index.
2. Run `scripts/route_chatgpt_commands.py` on a markdown/text file or processed import folder.
3. Review the generated command packet index.
4. Promote each packet into the correct workflow:
   - planning packet
   - campaign packet
   - ebook packet
   - code/spec packet
   - Zapier packet
   - Canva packet
   - skill packet
   - AgentBot/swarm packet
   - Web3 affiliate packet
   - GetBizFunds packet
5. Use GitHub sync automation for approved outputs.

## Routing rules

- Revenue, offers, funnels → `Campaigns/` or `Ebooks/`
- Durable business systems → `Records/Workflows/`
- New reusable processes → `Skills/`
- Site/page ideas → Zo Space or Zo Sites decision
- Lead/payment/wallet flows → GetBizFunds + governance review
- Agent/swarm systems → AgentBot workflow files and Skill stack

## Output

Return command packets with:

- packet_id
- source_file
- task_type
- target_area
- target_repo
- approval_required
- risk_level
- suggested_next_step
