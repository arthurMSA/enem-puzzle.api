from pymongo.database import Database
from bson.objectid import ObjectId

class QuestionRepository:
    db: Database
    def __init__(self, database: Database) -> None:
        self.db = database

    def listByArea(self, area: str):
        return self.db.aggregate([
        { '$match': { 'disciplina': area } },
        { '$sample': { 'size': 3 } },
        {'$project': { 'resposta': 0 } },
    ])

    def findById(self, id: str):
        return self.db.find_one({ '_id': ObjectId(id) })