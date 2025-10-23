import os
from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)
PROMPTS_DIR = os.path.join(os.path.dirname(__file__), "prompts")


def load_prompt(tool_name: str) -> str:
    file_path = os.path.join(PROMPTS_DIR, f"{tool_name}.txt")
    if not os.path.exists(file_path):
        return "You are a helpful AI assistant."
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def generate_ai_response(tool: str, user_input: str) -> str:
    system_prompt = load_prompt(tool)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input},
        ],
    )
    return response.choices[0].message.content