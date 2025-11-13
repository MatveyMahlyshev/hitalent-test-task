from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import Question, QuestionCreate, QuestionWithAnswers

router = APIRouter(tags=["Questions"])


@router.get(
    "/questions",
    response_model=list[QuestionWithAnswers],
    status_code=status.HTTP_200_OK,
)
async def get_all_questions(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_all_questions(session=session)


@router.post(
    "/questions",
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


@router.get(
    "/questions/{question_id}",
    response_model=Question,
    status_code=status.HTTP_200_OK,
)
async def get_question_by_id(
    question_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_question_by_id(
        session=session,
        question_id=question_id,
    )


@router.delete(
    "/questions/{question_id}",
    response_model=Question,
    status_code=status.HTTP_200_OK,
)
async def delete_question(
    question_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.delete_question(
        session=session,
        question_id=question_id,
    )
