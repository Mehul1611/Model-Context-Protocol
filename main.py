from mcp_server.server import mcp
import tools.csv_tools
import tools.parquet_tools
import tools.stock_price_tool
# Entry point to run the server
if __name__ == "__main__":
    mcp.run()


# Constants
# NWS_API_BASE = "https://api.weather.gov"
# USER_AGENT = "weather-app/1.0"