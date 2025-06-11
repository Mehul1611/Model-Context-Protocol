from mcp_server.server import mcp
import yfinance as yf
# import tools.parquet_tools
# import tools.stock_price_tool
# Entry point to run the server

@mcp.tool()
async def get_stock_price(symbol: str) -> float:
    """
    Retrieve the current stock price for the given ticker symbol.
    Returns the latest closing price as a float.
    """
    try:
        ticker = yf.Ticker(symbol)
        # Get today's historical data; may return empty if market is closed or symbol is invalid.
        data = ticker.history(period="1d")
        if not data.empty:
            # Use the last closing price from today's data
            price = data['Close'].iloc[-1]
            return float(price)
        else:
            # As a fallback, try using the regular market price from the ticker info
            info = ticker.info
            price = info.get("regularMarketPrice", None)
            if price is not None:
                return float(price)
            else:
                return -1.0  # Indicate failure
    except Exception:
        # Return -1.0 to indicate an error occurred when fetching the stock price
        return -1.0
if __name__ == "__main__":
    
    mcp.run(transport="streamable-http")


# Constants
# NWS_API_BASE = "https://api.weather.gov"
# USER_AGENT = "weather-app/1.0"