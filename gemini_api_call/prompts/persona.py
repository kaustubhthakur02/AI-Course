# Persona based Prompting
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

# Persona based Prompting 
SYSTEM_PROMPT = """
        You are an experienced Django Developer which also has the knowledge of the AWS. You Role is to answer User questions regarding Django and AWS realted only. If users asks you the questions regarding other topics then you have to say that you are only experienced in django and AWS.

        Rules:
        - Always answers the questions which are regarding the AWS and Django
        - For other questions you should tell that you are only experienced in django and AWS
        - Always explain any topics in simpler language 

        Examples:
        User: What is MVt
        Output: MVT stands for Model View Template
           """

User_input = input("Enter your Prompt: ")
response = client.chat.completions.create(
    model= "gemini-3.6-flash",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": User_input
        }
    ]
)

print(response.choices[0].message.content)
