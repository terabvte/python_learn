from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("My Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600, startx=650, starty=250)
screen.tracer(0)

R_PADDLE_POSITION = (350, 0)
L_PADDLE_POSITION = (-350, 0)

r_paddle = Paddle(R_PADDLE_POSITION)
l_paddle = Paddle(L_PADDLE_POSITION)

ball = Ball()
# d
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:

    ball.move()
    screen.update()
    time.sleep(0.005)

    # Detect collision with TOP and BOTTOM wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # Detect collision with LEFT and RIGHT wall
    if ball.xcor() > 385 or ball.xcor() < -385:
        game_is_on = False

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325:
        ball.bounce_x()

    # Detect collision with l_paddle

    if ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()
screen.exitonclick()
