import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from .model.question import QuestionModel

load_dotenv()

class MongoSettings():
    strConn: str = 'mongodb+srv://{}:{}@{}/?retryWrites=true&w=majority'.format(
        os.environ.get('MONGODB_USER'),
        os.environ.get('MONGODB_PASSWORD'),
        os.environ.get('MONGODB_HOST'),
    )

    async def connection(self):
        client = AsyncIOMotorClient(self.strConn)
        await init_beanie(database=client.enem_puzzle, document_models=[QuestionModel])
