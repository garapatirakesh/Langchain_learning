"""
DEMO: Converting a standard API integration into an MCP Server Tool.

This script demonstrates two approaches:
1. Standard API consumption (Script based)
2. MCP Tool consumption (Agent centric)
"""

import requests
import json
import logging
from mcp.server.fastmcp import FastMCP

# Setup logging to see what's happening without breaking the MCP pipe
logging.basicConfig(level=logging.INFO, filename="api_conversion.log")

# ==========================================
# APPROACH 1: Standard API (The "Old Way")
# ==========================================
def get_crypto_price_api(coin_id="bitcoin"):
    """
    Standard function to call a public API.
    A human developer must call this function in code.
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        return f"The current price of {coin_id} is ${data[coin_id]['usd']}"
    except Exception as e:
        return f"Error fetching price: {str(e)}"

# Example manual usage:
# print(get_crypto_price_api("ethereum"))


# ==========================================
# APPROACH 2: MCP Tool (The "New Way")
# ==========================================

# 1. Create the MCP Server instance
# FastMCP manages all the JSON-RPC boilerplate for us.
mcp = FastMCP("CryptoPriceHunter")

@mcp.tool()
def check_crypto_price(coin_name: str) -> str:
    """
    Fetches the live market price of a cryptocurrency in USD.
    Args:
        coin_name: The name of the coin (e.g., 'bitcoin', 'ethereum', 'solana')
    """
    # We simply re-use the existing API logic!
    logging.info(f"LLM is requesting price for: {coin_name}")
    
    # Simple normalization
    coin_id = coin_name.lower().strip()
    
    # Re-using the logic from Approach 1
    result = get_crypto_price_api(coin_id)
    
    return result

# ==========================================
# SUMMARY OF TRANSFORMATION
# ==========================================
# To convert the API, we did 3 things:
# 1. Wrapped the function in @mcp.tool().
# 2. Provided a clear docstring (essential for the LLM).
# 3. Made the function return a string/text that the LLM can interpret.

if __name__ == "__main__":
    # Running 'mcp run' or integrating with Claude Desktop 
    # will start the server. This script on its own won't do 
    # anything unless called by an MCP client.
    mcp.run()
