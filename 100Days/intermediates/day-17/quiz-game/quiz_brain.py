class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def still_has_questions(self):
        if self.question_number > len(self.question_list): return False
        else: return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number+1}: {current_question.text} (True/False)?: ").title()
        self.question_number += 1
        
        if self.check_answer(answer, current_question.answer):
            print("\nYou got it right!")
            self.score += 1
        else: print("\nThat's wrong...")
        print(f"The correct answer was {current_question.answer}.")
        print(f"Your current score is {self.score}/{self.question_number}\n")

    def check_answer(self, user_answer, question_answer):
        return user_answer == question_answer

