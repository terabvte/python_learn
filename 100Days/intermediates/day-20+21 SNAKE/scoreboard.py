from turtle import Turtle

ALIGNMENT = "center"
FONT = ("DejaVu Sans Mono", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0

        self.hideturtle()
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Score = {self.score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def game_over(self):
        self.goto(0, 0)
        self.write(
            f"GAME OVER",
            align=ALIGNMENT,
            font=("DejaVu Sans Mono", 16, "normal"),
        )

    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_score()
