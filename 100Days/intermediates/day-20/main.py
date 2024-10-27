from turtle import Turtle, Screen
import time
from snake import Snake
# Setup window
screen = Screen()
screen.setup(600, 600, 650, 250)
screen.bgcolor("black")
screen.title("Snake Game")
# Set it so the window updates only when .update() is called
screen = Screen()
screen.tracer(0)

snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.01)

    snake.move()

screen.exitonclick()
