import turtle as t

jimmy = t.Turtle()
t.colormode(255)
jimmy.shape('turtle')
from random import choice, randint

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)



# for _ in range(4):
#     jimmy.forward(150)
#     jimmy.right(90)

# jimmy.left(90)
# jimmy.penup()
# jimmy.color('teal')
# jimmy.forward(100)
# jimmy.left(90)
# jimmy.forward(300)
# jimmy.right(180)


# for _ in range(50):
#     jimmy.pd()
#     jimmy.forward(5)
#     jimmy.pu()
#     jimmy.forward(5)

# sides = 3
colors = ["green", "blue", "teal", "pink", "violet", "orange", "purple", "indigo", "yellow", "red"]
# for color in colors:
#     jimmy.color(color)
#     for _ in range(sides):
#         jimmy.forward(100)
#         jimmy.right(360/sides)
#     sides += 1

angles = [0, 90, 180, 270]

jimmy.width(1)
jimmy.speed("fastest")

# for _ in range(1000):
#     jimmy.setheading(choice(angles))
#     jimmy.color(random_color())
#     jimmy.forward(25)
def draw_spirograph(gap):
    for _ in range(round(360/gap)):
        jimmy.color(random_color())
        jimmy.circle(100)
        jimmy.seth(jimmy.heading() + gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()