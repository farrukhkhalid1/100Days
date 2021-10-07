import colorgram
import turtle
import random

colors = colorgram.extract('art.png',39)
color_list =[]

for w in colors:

    color_list.append((w.rgb.r,w.rgb.g,w.rgb.b))

tim = turtle.Turtle()
screen = turtle.Screen()

tim.penup()
tim.speed("fastest")
turtle.colormode(255)
tim.hideturtle()

tim.setheading(220)
tim.forward(330)
tim.setheading(0)
dots = 0

for i in range(100):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    dots +=1
    if dots >= 10:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        dots = 0

screen.exitonclick()