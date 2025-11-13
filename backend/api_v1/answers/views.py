from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import AnswerCreate, Answer

router = APIRouter(tags=["Answers"])


@router.post("/question/{question_id}", response_model=Answer)
async def create_answer(
    question_id: int,
    answer: AnswerCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_answer(
        session=session, question_id=question_id, answer=answer
    )
