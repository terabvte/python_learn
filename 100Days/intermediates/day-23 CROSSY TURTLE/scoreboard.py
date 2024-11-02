from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-280, 250)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        
        
        self.level = 1
        self.hideturtle()
        self.pu()
        self.goto(POSITION)
        self.write(f"Level {self.level}:", font=FONT)
        
    def increment_level(self):
        self.level +=1
        self.clear()
        self.write(f"Level {self.level}:", font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
    
