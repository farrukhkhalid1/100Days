import random
import turtle


screen = turtle.Screen()

screen.setup(height=400,width=500)
input = screen.textinput(title='Turtle race',prompt='Name the color of your turtle')
colors = ['red','green','brown','blue','orange','purple']
count = 0
y= -60
turtle_list =[]
race_on = True

for i in range(len(colors)):

    tim = turtle.Turtle(shape='turtle')
    tim.penup()
    tim.goto(x=-240, y=y)
    tim.color(colors[i])
    y+= 30
    turtle_list.append(tim)


while race_on:

    for turtle in turtle_list:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() > 220:
            race_on = False
            if turtle.color()[0] == input:
                print(f"You won.The turtle was {turtle.color()[0]}.")
            else:
                print(f"You lost.The winning color was {turtle.color()[0]}.")
            break

screen.exitonclick()
