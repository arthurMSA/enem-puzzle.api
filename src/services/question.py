from database.enemDB.settings import getQuestionsCollection
from database.enemDB.repository.question import QuestionRepository

class QuestionService:
    questionRepository: QuestionRepository

    def __init__(self) -> None:
        database = getQuestionsCollection()
        self.questionRepository = QuestionRepository(database)

    def listQuestionByArea(self, area: str):
        return self.questionRepository.listByArea(area)