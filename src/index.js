/**
 * lippytm.ai - AI Web3AI Connection Hub
 * Main entry point for the connection hub
 */

import { GitHubConnector } from './connectors/github.js';
import { GitLabConnector } from './connectors/gitlab.js';
import { GistConnector } from './connectors/gist.js';

class LippyTMHub {
  constructor() {
    this.connectors = {
      github: new GitHubConnector(),
      gitlab: new GitLabConnector(),
      gist: new GistConnector()
    };
  }

  /**
   * Initialize all connectors
   */
  async initialize() {
    console.log('🚀 Initializing lippytm.ai Connection Hub...');
    
    for (const [name, connector] of Object.entries(this.connectors)) {
      try {
        await connector.connect();
        console.log(`✓ ${name} connector initialized`);
      } catch (error) {
        console.error(`✗ Failed to initialize ${name} connector:`, error.message);
      }
    }
    
    console.log('✨ Hub ready for creative development!');
  }

  /**
   * Get status of all connectors
   */
  getStatus() {
    const status = {};
    for (const [name, connector] of Object.entries(this.connectors)) {
      status[name] = connector.isConnected();
    }
    return status;
  }
}

// Initialize hub if running directly
if (import.meta.url === `file://${process.argv[1]}`) {
  const hub = new LippyTMHub();
  hub.initialize().catch(console.error);
}

export default LippyTMHub;
