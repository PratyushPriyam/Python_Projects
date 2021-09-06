from Utilities import MENU, resources
from art import logo

print(logo)

shop_open_and_ingredients_available = True

pay = 0
Water = resources["water"]
Milk = resources["milk"]
Coffee = resources["coffee"]
espresso_water = MENU["espresso"]["ingredients"]["water"]
espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
latte_water = MENU["latte"]["ingredients"]["water"]
latte_coffee = MENU["latte"]["ingredients"]["coffee"]
latte_milk = MENU["latte"]["ingredients"]["milk"]
cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]


def report():
    print(f"Water left : {Water}")
    print(f"Milk left : {Milk}")
    print(f"Coffee left : {Coffee}")
    print(f"Total money collected: {pay}")

# Shut Down Machine when OFF is called


def make_coffee():
    global Water, Coffee, Milk, shop_open_and_ingredients_available, pay
    choice = input("What would you like to have? (espresso Rs.25/latte Rs.35/cappuccino Rs.50): ")
    if "report" in choice:
        report()

    elif "off" in choice:
        shop_open_and_ingredients_available = False
        print("SYSTEM IS CLOSED FOR REPAIR.")

    elif "espresso" in choice:
        money = int(input("Enter the money for the drink of your choice"))
        if money < MENU['espresso']['cost']:
            print(f"Money insufficient. Here's your refund of RS.{money}")
        elif Water >= espresso_water and Coffee >= espresso_coffee:
            print("Here is your Espresso. Thank You!")
            print(f"Here's your change of RS.{money - MENU['espresso']['cost']}")
            Water -= espresso_water
            Coffee -= espresso_coffee
            pay += 25
        elif Water < espresso_water and espresso_coffee:
            print("Sorry, Water is over")
        elif Water > espresso_water and espresso_coffee:
            print("Sorry, Coffee is over")
        elif Water < espresso_water and espresso_coffee:
            print("Water and Coffee are over")
        elif Water < espresso_water:
            print("Sorry, Water Shortage")
        elif Coffee < espresso_coffee:
            print("Sorry, Coffee Shortage")
        else:
            print("Sorry, We are currently facing some technical issues")

    elif "latte" in choice:
        money = int(input("Enter the money for the drink of your choice"))
        if money < MENU['latte']['cost']:
            print(f"Money insufficient. Here's your refund of RS.{money}")
        if Water >= latte_water and Coffee >= latte_coffee and Milk >= latte_milk:
            print("Here is your Latte. Thank You!")
            print(f"Here's your change of RS.{money - MENU['latte']['cost']}")
            Water -= latte_water
            Coffee -= latte_coffee
            Milk -= latte_milk
            pay += 35
        elif Water < latte_water and Coffee > latte_coffee and Milk > latte_milk:
            print("Sorry, Water is over")
        elif Water > latte_water and Coffee < latte_coffee and Milk > latte_milk:
            print("Sorry, Coffee is over")
        elif Water > latte_water and Coffee > latte_coffee and Milk < latte_milk:
            print("Sorry, Milk is over")
        elif Water < latte_water and Coffee < latte_coffee and Milk < latte_milk:
            print("Water, Coffee and Milk are over")
        elif Water < latte_water:
            print("Sorry, Water Shortage")
        elif Coffee < latte_coffee:
            print("Sorry, Coffee Shortage")
        elif Milk < latte_milk:
            print("Sorry, Milk shortage")
        else:
            print("Sorry, We are currently facing some technical issues")

    elif "cappuccino" in choice:
        money = int(input("Enter the money for the drink of your choice"))
        if money < MENU['cappuccino']['cost']:
            print(f"Money insufficient. Here's your refund of RS.{money}")
        if Water >= cappuccino_water and Coffee >= cappuccino_coffee and Milk >= cappuccino_milk:
            print("Here is your cappuccino. Thank You!")
            print(f"Here's your change of RS.{money - MENU['cappuccino']['cost']}")
            Water -= cappuccino_water
            Coffee -= cappuccino_coffee
            Milk -= cappuccino_milk
            pay += 50
        elif Water < cappuccino_water and Coffee > cappuccino_coffee and Milk > cappuccino_milk:
            print("Sorry, Water is over")
        elif Water > cappuccino_water and Coffee < cappuccino_coffee and Milk > cappuccino_milk:
            print("Sorry, Coffee is over")
        elif Water > cappuccino_water and Coffee > cappuccino_coffee and Milk < cappuccino_milk:
            print("Sorry, Milk is over")
        elif Water < cappuccino_water and Coffee < cappuccino_coffee and Milk < cappuccino_milk:
            print("Water, Coffee and Milk are over")
        elif Water < cappuccino_water:
            print("Sorry, Water Shortage")
        elif Coffee < cappuccino_coffee:
            print("Sorry, Coffee Shortage")
        elif Milk < cappuccino_milk:
            print("Sorry, Milk shortage")
        else:
            print("Sorry, We are currently facing some technical issues")


while shop_open_and_ingredients_available:
    make_coffee()
