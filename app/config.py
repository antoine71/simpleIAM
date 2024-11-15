from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_sdn: str = "sqlite:///:memory:"
    secret_key: str = "override_me"
    algorithm: str = "HS256"
    access_token_lifetime_minutes: int = 30

    model_config = ConfigDict(env_file=".env")


settings = Settings()
