from turtle import Turtle, Screen

jim = Turtle()
screen = Screen()

def move_forwards():
    jim.forward(10)

def move_backwards():
    jim.backward(10)

def turn_counter_clockwise():
    jim.left(10)

def turn_clockwise():
    jim.right(10);

def clear_screen():
    jim.clear()
    jim.pu()
    jim.home()
    jim.pd()

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_counter_clockwise)
screen.onkey(key='d', fun=turn_clockwise)
screen.onkey(key='c', fun=clear_screen)
screen.exitonclick()