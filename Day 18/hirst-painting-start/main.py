###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import random
import time

import colorgram
import turtle as t

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tom = t.Turtle()
t.colormode(255)
tom.speed("fastest")
tom.penup()
tom.hideturtle()



def hirst_painting(dots):
    tom.setheading(255)
    tom.forward(300)
    tom.setheading(0)
    number_of_dots = dots

    for dot_count in range(1, dots + 1):
        tom.dot(20, random.choice(color_list))
        tom.penup()
        tom.forward(50)

         # start from spot 1 again
        if dot_count % 10 == 0:
            tom.setheading(90)
            tom.forward(50)
            tom.setheading(180)
            tom.forward(500)
            tom.setheading(0)



hirst_painting(100)

screen = t.Screen()
screen.exitonclick()
