from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600, 650, 250)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


def up():
    snake[0].seth(90)


def down():
    snake[0].seth(270)


def left():
    snake[0].seth(0)


def right():
    snake[0].seth(180)


# Step 1: Create Snake Body

snake = [Turtle() for i in range(60)]
last_position = [0, 0]
for segment in snake:
    segment.shape("square")
    segment.color("white")
    segment.pu()
    segment.shapesize(0.5, 0.5, 0.5)
    segment.speed(1)
    segment.goto(last_position)
    last_position[0] -= 10
    # start_line[1] += 45

screen.update()

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
