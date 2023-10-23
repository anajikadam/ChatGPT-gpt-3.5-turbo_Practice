import os
import openai
import tiktoken
import re

# Set up your OpenAI API key
# Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv('OPEN_API_KEY_2')

def send(   prompt=None,
            text_data=None,
            chat_model="gpt-3.5-turbo",
            model_token_limit=100,
            max_tokens=250,
        ):
    # Check if the necessary arguments are provided
    if not prompt:
        return "Error: Prompt is missing. Please provide a prompt."
    if not text_data:
        return "Error: Text data is missing. Please provide some text data."

    # Initialize the tokenizer
    tokenizer = tiktoken.encoding_for_model(chat_model)

    # Encode the text_data into token integers
    token_integers = tokenizer.encode(text_data)
    print(token_integers)
    return 0

file_content = "hello, how are you"

# Define your prompt
prompt_text = "Summarize the following text for me:"

# Send the file content to ChatGPT
responses = send(prompt=prompt_text, text_data=file_content)


