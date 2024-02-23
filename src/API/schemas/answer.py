from pydantic import BaseModel

class AnswerQuestionPayload(BaseModel):
    answer: str
    questionId: str

class AnswerQuestionResponse(BaseModel):
    correctAnswer: str
    points: dict