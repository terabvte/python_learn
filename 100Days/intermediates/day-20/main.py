from turtle import Screen
import time
from snake import Snake
from food import Food
# Setup window
screen = Screen()
screen.setup(600, 600, 650, 250)
screen.bgcolor("black")
screen.title("Snake Game")
# Set it so the window updates only when .update() is called
screen = Screen()
screen.tracer(0)

snake = Snake()
food = Food()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()


screen.exitonclick()
