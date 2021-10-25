import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
screen.listen()
screen.onkey(fun=player.move, key="w")
scoreboard = Scoreboard()

game_is_on = True
n = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Generate cars
    if n % 6 == 0:
        cars.generate()
    cars.move()

    # Level up Condition
    if player.ycor() > 280:
        scoreboard.level_up()
        player.restart()
        cars.level_up()

    # Car collision
    for car in cars.cars:
        if car.distance(player) <20:
            scoreboard.game_over()
            game_is_on = False

    n += 1

screen.exitonclick()
