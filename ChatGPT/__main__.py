
print("ChatGPT App Started ===>>> \n")
import argparse
from App import app
from App.helper import read_file_content


def argsParser():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-i", "--id", type=int, help="Number 1 ", required=False)
    arg_parse.add_argument("-t", "--text", help="Text", required=False)

    # arg_parse.add_argument()
    args = vars(arg_parse.parse_args())
    return args

args = argsParser()
# print(args)
keys_with_values_not_none = [key for key, value in args.items() if value is not None]

# print(keys_with_values_not_none)
file_name = r"ChatGPT/App/test_prompt.txt"
if len(keys_with_values_not_none)==0:
    text = ''
    print("No arg passed")
elif keys_with_values_not_none[0] == 'id':
    id = args['id']
    if id==0:
        text = read_file_content(file_path = file_name)
    else:
        text = ''
        print("No file found...")
elif keys_with_values_not_none[0] == 'text':
    text = args['text']

try:
    prompt_text = text
    if len(prompt_text)>1:
        # print("Text:",prompt_text)
        gpt = app.ChatGPT_App(prompt_text)
        gpt.app_main__()

except Exception as ex:
    print(f"Error: {ex}")


# prompt_text = 'what is openai GPT best LLM model'
# prompt_text = ''








