import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent

from src.config import LLM_MODEL, SYSTEM_PROMPT, AGENT_PROMPT, USER_INPUT
from src.tools import list_tree, read_file, find_undocumented, write_proposal

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ-API-KEY")

os.makedirs("proposals", exist_ok=True)

llm = ChatGroq(
    model=LLM_MODEL,
    temperature=0.2,
    max_tokens=4096,
    api_key=GROQ_API_KEY,
    reasoning_effort='low'
)

tools = [list_tree, read_file, find_undocumented, write_proposal]
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT,
)

user_input = input(USER_INPUT)

try:
    agent.invoke(
        ({"messages": [{"role": "user", "content": user_input+AGENT_PROMPT}]})
    )
except Exception as e:
    print(f"ERROR: {e}")
