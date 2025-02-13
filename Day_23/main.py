from turtle import Screen
import time

from animal import Animal
from scoreboard import ScoreBoard
from cars import Cars

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('white')
screen.title('Turtle Crossing')
screen.listen()

animal = Animal()
level = ScoreBoard()
cars = Cars()

game_is_on = True

screen.onkey(animal.moveup, 'Up')
screen.onkey(animal.movedown, 'Down')

while game_is_on:
    screen.update()
    time.sleep(0.1)



    if animal.ycor() >= 280:
        animal.reset_animal()
        level.increment_score()
        cars.increase_speed()

    cars.create_car()
    cars.move_cars()

    for car in cars.cars:
        if car.xcor() > -20 and car.xcor() < 20 and animal.distance(car) < 20:
            level.game_over()
            game_is_on = False








screen.exitonclick()