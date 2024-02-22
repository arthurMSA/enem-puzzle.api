from abc import ABC, abstractmethod
from typing import List, Dict
from domain.entities.answer import Answer

class AnswerRepositoryInterface(ABC):
    @abstractmethod
    def answerQuestion(answer: Answer) -> None:
        raise NotImplementedError

