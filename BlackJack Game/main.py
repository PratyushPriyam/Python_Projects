import random
from art import logo
from replit import clear


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def play_game():
    user_cards = []
    computer_cards = []
    playing = True

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(user_score, computer_score):
        if computer_score == user_score:
            return "Game Draw!"
        elif computer_score == 0:
            return "Computer wins with a BlackJack!!"
        elif user_score == 0:
            return "You win with a BlackJack!!!"
        elif user_score > 21:
            return "You went over 21. You Loose!!"
        elif computer_score > 21:
            return "Computer went over 21. You Win!!!"
        elif computer_score > user_score:
            return "Computer Wins!!"
        else:
            return "You Win!!!"

    while playing:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are : {user_cards} and your score is : {user_score}")
        print(f"Computer's one card is : {computer_cards[0]} ")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            playing = False
        else:
            more_cards = input("Do you want to pick another card? 'y' for YES and 'n' for NO : ")
            if more_cards == "y":
                user_cards.append(deal_card())
            else:
                playing = False
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"User's final hand : {user_cards} and final score : {user_score}")
    print(f"Computer's final hand : {computer_cards} and final score : {computer_score}")
    game_decision = compare(user_score, computer_score)
    print(game_decision)


while input("Do you want to play the BlackJack game? 'y' for YES and 'n' for NO : ") == "y":
    print(logo)
    play_game()
    clear()
