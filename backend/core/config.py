from pydantic import BaseModel
from pydantic_settings import BaseSettings
import os
from redis.asyncio import Redis


class DBSettings(BaseModel):
    url: str = (
        os.getenv("DATABASE_URL")
        or "postgresql+asyncpg://postgres:postgres@localhost:5432/hitalent_db"
    )
    echo: bool = False


class RedisDB(BaseModel):
    cache: int = 0


class RedisConfig(BaseModel):
    host: str = "localhost"
    port: int = 6379
    db: RedisDB = RedisDB()


class CacheNamespace(BaseModel):
    questions_list: str = "questions-list"


class CacheConfig(BaseModel):
    prefix: str = "fastapi-cache"
    namespace: CacheNamespace = CacheNamespace()


class Settings(BaseSettings):
    db: DBSettings = DBSettings()
    redis: RedisConfig = RedisConfig()
    cache: CacheConfig = CacheConfig()
    api_v1_prefix: str = "/api/v1"


settings = Settings()
