from functools import partial
from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from tortoise.contrib.fastapi import RegisterTortoise


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    ENV: Literal["DEV", "PROD"]
    DB_USER: str = "authguard"
    DB_PASSWORD: SecretStr
    DATABASE: str = "authguard_db"
    DB_HOST: str
    DB_PORT: int = 3306
    DB_POOL_MIN: int = 5
    DB_POOL_MAX: int = 30
    DB_CONNECT_TIMEOUT: int = 10
    DB_POOL_RECYCLE: int = 1800
    DB_ECHO: bool = False


settings = Settings()  # type: ignore

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": settings.DB_HOST,
                "port": settings.DB_PORT,
                "user": settings.DB_USER,
                "password": settings.DB_PASSWORD.get_secret_value(),
                "database": settings.DATABASE,
                "minsize": settings.DB_POOL_MIN,
                "maxsize": settings.DB_POOL_MAX,
                "connect_timeout": settings.DB_CONNECT_TIMEOUT,
                "pool_recycle": settings.DB_POOL_RECYCLE,
                "echo": settings.DB_ECHO,
                "charset": "utf8mb4",
            },
        }
    },
    "apps": {
        "models": {
            "models": ["backend.models"],
            "default_connection": "default",
            "migrations": "backend.migrations",
        }
    },
}

register_orm = partial(
    RegisterTortoise,
    config=TORTOISE_ORM,
)
