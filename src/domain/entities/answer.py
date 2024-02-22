from pydantic import BaseModel

class Answer(BaseModel):
    value: str
    questionId: str
    userSession: str

    def __init__(self, value: str, userSession: str, questionId: str) -> None:
        self.value = value
        self.questionId = questionId
        self.userSession = userSession
    