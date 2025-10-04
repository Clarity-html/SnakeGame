from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# Border Setup
t = Turtle()
t.penup()
t.hideturtle()
t.color("white")
t.goto(-300, 240)
t.pendown()
for _ in range(4):
    t.forward(600)
    t.right(90)

# Game Components
snake = Snake()
food = Food()
scoreboard = Scoreboard()
food.spawn_food()

# Game Controls
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

# Game Loop
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move_forward()

    if scoreboard.score > scoreboard.high_score: # If the session score is higher than the high score, the game will do a live update of the high score
        scoreboard.reset()

    if snake.SNAKE_HEAD.distance(food) < 15: # Collision detection to check if the snake head has made contact with food
        snake.extend_snake()
        food.spawn_food()
        scoreboard.increase_score()

    if snake.SNAKE_HEAD.xcor() >= 295 or snake.SNAKE_HEAD.xcor() <= -295 or snake.SNAKE_HEAD.ycor() >= 240 or snake.SNAKE_HEAD.ycor() <= -300: # Collision detection to check if the snake is out of bounds
        scoreboard.clear_session_score()
        snake.reset()

    for seg in snake.all_segments[1:]: # Collision detection to check if the snake head has collided with the rest of its body: excluding the snake head itself
        if snake.SNAKE_HEAD.distance(seg) < 15:
            scoreboard.clear_session_score()
            snake.reset()
screen.exitonclick()



