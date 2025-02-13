from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0 
        self.read_high_score()
        self.color('white')
        self.pu()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def write_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def read_high_score(self):
        with open("high_score.txt") as file:
            self.high_score = int(file.read())

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        scoreString = f"Score: {self.score} High score: {self.high_score}"
        self.write(scoreString, move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()
        
