from dotenv import load_dotenv
import os
from google import genai
import gradio as gr

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_gemini(question):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=question
    )

    return response.text

demo = gr.Interface(
    fn=ask_gemini,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Ask Me anything..."
    ),
    outputs=gr.Textbox(label="Response"),
    title="AI ChatBot",
    description="A simple chatbot built using Python, Gemini API, and Gradio."
)


demo.launch()