from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.pu()
        self.goto(position)
        
        self.score = 0
        
    def go_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

    def go_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)

    # def scoreboard(self)