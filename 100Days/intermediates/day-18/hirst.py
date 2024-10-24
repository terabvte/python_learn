import turtle as t
from turtle import Screen
import random


tt = t.Turtle()
screen = Screen()
t.colormode(255)

screen.setup(width=550, height=550) 

screen_width = screen.window_width() // 2
screen_height = screen.window_height() // 2

home_x = -screen_width + 50
home_y = -screen_height + 50


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

tt.speed(0)

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