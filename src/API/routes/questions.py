from fastapi import APIRouter
from data.enemDB.settings import getQuestionsCollection
from utils.parseMongoDocument import parseDocumentToJson

router = APIRouter(
    prefix='/questions',
    tags=['question']
)

@router.get('/')
async def listQuestions():
    db = getQuestionsCollection()
    question = db.find_one()
    return parseDocumentToJson(question)