---
name: agentic-red-team-safety-review
description: Use when reviewing LippytmAI agents, AgentBots, automations, prompts, workflows, claims, public pages, financial/funding content, affiliate content, external messages, Zapier flows, GitHub actions, or autonomous systems for risk, misuse, privacy, security, hallucination, overclaiming, or unsafe automation.
compatibility: Created for Zo Computer
metadata:
  author: lippytmai.zo.computer
---
# Agentic Red Team Safety Review

## Purpose

Find and reduce risks before an AI agent, workflow, page, campaign, automation, or swarm affects users, money, reputation, privacy, or public systems.

## Review workflow

1. Identify what the system can do.
2. Identify who or what could be harmed if it fails.
3. Check for overpromising, especially funding, income, legal, tax, investment, health, or guaranteed outcomes.
4. Check for privacy or secret exposure.
5. Check for unsafe automation: external sending, payment actions, deleting data, changing live systems, or high-frequency runs.
6. Add approval gates, disclaimers, logging, and rollback.
7. Recommend the safest next build step.

## Risk categories

- Financial claims
- Affiliate disclosure
- Legal/tax/investment ambiguity
- Data privacy
- Credential exposure
- Prompt injection
- Automation runaway
- Public brand risk
- Poor user expectations
- Missing rollback

## Safer defaults

- Draft before send.
- Preview before publish.
- Human approval before external contact or money movement.
- Use read-only access unless write access is needed.
- Keep secrets in Zo Settings, never files.
- Log all important agent actions.
- Prefer reversible changes.

## Output format

Return:

- Risk summary
- Highest-risk failure modes
- Required approval gates
- Required disclaimers
- Data boundaries
- Rollback plan
- Safer alternative design
- Go / revise / stop recommendation
