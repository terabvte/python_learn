from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def calculate_coins(coins):
    return float(coins[0] * 0.25 + coins[1] * 0.10 + coins[2] * 0.05 + coins[3] * 0.01)


menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
coins = []
coin_inserted = 0
decision = ""
while not decision == "stop":
    decision = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    if decision == "off":
        exit()
    if decision == "report":
        print(coffee.report())

    if decision == "espresso" or decision == "latte" or decision == "cappuccino":
        print(
            f"You've chosen {decision.title()}... Checking if ingredients are present..."
        )
        if coffee.is_resource_sufficient(menu.find_drink(decision)):
            print("There's enough!")

            # for i in range(1, 5):
            #     if i == 1:
            #         coin_inserted = float(input("Please insert your quarters ($0.25) "))
            #     if i == 2:
            #         coin_inserted = float(input("Please insert your dimes ($0.10) "))
            #     if i == 3:
            #         coin_inserted = float(input("Please insert your nickels ($0.05) "))
            #     if i == 4:
            #         coin_inserted = float(input("Please insert your pennies ($0.01) "))

            #     coins.append(coin_inserted)
            # print(coins)
            # payment = calculate_coins(coins)
            # print(f"You've made a payment of ${payment:.2f}")
            print(f"The cost is {menu.find_drink(decision).cost:.2f}")
            money.make_payment(menu.find_drink(decision).cost)
            print(f"Here is your {decision.title()}")
            print(coffee.report())

        elif not coffee.is_resource_sufficient(f"{decision}"):
            print("Sorry there aren't enough ingredients...")


# print(menu.find_drink("latte").ingredients)
# print(menu.find_drink("cappuccino").ingredients)
# print(menu.find_drink("espresso").ingredients)
