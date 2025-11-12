from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result

from core.models import Question


async def get_all_questions(session: AsyncSession):
    questions: Result = await session.execute(
        statement=select(Question).order_by(Question.id)
    )
    questions = list(questions.scalars().all())
    return questions
