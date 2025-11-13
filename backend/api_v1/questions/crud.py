from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

from core.models import Question
from .schemas import QuestionCreate


async def get_all_questions(session: AsyncSession):
    questions: Result = await session.execute(
        statement=select(Question).order_by(Question.id)
    )
    questions = list(questions.scalars().all())
    return questions


async def get_question_by_text(session: AsyncSession, text: str):
    stmt = select(Question).where(Question.text == text)
    result: Result = await session.execute(statement=stmt)
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
    await session.flush()

    try:
        await session.commit()
    except IntegrityError as e:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return new_question
