"""5-segment email nurture sequences for AI Business Automation audience.

Segments: ai_entrepreneur, business_owner, developer, marketer, general
Each sequence: 5 emails over 14 days
Goal: convert subscribers to Twin.so trials via affiliate link
"""
from __future__ import annotations

import os
import json
import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

import anthropic

logger = logging.getLogger(__name__)

AFFILIATE_LINK = "https://twin.so?via=charles-lipshay"


class EmailSegment(str, Enum):
    AI_ENTREPRENEUR = "ai_entrepreneur"
    BUSINESS_OWNER = "business_owner"
    DEVELOPER = "developer"
    MARKETER = "marketer"
    GENERAL = "general"


@dataclass
class Email:
    subject: str
    preview_text: str
    body_html: str
    send_day: int  # days after signup
    cta_text: str
    cta_url: str
    segment: EmailSegment


SEQUENCES: dict[EmailSegment, list[dict]] = {
    EmailSegment.AI_ENTREPRENEUR: [
        {
            "send_day": 0,
            "subject": "Your AI automation starter kit is here",
            "preview": "Everything you need to automate 85% of your business...",
            "body": """Hey {first_name},

You're building something real with AI — I can tell.

Here's the exact stack I use to run my Business of Businesses (20 repos, 8 AI swarms, all automated):

**The Core Stack:**
• **Claude AI** — Strategic analysis, content, code (claude.ai)
• **Zapier** — Connects 8,000+ apps without code
• **Twin.so** — Your AI twin for sales calls 24/7
• **Cloudflare Workers** — Zero-cost serverless backend
• **Notion** — AI-powered knowledge base & KPIs

**What this stack costs:**
• Claude: $20/mo (Pro) or API usage
• Zapier: Free tier covers basics
• Twin.so: from $49/mo → **worth 10x that in time saved**
• Cloudflare: Free for 100K requests/day
• Notion: Free for solo

**Total: ~$100-200/mo for an AI-powered business machine.**

In the next email, I'll show you how to set up your first AI agent in 30 minutes.

To your automation,
Charles @ lippytm.ai

P.S. If you want to skip ahead, I highly recommend starting with Twin.so:
👉 {affiliate_link}
30-day free trial, cancel anytime.""",
        },
        {
            "send_day": 2,
            "subject": "Set up your first AI agent in 30 min (step by step)",
            "preview": "No code required. I timed it — exactly 28 minutes.",
            "body": """Hey {first_name},

Time check: can you spare 30 minutes today?

Because in 30 minutes, you can have an AI agent running that:
✅ Answers questions about your business 24/7
✅ Qualifies leads before they talk to you
✅ Books calls on your calendar automatically
✅ Follows up with no-shows (relentlessly)

**The 30-minute setup:**

1. **Sign up for Twin.so** (5 min)
   👉 {affiliate_link}
   
2. **Record a 10-minute training video** (10 min)
   Just talk about your business — who you help, what you do, how you work.
   Twin.so learns from this.

3. **Connect your calendar** (2 min)
   Calendly, Cal.com, or Google Calendar.

4. **Embed the chat widget on your site** (3 min)
   Copy one line of code.

5. **Test it yourself** (10 min)
   Chat with your own AI twin. Refine the responses.

That's it. Your AI sales agent is live.

I'll see you in the next email where I share actual revenue numbers from Month 1.

Charles""",
        },
        {
            "send_day": 5,
            "subject": "Month 1 results: $8,500 MRR from AI automation",
            "preview": "Here's exactly what worked and what didn't...",
            "body": """Hey {first_name},

Real numbers, no fluff:

**Month 1 Revenue by Channel:**
• SaaS subscriptions: $5,000
• Affiliate commissions: $500
• Web3/NFT: $2,000
• Marketplace: $1,000
• **Total MRR: $8,500**

**What drove it:**
1. Twin.so handling 23 inbound leads → 4 converted to $99/mo plans
2. Affiliate content on LinkedIn → 847 clicks → $500 in commissions
3. Automated follow-up sequences (like this one!) → 32% open rate

**What didn't work:**
- Posting without a clear CTA (obvious in hindsight)
- Trying to automate too much too fast (broke things)
- Not segmenting email list early enough (you're reading this because I fixed that)

**Month 3 target: $45K MRR**
Here's the math:
- Twin.so affiliate: 20 referrals × $99 × 30% = $594/mo in commissions
- SaaS: 200 customers × $100 avg = $20,000
- Marketplace + Web3: $24,400

Completely achievable with the right systems.

Next email: The exact Zapier automations that run my business while I sleep.

Charles""",
        },
        {
            "send_day": 8,
            "subject": "The 5 Zapier automations that run my business on autopilot",
            "preview": "Set these up once. They run forever.",
            "body": """Hey {first_name},

These 5 Zapier automations save me 20+ hours every week:

**1. Lead → CRM → Slack notification**
Trigger: New form submission on any landing page
Action: Create HubSpot contact → Send Slack alert with lead score
Time saved: 2 hrs/week of manual data entry

**2. Twin.so conversation → Follow-up email**
Trigger: Twin.so chat ends without booking
Action: Wait 2 hours → Send personalized follow-up via Gmail
Conversion lift: +34%

**3. New GitHub commit → Notion page**
Trigger: Push to any of my 20 repos
Action: Create Notion entry with commit details + Claude AI summary
Time saved: 3 hrs/week of documentation

**4. Content posted → Multi-platform syndication**
Trigger: New post on LinkedIn
Action: Cross-post to Twitter, save to Notion content library
Reach multiplier: 3x same effort

**5. Daily revenue report**
Trigger: Every morning at 8AM
Action: Pull Stripe data → Calculate metrics → Send to Slack
Value: Never fly blind on cash flow

All of these are available on Zapier's free tier to start.

And once you have Twin.so handling leads, Automation #2 becomes your best money-maker.

👉 Start your Twin.so free trial: {affiliate_link}

Charles""",
        },
        {
            "send_day": 14,
            "subject": "Last email: here's the full system map",
            "preview": "Everything in one diagram. This is how the machine works.",
            "body": """Hey {first_name},

This is the last email in this sequence (though I'll keep sending weekly insights).

I wanted to leave you with the full picture:

**The lippytm.ai Business of Businesses Stack:**

```
AWARENESS
  LinkedIn/Twitter content → ManyChat bot → Email capture
                                          ↓
NURTURE  
  Email sequences (you're reading one now) → Education → Trust
                                          ↓
CONVERSION
  Twin.so AI twin → Qualifies lead → Books call → Closes deal
                                          ↓
DELIVERY
  Claude AI swarms → Execute work → Report to Notion → Bill via Stripe
                                          ↓
RETENTION
  Automated check-ins → Usage analytics → Upsell triggers
```

Every piece of this runs on < $200/mo in tools and 85% automation.

**Your next step:**
Pick the ONE bottleneck in your business right now and automate it.

For most people, the biggest bottleneck is sales — specifically, talking to enough people.
That's exactly what Twin.so solves.

👉 {affiliate_link} — 30-day free trial

If you ever want to dig into any of this, just reply to this email.

Charles @ lippytm.ai

P.S. If this sequence was valuable, share it with one person building with AI.
That's all I ask.""",
        },
    ],
    EmailSegment.BUSINESS_OWNER: [
        {
            "send_day": 0,
            "subject": "Welcome — your AI business guide starts here",
            "preview": "Cut 40+ hours of manual work this month...",
            "body": """Hey {first_name},

You run a real business. You don't need theory — you need tools that work.

Here's what I'll show you in this series:
1. How to automate your most time-consuming sales tasks (Day 2)
2. The $200/mo AI stack replacing a $8,000/mo team (Day 5)
3. Real numbers from a business running 85% on autopilot (Day 8)
4. How to create your own AI sales rep in under an hour (Day 14)

The single most impactful thing you can do right now:
Create an AI version of yourself to handle inbound leads.

Every minute you spend on a call that could have been automated is a minute you're not growing.

Twin.so does exactly this. It learns how you sell, then does it for you — 24/7.
👉 {affiliate_link}

More in 2 days.

Charles""",
        },
        {
            "send_day": 2,
            "subject": "How to never miss a hot lead again (automated)",
            "preview": "Speed-to-lead is the #1 predictor of close rate...",
            "body": """Hey {first_name},

Fact: Responding to a lead within 5 minutes vs 30 minutes increases close rate by 900%.

Most business owners respond in hours. Or days. Or... never.

Here's how I solved this permanently:

1. **Twin.so on my website** responds to every visitor instantly
2. Qualifies them with 3 key questions
3. If qualified → books call on my calendar automatically
4. If not qualified → nurtures with educational content
5. I only talk to people who are ready to buy

The result: I went from 20% lead response rate to 100%.
Close rate improved 3x.

Setup time: 30 minutes.
Cost: $49/mo.
ROI: 1 extra deal/month pays for it 10x over.

👉 {affiliate_link} — try it free for 30 days

Charles""",
        },
        {
            "send_day": 5,
            "subject": "The $200/mo stack replacing an $8,000/mo team",
            "preview": "I fired no one — I just stopped needing to hire...",
            "body": """Hey {first_name},

Here's a breakdown that might surprise you:

**What a $8,000/mo team used to do for me:**
- 1 SDR for outbound ($3,500/mo)
- 1 VA for admin ($1,500/mo)
- 1 social media manager ($2,000/mo)
- 1 part-time ops ($1,000/mo)

**What my $200/mo AI stack does instead:**
- Claude AI swarms: strategy, content, analysis → replaces strategist
- Twin.so: all inbound sales qualification → replaces SDR
- Zapier: all integrations and data flow → replaces VA
- Buffer/Publer: content scheduling → replaces social manager

**Net savings: $7,800/mo or $93,600/year.**

I'm not saying you should fire people. I'm saying you should stop needing to hire them in the first place.

Start with the biggest bottleneck: sales. Fix that with Twin.so.
👉 {affiliate_link}

Charles""",
        },
        {
            "send_day": 8,
            "subject": "Case study: 3x revenue in 90 days with AI automation",
            "preview": "The exact playbook, step by step...",
            "body": """Hey {first_name},

90-day automation playbook (what I actually did):

**Month 1 — Foundation ($8.5K MRR)**
- Deployed Twin.so → immediate lead qualification
- Set up 5-email nurture sequence (like this one)
- Connected Zapier for lead → CRM automation

**Month 2 — Scale (target: $45K MRR)**
- LinkedIn content flywheel running daily
- Twin.so handling 50+ conversations/week
- ManyChat bot qualifying social media leads
- 3 new revenue streams activated

**Month 3 — Optimize (target: $167K MRR)**
- AI swarms running full analysis weekly
- A/B testing top-performing content
- Affiliate income compounding

**The key insight: automate sales FIRST.**
Everything else compounds once leads are flowing.

Twin.so is how you start.
👉 {affiliate_link} — 30-day free trial, no card needed

Charles""",
        },
        {
            "send_day": 14,
            "subject": "You have everything you need. Here's your first action.",
            "preview": "One step. 30 minutes. Compounding results.",
            "body": """Hey {first_name},

This is the last structured email — though I'll keep sending weekly insights.

You've learned:
✅ Speed-to-lead is the #1 sales lever
✅ AI can handle 80% of your sales process
✅ $200/mo in tools replaces $8K/mo in headcount
✅ The 90-day playbook to 3x revenue

Your one action right now:
**Start a Twin.so free trial.**

Not because I get a commission (I do, full disclosure — 30% recurring).
Because it's the fastest path to automated revenue.

Every day without it, you're leaving money on the table.

👉 {affiliate_link}

Let me know if you have questions. Just reply to this email.

Charles @ lippytm.ai""",
        },
    ],
    EmailSegment.DEVELOPER: [
        {
            "send_day": 0,
            "subject": "Dev to AI entrepreneur: the technical stack",
            "preview": "Claude API + Cloudflare Workers + Twin.so = automated revenue...",
            "body": """Hey {first_name},

You're a developer. Let's skip the fluff.

Here's the exact technical stack I use to run a Business of Businesses on autopilot:

```python
# The lippytm.ai AI swarms stack
stack = {
    "ai_core": "Claude API (claude-opus-4-8 + prompt caching)",
    "backend": "Cloudflare Workers + D1 (SQLite) + KV",
    "scheduler": "GitHub Actions (cron: '0 7 * * 1-5')",
    "sales": "Twin.so (AI sales agent)",
    "crm": "HubSpot (free tier)",
    "notifications": "Slack webhooks",
    "storage": "Cloudflare R2 (reports), Notion (knowledge)",
    "integrations": "Zapier (8,000+ apps)",
}
```

Full source code on GitHub: https://github.com/lippytm/lippytm.ai

Over the next 2 weeks, I'll cover:
- Prompt caching to cut Claude API costs 60-90%
- GitHub Actions as a free AI scheduler
- Cloudflare Workers as zero-cost serverless AI backend
- Using Twin.so as a revenue layer on top of any AI product

The affiliate angle: if you're selling any AI product, Twin.so is the fastest way to add a sales layer.
👉 {affiliate_link}

Charles""",
        },
        {
            "send_day": 2,
            "subject": "Cut Claude API costs 60-90% with prompt caching",
            "preview": "cache_control: ephemeral on system prompts. That's it.",
            "body": """Hey {first_name},

Quick technical win:

Prompt caching with Claude cuts API costs 60-90% on repeated calls.

```python
# Before: pay full price every call
messages.create(
    model="claude-opus-4-8",
    system="[2000 token system prompt]",  # charged every time
    messages=[...]
)

# After: cache the system prompt
messages.create(
    model="claude-opus-4-8",
    system=[
        {
            "type": "text",
            "text": "[2000 token system prompt]",
            "cache_control": {"type": "ephemeral"}  # cached for 5 min
        }
    ],
    messages=[...]
)
```

With 8 swarm agents running daily, this saves ~$180/mo in API costs.

Full implementation in the repo:
https://github.com/lippytm/lippytm.ai/blob/main/life_business_model/agents/base_agent.py

Next: GitHub Actions as a free AI job scheduler (no servers needed).

Charles""",
        },
        {
            "send_day": 5,
            "subject": "GitHub Actions as a free AI swarm scheduler",
            "preview": "0 7 * * 1-5 — 5 lines of YAML, runs forever free",
            "body": """Hey {first_name},

No need for a cron server. GitHub Actions runs your AI swarms free:

```yaml
# .github/workflows/ai_swarms_daily.yml
name: Daily AI Swarms
on:
  schedule:
    - cron: '0 7 * * 1-5'  # 7AM UTC, weekdays
  workflow_dispatch:  # manual trigger

jobs:
  run-swarms:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: pip install anthropic
      - name: Run AI Swarms
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          python -m life_business_model full \\
            --output reports/$(date +%Y-%m-%d).json
      - name: Commit report
        run: |
          git config user.email "swarms@lippytm.ai"
          git add reports/
          git commit -m "Daily swarm report $(date +%Y-%m-%d)" || true
          git push
```

2,000 free minutes/month on GitHub Free. More than enough.

The revenue layer on top: Twin.so handles all the sales while the swarms run strategy.
👉 {affiliate_link}

Charles""",
        },
        {
            "send_day": 8,
            "subject": "Cloudflare Workers: free AI API backend (100K req/day)",
            "preview": "D1 SQLite + KV store + Workers = zero-cost AI backend",
            "body": """Hey {first_name},

Cloudflare Workers free tier:
- 100,000 requests/day
- D1 SQLite (5GB storage)
- KV store (1GB)
- R2 (10GB storage)

Perfect for AI API backends.

My setup:
```javascript
// cloudflare_worker/src/index.js
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    
    // Store swarm results in D1
    if (url.pathname === '/swarm/result') {
      const body = await request.json();
      await env.DB.prepare(
        'INSERT INTO swarm_runs (name, result, ts) VALUES (?, ?, ?)'
      ).bind(body.swarm, JSON.stringify(body.result), Date.now()).run();
      return Response.json({ ok: true });
    }
    
    // Serve KPIs
    if (url.pathname === '/kpis') {
      const kpis = await env.DB.prepare(
        'SELECT * FROM kpis ORDER BY updated_at DESC LIMIT 20'
      ).all();
      return Response.json(kpis.results);
    }
  }
};
```

Full source: https://github.com/lippytm/lippytm.ai/tree/main/cloudflare_worker

Next: how to use Twin.so as a revenue API on top of any AI project.
👉 {affiliate_link}

Charles""",
        },
        {
            "send_day": 14,
            "subject": "Ship it: your AI business in production",
            "preview": "Everything you need to go from side project to revenue",
            "body": """Hey {first_name},

You've been following along for 2 weeks. Here's the production checklist:

**Week 1: Core Infrastructure**
- [ ] Claude API key + prompt caching configured
- [ ] Cloudflare Workers deployed with D1 + KV
- [ ] GitHub Actions running daily swarms

**Week 2: Revenue Layer**
- [ ] Twin.so trained and live on your site
- [ ] Email capture + 5-email nurture sequence
- [ ] First affiliate commission received

**Week 3-4: Scale**
- [ ] Content flywheel posting daily
- [ ] ManyChat bot qualifying social leads
- [ ] 10+ referrals in Twin.so pipeline

The full source code is open:
https://github.com/lippytm/lippytm.ai

Fork it, adapt it, ship it.

And if you want to monetize your AI audience immediately:
👉 {affiliate_link} (30% recurring — I get paid every month your referrals stay)

Charles @ lippytm.ai""",
        },
    ],
    EmailSegment.GENERAL: [
        {
            "send_day": 0,
            "subject": "Welcome to AI Business Automation Weekly",
            "preview": "Your guide to building with AI starts here...",
            "body": """Hey {first_name},

Welcome aboard.

I'm Charles — I run lippytm.ai, a Business of Businesses built almost entirely on AI automation.

Every week, I share:
- The exact tools and tactics I use to grow revenue
- Technical deep-dives into AI automation stacks
- Real numbers from a business running at 85% automation

This week's top tool: **Twin.so**

Create an AI version of yourself that handles sales calls, qualifies leads, and books meetings — 24/7.

I use it to handle all my inbound leads. Saves 20+ hours/week.

👉 Try it free: {affiliate_link}

See you next week,
Charles @ lippytm.ai""",
        },
        {
            "send_day": 3,
            "subject": "The AI automation stack under $200/mo",
            "preview": "Full breakdown of what I actually use...",
            "body": """Hey {first_name},

Quick breakdown of my full AI stack:

**For AI intelligence:** Claude API (~$50-100/mo)
**For automation:** Zapier free tier
**For sales:** Twin.so ($49/mo)
**For backend:** Cloudflare free tier
**For knowledge:** Notion free tier

Total: ~$100-150/mo for a system that replaces $8K/mo in labor.

The highest-ROI tool: **Twin.so**.

One extra qualified lead/month = paid for itself 10x.

👉 {affiliate_link} — start free

Charles""",
        },
        {
            "send_day": 7,
            "subject": "How I target $167K MRR with AI (the math)",
            "preview": "Breaking down each revenue stream...",
            "body": """Hey {first_name},

Here's the 6-month revenue breakdown:

| Stream | Month 1 | Month 6 |
|--------|---------|--------|
| SaaS | $5K | $54K |
| Affiliate | $500 | $5K |
| Web3 | $2K | $88K |
| Marketplace | $1K | $25K |
| **Total** | **$8.5K** | **$172K** |

The fastest path to $5K/mo passively: Twin.so affiliate.
166 active referrals × $99 avg × 30% = $4,900/mo.
Grows every month as long as customers stay subscribed.

My affiliate link: {affiliate_link}

Charles""",
        },
        {
            "send_day": 10,
            "subject": "The 30-minute AI sales setup",
            "preview": "Deploy once, close deals forever...",
            "body": """Hey {first_name},

30 minutes to set up an AI sales agent:

1. Sign up at Twin.so ({affiliate_link})
2. Record 10-min training video about your business
3. Connect your calendar
4. Add 1 line of code to your website
5. Your AI twin is live

It handles objections, qualifies leads, books calls.
You only talk to people ready to buy.

Free trial — no card required.
👉 {affiliate_link}

Charles""",
        },
        {
            "send_day": 14,
            "subject": "Last one: your AI automation action plan",
            "preview": "Pick one thing and start today...",
            "body": """Hey {first_name},

Final structured email. One recommendation:

**If you do ONE thing from this sequence, make it this:**
Set up Twin.so to handle your inbound leads.

Every other automation builds on top of leads flowing in.
Without that, nothing else matters.

30-day free trial: {affiliate_link}

I'll keep sending weekly insights with real numbers, new tools, and what's working.

Charles @ lippytm.ai""",
        },
    ],
}


class EmailSequenceEngine:
    """Manages email sequences and generates personalized content via Claude."""

    def __init__(self, api_key: str | None = None):
        self.client = anthropic.Anthropic(api_key=api_key or os.environ.get("ANTHROPIC_API_KEY"))

    def get_sequence(self, segment: EmailSegment) -> list[dict]:
        """Return the email sequence for a given segment."""
        return SEQUENCES.get(segment, SEQUENCES[EmailSegment.GENERAL])

    def personalize(self, email_template: dict, subscriber: dict) -> dict:
        """Personalize email body using subscriber data."""
        email = email_template.copy()
        email["body"] = email["body"].format(
            first_name=subscriber.get("first_name", "there"),
            affiliate_link=AFFILIATE_LINK,
            company=subscriber.get("company", "your company"),
        )
        return email

    def enhance_with_ai(self, email_template: dict, subscriber_context: str = "") -> dict:
        """Use Claude to enhance personalization based on subscriber context."""
        prompt = f"""Enhance this email body to be more personalized.

Original email (Day {email_template['send_day']}):
{email_template['body'][:500]}

Subscriber context: {subscriber_context}

Rules:
- Keep the same structure and CTAs
- Make the tone feel more personal/direct
- Max 10% longer than original
- Keep {affiliate_link} placeholder intact

Return the enhanced body text only."""

        response = self.client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=800,
            messages=[{"role": "user", "content": prompt}],
        )
        email_template["body"] = response.content[0].text
        return email_template

    def get_all_sequences_summary(self) -> dict:
        """Return a summary of all sequences."""
        return {
            segment.value: {
                "email_count": len(seq),
                "days_span": seq[-1]["send_day"] if seq else 0,
                "subjects": [e["subject"] for e in seq],
            }
            for segment, seq in SEQUENCES.items()
        }
