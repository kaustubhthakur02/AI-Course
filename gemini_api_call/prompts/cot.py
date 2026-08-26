# Chain of Thought Prompting
import json

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
        Q: Can you tell me the best driver in F1?
        Step 1: {'step' : "START", "content" : "Can you tell me the best driver in F1?"}
        Step 2: {'step' : "PLAN", "content" : "To determine the best driver in F1, I will consider factors such as race wins, championships, consistency, and overall performance. I will analyze recent seasons and historical data to identify the top driver."}
        Step 3: {'step' : "OUTPUT", "content" : "Based on recent performance and historical achievements, Lewis Hamilton is widely regarded as one of the best drivers in F1, with multiple World Championships and numerous race wins."}
"""



# response = client.chat.completions.create(
#     model= "gemini-3.6-flash",
#     response_format= {"type": "json_object"},
#     messages=[
#         {
#             "role": "system",
#             "content": SYSTEM_PROMPT
#         },
#         {
#             "role": "user",
#             "content": "Who is the best driver in F1? "
#         },
#         # Manually adding the history 
#         {"role": "user", "content": json.dumps({"step": "START", "content": "Who is the best driver in F1?"})},
#         {"role": "user", "content": json.dumps({"step": "PLAN", "content": "To answer who the best driver in F1 is, I need to consider both historical legends (like Michael Schumacher, Lewis Hamilton, Ayrton Senna, and Juan Manuel Fangio) and modern dominant drivers (like Max Verstappen). I will structure the response to highlight statistical leaders in world championships and race wins, while noting the subjective nature of comparing drivers across different eras."})},
#         {"role": "user", "content": json.dumps({"step": "OUTPUT", "content": "Determining the 'best' driver in F1 often depends on whether you look at overall historical stats or current performance:\n\n1. **Statistically (All-Time Greats)**:\n   - **Lewis Hamilton**: Holds the record for the most race wins (100+), pole positions, and is tied for the most World Drivers' Championships (7).\n   - **Michael Schumacher**: Tied with Hamilton for 7 World Championships and dominated the early 2000s with Ferrari.\n   - **Ayrton Senna & Juan Manuel Fangio**: Often cited by purists for their sheer raw speed and dominance relative to their eras.\n\n2. **Current Era Dominance**:\n   - **Max Verstappen**: Currently the dominant force in F1, breaking records for the most wins in a single season and showing unprecedented consistency with Red Bull Racing.\n\nUltimately, Lewis Hamilton and Michael Schumacher hold the strongest statistical claims to being the greatest of all time, while Max Verstappen represents the peak of modern performance."})},

#     ]
# )

# print(response.choices[0].message.content)


messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": json.dumps({"step": "START", "content": "Which is the best F1 Circuit?"})},
]

while True:
    response = client.chat.completions.create(
        model="gemini-3.6-flash",
        response_format={"type": "json_object"},
        messages=messages
    )
    content = response.choices[0].message.content
    parsed = json.loads(content)
    print(parsed)

    messages.append({"role": "assistant", "content": content})

    if parsed["step"] == "OUTPUT":
        break

    # nudge the model to continue — keeps last turn as "user"
    messages.append({"role": "user", "content": json.dumps({"step": "continue"})})