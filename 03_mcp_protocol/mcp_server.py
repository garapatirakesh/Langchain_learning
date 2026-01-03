from mcp.server.fastmcp import FastMCP
import yfinance as yf
import logging
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables (API Keys)
load_dotenv()

# Configure logging
logging.basicConfig(
    filename="mcp_server.log",
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("financial-helper")

# Initialize OpenAI Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Create the FastMCP instance
app = FastMCP("financial-helper")

# --- 1. TOOLS ---
@app.tool()
def get_stock_price(symbol: str) -> str:
    """
    Get the current stock price for a given ticker symbol using Yahoo Finance.
    """
    logger.info(f"Fetching stock price for: {symbol}")
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.fast_info
        
        if 'last_price' in info:
            price = info['last_price']
            currency = info.get('currency', 'USD')
            return f"The current stock price for {symbol.upper()} is {price:.2f} {currency}."
        else:
            hist = ticker.history(period="1d")
            if not hist.empty:
                price = hist['Close'].iloc[-1]
                return f"The current stock price for {symbol.upper()} is {price:.2f} USD."
            else:
                return f"Could not find stock data for symbol: {symbol}"
                
    except Exception as e:
        logger.error(f"Error fetching stock price: {str(e)}")
        return f"Error fetching stock price for {symbol}: {str(e)}"

# --- 2. RESOURCES (Static) ---
@app.resource("financial://market-summary")
def get_market_summary() -> str:
    """Returns a static market summary."""
    return "Market is currently bullish with focus on AI and semi-conductors."

# --- 3. RESOURCE TEMPLATES (Dynamic with AI) ---
@app.resource("financial://ticker/{symbol}/notes")
def get_ticker_notes(symbol: str) -> str:
    """
    Generates AI-powered analyst notes for a specific ticker symbol.
    This demonstrates how an MCP server can use another LLM to provide context.
    """
    logger.info(f"Generating AI notes for: {symbol}")
    try:
        # First, try to get some basic info to feed the LLM
        ticker = yf.Ticker(symbol)
        info = ticker.info
        summary = info.get('longBusinessSummary', 'No summary available.')
        
        # Use OpenAI to generate analyst notes
        response = client.chat.completions.create(
            model="gpt-4o-mini", # Using a fast model for resource generation
            messages=[
                {"role": "system", "content": "You are a professional financial analyst."},
                {"role": "user", "content": f"Based on this business summary for {symbol}: {summary[:500]}... \n\nProvide 3 bullet point 'Analyst Notes' regarding their market position and potential risks."}
            ]
        )
        ai_notes = response.choices[0].message.content
        return f"AI-Generated Analyst Notes for {symbol.upper()}:\n\n{ai_notes}"
        
    except Exception as e:
        logger.error(f"Error generating AI notes: {str(e)}")
        # Fallback to dummy notes if AI fails or key is missing
        return f"Analyst notes for {symbol.upper()}: (Fallback) This ticker shows strong growth in its sector despite market volatility."

# --- 4. PROMPTS ---
@app.prompt()
def analyze_stock(symbol: str) -> str:
    """Creates a prompt template for analyzing a stock."""
    return f"Please provide a detailed fundamental analysis for the stock ticker: {symbol}. Consider its P/E ratio, revenue growth, and debt-to-equity ratio."

if __name__ == "__main__":
    logger.info("Starting Financial Helper MCP Server with OpenAI...")
    app.run()