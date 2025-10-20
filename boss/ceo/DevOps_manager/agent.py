from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

from . import prompt

devops_manager_agent = Agent(
    model="gemini-2.5-flash",
    name="devops_manager_agent",
    description="Manages the infrastructure, CI/CD pipelines, and deployment processes to ensure the application runs smoothly in production.",
    instruction=prompt.DEVOPS_MANAGER_PROMPT,
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
