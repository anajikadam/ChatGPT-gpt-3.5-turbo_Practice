# chatgptmax.py

import os
import openai
import tiktoken
import re
from dotenv import load_dotenv

# from save_list import save_npList_file

# Set up your OpenAI API key
# Load your API key from an environment variable or secret management service

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


def clean(text):
    """
    Cleans the provided text by removing URLs, email addresses, non-letter characters, and extra whitespace.

    Args:
    - text (str): The input text to be cleaned.

    Returns:
    - str: The cleaned text.
    """
    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove email addresses
    text = re.sub(r"\S+@\S+", "", text)

    # Remove everything that's not a letter (a-z, A-Z)
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Remove whitespace, tabs, and new lines
    text = "".join(text.split())

    return text


def clean_stopwords(text: str) -> str:
    """
    Removes common stopwords from the provided text.

    Args:
    - text (str): The input text from which stopwords should be removed.

    Returns:
    - str: The text with stopwords removed.
    """
    stopwords = [
        "a",
        "an",
        "and",
        "at",
        "but",
        "how",
        "in",
        "is",
        "on",
        "or",
        "the",
        "to",
        # "what",
        "will",
    ]
    tokens = text.split()
    clean_tokens = [t for t in tokens if not t in stopwords]
    return " ".join(clean_tokens)

def read_data(file):
    """
    Reads the content of a file and returns it as a string.

    Args:
    - file (str): The path to the file to be read.

    Returns:
    - str: The content of the file.
    """
    # Open the file and read the text
    with open(file, "r", encoding="UTF-8") as f:
        text = f.read()
    return text


def clean_text_from_file(file):
    """
    Reads the content of a file, cleans it by removing stopwords, and returns the cleaned text.

    Args:
    - file (str): The path to the file whose content should be cleaned.

    Returns:
    - str: The cleaned content of the file or an error message if the file could not be read.
    """
    try:
        text = read_data(file)
    except:
        return "Error: could not read your file."
    return clean_stopwords(text)

def clean_text_file_( file_content ):
    """
    Reads the content of a file, cleans it by removing stopwords, and returns the cleaned text.

    Args:
    - file_content (str): File content paragraph.

    Returns:
    - str: remove stopword .
    """
    try:
        text = clean_stopwords(file_content)
    except :
        return "Error:"
    return text


def clean_text(text):
    try:
        text = clean_stopwords(text)
    except :
        return False, "Error:"
    return True, text

# def send(   prompt=None,
#             text_data=None,
#             chat_model="gpt-3.5-turbo",
#             model_token_limit=8192,
#             max_tokens=2500,
#         ):



# def send(   prompt=None,
#             text_data=None,
#             chat_model="gpt-3.5-turbo",
#             model_token_limit=8192,
#             max_tokens=2500,
#         ):
#     # Check if the necessary arguments are provided
#     if not prompt:
#         return "Error: Prompt is missing. Please provide a prompt."
#     if not text_data:
#         return "Error: Text data is missing. Please provide some text data."
    
#     clean_text_data = clean_text(text_data)
#     if clean_text_data == "Error:":
#         return "Error: whilen clean text data"
#     text_data = clean_text_data

#     # Initialize the tokenizer
#     tokenizer = tiktoken.encoding_for_model(chat_model)

#     # Encode the text_data into token integers
#     token_integers = tokenizer.encode(text_data)

#     # Split the token integers into chunks based on max_tokens
#     chunk_size = max_tokens - len(tokenizer.encode(prompt))
#     # print(chunk_size)
#     chunks = [
#         token_integers[i : i + chunk_size]
#         for i in range(0, len(token_integers), chunk_size)
#     ]
#     # print(chunks)
#     # Decode token chunks back to strings
#     chunks = [tokenizer.decode(chunk) for chunk in chunks]
#     # print(chunks)
#     responses = []
#     messages = [
#                 {"role": "user", "content": prompt},
#                 ]
#     for chunk in chunks:
#         messages.append({"role": "user", "content": chunk})

#         # Check if total tokens exceed the model's limit and remove oldest chunks if necessary
#         while ( sum(len(tokenizer.encode(msg["content"])) for msg in messages) > model_token_limit
#                ):
#             messages.pop(0)  # Remove the oldest chunk that is prompt

#     # print(messages)
#     response = openai.ChatCompletion.create(model=chat_model, messages=messages)
#     # print(response)
#     messages.append(response)
#     final_response = response.choices[0].message["content"].strip()
#     messages.append(final_response)
#     responses.append(final_response)
#     # save responses list in npy file 
#     # messages.append(responses[0])
#     save_npList_file(myList = messages, )
#     return responses
