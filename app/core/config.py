from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://coffee_user:3004@localhost:5432/cafe"
    DATABASE_URL_SYNC: str = "postgresql+psycopg2://coffee_user:3004@localhost:5432/cafe"
    SECRET_KEY: str = "3004"
    DEBUG: bool = True
    WEBHOOK_SECRET: str = "3004"


    SENTRY_DSN: str | None = None


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()