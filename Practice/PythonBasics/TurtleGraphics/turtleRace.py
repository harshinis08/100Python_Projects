import random
import turtle as t

t.colormode(255)
screen = t.Screen()
user_bet = screen.textinput(title="Make your bet..", prompt="Which turtle will win the race? Pick a color: ")
screen.setup(width=600, height=500)
colors = ["coral", "goldenrod3", "firebrick3", "DodgerBlue1", "magenta", "DarkOrange1", "red"]
y_positions = [0, 50, -50, 100, -100, 150]
all_turtles = []


is_race_on = True

for i in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-250,y=y_positions[i])
    new_turtle.speed("fastest")
    all_turtles.append(new_turtle)


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 270:
            is_race_on = False
            print(turtle.pencolor())
            if user_bet == turtle.pencolor():
                print(f"You won! {turtle.pencolor()} is the winne")
            else:
                print(f"No you've lost! {turtle.pencolor()} won the race")
        dist = random.randint(0, 10)
        turtle.forward(dist)

screen.exitonclick()