import os
from openai import OpenAI
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import docx2txt
import PyPDF2

client = OpenAI(api_key=settings.OPENAI_API_KEY)
PROMPTS_DIR = os.path.join(os.path.dirname(__file__), "prompts")


def load_prompt(tool_name):
    file_path = os.path.join(PROMPTS_DIR, f"{tool_name}.txt")
    if not os.path.exists(file_path):
        return "You are a helpful AI assistant."
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def generate_ai_response(tool, user_input):
    system_prompt = load_prompt(tool)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input},
        ],
    )
    return response.choices[0].message.content

def extract_text(uploaded_file):

    if not uploaded_file:
        return ""
    
    filename = uploaded_file.name.lower()
    
    try:
        if filename.endswith('.pdf'):
            reader = PyPDF2.PdfReader(uploaded_file)
            text = "\n".join(
                [page.extract_text() for page in reader.pages if page.extract_text()]
            )
            return text
        
        elif filename.endswith('.docx'):
            return docx2txt.process(uploaded_file)
        
        elif filename.endswith('.txt'):
            return uploaded_file.read().decode('utf-8', errors='ignore')
        
        else:
            return ""
    
    except Exception as e:
        print(f"Error extracting text from {filename}: {e}")
        return ""