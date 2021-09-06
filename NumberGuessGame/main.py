import random
from art import logo


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(0, 100)
    print(random_number)
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if "easy" in difficulty_level:
        choices_left_reverse = 0
        totallives = 10
        while choices_left_reverse < totallives:
            if choices_left_reverse == 10:
                print("You have run out of lives. Better luck next time")
                choices_left_reverse = 10
            print(f"You have {10-choices_left_reverse} attempts remaining to guess the number.")
            user_input = int(input("Make a guess : "))
            if user_input < random_number:
                print("Too Low")
            elif user_input > random_number:
                print("Too High")
            elif user_input == random_number:
                print("Bravo! Correct Choice")
                choices_left_reverse = 10
                totallives = 10
            else:
                print("Your Lives are Over...Better Luck Next Time")
                print(f"Correct choice{random_number}")
                choices_left_reverse = 10
            choices_left_reverse += 1

    if "hard" in difficulty_level:
        choices_left_reverse = 0
        total_lives = 5
        while choices_left_reverse < total_lives:
            print(f"You have {5-choices_left_reverse} attempts remaining to guess the number.")
            user_input = int(input("Make a guess : "))
            if user_input < random_number:
                print("Too Low")
            elif user_input > random_number:
                print("Too High")
            elif user_input == random_number:
                print("Bravo! Correct Choice")
                choices_left_reverse = 5
            else:
                print("Your Lives are Over...Better Luck Next Time")
                print(f"Correct choice{random_number}")
                choices_left_reverse = 5
            choices_left_reverse += 1


go_again = True
while go_again:
    again_choice = input("Wanna PLAY ? 'yes' to play, 'no' to quit : ")
    if "yes" in again_choice:
        game()
    else:
        print("Good Bye!")
        go_again = False
