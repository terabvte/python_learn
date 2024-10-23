from data import question_data
from quiz_brain import QuizBrain
from question_model import Question


question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

brain = QuizBrain(question_bank)

try:
    while brain.still_has_questions():
        brain.next_question()
except:
    print("--------------------------")
    print("\nYou've completed the quiz")
    print(f"Your final score was {brain.score}/{brain.question_number}\n")