from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENV: str = "development"

    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 300

    class Config:
        env_file = ".env"

settings = Settings()
