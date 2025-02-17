from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1) 
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increment_score() 
        snake.grow()
    
    if snake.check_wall_collision():
        # game_is_on = False
        # score.game_over()
        score.reset()
        snake.reset_snake()
    
    if snake.check_tail_collision():
        # game_is_on = False 
        # score.game_over() 
        score.reset()
        snake.reset_snake()









screen.exitonclick() 