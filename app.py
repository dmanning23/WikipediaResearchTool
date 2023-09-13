import os
from apikey import apikey
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType

import streamlit as st

os.environ["OPENAI_API_KEY"] = apikey

llm = OpenAI(temperature=0.0)

tools = load_tools(["wikipedia", "llm-math"], llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

st.title("Wikipedia Research Tool")
topic = st.text_input("Input Wikipedia research task\n")

if topic:
    response = agent.run(topic)
    st.write(response)