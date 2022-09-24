import tkinter
from tkinter import *
import requests

BACKGROUND_COLOR = "#b1e4eb"

class ConfigureGame(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Configure game")
        self.config(bg=BACKGROUND_COLOR, pady=20, padx=20)

        #Label
        self.title_label = Label(text="Configure game", width=50)
        self.title_label.grid(column=0, row=0, columnspan=2, pady=20)

        #Parameter variables
        self.amount = 2
        self.type = "boolean"
        self.difficulty = "easy"

        #List for quantity of questions
        self.questions_quantity = [
            5,
            10,
            20,
            30,
            35,
        ]
        self.quantity_clicked = StringVar()
        self.quantity_clicked.set("Quantity")

        #Dropdown menu for quantity of questions
        self.drop_quant = OptionMenu(self, self.quantity_clicked, *self.questions_quantity, command=self.quantity_questions_selected_func)
        self.drop_quant.config(bd=0, highlightthickness=0)
        self.drop_quant.grid(column=0, row=1, )

        #List of difficulties
        self.difficulties = [
            "easy",
            "medium",
            "hard"
        ]
        self.difficulty_clicked = StringVar()
        self.difficulty_clicked.set("Difficulty")

        #Dropdown menu for difficulty
        self.drop_difficulty = OptionMenu(self, self.difficulty_clicked, *self.difficulties, command=self.difficulty_selected_func)
        self.drop_difficulty.config(bd=0, highlightthickness=0)
        self.drop_difficulty.grid(column=0, row=2, pady=20)

        #Button to kill current window and start game
        self.exit_button = Button(self, text="Start trivia!", command=self.destroy, bd=0, highlightthickness=0)
        self.exit_button.grid(column=0, row=3)

        self.mainloop()

    def quantity_questions_selected_func(self,event):
        questions_quantity_label = Label(self, text=f"Quantity: {self.quantity_clicked.get()}", bg=BACKGROUND_COLOR)
        questions_quantity_label.grid(column=1, row=1)
        number = int(self.quantity_clicked.get())
        self.amount = number

    def difficulty_selected_func(self,event):
        difficulty_quantity_label = Label(self, text=f"Difficulty: {self.difficulty_clicked.get()}", bg=BACKGROUND_COLOR)
        difficulty_quantity_label.grid(column=1, row=2)
        self.difficulty = self.difficulty_clicked.get()

#conf = ConfigureGame()