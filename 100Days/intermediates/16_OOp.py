from turtle import Turtle, Screen

# Init Turtle object
jake = Turtle()
jake.shape("turtle")
jake.color("chartreuse4")
# Init Screen
my_screen = Screen()
print(my_screen.canvheight)
# Move jake by 100 paces forward
jake.forward(100)

my_screen.exitonclick()
