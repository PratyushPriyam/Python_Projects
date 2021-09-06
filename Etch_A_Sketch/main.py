import turtle
my_turtle = turtle.Turtle()
screen = turtle.Screen()
my_turtle


def forward():
    my_turtle.forward(20)


def backward():
    my_turtle.backward(20)


def clockwise(ang=int):
    ang = 0
    ang += 20
    my_turtle.right(ang)


def anti_clockwise(ang2=int):
    ang2 = 0
    ang2 += 20
    my_turtle.left(ang2)


def hide():
    my_turtle.hideturtle()


def clear():
    screen.clear()


def reset():
    my_turtle.reset()


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=anti_clockwise)
screen.onkey(key="space", fun=hide)
screen.onkey(key="c", fun=clear)
screen.onkey(key="r", fun=reset)
screen.exitonclick()
