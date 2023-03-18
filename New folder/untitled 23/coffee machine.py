resources = dict(milk=250, water=250, coffee=24)
amount = dict(espresso=1.5, latte=2.5, cappuccino=3.0)
coin = dict(Penney=0.01, Nickel=0.05, Dime=0.10, Quarter=0.25)
latte_1 = dict(water=200, milk=150, coffee=24)
espresso_1 = dict(water=50, coffee=18)
cappuccino_1 = dict(water=250, milk=100, coffee=24)
coins = []
your_coins = 0
brake_point = 0
is_on = True


def espresso():
    resources["water"] -= 50
    resources["coffee"] -= 18
    print(f"storage: {resources}")


def latte():
    resources["water"] -= 200
    resources["milk"] -= 150
    resources["coffee"] -= 24
    print(f"storage: {resources}")


def cappuccino():
    resources["water"] -= 250
    resources["milk"] -= 100
    resources["coffee"] -= 24
    print(f"storage: {resources}")


def coffee(name):
    if name.lower() == "espresso":
        espresso()
    elif name.lower() == "latte":
        latte()
    elif name.lower() == "cappuccino":
        cappuccino()


def check_resources(f_name):
    if f_name == "latte":
        f_name = latte_1
        for i in f_name:
            if f_name[i] < resources[i]:
                print(f"sorry there is not enough {i}.")


def check_amount(money, coffee_type):
    total_coins = 0
    for i in range(money[0]):
        total_coins += coin["Quarter"]
    for i in range(money[1]):
        total_coins += coin["Dime"]
    for i in range(money[2]):
        total_coins += coin["Nickel"]
    for i in range(money[3]):
        total_coins += coin["Penney"]
    if total_coins < amount[coffee_type]:
        print("Sorry that's not enough. Money refunded.")
    elif total_coins > amount[coffee_type]:
        amount[coffee_type] -= total_coins
        print(f"here is ${total_coins} in change.")


print(f"storage: {resources}")

while is_on:
    question = input("  What would you like? (espresso/latte/cappuccino): ")
    if question == "latte":
        print(f'  water : {latte_1["water"]}')
        print(f'  milk : {latte_1["milk"]}')
        print(f'  coffee : {latte_1["coffee"]}')
        print(f'  price : ${amount[question]}')
    elif question == "espresso":
        print(f'  water : {espresso_1["water"]}')
        print(f'  coffee : {espresso_1["coffee"]}')
        print(f'  price : ${amount[question]}')
    elif question == "cappuccino":
        print(f'  water : {cappuccino_1["water"]}')
        print(f'  milk : {cappuccino_1["milk"]}')
        print(f'  coffee : {cappuccino_1["coffee"]}')
        print(f'  price : ${amount[question]}')
    else:
        break
    print("Please insert coins.")
    coins.append(int(input("how manny quarters?: ")))
    coins.append(int(input("how manny dimes?: ")))
    coins.append(int(input("how manny nickels?: ")))
    coins.append(int(input("how manny pennies?: ")))
    check_amount(coins, question)
    coffee(question)
