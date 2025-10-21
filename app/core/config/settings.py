from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_USER: str = "myuser"
    DATABASE_PASSWORD: str = "mypassword"
    DATABASE_PORT: int = 5432
    DATABASE_SCHEMA: Optional[str] = None
    DATABASE_NAME: str = "mydb"
    DATABASE_DRIVER: str = "asyncpg"
    DATABASE_HOST: str = "localhost"

    APP_PORT: int = 8000
    APP_HOST: str = "127.0.0.1"
    DEBUG: bool = True

    SECRET_KEY: str = "mysecretkey"
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()
