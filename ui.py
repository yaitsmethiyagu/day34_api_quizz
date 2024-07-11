from tkinter import *
from quizz_brain import QuizzBrain

THEME = "#375362"
FONT = ("Ariel", 18, "normal")




class QuizzInterface():
    def __init__(self, quizz_brain: QuizzBrain):
        self.quizz_brain = quizz_brain
        self.question_text = self.quizz_brain.next_question()

        self.window = Tk()
        self.window.title("Quizz Game")
        self.window.config(background=THEME, pady=50, padx=50)

        self.score_label = Label()
        self.score_label.config(text=f"score: {self.quizz_brain.score}/{len(self.quizz_brain.question_list)}", background=THEME, font=("Arial", 25, "normal"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas()
        self.canvas.config(width=350, height=350, background="white")
        self.question_display = self.canvas.create_text(175, 175, text=self.question_text, font=FONT, fill="black", width=340)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right_button_image = PhotoImage(file="images/true.png")
        wrong_button_image = PhotoImage(file="images/false.png")

        self.wrong_button = Button()
        self.wrong_button.config(image=wrong_button_image, command=self.left_function, padx=10, pady=10)
        self.wrong_button.grid(column=0, row=2)

        self.right_button = Button()
        self.right_button.config(image=right_button_image, command=self.right_function, padx=10, pady=10)
        self.right_button.grid(column=1, row=2)
        self.update_question(self.question_text)
        self.window.mainloop()

    def left_function(self):
        self.quizz_brain.check_answer("False")
        self.update_score(self.quizz_brain.score)
        self.update_question(f"{self.quizz_brain.next_question()}")


    def right_function(self):
        self.quizz_brain.check_answer("True")
        self.update_score(self.quizz_brain.score)
        self.update_question(f"{self.quizz_brain.next_question()}")

    def update_question(self, new_question):
        self.question_text = new_question
        self.canvas.itemconfig(self.question_display, text=self.question_text)

    def update_score(self, score):
        self.score_label.config(text=f"score: {score}/{len(self.quizz_brain.question_list)}")

# quizz_interface = QuizzInterface()
# quizz_interface.window.mainloop()
