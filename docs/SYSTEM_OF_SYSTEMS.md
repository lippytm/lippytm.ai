# System of Systems

The unifying meta-architecture for the lippytm Business of Businesses empire.
It does not replace any existing layer — it composes everything already
built into one coherent, queryable object so the empire can be operated and
scored as a single system instead of disconnected modules.

```
┌─────────────────────────────────────────────────────────────────┐
│  LIFE OS                                                         │
│  Wealth · Freedom · Impact · Legacy — scored pillars              │
│  life_business_model/models/life_os.py                            │
└───────────────────────────┬───────────────────────────────────────┘
                             │
┌───────────────────────────▼───────────────────────────────────────┐
│  BUSINESS OF BUSINESSES                                            │
│  12 business units / 20 repositories, revenue streams, KPIs        │
│  life_business_model/models/business_model.py                      │
└───────────────────────────┬───────────────────────────────────────┘
                             │
┌───────────────────────────▼───────────────────────────────────────┐
│  AI SWARM NETWORK                                                  │
│  8 specialized Claude swarms (tower_control, revenue_generation,    │
│  business_intelligence, content_marketing, web3_defi,               │
│  knowledge_research, legal_compliance, finance_funding)             │
│  life_business_model/orchestrator.py + life_business_model/swarms/  │
└───────────────────────────┬───────────────────────────────────────┘
                             │
┌───────────────────────────▼───────────────────────────────────────┐
│  CREATIVE ENGINE                                                    │
│  Claude + ChatGPT diversity ensemble → ebooks, audiobooks, videos,   │
│  blog posts, social content from one topic input                    │
│  life_business_model/content/                                       │
└───────────────────────────┬───────────────────────────────────────┘
                             │
┌───────────────────────────▼───────────────────────────────────────┐
│  PLATFORM MESH                                                      │
│  GitHub · Slack · Notion · Cloudflare · HubSpot · Asana ·            │
│  Anthropic · OpenAI                                                  │
│  life_business_model/platform_mesh.py                                │
└─────────────────────────────────────────────────────────────────┘
```

## The orchestrating object

`life_business_model/system_of_systems.py` exposes `SystemOfSystems`,
which composes `LifeOS`, `LifeBusinessModel`, `MasterOrchestrator`,
`CreativeStudio`, and `PlatformMesh` into one entry point.

```python
from life_business_model.system_of_systems import SystemOfSystems

sos = SystemOfSystems()
sos.print_full_status()          # instant, zero API cost — pillar scores,
                                  # platform connectivity, business summary,
                                  # registered swarms, creative engine status

report = sos.run(
    run_swarms=True,             # executes all 8 Claude swarms
    run_creative=True,
    creative_topic="How to Automate 85% of Your Business with AI Swarms",
)
sos.save_report(report, "reports/system_of_systems.json")
```

## CLI

```bash
python -m life_business_model.main system status
python -m life_business_model.main system run --swarms --creative "20 Repos, 8 AI Swarms, 1 Automated Empire" -o reports/today.json
```

`system status` requires no API key and makes no network calls — it is
safe to run anytime to see the current shape of the whole empire.
`system run` requires `ANTHROPIC_API_KEY` when `--swarms` is used, and
`OPENAI_API_KEY` (optional) for the ChatGPT half of the creative ensemble.

## Why this layer exists

Every layer below already worked independently: the swarms ran, the
content pipeline generated bundles, the business model tracked targets.
What was missing was a single object that could answer "what is the
state of the whole empire right now" in one call, and a single Slack
notification path (`PlatformMesh.notify`) that any layer can use without
re-implementing webhook plumbing. `SystemOfSystems` and `PlatformMesh`
are that connective layer — thin on purpose, so the underlying modules
stay the source of truth.
