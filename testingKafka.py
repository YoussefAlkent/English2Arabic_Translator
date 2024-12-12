import os
from dotenv import load_dotenv
from ollama import chat
from kafka import KafkaConsumer, KafkaProducer

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "llama3.2")
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
KAFKA_INPUT_TOPIC = "E2A_Translate"
KAFKA_OUTPUT_TOPIC = "E2A_Done"

print("Connection Established with Ollama")
print(f"Listening to Kafka topic: {KAFKA_INPUT_TOPIC}")

consumer = KafkaConsumer(
    KAFKA_INPUT_TOPIC,
    bootstrap_servers=[KAFKA_BROKER],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='e2a_translate_group',
    value_deserializer=lambda x: x.decode('utf-8')
)

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda x: x.encode('utf-8')
)

message_content = """
You are an English to Arabic Translator, which can take any English text and translate it to Arabic text. The text should have the same meaning, even if it does not have the exact same words. Your output should be the Arabic text only. Here are a few examples, where the Prompt is the input you are given, and the answer is the exact answer you should give.

Prompt : Hello, Can I have a slice of Pie ?

Answer: مرحباً، هل يمكنني الحصول على قطعة من الفطيرة؟

Prompt : I think it might rain today, don't you think ?

Answer : أعتقد أنها قد تمطر اليوم، ألا تعتقد ذلك؟
"""

for message in consumer:
    translate = message.value
    print(f"Received message: {translate}")

    to_translate = f"Prompt to Translate : {translate}"

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

    producer.send(KAFKA_OUTPUT_TOPIC, translated_text)
    print(f"Sent translated text to topic {KAFKA_OUTPUT_TOPIC}")
