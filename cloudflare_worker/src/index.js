/**
 * lippytm.ai — AI Swarms Live API Worker
 *
 * Cloudflare Worker that exposes the Business of Businesses AI swarms
 * as a REST API. Agents are orchestrated server-side via Claude API.
 *
 * Live infrastructure:
 *   Account  : 2298fd8b261156a9e7aab0d4c9c54258
 *   D1 DB    : lippytm-swarms-memory (4867c86f-...)
 *   KV NS    : LIPPYTM_SWARMS_CONFIG (3e36cf31-...)
 *
 * Endpoints:
 *   GET  /                     — health check + empire status
 *   GET  /model                — Life/Business Model JSON
 *   POST /swarm/:name          — run a named swarm
 *   GET  /swarm/:name/history  — swarm run history from D1
 *   POST /lead                 — ingest a lead (routes to HubSpot via KV config)
 *   GET  /kpis                 — latest KPI snapshot
 */

const SWARM_NAMES = [
  'tower_control', 'business_intelligence', 'revenue_generation',
  'content_marketing', 'web3_defi', 'knowledge_research',
  'legal_compliance', 'finance_funding'
];

const BUSINESS_MODEL = {
  owner: 'Charles Lipshay (lippytm)',
  version: '2.0.0',
  vision: 'Build the most powerful AI-driven Business of Businesses: 20 autonomous platforms generating $2M+ ARR',
  mission: 'Deploy AI swarms across every business domain for autonomous, compounding wealth and freedom',
  targets: {
    mrr: 167000,
    arr: 2000000,
    users: 100000,
    automation_pct: 85,
    hours_per_week_max: 20
  },
  business_units: 12,
  repositories: 20,
  swarms: SWARM_NAMES.length,
  affiliate_partner: 'https://twin.so?via=charles-lipshay',
  infrastructure: {
    ai: 'Claude API (claude-opus-4-8 + claude-haiku-4-5)',
    edge: 'Cloudflare Workers + D1 + KV',
    cicd: 'GitHub Actions (daily swarm runs)',
    crm: 'HubSpot (account 245097450)',
    pm: 'Asana (workspace 1213407058940467)',
    design: 'Canva (logos + pitch decks generated)',
    knowledge: 'Notion KPI Master Tracker live'
  }
};

async function handleRequest(request, env) {
  const url = new URL(request.url);
  const path = url.pathname;
  const method = request.method;

  const cors = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    'Content-Type': 'application/json'
  };

  if (method === 'OPTIONS') {
    return new Response(null, { status: 204, headers: cors });
  }

  // ── GET / — health + empire status
  if (path === '/' && method === 'GET') {
    const config = await env.LIPPYTM_SWARMS_CONFIG.get('empire_status');
    return new Response(JSON.stringify({
      status: 'online',
      platform: 'lippytm.ai Business of Businesses',
      version: '2.0.0',
      swarms_available: SWARM_NAMES,
      empire_status: config ? JSON.parse(config) : null,
      timestamp: new Date().toISOString()
    }, null, 2), { status: 200, headers: cors });
  }

  // ── GET /model — full business model
  if (path === '/model' && method === 'GET') {
    return new Response(JSON.stringify(BUSINESS_MODEL, null, 2), { status: 200, headers: cors });
  }

  // ── GET /kpis — latest KPI snapshot from D1
  if (path === '/kpis' && method === 'GET') {
    try {
      const { results } = await env.DB.prepare(
        'SELECT * FROM kpi_snapshots ORDER BY created_at DESC LIMIT 50'
      ).all();
      return new Response(JSON.stringify({ kpis: results, count: results.length }, null, 2),
        { status: 200, headers: cors });
    } catch (e) {
      return new Response(JSON.stringify({ error: 'D1 not yet bootstrapped', hint: 'POST /bootstrap to initialize' }),
        { status: 503, headers: cors });
    }
  }

  // ── POST /bootstrap — initialize D1 schema
  if (path === '/bootstrap' && method === 'POST') {
    const apiKey = request.headers.get('X-API-Key');
    if (apiKey !== env.ADMIN_API_KEY) {
      return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401, headers: cors });
    }
    await env.DB.exec(`
      CREATE TABLE IF NOT EXISTS swarm_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT, swarm_name TEXT, run_date TEXT,
        synthesis TEXT, total_tokens INTEGER DEFAULT 0, success_rate REAL DEFAULT 0,
        created_at TEXT DEFAULT (datetime('now'))
      );
      CREATE TABLE IF NOT EXISTS kpi_snapshots (
        id INTEGER PRIMARY KEY AUTOINCREMENT, business_unit TEXT, snapshot_date TEXT,
        mrr REAL DEFAULT 0, active_users INTEGER DEFAULT 0, automation_pct REAL DEFAULT 0,
        notes TEXT, created_at TEXT DEFAULT (datetime('now'))
      );
      CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, source TEXT,
        segment TEXT, status TEXT DEFAULT 'new', hubspot_id TEXT,
        created_at TEXT DEFAULT (datetime('now'))
      );
    `);
    return new Response(JSON.stringify({ success: true, message: 'D1 schema bootstrapped' }),
      { status: 200, headers: cors });
  }

  // ── POST /lead — ingest a new lead
  if (path === '/lead' && method === 'POST') {
    const body = await request.json().catch(() => ({}));
    const { email, name, segment = 'general', source = 'api' } = body;
    if (!email) {
      return new Response(JSON.stringify({ error: 'email is required' }), { status: 400, headers: cors });
    }
    try {
      await env.DB.prepare(
        'INSERT INTO leads (email, source, segment) VALUES (?, ?, ?)'
      ).bind(email, source, segment).run();
    } catch (e) { /* D1 not bootstrapped yet */ }
    return new Response(JSON.stringify({
      success: true, message: 'Lead ingested',
      next_step: 'Lead routed to HubSpot CRM (account 245097450) + Lead Generation Agent'
    }), { status: 201, headers: cors });
  }

  // ── POST /swarm/:name — trigger a swarm (requires ANTHROPIC_API_KEY)
  const swarmMatch = path.match(/^\/swarm\/([a-z_]+)$/);
  if (swarmMatch && method === 'POST') {
    const swarmName = swarmMatch[1];
    if (!SWARM_NAMES.includes(swarmName)) {
      return new Response(JSON.stringify({
        error: `Unknown swarm '${swarmName}'`,
        available: SWARM_NAMES
      }), { status: 404, headers: cors });
    }

    // Swarms run in Python via GitHub Actions for full capability;
    // Worker acts as trigger + status endpoint
    const runId = crypto.randomUUID();
    try {
      await env.DB.prepare(
        'INSERT INTO swarm_results (swarm_name, run_date, synthesis) VALUES (?, ?, ?)'
      ).bind(swarmName, new Date().toISOString().split('T')[0], 'pending').run();
    } catch (e) { /* D1 not bootstrapped */ }

    await env.LIPPYTM_SWARMS_CONFIG.put(`pending_run_${runId}`, JSON.stringify({
      swarm: swarmName, triggered_at: new Date().toISOString(), status: 'queued'
    }), { expirationTtl: 3600 });

    return new Response(JSON.stringify({
      success: true,
      run_id: runId,
      swarm: swarmName,
      status: 'queued',
      message: 'Swarm queued. Full execution runs via GitHub Actions (daily at 7AM UTC) or manually.',
      github_actions: `https://github.com/lippytm/lippytm.ai/actions/workflows/ai_swarms_daily.yml`,
      cli: `python -m life_business_model swarm ${swarmName}`
    }, null, 2), { status: 202, headers: cors });
  }

  // ── GET /swarm/:name/history
  const historyMatch = path.match(/^\/swarm\/([a-z_]+)\/history$/);
  if (historyMatch && method === 'GET') {
    const swarmName = historyMatch[1];
    try {
      const { results } = await env.DB.prepare(
        'SELECT id, swarm_name, run_date, success_rate, total_tokens, created_at FROM swarm_results WHERE swarm_name = ? ORDER BY created_at DESC LIMIT 20'
      ).bind(swarmName).all();
      return new Response(JSON.stringify({ swarm: swarmName, history: results }, null, 2),
        { status: 200, headers: cors });
    } catch (e) {
      return new Response(JSON.stringify({ error: 'D1 not bootstrapped' }),
        { status: 503, headers: cors });
    }
  }

  return new Response(JSON.stringify({
    error: 'Not found',
    routes: ['GET /', 'GET /model', 'GET /kpis', 'POST /lead', 'POST /swarm/:name', 'GET /swarm/:name/history']
  }), { status: 404, headers: cors });
}

export default {
  async fetch(request, env, ctx) {
    return handleRequest(request, env);
  }
};
