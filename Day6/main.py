# Maze -Reeborg.ca
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        if front_is_clear():
            move()
    elif wall_in_front():
        turn_left()
        if front_is_clear():
            move()
    elif front_is_clear():
        move()

