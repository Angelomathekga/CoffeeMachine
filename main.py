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

def check_resources(selection) :
    ingredients = MENU[selection]["ingredients"]
    for i in ingredients:
        if ingredients[i]  resources[i]:
            print(f"Sorry there is not enough {i}")





turn_off = False
while not turn_off:
    choose_drink = input("“What would you like? (espresso/latte/cappuccino):\n").lower()
    if choose_drink in MENU :
        check_resources(choose_drink)

    elif  choose_drink == "off" :
        turn_off = True
    
    elif choose_drink == "report":
        print(resources)
