from data import question_data
from question_model import Question

question_bank = []

for question in question_data:
    q = question["text"]
    a = question["text"]
    question_created = Question(q_text=q, q_answer=a)
    question_bank.append(question_created)


print(question_bank[0])