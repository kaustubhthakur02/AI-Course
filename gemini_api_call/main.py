from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("GEMINI_API_BASE_URL")

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

response = client.chat.completions.create(
    model= "gemini-3.6-flash",
    messages=[
        {
            "role": "system",
            "content": "You are an expert F1 assistant, which helps users to answer the questions realted to F1 topic only and if the user"
            "is asking the questions outside the F1 topic, you should decline to answer in funny way. Also you should"
            "answer the questions in a funny way and also you should answer the questions in a very short way."
        },
        {
            "role": "user",
            "content": "Can you tell who is the best driver in F1 history?, rank them "
        }
    ]
)

print(response.choices[0].message.content)
