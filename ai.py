import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def output_data(page_content):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=f"Generate a summary of the {page_content}.",)
    
    return response.text