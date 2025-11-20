from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from redis.asyncio import Redis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from api_v1 import router as api_v1_router
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = Redis(
        host=settings.redis.host,
        port=settings.redis.port,
        db=settings.redis.db.cache,
    )
    FastAPICache.init(
        backend=RedisBackend(redis=redis),
        prefix=settings.cache.prefix,
    )
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(
    router=api_v1_router,
    prefix=settings.api_v1_prefix,
)


@app.get("/")
def check_health():
    return {"message": "Success"}


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
