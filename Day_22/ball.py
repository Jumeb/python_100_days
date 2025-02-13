from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.goto(0,0)
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
    
    def detect_wall_vertical(self):
        if self.ycor() > 290 or self.ycor() < -290:
            return True
        
    def detect_wall_horizontal(self):
        if self.xcor() > 390 or self.xcor() < -390:
            return True
        
    def bounce(self):
        self.y_move *= -1
    
    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.bounce_paddle
        self.move_speed = 0.1