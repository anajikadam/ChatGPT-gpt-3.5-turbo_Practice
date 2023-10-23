import numpy as np
import time

def save_npList_file(myList,filename = f"ChatGPT/NpList/{time.strftime('%d%m%y%H%M%S', time.localtime())}_nplist.npy"):
    # the filename should mention the extension 'npy'
    np.save(filename, myList)
    print(f"Response Saved in file {filename}, successfully!\n")


def load_npy_file(filename):
    # the filename should mention the extension 'npy'
    tempNumpyArray=np.load(filename, allow_pickle=True)
    return tempNumpyArray.tolist()


# sampleList1 = [{'role': 'user', 'content': 'Act AI Assistant and answer question short in 100 tokens'}, {'role': 'user', 'content': 'GPT'}]
# # timestamp = time.strftime('%d%m%y%H%M%S', time.localtime())
# f_name = f"NpList/{time.strftime('%d%m%y%H%M%S', time.localtime())}_nplist.npy"

# sampleList1 = [{'role': 'user', 'content': 'Act AI Assistant and answer question short in 100 tokens'}, {'role': 'user', 'content': 'what GPT'},'GPT stands for "Generative Pre-trained Transformer". It is a type of artificial intelligence model developed by OpenAI that uses deep learning techniques to generate and understand human-like text.']
# save_npList_file(sampleList1, )


# f_name = 'NpList/131023180741_nplist.npy'
# loadedList1 = load_npy_file(f_name)
# print(loadedList1)
