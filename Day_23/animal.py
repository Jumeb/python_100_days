from turtle import Turtle

class Animal(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('teal')
        self.pu()
        self.reset_animal()
        self.left(90)


    def reset_animal(self):
        self.goto(0, -280)

    def moveup(self):
        self.forward(10)

    def movedown(self):
        self.backward(10)