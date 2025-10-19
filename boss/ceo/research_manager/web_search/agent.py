from google.adk.agents.llm_agent import Agent
from . import prompt
from google.adk.tools import google_search
from google.adk.tools import agent_tool

google_search_agent = Agent(
    model="gemini-2.0-flash-exp",
    name="SearchAgent",
    instruction="""
    You're a spealist in Google Search
    """,
    tools=[google_search],
)
# Create the root_agent instance that lives for the duration of the application
web_search_agent = Agent(
    model="gemini-2.5-flash",
    name="web_search_agent",
    description="A specialized agent that performs Google searches to gather up-to-date information from the internet. It acts as the primary research tool for other agents, providing them with relevant data and source links to complete their tasks.",
    instruction=prompt.WEB_SEARCH_PROMPT,
    tools=[agent_tool.AgentTool(agent=google_search_agent)],
)
