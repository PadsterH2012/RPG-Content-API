from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./rpg_content.db"
    OLLAMA_HOST: str = "http://homelab101-a.zapto.org:3131/api/generate"
    OLLAMA_MODEL: str = "llama3"
    ENVIRONMENT: str = "development"  # Add an environment variable to switch between dev and prod

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()