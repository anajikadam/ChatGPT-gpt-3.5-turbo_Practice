import os, time
import openai
import tiktoken
from dotenv import load_dotenv

from App.helper import prompt_creation, gpt_send, writeTxt

load_dotenv()
# Set up your OpenAI API key
# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

timestamp0 = time.strftime('%d%m%y', time.localtime())
log_file_path = f"ChatGPT/App/Logs/app_log_{timestamp0}"

class ChatGPT_App:
    def __init__(self, prompt_text) -> None:
        print("===>>> In ChatGPT_App")
        self.api_key = openai.api_key
        self.prompt_text = prompt_text

    def app_main__(self):
        print("__________"*10)
        timestamp11 = time.strftime('%d-%m-%y_%H:%M:%S', time.localtime())
        print(f"===>>> In app main function: {timestamp11}")
        start_time = time.time()
        # Check if the necessary prompt_text are provided
        if len(self.prompt_text) <= 3:
            print("\nError: Text data is missing. Please provide some text data. or prompt lenths less than 3")
            return 0
        print()
        clean_prompt_text = prompt_creation(self.prompt_text)
        # print(clean_prompt_text)
        prompt_start = "Act AI Assistant and answer question short in 100 tokens"
            # Send the file content to ChatGPT
        ids, responses, gpt_time = gpt_send(prompt=prompt_start, text_data=clean_prompt_text)
        # print(responses)
        print(f"===>>> GPT Response: {ids}")
        for response in responses:
            print(response)

        req_time = round((time.time() - start_time), 2)
        proc_req_time = round((req_time), 2)
        print("\n===>>> --- GPT Time in %s seconds ---" % (gpt_time))
        print("===>>> --- Overall Time in %s seconds ---" % (proc_req_time))
        
        sent_1 = "|{:<18} | GPT Time: {:<5} | Overall Time: {:<5} | Chat ID: {:<45}|\n".format(timestamp11, gpt_time, proc_req_time, ids)
        save_sent = sent_1
        writeTxt(log_file_path, save_sent)
        print("__________"*10)




# model_3 = "gpt-3.5-turbo"
# response_2 = openai.ChatCompletion.create(
#                                         model = model_3,
#                                         messages=[
#                                             {"role": "system", "content": "Act as an AI Assistant."},
#                                             {"role": "user", "content": "Hello How are you?"}
#                                         ],
#                                         max_tokens=25,
#                                         temperature=0.5,
#                                         n = 1
# )

# print(response_2)


