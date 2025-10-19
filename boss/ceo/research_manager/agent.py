from google.adk.agents.llm_agent import Agent
from .web_search import web_search_agent
from . import prompt


# Create the root_agent instance that lives for the duration of the application
research_manager_agent = Agent(
    model="gemini-2.5-flash",
    name="research_manager_agent",
    description="Gathers all necessary information, from web search to documentation analysis, to support the development team",
    instruction=prompt.RESEARCH_MANAGER_PROMPT,
    sub_agents=[web_search_agent],
)
