from turtle import Turtle, Screen
import time

screen = Screen()

 # Setup window
screen = Screen()
screen.setup(600, 600, 650, 250)
screen.bgcolor("black")
screen.title("Snake Game")
# Set it so the window updates only when .update() is called
screen.tracer(0)

# Step 1: Create Snake Body

snake = [Turtle() for i in range(3)]
last_position = [0, 0]

# Step 2: Animating snake segments

i = 0

screen.listen()
screen.onkey(right, "a")
screen.onkey(left, "d")
screen.onkey(up, "w")
screen.onkey(down, "s")

while True:
    screen.update()
    time.sleep(0.05)

    positions = [seg.pos() for seg in snake]
    for i in range(len(snake) - 1, 0, -1):
        snake[i].goto(positions[i - 1])

    snake[0].forward(10)


screen.exitonclick()
