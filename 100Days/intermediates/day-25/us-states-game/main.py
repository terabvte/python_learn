from turtle import Turtle, Screen
import pandas as pd


turtle = Turtle()
screen = Screen()
screen.setup(700, 500, 650, 250)
screen.title("U.S. States Game")
image = "./100Days/intermediates/day-25/us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
write = Turtle()
write.pu()
write.hideturtle()

def get_mouse_click_coor(x, y):
    print(x, y)


df = pd.read_csv("./100Days/intermediates/day-25/us-states-game/50_states.csv")
# print(df)

states_list = df.values.tolist()
# print(states_list)

score = 0
while score != 50:
    answer = screen.textinput(title=f"Guess the State ({score}/50)", prompt="What's another state's name?").title()

    for state in states_list:
        if answer == state[0]:
            x, y = state[1], state[2]
            write.goto(x, y)
            write.write(answer)
            print("yeah that one's in")
            score += 1
            break

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
