import random
import turtle as t
from turtle import Screen

tim = t.Turtle()
direction = [0, 90, 180, 270]
t.colormode(255)
tim.speed("fastest")

tim.width(5)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(100):
    tim.color(random_color())
    tim.forward(25)
    tim.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()