import turtle

turtle.speed(4)


def move(a):
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a // 2)
    turtle.left(90)


def rectangle(a):
    for i in range(2):
        move(a)


def rectangle_color(a, color):
    turtle.color(color)
    turtle.begin_fill()
    rectangle(a)
    turtle.end_fill()


rectangle_color(300, 'blue')
turtle.goto(-200, 200)
rectangle_color(300, 'yellow')
