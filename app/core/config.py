# app/core/config.py
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_HOST: str | None = "127.0.0.1"
    DB_PORT: int | None = 5432
    INSTANCE_CONNECTION_NAME: str | None = None

    @property
    def sqlalchemy_uri(self) -> str:
        if self.INSTANCE_CONNECTION_NAME:
            return (
                "postgresql+asyncpg://"
                f"{self.DB_USER}:{self.DB_PASS}@/"
                f"{self.DB_NAME}"
                f"?host=/cloudsql/{self.INSTANCE_CONNECTION_NAME}"
            )
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",          # ← ahora busca en la raíz
        env_file_encoding="utf-8"
    )

settings = Settings()
