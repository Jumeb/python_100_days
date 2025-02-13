from turtle import Turtle
import random 

COLORS = ['black', 'teal', 'blue', 'violet', 'purple', 'yellow', 'orange']
MOVE_INCREMENT = 10
START_MOVE_DISTANCE = 5

class Cars:
    def __init__(self):
        self.cars = []
        self.speed = START_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 3:
            new_car = Turtle('square')
            new_car.pu()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(x=300, y=random.randint(-250, 270))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
