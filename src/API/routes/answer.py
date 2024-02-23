from fastapi import APIRouter
from . .schemas.answer import AnswerQuestionPayload, AnswerQuestionResponse
from database.enemDB.settings import getQuestionsCollection
from bson.objectid import ObjectId

router = APIRouter(
    prefix='/answer',
    tags=['question']
)

@router.post('/')
async def answerQuestion(answer: AnswerQuestionPayload) -> AnswerQuestionResponse:
    db = getQuestionsCollection()
    question = db.find_one({ '_id': ObjectId(answer.questionId) })
    if answer.answer.lower() == str(question['resposta']).lower():
        return { 'correctAnswer': question['resposta'], 'points': { 'gain': 10, 'loss': 0 } }
    return{ 'correctAnswer': question['resposta'], 'points': { 'gain': 0, 'loss': 5 } }