import random
import turtle as t

t.colormode(255)

colors = [(52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216)]

tim = t.Turtle()
tim.hideturtle()
tim.width(10)
tim.color("coral")
tim.speed("fastest")

tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

dots = 100


for dot_count in range(1, dots+1):

    tim.dot(20, random.choice(colors))
    tim.penup()
    tim.forward(50)
    tim.pendown()

    if dot_count % 10 == 0:
        tim.penup()
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()