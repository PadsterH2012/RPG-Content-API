from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OLLAMA_HOST: str
    OLLAMA_MODEL: str
    DATABASE_URL: str
    DEBUG: bool = False
    SECRET_KEY: str
    ENVIRONMENT: str = "development"

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def database_url(self):
        if self.ENVIRONMENT == "production":
            return self.DATABASE_URL
        else:
            return "sqlite:///./test.db"

settings = Settings()