from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Environment(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    DEBUG: bool = True
    POSTGRES_HOST: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_DB: str = "{{cookiecutter.db_name}}"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_PASS_FILE: str | None = None
    POSTGRES_PORT: int = 5432
    ALLOWED_HOSTS: str = "*"
    CSRF_TRUSTED_ORIGINS: str = "http://127.0.0.1:8000"

    SECRET_KEY: str = "STRONG_KEY"
    ENCRYPTION_KEY: str = "ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg="
    ENCRYPTION_KEY_FILE: str | None = None
    SECRET_KEY_FILE: str | None = None


ENV = Environment()
