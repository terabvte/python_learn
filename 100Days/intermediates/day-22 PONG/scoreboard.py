from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        
        
        self.shape("square")
        self.color("white")
        self.pensize(5)
        self.hideturtle()
        self.seth(90)
        self.pu()
        self.goto(0, -270)
        self.pd()
        
        # for i in range(6):
        #     self.pd()
        #     self.fd(10)
        #     self.pu() 
        #     self.fd(10)