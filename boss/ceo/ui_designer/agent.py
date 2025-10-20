from google.adk.agents.llm_agent import Agent
from . import prompt

ui_designer_agent = Agent(
    model="gemini-2.5-flash",
    name="ui_designer_agent",
    description="Creates visually appealing and user-friendly interface designs, focusing on layout, color schemes, and component styling. It produces mockups and style guides.",
    instruction=prompt.UI_DESIGNER_PROMPT,
)
