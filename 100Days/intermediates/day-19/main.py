from turtle import Turtle, Screen
import random


def movement(turtle):
    turtle.fd(random.randint(0, 10))


screen = Screen()
screen.setup(500, 400)
# tt.width(2.5)


# def move_forwards():
#     tt.fd(50)


# def move_backwards():
#     tt.bk(50)


# def turn_counter_clockwise():
#     tt.lt(25)


# def turn_clockwise():
#     tt.rt(25)


# def clear_drawing():
#     tt.clear()


# screen.listen()

# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_counter_clockwise, "a")
# screen.onkey(turn_clockwise, "d")
# screen.onkey(clear_drawing, "c")

bet = screen.textinput("Make your bet", "Who's gonna win?")

turtles = [Turtle() for i in range(6)]
finish_turtles = [Turtle() for i in range(6)]
colors = ["red", "orange", "turquoise", "green", "blue", "purple"]
start_line = [-225, -100]
finish_line = [205, -100]
i = 0
for turtle in turtles:
    turtle.shape("turtle")
    turtle.color(colors[i])
    turtle.pu()
    turtle.shapesize(2, 2, 2)
    turtle.goto(start_line)
    start_line[1] += 45
    i += 1

# for finish in finish_turtles:
#     finish.shape("turtle")
#     finish.color("black")
#     finish.pu()
#     finish.shapesize(2, 2, 2)
#     finish.goto(finish_line)
#     finish_line[1] += 45
#     i += 1

while True:
    if turtle.xcor() > finish_line[0]:
        winner = turtle.pencolor()
        if winner == bet:
            print(f"You've won! The {winner.title()} turtle is the winner!")
        else:
            print(f"You've lost... The {winner.title()} turtle is the winner!")
    for turtle in turtles:
        movement(turtles[random.randint(0, 5)])

    
# if bet == colors.find(winner): print("You bet correctly")
# else: print(f"Unlucky... the winner was {colors[winner]}")