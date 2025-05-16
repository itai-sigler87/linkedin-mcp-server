"""
LinkedIn MCP Server - Fully compatible with Retool via FastAPI
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from mcp.server.fastmcp import FastMCP
from linkedin_mcp_server.config import get_config
from linkedin_mcp_server.cli import print_claude_config
from linkedin_mcp_server.drivers.chrome import initialize_driver

# Create a FastAPI app
app = FastAPI()

# Create an MCP server
mcp = FastMCP()

# Register the MCP message handler as a POST /message endpoint
@app.post("/message")
async def message(request: Request):
    body = await request.json()
    # Let the MCP server process the tool request
    response = await mcp.handle_message(body)
    return JSONResponse(response)

# Optional: health check for Render
@app.get("/healthz")
def healthz():
    return {"status": "ok"}

def main():
    print("🔗 LinkedIn MCP Server 🔗")
    print("=" * 40)

    config = get_config()
    initialize_driver()

    if config.server.setup:
        print_claude_config()

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
