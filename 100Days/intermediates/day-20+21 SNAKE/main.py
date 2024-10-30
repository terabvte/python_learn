from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

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
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:

        food.refresh()
        scoreboard.increment_score()
        snake.extend()

    # Detect collision with wall
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    # for segment in snake:
    #     # if segment == snake.snake.head:
    #     #     pass
    #     if snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()


screen.exitonclick()
