MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

resources['Money'] = 0.0
turn_off_machine = False

# TODO: 1. Print report of all coffee machine resources
def print_report():
    for item, value in resources.items():
        print(f"{item}: {value}")

# TODO: 2. Prompt user by asking what they would like? (espresso/ latte/ cappuccino)

def coffee_machine(coffee_selected):

    total_paid = process_coins(coffee_selected)
    coffee_cost = MENU[coffee_selected]['cost']
    payment_successful = check_transaction(coffee_cost, total_paid)
    if payment_successful == True:
        make_coffee(coffee_selected)

# TODO: 3. Check if resources are sufficient?

def check_resources_sufficient(coffee_selected):
    coffee_ingredients = MENU[coffee_selected]['ingredients']
    for item in coffee_ingredients:
        if resources[item] > MENU[coffee_selected]['ingredients'][item]:
            return True
        else:
            print(f"Sorry there is not enough {item}")
            return False
    return False


# TODO: 4. Process coins

def process_coins(coffee_selected):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    total_money = quarters + dimes + nickels + pennies
    return total_money

# TODO: 5. Check transaction successful?

def check_transaction(coffee_cost, total_money):
    change = 0.0
    if coffee_cost > total_money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total_money > coffee_cost:
        change = total_money - coffee_cost
        print(f"Here is ${round(change,2)} in change.")
        return True
    else:
        # resources['Money'] = coffee_cost
        return False


# TODO: 6. Make coffee

def make_coffee(coffee_selected):
    coffee_ingredients = MENU[coffee_selected]['ingredients']
    for coffee in MENU:
        if coffee == coffee_selected:
            # if check_resources_sufficient(coffee_selected) == True:
            for item in coffee_ingredients:
                resources[item] -= MENU[coffee_selected]['ingredients'][item]
            resources['Money'] += MENU[coffee_selected]['cost']
            # resources['water'] -= MENU[coffee_selected]['ingredients']['water']
            print(f"Here is your {coffee_selected} ☕️. Enjoy!")

    # print(f"Here is your {coffee_selected} ☕️. Enjoy!")


# TODO: 7. Turn off the coffee machine by entering "Off" to the prompt

while not turn_off_machine:
    coffee_selected = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_selected == 'off':
        print("Bye Bye!")
        turn_off_machine = True
    elif coffee_selected == 'report':
        print_report()
    else:
        if check_resources_sufficient(coffee_selected) == True:
            coffee_machine(coffee_selected)
