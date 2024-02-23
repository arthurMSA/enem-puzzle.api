from fastapi import APIRouter
from utils.parseMongoDocument import parseDocumentToJson
from . .schemas.question import AreaParam
from services.question import QuestionService
from database.enemDB.settings import getQuestionsCollection
from database.enemDB.repository.question import QuestionRepository

router = APIRouter(
    prefix='/questions',
    tags=['question']
)

@router.get('/{area}')
async def listQuestions(area: AreaParam):
    repository = QuestionRepository(getQuestionsCollection())
    service = QuestionService(repository)
    return parseDocumentToJson(service.listQuestionByArea(area.value))