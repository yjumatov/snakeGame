from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import turtle


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SnakeGame 1.0")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
food = Food()
score = ScoreBoard()
game_on = True
while game_on:
    score
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extended()
        score.add_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.end_game()
        game_on = False
for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
        score.end_game()
        game_on = False
screen.exitonclick()
