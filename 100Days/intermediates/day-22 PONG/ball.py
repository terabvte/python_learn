from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(1, 1)
        self.speed(1)
        self.pu()
        self.x_move = 1.5
        self.y_move = 2.0
        # self.goto(position)

    def move(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        
    def respawn(self):
        self.goto(0, 0)
