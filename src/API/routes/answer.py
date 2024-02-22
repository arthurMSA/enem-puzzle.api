from fastapi import APIRouter

router = APIRouter(
    prefix='/answer',
    tags=['question']
)

@router.get('/')
async def listQuestions():
    pass
    # questions = QuestionRepository.listQuestions()
    # return questions

        #     question = EnemDB().connection()
        # questionRes = question.find().limit(10)
        # return json.loads(json_util.dumps(questionRes))