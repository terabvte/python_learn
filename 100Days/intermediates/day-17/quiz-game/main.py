from data import question_data
from question_model import Question

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

print(len(question_bank))
print(vars(question_bank[-1]))

for question in question_bank:
    print(vars(question))
