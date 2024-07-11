import data
from question_model import Question
from quizz_brain import QuizzBrain
from ui import QuizzInterface



#print(data.question_data)

question_bank = []
for items in data.question_data:
    question = Question(q_text=items["question"], q_answer= items["correct_answer"])
    question_bank.append(question)

quizz_brain = QuizzBrain(question_bank)

quizz_interface = QuizzInterface(quizz_brain)
#
# while quizz_brain.still_have_question():
#     quizz_interface.update_question(quizz_brain.next_question())

#
# print(f"You have completed the quizz. Your score is {quizz_brain.score}/{quizz_brain.question_number}")