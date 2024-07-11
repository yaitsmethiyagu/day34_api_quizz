import html


def validate_answer(user_answer, correct_answer) -> bool:
    return user_answer.lower() == correct_answer.lower()


class QuizzBrain():

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self) -> str:


        if self.still_have_question():
            current_question = self.question_list[self.question_number]
            current_question_text = current_question.text
            current_question_text = html.unescape(current_question_text)
            output = f"Q.{self.question_number +1}: {current_question_text}"

            return output
        else:
            return "You Finished the quizz"

    def check_answer(self, user_answer) -> bool:
        if self.still_have_question():
            current_question = self.question_list[self.question_number]
            current_question_answer = current_question.answer
            #print(user_answer, current_question_answer)

            if validate_answer(user_answer, current_question_answer):
                self.score += 1
                self.question_number += 1
                return True
            else:
                self.question_number += 1
                return False

    def still_have_question(self) -> bool:
        return self.question_number < (len(self.question_list))
