import turtle
import random

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Give your bet", "Which turtle would you bet on? ")
print(user_bet)
all_turtles = []
ang = 120
n_color = 0
game_is_on = False
while ang > -160:
    race_turtle = turtle.Turtle("turtle")
    race_turtle.penup()
    race_turtle.color(colors[n_color])
    race_turtle.goto(-230, ang)
    ang -= 40
    n_color += 1
    all_turtles.append(race_turtle)


if user_bet:
    game_is_on = True
    while game_is_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                game_is_on = False
                turtle_color = turtle.pencolor()
                if turtle_color == user_bet:
                    print(f"Yay! You have won. WINNER : {turtle_color}")
                else:
                    print(f"Oops! You have lost. WINNER : {turtle_color}")
            rand_distance = random.randint(1, 10)
            turtle.forward(rand_distance)


screen.exitonclick()
