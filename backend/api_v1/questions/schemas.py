from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

from api_v1.answers.schemas import Answer


class QuestionBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    text: str = Field(min_length=5)


class Question(QuestionBase):
    id: int
    created_at: datetime


class QuestionCreate(QuestionBase):
    pass


class QuestionWithAnswers(Question):
    answers: list[Answer]
