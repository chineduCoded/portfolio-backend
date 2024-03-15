from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_name: str
    mongodb_uri: str
    github_oauth_client_id: str
    github_oauth_client_secret: str
    redirect_uri: str
    client_origin: str
    jwt_secret_key: str
    jwt_refresh_secret_key: str
    token_url: str
    root_path: str = ""
    logging_level: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()