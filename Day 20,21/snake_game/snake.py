from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# create snake body of size 3 squares
class Snake:

    def __init__(self):
        self.new_snake = []
        self.create_snake()
        self.head = self.new_snake[0]   # head of the snake


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_length(position)


    def add_length(self, position):
        snake_segment = Turtle(shape="square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.new_snake.append(snake_segment)

    def grow_snake(self):
        self.add_length(self.new_snake[-1].position())


    def move(self):
        for seg_num in range(len(self.new_snake)-1,0,-1): # (start, stop, step)
            new_x = self.new_snake[seg_num - 1].xcor() # to make the snake body follow the head, move the body to the position of head and follow by making 2nd segment move into first and so on
            new_y = self.new_snake[seg_num - 1].ycor()
            self.new_snake[seg_num].goto(new_x,new_y) # this makes the body follow head's path by moving into head's previous coordinates
        self.new_snake[0].forward(MOVE_DISTANCE) # move the head to new position

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)