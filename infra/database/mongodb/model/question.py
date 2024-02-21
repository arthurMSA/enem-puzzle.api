from beanie import Document
from domain.entities.answer import Answer
from domain.entities.area import Area
from typing import List, Optional, Dict

class QuestionModel(Document):
    prompt: str
    area: Area
    response: str
    options: Dict[str, str]
    answers: Optional[List[Answer]] = None

    class Settings:
        name = "questions"