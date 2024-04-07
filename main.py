import os
from openai import OpenAI
import re

client = OpenAI(base_url="http://10.0.5.217:5555/v1", api_key="lm-studio")

directory_path = './Migration-Test/hackkosice2024-fe'
ignore_list = ['node_modules', '.git', 'venv']

relative_file_paths_excluding_ignore_list = []

for root, dirs, files in os.walk(directory_path):
    dirs[:] = [d for d in dirs if d not in ignore_list]

    for file in files:
        relative_path = os.path.relpath(os.path.join(root, file), start=directory_path)
        relative_file_paths_excluding_ignore_list.append(relative_path)

files_structure = ", ".join(relative_file_paths_excluding_ignore_list)

def find_triple_quoted_strings(text):
    pattern = r'```(.*?)```'
    matches = re.findall(pattern, text, re.DOTALL)
    return matches


completion = client.chat.completions.create(
  model="TheBloke/deepseek-coder-6.7B-instruct-GGUF/deepseek-coder-6.7b-instruct.Q8_0.gguf",
  messages=[
    {
        "role": "user",
        "content": f"""
            Based on this file structure: {files_structure}, generate me a new file structure but for react project, return me a structure of files in tree view
            YOUR ANSWER MUST CONTAIN ONLY FILE STRUCTURE, NO FURTHER EXPLANATIONS.
            FOLDER NAMES SHOULD ENDS WITH /
            NO TEXT CAN BE WRITTEN AFTER THE TREE. DO NOT MARK THE END OF CODE IN ANY COMMENTS.
        """
    }
  ],
  temperature=0.7,
)

print(completion.choices[0].message.content)

found_strings = find_triple_quoted_strings(completion.choices[0].message.content)

print(found_strings)