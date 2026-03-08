import os
from app import demo

# Vercel needs an 'app' variable to serve
# We ensure the MCP server and UI are initialized
app = demo.launch(
    mcp_server=True,
    prevent_thread_lock=True
)
