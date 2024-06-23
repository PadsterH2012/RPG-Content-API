import requests
from app.config import settings

def generate_content(prompt: str) -> str:
    try:
        response = requests.post(
            f"{settings.OLLAMA_HOST}/api/generate",
            json={"model": settings.OLLAMA_MODEL, "prompt": prompt, "stream": False}
        )
        response.raise_for_status()
        return response.json().get("response", "")
    except Exception as e:
        print(f"Error generating content: {e}")
        return "Sorry, I couldn't process that request."