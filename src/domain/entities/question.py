from domain.entities.area import Area
from domain.entities.answer import Answer
from pydantic import BaseModel
from typing import List, Dict

class Question(BaseModel):
    _id: str
    prompt: str
    response: str
    options: Dict[str, str]
    area: Area
    answers: List[Answer]
