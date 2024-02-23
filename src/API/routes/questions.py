from fastapi import APIRouter
from database.enemDB.settings import getQuestionsCollection
from utils.parseMongoDocument import parseDocumentToJson
from . .schemas.question import AreaParam

router = APIRouter(
    prefix='/questions',
    tags=['question']
)

@router.get('/{area}')
async def listQuestions(area: AreaParam):
    db = getQuestionsCollection()
    question = db.aggregate([
        { '$match': { 'disciplina': area.value } },
        { '$sample': { 'size': 5 } },
        {"$project": {"resposta": 0} }
    ])
    return parseDocumentToJson(question)