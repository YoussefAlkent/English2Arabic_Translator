import os
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

MODEL_NAME = "llama3.2"

print("Connection Established with Ollama")

translate = input("What prompt do you want to translate?\n")

to_translate = f"Prompt to Translate : {translate}"

message_content = """
You are an English to Arabic Translator, which can take any English text and translate it to Arabic text. The text should have the same meaning, even if it does not have the exact same words. Your output should be the Arabic text only. Here are a few examples, where the Prompt is the input you are given, and the answer is the exact answer you should give.

Prompt : Hello, Can I have a slice of Pie ?

Answer: مرحباً، هل يمكنني الحصول على قطعة من الفطيرة؟

Prompt : I think it might rain today, don't you think ?

Answer : أعتقد أنها قد تمطر اليوم، ألا تعتقد ذلك؟
"""

response = chat(model=MODEL_NAME, messages=[
    {
        'role': 'user',
        'content': (message_content + to_translate)
    },
])

translated_text = response.message.content
print(translated_text)

with open("output.txt", "a", encoding="utf-8") as f:
    f.write(translated_text + "\n")
