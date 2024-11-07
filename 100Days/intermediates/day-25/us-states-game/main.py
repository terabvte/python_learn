import turtle

screen = turtle.Screen()
screen.setup(700, 500, 650, 250)
screen.title("U.S. States Game")
image = "./100Days/intermediates/day-25/us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


screen.exitonclick()
