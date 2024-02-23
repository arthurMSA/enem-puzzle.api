from database.enemDB.settings import getQuestionsCollection
from database.enemDB.repository.question import QuestionRepository

class QuestionService:
    questionRepository: QuestionRepository

    def __init__(self, questionRepository: QuestionRepository) -> None:
        self.questionRepository = questionRepository

    def listQuestionByArea(self, area: str):
        return self.questionRepository.listByArea(area)