from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier',24,'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(arg=f"score: {self.score}",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over",align=ALIGNMENT,font=FONT)



