from fastapi import APIRouter
from . .schemas.answer import AnswerQuestionPayload, AnswerQuestionResponse
from services.answer import AnswerService
from database.enemDB.settings import getQuestionsCollection
from database.enemDB.repository.question import QuestionRepository

router = APIRouter(
    prefix='/answer',
    tags=['question']
)

@router.post('/')
async def answerQuestion(answer: AnswerQuestionPayload) -> AnswerQuestionResponse:
    repository = QuestionRepository(getQuestionsCollection())
    service = AnswerService(repository)
    return service.validateAnswer(answer)
