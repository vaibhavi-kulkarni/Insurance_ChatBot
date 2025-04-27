from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Function to generate responses from GPT-2
def generate_response(user_input):
    # Chatbot instruction to provide accurate and trustworthy information
    prompt = f"""
    ${user_input} , heyy i got you query regarding insurance . I'm helping you with that. I'm a chatbot designed to assist you with insurance policy and provide accurate and trustworthy information. about the insurance you are asking this is the information from my side . here are some insurance plan you 
    """

    # Encode the user input with the added instruction
    inputs = tokenizer.encode(prompt, return_tensors='pt')

    # Increase the response length and use parameters for better output quality
    outputs = model.generate(inputs, max_length=350, num_return_sequences=1, no_repeat_ngram_size=2, top_p=0.92, top_k=50)

    # Decode the model output and clean up the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Check if the split string exists in the response before attempting to split
    split_string = f"${user_input} , heyy"
    if split_string in response:
        response = response.split(split_string)[1].strip()
    else:
        # If the expected string is not found, return the whole response or a fallback message
        response = response.strip()

    return response
