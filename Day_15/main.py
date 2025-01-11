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


def show_report(money):
    for resource in resources:
        print(f"{resource}: {resources[resource]}")
    if money > 0:
        print(f'Money: ${money}')


def check_resources(available_resources, ingredients):
    depleted_resources = []
    for ingredient in ingredients:
        if available_resources[ingredient] <= ingredients[ingredient]:
            depleted_resources.append(ingredient)
    return depleted_resources

def make_drink(available_resources, ingredients):
    for ingredient in ingredients:
        available_resources[ingredient] -= ingredients[ingredient]

def calculate_total_amount(quarters, dimes, nickles, pennies):
    total = 0
    total += round(round(0.25 * quarters, 2) + round(0.10 * dimes, 2) + round(0.10 * nickles, 2) + round(0.10 * pennies, 2), 2)
    return total

def calculate_transaction(price_of_item, amount_inserted):
    return round(amount_inserted - price_of_item, 2)


continue_service = True
profit = 0

while continue_service:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if coffee_choice == 'report':
        show_report(profit)
    elif coffee_choice == 'off':
        continue_service = False
    elif coffee_choice == 'espresso' or coffee_choice == 'latte' or coffee_choice == 'cappuccino':
        choice = MENU[coffee_choice]['ingredients']
        if len(check_resources(resources, choice)) == 0:
            quarters = float(input("How many quarters: "))
            dimes = float(input("How many dimes: "))
            nickles = float(input("How many nickles: "))
            pennies = float(input("How many pennies: "))
            total_amount = calculate_total_amount(quarters, dimes, nickles, pennies)
            balance = calculate_transaction(MENU[coffee_choice]['cost'], total_amount)
            if balance >= 0:
                profit += MENU[coffee_choice]['cost']
                make_drink(resources, choice)
                if balance > 0:
                    print(f"Here is ${balance} dollars in change")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f'Sorry, there is not enough {", ".join(check_resources(resources, choice))}')
    else:
        print(f'Sorry, we do not offer {coffee_choice} here.')
    