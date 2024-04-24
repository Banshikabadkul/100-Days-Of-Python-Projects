# coffee--machine making
# 1. makes 3 hot flavors(espressso, cappuccino, latte) require(water,milk,coffee)
# 2. coin operated (penny,nickel,dime,quarter)
# program requiremenst---
# 1. print report
# 2.check resources sufficeint
# 3.process coins
# 4. check transaction successfull?
# 5.make coffee and deduct resources

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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO : 01 report of coffee
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def is_resources_sufficient(drink_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coin():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: "))
    total += int(input("how many dimes?: "))
    total += int(input("how many nickles?:"))
    total += int(input("how many pennies?: "))
    return total


def is_transaction_successfull(amnt_paid, drink_cost):
    if drink_cost <= amnt_paid:
        change = round(amnt_paid-drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for key in order_ingredients:
        resources[key] -= order_ingredients[key]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        is_on = False
    elif order == "report":
        report()
    else:
        drink = MENU[order]
        print(drink)
        if is_resources_sufficient(drink['ingredients']):
            print("Enough resources")
            payment = process_coin()
            if is_transaction_successfull(payment,drink['cost']):
                make_coffee(order, drink['ingredients'])

