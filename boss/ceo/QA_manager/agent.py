from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

from . import prompt

qa_manager_agent = Agent(
    model="gemini-2.5-flash",
    name="qa_manager_agent",
    description="Ensures software quality by designing test plans, overseeing the creation of automated tests, and verifying that the application meets all requirements.",
    instruction=prompt.QA_MANAGER_PROMPT,
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="npx",
                    args=[
                        "-y",
                        "@modelcontextprotocol/server-filesystem",
                        "~/",
                    ],
                ),
            ),
        )
    ],
)
