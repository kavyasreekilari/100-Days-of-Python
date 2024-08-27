import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# setup screen for the game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # to off the screen animation


snake = Snake() # create snake from snake class
food = Food() # create food from food class
scoreboard = Scoreboard() # create scoreboard for the game

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# move snake forward
game_is_on = True
while game_is_on:
    screen.update() # updates the screen after all the segments are moved instead of one square at a time
    time.sleep(0.1)  # adds 1 second delay between movement of snake
    snake.move()    # call move method from snake

    # Detect contact between snake and food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow_snake()
        scoreboard.increase_score()

    # Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision of head with any segment in the tail
    for segment in snake.new_snake[1:]:
        # if segment == snake.head:
        #     pass
        # elif (
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


# exit screen
screen.exitonclick()