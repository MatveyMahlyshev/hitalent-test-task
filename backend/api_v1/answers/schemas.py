from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class AnswerBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    text: str = Field(min_length=5)


class Answer(AnswerBase):
    id: int
    question_id: int
    user_id: str
    created_at: datetime


class AnswerCreate(AnswerBase):
    pass
