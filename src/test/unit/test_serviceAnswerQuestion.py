
import pytest
from unittest.mock import MagicMock
from database.enemDB.repository.question import QuestionRepository
from services.answer import AnswerService

listQuestion = [
    {
            "_id": {
            "$oid": "6512e2b5fd7b465b0251671b"
        },
        "focos": [],
        "imagem": "",
        "texto": "question 1",
        "alternativas": [
            "a) answer a",
            "b) answer b",
            "c) answer v",
            "d) answer d",
            "e) answer e"
        ],
        "resposta": "a",
        "video_resolucao": "",
        "disciplina": "biologia",
        "tematica": "Botânica",
        "Resolucao_GPT": "",
        "Dificuldade": "Intermediate-Low",
    },
    {
        "_id": {
            "$oid": "6512e2b5fd7b465b0251689c"
        },
        "focos": [],
        "imagem": "",
        "texto": "question 2",
        "alternativas": [
            "a) answer a",
            "b) answer b",
            "c) answer v",
            "d) answer d",
            "e) answer e"
        ],
        "resposta": "d",
        "video_resolucao": "",
        "disciplina": "biologia",
        "tematica": "rna",
        "Resolucao_GPT": "",
        "Dificuldade": "Intermediate-Low",
    }
]

@pytest.fixture
def mockQuestionRepository():
    mock = MagicMock()
    mock.find_one.return_value = listQuestion[0]
    mock.aggregate.return_value = listQuestion
    return mock

def testValidateCorrectAnswer(mockQuestionRepository):
    repository = QuestionRepository(database=mockQuestionRepository)
    service = AnswerService(repository)
    answerOption = 'a'
    result = service.validateAnswer('6512e2b5fd7b465b0251689c', answerOption)

    assert result['points']['gain'] == 10
    assert result['points']['loss'] == 0
    assert result['correctAnswer'] == answerOption

def testValidateWrongAnswer(mockQuestionRepository):
    repository = QuestionRepository(database=mockQuestionRepository)
    service = AnswerService(repository)
    answerOption = 'b'
    result = service.validateAnswer('6512e2b5fd7b465b0251689c', answerOption)

    assert result['points']['gain'] == 0
    assert result['points']['loss'] == 5
    assert result['correctAnswer'] == listQuestion[0]['resposta']