from abc import ABC, abstractmethod
from typing import List, Dict
from domain.entities.question import Question
from domain.entities.answer import Answer

class QuestionRepositoryInterface(ABC):
    @abstractmethod
    async def listQuestions() -> List[Question]:
        raise NotImplementedError
    
    @abstractmethod
    def findQuestionById(id: str) -> Question:
        raise NotImplementedError
    
    @abstractmethod
    def answerQuestion(questionId: str, answer: Answer) -> Question:
        raise NotImplementedError