from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OLLAMA_HOST: str
    OLLAMA_MODEL: str
    DATABASE_URL: str
    DEBUG: bool
    SECRET_KEY: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()