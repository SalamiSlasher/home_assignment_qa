from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    base_url: str = Field(
        default="https://httpbin.org",
        validation_alias="BASE_URL",
    )
    timeout: float = Field(
        default=5.0,
        validation_alias="TIMEOUT",
    )
    retries: int = Field(
        default=3,
        validation_alias="RETRIES",
    )
    retry_backoff: float = Field(
        default=0.5,
        validation_alias="RETRY_BACKOFF",
    )


settings = Settings()
