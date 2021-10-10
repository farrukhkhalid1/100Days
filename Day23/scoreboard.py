from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-270, 270)
        self.level = 1
        self.update()

    def update(self):
        self.write(arg=f"Level: {self.level}", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(-30, 0)
        self.write(arg="Game Over", font=FONT)
