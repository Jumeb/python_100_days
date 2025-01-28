# import colorgram

# colors = colorgram.extract('image.jpeg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# print(rgb_colors)

import turtle as t
from random import choice

color_list = [(208, 161, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (45, 55, 104), (158, 46, 84), (168, 160, 39), (128, 189, 143), (84, 20, 44), (38, 42, 66), (187, 93, 105), (187, 139, 170), (84, 122, 181), (59, 39, 31), (79, 153, 165), (88, 157, 91), (196, 80, 72), (161, 202, 220), (45, 74, 77), (80, 73, 44), (57, 130, 123), (218, 176, 187), (220, 182, 167), (166, 207, 163)]

jimmy = t.Turtle();
t.colormode(255)


jimmy.speed(7)
jimmy.hideturtle()
for y in range(10):
    jimmy.teleport(-200, (y - 4)*50)
    for _ in range(10):
        jimmy.dot(20, choice(color_list))
        jimmy.pu()
        jimmy.forward(50)
        jimmy.pd()





screen = t.Screen()
screen.exitonclick()