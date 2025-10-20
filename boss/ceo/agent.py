from google.adk.agents.llm_agent import Agent
from .files_manager import files_manager_agent
from .research_manager import research_manager_agent
from .architect_manager import architect_manager_agent
from .frontend_manager import frontend_manager_agent
from .backend_manager import backend_manager_agent
from .DevOps_manager import devops_manager_agent
from .QA_manager import qa_manager_agent
from .ui_designer import ui_designer_agent
from . import prompt


# Create the root_agent instance that lives for the duration of the application
ceo_agent = Agent(
    model="gemini-2.5-flash",
    name="ceo_agent",
    description="The central coordinator of the entire AI team. It interprets the user's goal, formulates a high-level strategic plan, and delegates tasks to the appropriate department leads.",
    instruction=prompt.CEO_PROMPT,
    sub_agents=[
        files_manager_agent,
        research_manager_agent,
        architect_manager_agent,
        frontend_manager_agent,
        backend_manager_agent,
        devops_manager_agent,
        qa_manager_agent,
        ui_designer_agent,
    ],
)
