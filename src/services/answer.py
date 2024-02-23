from database.enemDB.repository.question import QuestionRepository

class AnswerService:
    questionRepository: QuestionRepository

    def __init__(self, questionRepository: QuestionRepository) -> None:
        self.questionRepository = questionRepository

    def validateAnswer(self, questionId: str, answer: str):
        question = self.questionRepository.findById(questionId)
        correctAnswer = question['resposta']
        isCorrect = answer.lower() == correctAnswer.lower()
        points = { 'gain': 10, 'loss': 0 } if isCorrect else { 'gain': 0, 'loss': 5 }
        return { 'correctAnswer': correctAnswer, 'points': points }