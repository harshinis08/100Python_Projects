import turtle
import random

tim = turtle.Turtle()

colors = ["coral", "goldenrod3", "firebrick3", "DodgerBlue1", "brown3", "DarkOrange1", "CornflowerBlue"]

# tim.shape("turtle")
# tim.color("coral")

for side in range(4, 10):
    angle = 360/side
    tim.color(random.choice(colors))

    for i in range(side):
        tim.forward(70)
        tim.right(angle)





# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)

screen = turtle.Screen()
screen.exitonclick()