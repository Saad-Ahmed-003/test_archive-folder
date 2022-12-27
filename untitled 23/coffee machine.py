resources = dict(milk=1000, water=1500, coffee=300)
amount = dict(espresso=1.5, latte=2.5, cappuccino=3.0)
coin = dict(Penney=0.01, Nickel=0.05, Dime=0.10, Quarter=0.25)
coins = []
your_coins = 0
is_on = True


def espresso():
    resources["water"] -= 50
    resources["coffee"] -= 18


def latte():
    resources["water"] -= 200
    resources["milk"] -= 150
    resources["coffee"] -= 24


def cappuccino():
    resources["water"] -= 250
    resources["milk"] -= 100
    resources["coffee"] -= 24


def coffee(name):
    if name.lower() == "espresso":
        espresso()
    elif name.lower() == "latte":
        latte()
    elif name.lower() == "cappuccino":
        cappuccino()


def check_amount(money, coffee_type):
    total_coins = 0
    for i in range(money[0]):
        total_coins += coin["Quarter"]
    for i in range(money[1]):
        total_coins += coin["Dimes"]
    for i in range(money[2]):
        total_coins += coin["Nickels"]
    for i in range(money[3]):
        total_coins += coin["Pennies"]
    if total_coins < amount[coffee_type]:
        print("Sorry that's not enough. Money refunded.")
    elif total_coins > amount[coffee_type]:
        amount[coffee_type] -= total_coins
        print(f"here is ${total_coins} in change.")


while is_on:
    question = input("  What would you like? (espresso/latte/cappuccino): ")
    print("Please insert coins.")
    coins.append(int(input("how manny quarters?: ")))
    coins.append(int(input("how manny dimes?: ")))
    coins.append(int(input("how manny nickels?: ")))
    coins.append(int(input("how manny pennies?: ")))
    check_amount(coins, question)
    coffee(question)
