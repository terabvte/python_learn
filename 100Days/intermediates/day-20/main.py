from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600, 650, 250)
screen.bgcolor("black")
screen.title("Snake Game")

# Step 1: Create Snake Body

snakes = [Turtle() for i in range(3)]
last_position = [0, 0]
for snake in snakes:
    snake.shape("square")
    snake.color("white")
    snake.pu()
    snake.shapesize(0.5, 0.5, 0.5)

    snake.goto(last_position)
    last_position[0] -= 10
    # start_line[1] += 45



screen.exitonclick()
