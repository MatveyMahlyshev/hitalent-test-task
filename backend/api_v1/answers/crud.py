from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

from core.models import Answer
from .schemas import AnswerCreate
from api_v1.questions.crud import get_question_by_id


async def create_answer(
    session: AsyncSession,
    question_id: int,
    answer: AnswerCreate,
):
    await get_question_by_id(
        session=session,
        question_id=question_id,
    )

    new_answer = Answer(**answer.model_dump(), question_id=question_id)
    session.add(new_answer)
    try:
        await session.commit()
    except IntegrityError as e:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e,
        )
    return new_answer
