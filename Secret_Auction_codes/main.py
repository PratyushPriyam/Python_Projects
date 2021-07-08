from replit import clear
from art import logo
import os
print(logo)
print("Welcome to BLIND AUCTION PROGRAM")
bid_dictionary = {}


def bid_result():
    highest_bid = 0
    for bidder in bid_dictionary:
        bid_amount = int(bid_dictionary[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The highest bidder is {winner.upper()} with a bid of {highest_bid}")


start = input("Type 'Start' to start ").lower()
if "start" in start:
    contd = True
    while contd:
        name = input("Enter bidder's name : ")
        bid = input("Enter the bid amount : ")
        bid_dictionary[name.title()] = bid
        any_more_bidders = input("Are there any more bidders? yes/no: ")
        clear()
        if "yes" in any_more_bidders:
            clear()
            contd = True
        else:
            bid_result()
            contd = False
