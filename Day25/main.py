import turtle
from states import States

screen = turtle.Screen()
screen.title("US States")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = States()

while len(states.all_guessed_states) < 50:

    answer = screen.textinput(title=f"{states.score}/50 states Correct",
                              prompt="What is another state name?: ", ).title()
    states.update(answer)
    if answer == "Exit":
        break
