import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-380, 0))
right_paddle = Paddle((370, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_spead)

    ball.move()

    # detect collision with upper/lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(right_paddle) < 60 and ball.xcor() > 330 or ball.distance(left_paddle) < 60 and ball.xcor() < -340:
        ball.bounce_x()

    # detect collision with right wall
    if ball.xcor() > 390:
        scoreboard.r_score()
        ball.refresh()

    # detect collision with left wall
    if ball.xcor() < -390:
        scoreboard.l_score()
        ball.refresh()

    if scoreboard.score_left == 10 or scoreboard.score_right == 10:
        game_on = False
        scoreboard.game_over()

screen.exitonclick()
