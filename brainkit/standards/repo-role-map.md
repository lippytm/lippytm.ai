# BrainKit Repo Role Map

This document classifies repositories in the lippytm ecosystem so they can be governed, scaled, and mass-manufactured without losing clarity.

## Why this exists

Every repository should have a clear role in the ecosystem. Repositories may support multiple functions, but each must declare:

- one **Primary Role**
- one optional **Secondary Role**
- one **Manufacturing Lane**
- one **Revenue Profile**
- one **Operational Risk Level**

This keeps the fleet structured as it grows.

---

## Primary Roles

### 1. Standards Hub
Owns shared templates, contracts, governance, naming, policy, and quality gates.

### 2. Control Tower
Coordinates execution across repositories, environments, agents, and external systems.

### 3. Swarm Fabric
Provides routing, messaging, coordination, escalation, and task delivery between agents.

### 4. Revenue Gateway
Captures leads, presents offers, and converts visitors into customers, users, or partners.

### 5. Product Surface
Presents a user-facing application, assistant, API, bot, or operational tool.

### 6. Commerce Layer
Handles payments, access, tokenization, subscriptions, licensing, or affiliate economics.

### 7. Knowledge / Media Layer
Produces educational, documentary, entertainment, or brand-building content assets.

### 8. Lab / Experiment Layer
Runs isolated prototypes, sandboxes, diagnostics, and innovation trials.

---

## Manufacturing Lanes

Every repo belongs to one primary lane.

| Lane | Purpose |
|---|---|
| `hub` | Shared standards and architectural authority |
| `control` | Orchestration, approvals, rollout, telemetry |
| `swarm` | Agent communication and execution fabric |
| `revenue` | Sites, funnels, offers, and conversion assets |
| `product` | Applications, bots, interfaces, operator tools |
| `commerce` | Payments, subscriptions, tokenized access |
| `knowledge` | Courses, ebooks, media, story systems |
| `lab` | Experiments, proofs of concept, temporary prototypes |

---

## Revenue Profiles

| Profile | Meaning |
|---|---|
| `direct` | Directly sells products, services, subscriptions, or access |
| `supporting` | Improves conversion, retention, speed, or delivery efficiency |
| `platform` | Enables many other repos to produce value |
| `experimental` | Explores future value, not expected to monetize immediately |

---

## Risk Levels

| Level | Meaning |
|---|---|
| `low` | Documentation or isolated experimentation |
| `moderate` | Internal automation or operational helper |
| `high` | Production workflows, public products, or revenue systems |
| `critical` | Security-sensitive, payment-sensitive, or fleet-control systems |

---

## Current Ecosystem Classification

### Tier A — Foundation Repositories

| Repository | Primary Role | Secondary Role | Lane | Revenue Profile | Risk |
|---|---|---|---|---|---|
| `lippytm/lippytm.ai` | Standards Hub | Knowledge / Media Layer | `hub` | `platform` | `critical` |
| `lippytm/lippytm-lippytm.ai-tower-control-ai` | Control Tower | Product Surface | `control` | `platform` | `critical` |
| `lippytm/MyClaw.lippytm.AI-` | Swarm Fabric | Product Surface | `swarm` | `platform` | `high` |

### Tier B — Product and Revenue Repositories

| Repository | Primary Role | Secondary Role | Lane | Revenue Profile | Risk |
|---|---|---|---|---|---|
| `lippytm/lippytmai.getbizfunds.com-` | Revenue Gateway | Product Surface | `revenue` | `direct` | `high` |
| `lippytm/Web3AI` | Commerce Layer | Product Surface | `commerce` | `direct` | `critical` |
| `lippytm/OpenClaw-lippytm.AI-` | Product Surface | Swarm Fabric | `product` | `supporting` | `moderate` |
| `lippytm/Chatlippytm.ai.Bots` | Product Surface | Control Tower | `product` | `supporting` | `high` |

### Tier C — Bot Product Family

| Repository | Primary Role | Secondary Role | Lane | Revenue Profile | Risk |
|---|---|---|---|---|---|
| `lippytm/Clawlippytm.ai.Bots` | Product Surface | Revenue Gateway | `product` | `direct` | `high` |
| `lippytm/Clawlippytm.Bots` | Product Surface | Revenue Gateway | `product` | `direct` | `high` |
| `lippytm/AllBots.com` | Product Surface | Revenue Gateway | `product` | `direct` | `high` |
| `lippytm/AllBots.com.ai` | Product Surface | Revenue Gateway | `product` | `direct` | `high` |

### Tier D — Knowledge and Creative System Repositories

| Repository | Primary Role | Secondary Role | Lane | Revenue Profile | Risk |
|---|---|---|---|---|---|
| `lippytm/The-Encyclopedia-of-Everything-Applied-ChatAIBots` | Knowledge / Media Layer | Product Surface | `knowledge` | `direct` | `moderate` |
| `lippytm/Quantum-Questions-of-the-Many-Worlds-Universes-of-Reruns-` | Knowledge / Media Layer | Lab / Experiment Layer | `knowledge` | `experimental` | `low` |
| `lippytm/AI-Time-Machines` | Knowledge / Media Layer | Lab / Experiment Layer | `knowledge` | `experimental` | `moderate` |
| `lippytm/Time-Machines-Builders-` | Knowledge / Media Layer | Product Surface | `knowledge` | `supporting` | `moderate` |
| `lippytm/Transparency-Logic-Time-Machine-Bots-` | Knowledge / Media Layer | Product Surface | `knowledge` | `supporting` | `moderate` |
| `lippytm/AI-Intergalactic-Zoological-Social-Multimedia-Agency-Networks-` | Knowledge / Media Layer | Revenue Gateway | `knowledge` | `experimental` | `low` |
| `lippytm/Evolutionary-Evolutions-Social-Multimedia-Networks-Agency-` | Knowledge / Media Layer | Revenue Gateway | `knowledge` | `experimental` | `low` |

### Tier E — Lab and Prototype Repositories

| Repository | Primary Role | Secondary Role | Lane | Revenue Profile | Risk |
|---|---|---|---|---|---|
| `lippytm/superagent-app` | Lab / Experiment Layer | Product Surface | `lab` | `experimental` | `moderate` |
| `lippytm/chronos-flow` | Lab / Experiment Layer | Control Tower | `lab` | `experimental` | `moderate` |
| `lippytm/zenith-tasks` | Lab / Experiment Layer | Product Surface | `lab` | `experimental` | `moderate` |
| `lippytm/Base44-` | Lab / Experiment Layer | Revenue Gateway | `lab` | `experimental` | `low` |
| `lippytm/Factory.ai` | Lab / Experiment Layer | Product Surface | `lab` | `experimental` | `moderate` |

---

## Required Metadata for Every Repository

Each repository should document the following in its README or `ARCHITECTURE.md`:

```yaml
repo_name: example-repo
primary_role: control_tower
secondary_role: product_surface
manufacturing_lane: control
revenue_profile: platform
risk_level: critical
operator_owner: lippytm
fleet_managed: true
brainkit_managed: true
```

---

## Promotion Rules

A repository can move from `lab` to another lane only if:

1. a clear user or operator problem is defined
2. architecture is documented
3. quality gates are defined
4. a revenue or platform purpose is declared
5. security and operational risks are reviewed

---

## Rule of thumb

If a repository cannot clearly explain why it exists, how it connects, and what kind of value it creates, it is not ready for mass manufacturing.
