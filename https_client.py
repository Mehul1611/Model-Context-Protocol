from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from mcp_client.prompts import SYSTEM_PROMPT
from constant import MODEL_NAME, SERVER_PATH
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
import traceback
import asyncio

model = ChatGroq(model= MODEL_NAME, temperature=0)

# server_params = StdioServerParameters(
#     command="python",
#     args=[SERVER_PATH]
# )

async def run_agent(prompt: str):
    try:
        client = MultiServerMCPClient(
            {
                
                "new_client": {
                    # Ensure your start your weather server on port 8000
                    "url": "http://localhost:8000/mcp/",
                    "transport": "streamable_http",
                }
            }
        )
        tools = await client.get_tools()

        agent = create_react_agent(model, tools, prompt=SYSTEM_PROMPT)
        print("Tool-Calling Agent Created.")

        response = await agent.ainvoke({
            "messages": [("user", prompt)]
        })

        return response["messages"][-1].content
    except Exception as e:
        print("Caught exception in agent:")
        traceback.print_exc()
        raise e

    
if __name__ == "__main__":
    print("Starting MCP Client...")
    prompt = "Which tool you have access to"
    result = asyncio.run(run_agent(prompt))
    print("\nAgent Final Response:")
    print(result)