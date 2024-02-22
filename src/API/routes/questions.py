from fastapi import APIRouter
from data.enemDB.settings import getQuestionsCollection
from utils.parseMongoDocument import parseDocumentToJson
from domain.entities.area import Area

router = APIRouter(
    prefix='/questions',
    tags=['question']
)

@router.get('/{area}')
async def listQuestions(area: Area):
    db = getQuestionsCollection()
    question = db.aggregate([
        { '$match': { 'disciplina': area.value } },
        { '$sample': { 'size': 5 } },
        {"$project": {"resposta": 0} }
    ])
    return parseDocumentToJson(question)