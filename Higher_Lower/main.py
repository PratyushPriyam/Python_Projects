from art import logo, vs
from game_data import data
import random

print(logo)
score = 0
random_numberB = random.randint(0, len(data)-1)

game = True
while game:
    print(f"Your current score : {score}")
    random_numberA = random_numberB
    random_numberB = random.randint(0, len(data)-1)
    if random_numberA == random_numberB:
        random_numberA += 1

    followers_A = data[random_numberA]['follower_count']
    print(followers_A)
    print(f"Compare A : {data[random_numberA]['name']},"
          f" a {data[random_numberA]['description']}, from {data[random_numberA]['country']}")

    print(vs)

    followers_B = data[random_numberB]['follower_count']
    print(followers_B)
    print(f"Compare B : {data[random_numberB]['name']},"
          f" a {data[random_numberB]['description']}, from {data[random_numberB]['country']}")

    answer = input("Who has more followers ? Type A or B :🧐🧐 ")
    if (followers_A > followers_B) and ("A" in answer):
        score += 1
        print("------------------------------------------------------------------------------------------")
    elif (followers_B > followers_A) and ("B" in answer):
        score += 1
        print("------------------------------------------------------------------------------------------")
    else:
        game = False
        print(f"Wrong Choice. Your Final score : {score}")
