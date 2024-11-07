import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600, startx=650, starty=250)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkeypress(fun=player.move, key="space")

car_manager = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:


    time.sleep(0.05)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # If player hits car
    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()



    # If player reaches end of level
    if player.ycor() > 285:
        player.reset()
        car_manager.speedy()
        scoreboard.increment_level()


screen.exitonclick()
