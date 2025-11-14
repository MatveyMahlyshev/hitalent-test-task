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
    '''Список вопросов с ответами.'''
    return await crud.get_all_questions(session=session)


@router.post(
    "/questions",
    response_model=Question,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"description": "Успешное создание объекта."},
        status.HTTP_404_NOT_FOUND: {"description": "Нет вопроса с таким id."},
        status.HTTP_422_UNPROCESSABLE_CONTENT: {"description": "Невалидные данные."},
        status.HTTP_409_CONFLICT: {"description": "Такой вопрос уже существует."},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Неудачное создание объекта."
        },
    },
)
async def create_new_question(
    question: QuestionCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    
    '''Создание вопроса.'''
    return await crud.create_new_question(
        session=session,
        question=question,
    )


@router.get(
    "/questions/{question_id}",
    response_model=Question,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"description": "Хороший запрос."},
        status.HTTP_404_NOT_FOUND: {"description": "Нет вопроса с таким id."},
    },
)
async def get_question_by_id(
    question_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    '''Получение вопроса по id.'''
    return await crud.get_question_by_id(
        session=session,
        question_id=question_id,
    )


@router.delete(
    "/questions/{question_id}",
    response_model=Question,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"description": "Хороший запрос."},
        status.HTTP_404_NOT_FOUND: {"description": "Нет вопроса с таким id."},
    },
)
async def delete_question(
    question_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    '''Удаление вопроса по id с ответами.'''
    return await crud.delete_question(
        session=session,
        question_id=question_id,
    )
