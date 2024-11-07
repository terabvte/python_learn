from turtle import Turtle, Screen
import pandas as pd

class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()

    def writes(self, x, y, state):
        self.goto(x, y)
        self.write(state)


turtle = Turtle()
screen = turtle.Screen()
screen.setup(700, 500, 650, 250)
screen.title("U.S. States Game")
image = "./100Days/intermediates/day-25/us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
write = Writer()

def get_mouse_click_coor(x, y):
    print(x, y)


df = pd.read_csv("./100Days/intermediates/day-25/us-states-game/50_states.csv")
# print(df)

states_list = df.values.tolist()
# print(states_list)
# print(states_list)

score = 0

while score != 50:
    answer = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

    if answer == states_list[0:51]:
        write.writes()


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
