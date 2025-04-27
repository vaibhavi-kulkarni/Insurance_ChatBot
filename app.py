import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2" 
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Function to generate a response from GPT-2
def generate_response(input_text):
    # Encode the input text and add the end-of-sequence token
    inputs = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")
    
    # Generate response using the GPT-2 model
    outputs = model.generate(
        inputs, 
        max_length=150,          # Limit the response length
        num_return_sequences=1,  # Generate only one response
        no_repeat_ngram_size=2,  # Prevent repeating n-grams
        top_k=50,               # Limit the sampling pool to the top k logits
        top_p=0.95,             # Apply nucleus sampling
        temperature=0.7,         # Control randomness (higher values = more random)
    )
    
    # Decode the output tensor to text and return the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Streamlit UI setup
st.title("AI-Powered Insurance Policy Information Chatbot")
st.write("Ask me anything related to insurance policies!")

# Input text from the user
user_input = st.text_input("Enter your query about insurance policies:")

if user_input:
    # Generate response from GPT-2
    response = generate_response(user_input)
    
    # Display the response
    st.write("Chatbot Response:")
    st.write(response)
