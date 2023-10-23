import os, time
import openai
import tiktoken

from App.save_list import save_npList_file
from App.preprocess_prompt import clean_text


def prompt_creation(prompt_text):
    clean_prompt_text = ""
    try:
        flag, cln_text = clean_text(prompt_text)
        if flag:
            clean_prompt_text = cln_text
    except Exception as ex:
        print(f"Error: {ex}")
    return clean_prompt_text

def gpt_send(prompt=None,
        text_data=None,
        chat_model="gpt-3.5-turbo",
        model_token_limit=8192,
        max_tokens=2500,
        ):
    # Check if the necessary arguments are provided
    if not prompt:
        return "Error: Prompt is missing. Please provide a prompt."

    # Initialize the tokenizer
    tokenizer = tiktoken.encoding_for_model(chat_model)

    # Encode the text_data into token integers
    token_integers = tokenizer.encode(text_data)

    # Split the token integers into chunks based on max_tokens
    chunk_size = max_tokens - len(tokenizer.encode(prompt))
    # print(chunk_size)
    chunks = [
        token_integers[i : i + chunk_size]
        for i in range(0, len(token_integers), chunk_size)
    ]
    # print(chunks)
    # Decode token chunks back to strings
    chunks = [tokenizer.decode(chunk) for chunk in chunks]
    # print(chunks)
    responses = []
    messages = [
                {"role": "user", "content": prompt},
                ]
    for chunk in chunks:
        messages.append({"role": "user", "content": chunk})

        # Check if total tokens exceed the model's limit and remove oldest chunks if necessary
        while ( sum(len(tokenizer.encode(msg["content"])) for msg in messages) > model_token_limit
               ):
            messages.pop(0)  # Remove the oldest chunk that is prompt

    # print(messages)
    gpt_start_time = time.time()
    response = openai.ChatCompletion.create(model=chat_model, messages=messages)
    gpt_end_time = time.time()
    # response = {'dummy': "akaka"}
    # print(response)
    ids = response['id']
    # print(ids)
    obj_dict = response.to_dict_recursive()
    messages.append(obj_dict)
    final_response = response.choices[0].message["content"].strip()
    # final_response = "asas"
    messages.append(final_response)
    responses.append(final_response)
    # save responses list in npy file 
    # messages.append(responses[0])
    save_npList_file(myList = messages, )
    gpt_time = round((gpt_end_time - gpt_start_time), 2)
    return ids, responses, gpt_time



def writeTxt(fname, sent):
    with open(fname+'.txt', 'a') as fp:
        fp.write(sent)
    print("--- Saved Log.....")


# Define a function to read the content of a file
def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    

