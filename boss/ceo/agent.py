from google.adk.agents.llm_agent import Agent
from .files_manager import files_manager_agent
from .research_manager import research_manager_agent
from . import prompt


# Create the root_agent instance that lives for the duration of the application
ceo_agent = Agent(
    model="gemini-2.5-flash",
    name="ceo_agent",
    description="The central coordinator of the entire AI team. It interprets the user's goal, formulates a high-level strategic plan, and delegates tasks to the appropriate department leads.",
    instruction=prompt.CEO_PROMPT,
    sub_agents=[files_manager_agent, research_manager_agent],
)
