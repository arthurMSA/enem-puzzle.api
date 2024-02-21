from fastapi import FastAPI
from infra.database.mongodb.settings import MongoSettings
from infra.database.mongodb.repository.questionRepository import QuestionRepository
from infra.database.mongodb.model.question import QuestionModel

app = FastAPI()

@app.on_event('startup')
async def run():
    await MongoSettings().connection()

@app.get('/questions')
async def findAll():
    questionList = await QuestionModel.find_all().to_list()
    print(questionList)
    return questionList
    