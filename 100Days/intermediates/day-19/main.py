from turtle import Turtle, Screen

tt = Turtle()
screen = Screen()

tt.width(2.5)


def move_forwards():
    tt.fd(50)


def move_backwards():
    tt.bk(50)


def turn_counter_clockwise():
    tt.lt(25)
    


def turn_clockwise():
    tt.rt(25)


def clear_drawing():
    tt.clear()


screen.listen()

screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_counter_clockwise, "a")
screen.onkey(turn_clockwise, "d")
screen.onkey(clear_drawing, "c")


screen.exitonclick()
