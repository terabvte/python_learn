from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "turquoise", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2.5
X_AXIS = 300


class CarManager():
    def __init__(self):

        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.pu()
            new_car.color(random.choice(COLORS))
            new_car.seth(180)
            new_car.goto(x=X_AXIS, y=random.randint(-270, 270))
            self.all_cars.append(new_car)
        
    def move_car(self):
        for car in self.all_cars:
            car.fd(self.car_speed)
            
    def speedy(self):
        self.car_speed += MOVE_INCREMENT
