from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from fastapi_cache import FastAPICache

from core.config import settings
from core.models import Answer
from .schemas import AnswerCreate
from api_v1.questions.crud import get_question_by_id


async def cache_clear():
    if settings.cache.environment != "testing":
        await FastAPICache.clear(namespace=settings.cache.namespace.questions_list)


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
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Неудачное создание объекта.",
        )

    await cache_clear()
    return new_answer


async def get_answer_by_id(
    session: AsyncSession,
    answer_id: int,
):
    result: Result = await session.execute(select(Answer).where(Answer.id == answer_id))
    answer = result.scalar_one_or_none()
    if not answer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Вопроса с id {answer_id} не существует.",
        )

    return answer


async def delete_answer_by_id(
    session: AsyncSession,
    answer_id: int,
):
    answer = await get_answer_by_id(
        session=session,
        answer_id=answer_id,
    )
    await session.delete(answer)
    await session.commit()
    return answer
