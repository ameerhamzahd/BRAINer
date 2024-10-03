from os import name
import tkinter as tk
import random

class SequenceGame:
    def init(self):
        self.root = tk.Tk()
        self.root.title("Sequence Game")
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.buttons = []
        self.sequence = []
        self.user_sequence = []
        self.round = 0

        for i in range(4):
            button = tk.Button(self.frame, width=10, height=5, command=lambda i=i: self.click(i))
            button.grid(row=0, column=i)
            self.buttons.append(button)

        self.start_round()

    def start_round(self):
        self.sequence.append(random.randint(0, 3))
        for i in self.sequence:
            self.buttons[i].config(relief="sunken")
            self.root.update_idletasks()
            self.root.after(500)
            self.buttons[i].config(relief="raised")
            self.root.update_idletasks()
            self.root.after(500)

    def click(self, i):
        self.user_sequence.append(i)
        if self.user_sequence != self.sequence[:len(self.user_sequence)]:
            self.game_over()
        elif len(self.user_sequence) == len(self.sequence):
            self.round += 1
            self.user_sequence = []
            self.start_round()

    def game_over(self):
        self.root.title("Game Over! Your score was " + str(self.round))
        for button in self.buttons:
            button.config(state="disabled")

    def run(self):
        self.root.mainloop()

if name == "main":
    game = SequenceGame()
    game.run()