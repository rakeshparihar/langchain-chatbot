from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

# Explicitly specify the path to the .env file in the root directory
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)

# Debugging: Print .env file path
print(f".env file path: {dotenv_path}")

# Check if environment variables are loaded correctly
openai_api_key = os.getenv("OPENAI_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

# Debugging: Print environment variables to ensure they are loaded correctly
print(f"OPENAI_API_KEY: {openai_api_key}")
print(f"LANGCHAIN_API_KEY: {langchain_api_key}")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set")
if not langchain_api_key:
    raise ValueError("LANGCHAIN_API_KEY is not set")

os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["LANGCHAIN_TRACKING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = langchain_api_key

# Define the chat template
template = "You are a helpful assistant. Please respond to the user's queries."

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", template),
        ("user", "Question: {question}"),
    ]
)

# Streamlit framework
st.title("Helpful Assistant")
input_text = st.text_input("Enter your question here")

# OpenAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    try:
        response = chain.invoke({'question': input_text})
        st.write(response)
    except AttributeError as e:
        st.error(f"An AttributeError occurred: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
