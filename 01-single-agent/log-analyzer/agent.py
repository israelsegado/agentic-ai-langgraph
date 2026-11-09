import os
from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from groq import Groq
from langchain.agents.structured_output import ToolStrategy

from src.schemas import Report
from src.tools import read_log_chunk, search_pattern, count_by_level
from src.config import SYSTEM_PROMPT, LLM_MODEL, AGENT_PROMPT

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ-API-KEY")

llm = ChatGroq(
    model=LLM_MODEL,
    temperature=0.2,
    max_tokens=4096,
    api_key=GROQ_API_KEY,
    reasoning_effort='low'
)

agent = create_agent(
    model = llm,
    tools=[read_log_chunk, search_pattern, count_by_level],
    system_prompt=SYSTEM_PROMPT, 
    response_format=ToolStrategy(Report)
)

user_input = input("Write the files that you want to check or extra information prompt: ")

try:
    result = agent.invoke(
        ({"messages": [{"role": "user", "content": user_input+AGENT_PROMPT}]})
    )
    print(result["structured_response"])
except Exception as e:
    print(f"ERROR: {e}")