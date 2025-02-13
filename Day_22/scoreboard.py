from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')

class ScoreBoard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color('white')
        self.pu()
        self.goto(position[0], position[1])
        self.write(f"{self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        scoreString = f"{self.score}"
        self.write(scoreString, move=False, align=ALIGNMENT, font=FONT)
