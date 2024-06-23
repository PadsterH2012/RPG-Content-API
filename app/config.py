from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.config import settings
from app.database import Base
from app.models import item  # Import your models here

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata

# Set the sqlalchemy.url in the alembic configuration
config.set_main_option("sqlalchemy.url", settings.database_url)

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()


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