from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DBSettings(BaseModel):
    url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/hitalent"
    echo: bool = False


class Settings(BaseSettings):
    db: DBSettings = DBSettings()
    api_v1_prefix = "/api/v1"


settings = Settings()
