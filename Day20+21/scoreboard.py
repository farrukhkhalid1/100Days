from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier',24,'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("highscore.txt",'r') as file:
            self.high_score = int(file.read())
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(arg=f"score: {self.score} High score: {self.high_score}",align=ALIGNMENT,font=FONT)
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def write_score(self):
        with open("highscore.txt",'w') as file:
            file.write(f"{self.high_score}")




