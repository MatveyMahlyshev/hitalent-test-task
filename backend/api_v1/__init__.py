from fastapi import APIRouter

from api_v1.questions.views import router as questions_router
from api_v1.answers.views import router as answers_router

router = APIRouter()

router.include_router(router=questions_router, prefix="/questions")
router.include_router(router=answers_router, prefix="/answers")
