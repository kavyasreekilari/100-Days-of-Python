from turtle import Turtle, Screen
tom = Turtle()
screen = Screen()

def moves_forward():
    tom.forward(10)

def moves_backward():
    tom.backward(10)

def move_clockwise():
    tom.right(10)

def move_anticlockwise():
    new_heading = tom.heading() + 10
    tom.setheading(new_heading)

def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.listen()
screen.onkey(key="w",fun=moves_forward)
screen.onkey(key="s", fun=moves_backward)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a",fun=move_anticlockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
