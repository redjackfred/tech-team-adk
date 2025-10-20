from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

from . import prompt

frontend_manager_agent = Agent(
    model="gemini-2.5-flash",
    name="frontend_manager_agent",
    description="Oversees the development of the user interface (UI) and user experience (UX), managing all client-side code and components.",
    instruction=prompt.FRONTEND_MANAGER_PROMPT,
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
