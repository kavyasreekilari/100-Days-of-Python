from random import random
import turtle as t
import random


# using class alias name
tom = t.Turtle()

tom.shape("turtle")
tom.color("green")

# change colormode for turtle module t
t.colormode(255)
colors = ["DeepSkyBlue", "DarkOrchid", "aquamarine", "beige", "red", "DarkSeaGreen1", "goldenrod", "MistyRose", "SlateGray", "violet", "wheat"]
directions = [0, 90, 180, 270]
tom.pensize(20)
tom.speed("fastest")

def random_rgd_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)  # tuple with rgb colors
    return random_color

def turtle_draw_square():
    for n in range(4):
        tom.forward(100)
        tom.right(90)

# turtle_draw_square()


def turtle_draw_dashed_line():
    for _ in range(15):
        tom.pendown()
        tom.forward(10)
        tom.penup()
        tom.forward(10)

# turtle_draw_dashed_line()

def turtle_draw_shapes():
    num_sides = 3
    while num_sides <= 10:
        angle = 360 / num_sides
        for _ in range(num_sides):
            tom.forward(100)
            tom.right(angle)
        num_sides += 1
        tom.color(random.choice(colors))

# turtle_draw_shapes()

def turtle_random_walk():
    for _ in range(100):
        tom.forward(50)
        tom.setheading(random.choice(directions))
        # tom.color(random.choice(colors)) # using random colors from colors list
        tom.color(random_rgd_color())

# turtle_random_walk()

# takes degree to shift as parameter
def turtle_draw_spirograph(size_of_gap):
    tom.pensize(1)
    for _ in range(int(360 / size_of_gap)):
        tom.color(random_rgd_color())
        tom.circle(100)
        current_heading = tom.heading()
        tom.setheading(current_heading + size_of_gap)

turtle_draw_spirograph(5) # shifts heading to 5 degrees





# exit screen on click
screen = t.Screen()
screen.exitonclick()