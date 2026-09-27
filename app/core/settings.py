from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    
    APP_NAME: str 
    DATABASE_URL: str
    ADMIN_EMAIL: str
    SECRET_KEY: str
    ADMIN_PASSWORD: str

settings = Settings()  # pyright: ignore[reportCallIssue]
    