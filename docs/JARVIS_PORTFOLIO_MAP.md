# Jarvis Portfolio Map

**Status:** This is the proposed commercial ownership map, not evidence that the repositories are integrated or deployed. `lippytm.ai` is the commercial source of truth for the first launch.

## Ownership boundaries

| Repository | Proposed responsibility | First-launch relationship |
|---|---|---|
| [lippytm.ai](https://github.com/lippytm/lippytm.ai) | Commercial source of truth: offer, site, CRM definitions, campaigns, ebooks, operations, integration contracts, and acceptance tests | Own the offer and customer record; document or link external implementation work |
| [Hermes-AI-Hermes](https://github.com/lippytm/Hermes-AI-Hermes) | Orchestration, agent routing, memory, model delegation | Proposed decision/orchestration layer; not a launch dependency until an interface is tested |
| [Factory.ai](https://github.com/lippytm/Factory.ai) | Integrations, workflow execution, background jobs, connectors | Proposed execution layer for approved capture/follow-up/booking actions |
| [lippytm-lippytm.ai-tower-control-ai](https://github.com/lippytm/lippytm-lippytm.ai-tower-control-ai) | Operations control plane, fleet, quality, release gates, registries | Proposed cross-repo operations and release governance |
| [Chatlippytm.ai.Bots](https://github.com/lippytm/Chatlippytm.ai.Bots) | Customer-facing bots, channels, training, human handoff | Candidate conversation surface; select one channel only after validation |
| [Prompt-11-](https://github.com/lippytm/Prompt-11-) | Prompt, policy, schema, and governance registry | Proposed canonical source for reusable prompt/policy versions |
| [The-Encyclopedia-of-Everything-Applied-ChatAIBots](https://github.com/lippytm/The-Encyclopedia-of-Everything-Applied-ChatAIBots) | Education and ebook/audiobook/videobook source material | Source material; publishable assets and rights still require review |
| [lippytmai.getbizfunds.com-](https://github.com/lippytm/lippytmai.getbizfunds.com-) | Marketing campaigns and affiliate funnel assets | Planned Hostinger affiliate/business funnel; external publishing is not asserted |
| [AI-Time-Machines](https://github.com/lippytm/AI-Time-Machines) | R&D and experimental track | Parallel/later work; never a blocker for the first pilot |
| [Web3AI](https://github.com/lippytm/Web3AI) | Separate Web3 vertical | Parallel/later work; excluded from initial customer workflow |

## Dependencies and launch boundary

The first commercial workflow is limited to **lead capture → qualification → follow-up → appointment booking**. It needs a public entry point, consent-aware lead storage, a human-reviewed qualification rubric, a follow-up channel, and a calendar/booking destination. A pilot can use a manually operated step where a connector is not yet verified.

The proposed flow is `lippytm.ai` offer and customer definitions → (optional, after validation) customer-facing bot → orchestration/policy decision → approved connector execution → operations/quality monitoring. Prompt and content assets are versioned references; they do not replace product or legal approval. The actual order and transport are implementation decisions, not current guarantees.

Do not make first-launch completion depend on Web3AI, AI-Time-Machines, multi-agent automation, a billing platform, or integrations across every listed repository.

## Commercial source-of-truth rules

1. Keep first-launch offer, current price placeholders, customer commitments, consent language, KPIs, and launch status in this repository.
2. Each implementation repository owns its code, deployment, and technical behavior. This map does not transfer code ownership or prove a connection exists.
3. Link an external implementation and record its version/status here before treating it as a commercial dependency.
4. Resolve conflicting customer-facing claims in favor of the approved `lippytm.ai` offer record; never infer a feature from a roadmap or repository name.
5. Make changes traceable: owner, date, status (`proposed`, `in progress`, `verified`, `retired`), and evidence such as a test or observed pilot result.

## Evidence currently present in this repository

This repository contains strategy and workflow documentation, BrainKit templates/metadata, ebook/campaign assets, operational checklists, and tests for two JSON event-schema artifacts (`brainkit/contracts/customer-expansion-event-schema.json` and `brainkit/contracts/partner-event-schema.json`). Those artifacts do not establish working customer capture, booking, billing, affiliate tracking, or cross-repository runtime integrations. Verify every capability end-to-end before marking it `verified`.
