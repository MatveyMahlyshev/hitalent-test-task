from pydantic import BaseModel
from pydantic_settings import BaseSettings
import os


class DBSettings(BaseModel):
    url: str = os.getenv("DATABASE_URL")
    echo: bool = False


class Settings(BaseSettings):
    db: DBSettings = DBSettings()
    api_v1_prefix: str = "/api/v1"


settings = Settings()
