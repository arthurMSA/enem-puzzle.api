from database.enemDB.repository.question import QuestionRepository

class AnswerService:
    questionRepository: QuestionRepository

    def __init__(self, questionRepository: QuestionRepository) -> None:
        self.questionRepository = questionRepository

    def validateAnswer(self, answer: dict):
        question = self.questionRepository.findById(answer['questionId'])
        correctAnswer = question['resposta']
        isCorrect = answer['answer'].lower() == correctAnswer.lower()
        points = { 'gain': 10, 'loss': 0 } if isCorrect else { 'gain': 0, 'loss': 5 }
        return { 'correctAnswer': correctAnswer, 'points': points }