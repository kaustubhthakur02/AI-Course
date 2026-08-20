# Chain of Thought Prompting
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

SYSTEM_PROMPT = """
        You're an expert AI assisant which help users to solve there queries
        in Chain of though.
        You need to follow the Rules.
        You will work on START, PLAN and OUTPUT steps.
        You need to first PLAN what needs to be done. The PLAN can be multiple steps.
        Once you think engough PLAN has been done, finally you can give an OUTPUT

        Rules:
        - Strictly Follow the given JSON output format
        - Only run one step at a time
        - The Sequence of steps is START (where user gives and Input), PLAN(where you will do the planning of how to resolve the user query), OUTPUT(where you will give the user the output)

        Output JSON Format:
        {'step' : "START" | "PLAN" | "OUTPUT", "content" : "string"}

        Examples:
        Q: 
        

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