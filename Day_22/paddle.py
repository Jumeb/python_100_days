from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, coords):
        super().__init__()
        self.shape('square')
        self.pu()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color('white')
        self.goto(x=coords[0], y=coords[1])
    
    def moveup(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def movedown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    # def movedown(self):
    #     for seg_num in range(0, len(self.segments)-1, 1):
    #         new_x = self.segments[seg_num-1].xcor()
    #         new_y = self.segments[seg_num-1].ycor()
    #         self.segments[seg_num].goto(new_x, new_y)
    #     self.tail.forward(MOVE_DISTANCE)