from turtle import Turtle, Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)

r_paddle = Paddle((350, 0))
r_score = ScoreBoard((90, 190))
l_paddle = Paddle((-350, 0))
l_score = ScoreBoard((-90, 190))

ball = Ball()
screen.listen()

screen.onkey(r_paddle.moveup, 'Up')
screen.onkey(r_paddle.movedown, 'Down')
screen.onkey(l_paddle.moveup, 'w')
screen.onkey(l_paddle.movedown, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.detect_wall_vertical():
        ball.bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        l_score.increment_score()

    if ball.xcor() < -380:
        ball.reset_position()
        r_score.increment_score()

    if r_paddle.distance(ball) < 50 and ball.xcor() > 320 or l_paddle.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()






screen.exitonclick()