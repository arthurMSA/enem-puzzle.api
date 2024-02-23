from fastapi import APIRouter
from . .schemas.answer import AnswerQuestionPayload, AnswerQuestionResponse
from services.answer import AnswerService

router = APIRouter(
    prefix='/answer',
    tags=['question']
)

@router.post('/')
async def answerQuestion(answer: AnswerQuestionPayload) -> AnswerQuestionResponse:
    service = AnswerService()
    return service.validateAnswer(answer)
