import os

from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def sclr():
    os.system("clear")


def check_resourses(drink):
    """takes input 'drink' then gets water, milk & coffee requirement of it then compares those with resources.\n
    returns False if not enough, True is enough"""
    if (
        resources["water"] >= MENU[f"{drink}"]["ingredients"].get("water", 0) and
        resources["milk"] >= MENU[f"{drink}"]["ingredients"].get("milk", 0) and
        resources["coffee"] >= MENU[f"{drink}"]["ingredients"].get("coffee", 0)
    ):
        return True
    else:
        return False


def process_coins(drink):
    """inputs drink calculates the cost of drink, processes coins, and calcs chang\n
    returns change as float"""
    cost = MENU[f"{drink}"]["cost"]
    sclr()
    print(logo)
    print(f"Great! ill get that right out. Your total is ${cost}.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    chg = (quarters * 0.25 + dimes * 0.10 +
           nickles * 0.05 + pennies * 0.01) - cost
    return round(chg, 2)


def chg_resourses(drink):
    """inputs drink order accesses relative price and ingredient data from MENU and changes resourses accordingly"""
    resources[f"money"] = MENU[f"{drink}"]["cost"] + resources.get("money", 0)
    resources["water"] = resources["water"] - \
        MENU[f"{drink}"]["ingredients"].get("water", 0)
    resources["milk"] = resources["milk"] - \
        MENU[f"{drink}"]["ingredients"].get("milk", 0)
    resources["coffee"] = resources["coffee"] - \
        MENU[f"{drink}"]["ingredients"].get("coffee", 0)


def menu():
    """main menu of coffee machine handles order processing, reporting and turning off"""
    is_on = True
    while is_on:
        sclr()
        print(logo)
        order = input(
            "What would you like? (espresso/latte/cappuccino):\n").lower()

        if order == "off":
            print(
                "I was pretty tired... Thank you. have a nice day! *winding down noices* zzzz...")
            is_on = False
            return

        if order == "report":
            # the teacher has the dict formated a little neater, im def not ganna do that
            # its just redundent work from previous lessons. instead just printing the list
            # tbh if a tech guy cant read the dict then get a new tech guy LOL
            print(resources)
            input("Press anything to continue...")
            continue
        # __EasterEgg__

        if order != "espresso" and order != "latte" and order != "cappuccino" and order != "report" and order != "off":
            input(
                "Wooooo wooo woo.... im just a simple coffee machine not some fancy cortana ai... try again.")
            continue

        if not check_resourses(order):
            # really dont need to code sep prints for each prints... not ganna do that.
            input("Sorry were outta that right now. press anything to continue\n")
            continue

        chg = process_coins(order)
        if chg < 0:
            sclr()
            print(logo)
            print("Sorry id love to help a brother out but im just a machine...")
            input(
                f"You were ${abs(chg)} short. Money refunded. Press anything to continue...")
            continue
        sclr()
        print(logo)
        print(f"Cool your change was ${chg}. Give me a second")
        chg_resourses(order)
        print("Brrrrtttt! *brewing noices*\n")
        print(f"Heres your yummy {order}. Enjoy!")
        input(f"Phew that order was exhausting.... Press anything to continue")

menu()
