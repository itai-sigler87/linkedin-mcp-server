from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from linkedin_mcp_server.config import get_config
from linkedin_mcp_server.cli import print_claude_config
from linkedin_mcp_server.drivers.chrome import initialize_driver

app = FastAPI()

@app.post("/message")
async def message(request: Request):
    body = await request.json()
    
    query = body.get("tool_input", {}).get("query", "")
    session = body.get("session_id", "unknown")
    tool_name = body.get("tool_name", "linkedinFetcher")

    # Simulate a basic working response
    return JSONResponse({
        "text": f"(Simulated) Here's what {tool_name} found for: {query}",
        "tool_calls": [],
    })

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

def main():
    print("🔗 LinkedIn MCP Server - Retool Compatible")
    config = get_config()
    initialize_driver()
    
    if config.server.setup:
        print_claude_config()

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
