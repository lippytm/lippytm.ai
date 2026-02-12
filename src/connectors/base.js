/**
 * Base Connector class for all platform connectors
 */
export class BaseConnector {
  constructor(name) {
    this.name = name;
    this.connected = false;
  }

  /**
   * Connect to the platform
   */
  async connect() {
    console.log(`Connecting to ${this.name}...`);
    // Override in subclass
    this.connected = true;
  }

  /**
   * Check if connector is connected
   */
  isConnected() {
    return this.connected;
  }

  /**
   * Disconnect from the platform
   */
  async disconnect() {
    console.log(`Disconnecting from ${this.name}...`);
    this.connected = false;
  }
}
