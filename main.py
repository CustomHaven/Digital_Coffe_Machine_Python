from data import MENU, resources

# TODO: 2. Make a coin calculation function, return the price inserted by the user
def amount_paid():
    amount = 0
    print("Please insert coins!")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    quarters_sum = float(quarters * 0.25)
    dimes_sum = float(dimes * 0.1)
    nickles_sum = float(nickles * 0.05)
    pennies_sum = float(pennies * 0.01)
    amount += quarters_sum + dimes_sum + nickles_sum + pennies_sum
    return amount

# TODO: 3. Calculate the change function
def calculate_the_change(paid, drink_price):
    change = paid - drink_price
    return round(float(change), 2)

# TODO: 4. Create a function that compares the amount paid and the item price
def compare_paid_amount_and_item_price(paid, price, drink_type):
    change = None
    if price < paid:
        change = calculate_the_change(paid, price)
    elif price > paid:
        print("Sorry that is not enough money. Money refunded.")
        # TODO: 7. As they haven't paid the correct amount make a function to give the machine back its resources!
        return return_resources(drink_type)
    else:
        print("Thank you very much!")
        return paid
    if change is not None:
        print(f"Here is ${change} in change!")
    print(f"Here is your {user_choice} ☕. Enjoy!")
    return paid - price

# TODO: 5. Create a function that subtracts the total resources per purchase
def use_resources(drink_type):
    drink_resources_needed = [{a: b} for a,b in MENU[drink_type]["ingredients"].items()]

    temp_resources = {}
    for item in drink_resources_needed:

        for key, value in item.items():
            temp_resources[key] = resources[key] - value
            if temp_resources[key] < 0:
                return key
    
    resources["water"] = temp_resources["water"]
    resources["coffee"] = temp_resources["coffee"]
    if "milk" in temp_resources:
        resources["milk"] = temp_resources["milk"]


# TODO: 6. Create a function that returns simply "Sorry not enough <resource_type>"
def resource_missing(resource_type):
    print(f"Sorry there is not enough {resource_type}")
    
            
# TODO: 7 - continues return_resources
def return_resources(drink_type):
    drink_resources = [(a, b) for a,b in MENU[drink_type]["ingredients"].items()]

    for count in range(len(drink_resources)):
        ingredient = drink_resources[count][0]
        resources[ingredient] = resources[ingredient] + drink_resources[count][1]
 
# TODO: 8. function refil the machine.
def refil_machine():
    print("Welcome lets refil the machine.")
    print(f"""Currently we have: 
          water: {resources["water"]}
          milk: {resources["milk"]}
          coffee: {resources["coffee"]}
            """)
    resources["water"] += int(input("Add Water. "))
    resources["milk"] += int(input("Add Milk. "))
    resources["coffee"] += int(input("Add Coffee. "))

    print(f"""The new water, milk, and coffee level is: 
          water: {resources["water"]}
          milk: {resources["milk"]}
          coffee: {resources["coffee"]}
    """)

# TODO: 9. Function that gives the option to close the machine
def close_the_machine():
    print("Would you like to end the machine?")
    answer = input("yes or no?: ")
    return answer




# TODO: 1. Start the coffe machine question
is_on = True
count = 0
money = 0
while is_on:
    user_choice = input(" What would you like? (espresso, latte, cappuccino): ").lower()

    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        check_resource = None
        check_resource = use_resources(user_choice)
        if check_resource is not None:
            resource_missing(check_resource)
        else:
            user_paid = amount_paid()
            item_price = float(MENU[user_choice]["cost"])
            money_made = compare_paid_amount_and_item_price(user_paid, item_price, user_choice)
            if isinstance(money_made, float) or isinstance(money_made, int):
                money =+ money_made
            answer = close_the_machine()
            if answer == "yes":
                is_on = False
    elif user_choice == "employer" or user_choice == "employee":
        # TODO: 8. Employee to refil the machine
        refil_machine()
        answer = close_the_machine()
        if answer == "yes" and user_choice == "employer":
            is_on = False
            print(f"Currently the machine has ${money}")
    else:
        count += 1
        if count == 5:
            print("Too many incorrect selections!")
            print("Bye bye.")
            is_on = False
        else:
            print("Try again!")
            print()

