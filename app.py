from fastapi import FastAPI
from src.application.API.routes import question
from src.data.mongodb.settings import MongoSettings

app = FastAPI()

@app.on_event('startup')
async def run():
    await MongoSettings().connection()

app.include_router(question.router)