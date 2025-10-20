from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

from . import prompt


# Create the root_agent instance that lives for the duration of the application
backend_manager_agent = Agent(
    model="gemini-2.5-flash",
    name="backend_manager_agent",
    description="Manages all server-side development, including creating APIs, handling business logic, and managing database interactions.",
    instruction=prompt.BACKEND_MANAGER_PROMPT,
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
