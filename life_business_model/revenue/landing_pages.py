"""Cloudflare Pages landing page generator for affiliate funnel.

Generates HTML/CSS/JS landing pages:
- Affiliate page: Twin.so referral with email capture
- AI Starter Kit: lead magnet download page
- Webinar: live session registration
"""
from __future__ import annotations

import os
import json
import textwrap
from dataclasses import dataclass, field
from pathlib import Path

AFFILIATE_LINK = "https://twin.so?via=charles-lipshay"
SITE_NAME = "lippytm.ai"
ACCENT_COLOR = "#6366f1"  # indigo-500


@dataclass
class LandingPageConfig:
    title: str
    headline: str
    subheadline: str
    cta_text: str
    cta_url: str
    bullet_points: list[str] = field(default_factory=list)
    social_proof: str = ""
    urgency_text: str = ""
    page_type: str = "affiliate"  # affiliate, lead_magnet, webinar


class AffiliateLandingPage:
    """Generates the Twin.so affiliate landing page."""

    CONFIG = LandingPageConfig(
        title="AI Business Automation — Free Starter Kit | lippytm.ai",
        headline="Automate 85% of Your Business With AI\n(Under $200/Month)",
        subheadline=(
            "Download the free AI Automation Starter Kit — the exact stack used to build "
            "a Business of Businesses targeting $167K MRR with 20 automated projects."
        ),
        cta_text="Get the Free Starter Kit →",
        cta_url="#email-capture",
        bullet_points=[
            "The $200/mo AI stack that replaces an $8,000/mo team",
            "5 Zapier automations that save 20+ hours every week",
            "How to create your AI sales twin in 30 minutes",
            "GitHub Actions as a free AI swarm scheduler",
            "The 90-day playbook from $0 to $167K MRR",
        ],
        social_proof="Used by AI entrepreneurs targeting $1M+ ARR",
        urgency_text="Free for the first 500 subscribers",
        page_type="affiliate",
    )

    def render(self) -> str:
        c = self.CONFIG
        bullets_html = "\n".join(
            f'          <li class="bullet-item">✅ {bp}</li>'
            for bp in c.bullet_points
        )
        return textwrap.dedent(f"""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>{c.title}</title>
          <meta name="description" content="{c.subheadline}">
          <meta property="og:title" content="{c.headline.replace(chr(10), ' ')}">
          <meta property="og:description" content="{c.subheadline}">
          <style>
            *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
            body {{
              font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
              background: #0f0f13;
              color: #f1f1f4;
              line-height: 1.6;
            }}
            .hero {{
              min-height: 100vh;
              display: flex;
              flex-direction: column;
              align-items: center;
              justify-content: center;
              padding: 40px 20px;
              text-align: center;
              background: radial-gradient(ellipse at top, #1e1b4b 0%, #0f0f13 70%);
            }}
            .badge {{
              background: {ACCENT_COLOR}22;
              border: 1px solid {ACCENT_COLOR}44;
              color: {ACCENT_COLOR};
              padding: 6px 16px;
              border-radius: 100px;
              font-size: 13px;
              font-weight: 600;
              letter-spacing: 0.05em;
              text-transform: uppercase;
              margin-bottom: 24px;
            }}
            h1 {{
              font-size: clamp(2rem, 5vw, 3.5rem);
              font-weight: 800;
              line-height: 1.15;
              max-width: 820px;
              margin-bottom: 20px;
              background: linear-gradient(135deg, #fff 0%, {ACCENT_COLOR} 100%);
              -webkit-background-clip: text;
              -webkit-text-fill-color: transparent;
            }}
            .sub {{
              font-size: clamp(1rem, 2vw, 1.2rem);
              color: #94a3b8;
              max-width: 600px;
              margin-bottom: 40px;
            }}
            .bullets {{
              list-style: none;
              text-align: left;
              background: #1a1a2e;
              border: 1px solid #2d2d4a;
              border-radius: 16px;
              padding: 32px;
              max-width: 560px;
              width: 100%;
              margin-bottom: 40px;
            }}
            .bullet-item {{
              padding: 8px 0;
              font-size: 1rem;
              color: #e2e8f0;
              border-bottom: 1px solid #2d2d4a22;
            }}
            .bullet-item:last-child {{ border-bottom: none; }}
            .form-section {{
              width: 100%;
              max-width: 480px;
              margin-bottom: 16px;
            }}
            .form-section input[type=email] {{
              width: 100%;
              padding: 16px 20px;
              background: #1a1a2e;
              border: 1px solid #3d3d6a;
              border-radius: 12px;
              color: #f1f1f4;
              font-size: 1rem;
              margin-bottom: 12px;
              outline: none;
              transition: border-color 0.2s;
            }}
            .form-section input[type=email]:focus {{ border-color: {ACCENT_COLOR}; }}
            .cta-btn {{
              display: block;
              width: 100%;
              padding: 18px 32px;
              background: linear-gradient(135deg, {ACCENT_COLOR} 0%, #8b5cf6 100%);
              color: white;
              font-size: 1.1rem;
              font-weight: 700;
              border: none;
              border-radius: 12px;
              cursor: pointer;
              text-decoration: none;
              transition: opacity 0.2s, transform 0.1s;
            }}
            .cta-btn:hover {{ opacity: 0.9; transform: translateY(-1px); }}
            .cta-btn:active {{ transform: translateY(0); }}
            .urgency {{
              color: #f59e0b;
              font-size: 0.875rem;
              margin-top: 12px;
            }}
            .social-proof {{
              color: #64748b;
              font-size: 0.875rem;
              margin-top: 8px;
            }}
            .twin-section {{
              background: #111827;
              border-top: 1px solid #1f2937;
              padding: 80px 20px;
              text-align: center;
            }}
            .twin-section h2 {{
              font-size: clamp(1.5rem, 3vw, 2.5rem);
              font-weight: 700;
              margin-bottom: 16px;
            }}
            .twin-section p {{
              color: #94a3b8;
              max-width: 560px;
              margin: 0 auto 32px;
              font-size: 1.1rem;
            }}
            .twin-cta {{
              display: inline-block;
              padding: 16px 40px;
              background: linear-gradient(135deg, #10b981 0%, #059669 100%);
              color: white;
              font-size: 1rem;
              font-weight: 700;
              border-radius: 12px;
              text-decoration: none;
              transition: opacity 0.2s;
            }}
            .twin-cta:hover {{ opacity: 0.9; }}
            footer {{
              text-align: center;
              padding: 32px 20px;
              color: #475569;
              font-size: 0.875rem;
            }}
          </style>
        </head>
        <body>

          <section class="hero" id="email-capture">
            <div class="badge">Free Resource</div>
            <h1>{c.headline}</h1>
            <p class="sub">{c.subheadline}</p>

            <ul class="bullets">
        {bullets_html}
            </ul>

            <div class="form-section">
              <form id="signup-form" onsubmit="handleSubmit(event)">
                <input type="email" placeholder="Enter your email address" required>
                <button type="submit" class="cta-btn">{c.cta_text}</button>
              </form>
              <p class="urgency">{c.urgency_text}</p>
              <p class="social-proof">{c.social_proof}</p>
            </div>
          </section>

          <section class="twin-section">
            <h2>Ready to automate your sales calls?</h2>
            <p>
              Twin.so creates an AI version of you that qualifies leads,
              handles objections, and books calls — 24/7.
              30-day free trial, no credit card needed.
            </p>
            <a href="{AFFILIATE_LINK}" class="twin-cta" target="_blank" rel="noopener">
              Try Twin.so Free →
            </a>
            <p style="color:#475569;font-size:0.75rem;margin-top:16px;">
              Affiliate disclosure: I earn a 30% recurring commission if you subscribe.
              I use and recommend this tool personally.
            </p>
          </section>

          <footer>
            <p>© 2025 lippytm.ai — Business of Businesses | AI-Powered</p>
            <p style="margin-top:8px;">
              <a href="https://github.com/lippytm" style="color:{ACCENT_COLOR};">
                GitHub
              </a> ·
              Built with Claude AI + Cloudflare Workers
            </p>
          </footer>

          <script>
            async function handleSubmit(e) {{
              e.preventDefault();
              const email = e.target.querySelector('input[type=email]').value;
              const btn = e.target.querySelector('button');
              btn.textContent = 'Sending...';
              btn.disabled = true;
              try {{
                await fetch('https://lippytm-ai-swarms.workers.dev/lead', {{
                  method: 'POST',
                  headers: {{ 'Content-Type': 'application/json' }},
                  body: JSON.stringify({{
                    email,
                    source: 'landing_page_affiliate',
                    utm_campaign: new URLSearchParams(window.location.search).get('utm_campaign') || '',
                  }}),
                }});
                btn.textContent = '✅ Check your inbox!';
                btn.style.background = 'linear-gradient(135deg, #10b981 0%, #059669 100%)';
              }} catch (_) {{
                btn.textContent = '{c.cta_text}';
                btn.disabled = false;
              }}
            }}

            // UTM tracking
            const params = new URLSearchParams(window.location.search);
            const source = params.get('utm_source') || 'direct';
            document.querySelectorAll('a[href*="twin.so"]').forEach(a => {{
              const url = new URL(a.href);
              url.searchParams.set('utm_source', source);
              url.searchParams.set('utm_medium', 'landing_page');
              url.searchParams.set('utm_campaign', 'lippytm_affiliate');
              a.href = url.toString();
            }});
          </script>
        </body>
        </html>
        """)

    def write_to_disk(self, output_dir: str = "dist/affiliate") -> Path:
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        index_path = out / "index.html"
        index_path.write_text(self.render(), encoding="utf-8")

        # Write _headers file for Cloudflare Pages
        (out / "_headers").write_text(
            textwrap.dedent("""\
            /*
              X-Frame-Options: DENY
              X-Content-Type-Options: nosniff
              Referrer-Policy: strict-origin-when-cross-origin
              Permissions-Policy: camera=(), microphone=(), geolocation=()
            /
              Cache-Control: public, max-age=3600
            """),
            encoding="utf-8",
        )

        # Write _redirects for SPA
        (out / "_redirects").write_text("/  /index.html  200\n", encoding="utf-8")

        return index_path


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--page", default="affiliate", choices=["affiliate"])
    parser.add_argument("--output", default="dist/affiliate")
    args = parser.parse_args()

    if args.page == "affiliate":
        page = AffiliateLandingPage()
        path = page.write_to_disk(args.output)
        print(f"Landing page written to: {path}")
