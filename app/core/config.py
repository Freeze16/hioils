from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../../.env",
        env_ignore_empty=True,
        extra="ignore",
    )

    PROJECT_NAME: str = "hioils"
    API_V1_STR: str = ""
    SECRET_KEY: str = ""
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    FRONTEND_HOST: str = "http://localhost:8000"


settings = Settings()
