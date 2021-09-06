import turtle
import random
#import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst_painting.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(29, 106, 164), (227, 158, 66),
              (231, 214, 93), (188, 42, 84), (219, 139, 173), (139, 105, 59), (114, 185, 211), (216, 73, 99),
              (200, 167, 33), (159, 24, 65), (113, 191, 156), (24, 54, 129), (16, 182, 152), (105, 108, 192),
              (141, 208, 227), (236, 89, 50), (20, 139, 89), (230, 164, 185), (20, 167, 207), (99, 49, 38),
              (81, 42, 30), (24, 43, 79), (23, 90, 85), (239, 213, 6), (153, 214, 199), (26, 84, 90)]


i = 50
turtle.colormode(255)
my_turtle = turtle.Turtle()
my_turtle.hideturtle()
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.goto(-200, -200)
for _ in range(10):
    for dots in range(10):
        my_turtle.dot(20, random.choice(color_list))
        my_turtle.penup()
        my_turtle.forward(50)
        my_turtle.pendown()
        my_turtle.penup()
    x_pos = -200+i
    my_turtle.goto(-200, x_pos)
    my_turtle.pendown()
    i += 50
screen = turtle.Screen()
screen.exitonclick()
