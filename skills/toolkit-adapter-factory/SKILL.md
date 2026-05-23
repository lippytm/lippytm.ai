---
name: toolkit-adapter-factory
description: Use when creating reusable adapter templates for AI agent toolkits, APIs, GitHub repos, Zapier automations, ChatGPT Business workflows, Claude reviews, MCP servers, no-code platforms, or swarm systems that need standardized data contracts and safe handoffs.
compatibility: Created for Zo Computer
metadata:
  author: lippytmai.zo.computer
---
# Toolkit Adapter Factory

## Purpose

Create reusable adapters so LippytmAI AI Agentic Super Synthetic Intelligence Engines AgentsBots Swarms can work with different agent frameworks and automation platforms consistently.

## Adapter creation process

1. Identify toolkit or platform.
2. Define task types the adapter should support.
3. Create a normalized task packet.
4. Create a normalized result packet.
5. Define authentication and secret boundaries.
6. Add logging and failure handling.
7. Add human approval gates when needed.
8. Store the adapter specification in GitHub and workspace records.

## Standard task packet

```json
{
  "task_id": "uuid-or-readable-id",
  "source": "lippytmai",
  "target_toolkit": "toolkit-name",
  "mission": "one-sentence mission",
  "task_type": "research|draft|code|review|publish-proposal|automation-proposal",
  "inputs": {},
  "constraints": [],
  "approval_required": true,
  "logging_target": "github-issue-or-workspace-path",
  "return_format": "markdown|json|file|issue-comment"
}
```

## Standard result packet

```json
{
  "task_id": "same-id",
  "status": "success|needs_review|blocked|failed",
  "summary": "short result summary",
  "artifacts": [],
  "risks": [],
  "recommended_next_step": "next safe action",
  "approval_needed": true
}
```

## Best practices

- Prefer adapters over one-off integrations.
- Keep adapters narrow and auditable.
- Do not hardcode secrets.
- Separate draft generation from publishing.
- Separate fiction/entertainment outputs from serious financial or business advice.
- Use GitHub for versioned adapter specifications.
- Use Zapier for simple cross-app workflow movement before building custom code.
- Use MCP/API routes only when a repeatable tool-level bridge is needed.

## Output format

For each adapter, return:

- Adapter name
- Toolkit/platform
- Supported tasks
- Input schema
- Output schema
- Approval gates
- Security notes
- Logging target
- Test payload
- First build step
