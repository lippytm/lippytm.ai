---
name: chatgpt-zo-api-action-connector
description: Use when preparing ChatGPT Business or a custom GPT to call lippytmai.zo.computer/Zo APIs, create safe API action schemas, exchange task packets, or connect ChatGPT Business to Zo Computer through approved API keys and webhooks.
compatibility: Created for Zo Computer
metadata:
  author: lippytmai.zo.computer
---
# ChatGPT ↔ Zo API Action Connector

## Purpose

Create a safe API bridge so ChatGPT Business can send structured requests into Zo Computer and Zo Computer can produce response packages for ChatGPT Business.

## Important setup note

ChatGPT Business cannot use Zo's private credentials automatically. The user must create any required Zo access token in [Settings > Advanced](/?t=settings&s=advanced) and keep it secret. Do not place tokens in workspace files or GitHub.

## Recommended connection levels

1. **Manual package bridge**: ZIP exports/imports. Safest and default.
2. **GitHub bridge**: ChatGPT creates specs/docs; Zo syncs to GitHub.
3. **Zapier bridge**: ChatGPT-originated forms or docs trigger Zapier flows.
4. **API action bridge**: Custom GPT action calls a secured Zo API endpoint or Zo API token, only after approval.

## API safety rules

- Use least-privilege tokens.
- Use bearer auth.
- Log every request as a task packet.
- Require approval for public publishing, external messages, payments, wallet actions, and destructive edits.
- Never expose secrets in prompts, files, logs, or GitHub.

## References

Read `references/custom-gpt-action-openapi-template.yaml` when creating a Custom GPT Action schema.
Read `references/chatgpt-to-zo-api-setup.md` when preparing setup instructions.

## Output

Return:

- connection level
- required token/secrets
- endpoint or package path
- request schema
- response schema
- approval gates
- test packet
