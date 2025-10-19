from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
from . import prompt


# Create the root_agent instance that lives for the duration of the application
files_manager_agent = Agent(
    model="gemini-2.5-flash",
    name="files_manager_agent",
    description="Performs atomic file operations: reading, writing, updating, and deleting files.",
    instruction=prompt.FILES_MANAGER_PROMPT,
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
