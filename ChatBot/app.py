# Importing Modules

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
import streamlit as st
from dotenv import load_dotenv


# API Key Setup
load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN'] = os.getenv("LANGCHAIN_API_KEY")


# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI assistant, please respond to the user queries"),
        ("user", "Question:{question}")
    ]
)

# Streamlit Framework
st.title("Tenali Ramakrishna AI")
input_text = st.text_input("Ask anything you want")

# Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))