import data
import question_model
import quiz_brain
import os

os.system("clear")


questions = data.question_data
question_bank =[]
correct_count = 0

for i in questions:
    question_bank.append(question_model.Question(i["text"], i["answer"]))

quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()