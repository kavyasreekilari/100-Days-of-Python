from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

# turnOff = False
# def coffee_machine(coffee_selected):
#     for item in Menu.get_items():
#         if Menu.find_drink(coffee_selected):
#             if CoffeeMaker.is_resource_sufficient(coffee_selected) == True:
#                 money_entered = MoneyMachine.process_coins()
#                 if Menu(coffee_selected).menu["cost"]
#
#
#
#
#
# while not turnOff:
#     coffee_selected = input("What would you like? (espresso/latte/cappuccino/): ")
#     if coffee_selected == "report":
#         CoffeeMaker.report()
#     elif coffee_selected == "off":
#         turnOff = True
#     else:
#         coffee_machine(coffee_selected)


