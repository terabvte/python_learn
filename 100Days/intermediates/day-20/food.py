from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        random_coords = [random.randint(-280, 280), random.randint(-280, 280)]
        self.goto(random_coords)

    def refresh(self):
        random_coords = [random.randint(-280, 280), random.randint(-280, 280)]
        self.goto(random_coords)