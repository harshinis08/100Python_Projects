import turtle
import turtle as t

import pandas
import pandas as pd

screen = t.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"

screen.addshape(image)
t.shape(image)

guessed_states = []

df = pd.read_csv('50_states.csv')
states = df.state.to_list()


while len(guessed_states) < 50:
    user_input = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                  prompt="What's another state name? ").title()
    if user_input == 'Exit':
        missing_states = [state_name for state_name in states if state_name not in guessed_states]

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if user_input in states:
        guessed_states.append(user_input)
        tim = t.Turtle()
        tim.hideturtle()

        row = df[df.state == user_input]
        tim.penup()
        tim.goto(int(row.x), int(row.y))
        tim.write(user_input)

screen.mainloop()
