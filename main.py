import random
import turtle as turtle_module
from turtle import Screen

color_list = [(197, 166, 112), (141, 77, 54), (233, 235, 241), (235, 242, 236), (73, 98, 124), (158, 148, 54),
               (214, 203, 144), (120, 39, 28), (137, 160, 179), (70, 108, 76), (144, 175, 141), (72, 49, 42),
               (194, 93, 73), (97, 82, 89), (60, 51, 55), (224, 177, 164), (159, 143, 158), (101, 142, 126),
               (98, 129, 163), (49, 61, 84), (108, 138, 142), (72, 68, 49), (45, 55, 72), (110, 37, 41),
               (181, 200, 182), (176, 98, 102), (49, 76, 65), (179, 190, 208)]

tom = turtle_module.Turtle()
turtle_module.colormode(255)

tom.penup()
tom.hideturtle()
tom.setheading(225)
tom.forward(300)
tom.setheading(0)

number_of_dots = 100

for _ in range(1, number_of_dots + 1):
    tom.dot(20, random.choice(color_list))
    tom.forward(50)

    if _ % 10 == 0:
        tom.setheading(98)
        tom.forward(58)
        tom.setheading(180)
        tom.forward(490)
        tom.setheading(0)


screen = Screen()
screen.exitonclick()
