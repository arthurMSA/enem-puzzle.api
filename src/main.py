import uvicorn
from fastapi import FastAPI
from API.routes import question
from database.mongodb.settings import MongoSettings
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('API RUNNING')
    await MongoSettings().connection()
    yield
    print('API STOPPING')

app = FastAPI(lifespan=lifespan)

app.include_router(question.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)