from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import streamlit as st
from utils.data import predefined_system_info # Import the updated data

# Load DialoGPT-small
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

# Initialize chat history
chat_history_ids = None

# Function to generate response
def generate_response(user_input):
    global chat_history_ids

    user_input_lower = user_input.lower()

    # First, check predefined responses
    for item in predefined_system_info:
        for keyword in item["keywords"]:
            if keyword in user_input_lower:
                if callable(item["response"]):
                    return item["response"](user_input)  # Call the lambda function for plan details
                return item["response"]

    # Otherwise, fallback to DialoGPT model response
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1) if chat_history_ids is not None else new_input_ids

    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95
    )

    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response.strip()
