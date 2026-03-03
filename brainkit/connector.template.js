/**
 * AI BrainKit Connector Template
 *
 * Copy this file to your repository's src/connectors/ directory and
 * customize it for your specific platform or service integration.
 *
 * Part of the lippytm AI BrainKit — https://github.com/lippytm/lippytm.ai
 */

/**
 * Base connector interface. All platform connectors extend this class.
 */
export class BaseConnector {
  /**
   * @param {string} name - Human-readable connector name
   * @param {object} [config={}] - Connector-specific configuration
   */
  constructor(name, config = {}) {
    this.name = name;
    this.config = config;
    this.connected = false;
  }

  /** Establish connection to the platform. Override in subclass. */
  async connect() {
    throw new Error(`${this.name}: connect() not implemented`);
  }

  /** Disconnect from the platform. Override in subclass. */
  async disconnect() {
    this.connected = false;
  }

  /** @returns {{ name: string, connected: boolean }} Current connector status */
  status() {
    return { name: this.name, connected: this.connected };
  }
}

/**
 * Example platform connector — replace with your platform's API logic.
 *
 * @example
 * const connector = new MyPlatformConnector({ apiKey: process.env.MY_API_KEY });
 * await connector.connect();
 * const data = await connector.fetchData();
 */
export class MyPlatformConnector extends BaseConnector {
  constructor(config = {}) {
    super('MyPlatform', config);
  }

  async connect() {
    // TODO: Initialize your platform's API client here.
    // Wrap initialization in try/catch and surface a clear error on failure:
    //
    //   try {
    //     this.client = new PlatformSDK({ apiKey: this.config.apiKey });
    //     await this.client.authenticate();
    //     this.connected = true;
    //   } catch (err) {
    //     throw new Error(`${this.name}: failed to connect — ${err.message}`);
    //   }
    this.connected = true;
    return this;
  }

  /**
   * Fetch data from the platform.
   * @returns {Promise<Array>} List of items
   */
  async fetchData() {
    if (!this.connected) {
      throw new Error(`${this.name}: call connect() before fetchData()`);
    }
    // TODO: Replace with real API call
    return [];
  }
}
