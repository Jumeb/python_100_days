from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
menu = Menu()
coffer_maker = CoffeeMaker()

continue_service = True

while continue_service:
    options = menu.get_items()
    coffee_choice = input(f"What would you like? ({options}):").lower()
    if coffee_choice == 'report':
        coffer_maker.report()
        money_machine.report()
    elif coffee_choice == 'off':
        continue_service = False
    else:
       drink = menu.find_drink(coffee_choice)
       if coffer_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
               coffer_maker.make_coffee(drink)