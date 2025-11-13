from fastapi import APIRouter

from api_v1.questions.views import router as question_router

router = APIRouter()

router.include_router(router=question_router, prefix="/questions")
