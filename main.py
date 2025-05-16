"""
LinkedIn MCP Server - Retool-compatible MCP server with internal FastAPI app
"""

from mcp.server.fastmcp import FastMCP
from linkedin_mcp_server.config import get_config
from linkedin_mcp_server.cli import print_claude_config
from linkedin_mcp_server.drivers.chrome import initialize_driver

def main():
    print("🔗 LinkedIn MCP Server 🔗")
    print("=" * 40)

    config = get_config()
    initialize_driver()

    if config.server.setup:
        print_claude_config()

    mcp = FastMCP()
    mcp.run(transport="sse")  # Don't pass app=

if __name__ == "__main__":
    main()
