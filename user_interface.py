import tkinter as tk
from tkinter import *
from brain import QuizBrain
BACKGROUND_COLOR = "#0b487f"

class QuizInterface(tk.Tk):
    def __init__(self, quiz_brain: QuizBrain):
        super().__init__()
        self.quiz_brain = quiz_brain
        self.title("Quiz Trivia")
        self.config(pady=20, padx=20, bg=BACKGROUND_COLOR)

        #Create score label
        self.score_label = Label(text="Score: 0", bg=BACKGROUND_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        #Create Canvas
        self.canvas = Canvas(width=300, height=260)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.text = self.canvas.create_text(150,
                                100,
                                text=f"start",
                                font=("Arial", 20, "italic"),
                                width=280,

                                            )

        #Create buttons
        self.true_button_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_button_img, border=0, highlightthickness=0, command=self.check_true_button_pressed)
        self.true_button.grid(column=0, row=2)

        self.wrong_button_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.wrong_button_img, border=0, highlightthickness=0, command=self.check_false_button_pressed)
        self.false_button.grid(column=1, row=2)


        self.get_next_question()
        self.mainloop()

    def get_next_question(self):
         if self.quiz_brain.check_if_more_question():
                self.true_button.config(state="normal")
                self.false_button.config(state="normal")
                current_question = self.quiz_brain.ask_user_next_question()
                self.score_label.config(text=f"Score: {self.quiz_brain.score}")
                self.canvas.itemconfig(self.text, text=current_question)
                self.canvas.config(bg="white")

         else:
             self.canvas.itemconfig(self.text, text="No more questions")

    def check_true_button_pressed(self):
        is_true = self.quiz_brain.check_user_answer("true")
        self.provide_feedback(is_true)

    def check_false_button_pressed(self):
        is_true = self.quiz_brain.check_user_answer("false")
        self.provide_feedback(is_true)


    def provide_feedback(self, is_true):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.after(2000, self.get_next_question)