import streamlit as st
from mcp_client.client import run_agent
import asyncio
import traceback
import nest_asyncio

nest_asyncio.apply()

try:
    st.set_page_config(page_title="MCP Client", layout="centered")
    st.title("MCP Agent Client")
    st.write("Ask a question powered by LangGraph + MCP tools.")

    user_input = st.text_input("Enter your query:")

    if st.button("Run Agent"):
        if user_input:
            with st.spinner("Running agent..."):
                try:
                    result = asyncio.run(run_agent(user_input))
                    st.success("Agent responded:")
                    st.write(result)
                except Exception as e:
                    st.error(f"An error occurred:\n\n{e}")

except Exception as e:
    st.error(f"An error occurred:\n\n{e}")
    st.text("Details:")
    st.text(traceback.format_exc())