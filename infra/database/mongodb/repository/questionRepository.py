import json
from domain.repositories.questionRepository import QuestionRepositoryInterface
from typing import List
from domain.entities.question import Question
from domain.entities.answer import Answer
from . .model.question import QuestionModel

class QuestionRepository(QuestionRepositoryInterface):
    async def listQuestions() -> List[Question]:
        questionList = await QuestionModel.find_all().project(Question).to_list()
        return questionList
    
    def findQuestionById(id: str) -> Question:
        pass
    
    def answerQuestion(questionId: str, answer: Answer) -> Question:
        pass