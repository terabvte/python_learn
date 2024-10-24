from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

for i in range(15):
    turtle.fd(10)
    turtle.up()
    turtle.fd(10)
    turtle.pd()


screen.exitonclick()
