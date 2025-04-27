# app.py
import streamlit as st
from utils.chatbot import generate_response

# Streamlit UI
st.title('Insurance Chatbot')
st.write('Hello! How can I assist you with your insurance policy?')

# Initialize session state to keep track of previous conversation
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Input field for user query
user_input = st.text_input("Ask me anything about insurance:")

# If the user has input something, generate the response and append to conversation history
if user_input:
    response = generate_response(user_input)
    
    # Store the user's input and the bot's response in session state
    st.session_state.conversation.append(("Q: " + user_input, "A: " + response))

# Display the conversation history (questions and answers)
for question, answer in st.session_state.conversation:
    st.write(question)
    st.write(answer)
