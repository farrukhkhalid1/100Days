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
cost = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def enough_resources(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total +=int(input("How many dimes?: ")) * 0.1
    total +=int(input("How many nickles?: ")) * 0.05
    total +=int(input("How many pennies?: ")) * 0.01
    return total

def is_payment_successful(money_recieved,drink_cost):

    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost,2)
        print(f"here is your ${change} Change back.")
        global cost
        cost += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}.")

machine_on = True

while machine_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {cost}$")
    elif choice not in ("espresso", "latte", "cappuccino"):
        print("Invalid Input")
    else:
        drink = MENU[choice]
        if enough_resources(drink["ingredients"]):
            payment = process_coins()
            if is_payment_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])

