from fastapi import APIRouter
from domain.entities.answer import Answer
from data.enemDB.settings import getQuestionsCollection
from bson.objectid import ObjectId

router = APIRouter(
    prefix='/answer',
    tags=['question']
)

@router.post('/')
async def answerQuestion(answerPayload: Answer):
    db = getQuestionsCollection()
    question = db.find_one({ '_id': ObjectId(answerPayload.questionId) })
    if answerPayload.answer.lower() == str(question['resposta']).lower():
        return { 'correctAnswer': question['resposta'], 'points': { 'gain': 10, 'loss': 0 } }
    return{ 'correctAnswer': question['resposta'], 'points': { 'gain': 0, 'loss': 5 } }