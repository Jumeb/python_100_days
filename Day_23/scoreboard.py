from turtle import Turtle

FONT = ("Courier", 18, "normal")
ALIGNMENT = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color('black')
        self.pu()
        self.goto(-220, 250)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.score = 0
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.write_score()