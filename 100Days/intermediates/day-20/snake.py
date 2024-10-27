# Step 4: OOP Refactoring 
from turtle import Turtle, Screen
class Snake():

    def __init__(self):
        self.screen = Screen()
        self.snake = [Turtle() for i in range(3)]
        self.last_position = [0, 0]
        
        for segment in self.snake:
            segment.shape("square")
            segment.color("white")
            segment.pu()
            segment.shapesize(0.5, 0.5, 0.5)
            segment.speed(1)
            segment.goto(self.last_position)
            self.last_position[0] -= 10
        self.screen.update()  

    def move(self):
        i = 0
        positions = [seg.pos() for seg in self.snake]
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(positions[i - 1])
        
        self.screen.listen()
        self.screen.onkey(self.up, "w")
        self.screen.onkey(self.down, "s")
        self.screen.onkey(self.left, "a")
        self.screen.onkey(self.right, "d")

        self.snake[0].forward(10)

    def up(self):
        self.snake[0].seth(90)


    def down(self):
        self.snake[0].seth(270)


    def left(self):
        self.snake[0].seth(180)


    def right(self):
        self.snake[0].seth(0)
