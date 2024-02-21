from fastapi import APIRouter
from database.mongodb.repository.questionRepository import QuestionRepository

router = APIRouter(
    prefix='/question',
    tags=['question']
)

@router.get('/')
async def listQuestions():
    list = await QuestionRepository.listQuestions()
    return list
