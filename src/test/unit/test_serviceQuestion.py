
import pytest
from unittest.mock import MagicMock
from database.enemDB.repository.question import QuestionRepository
from services.question import QuestionService

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

def testListQuestionByArea(mockQuestionRepository):
    repository = QuestionRepository(database=mockQuestionRepository)
    service = QuestionService(repository)
    result = service.listQuestionByArea('biologia')

    assert len(result) == 2
    assert result[0]["_id"]["$oid"] == "6512e2b5fd7b465b0251671b"
    assert result[1]["_id"]["$oid"] == "6512e2b5fd7b465b0251689c"