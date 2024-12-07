import os, asyncio
from groq import AsyncGroq
from dotenv import load_dotenv

load_dotenv()

client = AsyncGroq(
    api_key = os.getenv("GROQ_API_KEY")
)

print("Connection Established with Groq")

translate = input("What prompt do you want to translate ?\n")

to_translate=f"Prompt to Translate : {translate}"

message_content="""
You are an English to Arabic Translator, which can take any english text and translate it to arabic text. the text should have the same meaning, even if it does not have the exact same words. Your output should be the Arabic Text only, Here is a few examples, where the Prompt is the input you are given, and the answer is the exact answer you should give.

Prompt : Hello, Can I have a slice of Pie ?

Answer: مرحباً، هل يمكنني الحصول على قطعة من الفطيرة؟

Prompt : I think it might rain today, don't you think ?

Answer : أعتقد أنها قد تمطر اليوم، ألا تعتقد ذلك؟

"""

async def firstRequest() -> None:
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": (message_content + to_translate)
            }
        ],
        model=os.getenv("MODEL_NAME")
    )
    print(chat_completion.choices[0].message.content)
    f = open("output.txt", "a")
    f.write(chat_completion.choices[0].message.content)
    f.close()

asyncio.run(firstRequest())
