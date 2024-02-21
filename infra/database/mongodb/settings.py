import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

load_dotenv()

class MongoSettings():
    strConn: str = 'mongodb+srv://{}:{}@{}/{}'.format(
        os.environ.get('MONGODB_USER'),
        os.environ.get('MONGODB_PASSWORD'),
        os.environ.get('MONGODB_HOST'),
        os.environ.get('MONGODB_DB_NAME'),
    )

    async def connection(self):
        client = AsyncIOMotorClient(self.strConn)
        await init_beanie(database=client.enem_puzzle, document_models=[])
