import turtle as t
import time

screen = t.Screen()
screen.setup(width=600, height=500)
screen.bgcolor("black")
screen.title("Snake Game.....")
screen.tracer()

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    segment1 = t.Turtle("square")
    segment1.color("coral")
    segment1.penup()
    segment1.goto(position)
    segments.append(segment1)


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    for seg in range(len(segments) - 1, 0, -1):
        new_x = segments[seg - 1].xcor()
        new_y = segments[seg - 1].ycor()
        segments[seg].goto(new_x, new_y)

    segments[0].forward(20)

screen.exitonclick()
