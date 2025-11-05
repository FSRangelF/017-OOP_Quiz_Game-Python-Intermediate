from question_model import Question
from quiz_brain import QuizBrain
import data

question_bank = []
for item in data.question_data:
    new_q = Question(item["question"],item["correct_answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quizz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
