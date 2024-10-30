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
        
        self.l_score = 0
        self.r_score = 0

        # Draw divider
        for i in range(14):
            self.pd()
            self.fd(20)
            self.pu()
            self.fd(20)
            
        # self.pd()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
        
    def r_point(self):
        self.l_score += 1
        self.update_scoreboard()