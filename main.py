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
    "money": 0,
}

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

power_on = True
while power_on == True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "espresso":
        if MENU["espresso"]["ingredients"]["water"] > resources["water"]:
            print("Not enough water.")
            sufficient_resources = False
        elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Not enough coffee.")
            sufficient_resources = False
        else:
            sufficient_resources = True

    if user_choice == "latte":
         if MENU["latte"]["ingredients"]["water"] > resources["water"]:
            print("Not enough water.")
            sufficient_resources = False
         elif MENU["latte"]["ingredients"]["milk"] > resources["milk"]:
             print("Not enough milk.")
             sufficient_resources = False
         elif MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]:
             print("Not enough coffee.")
             sufficient_resources = False
         else:
             sufficient_resources = True

    if user_choice == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] > resources["water"]:
            print("Not enough water.")
            sufficient_resources = False
        elif MENU["cappuccino"]["ingredients"]["milk"] > resources["milk"]:
            print("Not enough milk.")
            sufficient_resources = False
        elif MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Not enough coffee.")
            sufficient_resources = False
        else:
            sufficient_resources = True

    if user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${resources['money']}")
        sufficient_resources = False

    if user_choice == "off":
        power_on = False

    if sufficient_resources == True:
        print("Please insert coins.")
        quarter_number = int(input("How many quarters?: ")) * quarters
        dime_number = int(input("How many dimes?: ")) * dimes
        nickle_number = int(input("How many nickles?: ")) * nickles
        penny_number = int(input("How many pennies?: ")) * pennies
        total = (quarter_number + dime_number) + (nickle_number + penny_number)
        if user_choice == "espresso":
            if total < 1.5:
                print("Sorry that's not enough money. Money refunded.")
                total = 0
            elif total > 1.5:
                print (f"Here is ${round(total - 1.5, 2)} in change.")
                print(f"Here is your {user_choice}. Enjoy!")
                resources["water"] = resources["water"] - 50
                resources["coffee"] = resources["coffee"] - 18
                resources["money"] += 1.5

            else:
                print(f"Here is your {user_choice}. Enjoy!")
                resources["water"] = resources["water"] - 50
                resources["coffee"] = resources["coffee"] - 18
                resources["money"] += 1.5

        if user_choice == "latte":
            if total < 2.5:
                print("Sorry that's not enough money. Money refunded.")
                total = 0
            elif total > 2.5:
                print(f"Here is ${round(total - 2.5, 2)} in change.")
                resources["water"] = resources["water"] - 200
                resources["milk"] = resources["milk"] - 150
                resources["coffee"] = resources["coffee"] - 24
                resources["money"] += 2.5
            else:
                print(f"Here is your {user_choice}. Enjoy!")
                resources["water"] = resources["water"] - 200
                resources["milk"] = resources["milk"] - 150
                resources["coffee"] = resources["coffee"] - 24
                resources["money"] += 2.5

        if user_choice == "cappuccino":
            if total < 3.0:
                print("Sorry that's not enough money. Money refunded.")
                total = 0
            elif total > 3.0:
                print(f"Here is ${round(total - 3.0, 2)} in change.")
                print(f"Here is your {user_choice}. Enjoy!")
                resources["water"] = resources["water"] - 250
                resources["milk"] = resources["milk"] - 100
                resources["coffee"] = resources["coffee"] - 24
                resources["money"] += 3.0
            else:
                print(f"Here is your {user_choice}. Enjoy!")
                resources["water"] = resources["water"] - 250
                resources["milk"] = resources["milk"] - 100
                resources["coffee"] = resources["coffee"] - 24
                resources["money"] += 3.0