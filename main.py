import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    print("Sin prompt")
    sys.exit(1)
    
prompt = sys.argv[1]

messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=messages
)
print(response.text)

# print("Listando modelos disponibles...")
# try:
#     # Listamos los modelos compatibles con generateContent
#     for model in client.models.list():
#         print(f"- {model.name}") # Fíjate bien en el nombre que imprime aquí
            
# except Exception as e:
#     print(f"Error al listar: {e}")