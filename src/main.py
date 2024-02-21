from fastapi import FastAPI
from application.API.routes import question
from database.mongodb.settings import MongoSettings
from database.mongodb.repository.questionRepository import QuestionRepository
import uvicorn

app = FastAPI()

@app.on_event('startup')
async def run():
    await MongoSettings().connection()

app.include_router(question.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)