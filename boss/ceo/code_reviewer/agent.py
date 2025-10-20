from google.adk.agents.llm_agent import Agent
from . import prompt


code_reviewer_agent = Agent(
    model="gemini-2.5-flash",
    name="code_reviewer_agent",
    description="Analyzes code for quality, bugs, and adherence to standards. It provides feedback to ensure the codebase is clean and maintainable.",
    instruction=prompt.CODE_REVIEWER_PROMPT,
)
