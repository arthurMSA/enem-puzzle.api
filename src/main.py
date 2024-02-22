import uvicorn
from fastapi import FastAPI
from API.routes import questions, answer
from contextlib import asynccontextmanager
from data.enemDB.settings import enemDBConnection, getQuestionsCollection, enemDBDisconnect

@asynccontextmanager
async def lifespan(app: FastAPI):
    enemDBConnection()
    yield
    enemDBDisconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(questions.router)
app.include_router(answer.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)