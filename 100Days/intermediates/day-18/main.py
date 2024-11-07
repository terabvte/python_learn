import turtle as t
from turtle import Screen
import random
# import colorgram

tt = t.Turtle()
screen = Screen()
t.colormode(255)

# Resize the screen window (optional, but recommended)
screen.setup(width=550, height=550, startx=650, starty=250)  # Set the width and height as needed

# Get screen dimensions (this returns the width/2 and height/2)
screen_width = screen.window_width() // 2
screen_height = screen.window_height() // 2

# # Move the turtle to the bottom-left corner
# tt.penup()  # Lift the pen to avoid drawing a line while moving
# tt.setposition()  # Set to the bottom-left corner
# tt.pendown()  # Put the pen down to start drawing

home_x = -screen_width + 50
home_y = -screen_height + 50


# palette = colorgram.extract("./100Days/intermediates/day-18/hirst_spots.jpeg", 25)
# my_colors = []
# for color in palette:
#     my_colors.append(color.rgb)

color_list = [
    (198, 175, 119),
    (125, 36, 23),
    (187, 157, 50),
    (170, 104, 56),
    (5, 56, 83),
    (201, 216, 205),
    (109, 67, 85),
    (39, 35, 34),
    (84, 141, 61),
    (20, 122, 175),
    (111, 161, 176),
    (75, 38, 48),
    (8, 67, 47),
    (65, 154, 134),
    (132, 41, 43),
    (184, 98, 81),
    (183, 180, 181),
    (210, 200, 108),
    (178, 201, 186),
    (150, 180, 170),
    (90, 143, 158),
    (28, 81, 59),
]

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     colors = (r, g, b)
#     return colors


# Dotted line
# for i in range(15):
#     turtle.fd(10)
#     turtle.up()
#     turtle.fd(10)
#     turtle.pd()

# Init (bruv) screen
# screen.bgcolor("black")
# tt.shape("circle")
tt.speed(0)
tt.hideturtle()
# tt.color("white")

# Multi polygon challenge
# polygons = [3, 4, 5, 6, 7, 8, 9, 10]
# for shape in polygons:
#     angle = 360 / shape
#     tt.color(random.choice(colors))
#     i = shape
#     while i != 0:
#         tt.fd(100)
#         tt.rt(angle)
#         i -= 1

# My take on random walk:
# while True:

#     direction = random.randint(0, 3)

#     if direction == 0:
#         tt.fd(25)
#         tt.rt(90)
#         tt.color(random.choice(colors))
#     elif direction == 1:
#         tt.bk(25)
#         tt.rt(90)
#         tt.color(random.choice(colors))

# Random walk solution:
# directions = [0, 90, 180, 270]

# for i in range(200):
#     tt.color(random_color())
#     tt.fd(30)
#     tt.setheading(random.choice(directions))

# Spirograph
# for i in range(200):
#     tt.circle(175)
#     tt.tiltangle(50)
#     tt.lt(10)
#     tt.color(random_color())

# Final challenge:

# tt.width(5)

# for i in range(10):
#     tt.pd()
#     tt.fillcolor(random.choice(color_list))
#     tt.begin_fill()
#     # tt.color(random.choice(color_list))
#     tt.circle(20)
#     tt.end_fill
#     tt.pu()
#     tt.fd(50)


for i in range(10):
    tt.teleport(home_x, home_y)
    for i in range(10):
        tt.pd()
        chosen_color = random.choice(color_list)
        tt.fillcolor(chosen_color)
        tt.begin_fill()

        tt.color(chosen_color)

        tt.circle(10)
        tt.end_fill()
        tt.pu()
        tt.fd(50)
    home_y += 50

screen.exitonclick()
