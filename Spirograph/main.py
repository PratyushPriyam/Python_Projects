from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)
screen = Screen()
my_turtle = Turtle()
my_turtle.color("navy")
my_turtle.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


def spirograph(angle):
    for _ in range(int(360 / angle)):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        turtle_heading = my_turtle.heading()
        my_turtle.setheading(turtle_heading + angle)


spirograph(10)
screen.exitonclick()
