import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from API.routes import questions, answer
from contextlib import asynccontextmanager
from database.enemDB.settings import enemDBConnection, enemDBDisconnect

@asynccontextmanager
async def lifespan(app: FastAPI):
    enemDBConnection()
    yield
    enemDBDisconnect()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(questions.router)
app.include_router(answer.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)