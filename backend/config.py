# config.py
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    app_env: str = "development"
    app_host: str = "127.0.0.1"
    app_port: int = 8000
    allowed_origins: str = "http://localhost:3000"

    model_name: str = "gemma4-E4b-it-uncensored"
    model_base_url: str = "http://127.0.0.1:11434"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def origins_list(self) -> list[str]:
        return [o.strip() for o in self.allowed_origins.split(",")]


@lru_cache()  # 只讀一次，不會重複 I/O
def get_settings() -> Settings:
    return Settings()