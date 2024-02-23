import os
from pymongo import MongoClient, errors
from pymongo.database import Database
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()

client: MongoClient = None
database: Database = None

def getQuestionsCollection() -> Database:
    return database['enem_questions']

def enemDBConnection():
    global client, database

    MONGO_URL = os.environ.get('ENEM_DATA_BASE_URI')
    DATABASE_NAME = 'ENEM_crawler'
    
    try:
        client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)
        client.admin.command('ping')
        database = client[DATABASE_NAME]
    except errors.ServerSelectionTimeoutError as error:
        raise HTTPException(status_code=500, detail="MongoDB connection failed")

def enemDBDisconnect():
    global client, database

    client.close()
    database = None