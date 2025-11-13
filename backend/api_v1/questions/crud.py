from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from sqlalchemy.orm import selectinload

from core.models import Question
from .schemas import QuestionCreate


async def get_all_questions(session: AsyncSession):
    questions: Result = await session.execute(
        statement=select(Question)
        .options(selectinload(Question.answers))
        .order_by(Question.id)
    )
    questions: list[Question] = list(questions.scalars().all())

    return questions


async def get_question_by_text(
    session: AsyncSession,
    text: str,
):
    result: Result = await session.execute(
        statement=select(Question).where(Question.text == text)
    )
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Вопрос с таким текстом уже существует.",
        )


async def create_new_question(
    session: AsyncSession,
    question: QuestionCreate,
):
    new_question = Question(**question.model_dump())

    await get_question_by_text(
        session=session,
        text=new_question.text,
    )

    session.add(new_question)

    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return new_question


async def get_question_by_id(
    session: AsyncSession,
    question_id: int,
):
    result: Result = await session.execute(
        statement=select(Question).where(Question.id == question_id)
    )
    question: Question = result.scalar_one_or_none()
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Вопроса с id {question_id} не существует.",
        )
    return question


async def delete_question(
    session: AsyncSession,
    question_id: int,
):
    question = await get_question_by_id(
        session=session,
        question_id=question_id,
    )
    await session.delete(question)
    await session.commit()
    return question
