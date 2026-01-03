# 🌐 API vs. MCP: The Detailed Comparison

When building agentic systems, understanding the shift from **Standard APIs** to the **Model Context Protocol (MCP)** is crucial. While they share some similarities, their purpose, architecture, and "audience" are fundamentally different.

---

## 📊 High-Level Comparison Table

| Feature | Standard API (REST/GraphQL) | Model Context Protocol (MCP) |
| :--- | :--- | :--- |
| **Primary Audience** | Human Developers / Other Applications | Large Language Models (LLMs) |
| **Communication** | HTTP (GET, POST, etc.) | JSON-RPC 2.0 (over Stdio or SSE) |
| **Schema** | External (OpenAPI / Swagger) | **Internal & Self-Describing** |
| **State** | Often Stateless / Session-based | Stateful Contextual Sessions |
| **Discovery** | Manual Documentation reading | Automatic Tool/Resource Discovery |
| **Payload** | Pure Data (JSON/XML) | Context-Augmented Data (Text/Images/Prompts) |

---

## 🧠 Deep Dive: Architectural Differences

### 1. The "Audience" Shift
- **Standard API**: Designed for a human to read documentation, write code, and handle specific error codes. It is a "dumb" endpoint that expects precise input.
- **MCP**: Designed for an **Agent** to "look" at the available tools, understand what they do via natural language descriptions, and decide when to call them. 

### 2. Self-Documentation (The "Magic" of MCP)
In a standard API, if you change a parameter, you must update the Swagger UI and the developer must update their code. 
In MCP, you simply update the docstring of your Python function. The LLM immediately "sees" the new capability and starts using it without any human code changes in the middle.

### 3. Unified Context
Standard APIs give you raw data. MCP can provide:
- **Tools**: Actions the model can take.
- **Resources**: Raw data fragments the model can read.
- **Prompts**: Reusable patterns for interaction.
This creates a "unified playground" for the LLM to interact with your local environment.

---

## 🛠️ From API to MCP: Practical Conversion Example

Let's take a simple **Public Weather API** and see how we transform it from a standard script into an MCP tool.

### Scenario: A Weather Tool
We want to give an LLM the ability to fetch weather for a city.

### Phase 1: The "Old Way" (Standard API Wrapper)
Standard Python code that an LLM cannot "call" by itself unless you write a specific plugin or hardcoded logic.

```python
import requests

def get_weather(city: str):
    # Imagine this is a real API call
    base_url = f"https://api.weather.com/v1/{city}"
    response = requests.get(base_url)
    return response.json()
```

### Phase 2: The "New Way" (MCP Server)
By wrapping the logic in an MCP Server, the LLM (like Claude) can now **autonomously** decide to fetch weather when a user asks: *"Is it raining in London?"*

---

## 🚀 How to Convert: The Step-by-Step Logic

1.  **Define the Server**: Create a name for your capability (e.g., "weather-service").
2.  **Define the Tool**: Use the `@mcp.tool()` decorator.
3.  **Self-Descibe**: Write clear docstrings. The LLM uses these to understand "why" it should use this tool.
4.  **Handle IO**: MCP handles the JSON-RPC wrapping automatically.

### 🔗 Code Example: `api_to_mcp_conversion.py`
*(Check the companion file in this folder for the full implementation)*

```python
from mcp.server.fastmcp import FastMCP
import requests

# 1. Initialize FastMCP
mcp = FastMCP("WeatherService")

# 2. Convert the API Logic into a Tool
@mcp.tool()
def fetch_weather(city: str) -> str:
    """
    Fetches real-time weather information for a specified city.
    Use this when the user asks about temperature or conditions.
    """
    # Standard API Logic remains inside!
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    return f"Error: Could not find weather for {city}"

# The MCP Server will now expose 'fetch_weather' as a tool 
# that an LLM can discover and use instantly.
```

---

## 🎯 Key Takeaway
- **APIs** are the pipes.
- **MCP** is the interface that lets the LLM "see" and "operate" those pipes.

To convert an API, you don't rewrite the logic; you **wrap** it in an MCP decorator and provide clear natural language descriptions so the model knows what the logic is for.
