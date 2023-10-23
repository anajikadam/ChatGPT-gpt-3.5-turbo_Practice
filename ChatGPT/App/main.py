import os
import openai
import tiktoken

# Set up your OpenAI API key
# Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("OPENAI_API_KEY")

# First, import the necessary modules and the function
import os

from chatgptmax import send

# Define a function to read the content of a file
def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Use the function
if __name__ == "__main__":
    # Specify the path to your file
    file_path = "abc1.txt"
    # file_path = "abc.txt"
    
    # Read the content of the file
    file_content = read_file_content(file_path)
    # print(file_content)
    # Define your prompt
    prompt_text = "Summarize the following text for me:"
    prompt_text = "Act AI Assistant and answer question short in 100 tokens"

    # Send the file content to ChatGPT
    responses = send(prompt=prompt_text, text_data=file_content)
    # print(responses)
    # Print the responses
    for response in responses:
        print(response)