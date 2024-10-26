# Step 4: OOP Refactoring 
from turtle import Turtle, Screen
import time

class Snake():

    def start(self):
        screen = Screen()
        # Initialize a range(x) list segments for the snake
        snake = [Turtle() for i in range(3)]
        last_position = [0, 0]
        # For loop which initializes the segments and positions them accordingly
        for segment in snake:
            segment.shape("square")
            segment.color("white")
            segment.pu()
            segment.shapesize(0.5, 0.5, 0.5)
            segment.speed(1)
            segment.goto(last_position)
            last_position[0] -= 10
        screen.update()


    #Step 3: Movement
    def up(self):
    snake[0].seth(90)


    def down(self):
    snake[0].seth(270)


    def left(self):
    snake[0].seth(0)


    def right(self):
    snake[0].seth(180)
