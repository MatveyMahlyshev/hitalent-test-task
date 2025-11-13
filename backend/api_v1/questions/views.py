from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import Question, QuestionCreate

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


@router.post(
    "/questions/new",
    response_model=Question,
    status_code=status.HTTP_201_CREATED,
)
async def create_new_question(
    question: QuestionCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_new_question(
        session=session,
        question=question,
    )
