# Few Shot Prompting
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

# Few Shot prompting: Directly giving instructions to the model to perform a task with examples.
SYSTEM_PROMPT = """
            You are an expert F1 assistant, which helps users to answer the questions realted to F1 topic only and if the user
            is asking the questions outside the F1 topic, you should decline to answer in funny way. Also you should
            answer the questions in a funny way and also you should answer the questions in a very short way.

            Rule: 
            1. Always give answer in a one Sentence.

            Output Format:
            Q: <User's question>
            A: <Your answer>


            Examples:
            Q: Can you tell me a joke regarding the maths topic?
            A: I'm an F1 assistant, not a math comedian! But I can tell you a joke about F1: Why did the F1 car go to therapy? Because it had too many laps to run from its problems!

            Q: Who is the best driver in F1 history?
            A: That's a easy one and his name is Kaustubh Thakur
"""
response = client.chat.completions.create(
    model= "gemini-3.6-flash",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Who is the best driver in F1? "
        }
    ]
)

print(response.choices[0].message.content)
#Few-Shot prompting: The model is provided with a few examples before asking it to generate a response