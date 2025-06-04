from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_tool_calling_agent
from mcp_client.prompts import SYSTEM_PROMPT
from langchain_groq import ChatGroq
import asyncio

model = ChatGroq(model="llama3-8b-8192", temperature=0)

server_params = StdioServerParameters(
    command="python",
    args=["/Users/apple/Downloads/mix_server/main.py"]
)

async def run_agent(prompt: str):
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                print("MCP Session Initialized.")

                tools = await load_mcp_tools(session)
                print(f"Loaded Tools: {[tool.name for tool in tools]}")

                system_prompt = SYSTEM_PROMPT
                agent = create_tool_calling_agent(model, tools, system_prompt)
                print("Tool-Calling Agent Created.")

                print(f"Prompt: {prompt}")
                response = await agent.ainvoke({
                    "messages": [("user", prompt)]
                })

                return response["messages"][-1].content
    except Exception as e:
        print("Caught exception in agent:")
        import traceback
        traceback.print_exc()
        raise e

       
if __name__ == "__main__":
    print("Starting MCP Client...")
    prompt = "I want the column names in my csv"
    result = asyncio.run(run_agent(prompt))
    print("\nAgent Final Response:")
    print(result)