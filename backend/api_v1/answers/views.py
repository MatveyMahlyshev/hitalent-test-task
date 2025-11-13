from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import AnswerCreate, Answer

router = APIRouter(tags=["Answers"])


@router.post(
    "/question/{question_id}",
    response_model=Answer,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"description": "Успешное создание объекта."},
        status.HTTP_404_NOT_FOUND: {"description": "Нет вопроса с таким id."},
        status.HTTP_422_UNPROCESSABLE_CONTENT: {"description": "Невалидные данные."},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Неудачное создание объекта."
        },
    },
)
async def create_answer(
    question_id: int,
    answer: AnswerCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    '''
    Создание ответов к вопросу
    '''
    return await crud.create_answer(
        session=session,
        question_id=question_id,
        answer=answer,
    )


@router.get(
    "/{answer_id}",
    response_model=Answer,
    responses={
        status.HTTP_200_OK: {"description": "Хороший запрос."},
        status.HTTP_404_NOT_FOUND: {"description": "Нет вопроса с таким id."},
        status.HTTP_422_UNPROCESSABLE_CONTENT: {"description": "Невалидные данные."},
    },
)
async def get_answer_by_id(
    answer_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    '''
    Получение ответа по id
    '''
    return await crud.get_answer_by_id(
        session=session,
        answer_id=answer_id,
    )
