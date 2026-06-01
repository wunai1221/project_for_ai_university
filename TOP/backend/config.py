from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    app_env: str = "development"
    app_host: str = "127.0.0.1"
    app_port: int = 8000
    # ✅ 改成允許所有 localhost（通用）
    allowed_origins: str = "*"

    # ✅ 改成你實際的 Ollama 模型名稱
    model_name: str = "gemma3:4b"
    model_base_url: str = "http://127.0.0.1:11434"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def origins_list(self) -> list[str]:
        if self.allowed_origins == "*":
            return ["*"]
        return [o.strip() for o in self.allowed_origins.split(",")]


@lru_cache()
def get_settings() -> Settings:
    return Settings()