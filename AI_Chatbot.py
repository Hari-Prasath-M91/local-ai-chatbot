from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGSMITH_TRACING_V2"]=os.getenv("LANGSMITH_TRACING_V2")
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", 'You are a helpful assistant. Please respond to the user queries'),
        ("user", "Question:{question}")
    ]
)

st.title("Example ChatBot Using LLAMA3.1 running Locally")
input_text = st.text_input("Enter your Query")

llm = OllamaLLM(model="llama3.1")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))