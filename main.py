"""
LinkedIn MCP Server - Retool-compatible MCP server with /sse support
"""

from fastapi import FastAPI
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

    # Create a FastAPI app and let MCP populate it internally
    app = FastAPI()
    mcp.run(app=app, transport="sse")

if __name__ == "__main__":
    main()
