import hashlib
from typing import Any, Callable, Dict, Optional, Tuple
from sqlalchemy.ext.asyncio.scoping import async_scoped_session
from fastapi import Request, Response


def questions_key_builder(
    func: Callable[..., Any],
    namespace: str = "",
    *,
    request: Optional[Request] = None,
    response: Optional[Response] = None,
    args: Tuple[Any, ...],
    kwargs: Dict[str, Any],
) -> str:
    print("args:", args)
    print("kwargs:", kwargs)
    excluded_types = (async_scoped_session,)
    cache_kw = {}
    for name, value in kwargs.items():
        if isinstance(value, excluded_types):
            continue
        cache_kw[name] = value
    cache_key = hashlib.md5(  # noqa: S324
        f"{func.__module__}:{func.__name__}:{args}:{cache_kw}".encode()
    ).hexdigest()
    return f"{namespace}:{cache_key}"
