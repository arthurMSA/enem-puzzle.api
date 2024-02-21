from pydantic import BaseModel

class Answer(BaseModel):
    value: str
    userSession: int

    def __init__(self, value: str, userSession: int) -> None:
        self.value = value
        self.userSession = userSession
    