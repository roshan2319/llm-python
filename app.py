from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

question = input("Ask Gemini: ")

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=question

)

print("\nGemini:")
print(response.text)