from google.genai import types
from google.genai.agents import Agent, SequentialAgent, InMemorySessionService
from google.genai.tools import CodeExecutionTool

session = InMemorySessionService()

code_tool = CodeExecutionTool()

task_cleaner = Agent(
    model="gemini-2.0-flash",
    instructions="Clean and normalize the list of tasks.",
    session=session
)

scheduler = Agent(
    model="gemini-2.0-flash",
    instructions="Turn the cleaned tasks into a morning-afternoon-evening schedule.",
    session=session
)

summarizer = Agent(
    model="gemini-2.0-flash",
    instructions="Summarize and format the final daily plan.",
    session=session
)

daily_planner = SequentialAgent(
    agents=[task_cleaner, scheduler, summarizer],
    session=session
)

tasks = """
- finish homework
- study for math exam
- go to gym
- buy groceries
"""

response = daily_planner.run(f"Here are my tasks: {tasks}. Plan my day.")

print(response.text)
