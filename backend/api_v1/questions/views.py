from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import Question

router = APIRouter()


@router.get(
    "/questions",
    response_model=list[Question],
    status_code=status.HTTP_200_OK,
)
async def get_all_questions(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_all_questions(session=session)
