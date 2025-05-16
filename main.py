"""
LinkedIn MCP Server - A Model Context Protocol server for LinkedIn integration.
"""

import sys
import logging
from typing import NoReturn

from linkedin_mcp_server.config import get_config
from linkedin_mcp_server.cli import print_claude_config
from linkedin_mcp_server.drivers.chrome import initialize_driver
from linkedin_mcp_server.server import create_mcp_server, shutdown_handler


def main() -> None:
    print("🔗 LinkedIn MCP Server 🔗")
    print("=" * 40)

    config = get_config()

    log_level = logging.DEBUG if config.server.debug else logging.ERROR
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    logger = logging.getLogger("linkedin_mcp_server")
    logger.debug(f"Server configuration: {config}")

    initialize_driver()

    # Force SSE as default for non-interactive production environments
    transport = config.server.transport or "sse"

    if config.server.setup:
        print_claude_config()

    mcp = create_mcp_server()
    print(f"\n🚀 Running LinkedIn MCP server ({transport.upper()} mode)...")
    mcp.run(transport=transport)


def exit_gracefully(exit_code: int = 0) -> NoReturn:
    print("\n👋 Shutting down LinkedIn MCP server...")
    shutdown_handler()
    sys.exit(exit_code)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit_gracefully(0)
    except Exception as e:
        print(f"❌ Error running MCP server: {e}")
        exit_gracefully(1)
