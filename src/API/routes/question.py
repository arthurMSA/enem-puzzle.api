from fastapi import APIRouter
from database.mongodb.repository.questionRepository import QuestionRepository
from database.mongodb.settings import MongoSettings

router = APIRouter(
    prefix='/question',
    tags=['question']
)

@router.get('/')
async def listQuestions():
    await MongoSettings().connection()
    list = await QuestionRepository.listQuestions()
    return list
