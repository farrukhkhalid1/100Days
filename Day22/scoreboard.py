from turtle import Turtle

FONT = ("Arial", 30, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score_left = 0
        self.score_right = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-60, 250)
        self.write(arg=f"{self.score_left}", font=FONT, align=ALIGNMENT)
        self.goto(60, 250)
        self.write(arg=f"{self.score_right}", font=FONT, align=ALIGNMENT)

    def l_score(self):
        self.score_left += 1
        self.update_score()

    def r_score(self):
        self.score_right += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", font=FONT, align=ALIGNMENT)
