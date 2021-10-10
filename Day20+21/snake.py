from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.allboxes =[]
        self.create_snake()
        self.head = self.allboxes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        box = Turtle("square")
        box.color("white")
        box.penup()
        box.goto(position)
        self.allboxes.append(box)

    def extend(self):
        self.add_segment(self.allboxes[-1].position())

    def move(self):
        for box in range(len(self.allboxes) - 1, 0, -1):
            new_x = self.allboxes[box - 1].xcor()
            new_y = self.allboxes[box - 1].ycor()
            self.allboxes[box].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)