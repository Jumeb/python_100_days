from turtle import Turtle;
from random import choice

MOVE_DISTANCE = 20
COLORS = ['white', 'teal', 'blue', 'violet', 'purple', 'yellow', 'orange']

class Snake :
    def __init__(self):
        self.segments = []
        self.heading = 0
        self.create_snake()
        self.head = self.segments[0]

    
    def create_snake(self):
        for index in range(0, 3):
            new_segment = Turtle('square')
            new_segment.pu()
            new_segment.color(choice(COLORS))
            new_segment.goto(x=(index*-20), y=0)
            self.segments.append(new_segment)

    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def left(self):
       if self.heading != 0:
            self.heading = 180 
            self.head.setheading(self.heading)
    
    def right(self):
       if self.heading != 180:
            self.heading = 0 
            self.head.setheading(self.heading)

    def up(self):
       if self.heading != 270:
            self.heading = 90 
            self.head.setheading(self.heading)
    def down(self):
       if self.heading != 90:
            self.heading = 270 
            self.segments[0].setheading(self.heading)

    def grow(self):
        new_segment = Turtle('square')
        new_segment.pu()
        new_segment.color(choice(COLORS))
        x_cor = self.segments[-1].xcor()
        y_cor = self.segments[ -1].ycor()
        new_segment.goto(x=x_cor, y=y_cor)
        self.segments.append(new_segment)

    def check_wall_collision(self):
        if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
            return True
    
    def check_tail_collision(self):
        for segment in self.segments[2:]:
            if self.head.distance(segment) < 10:
                return True
    
    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

