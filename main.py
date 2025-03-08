import time
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increment_score()

    # Detect collision with wall.
    if (snake.head.xcor() <= -250 or snake.head.ycor() <= -250 or
        snake.head.xcor() >= 250 or snake.head.ycor() >= 250):
        score.reset_score()
        snake.reset_snake()

    # Detect collision with tail.
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()