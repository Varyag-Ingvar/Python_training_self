# def even(a):
#     if a%2==0:
#         print(a, "chetnoe")
#     else:
#         print(b,"nechetnoe")
# even(int(input("Enter a number: ")))

import turtle

# def draw_square():
#     turtle.forward(100)
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.left(90)
#
# turtle.speed(1)

# draw_square()
# turtle.goto(150,150)
# draw_square()
# turtle.goto(-150,-150)
# draw_square()


def move(a):
    turtle.forward(a)
    turtle.left(90)


def draw_square(a):
    for i in range(4):
        move(a)


def draw_square_color(a, color):
    turtle.color(color)
    turtle.begin_fill()
    draw_square(a)
    turtle.end_fill()
turtle.speed(2)

draw_square_color(50, 'red')
turtle.goto(100, 100)
draw_square_color(100, 'blue')
