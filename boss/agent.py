from google.adk.agents.llm_agent import Agent
from . import prompt
from .ceo import ceo_agent


# Create the root_agent instance that lives for the duration of the application
root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="The primary entry point for all user requests. It receives the initial high-level goal and delegates it to the CEO to begin the workflow.",
    instruction=prompt.BOSS_PROMPT,
    sub_agents=[ceo_agent],
)
