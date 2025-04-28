# app.py

import streamlit as st
from utils.chatbot import generate_response

# Streamlit UI
st.title('Insurance Chatbot')
st.write('Hello! How can I assist you with your insurance policy?')

# Chat loop
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask me anything about insurance:")

if user_input:
    response = generate_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Display the conversation
for speaker, text in st.session_state.chat_history:
    st.write(f"**{speaker}:** {text}")
