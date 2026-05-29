#!/usr/bin/env bash
set -euo pipefail

# =============================================================================
# LIPPYTM.AI — ONE-SHOT ACTIVATION SCRIPT
# Activates all revenue systems: Cloudflare, GitHub, Affiliate Funnel
# Usage: bash scripts/activate.sh
# =============================================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log()  { echo -e "${BLUE}[INFO]${NC} $1"; }
ok()   { echo -e "${GREEN}[OK]${NC}   $1"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
err()  { echo -e "${RED}[ERR]${NC}  $1"; exit 1; }

echo ""
echo "====================================================="
echo "  🚀 LIPPYTM.AI REVENUE ACTIVATION"
echo "  Business of Businesses — AI Swarms Stack"
echo "====================================================="
echo ""

# --- PREFLIGHT ---
log "Checking prerequisites..."
command -v python3 >/dev/null 2>&1 || err "Python 3 required. Install at python.org"
command -v node >/dev/null 2>&1   || err "Node.js required. Install at nodejs.org"
command -v git >/dev/null 2>&1    || err "Git required."

[[ -z "${ANTHROPIC_API_KEY:-}" ]] && err "Set ANTHROPIC_API_KEY first: export ANTHROPIC_API_KEY=sk-ant-..."
ok "Prerequisites met"

# --- PYTHON DEPS ---
log "Installing Python dependencies..."
pip install anthropic requests python-dotenv --quiet
ok "Python deps installed"

# --- TEST CLAUDE API ---
log "Testing Claude API connection..."
python3 -c "
import anthropic
client = anthropic.Anthropic()
msg = client.messages.create(
    model='claude-haiku-4-5-20251001',
    max_tokens=50,
    messages=[{'role':'user','content':'Say OK'}]
)
print('Claude API:', msg.content[0].text)
" || err "Claude API failed. Check ANTHROPIC_API_KEY"
ok "Claude API connected"

# --- CLOUDFLARE WORKER ---
if command -v npx >/dev/null 2>&1; then
    log "Deploying Cloudflare Worker..."
    if [[ -d "cloudflare_worker" ]]; then
        cd cloudflare_worker
        npm install --silent
        npx wrangler deploy --quiet && ok "Cloudflare Worker deployed" || warn "Worker deploy failed — run manually: cd cloudflare_worker && npx wrangler deploy"
        # Bootstrap D1 schema
        sleep 2
        curl -s -X POST https://lippytm-ai-swarms.workers.dev/bootstrap > /dev/null && ok "D1 schema bootstrapped" || warn "Bootstrap failed — run: curl -X POST https://lippytm-ai-swarms.workers.dev/bootstrap"
        cd ..
    else
        warn "cloudflare_worker/ not found — skipping Worker deploy"
    fi
else
    warn "npx not found — skipping Cloudflare Worker deploy"
fi

# --- GENERATE LANDING PAGE ---
log "Generating affiliate landing page..."
python3 -c "
from life_business_model.revenue.landing_pages import AffiliateLandingPage
page = AffiliateLandingPage()
page.write_to_disk('dist/affiliate')
print('Landing page written to dist/affiliate/')
" && ok "Landing page generated → dist/affiliate/" || warn "Landing page generation failed"

# --- RUN FIRST SWARM ---
log "Running Tower Control swarm (first activation)..."
python3 -m life_business_model swarm tower_control \
    --output reports/activation-$(date +%Y-%m-%d).json \
    && ok "First swarm report saved" \
    || warn "Swarm run failed — check ANTHROPIC_API_KEY and dependencies"

# --- SUMMARY ---
echo ""
echo "====================================================="
echo -e "  ${GREEN}ACTIVATION COMPLETE${NC}"
echo "====================================================="
echo ""
echo "  Next steps:"
echo "  1. Add ANTHROPIC_API_KEY to GitHub Secrets:"
echo "     https://github.com/lippytm/lippytm.ai/settings/secrets/actions"
echo ""
echo "  2. Deploy landing page to Cloudflare Pages:"
echo "     npx wrangler pages deploy dist/affiliate --project-name lippytm-affiliate"
echo ""
echo "  3. Post affiliate content on LinkedIn & Twitter/X"
echo "     (see ACTIVATE.md for exact copy)"
echo ""
echo "  4. Verify daily swarms trigger at 7AM UTC:"
echo "     https://github.com/lippytm/lippytm.ai/actions"
echo ""
echo "  Affiliate link: https://twin.so?via=charles-lipshay"
echo "  API: https://lippytm-ai-swarms.workers.dev"
echo ""
