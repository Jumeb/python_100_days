from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.pu()
        self.goto(-250, 270)
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        scoreString = f"Score: {self.score}"
        self.write(scoreString, move=False, align=ALIGNMENT, font=FONT)
