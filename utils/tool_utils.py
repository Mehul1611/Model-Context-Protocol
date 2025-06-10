from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from constant import SERVER_PATH
import asyncio

server_params = StdioServerParameters(
    command="python",
    args=[SERVER_PATH]
)

async def get_tool_names():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            return [tool.name for tool in tools]
