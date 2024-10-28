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
            segment.shapesize(0.7, 0.7, 0.7)
            segment.speed(1)
            segment.goto(self.last_position)
            self.last_position[0] -= 10
        self.head = self.snake[0]
        self.screen.update()  

    def move(self):
        i = 0
        positions = [seg.pos() for seg in self.snake]
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(positions[i - 1])

        # HUUUGE bug, "w" is case sensitive...
        # thought i was going crazy        
        self.screen.listen()
        self.screen.onkeypress(self.up, "w")
        self.screen.onkeypress(self.down, "s")
        self.screen.onkeypress(self.left, "a")
        self.screen.onkeypress(self.right, "d")

        # uppercase to fix case sensitive bug

        self.screen.onkeypress(self.up, "W")
        self.screen.onkeypress(self.down, "S")
        self.screen.onkeypress(self.left, "A")
        self.screen.onkeypress(self.right, "D")

        self.head.forward(10)

    def up(self):
        self.head.seth(90)


    def down(self):
        self.head.seth(270)


    def left(self):
        self.head.seth(180)


    def right(self):
        self.head.seth(0)