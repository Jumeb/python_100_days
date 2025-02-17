import turtle

import pandas

screen = turtle.Screen()
screen.title("US state Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)


data = pandas.read_csv("50_states.csv")

correct_states = []

while len(correct_states) != 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 States", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [n for n in data.state.to_list() if n not in correct_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in data.state.to_list():
        correct_states.append(answer_state.title())
        state_data = data[data.state == answer_state]
        tim = turtle.Turtle()
        tim.hideturtle() 
        tim.pu()
        tim.goto(x=int(state_data.x), y=int(state_data.y))
        tim.write(answer_state, move=False, align='center', font=("Courier", 10, "normal"))




turtle.mainloop()