from google.adk.agents.llm_agent import Agent
from . import prompt


architect_manager_agent = Agent(
    model="gemini-2.5-flash",
    name="architect_manager_agent",
    description="This agent acts as the high-level planner. It receives the main project goal, analyzes it, and then designs the entire software architecture, including the technology stack, project structure, and data models.",
    instruction=prompt.ARCHITECT_MANAGER_PROMPT,
)
