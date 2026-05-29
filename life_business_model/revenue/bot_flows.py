"""ManyChat/chatbot qualification flows for AI business automation leads.

Flow design:
- Entry: comment keyword triggers (AI, automate, swarm, business)
- Qualification: 3-question flow to segment lead
- Exit: send appropriate affiliate link + enroll in email sequence
"""
from __future__ import annotations

import os
import json
import logging
from dataclasses import dataclass, field
from typing import Callable, Optional

import anthropic

logger = logging.getLogger(__name__)

AFFILIATE_LINK = "https://twin.so?via=charles-lipshay"


@dataclass
class BotMessage:
    text: str
    quick_replies: list[str] = field(default_factory=list)
    media_url: str = ""
    delay_ms: int = 500


@dataclass
class BotNode:
    id: str
    message: BotMessage
    next_nodes: dict[str, str] = field(default_factory=dict)  # reply → node_id
    is_terminal: bool = False
    tag: str = ""  # segment tag to apply
    action: str = ""  # email_subscribe, notify_owner, etc.


@dataclass
class BotFlow:
    name: str
    trigger_keywords: list[str]
    platform: str  # manychat, chatfuel, botbuilders
    nodes: dict[str, BotNode]
    entry_node: str

    def to_manychat_json(self) -> dict:
        """Export flow as ManyChat-compatible JSON for import."""
        flow_data = {
            "name": self.name,
            "trigger": {"keywords": self.trigger_keywords, "match": "any"},
            "messages": [],
        }
        for node_id, node in self.nodes.items():
            msg = {
                "id": node_id,
            "type": "text",
                "text": node.message.text,
                "delay": node.message.delay_ms,
            }
            if node.message.quick_replies:
                msg["quick_replies"] = [
                    {"title": r, "next": node.next_nodes.get(r, "end")}
                    for r in node.message.quick_replies
                ]
            if node.tag:
                msg["actions"] = [{"type": "add_tag", "tag": node.tag}]
            flow_data["messages"].append(msg)
        return flow_data


class BotFlowEngine:
    """Manages bot qualification flows with Claude-powered dynamic responses."""

    # Main qualification flow — 3 questions to segment lead
    MAIN_FLOW = BotFlow(
        name="AI Business Automation Qualifier",
        trigger_keywords=["AI", "automate", "automation", "swarm", "business", "tools"],
        platform="manychat",
        entry_node="welcome",
        nodes={
            "welcome": BotNode(
                id="welcome",
                message=BotMessage(
                    text=(
                        "Hey! 👋 Thanks for reaching out.\n\n"
                        "I'm sharing a free AI automation guide with everyone who connects here.\n\n"
                        "Quick question to make sure I send you the right stuff:"
                    ),
                    quick_replies=[],
                    delay_ms=800,
                ),
                next_nodes={"default": "q1"},
            ),
            "q1": BotNode(
                id="q1",
                message=BotMessage(
                    text="What best describes you?",
                    quick_replies=[
                        "Building an AI business",
                        "I run an existing business",
                        "Developer / technical",
                        "Marketer / creator",
                    ],
                    delay_ms=500,
                ),
                next_nodes={
                    "Building an AI business": "q2_ai_entrepreneur",
                    "I run an existing business": "q2_business_owner",
                    "Developer / technical": "q2_developer",
                    "Marketer / creator": "q2_marketer",
                },
                tag="",
            ),
            "q2_ai_entrepreneur": BotNode(
                id="q2_ai_entrepreneur",
                message=BotMessage(
                    text="Nice! What's your biggest challenge right now?",
                    quick_replies=[
                        "Scaling revenue",
                        "Finding customers",
                        "Automating operations",
                        "Building the product",
                    ],
                ),
                next_nodes={"default": "q3"},
                tag="segment:ai_entrepreneur",
            ),
            "q2_business_owner": BotNode(
                id="q2_business_owner",
                message=BotMessage(
                    text="Got it. What's eating most of your time?",
                    quick_replies=[
                        "Sales & follow-up",
                        "Customer support",
                        "Admin & operations",
                        "Content & marketing",
                    ],
                ),
                next_nodes={"default": "q3"},
                tag="segment:business_owner",
            ),
            "q2_developer": BotNode(
                id="q2_developer",
                message=BotMessage(
                    text="Cool! What are you working on?",
                    quick_replies=[
                        "Building AI products",
                        "Automating my workflow",
                        "Monetizing AI skills",
                        "Just exploring",
                    ],
                ),
                next_nodes={"default": "q3"},
                tag="segment:developer",
            ),
            "q2_marketer": BotNode(
                id="q2_marketer",
                message=BotMessage(
                    text="Love it! What's your main goal?",
                    quick_replies=[
                        "More leads",
                        "Better conversions",
                        "Content at scale",
                        "Affiliate income",
                    ],
                ),
                next_nodes={"default": "q3"},
                tag="segment:marketer",
            ),
            "q3": BotNode(
                id="q3",
                message=BotMessage(
                    text="Last one — what's your current monthly revenue (or target)?",
                    quick_replies=[
                        "Pre-revenue",
                        "$1K - $10K/mo",
                        "$10K - $50K/mo",
                        "$50K+/mo",
                    ],
                ),
                next_nodes={
                    "Pre-revenue": "result_starter",
                    "$1K - $10K/mo": "result_growth",
                    "$10K - $50K/mo": "result_scale",
                    "$50K+/mo": "result_enterprise",
                },
            ),
            "result_starter": BotNode(
                id="result_starter",
                message=BotMessage(
                    text=(
                        f"Perfect — I've got exactly the right guide for you.\n\n"
                        f"**AI Business Automation Starter Kit** (free):\n"
                        f"→ The $200/mo stack to replace $8K/mo in labor\n"
                        f"→ How to get your first 10 customers with AI\n"
                        f"→ Step-by-step automation playbook\n\n"
                        f"I'm also sending you access to Twin.so — the #1 tool for getting early customers:\n"
                        f"{AFFILIATE_LINK}\n\n"
                        f"What email should I send the guide to?"
                    ),
                    delay_ms=1000,
                ),
                next_nodes={"default": "email_capture"},
                tag="revenue:pre",
                action="email_subscribe",
            ),
            "result_growth": BotNode(
                id="result_growth",
                message=BotMessage(
                    text=(
                        f"Nice — you're in the growth phase. Let me send you what's working at this stage.\n\n"
                        f"**AI Growth Acceleration Guide** (free):\n"
                        f"→ 5 automations that 10x lead response rate\n"
                        f"→ How Twin.so can double your close rate\n"
                        f"→ The Zapier flows saving 20 hrs/week\n\n"
                        f"Tool I recommend at your stage: {AFFILIATE_LINK}\n\n"
                        f"What email should I send this to?"
                    ),
                    delay_ms=1000,
                ),
                next_nodes={"default": "email_capture"},
                tag="revenue:1k_10k",
                action="email_subscribe",
            ),
            "result_scale": BotNode(
                id="result_scale",
                message=BotMessage(
                    text=(
                        f"You're scaling — this is where AI really compounds.\n\n"
                        f"**AI Scale Playbook** (free):\n"
                        f"→ How to build AI swarms for each business unit\n"
                        f"→ Cloudflare Workers as zero-cost AI backend\n"
                        f"→ Path to $167K MRR with 85% automation\n\n"
                        f"At your stage, I'd prioritize Twin.so for sales automation:\n"
                        f"{AFFILIATE_LINK}\n\n"
                        f"Email for the playbook?"
                    ),
                    delay_ms=1000,
                ),
                next_nodes={"default": "email_capture"},
                tag="revenue:10k_50k",
                action="email_subscribe",
            ),
            "result_enterprise": BotNode(
                id="result_enterprise",
                message=BotMessage(
                    text=(
                        f"You're at serious scale — let's talk AI infrastructure.\n\n"
                        f"I actually want to get on a call and walk you through our AI swarms setup.\n"
                        f"20 automated business units, $167K MRR target, full stack:\n"
                        f"GitHub: https://github.com/lippytm\n\n"
                        f"For your sales team: {AFFILIATE_LINK}\n\n"
                        f"What's your email so I can send calendar link?"
                    ),
                    delay_ms=1200,
                ),
                next_nodes={"default": "email_capture"},
                tag="revenue:50k_plus",
                action="notify_owner",
            ),
            "email_capture": BotNode(
                id="email_capture",
                message=BotMessage(
                    text="Type your email below and I'll send everything right now 👇",
                ),
                next_nodes={"default": "thank_you"},
                action="capture_email",
            ),
            "thank_you": BotNode(
                id="thank_you",
                message=BotMessage(
                    text=(
                        "✅ Guide sent! Check your inbox in the next 2 minutes.\n\n"
                        "While you wait — here's the #1 tool from the guide:\n"
                        f"{AFFILIATE_LINK}\n\n"
                        "30-day free trial, no card needed.\n\n"
                        "See you inside! 🚀"
                    ),
                    delay_ms=500,
                ),
                is_terminal=True,
                action="send_welcome_email",
            ),
        },
    )

    def __init__(self, api_key: str | None = None):
        self.client = anthropic.Anthropic(api_key=api_key or os.environ.get("ANTHROPIC_API_KEY"))
        self.flows = {self.MAIN_FLOW.name: self.MAIN_FLOW}

    def generate_dynamic_response(self, user_message: str, context: dict) -> str:
        """Generate a context-aware bot response using Claude for edge cases."""
        prompt = f"""You are a friendly chatbot for lippytm.ai, an AI automation business.

User said: \"{user_message}\"
Context: {json.dumps(context)}

Generate a natural, helpful response (max 3 sentences) that:
1. Acknowledges what they said
2. Guides them toward our AI automation guide
3. Includes our affiliate link if relevant: {AFFILIATE_LINK}

Tone: friendly, direct, peer-to-peer. No corporate speak."""

        response = self.client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=200,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text.strip()

    def export_manychat(self) -> dict:
        """Export all flows as ManyChat import JSON."""
        return {
            "version": "1.0",
            "flows": [flow.to_manychat_json() for flow in self.flows.values()],
            "setup_instructions": [
                "1. Go to manychat.com and connect Instagram/Facebook",
                "2. Go to Automation > Keywords",
                "3. Import this JSON file",
                "4. Set trigger keywords: AI, automate, business, tools",
                "5. Test by commenting 'AI' on one of your posts",
            ],
        }

    def get_flow_stats(self) -> dict:
        """Return stats about configured flows."""
        stats = {}
        for name, flow in self.flows.items():
            stats[name] = {
                "platform": flow.platform,
                "trigger_keywords": flow.trigger_keywords,
                "node_count": len(flow.nodes),
                "terminal_nodes": sum(1 for n in flow.nodes.values() if n.is_terminal),
                "has_email_capture": any(n.action == "capture_email" for n in flow.nodes.values()),
                "affiliate_link_in_flow": AFFILIATE_LINK,
            }
        return stats
