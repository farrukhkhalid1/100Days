from turtle import Turtle
import pandas

FILE = "50_states.csv"
FONT = ("Arial", 7, "normal")
NEW_FILE = "remaining states.csv"


class States(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.all_guessed_states = []
        self.all_states = []
        self.remaining_states = []

    def update(self, answer):
        data = pandas.read_csv(FILE)
        self.all_states = data.state.tolist()

        if answer in self.all_states:
            state_data = data[data.state == answer]
            self.goto(int(state_data.x), int(state_data.y))
            self.write(f"{state_data.state.item()}", font=FONT)
            self.score += 1
            self.all_guessed_states.append(answer)
        if answer == "Exit":
            self.exit()

    def exit(self):
        for state in self.all_states:
            if state not in self.all_guessed_states:
                self.remaining_states.append(state)
        new_data = pandas.DataFrame(self.remaining_states)
        new_data.to_csv(NEW_FILE)
