import streamlit as st
import os
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.error("OpenAI API Key not found. Set it as an environment variable.")
    st.stop()

# Initialize Chat Model
chat = ChatOpenAI(temperature=0.5, openai_api_key=openai_api_key)

# Set page title
st.set_page_config(page_title="Interactive Chat Bot")
st.header("Welcome to PseudoServices Chat! 💬")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []
    st.session_state["step"] = "waiting_for_hi"

# Function to display chat history
def display_chat():
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])

display_chat()

# Chatbot interaction
if st.session_state["step"] == "waiting_for_hi":
    user_input = st.chat_input("Type 'Hi' to start the conversation")
    if user_input and user_input.lower() == "hi":
        st.session_state["messages"].append({"role": "user", "content": user_input})
        st.session_state["messages"].append({"role": "assistant", "content": "Welcome to PseudoServices! How can I assist you today?\n1. Upload a Project\n2. Track Ticket\n3. Support"})
        st.session_state["step"] = "intro"
        st.rerun()

elif st.session_state["step"] == "intro":
    user_input = st.chat_input("")
    if user_input in ["1", "2", "3"]:
        st.session_state["messages"].append({"role": "user", "content": user_input})
        st.session_state["messages"].append({"role": "assistant", "content": "Thank you! Proceeding with your request..."})
        st.session_state["step"] = "complete"
        st.rerun()
    elif user_input:
        st.session_state["messages"].append({"role": "user", "content": user_input})
        st.session_state["messages"].append({"role": "assistant", "content": "Invalid choice. Please enter 1, 2, or 3."})
        st.rerun()

elif st.session_state["step"] == "complete":
    st.write("pseudoteam")
