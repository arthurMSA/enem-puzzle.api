from .routes import question
from fastapi import FastAPI
from database.mongodb.settings import MongoSettings
from database.mongodb.repository.questionRepository import QuestionRepository

app = FastAPI()

@app.on_event('startup')
async def run():
    await MongoSettings().connection()

app.include_router(question.router)