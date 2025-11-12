from pydantic import BaseModel, ConfigDict
from datetime import datetime


class QuestionBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    text: str


class Question(QuestionBase):
    id: int
    created_at: datetime
