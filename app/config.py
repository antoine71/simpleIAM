from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    postgres_sdn: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_lifetime_minutes = 30

    class Config:
        env_file = ".env"

settings = Settings()