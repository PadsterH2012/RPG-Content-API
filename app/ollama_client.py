from ollama import Client
from app.config import settings

client = Client(host=settings.OLLAMA_HOST)

def generate_content(prompt: str) -> str:
    try:
        response = client.chat(model=settings.OLLAMA_MODEL, messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])
        return response['message']['content']
    except Exception as e:
        print(f"Error generating content: {e}")
        return "Sorry, I couldn't process that request."