# Deep Dive into MCP Servers

## What is an MCP Server?
An **MCP (Model Context Protocol) Server** is a bridge between an LLM (like Claude) and your local or remote data. It exposes three main capabilities:

1.  **Tools**: Executable functions (e.g., `calculate_interest`, `fetch_weather`).
2.  **Resources**: Data that can be read (e.g., `financial://notes`, `file:///logs.txt`).
3.  **Prompts**: Pre-defined templates for interaction.

---

## 🆚 API vs. MCP (New)
If you are wondering how MCP differs from a standard REST API, see our detailed guide:
👉 **[API_VS_MCP.md](./API_VS_MCP.md)**

---

## How to Run Your Server

### 1. The Python Script
We have updated `mcp_server.py` to use **`yfinance`** for real-time stock data.
To run it, make sure you have the dependency installed:
```bash
pip install yfinance
```

The script defines a real-time tool:
*   **Tool**: `get_stock_price(symbol)` - Fetches the live price from Yahoo Finance.

**DO NOT** run this script manually in the terminal hoping to see output! It expects JSON-RPC messages from a client. If you run it, it will just sit there waiting for input.

### 2. Configuring the Client (Claude Desktop)
To use this server, you must tell Claude Desktop where to find it.

1.  Open your Claude Desktop config file:
    *   **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
    *   **Mac**: `~/Library/Application Support/Claude/claude_desktop_config.json`

2.  Add your server to the configuration:
    ```json
    {
      "mcpServers": {
        "financial-helper": {
          "command": "python",
          "args": ["c:/Users/Rakesh/vscode_projects/learning/mcp_server.py"]
        }
      }
    }
    ```
    *(Make sure to use the absolute path to your python executable if `python` isn't in the global path, e.g., `c:/Users/Rakesh/vscode_projects/learning/.venv/Scripts/python.exe`)*

3.  **Restart Claude Desktop**. You should see a plug icon indicating the server is connected.

## How to Debug MCP Servers

Debugging is tricky because `print()` statements will corrupt the JSON-RPC communication line.

### Method 1: Logging to File or Stderr
In the `mcp_server.py` I created for you, I added this logging configuration:
```python
logging.basicConfig(
    filename="mcp_server.log",
    level=logging.DEBUG
)
```
This sends all logs to a file. You can `tail -f mcp_server.log` (or open it in VS Code) to see what your server is doing while Claude interacts with it.

Alternatively, you can log to `sys.stderr`, which MCP clients usually ignore or capture separately without breaking the protocol.

### Method 2: The MCP Inspector
The MCP team provides a web-based inspector to test your server without needing the full Claude Desktop app.
1.  Install the inspector: `npx @modelcontextprotocol/inspector`

2.  Run your server through the inspector:
    ```powershell
    npx @modelcontextprotocol/inspector python mcp_server.py
    ```
3.  This will open a web interface where you can:
    *   See the list of tools and resources.
    *   Manually call tools and see the JSON inputs/outputs.
    *   View the raw protocol logs.

### Method 3: Smithery / MCP CLI
There are CLI tools emerging. The `mcp` python package itself (if updated) or community tools often help validates servers.

## Transports: Stdio vs SSE
- **Stdio (Standard IO)**: Used for local processes (like we are doing). The client spawns the server process and talks via pipes.
- **SSE (Server-Sent Events)**: Used for remote servers. The server runs as a web server (e.g., using FastAPI/Starlette) and exposes an HTTP endpoint. The client connects via HTTP.

## Next Steps for Teaching
1.  **Show the Code**: Walk students through the decorators `@mcp.tool()` and `@mcp.resource()`.
2.  **Show the Config**: Explain why we need absolute paths.
3.  **Show the Logs**: Trigger a tool in Claude, then flip to VS Code to show the `mcp_server.log` updating in real-time.
