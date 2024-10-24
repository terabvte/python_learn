from turtle import Turtle, Screen
import random

tt = Turtle()
screen = Screen()

colors = [
    "alice blue", "antique white", "aqua", "aquamarine", "azure", "beige", 
    "bisque", "blanched almond", "blue", "blue violet", "brown", 
    "burlywood", "cadet blue", "chartreuse", "chocolate", "coral", 
    "cornflower blue", "cornsilk", "crimson", "cyan", "dark blue", 
    "dark cyan", "dark goldenrod", "dark gray", "dark green", "dark khaki", 
    "dark magenta", "dark olive green", "dark orange", "dark orchid", 
    "dark red", "dark salmon", "dark sea green", "dark slate blue", 
    "dark slate gray", "dark turquoise", "dark violet", "deep pink", 
    "deep sky blue", "dim gray", "dodger blue", "firebrick", "floral white", 
    "forest green", "gainsboro", "ghost white", "gold", "goldenrod", 
    "gray", "green", "green yellow", "honeydew", "hot pink", "indian red", 
    "indigo", "ivory", "khaki", "lavender", "lavender blush", "lawn green", 
    "lemon chiffon", "light blue", "light coral", "light cyan", 
    "light goldenrod yellow", "light gray", "light green", "light pink", 
    "light salmon", "light sea green", "light sky blue", "light slate gray", 
    "light steel blue", "light yellow", "lime", "lime green", 
    "linen", "magenta", "maroon", "medium aquamarine", "medium blue", 
    "medium orchid", "medium purple", "medium sea green", "medium slate blue", 
    "medium spring green", "medium turquoise", "medium violet red", 
    "midnight blue", "mint cream", "misty rose", "moccasin", "navajo white", 
    "navy", "old lace", "olive", "olive drab", "orange", "orange red", 
    "orchid", "pale goldenrod", "pale green", "pale turquoise", 
    "pale violet red", "papaya whip", "peach puff", "peru", "pink", 
    "plum", "powder blue", "purple", "red", "rosy brown", "royal blue", 
    "saddle brown", "salmon", "sandy brown", "sea green", "seashell", 
    "sienna", "silver", "sky blue", "slate blue", "slate gray", 
    "snow", "spring green", "steel blue", "tan", "teal", "thistle", 
    "tomato", "turquoise", "violet", "wheat", "white", "white smoke", 
    "yellow", "yellow green"
]

# Dotted line
# for i in range(15):
#     turtle.fd(10)
#     turtle.up()
#     turtle.fd(10)
#     turtle.pd()

screen.bgcolor("black")
tt.width(5)

# Multi polygon challenge
polygons = [3, 4, 5, 6, 7, 8, 9, 10]
for shape in polygons:
    angle = 360 / shape
    tt.color(random.choice(colors))
    i = shape
    while i != 0:
        tt.fd(100)
        tt.rt(angle)
        i -= 1
     
screen.exitonclick()
