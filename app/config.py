import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BASE_DIR: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
    DATABASE_URL: str = f"sqlite:///{os.path.join(BASE_DIR, 'rpg_content.db')}"
    OLLAMA_HOST: str = os.getenv('OLLAMA_HOST', "http://homelab101-a.zapto.org:3131/api/generate")
    OLLAMA_MODEL: str = os.getenv('OLLAMA_MODEL', "llama3")
    ENVIRONMENT: str = os.getenv('ENVIRONMENT', "development")

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
