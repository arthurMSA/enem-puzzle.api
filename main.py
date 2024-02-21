from fastapi import FastAPI
from infra.database.mongodb.settings import MongoSettings

app = FastAPI()

@app.on_event('startup')
async def run():
    await MongoSettings().connection()



