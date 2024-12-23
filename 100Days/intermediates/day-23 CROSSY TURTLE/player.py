from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        
        self.seth(90)
        self.pu()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        
        
        
    def move(self):
        self.fd(MOVE_DISTANCE)
        
    def reset(self):
        self.goto(STARTING_POSITION)