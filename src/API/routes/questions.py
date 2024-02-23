from fastapi import APIRouter
from utils.parseMongoDocument import parseDocumentToJson
from . .schemas.question import AreaParam
from services.question import QuestionService

router = APIRouter(
    prefix='/questions',
    tags=['question']
)

@router.get('/{area}')
async def listQuestions(area: AreaParam):
    service = QuestionService()
    return parseDocumentToJson(service.listQuestionByArea(area.value))