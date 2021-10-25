from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []
        self.hideturtle()

    def generate(self):
        self.car = Turtle(shape="square")
        self.car.penup()
        self.car.color(random.choice(COLORS))
        self.car.shapesize(stretch_wid=1, stretch_len=2)
        self.car.goto(300, random.randint(-250, 250))
        self.cars.append(self.car)

    def move(self):
        for self.car in self.cars:
            if self.car.xcor() > -320:
                self.car.backward(self.car_speed)
            else:
                self.car.clear()
                self.cars.remove(self.car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


